# Zwei Seitenhalbierende: Viereck an der Spitze = 2 · kleines Dreieck.
import math, random
from _basis import *
from shapely.geometry import Polygon as SP

NR, KURZ = 23, "seitenmitten"
TITEL = {"de": [("Grün", GRUEN_TXT), (" = ?", TINTE)], "en": [("Green", GRUEN_TXT), (" = ?", TINTE)]}
ZEILE = {"de": "Die Zahl ist eine Fläche.", "en": "The number is an area."}
STICHWORT = {"de": None, "en": None}
ANTWORT = {"de": [("Grün", GRUEN_TXT), (" = 8", TINTE)], "en": [("Green", GRUEN_TXT), (" = 8", TINTE)]}
SCHRITTE = {
    "de": ["Zeichne die dritte Linie: von der oberen Ecke durch den Schnittpunkt zur Mitte der unteren Seite.",
           "Die drei Linien teilen das Dreieck in sechs gleich große Dreiecke. Grund: Je zwei Nachbardreiecke an einer halbierten Seite haben gleiche Grundseite und gleiche Höhe.",
           "Grün besteht aus zwei dieser Dreiecke: Grün = 2 · 4 = 8."],
    "en": ["Draw the third line: from the top corner through the crossing point to the middle of the bottom side.",
           "The three lines cut the triangle into six triangles of equal area. Reason: two neighbouring triangles on a halved side have the same base and the same height.",
           "Green is made of two of these triangles: green = 2 · 4 = 8."],
}

def bau(A=(1.6, 5.0), B=(0.0, 0.0), C=(7.0, 0.0)):
    F = ((A[0]+B[0])/2, (A[1]+B[1])/2); E = ((A[0]+C[0])/2, (A[1]+C[1])/2)
    G = ((A[0]+B[0]+C[0])/3, (A[1]+B[1]+C[1])/3)
    k = math.sqrt(4/SP([B, G, F]).area)                # so skalieren, dass das kleine Dreieck 4 ist
    sk = lambda p: (p[0]*k, p[1]*k)
    return [sk(p) for p in (A, B, C, F, E, G)]

def pruefen():
    for _ in range(40):
        A = (random.uniform(-5, 10), random.uniform(1, 10)); C = (random.uniform(1, 10), 0)
        A, B, C, F, E, G = bau(A, (0, 0), C)
        assert abs(SP([B, G, F]).area - 4) < 1e-9 and abs(SP([A, F, G, E]).area - 8) < 1e-9
    A, B, C, F, E, G = bau()
    # G liegt wirklich auf beiden Linien
    cross = lambda p, q, r: (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
    assert abs(cross(B, E, G)) < 1e-9 and abs(cross(C, F, G)) < 1e-9
    return "Grün = 8 für 40 zufällige Dreiecke"

def figur(ax, loesung=False):
    A, B, C, F, E, G = bau()
    if loesung:
        M = ((B[0]+C[0])/2, 0)
        flaeche(ax, [A, F, G, E], GRUEN, kontur=False)
        flaeche(ax, [B, G, F], HELLBLAU, kontur=False)
    else:
        flaeche(ax, [A, F, G, E], GRUEN, kontur=False)
        flaeche(ax, [B, G, F], HELLBLAU, kontur=False)
    zug(ax, [A, B, C]); linie(ax, B, E); linie(ax, C, F)
    strich(ax, A, F); strich(ax, F, B); strich(ax, A, E, 2); strich(ax, E, C, 2)
    for p in (F, E, G): punkt(ax, p)
    c = lambda *ps: (sum(p[0] for p in ps)/len(ps), sum(p[1] for p in ps)/len(ps))
    zahl(ax, c(B, G, F), "4", groesse=34)
    if loesung:
        hilfslinie(ax, A, M); punkt(ax, M)
        strich(ax, B, M, 3); strich(ax, M, C, 3)
        for tri in ((A, F, G), (A, G, E), (G, E, C), (G, C, M), (G, M, B)):
            zahl(ax, c(*tri), "4", groesse=30)
    else:
        zahl(ax, c(A, F, G, E), "?", farbe=GRUEN_TXT, groesse=44)
