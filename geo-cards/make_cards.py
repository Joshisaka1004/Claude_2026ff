"""Erzeugt die Rätselkarten GEO/52 und GEO/54 (DE+EN) als HTML.

Alle Punkte werden aus der Rechnung konstruiert, nicht frei platziert.
Rendern: node render.js
"""
import math
import pathlib

OUT = pathlib.Path(__file__).parent / "html"
OUT.mkdir(exist_ok=True)

BG = "#faf9f4"
DARK = "#16303f"
TEAL = "#0f7782"
LINE = "#1b2f3f"
BEIGE = "#efece2"
GREEN = "#98d7b5"
PURPLE = "#dcc3eb"
ORANGE = "#f6c379"
BLUE = "#aed3ee"

R2 = math.sqrt(2)


def page(card, lang, difficulty, title, body, question, svg, fig_h):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;padding:0;}}
body{{width:1080px;height:1350px;background:{BG};font-family:'Liberation Sans',Arial,sans-serif;color:{DARK};position:relative;overflow:hidden;}}
.top{{position:absolute;left:64px;right:64px;top:56px;display:flex;justify-content:space-between;font-weight:700;font-size:23px;}}
.top .id{{color:{TEAL};letter-spacing:.5px;}}
h1{{position:absolute;left:64px;right:64px;top:108px;margin:0;font-size:56px;line-height:66px;font-weight:700;}}
.text{{position:absolute;left:64px;right:64px;top:192px;font-size:32px;line-height:44px;}}
.text p{{margin:0;}}
.text .q{{margin-top:14px;color:{TEAL};font-weight:700;}}
.fig{{position:absolute;left:0;right:0;bottom:130px;height:{fig_h}px;display:flex;justify-content:center;}}
.foot{{position:absolute;left:64px;right:64px;top:1254px;border-top:1.5px solid #d9d6cc;padding-top:22px;display:flex;justify-content:space-between;font-size:19px;color:#4c5d68;}}
.foot .sig{{font-size:24px;color:{DARK};}}
</style></head><body>
<div class="top"><span class="id">GEO&nbsp;&nbsp;/&nbsp;&nbsp;{card}</span><span>{difficulty}</span></div>
<h1>{title}</h1>
<div class="text"><p>{body}</p><p class="q">{question}</p></div>
<div class="fig">{svg}</div>
<div class="foot"><span>{lang}&nbsp;&nbsp;·&nbsp;&nbsp;GEO-20261105-{card}</span><span class="sig">#Jochen V.</span></div>
</body></html>"""


def label(x, y, t, size=38):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="700" '
            f'fill="{DARK}" text-anchor="middle" dominant-baseline="central">{t}</text>')


def poly(pts, fill, stroke=LINE, sw=3):
    p = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
    return f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'


def area(pts):
    s = 0
    for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
        s += x1 * y2 - x2 * y1
    return abs(s) / 2


# ---------------------------------------------------------------- GEO/52
def card52():
    # Achteck mit Mittelpunkt (cx, cy), Abstand Mitte-Seite a, Seite s.
    # Bekannt: Dreiecke an Gegenseiten ergeben zusammen 2A; A = s*a/2.
    # 60 = A+u, 40 = A+v, 50 = A-(u+v)/sqrt2  ->  A = 50, u = 10, v = -10
    # Lage von P: x = a*u/A, y(nach unten) = -a*v/A
    W, H = 900, 760
    cx, cy, a = W / 2, H / 2, 375
    s = 2 * a / (1 + R2)
    h = s / 2
    TL, TR = (cx - h, cy - a), (cx + h, cy - a)
    RT, RB = (cx + a, cy - h), (cx + a, cy + h)
    BR, BL = (cx + h, cy + a), (cx - h, cy + a)
    LB, LT = (cx - a, cy + h), (cx - a, cy - h)
    octo = [TL, TR, RT, RB, BR, BL, LB, LT]
    A, u, v = 50, 10, -10
    P = (cx + a * u / A, cy - a * v / A)

    green = [P, LT, TR]
    purple = [P, TR, RT]
    orange = [P, LT, LB]
    blue = [P, BL, BR]
    k = area(orange) / 60  # px² pro cm²
    for name, tri, val in [("purple", purple, 50), ("blue", blue, 40)]:
        assert abs(area(tri) / k - val) < 1e-6, name
    g = area(green) / k
    assert abs(g - (10 + 60 * R2)) < 1e-6
    assert abs(area(octo) / k - 400) < 1e-6

    def c(t, dx=0, dy=0):
        return (sum(p[0] for p in t) / 3 + dx, sum(p[1] for p in t) / 3 + dy)

    parts = [poly(octo, BEIGE),
             poly(orange, ORANGE), poly(purple, PURPLE), poly(blue, BLUE),
             poly(green, GREEN, stroke=TEAL, sw=2.5),
             poly(octo, "none")]
    gx, gy = c(green, 0, -20)
    ox, oy = c(orange, -60, 0)
    px_, py_ = c(purple, 40, -10)
    bx, by = c(blue, 0, 60)
    parts += [label(gx, gy, "?", 50), label(ox, oy, "60"),
              label(px_, py_, "50"), label(bx, by, "40")]
    parts.append(f'<circle cx="{P[0]:.2f}" cy="{P[1]:.2f}" r="8" fill="{LINE}"/>')
    parts.append(f'<text x="{P[0] + 22:.1f}" y="{P[1] + 14:.1f}" font-size="30" '
                 f'font-weight="700" fill="{DARK}" dominant-baseline="central">P</text>')
    svg = (f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
           f'xmlns="http://www.w3.org/2000/svg">{"".join(parts)}</svg>')
    print(f"GEO/52: green = {g:.4f} cm² (10+60√2), octagon = 400 cm²")

    texts = {
        "EN": dict(difficulty="VERY HARD", title="The Fan in the Octagon",
                   body="The octagon has eight equal sides and eight equal angles. "
                        "The orange, green, purple and blue triangles each have one corner at P. "
                        "Their other corners are corners of the octagon. "
                        "The numbers are areas in cm².",
                   question="What is the area of the green triangle?"),
        "DE": dict(difficulty="SEHR SCHWER", title="Der Fächer im Achteck",
                   body="Das Achteck hat acht gleich lange Seiten und acht gleich große Winkel. "
                        "Das orange, das grüne, das lila und das blaue Dreieck haben je eine Ecke in P. "
                        "Ihre anderen Ecken sind Ecken des Achtecks. "
                        "Die Zahlen sind Flächen in cm².",
                   question="Welche Fläche hat das grüne Dreieck?"),
    }
    for lang, t in texts.items():
        (OUT / f"GEO-52_{lang}.html").write_text(page("52", lang, svg=svg, fig_h=H, **t))


# ---------------------------------------------------------------- GEO/54
def card54():
    # Lücken links = unten = p, oben = rechts = q, grüne Seite g.
    # Blau q(p+g), Orange q(q+g), Lila p(q+g), Beige p(p+g) (nicht angegeben).
    p, q, g = 2, 5, 6
    blue_a, orange_a, purple_a = q * (p + g), q * (q + g), p * (q + g)
    assert (blue_a, orange_a, purple_a) == (40, 55, 22)
    # Eindeutigkeit: q/p = Orange/Lila; q = 5t, p = 2t
    sols = []
    for pp in [x / 100 for x in range(1, 2000)]:
        qq = pp * orange_a / purple_a
        gg = blue_a / qq - pp
        if gg > 0 and abs(qq * (qq + gg) - orange_a) < 1e-6:
            sols.append((pp, qq, gg))
    assert sols == [(2.0, 5.0, 6.0)], sols

    S = p + g + q
    side = 790
    m = 8
    W = H = side + 2 * m
    k = side / S
    x0, y0 = m, m

    def R(x1, y1, x2, y2, fill):
        return (f'<rect x="{x0 + x1 * k:.2f}" y="{y0 + y1 * k:.2f}" width="{(x2 - x1) * k:.2f}" '
                f'height="{(y2 - y1) * k:.2f}" fill="{fill}" stroke="{LINE}" stroke-width="3"/>')

    parts = [R(0, 0, p + g, q, BLUE),                 # oben
             R(p + g, 0, S, q + g, ORANGE),           # rechts
             R(p, q + g, S, S, PURPLE),               # unten
             R(0, q, p, S, BEIGE),                    # links
             R(p, q, p + g, q + g, GREEN)]            # grünes Quadrat
    # Diagonale: Strichmuster so gewählt, dass sie genau in beiden Ecken endet
    L = S * R2 * k
    n = 30
    dash = L / (n + (n - 1) * 0.75)
    gap = 0.75 * dash
    ax, ay = x0, y0 + S * k
    ux, uy = 1 / R2, -1 / R2
    segs = []
    for i in range(n):
        t0 = i * (dash + gap)
        t1 = t0 + dash
        segs.append(f'<line x1="{ax + ux * t0:.2f}" y1="{ay + uy * t0:.2f}" '
                    f'x2="{ax + ux * t1:.2f}" y2="{ay + uy * t1:.2f}" stroke="#5a6b75" '
                    f'stroke-width="2" stroke-linecap="butt"/>')
    parts += segs
    parts.append(f'<rect x="{x0}" y="{y0}" width="{side}" height="{side}" fill="none" '
                 f'stroke="{LINE}" stroke-width="3.5"/>')

    def P(x, y):
        return x0 + x * k, y0 + y * k

    parts += [label(*P((p + g) / 2, q / 2), str(blue_a)),
              label(*P(p + g + q / 2, (q + g) / 2 + 1), str(orange_a)),
              label(*P(p + (g + q) / 2, q + g + p / 2), str(purple_a)),
              label(*P(p + g * 0.72, q + g * 0.72), "?", 50)]
    svg = (f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
           f'xmlns="http://www.w3.org/2000/svg">{"".join(parts)}</svg>')
    print(f"GEO/54: p={p}, q={q}, g={g}: green = {g * g} cm²; beige (not given) = {p * (p + g)}")

    texts = {
        "EN": dict(difficulty="HARD", title="The Diagonal in the Frame",
                   body="A big square is made of a green square and four rectangles. "
                        "The dashed line runs through opposite corners of both squares. "
                        "The numbers are areas in cm².",
                   question="What is the area of the green square?"),
        "DE": dict(difficulty="SCHWER", title="Die Diagonale im Rahmen",
                   body="Ein großes Quadrat besteht aus einem grünen Quadrat und vier Rechtecken. "
                        "Die gestrichelte Linie läuft durch gegenüberliegende Ecken beider Quadrate. "
                        "Die Zahlen sind Flächen in cm².",
                   question="Welche Fläche hat das grüne Quadrat?"),
    }
    for lang, t in texts.items():
        (OUT / f"GEO-54_{lang}.html").write_text(page("54", lang, svg=svg, fig_h=H, **t))


card52()
card54()
