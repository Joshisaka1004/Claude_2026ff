# Viertelkreis mit Rechteck, Ecke auf dem Bogen: Diagonale = Radius. (r-2)^2+(r-1)^2=r^2 -> r=5, Fläche 12.
import math
from _basis import *

NR, KURZ = 25, "viertelkreis"
TITEL = {"de": [("Grün", GRUEN_TXT), (" = ?", TINTE)], "en": [("Green", GRUEN_TXT), (" = ?", TINTE)]}
ZEILE = {"de": None, "en": None}
STICHWORT = {"de": "Viertelkreis", "en": "quarter circle"}
ANTWORT = {"de": [("Grün", GRUEN_TXT), (" = 12", TINTE)], "en": [("Green", GRUEN_TXT), (" = 12", TINTE)]}
SCHRITTE = {
    "de": ["Die Diagonale vom Mittelpunkt zur Ecke auf dem Bogen ist ein Radius r.",
           "Die Rechteckseiten sind r − 2 und r − 1.",
           "Pythagoras: (r − 2)² + (r − 1)² = r². Das ergibt r² − 6r + 5 = 0, also r = 5 (r = 1 ist zu klein).",
           "Das Rechteck ist 3 mal 4. Grün = 12."],
    "en": ["The diagonal from the centre to the corner on the arc is a radius r.",
           "The sides of the rectangle are r − 2 and r − 1.",
           "Pythagoras: (r − 2)² + (r − 1)² = r². This gives r² − 6r + 5 = 0, so r = 5 (r = 1 is too small).",
           "The rectangle is 3 by 4. Green = 12."],
}
R = 5.0

def pruefen():
    # r^2 - 6r + 5 = 0
    wurzeln = sorted([(6 - math.sqrt(16))/2, (6 + math.sqrt(16))/2])
    gueltig = [r for r in wurzeln if r - 2 > 0 and r - 1 > 0]
    assert gueltig == [5.0]
    assert abs(3**2 + 4**2 - R**2) < 1e-12
    return "einzige gültige Lösung r = 5, Fläche 3 · 4 = 12"

def figur(ax, loesung=False):
    flaeche(ax, [(0, 0), (3, 0), (3, 4), (0, 4)], GRUEN, kontur=False)
    linie(ax, (0, 0), (R, 0)); linie(ax, (0, 0), (0, R)); bogen(ax, (0, 0), R, 0, 90)
    zug(ax, [(0, 0), (3, 0), (3, 4), (0, 4)])
    rechter_winkel(ax, (0, 0), (1, 0), (0, 1), groesse=3.5)
    punkt(ax, (3, 4)); punkt(ax, (3, 0)); punkt(ax, (0, 4)); punkt(ax, (R, 0)); punkt(ax, (0, R))
    masslinie(ax, (3, 0), (R, 0), "2", seite=-1, abstand=6)
    masslinie(ax, (0, 4), (0, R), "1", seite=1, abstand=6)
    if loesung:
        hilfslinie(ax, (0, 0), (3, 4))
        an_strecke(ax, (0, 0), (3, 4), "r", seite=1, abstand=3)
        an_strecke(ax, (0, 0), (3, 0), "r − 2", seite=1, abstand=3.5, groesse=22)
        an_strecke(ax, (3, 0), (3, 4), "r − 1", seite=1, abstand=3.5, groesse=22)
    else:
        zahl(ax, (1.5, 2.0), "?", farbe=GRUEN_TXT, groesse=48)
