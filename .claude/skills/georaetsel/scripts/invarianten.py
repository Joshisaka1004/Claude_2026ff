"""Invariantensuche: findet in einer beweglichen Figur Größen, die sich NICHT ändern.

Die Idee: Neue Rätsel entstehen nicht aus dem Gedächtnis (dort liegen die bekannten),
sondern aus einer frisch kombinierten Figur, in der sich überraschend etwas nicht bewegt.

Benutzung:

    import random, sys; sys.path.insert(0, "<skill>/scripts")
    from invarianten import suche, zeige

    def bau(rng):
        # Eine zufällige, zulässige Lage der Figur in einem FESTEN Rahmen (z. B. Quadrat 0..1).
        # Gibt ein dict Name -> (x, y) zurück. Ungültige Lagen: None zurückgeben.
        t = rng.uniform(0, 1)
        A, B, C, D = (0, 0), (1, 0), (1, 1), (0, 1)
        P = (t, 1); Q = (t - 1, 1 + t)
        return dict(A=A, B=B, C=C, D=D, P=P, Q=Q)

    funde = suche(bau, bezug=("A", "B", "C", "D"))    # Bezug: Fläche dieses Vielecks = 1
    zeige(funde)

Geprüft werden: Flächen aller Dreiecke und Vierecke aus den Punkten (relativ zum Bezug),
Verhältnisse zweier solcher Flächen, Längen und Längenverhältnisse, Winkel.
Gemeldet wird nur, was über alle Proben konstant ist, einen „glatten“ Wert hat
(kleiner Bruch, auch mal √2, √3 oder π) UND mindestens einen beweglichen Punkt enthält
– sonst wäre es nur eine Eigenschaft des festen Rahmens.

Danach gilt: jeden Fund selbst verstehen (gibt es einen kurzen Trick?) und erst dann
zu einem Rätsel machen. Viele Funde sind trivial oder Standard – die Bekanntheitsprüfung
und das eigene Urteil sortieren aus.
"""
from __future__ import annotations

import itertools
import math
import random
from fractions import Fraction

FAKTOREN = {"": 1.0, "√2": math.sqrt(2), "√3": math.sqrt(3), "π": math.pi}


def _flaeche(pts):
    s = 0.0
    for i in range(len(pts)):
        x1, y1 = pts[i]; x2, y2 = pts[(i + 1) % len(pts)]
        s += x1 * y2 - x2 * y1
    return abs(s) / 2


def _einfach(pts):
    """Viereck ohne sich kreuzende Seiten?"""
    def kreuzt(p1, p2, p3, p4):
        def o(a, b, c):
            return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
        return o(p1, p2, p3)*o(p1, p2, p4) < 0 and o(p3, p4, p1)*o(p3, p4, p2) < 0
    a, b, c, d = pts
    return not kreuzt(a, b, c, d) and not kreuzt(b, c, d, a)


def _glatt(wert, max_nenner=12, tol=1e-6):
    """Glatter Wert? Gibt Text wie '3/4', '1/2·√3', '2π' zurück oder None."""
    if not math.isfinite(wert) or wert <= 1e-9:
        return None
    for name, f in FAKTOREN.items():
        q = wert / f
        fr = Fraction(q).limit_denominator(max_nenner)
        if fr.numerator > 0 and abs(float(fr) - q) < tol * max(1, q) and fr.numerator <= 60:
            zahl = str(fr) if fr.denominator > 1 else str(fr.numerator)
            if not name:
                return zahl
            return name if zahl == "1" else f"{zahl}·{name}"
    return None


def suche(bau, bezug=None, proben=25, saat=1, max_nenner=12, vierecke=True, winkel=True,
          laengen=True, verhaeltnisse=True, max_funde=80, starr=()):
    """starr: Punktgruppen, die per Konstruktion eine feste Form haben (z. B. ein aufgesetztes
    gleichseitiges Dreieck ("A", "P", "E")). Größen, die nur aus festen Rahmenpunkten und
    EINER solchen Gruppe bestehen, sind trivial und werden nicht gemeldet."""
    rng = random.Random(saat)
    lagen = []
    versuche = 0
    while len(lagen) < proben and versuche < proben * 50:
        versuche += 1
        z = bau(rng)
        if z:
            lagen.append(z)
    if len(lagen) < 3:
        raise ValueError("bau() lieferte zu wenige gültige Lagen")
    namen = sorted(lagen[0])

    # bewegliche Punkte (im festen Rahmen)
    beweglich = {n for n in namen
                 if max(math.dist(l[n], lagen[0][n]) for l in lagen) > 1e-7}

    def norm_flaeche(l):
        return _flaeche([l[n] for n in bezug]) if bezug else 1.0

    def norm_laenge(l):
        return math.sqrt(norm_flaeche(l))

    groessen = {}            # Schlüssel -> Liste von Werten über die Proben
    for l in lagen:
        F = norm_flaeche(l); L = norm_laenge(l)
        for tri in itertools.combinations(namen, 3):
            groessen.setdefault(("Fläche", tri), []).append(_flaeche([l[n] for n in tri]) / F)
        if vierecke:
            for quad in itertools.combinations(namen, 4):
                for perm in (quad, (quad[0], quad[1], quad[3], quad[2]), (quad[0], quad[2], quad[1], quad[3])):
                    pts = [l[n] for n in perm]
                    if _einfach(pts):
                        groessen.setdefault(("Fläche", perm), []).append(_flaeche(pts) / F)
                        break
                else:
                    groessen.setdefault(("Fläche", quad), []).append(float("nan"))
        if laengen:
            for a, b in itertools.combinations(namen, 2):
                groessen.setdefault(("Länge", (a, b)), []).append(math.dist(l[a], l[b]) / L)
        if winkel:
            for s in namen:
                for a, b in itertools.combinations([n for n in namen if n != s], 2):
                    va = (l[a][0]-l[s][0], l[a][1]-l[s][1]); vb = (l[b][0]-l[s][0], l[b][1]-l[s][1])
                    na, nb = math.hypot(*va), math.hypot(*vb)
                    if na < 1e-9 or nb < 1e-9:
                        w = float("nan")
                    else:
                        c = max(-1, min(1, (va[0]*vb[0] + va[1]*vb[1]) / (na*nb)))
                        w = math.degrees(math.acos(c))
                    groessen.setdefault(("Winkel", (a, s, b)), []).append(w)

    def konstant(werte, tol=1e-7):
        if any(not math.isfinite(w) for w in werte):
            return None
        m = sum(werte) / len(werte)
        if max(abs(w - m) for w in werte) > tol * max(1, abs(m)):
            return None
        return m

    rahmen = set(namen) - beweglich
    gruppen = [set(g) for g in starr]

    def interessant(pkte):
        pk = set(pkte) if not isinstance(pkte[0], tuple) else set(pkte[0]) | set(pkte[1])
        if not pk & beweglich:
            return False
        return not any(pk <= rahmen | g for g in gruppen)

    funde = []
    konst_flaechen = {}
    for (art, pkte), werte in groessen.items():
        if not interessant(pkte):
            continue
        m = konstant(werte)
        if m is None:
            continue
        if art == "Winkel":
            if 1 < m < 179 and abs(m - round(m)) < 1e-6 and round(m) % 90 != 0:
                funde.append((len(set(pkte) & beweglich), art, pkte, f"{round(m)}°"))
            continue
        if art == "Fläche" and m < 1e-7:
            continue                       # entartet (Punkte auf einer Geraden)
        if art == "Fläche":
            konst_flaechen[pkte] = m
        g = _glatt(m, max_nenner)
        if g and (bezug or art != "Fläche"):
            funde.append((len(set(pkte) & beweglich), art, pkte, g))

    if verhaeltnisse:
        # Verhältnisse zweier NICHT konstanter Flächen, die trotzdem konstant sind (z. B. „immer gleich groß“)
        bewegte = [(k, v) for k, v in groessen.items() if k[0] == "Fläche" and interessant(k[1])
                   and k[1] not in konst_flaechen and all(math.isfinite(x) and x > 1e-7 for x in v)]
        for (k1, v1), (k2, v2) in itertools.combinations(bewegte, 2):
            if set(k1[1]) == set(k2[1]) or not interessant((k1[1], k2[1])):
                continue
            r = [a / b for a, b in zip(v1, v2)]
            m = konstant(r, 1e-7)
            if m is not None:
                g = _glatt(m, max_nenner)
                if g:
                    funde.append((len((set(k1[1]) | set(k2[1])) & beweglich) + 1, "Verhältnis",
                                  (k1[1], k2[1]), g))

    rang = {"Fläche": 0, "Länge": 0, "Winkel": 1, "Verhältnis": 2}
    funde.sort(key=lambda f: (rang[f[1]], -f[0]))
    return {"beweglich": sorted(beweglich), "proben": len(lagen), "funde": funde[:max_funde]}


def zeige(ergebnis):
    print(f"Proben: {ergebnis['proben']} · bewegliche Punkte: {', '.join(ergebnis['beweglich']) or '–'}")
    if not ergebnis["funde"]:
        print("Keine glatten Invarianten gefunden.")
    for gewicht, art, pkte, wert in ergebnis["funde"]:
        if art == "Verhältnis":
            gemeinsam = len(set(pkte[0]) & set(pkte[1]))
            hinweis = "  (gemeinsame Seite – oft nur „gleiche Grundseite, gleiche Höhe“)" if gemeinsam >= 2 else ""
            print(f"  [{gewicht}] Fläche {''.join(pkte[0])} : Fläche {''.join(pkte[1])} = {wert}{hinweis}")
        elif art == "Winkel":
            print(f"  [{gewicht}] Winkel {''.join(pkte)} = {wert}")
        else:
            print(f"  [{gewicht}] {art} {''.join(pkte)} = {wert}")


if __name__ == "__main__":
    # Selbsttest: Quadrat ABCD, P auf CD, Quadrat über AP mit Ecke Q → Dreieck ACQ = Quadrat
    def bau(rng):
        t = rng.uniform(0.05, 0.95)
        return dict(A=(0, 0), B=(1, 0), C=(1, 1), D=(0, 1), P=(t, 1), Q=(t - 1, 1 + t))
    zeige(suche(bau, bezug=("A", "B", "C", "D")))
