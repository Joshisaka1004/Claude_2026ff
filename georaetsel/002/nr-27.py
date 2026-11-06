# Quadrat ABCD, P beliebig auf CD, Quadrat über AP nach außen mit Ecke Q: Dreieck ACQ = Quadrat ABCD.
import random
from _basis import *

NR, KURZ = 27, "gleitendes-quadrat"
TITEL = {"de": [("Gelb", GOLD_TXT), (" = ?", TINTE)], "en": [("Yellow", GOLD_TXT), (" = ?", TINTE)]}
ZEILE = {"de": None, "en": None}
STICHWORT = {"de": "zwei Quadrate", "en": "two squares"}
ANTWORT = {"de": [("Gelb", GOLD_TXT), (" = 16", TINTE)], "en": [("Yellow", GOLD_TXT), (" = 16", TINTE)]}
SCHRITTE = {
    "de": ["Schiebt man den Punkt auf der oberen Seite ein Stück nach rechts, rückt die Spitze von Gelb um dasselbe Stück nach rechts UND nach oben – denn das zweite Quadrat ist um 90° gedreht.",
           "Die Spitze wandert also auf einer Geraden parallel zur Diagonale (gestrichelt). Gleiche Grundseite, gleiche Höhe: Gelb bleibt immer gleich groß.",
           "Schiebe den Punkt ganz nach links in die Ecke. Dann ist Gelb ein halbes Rechteck mit 8 mal 4.",
           "Gelb = 8 · 4 : 2 = 16 – so groß wie das Quadrat."],
    "en": ["Slide the point on the top side a little to the right: the tip of yellow moves the same distance to the right AND up – because the second square is turned by 90°.",
           "So the tip moves on a line parallel to the diagonal (dashed). Same base, same height: yellow always has the same area.",
           "Slide the point all the way left into the corner. Then yellow is half of an 8 by 4 rectangle.",
           "Yellow = 8 · 4 : 2 = 16 – the same as the square."],
}
S, T = 4.0, 1.4

def bau(s=S, t=T):
    A, B, C, D = (0, 0), (s, 0), (s, s), (0, s)
    P = (t, s); Q = (t - s, s + t); R = (-s, t)
    return A, B, C, D, P, Q, R

def flaeche3(a, b, c):
    return abs((b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])) / 2

def pruefen():
    for _ in range(40):
        s = random.uniform(0.5, 20); t = random.uniform(0, s)
        A, B, C, D, P, Q, R = bau(s, t)
        # Q ist wirklich die Ecke des Quadrats über AP (AP ⟂ PQ, gleich lang)
        assert abs((P[0]-A[0])*(Q[0]-P[0]) + (P[1]-A[1])*(Q[1]-P[1])) < 1e-9
        assert abs(flaeche3(A, C, Q) - s*s) < 1e-9
    return "Gelb = Quadratfläche für 40 zufällige Größen und Lagen von P"

def figur(ax, loesung=False):
    A, B, C, D, P, Q, R = bau()
    flaeche(ax, [A, C, Q], GELB, kontur=False)
    zug(ax, [A, B, C, D]); zug(ax, [A, P, Q, R])
    zug(ax, [A, C, Q])
    for p in (P, Q): punkt(ax, p)
    masslinie(ax, A, B, "4", seite=-1, abstand=5)
    if loesung:
        Q2 = (-S, S)
        hilfslinie(ax, (Q[0] - 2.2, Q[1] - 2.2), (Q[0] + 1.6, Q[1] + 1.6))
        hilfslinie(ax, A, Q2); hilfslinie(ax, Q2, C); hilfslinie(ax, D, Q2)
        punkt(ax, Q2)
    else:
        zahl(ax, (-0.45, 3.2), "?", farbe=GOLD_TXT, groesse=46)
