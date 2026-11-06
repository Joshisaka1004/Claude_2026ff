# Regelmäßiges Sechseck mit Inkreis; Tangente schneidet an einer Ecke 8 und 7 ab: Seite = 8 + 7 + 13 = 28.
import math
from _basis import *

NR, KURZ = 28, "sechseck-tangente"
TITEL = {"de": [("x = ?", TINTE)], "en": [("x = ?", TINTE)]}
ZEILE = {"de": None, "en": None}
STICHWORT = {"de": "regelmäßiges Sechseck", "en": "regular hexagon"}
ANTWORT = {"de": [("x = 28", TINTE)], "en": [("x = 28", TINTE)]}
SCHRITTE = {
    "de": ["Von einem Punkt aus sind die zwei Tangenten an einen Kreis gleich lang. Darum ist der Umfang des gelben Dreiecks so lang wie die zwei halben Sechseckseiten bis zu den Berührpunkten: Umfang = x.",
           "Die dritte Seite des gelben Dreiecks: Der Winkel an der Sechseck-Ecke ist 120°. Damit ist sie √(8² + 7² + 8 · 7) = √169 = 13.",
           "x = 8 + 7 + 13 = 28."],
    "en": ["From one point, the two tangents to a circle are equally long. So the perimeter of the yellow triangle equals the two half sides up to the touching points: perimeter = x.",
           "The third side of the yellow triangle: the angle at the hexagon corner is 120°. So it is √(8² + 7² + 8 · 7) = √169 = 13.",
           "x = 8 + 7 + 13 = 28."],
}
SEITE = 28.0

def bau(s=SEITE, a=8.0, b=7.0):
    E = regelmaessiges_vieleck((0, 0), s, 6, 90)       # Ecken, E[0] oben
    V, V1, V2 = E[0], E[5], E[1]                       # V1 rechts davon, V2 links davon
    u1 = ((V1[0]-V[0])/s, (V1[1]-V[1])/s); u2 = ((V2[0]-V[0])/s, (V2[1]-V[1])/s)
    X = (V[0] + a*u1[0], V[1] + a*u1[1]); Y = (V[0] + b*u2[0], V[1] + b*u2[1])
    return E, X, Y

def pruefen():
    E, X, Y = bau()
    ri = SEITE*math.sqrt(3)/2
    # Abstand Mittelpunkt–Gerade XY = Inkreisradius → wirklich Tangente
    d = abs((Y[0]-X[0])*(0-X[1]) - (Y[1]-X[1])*(0-X[0])) / math.hypot(Y[0]-X[0], Y[1]-X[1])
    assert abs(d - ri) < 1e-9
    assert abs(math.hypot(Y[0]-X[0], Y[1]-X[1]) - 13) < 1e-9
    # Eindeutigkeit: Abstand minus Inkreisradius wechselt für x in (10, 40) nur einmal das Vorzeichen
    def g(sx):
        E2, X2, Y2 = bau(sx)
        d = abs((Y2[0]-X2[0])*(0-X2[1]) - (Y2[1]-X2[1])*(0-X2[0])) / math.hypot(Y2[0]-X2[0], Y2[1]-X2[1])
        return d - sx*math.sqrt(3)/2
    werte = [g(16.01 + k/100) for k in range(4400)]
    wechsel = sum(1 for u, v in zip(werte, werte[1:]) if (u < 0 <= v) or (u > 0 >= v))
    assert wechsel == 1 and abs(g(28.0)) < 1e-9
    return "Tangente bei x = 28 bestätigt, dritte Seite 13, einzige Lösung für x zwischen 16 und 60"

def figur(ax, loesung=False):
    E, X, Y = bau()
    V = E[0]
    flaeche(ax, [V, X, Y], GELB, kontur=False)
    ri = SEITE*math.sqrt(3)/2
    kreis(ax, (0, 0), ri)
    zug(ax, E)
    # Gerade XY etwas über die Endpunkte hinaus ist nicht nötig – Strecke reicht
    linie(ax, X, Y)
    for p in (X, Y): punkt(ax, p)
    # Berührpunkt der Tangente = Fußpunkt des Lotes vom Mittelpunkt
    dx, dy = Y[0]-X[0], Y[1]-X[1]; L2 = dx*dx + dy*dy
    t = ((0-X[0])*dx + (0-X[1])*dy) / L2
    Tb = (X[0] + t*dx, X[1] + t*dy)
    punkt(ax, Tb)
    an_strecke(ax, V, X, "8", seite=1, abstand=5, groesse=30, drehen=False)
    an_strecke(ax, Y, V, "7", seite=1, abstand=5, groesse=30, drehen=False)
    an_strecke(ax, E[3], E[2], "x", seite=-1, abstand=4.5, groesse=30)
    linie(ax, E[2], E[3], farbe=ROT_TXT, lw=LW*1.6)
    if loesung:
        M1 = ((V[0]+E[5][0])/2, (V[1]+E[5][1])/2); M2 = ((V[0]+E[1][0])/2, (V[1]+E[1][1])/2)
        for m in (M1, M2): punkt(ax, m)
        hilfslinie(ax, (0, 0), M1); hilfslinie(ax, (0, 0), M2); hilfslinie(ax, (0, 0), Tb)
