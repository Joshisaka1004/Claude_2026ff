"""Gemeinsamer Kopf für alle Karten dieser Serie."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / ".claude/skills/georaetsel/scripts"))
from karte import *  # noqa
DATUM = "06.11.2026"
