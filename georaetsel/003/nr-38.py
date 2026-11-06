# 3-4-5-Dreieck mit Inkreismittelpunkt I; P beliebig auf der Hypotenuse; Kreise durch A, I, P und B, I, P:
# R : r = AI : BI = √10 : √5 = √2 : 1.
import math, random
from _basis import *
from _geo import abst, inkreis, umkreis, fuss, buchstabe

NR, KURZ = 38, "zwei-kreise-inkreis"
TITEL = {"de": [("R : r = ?", TINTE)], "en": [("R : r = ?", TINTE)]}
ZEILE = {"de": None, "en": None}
STICHWORT = {"de": "I = Mittelpunkt des Inkreises", "en": "I = centre of the incircle"}
ANTWORT = {"de": [("R : r = √2 : 1", TINTE)], "en": [("R : r = √2 : 1", TINTE)]}
SCHRITTE = {
    "de": ["Beide Kreise gehen durch I und P – sie haben dieselbe Sehne IP. Über dieser Sehne sieht man von A aus den halben Winkel bei A, von B aus den halben Winkel bei B (I liegt auf den Winkelhalbierenden).",
           "Gleiche Sehne: Der Radius hängt nur von diesem Winkel ab. Darum ist R : r für jede Lage von P gleich.",
           "Also darf P auf den Berührpunkt T des Inkreises rücken (gestrichelt). Dann ist der Winkel bei T ein rechter, und AI bzw. BI sind Durchmesser (Thales).",
           "Inkreis: Radius (3 + 4 − 5) : 2 = 1, Tangentenstücke 3 und 2. AI = √(3² + 1²) = √10, BI = √(2² + 1²) = √5.",
           "R : r = √10 : √5 = √2 : 1."],
    "en": ["Both circles pass through I and P – they share the chord IP. From A this chord is seen under half the angle at A, from B under half the angle at B (I lies on the angle bisectors).",
           "Same chord: the radius only depends on this angle. So R : r is the same for every position of P.",
           "So P may move onto the touching point T of the incircle (dashed). Then the angle at T is a right angle, and AI and BI are diameters (Thales).",
           "Incircle: radius (3 + 4 − 5) : 2 = 1, tangent pieces 3 and 2. AI = √(3² + 1²) = √10, BI = √(2² + 1²) = √5.",
           "R : r = √10 : √5 = √2 : 1."],
}
C, A, B = (0.0, 0.0), (4.0, 0.0), (0.0, 3.0)
I, RI = inkreis(A, B, C)

def bau(t=0.89):
    P = (A[0] + t*(B[0]-A[0]), A[1] + t*(B[1]-A[1]))
    return P, umkreis(A, I, P), umkreis(B, I, P)

def pruefen():
    assert abs(RI - 1) < 1e-12 and abs(I[0] - 1) < 1e-12 and abs(I[1] - 1) < 1e-12
    for _ in range(40):
        P, (m1, R1), (m2, R2) = bau(random.uniform(0.03, 0.97))
        assert abs(R1 / R2 - math.sqrt(2)) < 1e-9
    return "R : r = √2 für 40 zufällige Lagen von P; Inkreis (1, 1) mit Radius 1"

def figur(ax, loesung=False):
    P, (m1, R1), (m2, R2) = bau()
    from matplotlib.patches import Circle
    flaeche(ax, [A, B, C], GELB, kontur=False)
    ax.add_patch(Circle(m1, R1, facecolor=TUERKIS, alpha=0.22, edgecolor="none", zorder=2))
    ax.add_patch(Circle(m2, R2, facecolor=VIOLETT, alpha=0.25, edgecolor="none", zorder=2))
    kreis(ax, m1, R1, z=4); kreis(ax, m2, R2, z=4)
    zug(ax, [A, B, C])
    kreis(ax, I, RI, lw=2.6, farbe=WEISS, z=3)
    rechter_winkel(ax, C, A, B, groesse=3.5)
    masslinie(ax, C, A, "4", seite=-1, abstand=7)
    masslinie(ax, B, C, "3", seite=-1, abstand=42)
    for m, rr, w, t in ((m1, R1, -25, "R"), (m2, R2, 160, "r")):
        e = (m[0] + rr*math.cos(math.radians(w)), m[1] + rr*math.sin(math.radians(w)))
        linie(ax, m, e, lw=2.2, farbe=GESUCHT, z=6); punkt(ax, m, "rot")
        zahl(ax, ((m[0]+e[0])/2 + 0.0, (m[1]+e[1])/2 + 0.22), t, farbe=GESUCHT, groesse=28)
    punkt(ax, I, "rot"); punkt(ax, P); punkt(ax, A); punkt(ax, B)
    if loesung:
        T = fuss(I, A, B)
        kreis_r = RI
        from matplotlib.patches import Circle as C2
        hilfslinie(ax, A, I); hilfslinie(ax, B, I); hilfslinie(ax, I, T)
        punkt(ax, T)
        for p, s, dx, dy in ((A, "A", 0.2, -0.25), (B, "B", -0.25, 0.15), (C, "C", -0.25, -0.25),
                             (I, "I", -0.25, 0.12), (P, "P", 0.28, 0.12), (T, "T", 0.22, 0.25)):
            buchstabe(ax, p, s, dx, dy)
    else:
        buchstabe(ax, I, "I", 0.28, 0.32, groesse=26)
