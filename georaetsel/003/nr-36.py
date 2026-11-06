# Raute mit 60°, Inkreis, Tangente schneidet an der spitzen Ecke A ab (X auf AB, Y auf AD):
# Dreieck CXY : Raute = 3 : 8, egal wo die Tangente liegt.
import math, random
from _basis import *
from _geo import fuss, abst, flaeche as fl, buchstabe, schnitt

NR, KURZ = 36, "raute-tangente"
TITEL = {"de": [("Grün", GRUEN_TXT), (" : Raute = ?", TINTE)], "en": [("Green", GRUEN_TXT), (" : rhombus = ?", TINTE)]}
ZEILE = {"de": None, "en": None}
STICHWORT = {"de": "Raute mit Inkreis", "en": "rhombus with incircle"}
ANTWORT = {"de": [("Grün", GRUEN_TXT), (" : Raute = 3 : 8", TINTE)], "en": [("Green", GRUEN_TXT), (" : rhombus = 3 : 8", TINTE)]}
SCHRITTE = {
    "de": ["C ist das Spiegelbild von A am Mittelpunkt O. Liegt A um h vor der Tangente, liegt C um 2r + h dahinter. Also: Grün = XY · (2r + h) : 2 = XY · r + Dreieck AXY.",
           "Der Kreis berührt das Eckdreieck AXY von außen. Dann gilt: Fläche AXY = r · (halber Umfang − XY). Wegen der gleich langen Tangentenstücke ist der halbe Umfang genau AT.",
           "Zusammen: Grün = r · AT – so groß wie das Drachenviereck aus A, den zwei Berührpunkten und O. Wo die Tangente liegt, ist egal.",
           "In der 60°-Raute mit Seite a ist AT = ¾ a und r = √3/4 · a. Drachen = 3√3/16 · a², Raute = √3/2 · a². Grün : Raute = 3 : 8."],
    "en": ["C is the mirror image of A in the centre O. If A lies h in front of the tangent, C lies 2r + h behind it. So: green = XY · (2r + h) : 2 = XY · r + triangle AXY.",
           "The circle touches the corner triangle AXY from outside. Then: area AXY = r · (half perimeter − XY). Because the tangent pieces are equal, the half perimeter is exactly AT.",
           "Together: green = r · AT – as big as the kite made of A, the two touching points and O. Where the tangent lies does not matter.",
           "In the 60° rhombus with side a, AT = ¾ a and r = √3/4 · a. Kite = 3√3/16 · a², rhombus = √3/2 · a². Green : rhombus = 3 : 8."],
}
A_ = 4.0

def bau(phi=math.radians(200), a=A_):
    A = (0.0, 0.0); B = (a, 0.0); D = (a/2, a*math.sqrt(3)/2); C = (B[0] + D[0], B[1] + D[1])
    O = (C[0]/2, C[1]/2); r = a*math.sqrt(3)/4
    P = (O[0] + r*math.cos(phi), O[1] + r*math.sin(phi))
    t = (-math.sin(phi), math.cos(phi))
    X = schnitt(P, (P[0] + t[0], P[1] + t[1]), A, B); Y = schnitt(P, (P[0] + t[0], P[1] + t[1]), A, D)
    return A, B, C, D, O, r, P, X, Y

def pruefen():
    n = 0
    for _ in range(200):
        a = random.uniform(0.5, 20); phi = math.radians(random.uniform(185, 235))
        A, B, C, D, O, r, P, X, Y = bau(phi, a)
        if not (0 < X[0] < a and 0 < abst(A, Y) < a):
            continue
        assert abs(fl(C, X, Y) / fl(A, B, C, D) - 3/8) < 1e-9
        n += 1
    assert n >= 30
    return f"Grün : Raute = 3 : 8 für {n} zufällige Tangenten und Größen"

def figur(ax, loesung=False):
    A, B, C, D, O, r, P, X, Y = bau()
    flaeche(ax, [A, B, C, D], HELLBLAU, kontur=False)
    kreis(ax, O, r, farbe=WEISS)
    flaeche(ax, [C, X, Y], GRUEN, kontur=False, z=3)
    zug(ax, [A, B, C, D]); kreis(ax, O, r, z=4); zug(ax, [C, X, Y])
    for p, q in ((A, B), (B, C), (C, D), (D, A)): strich(ax, p, q)
    winkel(ax, A, B, D, "60°", r=9, groesse=20, text_abstand=1.7)
    punkt(ax, O, "rot")
    for p in (P, X, Y): punkt(ax, p)
    if loesung:
        T1 = fuss(O, A, B); T2 = fuss(O, A, D)
        flaeche(ax, [A, T1, O, T2], GELB, kontur=False, z=2)
        hilfslinie(ax, O, T1); hilfslinie(ax, O, T2); hilfslinie(ax, A, O)
        for p in (T1, T2): punkt(ax, p)
        for p, t, dx, dy in ((A, "A", -0.25, -0.2), (C, "C", 0.25, 0.2), (O, "O", 0.0, 0.3), (T1, "T", 0.0, -0.3),
                             (X, "X", 0.15, -0.3), (Y, "Y", -0.3, 0.1)):
            buchstabe(ax, p, t, dx, dy)
    else:
        zahl(ax, ((C[0] + X[0] + Y[0])/3 + 0.75, (C[1] + X[1] + Y[1])/3 + 0.05), "?", farbe=GRUEN_TXT, groesse=40, z=7)
