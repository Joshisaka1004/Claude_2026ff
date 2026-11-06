# Klassische Georätsel – Serie 003 (06.11.2026, #35–#38)

Erstellt mit `/georaetsel` im Stil „bunt“. Jede Karte gibt es als Aufgabe und als Lösung, auf Deutsch und Englisch, im Ordner `png/`.
`nr-XX.py` rechnet die Lösung mit zufällig veränderten Figuren nach und zeichnet die Karten; `python3 render.py` erzeugt alle PNGs neu.

## Einstellungen
- Anzahl: 4 · Stufe: schwer · Sprachen: Deutsch + Englisch
- Modelle (gemischt): Rechnen, Zeichnen, Entscheiden – diese Sitzung; Ideengeber – Opus; Bekanntheitsprüfer – Opus und Fable (mit Websuche); Kaltlösen – Opus; Kaltlesen – Sonnet

## Übersicht

| Nr. | Titel | Form · Frageart · Trick | Herkunft | Bekanntheit (Opus / Fable) | Note (Opus / Fable) | Lösung |
|---|---|---|---|---|---|---|
| 35 | Gelb = ? | Halbkreis + zwei Quadrate · Fläche · Spiegel-Dreieck, Seitenhalbierende ⟂ | Invariantensuche (diese Sitzung) | b / b | 4 / 3 | 9 |
| 36 | Grün : Raute = ? | Raute 60° + Inkreis · Flächenverhältnis · Punktspiegelung + Tangentenstücke | Invariantensuche (Ideengeber) | b / b | 3 / 3 | 3 : 8 |
| 37 | Gelb : Blau = ? | Kreis + gleichseitiges Dreieck · Flächenverhältnis · Drehung um 60° + 120°-Flächen | Invariantensuche (diese Sitzung) | b / b | 3 / 3–4 | 1 : 1 |
| 38 | R : r = ? | 3-4-5-Dreieck + zwei Kreise · Radienverhältnis · gemeinsame Sehne + Sonderlage | Invariantensuche (Ideengeber) | b / b | 3–4 / 2–3 | √2 : 1 |

Was ist neu?
- **#35:** Bekannt ist die Familie „Quadrate über den Seiten eines Thales-Dreiecks“. Neu ist das Dreieck aus den äußeren Ecken und dem höchsten Bogenpunkt: Es bleibt immer gleich groß.
- **#36:** Bekannt ist die Tangente am Inkreis eines Quadrats (Umfang des Eckdreiecks). Neu sind die 60°-Raute und die Fläche bis zur Gegenecke.
- **#37:** Bekannt ist der Satz von van Schooten (PA = PB + PC). Neu ist die Flächenfrage: Das Viereck BXYC ist so groß wie das Dreieck.
- **#38:** Bekannt ist das Verhältnis der Umkreise zweier Teildreiecke. Neu ist der Inkreismittelpunkt statt einer Ecke und das 3-4-5-Dreieck.

Aussortiert: zwei Kandidaten, weil die Prüfer sie als Standardrätsel oder Lemma ohne eigenen Dreh einstuften (Quadrat mit Halbkreis, x = √(4 · 9); innen berührende Kreise mit Tangente). Zwei weitere passten nicht zur Vielfalt der Serie.

## Lösungswege in leichter Sprache

**#35 Gelb = 9.** Der Winkel bei P ist ein rechter (Thales). Darum liegen die zwei äußeren Quadratecken auf den Verlängerungen von BP und AP. Das Dreieck aus P und diesen Ecken hat dieselben Schenkel wie APB: Seine lange Seite ist 6. Ihre Mitte M liegt 3 von P entfernt, senkrecht über AB – UM ist also eine Kopie von OP und steht senkrecht auf der langen Seite. Gelb = 6 · 3 : 2 = 9, egal wo P liegt.

**#36 Grün : Raute = 3 : 8.** C ist das Spiegelbild von A am Mittelpunkt O. Daraus folgt: Grün = Dreieck AXY + XY · r. Weil der Kreis das Eckdreieck von außen berührt, ist Dreieck AXY = r · (AT − XY). Zusammen: Grün = r · AT, so groß wie das Drachenviereck aus A, den Berührpunkten und O. In der 60°-Raute ist das 3/8 der Raute – egal wo die Tangente liegt.

**#37 Gelb : Blau = 1 : 1.** Der Winkel APB ist 60°, also ist APX gleichseitig. Eine Drehung um A um 60° zeigt BX = PC und ebenso CY = PB. Gelb = Dreieck PXY − Dreieck PBC; beide haben bei P 120°. Mit dem Kosinussatz bleibt √3/4 · BC² – genau Blau.

**#38 R : r = √2 : 1.** Beide Kreise haben die Sehne IP. Von A aus sieht man sie unter dem halben Winkel bei A, von B aus unter dem halben Winkel bei B. Darum hängt R : r nicht von P ab. Legt man P auf den Berührpunkt des Inkreises, sind AI = √10 und BI = √5 Durchmesser. R : r = √2 : 1.

## Prüfungen
- Jede Lösung mit 40–200 zufälligen Figuren nachgerechnet (`nr-XX.py`, Funktion `pruefen`).
- Ideen: 24 eigene Figuren durchsucht (3 Funde), dazu 8 Ideen vom Ideengeber (7 davon aus der Invariantensuche).
