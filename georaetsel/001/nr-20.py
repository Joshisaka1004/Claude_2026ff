# Rechteck, Punkt auf der Diagonale, Parallelen zu den Seiten: die zwei Rechtecke neben der Diagonale sind gleich groß.
import random
from _basis import *

NR, KURZ = 20, "diagonale"
TITEL = {"de": [("Grün", GRUEN_TXT), (" = ?", TINTE)], "en": [("Green", GRUEN_TXT), (" = ?", TINTE)]}
ZEILE = {"de": None, "en": None}
STICHWORT = {"de": "Rechteck", "en": "rectangle"}
ANTWORT = {"de": [("Grün", GRUEN_TXT), (" = 6", TINTE)], "en": [("Green", GRUEN_TXT), (" = 6", TINTE)]}
SCHRITTE = {
    "de": ["Die Diagonale teilt das große Rechteck in zwei gleich große Hälften.",
           "Sie teilt auch die zwei kleinen Rechtecke an der Diagonale in je zwei gleiche Dreiecke (gelb und orange).",
           "Oben links bleibt nach dem Abziehen der gelben und orangen Dreiecke das Rechteck 6. Unten rechts bleibt Grün.",
           "Gleiches minus Gleiches ergibt Gleiches: Grün = 6."],
    "en": ["The diagonal cuts the big rectangle into two halves of equal area.",
           "It also cuts the two small rectangles on the diagonal into two equal triangles each (yellow and orange).",
           "Take the yellow and orange triangles away: top left the rectangle 6 is left, bottom right green is left.",
           "Equal minus equal is equal: green = 6."],
}
W, H, T = 7.5, 5.0, 0.2

def pruefen():
    for _ in range(40):
        w, h, t = random.uniform(1, 10), random.uniform(1, 10), random.uniform(0.05, 0.95)
        oben_links = t*w*(1-t)*h; k = 6/oben_links
        unten_rechts = (1-t)*w*t*h*k
        assert abs(unten_rechts - 6) < 1e-9
    assert abs(T*W*(1-T)*H - 6) < 1e-12 and abs((1-T)*W*T*H - 6) < 1e-12
    return "Grün = 6 für 40 zufällige Rechtecke und Lagen des Punktes"

def figur(ax, loesung=False):
    px, py = T*W, T*H
    flaeche(ax, [(0, py), (px, py), (px, H), (0, H)], HELLBLAU, kontur=False)
    flaeche(ax, [(px, 0), (W, 0), (W, py), (px, py)], GRUEN, kontur=False)
    if loesung:
        flaeche(ax, [(0, 0), (px, 0), (px, py)], GELB, kontur=False)
        flaeche(ax, [(0, 0), (0, py), (px, py)], GELB, kontur=False)
        flaeche(ax, [(px, py), (W, py), (W, H)], ORANGE, kontur=False)
        flaeche(ax, [(px, py), (px, H), (W, H)], ORANGE, kontur=False)
    zug(ax, [(0, 0), (W, 0), (W, H), (0, H)])
    linie(ax, (px, 0), (px, H)); linie(ax, (0, py), (W, py)); linie(ax, (0, 0), (W, H))
    punkt(ax, (px, py))
    zahl(ax, (px/2, (py+H)/2), "6")
    zahl(ax, ((px+W)/2, py/2), "?" if not loesung else "6", farbe=GRUEN_TXT)
