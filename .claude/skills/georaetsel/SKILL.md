---
name: georaetsel
description: "Use when Jochen types /georaetsel or asks for classic geometry puzzle cards (klassische Georätsel): one clean figure, a title question like „Grün = ?“, „Gelb : Rot = ?“ or „r : R = ?“, markings instead of text, a hidden aha. First asks interactively for number, difficulty, languages and which models do idea-finding and checking; then creates new, not widely known puzzles as PNG cards (puzzle + solution) with verified solutions and an iPad gallery."
---

# /georaetsel – klassische Georätsel

Ziel: neue, eigene Geometrie-Rätselkarten im **klassischen Stil** – so wie die Vorlagen in `referenz/`: eine saubere Figur, eine kurze Frage als Titel, fast kein Text, ein echter Aha-Moment. Die Rätsel sollen **nicht schon hundertfach bekannt** sein. Jede Karte als PNG für Aufgabe und Lösung, fertig geprüft, mit Lösungsblatt und Galerie für das iPad.

Unterschied zu /ahaaufgaben: Dort sind auch Alltag, 3D, Längen-Geschichten erlaubt. Hier **nur ebene Geometrie, keine Einkleidung, kein Fließtext**. Die Figur trägt die ganze Aufgabe.

## 0. Zuerst abfragen (Pflicht, vor jeder anderen Arbeit)

Mit dem Tool `AskUserQuestion` **in einem einzigen Aufruf** diese vier Fragen stellen. Gibt es das Tool nicht, dieselben Fragen in einer kurzen Chat-Nachricht mit den Vorschlägen stellen und auf die Antwort warten.

1. **Anzahl** (Kopf „Anzahl“): Optionen „4“, „8 (Empfohlen)“, „12“. Eigene Zahl über „Other“.
2. **Schwierigkeit** (Kopf „Stufe“, Mehrfachauswahl): „leicht“, „mittel“, „schwer“, „sehr schwer“. Die Karten werden gleichmäßig auf die gewählten Stufen verteilt.
3. **Sprachen** (Kopf „Sprachen“): „Deutsch + Englisch (Empfohlen)“, „nur Deutsch“, „nur Englisch“.
4. **Modelle** (Kopf „Modelle“): wer welche Rolle übernimmt (Rollen siehe unten):
   - „Gemischt (Empfohlen)“: Ideen von dieser Sitzung plus zweite Ideenliste von Opus; Bekanntheitsprüfung und Kaltlösen Opus; Kaltlesen Sonnet.
   - „Alles Opus“: alle Helfer-Rollen mit Opus.
   - „Schnell (Sonnet)“: alle Helfer-Rollen mit Sonnet – schneller, etwas weniger gründlich.
   - „Mit Fable“: zweite Ideenliste von Fable, Prüfer Opus.
   Über „Other“ kann Jochen jede Rolle einzeln festlegen (z. B. „Ideen Fable, Kaltlösen Opus, Kaltlesen Haiku“).

Abkürzung: Stehen die Antworten schon hinter dem Befehl (z. B. `/georaetsel 8 mittel,schwer de+en opus`), nur noch nach dem Fehlenden fragen. Erkennbare Wörter: Zahl; leicht/mittel/schwer/sehr schwer; de, en, de+en; gemischt, opus, sonnet, fable.

**Rollen und Modelle.** Diese Sitzung selbst rechnet, zeichnet und entscheidet; ihr eigenes Modell kann der Befehl nicht wechseln (dafür vor dem Start `/model`). Die Helfer-Rollen laufen als frische Subagenten (Agent-Tool, `subagent_type: general-purpose`) mit dem gewählten Modell im Parameter `model` (`opus`, `sonnet`, `haiku`, `fable`):
- **Ideengeber** – liefert eine zweite, unabhängige Ideenliste (siehe 3.2).
- **Bekanntheitsprüfer** – sagt, welche Ideen schon bekannt sind (siehe 3.3).
- **Kaltlöser** – löst die fertigen Karten nur aus dem Bild (siehe 3.6).
- **Kaltleser** – liest Text und Skizze Korrektur (siehe 3.6).
Die gewählte Belegung kommt ins Lösungsblatt.

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

## 2. Nicht schon 100× bekannt

Jedes Geometrie-Rätsel beruht auf bekannten Sätzen – das ist in Ordnung. Aber die **konkrete Figur mit ihrer Frage** darf kein Standardrätsel sein, das man in Schulbüchern, Wettbewerben oder Social-Media-Sammlungen ständig sieht.

**Sperrliste** – diese Konstellationen nie als Kern verwenden (auch nicht mit anderen Zahlen oder gespiegelt):
- Ecke eines Quadrats im Mittelpunkt eines anderen (Überlappung = ¼)
- Punkt auf der Rechteck-Diagonale, Ergänzungsrechtecke gleich groß
- Inkreis/Umkreis des gleichseitigen Dreiecks (R = 2r, Ring 3 : 1)
- gleichseitiges Dreieck in/auf einem Quadrat, Winkel 150° bzw. 30° bzw. 15°
- Seitenhalbierende → sechs gleiche Dreiecke
- drei Halbkreise mit Lot (Arbelos, Kreis über dem Lot)
- Rechteck im Viertelkreis, Diagonale = Radius (3-4-5)
- Möndchen des Hippokrates; Halbkreise über den Seiten eines rechtwinkligen Dreiecks
- Schmetterling im Trapez (seitliche Dreiecke gleich, Produkt gegenüberliegender Flächen)
- Quadrat im Halbkreis gegen Quadrat im Kreis (2 : 5)
- zwei Quadrate nebeneinander, Dreieck = halbes großes Quadrat
- Punkt im Rechteck/Parallelogramm mit allen Ecken verbunden (gegenüberliegende Paare = halbe Fläche); Punkt im regelmäßigen Sechseck mit allen Ecken verbunden
- Rechteck aus zwei gegenüberliegenden Seiten im regelmäßigen Achteck (= halbes Achteck)
- Viviani (Summe der Abstände im gleichseitigen Dreieck), Pizza-Satz
- vier gleiche Kreise im Quadrat mit kleinem Quadrat in der Mitte
- alle Motive aus `referenz/` und aus früheren Serien (siehe 3.1)
Die Liste nach jeder Serie um neu entdeckte Standardmotive ergänzen.

**So entstehen frische Rätsel:**
- **Zwei Ahas verketten:** Das Ergebnis des ersten Tricks ist die Zutat des zweiten (z. B. eine Flächengleichheit liefert ein Verhältnis, das dann in einem Kreis weiterwirkt).
- **Ungewohnte Formen kombinieren:** regelmäßiges Fünf-, Zehn- oder Zwölfeck, zwei verschiedene regelmäßige Vielecke an einer gemeinsamen Seite, Viertelkreise in Rechtecken, drei Quadrate in einer Reihe mit einem Kreis, Kreisbögen statt Strecken.
- **Den Klassiker umdrehen:** Was dort gegeben ist, wird gesucht, und umgekehrt – aber nur, wenn dadurch wirklich ein neuer Gedanke nötig wird.
- **Eine überraschende Unabhängigkeit suchen:** Python-Experimente mit zufälligen Figuren: Welche Größe bleibt konstant, obwohl sich alles bewegt? Solche Funde sind die besten Rätsel.
- **Ungewohnte Frageart:** Verhältnis statt Fläche, Winkel in einer Flächenfigur, Länge aus Flächen.
Pro Idee in der Tabelle eine Spalte **„Was ist neu?“**: ein Satz, was diese Figur von der bekanntesten verwandten Aufgabe unterscheidet. Wer diesen Satz nicht schreiben kann, hat keine neue Idee.

## 2a. Aha-Zutaten (Bausteine, keine fertigen Rätsel – gut mischen)

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
- Alle bisherigen Serien suchen und jede `loesungen.md` lesen: `/mnt/project-files/aufgaben-*/`, `/mnt/project-files/georaetsel-*/` und im Repo `georaetsel/*/` bzw. `/mnt/project-files/georaetsel/*/` (was davon existiert). Daraus die Liste benutzter Motive bilden. Kein Motiv wiederholen.
- Nummer: höchste bisher benutzte Nummer + 1 (gemeinsame Zählung mit /ahaaufgaben). Datum = heute, Format `TT.MM.JJJJ`.
- Den Skill `raetselgrafik-pruefung` laden und befolgen. Wo er Text verlangt, gilt hier zuerst: **eine Marke in der Figur statt eines Satzes**. Nur was sich nicht zeichnen lässt, kommt als eine kurze Zeile dazu.

### 3.2 Ideen
- Etwa doppelt so viele Ideen sammeln wie Karten gewünscht – die Bekanntheitsprüfung siebt aus.
- Eigene Ideen dieser Sitzung **plus** eine unabhängige Liste vom **Ideengeber** (gewähltes Modell). Auftrag an ihn: Stilregeln aus Abschnitt 1, Sperrliste aus Abschnitt 2, die Liste schon benutzter Motive, gewünschte Stufen; er soll ebenfalls doppelt so viele Ideen liefern, jede mit Figur, Gegeben, Gesucht, Aha, vermuteter Lösung und „Was ist neu?“. Seine Ideen werden hier nachgerechnet wie die eigenen, nie ungeprüft übernommen.
- Eine Tabelle: Nr. · Figur · Gegeben · Gesucht · Aha · Lösung · Stufe · Was ist neu?
- Stufen nach Jochens Auswahl gleichmäßig verteilen. „Sehr schwer“ heißt: zwei Ahas hintereinander oder ein gut versteckter Trick; trotzdem glattes Ergebnis.
- Fragearten gemischt: Fläche, Verhältnis, Winkel, Länge, höchstens ein Beweis pro Serie. Jede Karte ein eigener Aha-Typ.

### 3.3 Bekanntheitsprüfung (Pflicht, vor dem Zeichnen)
1. **Bekanntheitsprüfer** (frischer Subagent, gewähltes Modell) bekommt nur die Ideen als kurze Beschreibung – ohne Lösungen. Auftrag: „Bewerte jede Idee: (a) Standardrätsel, kenne ich in genau dieser Form; (b) nahe Verwandte bekannt – nenne die bekannte Aufgabe und was hier anders ist; (c) mir unbekannt. Sei streng: Lieber einmal zu oft ‚bekannt‘ sagen.“
2. Falls die Websuche verfügbar ist: für jede Idee mit (b) oder (c) eine kurze Suche nach der Kernfigur (z. B. „square inscribed quarter circle area puzzle“). Taucht die Figur mit derselben Frage als bekanntes Rätsel auf → wie (a) behandeln.
3. (a) verwerfen. (b) nur behalten, wenn der Unterschied einen neuen Gedanken verlangt – sonst abwandeln und erneut prüfen. Aus den übrigen die gewünschte Anzahl auswählen, Stufen und Aha-Typen gut gemischt.
4. Im Lösungsblatt pro Karte die Einstufung (b/c) und den Satz „Was ist neu?“ festhalten.

### 3.4 Rechnen und Bestimmtheit (Pflicht, Python)
Für jede Karte ein kleines Skript `nr-XX.py` (wird mit ausgeliefert):
1. Die Figur aus wenigen freien Größen bauen (z. B. Seitenlänge, Lage eines Punktes). Alle Punkte daraus berechnen.
2. **Bestimmtheitsprüfung:** Die freien Größen zufällig variieren (mindestens 20 Fälle), dabei die gegebenen Angaben erzwingen (direkt oder mit `scipy.optimize`). Die gesuchte Größe muss in allen Fällen gleich sein. Schwankt sie, fehlt eine Angabe → Marke oder Zahl ergänzen.
3. **Redundanzprüfung:** Jede Angabe einzeln weglassen. Bleibt die Lösung trotzdem fest, die Angabe streichen (außer sie ist das Aha, z. B. „egal wo der Punkt liegt“ – dann bewusst so lassen und im Lösungsblatt erwähnen).
4. Die gezeichnete Instanz ist einer dieser Fälle; ihre Flächen müssen genau die aufgedruckten Zahlen haben (mit shapely nachmessen).
5. Ergebnis exakt (Bruch, Wurzel, π) und als Dezimalzahl notieren.

### 3.5 Zeichnen
- Baukasten benutzen: `scripts/karte.py` (Karte, Flächen, Kreise, Strichmarken, Parallelpfeile, rechte Winkel, Winkelbögen, Punkte, Maßlinien, Kontaktbogen). Bei Bedarf `pip install matplotlib shapely scipy pillow`.
- Format 1100 × 1100 px, weißer Grund, Schrift Inter. Titel fett oben, ggf. eine Zeile darunter, Figur in der Mitte, Stichwort kursiv darunter, Datum + #Nr senkrecht links, Signatur unten: `#GeoRätsel` (DE) bzw. `#GeoPuzzle` (EN). Nie den Namen eines fremden Autors.
- Farben aus dem Baukasten: `GRUEN` für das Gesuchte, `HELLBLAU`, `GELB`, `ROT`, `GOLD`, `ORANGE`, `VIOLETT` für gegebene oder verglichene Flächen. Höchstens drei Füllfarben pro Karte.
- Marken (Striche, Pfeile, Winkel) erst nach den Umrissen zeichnen – ihre Größe richtet sich nach der Figur.
- Zahlen mittig in ihre Fläche, nie auf eine Linie; gesuchte Fläche mit „?“ in `GRUEN_TXT`.
- Zu jeder Aufgabe eine **Lösungskarte** (`Loesungskarte` im Baukasten): Antwort als Titel, dieselbe Figur mit gestrichelten Hilfslinien und Farben, die den Trick zeigen, darunter der Lösungsweg in 3–5 kurzen Sätzen (Trick zuerst).
- Nur die gewählten Sprachen rendern. Dateinamen: `XX-kurzname-aufgabe-de.png`, `XX-kurzname-loesung-de.png` (EN entsprechend), Ordner `png/`. Ein `render.py` rendert alles auf einmal (Vorlage: `georaetsel/001/render.py` im Repo).
- Kontaktbogen aller Karten bauen und ansehen, dann jede Karte in voller Größe. Mängel sofort beheben.

### 3.6 Prüfen (Pflicht)
Kaltleser und Kaltlöser laufen mit den in Abschnitt 0 gewählten Modellen, parallel im Hintergrund. Beide bekommen nur die Pfade der Aufgaben-PNGs und die Zeichensprache aus Abschnitt 1, ausdrücklich keine Lösungskarten, Skripte oder `loesungen.md`.
1. **Kaltlesen** wie in `raetselgrafik-pruefung` (frischer Subagent, alle Aufgaben-PNGs in allen gewählten Sprachen, keine Lösungen). Zusätzlich fragen: „Gibt es Text, den die Skizze schon zeigt oder der durch eine Marke ersetzbar wäre?“
2. **Kaltlösen:** Ein zweiter frischer Subagent bekommt nur die Aufgaben-PNGs einer Sprache und löst jede Karte: Antwort plus Lösungsidee in 2–3 Sätzen, und welche Annahmen er treffen musste. Abweichung von der eigenen Lösung → klären: Ist die Figur mehrdeutig (Punkt auf Seite oder in Ecke? Berührung oder Schnitt? parallel oder nicht?), fehlt eine Marke, oder irrt der Agent? Musste er etwas annehmen, das nicht markiert ist → Marke ergänzen. Fand er eine Karte sofort „aus dem Lehrbuch bekannt“ → zurück zu 3.3.
3. Korrigieren, neu rendern, ansehen; zweiter Durchgang nur für Befunde hoch/mittel.

### 3.7 Ausliefern
- **Jeder Auftrag bekommt einen eigenen, fortlaufend nummerierten Ordner** mit drei Ziffern: `georaetsel/001/`, `georaetsel/002/` … Gibt es noch keinen, ist es `001`; ist `005` der höchste, kommt `006`. Lücken nicht auffüllen, bestehende Ordner nie überschreiben. Anlegen mit `python3 <skill>/scripts/naechster_ordner.py <repo>/georaetsel` (gibt den neuen Pfad aus; den Basisordner immer angeben). Den Ordner gleich zu Beginn der Arbeit anlegen (nach der Abfrage), damit Skripte und Bilder von Anfang an dort liegen.
- Ort: im Repo `georaetsel/NNN/`. Gibt es kein Repo, aber `/mnt/project-files`, dann `/mnt/project-files/georaetsel/NNN/` (Skript mit diesem Basisordner aufrufen).
- Inhalt: `png/` mit allen Aufgaben- und Lösungskarten, alle `nr-XX.py`, `render.py`, `loesungen.md` (oben Datum und Kartennummern der Serie), ZIP mit allem.
- `loesungen.md`: gewählte Einstellungen (Anzahl, Stufen, Sprachen, Modelle je Rolle), Tabelle Nr. · Titel · Aha · Was ist neu? · Bekanntheit (b/c) · Lösung · Stufe, danach pro Karte der kurze Lösungsweg in leichter Sprache (3–6 Sätze, der Trick zuerst), zuletzt die Prüfbefunde und was geändert wurde.
- Im Repo: committen und auf den vorgegebenen Branch pushen.
- Galerie-Artifact veröffentlichen: Karten als JPG neben der Seite, Schalter Deutsch/English, unter jeder Karte die eingeklappte Lösungskarte (Vorlage: Galerie der Serie 001). Bei nur einer Sprache entfällt der Schalter. Jochen öffnet die Galerie auf dem iPad – sie ist der Hauptweg (ZIPs gehen dort nicht).
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
