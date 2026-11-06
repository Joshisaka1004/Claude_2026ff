# Gleichseitiges Dreieck ABC im Umkreis, P auf dem Bogen BC; PB, PC bis X, Y verlängert mit PX = PY = PA:
# Viereck BXYC = Dreieck ABC (van Schooten + 120°-Flächen).
import math, random
from _basis import *
from _geo import abst, flaeche as fl, buchstabe

NR, KURZ = 37, "kreis-dreieck"
TITEL = {"de": [("Gelb", GOLD_TXT), (" : ", TINTE), ("Blau", BLAU_TXT), (" = ?", TINTE)],
         "en": [("Yellow", GOLD_TXT), (" : ", TINTE), ("Blue", BLAU_TXT), (" = ?", TINTE)]}
ZEILE = {"de": None, "en": None}
STICHWORT = {"de": "gleichseitiges Dreieck", "en": "equilateral triangle"}
ANTWORT = {"de": [("Gelb", GOLD_TXT), (" : ", TINTE), ("Blau", BLAU_TXT), (" = 1 : 1", TINTE)],
           "en": [("Yellow", GOLD_TXT), (" : ", TINTE), ("Blue", BLAU_TXT), (" = 1 : 1", TINTE)]}
SCHRITTE = {
    "de": ["Der graue Bogen um P zeigt: PX = PA = PY. Der Winkel APB ist 60° (Umfangswinkel über AB). Mit PA = PX ist das Dreieck APX also gleichseitig.",
           "Dreht man um A um 60°, wandert C auf B und P auf X. Darum ist BX = PC. Genauso ist CY = PB, also PA = PB + PC.",
           "Gelb = Dreieck PXY − Dreieck PBC. Beide haben bei P den Winkel 120°. Ein solches Dreieck mit den Seiten u und v hat die Fläche √3/4 · u · v.",
           "Gelb = √3/4 · ((PB + PC)² − PB · PC) = √3/4 · (PB² + PB · PC + PC²) = √3/4 · BC² (Kosinussatz mit 120°) – genau die Fläche von Blau.",
           "Gelb : Blau = 1 : 1, egal wo P auf dem Bogen liegt."],
    "en": ["The grey arc around P shows: PX = PA = PY. Angle APB is 60° (inscribed angle on AB). With PA = PX, triangle APX is equilateral.",
           "Turn by 60° around A: C goes to B and P goes to X. So BX = PC. In the same way CY = PB, so PA = PB + PC.",
           "Yellow = triangle PXY − triangle PBC. Both have a 120° angle at P. Such a triangle with sides u and v has area √3/4 · u · v.",
           "Yellow = √3/4 · ((PB + PC)² − PB · PC) = √3/4 · (PB² + PB · PC + PC²) = √3/4 · BC² (cosine rule with 120°) – exactly the area of blue.",
           "Yellow : Blue = 1 : 1, wherever P lies on the arc."],
}

def bau(w=math.radians(252), R=3.0):
    A = (0.0, R); B = (R*math.cos(math.radians(210)), R*math.sin(math.radians(210)))
    C = (R*math.cos(math.radians(330)), R*math.sin(math.radians(330)))
    P = (R*math.cos(w), R*math.sin(w)); pa = abst(P, A)
    X = (P[0] + (B[0]-P[0])*pa/abst(P, B), P[1] + (B[1]-P[1])*pa/abst(P, B))
    Y = (P[0] + (C[0]-P[0])*pa/abst(P, C), P[1] + (C[1]-P[1])*pa/abst(P, C))
    return A, B, C, P, X, Y, R

def pruefen():
    for _ in range(40):
        A, B, C, P, X, Y, R = bau(math.radians(random.uniform(212, 328)), random.uniform(0.5, 20))
        assert abs(fl(B, X, Y, C) / fl(A, B, C) - 1) < 1e-9
        assert abs(abst(B, X) - abst(P, C)) < 1e-9
    return "Gelb = Blau für 40 zufällige Lagen von P und Größen; BX = PC bestätigt"

def figur(ax, loesung=False):
    A, B, C, P, X, Y, R = bau()
    from shapely.geometry import Polygon as SP
    gelb, blau = SP([B, X, Y, C]), SP([A, B, C])
    bereich(ax, gelb.difference(blau), GELB)
    bereich(ax, blau.difference(gelb), HELLBLAU)
    bereich(ax, gelb.intersection(blau), HELLBLAU, schraffur="/", schraffur_farbe=GOLD)
    kreis(ax, (0, 0), R)
    zug(ax, [A, B, C]); zug(ax, [B, X, Y, C]); linie(ax, P, X); linie(ax, P, Y); linie(ax, P, A, lw=2.4)
    # Zirkelbogen um P durch X, A, Y: zeigt PX = PA = PY
    wx = math.degrees(math.atan2(X[1]-P[1], X[0]-P[0])); wy = math.degrees(math.atan2(Y[1]-P[1], Y[0]-P[0]))
    from matplotlib.patches import Arc
    pa = abst(P, A)
    ax.add_patch(Arc(P, 2*pa, 2*pa, theta1=wy - 4, theta2=wx + 4, edgecolor=GRAU, lw=1.8, zorder=5))
    strich(ax, A, B, 2, t=0.4); strich(ax, B, C, 2, t=0.22); strich(ax, C, A, 2, t=0.6)
    for p in (A, B, C, X, Y): punkt(ax, p)
    punkt(ax, P, "rot")
    if loesung:
        hilfslinie(ax, A, X)
        winkel(ax, P, Y, X, "120°", r=6, groesse=17, text_abstand=1.9)
        for p, t, dx, dy in ((A, "A", 0, 0.38), (B, "B", -0.32, -0.25), (C, "C", 0.32, -0.25), (P, "P", 0, -0.4),
                             (X, "X", -0.32, 0.1), (Y, "Y", 0.32, 0.1)):
            buchstabe(ax, p, t, dx, dy)
