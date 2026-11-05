// Rendert html/*.html nach png/*.png (1080x1350, Faktor 2)
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const dir = path.join(__dirname, 'html');
  const out = path.join(__dirname, 'png');
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
  for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.html')).sort()) {
    await page.goto('file://' + path.join(dir, f));
    // Prüfen, dass der Text nicht in die Figur läuft
    const gap = await page.evaluate(() => {
      const t = document.querySelector('.text').getBoundingClientRect();
      const s = document.querySelector('.fig svg').getBoundingClientRect();
      return s.top - t.bottom;
    });
    console.log(f, 'gap text→figure:', Math.round(gap), 'px');
    await page.screenshot({ path: path.join(out, f.replace('.html', '.png')) });
  }
  await browser.close();
})();
