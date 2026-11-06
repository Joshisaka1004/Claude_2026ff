# Quadrat, P auf BC, Lot von A auf DP: AF = 4, DP = 5 → Quadrat 20 → Viereck ABPF = 11.
import math, random
from _basis import *
from _geo import fuss, flaeche as fl, abst

NR, KURZ = 31, "quadrat-lot"
TITEL = {"de": [("Grün", GRUEN_TXT), (" = ?", TINTE)], "en": [("Green", GRUEN_TXT), (" = ?", TINTE)]}
ZEILE = {"de": None, "en": None}
STICHWORT = {"de": "Quadrat", "en": "square"}
ANTWORT = {"de": [("Grün", GRUEN_TXT), (" = 11", TINTE)], "en": [("Green", GRUEN_TXT), (" = 11", TINTE)]}
SCHRITTE = {
    "de": ["Das Dreieck aus der linken Seite und dem Punkt rechts ist genau ein halbes Quadrat (Grundseite = Seite, Höhe = Seite).",
           "Mit der schrägen Seite 5 als Grundseite ist seine Höhe 4: Fläche 5 · 4 : 2 = 10. Das Quadrat hat also die Fläche 20.",
           "Links fehlt Grün das Dreieck mit den Seiten 4 und 2 (Pythagoras: 20 − 16 = 4 = 2²). Fläche 4 · 2 : 2 = 4.",
           "Oben rechts fehlt das Dreieck mit der langen Seite 5. Pythagoras gibt seine kurze Seite: √(25 − 20) = √5. Fläche √20 · √5 : 2 = 10 : 2 = 5.",
           "Grün = 20 − 4 − 5 = 11."],
    "en": ["The triangle made of the left side and the point on the right is exactly half the square (base = side, height = side).",
           "Taking the slanted side 5 as base, its height is 4: area 5 · 4 : 2 = 10. So the square has area 20.",
           "On the left, green is missing the triangle with sides 4 and 2 (Pythagoras: 20 − 16 = 4 = 2²). Area 4 · 2 : 2 = 4.",
           "At the top right, green is missing the triangle with the long side 5. Pythagoras gives its short side: √(25 − 20) = √5. Area √20 · √5 : 2 = 10 : 2 = 5.",
           "Green = 20 − 4 − 5 = 11."],
}

def bau(af=4.0, dp=5.0):
    s = math.sqrt(af*dp)
    A, B, C, D = (0, 0), (s, 0), (s, s), (0, s)
    P = (s, s - math.sqrt(dp*dp - s*s))
    F = fuss(A, D, P)
    return A, B, C, D, P, F

def pruefen():
    # Für jedes Quadrat und jede Lage von P gilt AF · DP = Seite² (Dreieck ADP = halbes Quadrat).
    # Also legen AF = 4 und DP = 5 die Seite (√20) und dann P fest → Grün eindeutig.
    for _ in range(40):
        s = random.uniform(1, 10); p = random.uniform(0, s)
        A, B, C, D, P = (0, 0), (s, 0), (s, s), (0, s), (s, p)
        F = fuss(A, D, P)
        assert abs(abst(A, F)*abst(D, P) - s*s) < 1e-9
    A, B, C, D, P, F = bau()
    assert abs(abst(A, F) - 4) < 1e-9 and abs(abst(D, P) - 5) < 1e-9
    assert abs(fl(A, B, P, F) - 11) < 1e-9
    # F liegt zwischen D und P
    assert abs(abst(D, F) + abst(F, P) - 5) < 1e-9
    # Eindeutig: AF·DP = s² legt s fest, DP legt P fest
    return "AF · DP = Seite² → Quadrat 20, Grün = 11 (Zeichnung nachgemessen)"

def figur(ax, loesung=False):
    A, B, C, D, P, F = bau()
    flaeche(ax, [A, B, P, F], GRUEN, kontur=False)
    if loesung:
        flaeche(ax, [A, F, D], HELLBLAU, kontur=False)
        flaeche(ax, [D, C, P], HELLBLAU, kontur=False)
    zug(ax, [A, B, C, D]); linie(ax, D, P); linie(ax, A, F)
    rechter_winkel(ax, F, A, P, groesse=3)
    for p in (P, F): punkt(ax, p)
    an_strecke(ax, A, F, "4", seite=-1, abstand=3, groesse=30)
    masslinie(ax, D, P, "5", seite=1, abstand=5, groesse=30)
    if loesung:
        zahl(ax, ((A[0]+F[0]+D[0])/3, (A[1]+F[1]+D[1])/3), "4", groesse=28)
        zahl(ax, (C[0] - 0.55, C[1] - 0.5), "5", groesse=28)
        an_strecke(ax, D, F, "2", seite=-1, abstand=3, groesse=22)
        zahl(ax, ((A[0]+B[0]+P[0]+F[0])/4 + 0.3, (A[1]+B[1]+P[1]+F[1])/4 - 0.3), "11", farbe=GRUEN_TXT, groesse=30)
    else:
        zahl(ax, ((A[0]+B[0]+P[0]+F[0])/4 + 0.3, (A[1]+B[1]+P[1]+F[1])/4 - 0.3), "?", farbe=GRUEN_TXT, groesse=46)
