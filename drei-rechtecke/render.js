// Rendert die Rätselkarte "Drei Rechtecke mit gleicher Fläche" (DE + EN) als PNG.
// Rechnung (wahre Maße): Spalten a=5, b=4, c=6; Zeilen unten h1=12, Mitte h2=8, oben h3=16.
// Felder: a*h3=80, b*h2=32, c*h1=72, grün a*h1=60; alle drei Rechtecke 180 cm².
// Die Skizze ist absichtlich NICHT maßstäblich, damit man das grüne Feld nicht abmessen kann.
const { chromium } = require('playwright');
const path = require('path');

// Skizzenmaße in px (schematisch, gleiche Lage/Topologie wie die Rechnung)
const A = 210, B = 170, C = 210;   // Spaltenbreiten
const H1 = 170, H2 = 120, H3 = 190; // Zeilenhöhen (unten, Mitte, oben)

const COL = {
  ink: '#1f2a37', line: '#3b4654', faint: '#8f877b', bg: '#fbf9f4', cell: '#ffffff',
  green: '#a5d6b8', blue: '#b7d1ec', blueE: '#3a6ea5', purple: '#d9c4ea', purpleE: '#6f4a94',
  orange: '#efc584', orangeE: '#b0662a', accent: '#2f6f7e',
};

// Felder relativ zur linken unteren Ecke (x nach rechts, y nach oben)
const cells = [
  { x: 0,     y: H1 + H2, w: A, h: H3, label: '80' },
  { x: 0,     y: H1,      w: A, h: H2, label: '' },
  { x: A,     y: H1,      w: B, h: H2, label: '32' },
  { x: 0,     y: 0,       w: A, h: H1, label: '?', green: true },
  { x: A,     y: 0,       w: B, h: H1, label: '' },
  { x: A + B, y: 0,       w: C, h: H1, label: '72' },
];
const rects = [
  { w: A,         h: H1 + H2 + H3, fill: COL.blue,   edge: COL.blueE },
  { w: A + B,     h: H1 + H2,      fill: COL.purple, edge: COL.purpleE },
  { w: A + B + C, h: H1,           fill: COL.orange, edge: COL.orangeE },
];
const TOT_W = A + B + C, TOT_H = H1 + H2 + H3;

function mainFigure(ox, oy, S) { // oy = y der Unterkante, S = Maßstab
  let s = '';
  for (const c of cells) {
    const x = ox + c.x * S, y = oy - (c.y + c.h) * S, w = c.w * S, h = c.h * S;
    s += `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${c.green ? COL.green : COL.cell}" stroke="${COL.line}" stroke-width="4" stroke-linejoin="round"/>`;
    if (c.label) s += `<text x="${x + w / 2}" y="${y + h / 2}" font-size="${c.label === '?' ? 64 : 50}" font-weight="700" fill="${COL.ink}" text-anchor="middle" dominant-baseline="central">${c.label}</text>`;
  }
  return s;
}

function mini(ox, oy, k, r) { // oy = Unterkante, k = Maßstab
  // erst die Farbfläche, dann alle Feldlinien darüber, zuletzt der farbige Rand
  let s = `<rect x="${ox}" y="${oy - r.h * k}" width="${r.w * k}" height="${r.h * k}" fill="${r.fill}"/>`;
  for (const c of cells) {
    s += `<rect x="${ox + c.x * k}" y="${oy - (c.y + c.h) * k}" width="${c.w * k}" height="${c.h * k}" fill="none" stroke="${COL.faint}" stroke-width="2.5"/>`;
  }
  s += `<rect x="${ox}" y="${oy - r.h * k}" width="${r.w * k}" height="${r.h * k}" fill="none" stroke="${r.edge}" stroke-width="5" stroke-linejoin="round"/>`;
  return s;
}

const TEXT = {
  de: {
    title: 'Drei Rechtecke mit gleicher Fläche',
    body: ['Links siehst du drei Rechtecke. Sie überlappen sich teilweise.',
           'Rechts siehst du dieselbe Figur noch dreimal, kleiner.',
           'In jedem Bild ist eines der Rechtecke farbig.',
           'Alle drei Rechtecke haben dieselbe Fläche.',
           'Die Zahlen sind die Flächen der einzelnen Felder in cm².',
           'Bei Feldern ohne Zahl ist die Fläche nicht bekannt.'],
    q: 'Wie groß ist das grüne Feld in cm²?',
    foot: 'Skizzen nicht maßstabsgetreu',
    level: 'Schwierigkeit: mittel',
  },
  en: {
    title: 'Three Rectangles of Equal Area',
    body: ['On the left are three rectangles. They partly overlap.',
           'On the right, the same shape is shown three more times, smaller.',
           'In each picture, one of the rectangles is coloured.',
           'All three rectangles have the same area.',
           'The numbers are the areas of the individual boxes in cm².',
           'The areas of the boxes without a number are not given.'],
    q: 'What is the area of the green box in cm²?',
    foot: 'Not drawn to scale',
    level: 'Difficulty: medium',
  },
};

function card(lang) {
  const t = TEXT[lang];
  const W = 1600, H = 1170, P = 80;
  let s = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" font-family="Inter, 'DejaVu Sans', sans-serif">`;
  s += `<rect width="${W}" height="${H}" fill="${COL.bg}"/>`;
  s += `<text x="${P}" y="118" font-size="62" font-weight="800" fill="${COL.ink}">${t.title}</text>`;
  s += `<text x="${W - P}" y="112" font-size="26" font-weight="600" fill="${COL.accent}" text-anchor="end">${t.level}</text>`;
  t.body.forEach((line, i) => {
    s += `<text x="${P}" y="${196 + i * 46}" font-size="34" fill="${COL.ink}">${line}</text>`;
  });
  s += `<text x="${P}" y="${196 + t.body.length * 46 + 30}" font-size="38" font-weight="700" fill="${COL.accent}">${t.q}</text>`;

  // Hauptfigur links
  const figBottom = 1060, figLeft = P + 20;
  s += mainFigure(figLeft, figBottom, 0.9);

  // Drei Einzelrechtecke rechts, mit Gleichheitszeichen
  const k = 0.38, mw = TOT_W * k, mh = TOT_H * k, gap = 76;
  const rowW = 3 * mw + 2 * gap;
  const rx0 = W - P - rowW;
  const ry = figBottom - (TOT_H * 0.9 - mh) / 2; // vertikal mittig zur Hauptfigur
  rects.forEach((r, i) => {
    const x = rx0 + i * (mw + gap);
    s += mini(x, ry, k, r);
    if (i < 2) s += `<text x="${x + mw + gap / 2}" y="${ry - mh / 2}" font-size="64" font-weight="700" fill="${COL.ink}" text-anchor="middle" dominant-baseline="central">=</text>`;
  });

  s += `<text x="${W - P}" y="${H - 50}" font-size="24" fill="#4b5563" text-anchor="end">${t.foot}</text>`;
  s += `</svg>`;
  return s;
}

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1600, height: 1170 }, deviceScaleFactor: 2 });
  for (const lang of ['de', 'en']) {
    await page.setContent(`<html><body style="margin:0">${card(lang)}</body></html>`);
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(__dirname, `drei-rechtecke-${lang}.png`), clip: { x: 0, y: 0, width: 1600, height: 1170 } });
  }
  await browser.close();
})();
