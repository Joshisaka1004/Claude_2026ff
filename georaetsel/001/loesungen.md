# Klassische Georätsel – Serie 001 (06.11.2026, #19–#26)

Erstellt mit `/georaetsel`. Jede Karte gibt es als Aufgabe und als Lösung, jeweils auf Deutsch und Englisch, im Ordner `png/`.
`nr-XX.py` rechnet die Lösung mit zufällig veränderten Figuren nach und zeichnet die Karten; `python3 render.py` erzeugt alle PNGs neu.

| Nr. | Titel | Figur | Aha | Lösung | Stufe |
|---|---|---|---|---|---|
| 19 | Grün = ? | zwei Quadrate, Ecke im Mittelpunkt | Drehung um 90°: die Überlappung ist immer ein Viertel | 9 | leicht |
| 20 | Grün = ? | Rechteck, Punkt auf der Diagonale | Gleiches minus Gleiches: die Rechtecke neben der Diagonale sind gleich groß | 6 | leicht |
| 21 | Gelb : Grün = ? | gleichseitiges Dreieck, Inkreis, Umkreis | R = 2r, also vierfache Fläche | 3 : 1 | leicht |
| 22 | x = ? | Quadrat mit aufgesetztem gleichseitigem Dreieck | verstecktes gleichschenkliges Dreieck | 30° | mittel |
| 23 | Grün = ? | Dreieck mit zwei Linien zu Seitenmitten | dritte Linie ergänzen: sechs gleich große Dreiecke | 8 | mittel |
| 24 | Grün = ? | regelmäßiges Achteck | Zerlegen: das Mittelrechteck ist das halbe Achteck | 14 | mittel |
| 25 | Grün = ? | Viertelkreis mit Rechteck | die Rechteck-Diagonale ist ein Radius | 12 | mittel |
| 26 | Grün gesamt = ? | drei Halbkreise | nur die Strecke 6 zählt: Grün = Kreis über dieser Strecke | 9π ≈ 28,3 | schwer |

## Lösungswege in leichter Sprache

**#19 Grün = 9.** Zeichne vom Mittelpunkt zwei Linien zur Mitte der rechten und der oberen Seite. Sie schneiden ein Viertel ab. Das Stück, das Grün unten fehlt, kommt oben links dazu – gedreht um 90° ist es dasselbe Dreieck. Grün ist also immer ein Viertel: 36 : 4 = 9. Wie das zweite Quadrat gedreht ist, spielt keine Rolle.

**#20 Grün = 6.** Die Diagonale halbiert das große Rechteck und auch die zwei kleinen Rechtecke, durch die sie läuft. Zieht man von beiden Hälften die gleichen Dreiecke ab, bleiben links oben 6 und rechts unten Grün übrig. Also Grün = 6 – egal, wo der Punkt auf der Diagonale liegt.

**#21 Gelb : Grün = 3 : 1.** Mittelpunkt, Ecke und Berührpunkt bilden ein halbes gleichseitiges Dreieck (Winkel 30°, 60°, 90°). Darum ist der große Radius doppelt so lang wie der kleine. Doppelter Radius heißt vierfache Fläche. Gelb ist der große Kreis ohne den grünen: 4 − 1 = 3.

**#22 x = 30°.** Die linke Dreiecksseite ist so lang wie die linke Quadratseite. Das schmale Dreieck links hat also zwei gleich lange Seiten. Sein Winkel oben links ist 90° + 60° = 150°, die beiden anderen sind je 15°. Rechts genauso. x = 60° − 15° − 15° = 30°.

**#23 Grün = 8.** Ergänze die dritte Linie von der Spitze durch den Schnittpunkt zur Mitte der unteren Seite. Die drei Linien teilen das Dreieck in sechs gleich große Dreiecke (je zwei Nachbarn an einer halbierten Seite haben gleiche Grundseite und gleiche Höhe). Grün besteht aus zwei davon: 2 · 4 = 8.

**#24 Grün = 14.** Zwei waagerechte Hilfslinien zerlegen das Achteck. Das linke Stück besteht aus einem Streifen und zwei Ecken; die zwei Ecken sind zusammen ein halbes Mittelquadrat. Grün besteht aus zwei solchen Streifen und einem ganzen Mittelquadrat – das ist doppelt so viel. Grün = 2 · 7 = 14.

**#25 Grün = 12.** Die Diagonale vom Mittelpunkt zur Ecke auf dem Bogen ist ein Radius r. Die Seiten sind r − 2 und r − 1. Pythagoras: (r − 2)² + (r − 1)² = r², also r = 5. Das Rechteck ist 3 × 4, Grün = 12.

**#26 Grün = 9π.** Kleine Radien a und b, großer Radius a + b. Grün = π/2 · ((a + b)² − a² − b²) = π · a · b. Nach dem Höhensatz im Thales-Dreieck ist 6² = 2a · 2b, also a · b = 9. Grün = 9π – genau so groß wie der Kreis mit der Strecke 6 als Durchmesser. Wo die Strecke steht, ist egal.

## Prüfungen
- Jede Lösung mit 10–40 zufälligen Figuren nachgerechnet (`nr-XX.py`, Funktion `pruefen`).
- Redundanz: Jede Karte hat nur die nötigen Angaben (eine Zahl bzw. zwei Längen bei #25).
- Kaltlösen: Ein frischer Prüfer hat alle 8 Karten nur aus dem Bild richtig gelöst. Befund: Bei #26 war unklar, ob die ganze grüne Fläche gemeint ist → Titel „Grün gesamt = ?“. Bei #25 war der Mittelpunkt nicht markiert → roter Punkt.
- Kaltlesen (DE + EN): „?“ aus dem Verhältnis-Kreis #21 entfernt; Zusatzzeile bei #23 gestrichen (einheitlich mit den anderen Karten), Stichwort „Dreieck“; #25 Stichwort „Viertelkreis und Rechteck“; #22 ohne bedeutungslose Farbfüllung; #20 blaues Feld länglicher (sah wie ein Quadrat aus); #26 Zahl 6 freigestellt.
- Zweiter Kaltlese-Durchgang: alle Karten ok bis auf #26 → Länge 6 jetzt als Maßlinie (nicht als Flächenzahl lesbar), „?“ nur im Titel, weil Grün aus zwei Teilen besteht.
