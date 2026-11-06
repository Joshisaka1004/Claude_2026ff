# Klassische Georätsel – Serie 002 (06.11.2026, #27–#34)

Erstellt mit `/georaetsel`. Jede Karte gibt es als Aufgabe und als Lösung, auf Deutsch und Englisch, im Ordner `png/`.
`nr-XX.py` rechnet die Lösung mit zufällig veränderten Figuren nach und zeichnet die Karten; `python3 render.py` erzeugt alle PNGs neu.

## Einstellungen
- Anzahl: 8 · Stufe: schwer · Sprachen: Deutsch + Englisch
- Modelle (gemischt): Rechnen, Zeichnen, Entscheiden – diese Sitzung; zweite Ideenliste – Opus; Bekanntheitsprüfung – Opus (mit Websuche); Kaltlösen – Opus; Kaltlesen – Sonnet

## Übersicht

| Nr. | Titel | Aha | Was ist neu? | Bekanntheit | Lösung | Stufe |
|---|---|---|---|---|---|---|
| 27 | Gelb = ? | Die Spitze wandert parallel zur Diagonale – P darf man in die Ecke schieben | Quadrat über AP an ein Quadrat angesetzt, gefragt ist das Dreieck ACQ | c | 16 | schwer |
| 28 | x = ? | Umfang des abgeschnittenen Dreiecks = Seite; dritte Seite aus 120° | Sechseck statt Quadrat/Viertelkreis, versteckte 7-8-13-Kombination | b | 28 | schwer |
| 29 | Fläche des Dreiecks = ? | Pythagoras gilt auch für die Inkreisradien, dann 3-4-5-Form | Gefragt ist die Fläche, zwei Ähnlichkeitsschritte | b | 150 | schwer |
| 30 | Gesamtfläche = ? | Die Kappe über drei Seiten ist genau ein Zwölftel | Klassiker „Zwölfeck = 3R²“ umgedreht | b | 12 | schwer |
| 31 | Grün = ? | Dreieck ADP = halbes Quadrat, also AF · DP = Seite² | Viereck statt Dreieck gefragt – zusätzliche Schritte | b | 11 | schwer |
| 32 | r : R = ? | Streckung vom Schnittpunkt der Schenkel: Mittellinie = √(4 · 9) = 6 | Zwei gestapelte Inkreise; Falle 4 : 9 | b | 2 : 3 | schwer |
| 33 | Fläche des Trapezes = ? | r² = Produkt der Schenkelstücke (Höhensatz), zweimal | Schiefes Trapez, nur Berührstücke gegeben | b | 168 | schwer |
| 34 | Grün = ? | Kreis durch die Berührpunkte = Inkreis des Mittelpunktsdreiecks | Gefragt ist der Kreis, nicht das Dreieck der Berührpunkte | b | 9π ≈ 28,3 | schwer |

Bekanntheit: b = verwandte Aufgabe bekannt, aber hier ist ein zusätzlicher Gedanke nötig; c = als Rätselkarte unbekannt.

## Lösungswege in leichter Sprache

**#27 Gelb = 16.** Rückt der Punkt oben ein Stück nach rechts, rückt die Spitze von Gelb um dasselbe Stück nach rechts und nach oben – das zweite Quadrat ist ja um 90° gedreht. Die Spitze läuft also parallel zur Diagonale: gleiche Grundseite, gleiche Höhe, Gelb bleibt gleich. Schiebt man den Punkt in die linke obere Ecke, ist Gelb ein halbes Rechteck 8 × 4 = 16 – genau das Quadrat.

**#28 x = 28.** Von einem Punkt aus sind beide Tangenten an einen Kreis gleich lang. Darum ist der Umfang des gelben Dreiecks genau eine Sechseckseite. Die dritte Seite folgt aus dem 120°-Winkel: √(8² + 7² + 8 · 7) = 13. Also x = 8 + 7 + 13 = 28.

**#29 Fläche = 150.** Die zwei Teildreiecke und das ganze Dreieck haben dieselbe Form; ihre Inkreisradien verhalten sich wie die langen Seiten. Darum gilt Pythagoras auch für die Radien: 3² + 4² = 5². Das Dreieck hat die Form 3-4-5 (Inkreisradius 1) und ist 5-mal so groß: 15, 20, 25. Fläche 150.

**#30 Gesamtfläche = 12.** Das Zwölfeck besteht aus 12 Mittelpunktsdreiecken mit je R²/4. Die Kappe ist drei solche Dreiecke minus das rechtwinklige Dreieck aus Mittelpunkt und Sehnenenden (R²/2): 3 · R²/4 − R²/2 = R²/4. Die Kappe ist also ein Zwölftel: Gesamtfläche 12.

**#31 Grün = 11.** Das Dreieck aus linker Seite und Punkt rechts ist ein halbes Quadrat und hat die Fläche 5 · 4 : 2 = 10. Also ist das Quadrat 20. Links fehlt Grün das Dreieck 4 · 2 : 2 = 4 (Pythagoras), oben rechts das Dreieck √20 · √5 : 2 = 5. Grün = 20 − 4 − 5 = 11.

**#32 r : R = 2 : 3.** Vom Schnittpunkt der Schenkel aus ist das obere Teiltrapez eine verkleinerte Kopie des unteren. Darum 4 : m = m : 9, die Mittellinie ist m = 6. Der Maßstab 4 : 6 = 2 : 3 gilt auch für die Radien – nicht 4 : 9.

**#33 Fläche = 168.** Die Winkelhälften an einem Schenkel ergeben zusammen 90°, der Radius ist die Höhe im rechtwinkligen Dreieck: r² = 4 · 9, also r = 6. Rechts: 3 · x = 36, also x = 12. Grundseiten 4 + 3 = 7 und 9 + 12 = 21, Höhe 12. Fläche (7 + 21) : 2 · 12 = 168.

**#34 Grün = 9π.** Die Berührpunkte liegen auf den Verbindungen der Mittelpunkte, und von jedem Mittelpunkt aus sind seine zwei Berührpunkte gleich weit weg. Grün ist also der Inkreis des Mittelpunktsdreiecks 10-10-12. Fläche 48, halber Umfang 16, Radius 3. Grün = 9π.

## Prüfungen
- Jede Lösung mit 10–40 zufälligen Figuren nachgerechnet (`nr-XX.py`, Funktion `pruefen`), Eindeutigkeit geprüft.
- Ideen: 20 Kandidaten (4 aus dieser Sitzung, 16 vom Ideengeber). Die Bekanntheitsprüfung hat 12 als Standardrätsel aussortiert, darunter auch eine eigene Idee („Pizza-Satz“ im gleichseitigen Dreieck).
