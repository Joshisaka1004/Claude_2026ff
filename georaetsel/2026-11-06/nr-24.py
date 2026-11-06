# Regelmäßiges Achteck: Rechteck aus zwei gegenüberliegenden Seiten = halbes Achteck = 2 · seitliches Stück.
import math, random
from _basis import *
from shapely.geometry import Polygon as SP

NR, KURZ = 24, "achteck"
TITEL = {"de": [("Grün", GRUEN_TXT), (" = ?", TINTE)], "en": [("Green", GRUEN_TXT), (" = ?", TINTE)]}
ZEILE = {"de": None, "en": None}
STICHWORT = {"de": "regelmäßiges Achteck", "en": "regular octagon"}
ANTWORT = {"de": [("Grün", GRUEN_TXT), (" = 14", TINTE)], "en": [("Green", GRUEN_TXT), (" = 14", TINTE)]}
SCHRITTE = {
    "de": ["Zwei waagerechte Hilfslinien zerlegen alles in Streifen, Ecken und ein Quadrat in der Mitte.",
           "Links (7): ein gelber Streifen und zwei orange Ecken. Die zwei Ecken sind zusammen genau ein halbes violettes Quadrat.",
           "Grün: zwei gelbe Streifen und ein ganzes violettes Quadrat. Das ist doppelt so viel wie links.",
           "Grün = 2 · 7 = 14."],
    "en": ["Two horizontal helper lines cut everything into strips, corners and a square in the middle.",
           "Left (7): one yellow strip and two orange corners. Together the two corners are exactly half of the purple square.",
           "Green: two yellow strips and one whole purple square. That is twice the left part.",
           "Green = 2 · 7 = 14."],
}

def bau(links=7.0):
    E = regelmaessiges_vieleck((0, 0), 1.0, 8, 67.5)     # Ecken ab rechts oben; obere Seite waagerecht
    # E[0]=rechts oben (oben), E[1]=links oben (oben), E[2],E[3] links, E[4],E[5] unten, E[6],E[7] rechts
    T = SP([E[1], E[2], E[3], E[4]]).area
    k = math.sqrt(links / T)
    return [(x*k, y*k) for x, y in E]

def pruefen():
    for _ in range(10):
        l = random.uniform(1, 100); E = bau(l)
        assert abs(SP([E[1], E[2], E[3], E[4]]).area - l) < 1e-9
        assert abs(SP([E[0], E[1], E[4], E[5]]).area - 2*l) < 1e-9
    E = bau()
    assert abs(E[1][0] - E[4][0]) < 1e-12                 # die Linien sind wirklich senkrecht
    return "Rechteck = 2 · seitliches Stück für 10 zufällige Größen; Zeichnung: links 7, grün 14"

def figur(ax, loesung=False):
    E = bau()
    flaeche(ax, [E[0], E[1], E[4], E[5]], GRUEN, kontur=False)
    flaeche(ax, [E[1], E[2], E[3], E[4]], HELLBLAU, kontur=False)
    if loesung:
        xl, yo, yu = E[1][0], E[2][1], E[3][1]
        xr = E[0][0]
        flaeche(ax, [(E[2][0], yo), (xl, yo), (xl, yu), (E[3][0], yu)], GELB, kontur=False)
        flaeche(ax, [E[1], E[2], (xl, yo)], ORANGE, kontur=False)
        flaeche(ax, [E[4], E[3], (xl, yu)], ORANGE, kontur=False)
        flaeche(ax, [(xl, yo), (xr, yo), E[0], E[1]], GELB, kontur=False)
        flaeche(ax, [(xl, yu), (xr, yu), E[5], E[4]], GELB, kontur=False)
        flaeche(ax, [(xl, yo), (xr, yo), (xr, yu), (xl, yu)], VIOLETT, kontur=False)
        hilfslinie(ax, E[2], E[7]); hilfslinie(ax, E[3], E[6])
    zug(ax, E)
    linie(ax, E[1], E[4]); linie(ax, E[0], E[5])
    if not loesung:
        zahl(ax, ((E[1][0]+E[2][0])/2, 0), "7")
        zahl(ax, (0, 0), "?", farbe=GRUEN_TXT, groesse=48)
    else:
        zahl(ax, ((E[1][0]+E[2][0])/2, 0), "7", groesse=30)
