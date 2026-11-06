"""Legt den nächsten Serien-Ordner an und gibt seinen Pfad aus.

Ordner heißen 001, 002, 003 … (drei Ziffern). Gibt es noch keinen, wird 001 angelegt;
ist 005 der höchste, wird 006 angelegt. Lücken werden nicht aufgefüllt.

    python3 naechster_ordner.py [basisordner]      # Standard: <repo>/georaetsel
"""
import re
import sys
from pathlib import Path

basis = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[4] / "georaetsel"
basis.mkdir(parents=True, exist_ok=True)
nummern = [int(p.name) for p in basis.iterdir() if p.is_dir() and re.fullmatch(r"\d{3}", p.name)]
neu = basis / f"{max(nummern, default=0) + 1:03d}"
neu.mkdir()
print(neu)
