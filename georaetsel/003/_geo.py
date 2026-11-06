"""Kleine Geometrie-Helfer für diese Serie."""
import math

def fuss(p, a, b):
    dx, dy = b[0]-a[0], b[1]-a[1]
    t = ((p[0]-a[0])*dx + (p[1]-a[1])*dy) / (dx*dx + dy*dy)
    return (a[0] + t*dx, a[1] + t*dy)

def abst(p, q):
    return math.hypot(p[0]-q[0], p[1]-q[1])

def inkreis(a, b, c):
    la, lb, lc = abst(b, c), abst(c, a), abst(a, b)
    s = la + lb + lc
    m = ((la*a[0] + lb*b[0] + lc*c[0]) / s, (la*a[1] + lb*b[1] + lc*c[1]) / s)
    return m, abst(m, fuss(m, a, b))

def flaeche(*p):
    return abs(sum(p[i][0]*p[(i+1) % len(p)][1] - p[(i+1) % len(p)][0]*p[i][1] for i in range(len(p)))) / 2

def drehe(p, c, w):
    x, y = p[0]-c[0], p[1]-c[1]
    return (c[0] + x*math.cos(w) - y*math.sin(w), c[1] + x*math.sin(w) + y*math.cos(w))

def schnitt(p1, p2, p3, p4):
    x1, y1 = p1; x2, y2 = p2; x3, y3 = p3; x4, y4 = p4
    d = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    a = x1*y2 - y1*x2; b = x3*y4 - y3*x4
    return ((a*(x3-x4) - (x1-x2)*b)/d, (a*(y3-y4) - (y1-y2)*b)/d)

def umkreis(a, b, c):
    ax_, ay = a; bx, by = b; cx, cy = c
    d = 2*(ax_*(by-cy) + bx*(cy-ay) + cx*(ay-by))
    ux = ((ax_**2+ay**2)*(by-cy) + (bx**2+by**2)*(cy-ay) + (cx**2+cy**2)*(ay-by))/d
    uy = ((ax_**2+ay**2)*(cx-bx) + (bx**2+by**2)*(ax_-cx) + (cx**2+cy**2)*(bx-ax_))/d
    return (ux, uy), abst((ux, uy), a)

def buchstabe(ax, p, text, dx=0.0, dy=0.0, groesse=22, farbe="#1D2330"):
    """Punktname (nur auf Lösungskarten), leicht versetzt neben den Punkt."""
    ax.text(p[0] + dx, p[1] + dy, text, fontsize=groesse, fontweight="bold", color=farbe,
            ha="center", va="center", zorder=9)
