"""Prüft und rendert alle Karten dieser Serie (Aufgabe + Lösung, DE + EN)."""
import importlib.util, sys
from pathlib import Path
from _basis import *

HIER = Path(__file__).resolve().parent
OUT = HIER / "png"; OUT.mkdir(exist_ok=True)

def laden(p):
    spec = importlib.util.spec_from_file_location(p.stem.replace("-", "_"), p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

alle = []
for p in sorted(HIER.glob("nr-*.py")):
    if len(sys.argv) > 1 and p.stem not in sys.argv[1:]:
        continue
    m = laden(p)
    print(f"#{m.NR} {m.KURZ}: {m.pruefen()}")
    for spr in ("de", "en"):
        k = Karte(titel=m.TITEL[spr], zeile=m.ZEILE[spr], stichwort=m.STICHWORT[spr],
                  datum=DATUM, nr=m.NR, sprache=spr)
        m.figur(k.ax, loesung=False)
        a = k.speichern(OUT / f"{m.NR}-{m.KURZ}-aufgabe-{spr}.png")
        l = Loesungskarte(antwort=m.ANTWORT[spr], schritte=m.SCHRITTE[spr], datum=DATUM, nr=m.NR, sprache=spr)
        m.figur(l.ax, loesung=True)
        b = l.speichern(OUT / f"{m.NR}-{m.KURZ}-loesung-{spr}.png")
        alle += [a, b]
if len(sys.argv) == 1:
    kontaktbogen([p for p in alle if p.name.endswith("-de.png")], HIER / "kontaktbogen-de.png", spalten=4, breite=330)
