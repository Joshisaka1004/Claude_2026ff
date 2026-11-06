"""Zeichen-Baukasten für klassische Georätsel-Karten (1100 x 1100 px).

Benutzung (Kurzform):

    import sys; sys.path.insert(0, "<skill>/scripts")
    from karte import *

    k = Karte(titel=[("Grün", GRUEN_TXT), (" = ?", TINTE)],
              zeile="Die Zahlen sind Flächen.",      # optional, eine kurze Zeile
              stichwort="Quadrat",                   # optional, kursiv unter der Figur
              datum="06.11.2026", nr=13, sprache="de")
    ax = k.ax                                         # Datenkoordinaten, y nach oben
    flaeche(ax, [(0,0),(4,0),(4,4)], GRUEN)
    linie(ax, (0,0), (4,4))
    zahl(ax, (2.7,1.3), "?", farbe=GRUEN_TXT)
    k.speichern("karte-13-de.png")

Alle Punkte kommen aus der Rechnung – hier wird nur gezeichnet.
"""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Arc, Circle, Polygon, PathPatch
from matplotlib.path import Path as MPath
import matplotlib.patheffects as pe
import numpy as np

# ---------------------------------------------------------------- Schrift
_INTER = Path("/usr/share/fonts/opentype/inter")
for _n in ("Inter-Regular", "Inter-Bold", "Inter-Italic", "Inter-SemiBold", "Inter-BoldItalic"):
    _p = _INTER / f"{_n}.otf"
    if _p.exists():
        font_manager.fontManager.addfont(str(_p))
plt.rcParams["font.family"] = "Inter"
plt.rcParams["hatch.linewidth"] = 2.4   # kräftige, gut sichtbare Schraffur

# ---------------------------------------------------------------- Farben (Stil „bunt“)
TINTE = "#1D2330"        # Konturen, Zahlen
GRAU = "#5B6475"         # Unterzeile, Stichwort
GRUEN = "#6FD58E"        # gesuchte Fläche (Füllung)
GRUEN_TXT = "#1E8E4E"    # „?“ und Wort „Grün“ im Titel
GELB = "#FFD45E"
HELLGELB = "#FFF2C2"
HELLBLAU = "#9CCFFF"
BLAU_TXT = "#1F6FC4"
ROT = "#FF8C82"
ROT_TXT = "#E0473C"
GOLD = "#FFC233"
GOLD_TXT = "#C98600"
ORANGE = "#FFB066"
ORANGE_TXT = "#D9691A"
VIOLETT = "#CDB2FF"
VIOLETT_TXT = "#6E47D1"
TUERKIS = "#79DBD2"
TUERKIS_TXT = "#138A80"
KORALLE = "#FF9E9E"
WEISS = "#FFFFFF"
MASS = "#E0473C"         # gegebene Längen (Maßlinien, Zahlen an Strecken)
GESUCHT = "#1F6FC4"      # gesuchte Länge (z. B. „x“ an einer Maßlinie)

# Kartengrund: zarte Pastelltöne mit passender Akzentfarbe (für Datum, Kopfzeile)
HINTERGRUENDE = [("#EAF4FF", "#2F6FB8"), ("#FFF0E5", "#C8621C"), ("#EBF9EE", "#25884A"),
                 ("#F4EEFF", "#6847C2"), ("#FFF7D9", "#A87A00"), ("#E6F8F6", "#14857B"),
                 ("#FFEEF1", "#C2405A")]


def _grund(nr, hintergrund):
    if hintergrund:
        return hintergrund if isinstance(hintergrund, tuple) else (hintergrund, TINTE)
    return HINTERGRUENDE[(nr or 0) % len(HINTERGRUENDE)]


def _tafel(fig, x0, y0, x1, y1):
    """Weiße, abgerundete Tafel mit weichem Schatten (Figurkoordinaten 0..1)."""
    from matplotlib.patches import FancyBboxPatch
    w, h = x1 - x0, y1 - y0
    for d, a in ((0.010, 0.05), (0.006, 0.07)):
        fig.patches.append(FancyBboxPatch((x0 + d*0.4, y0 - d), w, h, boxstyle="round,pad=0,rounding_size=0.028",
                                          transform=fig.transFigure, facecolor="#1D2330", alpha=a,
                                          edgecolor="none", zorder=-10))
    fig.patches.append(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0,rounding_size=0.028",
                                      transform=fig.transFigure, facecolor=WEISS, edgecolor="none", zorder=-10))


LW = 3.2                 # Linienstärke in pt (≈ 4,4 px)

PX = 1100
DPI = 100


# ---------------------------------------------------------------- Karte
class Karte:
    """Eine Karte: Titel auf farbigem Grund, Figur auf weißer Tafel, Stichwort,
    Datum/Nr. senkrecht links, Signatur unten. hintergrund: Farbe oder (Farbe, Akzent);
    ohne Angabe wechselt der Grund mit der Nummer."""

    def __init__(self, titel, zeile=None, stichwort=None, datum="", nr=None,
                 sprache="de", signatur=None, hintergrund=None):
        self.grund, self.akzent = _grund(nr, hintergrund)
        self.fig = plt.figure(figsize=(PX / DPI, PX / DPI), dpi=DPI, facecolor=self.grund)
        self.titel = titel if isinstance(titel, list) else [(titel, TINTE)]
        self.zeile = zeile
        self.stichwort = stichwort
        self.datum = datum
        self.nr = nr
        self.signatur = signatur or ("#GeoRätsel" if sprache == "de" else "#GeoPuzzle")
        tafel_oben = 0.83 if zeile else 0.865
        tafel_unten = 0.07
        _tafel(self.fig, 0.085, tafel_unten, 0.955, tafel_oben)
        oben = tafel_oben - 0.03
        unten = tafel_unten + (0.075 if stichwort else 0.03)
        self.ax = self.fig.add_axes([0.13, unten, 0.78, oben - unten])
        self.ax.set_aspect("equal")
        self.ax.axis("off")
        self.ax.patch.set_alpha(0)

    # -- Textteile
    def _titel_zeichnen(self):
        r = self.fig.canvas.get_renderer()
        teile, breiten = [], []
        for text, farbe in self.titel:
            t = self.fig.text(0, 0.932, text, fontsize=46, fontweight="bold", color=farbe,
                              ha="left", va="center")
            teile.append(t)
            breiten.append(t.get_window_extent(r).width / PX)
        x = 0.52 - sum(breiten) / 2
        for t, b in zip(teile, breiten):
            t.set_x(x)
            x += b
        if self.zeile:
            self.fig.text(0.52, 0.868, self.zeile, fontsize=23, color=GRAU,
                          ha="center", va="center")

    def _rand_zeichnen(self):
        if self.datum or self.nr is not None:
            s = f"{self.datum}  #{self.nr}" if self.nr is not None else self.datum
            self.fig.text(0.043, 0.47, s, fontsize=22, fontweight="bold", color=self.akzent,
                          rotation=90, ha="center", va="center")
        if self.stichwort:
            self.fig.text(0.52, 0.11, self.stichwort, fontsize=28, style="italic",
                          color=TINTE, ha="center", va="center")
        self.fig.text(0.52, 0.035, self.signatur, fontsize=15, fontweight="bold",
                      color=self.akzent, ha="center", va="center")

    def speichern(self, pfad, rand=0.04):
        """Figur einpassen (gleicher Maßstab in x und y) und PNG schreiben."""
        ax = self.ax
        ax.relim(visible_only=True)
        ax.autoscale_view()
        (x0, x1), (y0, y1) = ax.get_xlim(), ax.get_ylim()
        dx, dy = (x1 - x0) * rand, (y1 - y0) * rand
        ax.set_xlim(x0 - dx, x1 + dx)
        ax.set_ylim(y0 - dy, y1 + dy)
        ax.set_anchor("C")
        self._titel_zeichnen()
        self._rand_zeichnen()
        self.fig.savefig(pfad, dpi=DPI, facecolor=self.grund)
        plt.close(self.fig)
        return pfad


class Loesungskarte(Karte):
    """Lösungskarte (1100 px breit, Höhe passt sich dem Text an): Kopf „Lösung #Nr“,
    Antwort als Titel, große Figur mit Hilfslinien, darunter der Lösungsweg
    (Liste von Absätzen, kurze Sätze) – alles auf einer weißen Tafel."""

    FIG_OBEN, FIG_UNTEN = 175, 805          # Figurbereich in px von oben

    def __init__(self, antwort, schritte, datum="", nr=None, sprache="de", signatur=None,
                 umbruch=60, hintergrund=None):
        import textwrap
        self.grund, self.akzent = _grund(nr, hintergrund)
        self.titel = antwort if isinstance(antwort, list) else [(antwort, TINTE)]
        kopf = "Lösung" if sprache == "de" else "Solution"
        self.zeile = f"{kopf} #{nr}" if nr is not None else kopf
        self.stichwort = None
        self.datum, self.nr = datum, nr
        self.signatur = signatur or ("#GeoRätsel" if sprache == "de" else "#GeoPuzzle")
        self.zeilen = []
        for absatz in schritte:
            self.zeilen += textwrap.wrap(absatz, umbruch) or [""]
            self.zeilen.append(None)
        if self.zeilen:
            self.zeilen.pop()
        text_px = 36 * sum(z is not None for z in self.zeilen) + 16 * sum(z is None for z in self.zeilen)
        self.H = max(PX, self.FIG_UNTEN + 40 + text_px + 110)
        self.fig = plt.figure(figsize=(PX / DPI, self.H / DPI), dpi=DPI, facecolor=self.grund)
        f = self._f
        _tafel(self.fig, 0.085, f(self.H - 72), 0.955, f(150))
        self.ax = self.fig.add_axes([0.14, f(self.FIG_UNTEN), 0.74, f(self.FIG_OBEN) - f(self.FIG_UNTEN)])
        self.ax.set_aspect("equal")
        self.ax.axis("off")
        self.ax.patch.set_alpha(0)

    def _f(self, y_px):
        return 1 - y_px / self.H

    def _titel_zeichnen(self):
        r = self.fig.canvas.get_renderer()
        teile, breiten = [], []
        for text, farbe in self.titel:
            t = self.fig.text(0, self._f(100), text, fontsize=44, fontweight="bold", color=farbe,
                              ha="left", va="center")
            teile.append(t)
            breiten.append(t.get_window_extent(r).width / PX)
        x = 0.52 - sum(breiten) / 2
        for t, b in zip(teile, breiten):
            t.set_x(x)
            x += b
        self.fig.text(0.52, self._f(40), self.zeile, fontsize=22, fontweight="bold", color=self.akzent,
                      ha="center", va="center")

    def _rand_zeichnen(self):
        f = self._f
        if self.datum or self.nr is not None:
            s = f"{self.datum}  #{self.nr}" if self.nr is not None else self.datum
            self.fig.text(0.043, f((self.FIG_OBEN + self.FIG_UNTEN) / 2), s, fontsize=22,
                          fontweight="bold", color=self.akzent, rotation=90, ha="center", va="center")
        y = self.FIG_UNTEN + 40
        for z in self.zeilen:
            if z is None:
                y += 16
                continue
            self.fig.text(0.13, f(y), z, fontsize=21, color=TINTE, ha="left", va="top")
            y += 36
        self.fig.text(0.52, f(self.H - 36), self.signatur, fontsize=15, fontweight="bold",
                      color=self.akzent, ha="center", va="center")


def hilfslinie(ax, p, q, farbe="#1565C0", lw=2.4, z=5):
    """Gestrichelte Hilfslinie – nur auf Lösungskarten."""
    ax.plot([p[0], q[0]], [p[1], q[1]], color=farbe, lw=lw, ls=(0, (5, 3)), zorder=z)


# ---------------------------------------------------------------- Hilfen
def _v(p):
    return np.asarray(p, dtype=float)


def _einheit(p, q):
    d = _v(q) - _v(p)
    return d / np.linalg.norm(d)


def _massstab(ax):
    """Datenlänge, die etwa 1 % der Figurbreite entspricht (für Marken-Größen)."""
    x0, x1 = ax.dataLim.x0, ax.dataLim.x1
    y0, y1 = ax.dataLim.y0, ax.dataLim.y1
    s = max(x1 - x0, y1 - y0)
    return (s if np.isfinite(s) and s > 0 else 1.0) / 100


# ---------------------------------------------------------------- Formen
def flaeche(ax, punkte, farbe, kontur=True, schraffur=None, schraffur_farbe=None, z=1):
    """Gefülltes Vieleck. schraffur '/' (locker) oder '//' für Überlappungen,
    gemalt in schraffur_farbe über der Füllung (wie Gold-Streifen auf Rot)."""
    p = Polygon(punkte, closed=True, facecolor=farbe, edgecolor=TINTE if kontur else "none",
                lw=LW if kontur else 0, joinstyle="round", zorder=z)
    ax.add_patch(p)
    if schraffur:
        h = Polygon(punkte, closed=True, facecolor="none", lw=0, hatch=schraffur,
                    edgecolor=schraffur_farbe or GOLD, zorder=z + 0.1)
        ax.add_patch(h)
    return p


def bereich(ax, geom, farbe, schraffur=None, schraffur_farbe=None, z=1):
    """Gefüllte shapely-Fläche (auch mit Kreisbögen, Löchern, Mehrteilen). Ohne Kontur –
    Konturen separat mit linie/kreis/bogen zeichnen."""
    from shapely.geometry import MultiPolygon, Polygon as SPoly
    teile = geom.geoms if isinstance(geom, MultiPolygon) else [geom]
    for g in teile:
        if not isinstance(g, SPoly) or g.is_empty:
            continue
        verts, codes = [], []
        for ring in [g.exterior, *g.interiors]:
            xy = list(ring.coords)
            verts += xy
            codes += [MPath.MOVETO] + [MPath.LINETO] * (len(xy) - 2) + [MPath.CLOSEPOLY]
        pfad = MPath(verts, codes)
        ax.add_patch(PathPatch(pfad, facecolor=farbe, lw=0, zorder=z))
        if schraffur:
            ax.add_patch(PathPatch(pfad, facecolor="none", lw=0, hatch=schraffur,
                                   edgecolor=schraffur_farbe or GOLD, zorder=z + 0.1))


def kreisflaeche(mitte, r, n=720):
    """shapely-Kreis (für bereich(), Schnitte, Flächenrechnung)."""
    from shapely.geometry import Point
    return Point(mitte).buffer(r, quad_segs=n // 4)


def linie(ax, p, q, lw=LW, farbe=TINTE, z=3):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=farbe, lw=lw, solid_capstyle="round", zorder=z)


def zug(ax, punkte, geschlossen=True, lw=LW, z=3):
    pts = list(punkte) + ([punkte[0]] if geschlossen else [])
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=TINTE, lw=lw, solid_joinstyle="round", solid_capstyle="round", zorder=z)


def kreis(ax, mitte, r, lw=LW, farbe=None, z=3):
    ax.add_patch(Circle(mitte, r, facecolor=farbe or "none", edgecolor=TINTE, lw=lw, zorder=z))


def bogen(ax, mitte, r, von_grad, bis_grad, lw=LW, z=3):
    """Kreisbogen gegen den Uhrzeigersinn von von_grad bis bis_grad."""
    ax.add_patch(Arc(mitte, 2 * r, 2 * r, theta1=von_grad, theta2=bis_grad,
                     edgecolor=TINTE, lw=lw, zorder=z))


def regelmaessiges_vieleck(mitte, r, n, start_grad=90):
    """Ecken eines regelmäßigen n-Ecks (Umkreisradius r)."""
    return [(mitte[0] + r * math.cos(math.radians(start_grad + 360 * k / n)),
             mitte[1] + r * math.sin(math.radians(start_grad + 360 * k / n))) for k in range(n)]


# ---------------------------------------------------------------- Marken
def punkt(ax, p, art="hohl", z=6):
    """Wichtiger Punkt: 'hohl' (weiß mit Rand), 'voll' (schwarz) oder 'rot' (Mittelpunkt)."""
    fc = {"hohl": WEISS, "voll": TINTE, "rot": "#E02020"}[art]
    ax.plot([p[0]], [p[1]], marker="o", ms=11, mfc=fc, mec=TINTE, mew=2.2, zorder=z)


def strich(ax, p, q, anzahl=1, t=0.5, laenge=2.2):
    """Strichmarke(n) 'gleich lang' quer auf der Strecke pq bei Anteil t."""
    s = _massstab(ax) * laenge
    u = _einheit(p, q)
    n = np.array([-u[1], u[0]])
    m = _v(p) + t * (_v(q) - _v(p))
    abstand = s * 0.55
    for i in range(anzahl):
        c = m + u * abstand * (i - (anzahl - 1) / 2)
        a, b = c - n * s, c + n * s
        ax.plot([a[0], b[0]], [a[1], b[1]], color=TINTE, lw=LW * 0.8, zorder=4)


def parallel(ax, p, q, anzahl=1, t=0.55, groesse=2.4):
    """Pfeilspitze(n) 'parallel' auf der Strecke pq, zeigt von p nach q."""
    s = _massstab(ax) * groesse
    u = _einheit(p, q)
    n = np.array([-u[1], u[0]])
    m = _v(p) + t * (_v(q) - _v(p))
    for i in range(anzahl):
        spitze = m + u * s * 0.9 * i
        a = spitze - u * s * 1.3 + n * s * 0.55
        b = spitze - u * s * 1.3 - n * s * 0.55
        ax.plot([a[0], spitze[0], b[0]], [a[1], spitze[1], b[1]], color=TINTE,
                lw=LW * 0.8, solid_joinstyle="miter", zorder=4)


def rechter_winkel(ax, ecke, p1, p2, groesse=3.5):
    """Quadrätchen im rechten Winkel bei 'ecke' zwischen den Richtungen zu p1 und p2."""
    s = _massstab(ax) * groesse
    e = _v(ecke)
    a = e + _einheit(e, p1) * s
    b = e + _einheit(e, p2) * s
    c = a + (b - e)
    ax.plot([a[0], c[0], b[0]], [a[1], c[1], b[1]], color=TINTE, lw=LW * 0.6, zorder=4)


def winkel(ax, ecke, p1, p2, text=None, r=7, farbe=TINTE, groesse=22, text_abstand=1.55):
    """Winkelbogen von Richtung p1 nach p2 (gegen den Uhrzeigersinn), Text IM Winkel."""
    s = _massstab(ax) * r
    e = _v(ecke)
    a1 = math.degrees(math.atan2(p1[1] - e[1], p1[0] - e[0]))
    a2 = math.degrees(math.atan2(p2[1] - e[1], p2[0] - e[0]))
    if a2 < a1:
        a2 += 360
    ax.add_patch(Arc(e, 2 * s, 2 * s, theta1=a1, theta2=a2, edgecolor=farbe,
                     lw=LW * 0.7, zorder=4))
    if text:
        m = math.radians((a1 + a2) / 2)
        pos = e + np.array([math.cos(m), math.sin(m)]) * s * text_abstand
        ax.text(pos[0], pos[1], text, fontsize=groesse, fontweight="bold", color=farbe,
                ha="center", va="center", zorder=7)


def zahl(ax, p, text, groesse=40, farbe=TINTE, fett=True, z=7):
    """Zahl oder Buchstabe in einer Fläche (Fläche = Zahl)."""
    ax.text(p[0], p[1], text, fontsize=groesse, fontweight="bold" if fett else "normal",
            color=farbe, ha="center", va="center", zorder=z,
            path_effects=[pe.withStroke(linewidth=0, foreground="none")])


def an_strecke(ax, p, q, text, seite=1, abstand=3.5, groesse=26, farbe=MASS, drehen=None):
    """Längen-Beschriftung neben der Strecke pq (wie '15k'). seite=+1 links von p→q.
    Gedreht wird nur bei flachen Strecken (bis 60°), damit z. B. eine 6 nie wie eine 9 aussieht."""
    s = _massstab(ax) * abstand
    u = _einheit(p, q)
    n = np.array([-u[1], u[0]]) * seite
    m = (_v(p) + _v(q)) / 2 + n * s
    w = math.degrees(math.atan2(u[1], u[0]))
    if w > 90:
        w -= 180
    if w < -90:
        w += 180
    ha = "center"
    if drehen is False or (drehen is None and abs(w) > 60):
        w = 0
        ha = "left" if n[0] > 0.5 else "right" if n[0] < -0.5 else "center"
    ax.text(m[0], m[1], text, fontsize=groesse, fontweight="bold", color=farbe,
            rotation=w, rotation_mode="anchor", ha=ha, va="center", zorder=7)


def masslinie(ax, p, q, text, abstand=6, seite=1, groesse=26, farbe=MASS):
    """Maßlinie mit Hilfslinien an den echten Bezugspunkten p, q; Text mittig daneben.
    Gegebene Längen in MASS (korallenrot), gesuchte z. B. mit farbe=GESUCHT (blau)."""
    s = _massstab(ax)
    u = _einheit(p, q)
    n = np.array([-u[1], u[0]]) * seite
    a, b = _v(p) + n * s * abstand, _v(q) + n * s * abstand
    for x, y in ((p, a), (q, b)):
        e = _v(y) + n * s * 1.2
        ax.plot([x[0] + n[0] * s, e[0]], [x[1] + n[1] * s, e[1]], color=farbe, lw=1.6, zorder=4)
    ax.annotate("", xy=a, xytext=b, arrowprops=dict(arrowstyle="<|-|>", color=farbe, lw=1.8,
                                                    shrinkA=0, shrinkB=0, mutation_scale=18),
                zorder=4)
    an_strecke(ax, a, b, text, seite=seite, abstand=2.6, groesse=groesse, farbe=farbe)


# ---------------------------------------------------------------- Kontaktbogen
def kontaktbogen(pfade, ziel, spalten=4, breite=360):
    """Alle Karten verkleinert auf einem Blatt – zum schnellen Ansehen."""
    from PIL import Image
    bilder = [Image.open(p).convert("RGB").resize((breite, breite)) for p in pfade]
    zeilen = math.ceil(len(bilder) / spalten)
    blatt = Image.new("RGB", (spalten * (breite + 10) + 10, zeilen * (breite + 10) + 10), "#DDDDDD")
    for i, b in enumerate(bilder):
        blatt.paste(b, (10 + (i % spalten) * (breite + 10), 10 + (i // spalten) * (breite + 10)))
    blatt.save(ziel)
    return ziel
