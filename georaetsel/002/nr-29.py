# Rechtwinkliges Dreieck mit Höhe; Inkreise der Teildreiecke 3 und 4 → großer Inkreis 5 → Dreieck 15-20-25, Fläche 150.
import math, random
from _basis import *
from _geo import fuss, inkreis, flaeche as fl, abst

NR, KURZ = 29, "drei-inkreise"
TITEL = {"de": [("Fläche des Dreiecks = ?", TINTE)], "en": [("Area of the triangle = ?", TINTE)]}
ZEILE = {"de": None, "en": None}
STICHWORT = {"de": None, "en": None}
ANTWORT = {"de": [("Fläche = 150", TINTE)], "en": [("Area = 150", TINTE)]}
SCHRITTE = {
    "de": ["Die zwei Teildreiecke und das ganze Dreieck haben dieselbe Form – nur verschieden groß. Ihre Inkreise wachsen mit: Die Radien verhalten sich wie die langen Seiten.",
           "Für die langen Seiten gilt Pythagoras. Also auch für die Radien: 3² + 4² = 5². Der Inkreis des ganzen Dreiecks hat den Radius 5 (gestrichelt).",
           "Das Dreieck hat die Form 3-4-5. Ein 3-4-5-Dreieck hat den Inkreisradius 1 – unseres ist also 5-mal so groß: Seiten 15, 20, 25.",
           "Fläche = 15 · 20 : 2 = 150."],
    "en": ["The two small triangles and the whole triangle have the same shape – just different sizes. Their incircles grow with them: the radii are in the same ratio as the long sides.",
           "Pythagoras holds for the long sides. So it holds for the radii too: 3² + 4² = 5². The incircle of the whole triangle has radius 5 (dashed).",
           "The triangle has the shape 3-4-5. A 3-4-5 triangle has incircle radius 1 – ours is 5 times as big: sides 15, 20, 25.",
           "Area = 15 · 20 : 2 = 150."],
}

def bau(a=20.0, b=15.0):
    C, B, A = (0.0, 0.0), (a, 0.0), (0.0, b)
    H = fuss(C, A, B)
    return A, B, C, H

def pruefen():
    # 1) Für jede Form gilt r1² + r2² = r² (r = Inkreis des ganzen Dreiecks)
    for _ in range(30):
        A, B, C, H = bau(random.uniform(1, 30), random.uniform(1, 30))
        r1, r2, r = inkreis(A, C, H)[1], inkreis(C, B, H)[1], inkreis(A, B, C)[1]
        assert abs(r1*r1 + r2*r2 - r*r) < 1e-9
    # 2) Vorgabe 3 und 4 legt das Dreieck fest: Form aus r2 : r1 (monoton in b), Größe aus r1
    def q(b):
        A, B, C, H = bau(1.0, b); return inkreis(C, B, H)[1] / inkreis(A, C, H)[1] - 4/3
    lo, hi = 0.01, 100.0
    for _ in range(200):
        m = (lo + hi) / 2
        lo, hi = (lo, m) if q(lo) * q(m) <= 0 else (m, hi)
    A, B, C, H = bau(1.0, lo); k = 3 / inkreis(A, C, H)[1]
    assert abs(fl(A, B, C) * k*k - 150) < 1e-6
    werte = [q(0.01 + i/10) for i in range(1000)]
    assert sum(1 for u, v in zip(werte, werte[1:]) if (u < 0 <= v) or (u > 0 >= v)) == 1
    A, B, C, H = bau()
    assert abs(inkreis(A, C, H)[1] - 3) < 1e-9 and abs(inkreis(C, B, H)[1] - 4) < 1e-9
    return "r1² + r2² = r² für 30 Formen; Radien 3 und 4 legen das Dreieck eindeutig fest; Fläche 150"

def figur(ax, loesung=False):
    A, B, C, H = bau()
    flaeche(ax, [A, B, C], GELB, kontur=False)
    (m1, r1), (m2, r2) = inkreis(A, C, H), inkreis(C, B, H)
    kreis(ax, m1, r1, farbe=HELLBLAU); kreis(ax, m2, r2, farbe=HELLBLAU)
    zug(ax, [A, B, C]); linie(ax, C, H)
    rechter_winkel(ax, C, B, A, groesse=3); rechter_winkel(ax, H, C, B, groesse=3)
    for m, r, t in ((m1, r1, "3"), (m2, r2, "4")):
        f = fuss(m, A, B)
        linie(ax, m, f, lw=2.2); punkt(ax, m, "rot")
        an_strecke(ax, m, f, t, seite=1, abstand=2.6, groesse=28, drehen=True)
    punkt(ax, H)
    if loesung:
        M, R = inkreis(A, B, C)
        from matplotlib.patches import Circle
        ax.add_patch(Circle(M, R, facecolor="none", edgecolor="#1565C0", lw=2.6, ls=(0, (5, 3)), zorder=5))
        an_strecke(ax, C, A, "15", seite=1, abstand=4, groesse=24)
        an_strecke(ax, C, B, "20", seite=-1, abstand=4, groesse=24)
        an_strecke(ax, A, B, "25", seite=1, abstand=4, groesse=24)
