---
name: georaetsel
description: "Use when Jochen types /georaetsel or asks for classic geometry puzzle cards (klassische Georätsel): one clean figure, a title question like „Grün = ?“, „Gelb : Rot = ?“ or „r : R = ?“, markings instead of text, a hidden aha. Creates new original cards DE+EN (default 12, or the number given as argument) with verified solutions and an iPad gallery."
---

# /georaetsel – klassische Georätsel

Ziel: neue, eigene Geometrie-Rätselkarten im **klassischen Stil** – so wie die Vorlagen in `referenz/`: eine saubere Figur, eine kurze Frage als Titel, fast kein Text, ein echter Aha-Moment. Deutsch und Englisch, fertig geprüft, mit Lösungsblatt und Galerie für das iPad.

Anzahl: Steht eine Zahl hinter dem Befehl (z. B. `/georaetsel 6`), so viele Karten. Sonst 12.

Unterschied zu /ahaaufgaben: Dort sind auch Alltag, 3D, Längen-Geschichten erlaubt. Hier **nur ebene Geometrie, keine Einkleidung, kein Fließtext**. Die Figur trägt die ganze Aufgabe.

## 1. Der klassische Stil (Kern – immer einhalten)

Vorher die Vorlagen in `referenz/` ansehen und `referenz/stil.md` lesen. Die Vorlagen dienen nur als Stilmaß – kein Motiv daraus nachbauen, auch nicht abgewandelt.

1. **Titel = Frage.** Kurz und fett: „Grün = ?“, „Gelb : Rot = ?“, „r : R = ?“, „A / B = ?“, „x = ?“, „Gesamtfläche = ?“, „Fläche des Quadrats = ?“, bei Beweisen „Zeige: S = (a² − b²) / 4“. Farbwörter im Titel in der Farbe ihrer Fläche.
2. **Fast kein Text.** Am besten gar keiner. Erlaubt:
   - ein kursives Stichwort unter der Figur: „Quadrat“, „regelmäßiges Sechseck“, „gleichseitiges Dreieck“, „drei Quadrate“, „Halbkreis“;
   - höchstens **eine** kurze Zeile unter dem Titel – nur für etwas, das man nicht zeichnen kann, z. B. „Die Zahlen sind Flächen.“
   Mehr als ein Satz = zurück an den Zeichentisch: Lässt sich die Bedingung als Marke zeichnen, wird sie gezeichnet.
3. **Die Figur spricht.** Feste Zeichensprache:
   - Strichmarken (1, 2, 3 Striche) = gleich lange Strecken
   - Pfeilspitzen auf Strecken = parallel
   - Quadrätchen = rechter Winkel
   - Gradzahl im Winkel = Winkelgröße
   - kleiner Kreis (hohl) = wichtiger Punkt: Ecke, Teilpunkt, Berührpunkt, Punkt, durch den eine Linie geht; rot gefüllt = Mittelpunkt
   - Zahl in einer Fläche = Flächeninhalt; Zahl an einer Strecke = Länge; „3k“, „2k“ = Längenverhältnis ohne Einheit
   - Buchstaben (A, B, S, r, R, x) für Größen, nach denen gefragt wird oder die gleich sind (A, A, A = drei gleiche Flächen)
   - Schraffur = Überlappung zweier farbiger Flächen
4. **Nur klassische Formen:** Quadrat, Rechteck, regelmäßiges Sechseck/Achteck, gleichseitiges, gleichschenkliges, rechtwinkliges Dreieck, Kreis, Halbkreis, Viertelkreis, Trapez, Parallelogramm, Raute. Keine Einheiten, keine Geschichten, kein 3D.
5. **Wenige Angaben:** meist 1–4 Zahlen, klein und glatt. Das Ergebnis ist glatt: ganze Zahl, einfacher Bruch, einfaches Verhältnis, einfache Wurzel, Vielfaches von π, Grad.
6. **Aha statt Rechnen.** Mit dem Trick ist die Lösung 3–5 Zeilen lang. Ohne Trick bleibt nur mühsames Koordinaten-Rechnen. Ein Gleichungssystem ist nie der Kern.
7. **Maßstabsgetreu.** Jede Karte zeigt eine echte Lösung der Aufgabe, aus der Rechnung konstruiert. Eine Fläche „10“ sieht größer aus als eine Fläche „4“. Gesuchte Längen, die man abmessen könnte, nicht mit Maßlinie zeigen.
8. **Ruhig und klar:** dicke schwarze Konturen, wenige kräftige Farben, viel Weiß. Kein Lösungsweg, keine Hilfslinie, die nicht zur Aufgabe gehört.

## 2. Aha-Baukasten (für die Ideen, gut mischen)

- Gleiche Grundseite, gleiche Höhe → gleiche Fläche (Spitze auf einer Parallelen verschieben).
- Punkt im Rechteck/Parallelogramm: gegenüberliegende Dreiecke ergeben zusammen die halbe Fläche. Im regelmäßigen Sechseck: abwechselnde Dreiecke ergeben zusammen die halbe Fläche.
- Eine Größe kürzt sich heraus: Ergebnis hängt nicht von der Lage eines Punktes oder der Größe einer Teilfigur ab.
- Pythagoras über Flächen: Halbkreise, Quadrate oder ähnliche Figuren über den Seiten, Möndchen.
- Schmetterling im Trapez: die zwei seitlichen Dreiecke sind gleich groß; Produkt gegenüberliegender Teilflächen gleich.
- Ähnliche Dreiecke: Flächen verhalten sich wie die Quadrate der Seiten.
- Ergänzen zu einer bekannten Figur (gedrehtes Quadrat im Quadrat, Sechseck aus 6 oder 24 Dreiecken, Dreieck zum Parallelogramm verdoppeln).
- Drehen um 90° oder 60° (kongruente Teile um die Mitte eines Quadrats oder gleichseitigen Dreiecks).
- Gleiche Flächen (A, A, A) führen auf eine Gleichung, die sich überraschend vereinfacht.
- Seitenhalbierende, Schwerpunkt, Teilverhältnisse auf Seiten → Flächen im Verhältnis.
- Kreise, die sich berühren: Mittelpunktabstand = Summe/Differenz der Radien; Tangenten von einem Punkt sind gleich lang.
- Thales, Umfangswinkel, Sehnensatz, Sekanten-Tangenten-Satz.
- Winkeljagd mit 15°, 30°, 45°, 60°, 75°, 105°.

## 3. Ablauf

### 3.1 Vorbereitung
- Projektgedächtnis lesen (Rätselkarten: Stil, Signatur, Serien, nächste Nummer).
- Alle bisherigen Serien suchen und jede `loesungen.md` lesen: `/mnt/project-files/aufgaben-*/`, `/mnt/project-files/georaetsel-*/` und im Repo `georaetsel/*/` (was davon existiert). Daraus die Liste benutzter Motive bilden. Kein Motiv wiederholen.
- Nummer: höchste bisher benutzte Nummer + 1 (gemeinsame Zählung mit /ahaaufgaben). Datum = heute, Format `TT.MM.JJJJ`.
- Den Skill `raetselgrafik-pruefung` laden und befolgen. Wo er Text verlangt, gilt hier zuerst: **eine Marke in der Figur statt eines Satzes**. Nur was sich nicht zeichnen lässt, kommt als eine kurze Zeile dazu.

### 3.2 Ideen
- Erst eine Tabelle: Nr. · Figur · Gegeben · Gesucht · Aha · Lösung · Stufe.
- Stufen gemischt: etwa ¼ leicht, ½ mittel, ¼ schwer. Fragearten gemischt: Fläche, Verhältnis, Winkel, Länge, höchstens ein Beweis pro Serie.
- Jede Idee bekommt einen eigenen Aha-Typ; derselbe Typ höchstens zweimal pro Serie.

### 3.3 Rechnen und Bestimmtheit (Pflicht, Python)
Für jede Karte ein kleines Skript `nr-XX.py` (wird mit ausgeliefert):
1. Die Figur aus wenigen freien Größen bauen (z. B. Seitenlänge, Lage eines Punktes). Alle Punkte daraus berechnen.
2. **Bestimmtheitsprüfung:** Die freien Größen zufällig variieren (mindestens 20 Fälle), dabei die gegebenen Angaben erzwingen (direkt oder mit `scipy.optimize`). Die gesuchte Größe muss in allen Fällen gleich sein. Schwankt sie, fehlt eine Angabe → Marke oder Zahl ergänzen.
3. **Redundanzprüfung:** Jede Angabe einzeln weglassen. Bleibt die Lösung trotzdem fest, die Angabe streichen (außer sie ist das Aha, z. B. „egal wo der Punkt liegt“ – dann bewusst so lassen und im Lösungsblatt erwähnen).
4. Die gezeichnete Instanz ist einer dieser Fälle; ihre Flächen müssen genau die aufgedruckten Zahlen haben (mit shapely nachmessen).
5. Ergebnis exakt (Bruch, Wurzel, π) und als Dezimalzahl notieren.

### 3.4 Zeichnen
- Baukasten benutzen: `scripts/karte.py` (Karte, Flächen, Kreise, Strichmarken, Parallelpfeile, rechte Winkel, Winkelbögen, Punkte, Maßlinien, Kontaktbogen). Bei Bedarf `pip install matplotlib shapely scipy pillow`.
- Format 1100 × 1100 px, weißer Grund, Schrift Inter. Titel fett oben, ggf. eine Zeile darunter, Figur in der Mitte, Stichwort kursiv darunter, Datum + #Nr senkrecht links, Signatur unten: `#GeoRätsel` (DE) bzw. `#GeoPuzzle` (EN). Nie den Namen eines fremden Autors.
- Farben aus dem Baukasten: `GRUEN` für das Gesuchte, `HELLBLAU`, `GELB`, `ROT`, `GOLD`, `ORANGE`, `VIOLETT` für gegebene oder verglichene Flächen. Höchstens drei Füllfarben pro Karte.
- Marken (Striche, Pfeile, Winkel) erst nach den Umrissen zeichnen – ihre Größe richtet sich nach der Figur.
- Zahlen mittig in ihre Fläche, nie auf eine Linie; gesuchte Fläche mit „?“ in `GRUEN_TXT`.
- Dateinamen: `XX-kurzname-de.png`, `XX-kurzname-en.png`.
- Kontaktbogen aller Karten bauen und ansehen, dann jede Karte in voller Größe. Mängel sofort beheben.

### 3.5 Prüfen (Pflicht)
1. **Kaltlesen** wie in `raetselgrafik-pruefung` (frischer Subagent, nur die PNGs, keine Lösungen). Zusätzlich fragen: „Gibt es Text, den die Skizze schon zeigt oder der durch eine Marke ersetzbar wäre?“
2. **Kaltlösen:** Ein zweiter frischer Subagent bekommt nur die deutschen PNGs und löst jede Karte: Antwort plus Lösungsidee in 2–3 Sätzen, und welche Annahmen er treffen musste. Abweichung von der eigenen Lösung → klären: Ist die Figur mehrdeutig (Punkt auf Seite oder in Ecke? Berührung oder Schnitt? parallel oder nicht?), fehlt eine Marke, oder irrt der Agent? Musste er etwas annehmen, das nicht markiert ist → Marke ergänzen.
3. Korrigieren, neu rendern, ansehen; zweiter Durchgang nur für Befunde hoch/mittel.

### 3.6 Ausliefern
- Ordner: `/mnt/project-files/georaetsel-JJJJ-MM-TT/`, falls `/mnt/project-files` existiert; sonst im Repo `georaetsel/JJJJ-MM-TT/` (bei zweiter Serie am selben Tag Suffix b, c …). Inhalt: alle PNGs, alle `nr-XX.py`, `loesungen.md`, ZIP mit allem.
- `loesungen.md`: Tabelle Nr. · Titel · Aha · Lösung, danach pro Karte der kurze Lösungsweg in leichter Sprache (3–6 Sätze, der Trick zuerst).
- Im Repo: committen und auf den vorgegebenen Branch pushen.
- Galerie-Artifact veröffentlichen: Karten als JPG neben der Seite, Schalter Deutsch/English, unter jeder Karte eine eingeklappte Lösung. Jochen öffnet die Galerie auf dem iPad – sie ist der Hauptweg (ZIPs gehen dort nicht).
- Antwort: Galerie-Link zuerst, dann 2–3 Sätze zu den schönsten Aha-Momenten, Lösungsblatt und ZIP anhängen (höchstens 6 Anhänge).
- Projektgedächtnis ergänzen: Serie, Ordner, Galerie-Link, neue Motive, nächste Nummer.

## 4. Wörter DE → EN (immer gleich übersetzen)

| Deutsch | English |
|---|---|
| Grün = ? | Green = ? |
| Gelb : Rot = ? | Yellow : Red = ? |
| Gesamtfläche = ? | Total area = ? |
| Fläche des Quadrats = ? | Area of the square = ? |
| Zeige: … | Prove: … |
| Die Zahlen sind Flächen. | The numbers are areas. |
| Quadrat / drei Quadrate | square / three squares |
| Rechteck | rectangle |
| regelmäßiges Sechseck | regular hexagon |
| gleichseitiges Dreieck | equilateral triangle |
| Halbkreis / Viertelkreis | semicircle / quarter circle |
| Trapez / Parallelogramm / Raute | trapezoid / parallelogram / rhombus |

Farbwörter: Grün/Green, Blau/Blue, Gelb/Yellow, Rot/Red, Gold/Gold, Orange/Orange, Lila/Purple.
