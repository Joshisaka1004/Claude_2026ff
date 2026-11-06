# Quadrat mit außen aufgesetztem gleichseitigem Dreieck, Spitze mit den unteren Ecken verbunden: x = 30°.
import math, random
from _basis import *

NR, KURZ = 22, "winkel"
TITEL = {"de": [("x = ?", TINTE)], "en": [("x = ?", TINTE)]}
ZEILE = {"de": None, "en": None}
STICHWORT = {"de": "Quadrat", "en": "square"}
ANTWORT = {"de": [("x = 30°", TINTE)], "en": [("x = 30°", TINTE)]}
SCHRITTE = {
    "de": ["Die linke Dreiecksseite ist so lang wie die linke Quadratseite. Das schmale Dreieck links hat also zwei gleich lange Seiten.",
           "Sein Winkel oben links ist 90° + 60° = 150°.",
           "Die zwei anderen Winkel sind gleich: (180° − 150°) : 2 = 15°. Rechts genauso.",
           "x = 60° − 15° − 15° = 30°."],
    "en": ["The left side of the triangle is as long as the left side of the square. So the thin triangle on the left has two equal sides.",
           "Its angle at the top left is 90° + 60° = 150°.",
           "The two other angles are equal: (180° − 150°) : 2 = 15°. The same on the right.",
           "x = 60° − 15° − 15° = 30°."],
}
S = 4.0
A, B, C, D = (0, 0), (S, 0), (S, S), (0, S)
E = (S/2, S + S*math.sqrt(3)/2)

def winkel_grad(e, p, q):
    v = (p[0]-e[0], p[1]-e[1]); w = (q[0]-e[0], q[1]-e[1])
    return math.degrees(math.acos((v[0]*w[0]+v[1]*w[1])/math.hypot(*v)/math.hypot(*w)))

def pruefen():
    for _ in range(20):
        s = random.uniform(0.5, 50); e = (s/2, s + s*math.sqrt(3)/2)
        assert abs(winkel_grad(e, (0, 0), (s, 0)) - 30) < 1e-9
    return "x = 30° für 20 zufällige Quadratgrößen"

def figur(ax, loesung=False):
    flaeche(ax, [D, C, E], HELLBLAU, kontur=False)
    zug(ax, [A, B, C, D]); zug(ax, [D, C, E]); linie(ax, E, A); linie(ax, E, B)
    for p, q in ((A, B), (B, C), (C, D), (D, A), (D, E), (C, E)):
        strich(ax, p, q)
    for p in (A, B, C, D, E): punkt(ax, p)
    winkel(ax, E, A, B, "x", r=16, groesse=28, text_abstand=1.5)
    if loesung:
        winkel(ax, D, A, E, "150°", r=7, groesse=19, text_abstand=2.0)
        winkel(ax, A, E, D, "15°", r=22, groesse=19, text_abstand=1.35)
        winkel(ax, E, D, A, "15°", r=26, groesse=19, text_abstand=1.25)
