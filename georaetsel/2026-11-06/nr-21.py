# Gleichseitiges Dreieck mit Inkreis und Umkreis: Ring : Inkreis = 3 : 1.
import math, random
from _basis import *

NR, KURZ = 21, "ring"
TITEL = {"de": [("Gelb", GOLD_TXT), (" : ", TINTE), ("Grün", GRUEN_TXT), (" = ?", TINTE)],
         "en": [("Yellow", GOLD_TXT), (" : ", TINTE), ("Green", GRUEN_TXT), (" = ?", TINTE)]}
ZEILE = {"de": None, "en": None}
STICHWORT = {"de": "gleichseitiges Dreieck", "en": "equilateral triangle"}
ANTWORT = {"de": [("Gelb", GOLD_TXT), (" : ", TINTE), ("Grün", GRUEN_TXT), (" = 3 : 1", TINTE)],
           "en": [("Yellow", GOLD_TXT), (" : ", TINTE), ("Green", GRUEN_TXT), (" = 3 : 1", TINTE)]}
SCHRITTE = {
    "de": ["Das Dreieck aus Mittelpunkt, Ecke und Berührpunkt ist ein halbes gleichseitiges Dreieck. Darum ist R doppelt so lang wie r.",
           "Doppelter Radius heißt vierfache Fläche: Der große Kreis ist 4-mal so groß wie Grün.",
           "Gelb = 4 − 1 = 3 grüne Kreise. Gelb : Grün = 3 : 1."],
    "en": ["The triangle made of centre, corner and touching point is half of an equilateral triangle. So R is twice as long as r.",
           "Twice the radius means four times the area: the big circle is 4 times green.",
           "Yellow = 4 − 1 = 3 green circles. Yellow : Green = 3 : 1."],
}
R, r = 2.0, 1.0
ECKEN = regelmaessiges_vieleck((0, 0), R, 3, 90)

def pruefen():
    for _ in range(20):
        s = random.uniform(0.5, 20)                       # Seitenlänge
        h = s*math.sqrt(3)/2; ri = h/3; Ru = 2*h/3       # Inkreis/Umkreis aus der Höhe
        assert abs((math.pi*Ru**2 - math.pi*ri**2)/(math.pi*ri**2) - 3) < 1e-9
    # Zeichnung: Inkreis berührt die Seiten
    (x1, y1), (x2, y2) = ECKEN[1], ECKEN[2]
    assert abs(abs(y1) - r) < 1e-12
    return "Verhältnis 3 : 1 für 20 zufällige Seitenlängen"

def figur(ax, loesung=False):
    kreis(ax, (0, 0), R, farbe=GELB)
    kreis(ax, (0, 0), r, farbe=GRUEN)
    zug(ax, ECKEN)
    for e in ECKEN: punkt(ax, e)
    beruehr = [(-ECKEN[i][0]/2, -ECKEN[i][1]/2) for i in range(3)]
    for b in beruehr: punkt(ax, b)
    if loesung:
        V = ECKEN[2]
        hilfslinie(ax, (0, 0), V); hilfslinie(ax, (0, 0), (0, -r)); hilfslinie(ax, (0, -r), V)
        rechter_winkel(ax, (0, -r), (0, 0), V, groesse=3.5)
        an_strecke(ax, (0, 0), (0, -r), "r", seite=1, abstand=2.5, drehen=False)
        an_strecke(ax, (0, 0), V, "R", seite=1, abstand=3, drehen=False)
        winkel(ax, V, (0, 0), (0, -r), "30°", r=16, groesse=17, text_abstand=1.75)
        punkt(ax, (0, 0), "rot")
    else:
        zahl(ax, (0, 0.05), "?", farbe=GRUEN_TXT, groesse=48)
