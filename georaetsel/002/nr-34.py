# Kreise mit Radius 6, 6, 4 berühren sich; Kreis durch die drei Berührpunkte = Inkreis des Mittelpunktsdreiecks (10, 10, 12) → r = 3 → 9π.
import math, random
from _basis import *
from _geo import abst, inkreis

NR, KURZ = 34, "drei-kreise"
TITEL = {"de": [("Grün", GRUEN_TXT), (" = ?", TINTE)], "en": [("Green", GRUEN_TXT), (" = ?", TINTE)]}
ZEILE = {"de": "Der grüne Kreis geht durch die drei Berührpunkte.", "en": "The green circle passes through the three touching points."}
STICHWORT = {"de": None, "en": None}
ANTWORT = {"de": [("Grün", GRUEN_TXT), (" = 9π ≈ 28,3", TINTE)], "en": [("Green", GRUEN_TXT), (" = 9π ≈ 28.3", TINTE)]}
SCHRITTE = {
    "de": ["Verbinde die drei Mittelpunkte. Die Berührpunkte liegen auf diesen Verbindungen; die Seiten sind 6 + 6 = 12, 6 + 4 = 10 und 10.",
           "Von jedem Mittelpunkt aus sind seine zwei Berührpunkte gleich weit weg – so wie die Berührpunkte eines Inkreises. Grün ist also der Inkreis dieses Dreiecks.",
           "Das Dreieck 10-10-12 hat die Höhe 8 und die Fläche 12 · 8 : 2 = 48, der halbe Umfang ist 16. Inkreisradius = 48 : 16 = 3.",
           "Grün = π · 3² = 9π."],
    "en": ["Join the three centres. The touching points lie on these lines; the sides are 6 + 6 = 12, 6 + 4 = 10 and 10.",
           "From each centre its two touching points are equally far away – just like the touching points of an incircle. So green is the incircle of this triangle.",
           "The 10-10-12 triangle has height 8 and area 12 · 8 : 2 = 48, half its perimeter is 16. Incircle radius = 48 : 16 = 3.",
           "Green = π · 3² = 9π."],
}
O1, O2, O3 = (-6.0, 0.0), (6.0, 0.0), (0.0, 8.0)
R1, R2, R3 = 6.0, 6.0, 4.0

def beruehr(o1, r1, o2, r2):
    d = abst(o1, o2); t = r1 / d
    return (o1[0] + t*(o2[0]-o1[0]), o1[1] + t*(o2[1]-o1[1]))

def umkreis(a, b, c):
    ax_, ay = a; bx, by = b; cx, cy = c
    d = 2*(ax_*(by-cy) + bx*(cy-ay) + cx*(ay-by))
    ux = ((ax_**2+ay**2)*(by-cy) + (bx**2+by**2)*(cy-ay) + (cx**2+cy**2)*(ay-by))/d
    uy = ((ax_**2+ay**2)*(cx-bx) + (bx**2+by**2)*(ax_-cx) + (cx**2+cy**2)*(bx-ax_))/d
    return (ux, uy), abst((ux, uy), a)

def pruefen():
    assert abs(abst(O1, O2) - 12) < 1e-12 and abs(abst(O1, O3) - 10) < 1e-12 and abs(abst(O2, O3) - 10) < 1e-12
    T = [beruehr(O1, R1, O2, R2), beruehr(O1, R1, O3, R3), beruehr(O2, R2, O3, R3)]
    m, r = umkreis(*T)
    assert abs(r - 3) < 1e-12
    # allgemein: Kreis durch die Berührpunkte = Inkreis des Mittelpunktsdreiecks
    for _ in range(20):
        a, b, c = (random.uniform(1, 10) for _ in range(3))
        p1 = (0.0, 0.0); p2 = (a + b, 0.0)
        # dritter Mittelpunkt mit Abständen a + c und b + c
        x = ((a + c)**2 - (b + c)**2 + (a + b)**2) / (2*(a + b)); y = math.sqrt((a + c)**2 - x*x)
        p3 = (x, y)
        T = [beruehr(p1, a, p2, b), beruehr(p1, a, p3, c), beruehr(p2, b, p3, c)]
        assert abs(umkreis(*T)[1] - inkreis(p1, p2, p3)[1]) < 1e-9
    return "Kreis durch die Berührpunkte hat Radius 3 (Grün = 9π); = Inkreis des Mittelpunktsdreiecks für 20 Zufallsfälle"

def figur(ax, loesung=False):
    T = [beruehr(O1, R1, O2, R2), beruehr(O1, R1, O3, R3), beruehr(O2, R2, O3, R3)]
    m, r = umkreis(*T)
    for o, rr in ((O1, R1), (O2, R2), (O3, R3)):
        kreis(ax, o, rr, farbe=HELLBLAU)
    kreis(ax, m, r, farbe=GRUEN, z=5)
    for p in T: punkt(ax, p)
    for o, rr, ziel, t in ((O1, R1, (-12.0, 0.0), "6"), (O2, R2, (12.0, 0.0), "6"), (O3, R3, (0.0, 12.0), "4")):
        linie(ax, o, ziel, lw=2.2, z=6); punkt(ax, o, "rot")
        an_strecke(ax, o, ziel, t, seite=1 if t != "4" else -1, abstand=2.5, groesse=28, drehen=False)
    if loesung:
        hilfslinie(ax, O1, O2, z=7); hilfslinie(ax, O1, O3, z=7); hilfslinie(ax, O2, O3, z=7)
        hilfslinie(ax, O3, (0.0, 0.0), z=7)
        an_strecke(ax, O3, (0.0, 0.0), "8", seite=1, abstand=2, groesse=22, drehen=False)
        an_strecke(ax, (0.0, 0.0), m, "3", seite=1, abstand=2, groesse=22, drehen=False)
    else:
        zahl(ax, (m[0], m[1] + 0.05), "?", farbe=GRUEN_TXT, groesse=34, z=8)
