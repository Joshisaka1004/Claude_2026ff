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
