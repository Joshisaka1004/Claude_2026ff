# Schiefes Trapez mit Inkreis: Schenkelstücke 4 | 9 und 3 | ? → r² = 4·9 → r = 6, ? = 12 → Fläche (7 + 21)/2 · 12 = 168.
import math, random
from _basis import *
from _geo import fuss, abst, flaeche as fl

NR, KURZ = 33, "tangententrapez"
TITEL = {"de": [("Fläche des Trapezes = ?", TINTE)], "en": [("Area of the trapezoid = ?", TINTE)]}
ZEILE = {"de": None, "en": None}
STICHWORT = {"de": None, "en": None}
ANTWORT = {"de": [("Fläche = 168", TINTE)], "en": [("Area = 168", TINTE)]}
SCHRITTE = {
    "de": ["Verbinde den Kreismittelpunkt mit den zwei Ecken der linken Seite. Die zwei Winkel an dieser Seite ergeben zusammen 180°, ihre Hälften also 90°: Das Dreieck hat am Mittelpunkt einen rechten Winkel.",
           "Der Radius zum Berührpunkt ist die Höhe in diesem rechtwinkligen Dreieck. Höhensatz: r² = 4 · 9 = 36, also r = 6.",
           "Rechts genauso: 3 · x = 36, also x = 12.",
           "Von einer Ecke aus sind beide Tangenten gleich lang: oben 4 + 3 = 7, unten 9 + 12 = 21. Höhe = 2r = 12.",
           "Fläche = (7 + 21) : 2 · 12 = 168."],
    "en": ["Join the centre of the circle to the two corners of the left side. The two angles at this side add up to 180°, their halves to 90°: the triangle has a right angle at the centre.",
           "The radius to the touching point is the height in this right triangle. Altitude rule: r² = 4 · 9 = 36, so r = 6.",
           "The same on the right: 3 · x = 36, so x = 12.",
           "From one corner both tangents are equally long: top 4 + 3 = 7, bottom 9 + 12 = 21. Height = 2r = 12.",
           "Area = (7 + 21) : 2 · 12 = 168."],
}
A, B, C, D = (0.0, 0.0), (21.0, 0.0), (12.0, 12.0), (5.0, 12.0)
I, RAD = (9.0, 6.0), 6.0

def pruefen():
    for a, b in ((A, B), (B, C), (C, D), (D, A)):
        assert abs(abst(I, fuss(I, a, b)) - RAD) < 1e-12                 # Inkreis berührt alle Seiten
    TL = fuss(I, A, D); TR = fuss(I, B, C)
    assert abs(abst(D, TL) - 4) < 1e-9 and abs(abst(TL, A) - 9) < 1e-9 and abs(abst(C, TR) - 3) < 1e-9
    assert abs(fl(A, B, C, D) - 168) < 1e-9
    # Bestimmtheit: Für zufällige Tangententrapeze gilt r² = (Stück oben)·(Stück unten) je Schenkel,
    # also legen 4, 9, 3 Radius und alle Tangentenstücke fest → Fläche fest.
    for _ in range(20):
        r = random.uniform(1, 10); a1 = random.uniform(0.2, 3*r); a2 = random.uniform(0.2, 3*r)
        b1, b2 = r*r/a1, r*r/a2                          # untere Stücke aus dem Höhensatz
        # Trapez aus den Tangentenstücken bauen und Inkreis prüfen
        Dd, Cc = (-a1, 2*r), (a2, 2*r); Aa, Bb = (-b1, 0.0), (b2, 0.0)   # Berührpunkte oben/unten bei x = 0
        Ii = (0.0, r)
        for p, q in ((Aa, Bb), (Bb, Cc), (Cc, Dd), (Dd, Aa)):
            assert abs(abst(Ii, fuss(Ii, p, q)) - r) < 1e-7
    return "Inkreis berührt alle vier Seiten; Stücke 4 | 9 | 3 | 12; Fläche 168; Höhensatz an 20 Zufallstrapezen bestätigt"

def figur(ax, loesung=False):
    flaeche(ax, [A, B, C, D], GRUEN, kontur=False)
    kreis(ax, I, RAD)
    zug(ax, [A, B, C, D])
    parallel(ax, A, B, t=0.75); parallel(ax, D, C, t=0.25)
    TL, TR, TB, TT = fuss(I, A, D), fuss(I, B, C), fuss(I, A, B), fuss(I, D, C)
    for p in (TL, TR, TB, TT): punkt(ax, p)
    masslinie(ax, A, TL, "9", seite=1, abstand=5, groesse=28)
    masslinie(ax, TL, D, "4", seite=1, abstand=5, groesse=28)
    masslinie(ax, TR, C, "3", seite=-1, abstand=5, groesse=28)
    if loesung:
        punkt(ax, I, "rot")
        hilfslinie(ax, I, A); hilfslinie(ax, I, D); hilfslinie(ax, I, TL)
        hilfslinie(ax, I, B); hilfslinie(ax, I, C); hilfslinie(ax, I, TR)
        rechter_winkel(ax, I, A, D, groesse=3); rechter_winkel(ax, TL, I, D, groesse=2.5)
        masslinie(ax, B, TR, "12", seite=-1, abstand=5, groesse=24)
        an_strecke(ax, I, TL, "6", seite=1, abstand=2.5, groesse=24, drehen=False)
