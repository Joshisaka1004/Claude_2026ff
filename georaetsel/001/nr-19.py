# Zwei Quadrate: Ecke des zweiten im Mittelpunkt des ersten. Überlappung = 1/4, egal wie gedreht.
import math, random
from _basis import *
from shapely.geometry import box, Polygon as SP

NR, KURZ = 19, "ueberlappung"
TITEL = {"de": [("Grün", GRUEN_TXT), (" = ?", TINTE)], "en": [("Green", GRUEN_TXT), (" = ?", TINTE)]}
ZEILE = {"de": None, "en": None}
STICHWORT = {"de": "zwei Quadrate", "en": "two squares"}
ANTWORT = {"de": [("Grün", GRUEN_TXT), (" = 9", TINTE)], "en": [("Green", GRUEN_TXT), (" = 9", TINTE)]}
SCHRITTE = {
    "de": ["Zeichne vom Mittelpunkt zwei Linien: zur Mitte der rechten und zur Mitte der oberen Seite. Sie schneiden ein Viertel des Quadrats ab.",
           "Die zwei gelben Dreiecke sind gleich groß. Dreht man das untere um 90° um den Mittelpunkt, liegt es genau auf dem oberen.",
           "Grün ist also immer ein Viertel des Quadrats – egal, wie das zweite Quadrat gedreht ist.",
           "Grün = 6 · 6 : 4 = 9."],
    "en": ["From the centre, draw two lines: to the middle of the right side and to the middle of the top side. They cut off a quarter of the square.",
           "The two yellow triangles have the same area. Turn the lower one by 90° around the centre and it lands exactly on the upper one.",
           "So green is always a quarter of the square – no matter how the second square is turned.",
           "Green = 6 · 6 : 4 = 9."],
}

def bau(theta=math.radians(22), s=5.0, a=6.0):
    h = a / 2
    A = box(-h, -h, h, h)
    u = (math.cos(theta), math.sin(theta)); v = (-u[1], u[0])
    B = [(0, 0), (s*u[0], s*u[1]), (s*(u[0]+v[0]), s*(u[1]+v[1])), (s*v[0], s*v[1])]
    return A, B, A.intersection(SP(B))

def pruefen():
    for _ in range(40):
        th = math.radians(random.uniform(1, 89)); s = random.uniform(4.3, 9)
        assert abs(bau(th, s)[2].area - 9) < 1e-9
    return "Überlappung = 9 für 40 zufällige Drehungen und Größen (Seite des zweiten Quadrats ≥ 4,25)"

def figur(ax, loesung=False):
    A, B, ov = bau()
    h = 3
    flaeche(ax, [(-h, -h), (h, -h), (h, h), (-h, h)], HELLBLAU, kontur=False)
    if loesung:
        t = 3 * math.tan(math.radians(22))
        bereich(ax, ov, GRUEN)
        flaeche(ax, [(0, 0), (3, 0), (3, t)], GELB, kontur=False, z=2)
        flaeche(ax, [(0, 0), (0, 3), (-t, 3)], GELB, kontur=False, z=2)
        zug(ax, [(-h, -h), (h, -h), (h, h), (-h, h)]); zug(ax, B)
        hilfslinie(ax, (0, 0), (3, 0)); hilfslinie(ax, (0, 0), (0, 3))
        punkt(ax, (3, 0)); punkt(ax, (0, 3))
    else:
        bereich(ax, ov, GRUEN)
        zug(ax, [(-h, -h), (h, -h), (h, h), (-h, h)]); zug(ax, B)
        c = ov.centroid; zahl(ax, (c.x + 0.25, c.y + 0.1), "?", farbe=GRUEN_TXT, groesse=48)
    rechter_winkel(ax, (0, 0), B[1], B[3], groesse=4)
    punkt(ax, (0, 0), "rot")
    masslinie(ax, (-h, -h), (h, -h), "6", seite=-1, abstand=5)
