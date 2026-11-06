# Regelmäßiges Zwölfeck: Kappe über drei Seiten = genau 1/12 des Zwölfecks.
import math, random
from _basis import *
from shapely.geometry import Polygon as SP

NR, KURZ = 30, "zwoelfeck"
TITEL = {"de": [("Gesamtfläche = ?", TINTE)], "en": [("Total area = ?", TINTE)]}
ZEILE = {"de": None, "en": None}
STICHWORT = {"de": "regelmäßiges Zwölfeck", "en": "regular dodecagon"}
ANTWORT = {"de": [("Gesamtfläche = 12", TINTE)], "en": [("Total area = 12", TINTE)]}
SCHRITTE = {
    "de": ["Zerlege das Zwölfeck vom Mittelpunkt aus in 12 gleiche Dreiecke mit 30° an der Spitze. Jedes hat die Fläche R · (R/2) : 2 = R²/4.",
           "Die blaue Kappe besteht aus drei solchen Dreiecken minus dem Dreieck aus Mittelpunkt und den Enden der Sehne. Dieses hat an der Spitze 3 · 30° = 90°, also die Fläche R · R : 2 = R²/2.",
           "Kappe = 3 · R²/4 − R²/2 = R²/4 – genau so groß wie eines der 12 Dreiecke.",
           "Gesamtfläche = 12 · 1 = 12."],
    "en": ["Cut the dodecagon from the centre into 12 equal triangles with 30° at the tip. Each has area R · (R/2) : 2 = R²/4.",
           "The blue cap is three such triangles minus the triangle made of the centre and the ends of the chord. That one has 3 · 30° = 90° at the tip, so its area is R · R : 2 = R²/2.",
           "Cap = 3 · R²/4 − R²/2 = R²/4 – exactly as big as one of the 12 triangles.",
           "Total area = 12 · 1 = 12."],
}

def bau(R=2.0):
    return regelmaessiges_vieleck((0, 0), R, 12, 225)   # E[0]..E[3] unten, Sehne E0E3 waagerecht

def pruefen():
    for _ in range(20):
        E = bau(random.uniform(0.1, 50))
        assert abs(SP(E).area / SP(E[:4]).area - 12) < 1e-9
    E = bau(); assert abs(SP(E[:4]).area - 1) < 1e-12 and abs(SP(E).area - 12) < 1e-12
    return "Zwölfeck / Kappe = 12 für 20 Größen; Zeichnung: Kappe 1, Zwölfeck 12"

def figur(ax, loesung=False):
    E = bau()
    flaeche(ax, E[:4], HELLBLAU, kontur=False)
    zug(ax, E); linie(ax, E[0], E[3])
    for p in (E[0], E[3]): punkt(ax, p)
    zahl(ax, (0, (E[0][1] + E[1][1]) / 2 + 0.03), "1", groesse=34)
    if loesung:
        for k in range(4):
            hilfslinie(ax, (0, 0), E[k])
        rechter_winkel(ax, (0, 0), E[0], E[3], groesse=3.5)
        winkel(ax, (0, 0), E[1], E[2], "30°", r=12, groesse=17, text_abstand=1.6)
        punkt(ax, (0, 0), "rot")
        an_strecke(ax, (0, 0), E[0], "R", seite=1, abstand=3, groesse=24, drehen=False)
