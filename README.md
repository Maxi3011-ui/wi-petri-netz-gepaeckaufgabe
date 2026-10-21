# Gepäckaufgabe als Petri-Netz (Wirtschaftsinformatik, S. 27)

Fertige **`.hps`-Dateien** für HPSim/HPetriSim zum Herunterladen am Schul-PC,
dazu die Lösungen der Aufgaben von Seite 26.

## Herunterladen

Am einfachsten über die Downloadseite:
**https://maxi3011-ui.github.io/wi-petri-netz-gepaeckaufgabe/**

Oder direkt hier im Repo unter `dateien/` auf die Datei klicken und auf
**„Download raw file"** (der Knopf mit dem Pfeil nach unten) gehen.
Nicht den angezeigten Text kopieren – es ist eine Binärdatei.

| Datei | Inhalt |
|---|---|
| `dateien/gepaeckaufgabe.hps` | das Netz aus **M1** im Buch, unverändert |
| `dateien/gepaeckaufgabe-verbessert.hps` | Verbesserung: zweiter Schalter, zweiter Verlader, größerer Puffer |
| `loesungen.md` | Antworten auf die Aufgaben 1–7 von Seite 26 |

## Öffnen

1. HPSim starten (das Programm aus dem Buch, QR-Code 82111-03).
2. **Datei → Öffnen**, die `.hps`-Datei auswählen.
3. Mit dem Startknopf die Simulation laufen lassen. Die Marken wandern dann wie
   in M3 durch das Netz.

**Kein HPSim auf dem Rechner?** Dieselben Dateien lassen sich ohne Installation
im Browser öffnen unter <https://hpsim.vercel.app> (File → Open). Das ist ein
freier Nachbau, der dasselbe Dateiformat liest.

## Das Modell

```
Passagiere ──> aufgeben ──> Schalterbereich ──> wiegen ──> Gepäcklager ──> verladen ──> Flugzeug
   50/50          2 ZE            0/5            1 ZE         0/50          5 ZE         0/50
```

Oben: Marken/Kapazität der Plätze. Unten: Zeitbedarf der Transitionen.
Alle Kanten haben das Gewicht 1.

## Was die Simulation zeigt

| Variante | Dauer für 50 Gepäckstücke | Ersparnis |
|---|---|---|
| Buchmodell | **253 ZE** | – |
| nur zweiter Check-in-Schalter | 253 ZE | **0 %** |
| nur zweiter Verlader | **130 ZE** | **49 %** |
| zweiter Schalter **und** zweiter Verlader | 129 ZE | 49 % |
| ein Schalter, drei Verlader | 106 ZE | 58 % |

Der Engpass ist das **Verladen** (5 ZE je Stück → 50 × 5 = 250 ZE). Ein zweiter
Schalter beschleunigt eine Station, die gar nicht bremst, und bringt deshalb
exakt nichts. Mit drei Verladern wandert der Engpass zum Aufgeben – dann lohnt
sich der zweite Schalter plötzlich doch. Begründung siehe `loesungen.md`,
Aufgabe 3.

## Wie die Dateien entstanden sind

`.hps` ist ein Binärformat (MFC-CArchive von HPSim), kein XML. Unter `werkzeug/`
liegt alles, womit die Dateien erzeugt wurden:

| Datei | Zweck |
|---|---|
| `werkzeug/hps.py` | Leser und Schreiber für das `.hps`-Format |
| `werkzeug/bauen.py` | baut die beiden Netze |
| `werkzeug/simulieren.py` | rechnet die Durchlaufzeiten der Tabelle oben |

Neu erzeugen:

```
python3 werkzeug/bauen.py dateien
```

Geprüft wurde gegen echte HPSim-Dateien und zusätzlich mit dem unabhängigen
Leser aus <https://github.com/jeremybacher/hpsim> – beide lesen die erzeugten
Dateien mit identischem Ergebnis.
