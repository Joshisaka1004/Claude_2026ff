# Trapez, durch eine Parallele in zwei Teiltrapeze mit je einem Inkreis geteilt; Grundseiten 4 und 9 → Mitte 6 → r : R = 2 : 3.
import math, random
from _basis import *
from _geo import fuss, abst

NR, KURZ = 32, "zwei-inkreise"
TITEL = {"de": [("r : R = ?", TINTE)], "en": [("r : R = ?", TINTE)]}
ZEILE = {"de": None, "en": None}
STICHWORT = {"de": None, "en": None}
ANTWORT = {"de": [("r : R = 2 : 3", TINTE)], "en": [("r : R = 2 : 3", TINTE)]}
SCHRITTE = {
    "de": ["Verlängere die zwei schrägen Seiten nach oben (gestrichelt), bis sie sich in einem Punkt treffen.",
           "Vergrößert man vom Treffpunkt aus den oberen Kreis, bis er genau auf den unteren passt, dann wandert die mittlere Linie auf die untere und die obere auf die mittlere. Das obere Trapez wird genau zum unteren.",
           "Also gilt für die mittlere Linie m: 4 : m = m : 9. Das ergibt m = 6.",
           "Der Maßstab ist 4 : 6 = 2 : 3 – genauso bei den Radien. r : R = 2 : 3 (nicht 4 : 9!)."],
    "en": ["Extend the two slanted sides upwards (dashed) until they meet in one point.",
           "Enlarge the upper circle from that meeting point until it fits exactly onto the lower one: the middle line moves onto the bottom line, and the top line onto the middle one. The upper trapezoid becomes exactly the lower one.",
           "So for the middle line m: 4 : m = m : 9. This gives m = 6.",
           "The scale is 4 : 6 = 2 : 3 – the same for the radii. r : R = 2 : 3 (not 4 : 9!)."],
}

def bau(unten=9.0, oben=4.0, x1=0.8):
    m = math.sqrt(unten*oben)
    # unteres Teiltrapez: Grundseite unten (0,0)-(unten,0), oben Breite m bei Höhe H; Tangentenbedingung: Schenkel = unten + m
    d = unten - m
    lo, hi = 0.01, 100.0
    f = lambda H: math.hypot(x1, H) + math.hypot(d - x1, H) - (unten + m)
    for _ in range(200):
        mid = (lo + hi)/2
        lo, hi = (lo, mid) if f(lo)*f(mid) <= 0 else (mid, hi)
    H = (lo + hi)/2
    k = oben / m                                     # Höhe des oberen Teiltrapezes = k·H
    L0, R0 = (0.0, 0.0), (unten, 0.0)
    L1, R1 = (x1, H), (x1 + m, H)
    L2 = (x1 + (x1 - 0)*k, H + H*k); R2 = (R1[0] + (R1[0] - R0[0])*k, H + H*k)
    return L0, R0, L1, R1, L2, R2, H, k

def mittelpunkt(L_unten, L_oben, R_unten, y0, r):
    # Kreis mit Radius r, Mittelpunkt auf Höhe y0 + r, Abstand r zum linken Schenkel
    yc = y0 + r
    lo, hi = min(L_unten[0], L_oben[0]), max(R_unten[0], 50)
    g = lambda x: abst((x, yc), fuss((x, yc), L_unten, L_oben)) - r
    a, b = lo, (lo + hi)/2
    for _ in range(200):
        c = (a + b)/2
        a, b = (a, c) if g(a)*g(c) <= 0 else (c, b)
    return ((a + b)/2, yc)

def pruefen():
    for _ in range(10):
        x1 = random.uniform(-1.5, 3.5)
        L0, R0, L1, R1, L2, R2, H, k = bau(x1=x1)
        assert abs(R2[0] - L2[0] - 4) < 1e-9 and abs(R1[0] - L1[0] - 6) < 1e-9
        # beide Teiltrapeze haben einen Inkreis (Pitot: Summe der Schenkel = Summe der Grundseiten)
        assert abs(abst(L0, L1) + abst(R0, R1) - (9 + 6)) < 1e-9
        assert abs(abst(L1, L2) + abst(R1, R2) - (6 + 4)) < 1e-9
        assert abs((H*k/2)/(H/2) - 2/3) < 1e-12
    L0, R0, L1, R1, L2, R2, H, k = bau()
    R, r = H/2, H*k/2
    M1 = mittelpunkt(L0, L1, R0, 0.0, R); M2 = mittelpunkt(L1, L2, R1, H, r)
    for M, rr, legs in ((M1, R, ((L0, L1), (R0, R1))), (M2, r, ((L1, L2), (R1, R2)))):
        for a, b in legs:
            assert abs(abst(M, fuss(M, a, b)) - rr) < 1e-7      # Kreis berührt beide Schenkel
    return "Mittellinie 6, beide Teiltrapeze tangential, r : R = 2 : 3 für 10 zufällige Schenkel"

def figur(ax, loesung=False):
    L0, R0, L1, R1, L2, R2, H, k = bau()
    R, r = H/2, H*k/2
    M1 = mittelpunkt(L0, L1, R0, 0.0, R); M2 = mittelpunkt(L1, L2, R1, H, r)
    if loesung:
        # Treffpunkt der Schenkel
        # Schnitt der Geraden L0L1 und R0R1
        (x1, y1), (x2, y2), (x3, y3), (x4, y4) = L0, L1, R0, R1
        den = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
        px = ((x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4))/den
        py = ((x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4))/den
        q = 0.45
        hilfslinie(ax, L2, (L2[0] + q*(px-L2[0]), L2[1] + q*(py-L2[1])))
        hilfslinie(ax, R2, (R2[0] + q*(px-R2[0]), R2[1] + q*(py-R2[1])))
    kreis(ax, M1, R, farbe=HELLBLAU); kreis(ax, M2, r, farbe=GRUEN)
    zug(ax, [L0, R0, R2, L2]); linie(ax, L1, R1)
    for p, q in ((L0, R0), (L1, R1), (L2, R2)): parallel(ax, p, q, t=0.18)
    for (mx, my), rr, a, b in ((M1, R, L0, L1), (M1, R, R0, R1), (M2, r, L1, L2), (M2, r, R1, R2)):
        punkt(ax, fuss((mx, my), a, b))
    for (mx, my), rr in ((M1, R), (M2, r)):
        punkt(ax, (mx, my - rr)); punkt(ax, (mx, my + rr))
    linie(ax, M1, (M1[0] + R, M1[1]), lw=2.2); linie(ax, M2, (M2[0] + r, M2[1]), lw=2.2)
    punkt(ax, M1, "rot"); punkt(ax, M2, "rot")
    zahl(ax, (M1[0] + R/2, M1[1] + 0.55), "R", groesse=30); zahl(ax, (M2[0] + r/2, M2[1] + 0.5), "r", groesse=28)
    masslinie(ax, L2, R2, "4", seite=1, abstand=6)
    masslinie(ax, L0, R0, "9", seite=-1, abstand=6)
