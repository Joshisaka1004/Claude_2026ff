# Halbkreis über AB = 6, P auf dem Bogen, Quadrate über AP und PB nach außen; Q, T = äußere Ecken an P; U = höchster Punkt.
# Dreieck QTU = 9, egal wo P liegt (QT = AB, Höhe von U über QT = Radius).
import math, random
from _basis import *
from _geo import drehe, flaeche as fl, abst, buchstabe

NR, KURZ = 35, "halbkreis-quadrate"
TITEL = {"de": [("Gelb", GOLD_TXT), (" = ?", TINTE)], "en": [("Yellow", GOLD_TXT), (" = ?", TINTE)]}
ZEILE = {"de": None, "en": None}
STICHWORT = {"de": "Halbkreis und zwei Quadrate", "en": "semicircle and two squares"}
ANTWORT = {"de": [("Gelb", GOLD_TXT), (" = 9", TINTE)], "en": [("Yellow", GOLD_TXT), (" = 9", TINTE)]}
SCHRITTE = {
    "de": ["Der Winkel bei P ist ein rechter (Thales). Darum liegt die Quadratecke links auf der Verlängerung von BP und die rechte auf der Verlängerung von AP.",
           "Das Dreieck aus P und den zwei Quadratecken hat also dieselben Schenkel wie das Dreieck APB, nur vertauscht. Seine lange Seite ist so lang wie AB: 6.",
           "Die Mitte M dieser Seite ist 3 von P entfernt, und eine kurze Winkeljagd zeigt: PM steht senkrecht auf AB. PM ist also eine Kopie des Radius OU – und UM eine Kopie von OP.",
           "Genau wie OP steht UM senkrecht auf der langen Seite. Gelb hat also die Grundseite 6 und die Höhe 3: Gelb = 6 · 3 : 2 = 9 – egal, wo P liegt."],
    "en": ["The angle at P is a right angle (Thales). So the left square corner lies on the extension of BP and the right one on the extension of AP.",
           "So the triangle made of P and the two square corners has the same legs as triangle APB, just swapped. Its long side is as long as AB: 6.",
           "The midpoint M of this side is 3 away from P, and a short angle chase shows: PM is perpendicular to AB. So PM is a copy of the radius OU – and UM a copy of OP.",
           "Just like OP, UM is perpendicular to the long side. So yellow has base 6 and height 3: yellow = 6 · 3 : 2 = 9 – wherever P is."],
}
R = 3.0

def bau(w=math.radians(122), r=R):
    A, B, O, U = (-r, 0.0), (r, 0.0), (0.0, 0.0), (0.0, r)
    P = (r*math.cos(w), r*math.sin(w))
    Q = drehe(A, P, -math.pi/2); S1 = (A[0] + Q[0] - P[0], A[1] + Q[1] - P[1])
    T = drehe(B, P, math.pi/2);  S2 = (B[0] + T[0] - P[0], B[1] + T[1] - P[1])
    return A, B, O, U, P, Q, S1, T, S2

def pruefen():
    for _ in range(40):
        r = random.uniform(0.5, 20); w = random.uniform(0.05, math.pi - 0.05)
        A, B, O, U, P, Q, S1, T, S2 = bau(w, r)
        assert abs(fl(Q, T, U) - r*r) < 1e-9 and abs(abst(Q, T) - 2*r) < 1e-9
    A, B, O, U, P, Q, S1, T, S2 = bau()
    assert abs(fl(Q, T, U) - 9) < 1e-12
    return "Gelb = Radius² = 9 für 40 zufällige Lagen und Größen; QT = AB"

def figur(ax, loesung=False):
    A, B, O, U, P, Q, S1, T, S2 = bau()
    halb = kreisflaeche(O, R) & __import__("shapely.geometry", fromlist=["box"]).box(-R, 0, R, R)
    bereich(ax, halb, HELLGELB)
    flaeche(ax, [A, P, Q, S1], HELLBLAU, kontur=False)
    flaeche(ax, [P, B, S2, T], VIOLETT, kontur=False)
    flaeche(ax, [Q, T, U], GELB, kontur=False, z=2)
    bogen(ax, O, R, 0, 180); linie(ax, A, B)
    zug(ax, [A, P, Q, S1]); zug(ax, [P, B, S2, T]); zug(ax, [Q, T, U])
    linie(ax, O, U, lw=2.4); rechter_winkel(ax, O, B, U, groesse=3)
    punkt(ax, O, "rot")
    for p in (A, B, P, Q, T, U): punkt(ax, p)
    masslinie(ax, A, B, "6", seite=-1, abstand=5)
    if loesung:
        M = ((Q[0] + T[0])/2, (Q[1] + T[1])/2)
        hilfslinie(ax, P, M); hilfslinie(ax, U, M); hilfslinie(ax, O, P)
        hilfslinie(ax, B, P); hilfslinie(ax, A, P)
        rechter_winkel(ax, M, U, T, groesse=3)
        punkt(ax, M)
        for p, t, dx, dy in ((A, "A", -0.3, -0.3), (B, "B", 0.3, -0.3), (O, "O", -0.3, -0.35), (U, "U", 0.32, 0.25),
                             (P, "P", -0.35, -0.1), (M, "M", -0.35, 0.2)):
            buchstabe(ax, p, t, dx, dy)
        zahl(ax, ((Q[0]+T[0]+U[0])/3 + 0.75, (Q[1]+T[1]+U[1])/3 + 0.35), "9", farbe=GOLD_TXT, groesse=40)
    else:
        zahl(ax, ((Q[0]+T[0]+U[0])/3, (Q[1]+T[1]+U[1])/3 + 0.2), "?", farbe=GOLD_TXT, groesse=46)
