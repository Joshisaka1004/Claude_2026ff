# Arbelos: Fläche = Kreis mit Durchmesser CD = pi*3^2 = 9pi, unabhängig von der Teilung.
import math, random
from _basis import *
from shapely.geometry import box

NR, KURZ = 26, "drei-halbkreise"
TITEL = {"de": [("Grün gesamt", GRUEN_TXT), (" = ?", TINTE)], "en": [("Total green", GRUEN_TXT), (" = ?", TINTE)]}
ZEILE = {"de": None, "en": None}
STICHWORT = {"de": "drei Halbkreise", "en": "three semicircles"}
ANTWORT = {"de": [("Grün gesamt", GRUEN_TXT), (" = 9π ≈ 28,3", TINTE)], "en": [("Total green", GRUEN_TXT), (" = 9π ≈ 28.3", TINTE)]}
SCHRITTE = {
    "de": ["Nenne die kleinen Radien a und b. Der große Radius ist a + b.",
           "Grün (beide Teile) = halber großer Kreis minus zwei halbe kleine Kreise = π/2 · ((a + b)² − a² − b²) = π · a · b.",
           "Der Winkel oben an der Spitze der gestrichelten Linien ist ein rechter (Thales). Dafür gilt: 6² = 2a · 2b, also a · b = 9.",
           "Grün = 9π – genau so groß wie der gestrichelte Kreis über der Strecke 6. Wo die Strecke steht, ist egal."],
    "en": ["Call the small radii a and b. The big radius is a + b.",
           "Green (both parts) = half big circle minus two half small circles = π/2 · ((a + b)² − a² − b²) = π · a · b.",
           "The angle at the top of the dashed lines is a right angle (Thales). So 6² = 2a · 2b, which gives a · b = 9.",
           "Green = 9π – exactly the dashed circle on the segment 6. Where the segment stands does not matter."],
}

def bau(ac=4.0, cb=9.0):
    ab = ac + cb
    D = (ac, math.sqrt(ac*cb))
    return ab, D

def gruen(ac, cb):
    ab = ac + cb; oben = box(-1, 0, ab + 1, ab)
    g = kreisflaeche((ab/2, 0), ab/2, 4000) & oben
    g = g.difference(kreisflaeche((ac/2, 0), ac/2, 4000)).difference(kreisflaeche((ac + cb/2, 0), cb/2, 4000))
    return g & oben

def pruefen():
    for _ in range(20):
        ac = random.uniform(0.5, 30); cb = 36/ac
        assert abs(gruen(ac, cb).area - 9*math.pi) < 1e-3
    ab, D = bau(); assert abs(D[1] - 6) < 1e-12
    return "Grün = 9π (bis auf Zeichengenauigkeit) für 20 zufällige Teilungen mit Strecke 6"

def figur(ax, loesung=False):
    ac, cb = 4.0, 9.0
    ab, D = bau(ac, cb)
    bereich(ax, gruen(ac, cb), GRUEN)
    bogen(ax, (ab/2, 0), ab/2, 0, 180); bogen(ax, (ac/2, 0), ac/2, 0, 180); bogen(ax, (ac + cb/2, 0), cb/2, 0, 180)
    linie(ax, (0, 0), (ab, 0)); linie(ax, (ac, 0), D)
    rechter_winkel(ax, (ac, 0), D, (ab, 0), groesse=3)
    for p in ((0, 0), (ac, 0), (ab, 0), D): punkt(ax, p)
    masslinie(ax, (ac, 0), D, "6", seite=1, abstand=3.2, groesse=28)
    if loesung:
        hilfslinie(ax, (0, 0), D); hilfslinie(ax, D, (ab, 0))
        rechter_winkel(ax, D, (0, 0), (ab, 0), groesse=3)
        m = (ac, 3.0)
        from matplotlib.patches import Circle
        ax.add_patch(Circle(m, 3.0, facecolor="none", edgecolor="#1565C0", lw=2.4, ls=(0, (5, 3)), zorder=5))
