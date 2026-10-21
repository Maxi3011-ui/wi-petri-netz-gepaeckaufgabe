# Lösungen – Verbesserung von Geschäftsprozessen (S. 26/27)

> **Hinweis:** Die Aufgaben 1 und 4 verweisen auf **M1** und **M2**, die auf den
> Seiten davor stehen. Die habe ich nicht vorliegen – die Antworten sind deshalb
> aus der Sache heraus geschrieben und passen auf jedes übliche M1 (Check-in-Prozess)
> und M2 (statisches Prozessmodell, z. B. EPK oder Flussdiagramm). Wenn dort etwas
> Bestimmtes abgebildet ist, bitte kurz sagen, dann ziehe ich es nach.

---

## 1 Verbesserungsvorschläge: Wie wird der Check-in kürzer?

**Den Schalter ganz vermeiden**

- **Online- und Mobile-Check-in** vor der Anreise: Die Bordkarte liegt als Code
  auf dem Handy, der Schalterbesuch entfällt für alle ohne Aufgabegepäck.
- **Gepäckanhänger selbst drucken** (Self-Tagging) am Automaten oder als
  wiederverwendbarer elektronischer Anhänger, danach nur noch **Self-Bag-Drop**:
  Koffer auf das Band stellen, fertig.

**Den Schalter beschleunigen**

- **Mehr Stationen parallel** in der Spitzenzeit statt eines einzelnen Schalters.
- **Ströme trennen:** eigene Spuren für „nur Handgepäck", „Gepäckabgabe" und
  Sonderfälle (Sperrgepäck, Tiere, Betreuung). Ein einziger Sonderfall blockiert
  sonst alle Wartenden dahinter.
- **Einmal erfassen, überall nutzen** (One-ID): Pass und Gesicht werden einmal
  hinterlegt, danach genügt an Gepäckabgabe, Kontrolle und Gate ein Blick in
  die Kamera statt erneuter Dokumentenprüfung.
- **Zeitfenster buchen:** Die App weist einen Abgabezeitraum zu und verteilt die
  Ankünfte, statt dass alle zur selben Minute kommen.

**Dahinter weitermachen**

- **Gepäckförderung mit RFID statt Barcode:** weniger Lesefehler, weniger
  Nacharbeit von Hand.
- **Mehr Verladekapazität** am Flugzeug – das ist nach der Simulation der
  eigentliche Engpass, siehe Aufgabe 3.

---

## 2 Bewertung vor dem Hintergrund weiterer Ziele des Flughafenbetreibers

Ein Flughafenbetreiber verfolgt nicht nur „schnell". Sein Zielsystem enthält
mindestens:

| Ziel | Wirkung der Vorschläge |
|---|---|
| **Wirtschaftlichkeit** | Automaten senken dauerhaft Personalkosten, kosten aber zuerst Investition, Wartung und Schulung. Sie rechnen sich erst ab einer bestimmten Auslastung. |
| **Sicherheit** | Darf nie dem Tempo geopfert werden. Gepäck- und Personenkontrolle sind gesetzlich vorgeschrieben; „schneller" heißt hier nur „besser organisiert", nicht „weniger geprüft". |
| **Pünktlichkeit / Slot-Treue** | Starke positive Wirkung: Wer die Startzeit verpasst, wartet auf einen neuen Slot. Das kostet mehr als jeder Schalter. |
| **Kapazitätsauslastung** | Kürzere Abfertigung heißt mehr Flüge pro Tag mit demselben Terminal – der größte Hebel überhaupt. |
| **Erlöse aus Läden und Gastronomie** | **Zielkonflikt:** Ein Flughafen verdient erheblich am Einzelhandel. Passagiere, die schneller durch den Check-in kommen, haben mehr Zeit im Sicherheitsbereich – das nützt den Läden. Wer dagegen „gerade noch rechtzeitig" ankommt, kauft nichts. Tempo am Anfang ist also auch wirtschaftlich erwünscht. |
| **Servicequalität und Barrierefreiheit** | **Zielkonflikt:** Nicht alle kommen mit Automaten zurecht – ältere Menschen, Menschen mit Behinderung, Erstflieger, Sprachbarrieren. Es muss weiter bediente Schalter geben, sonst sinkt die Zufriedenheit, obwohl die Zahlen besser aussehen. |
| **Datenschutz** | Gesichtserkennung verarbeitet biometrische Daten. Die sind nach DSGVO besonders geschützt und brauchen eine echte, freiwillige Einwilligung samt Alternative. |
| **Beschäftigte** | Automatisierung baut Arbeitsplätze ab oder verändert sie stark. Das ist mit Betriebsrat und Sozialplan zu klären. |
| **Störungsfestigkeit** | Je digitaler, desto härter trifft ein Ausfall. Es braucht einen Rückfallweg von Hand. |

**Fazit:** Online-Check-in, Self-Bag-Drop und mehr Verladekapazität zahlen auf
fast alle Ziele gleichzeitig ein und sind daher zuerst umzusetzen. Flächendeckende
Gesichtserkennung bringt vergleichsweise wenig Zeitgewinn und erzeugt den größten
rechtlichen und gesellschaftlichen Widerstand – sie gehört ans Ende der Liste.

---

## 3 Zeitökonomische Abschätzung

Gerechnet mit dem Netz aus M1 (50 Passagiere, Aufgeben 2 ZE, Wiegen 1 ZE,
Verladen 5 ZE, Schalterbereich fasst 5). Alle Werte sind mit dem beiliegenden
Modell simuliert, nicht geschätzt:

| Variante | Dauer bis alle 50 Stück im Flugzeug | Ersparnis |
|---|---|---|
| Buchmodell (1 Schalter, 1 Verlader) | **253 ZE** | – |
| **nur** zweiter Check-in-Schalter | **253 ZE** | **0 %** |
| **nur** zweiter Verlader | **130 ZE** | **49 %** |
| zweiter Schalter **und** zweiter Verlader | 129 ZE | 49 % |
| ein Schalter, drei Verlader | 106 ZE | 58 % |
| zwei Schalter, drei Verlader | 89 ZE | 65 % |

**Der entscheidende Satz:** Die Gesamtdauer wird allein vom **Engpass** bestimmt,
hier vom Verladen mit 5 ZE je Stück. 50 × 5 = 250 ZE, plus Anlaufzeit = 253 ZE.
Ein zweiter Schalter beschleunigt eine Station, die gar nicht bremst – er kostet
Geld und bringt **exakt nichts**. Erst der zweite Verlader halbiert die Zeit.

Mit drei Verladern kippt der Engpass: Dann bremst das Aufgeben (50 × 2 = 100 ZE),
und ein zweiter Schalter lohnt sich plötzlich doch (106 → 89 ZE). **Verbesserungen
wirken nur am jeweils engsten Punkt, und der wandert**, sobald man ihn beseitigt.
Genau das lässt sich ohne Simulation nicht erkennen – ein statisches Modell hätte
hier zum teuren Fehlschluss „zweiter Schalter" geführt.

---

## 4 Statische Modellierung: Stärken und Schwächen

| | **Statische Modellierung** (z. B. EPK, Flussdiagramm) | **Dynamische Modellierung** (Petri-Netz, Simulation) |
|---|---|---|
| **Zeigt** | Aufbau: Reihenfolge, Verzweigungen, Zuständigkeiten, Dokumente | Verhalten über die Zeit: Bestände, Wartezeiten, Auslastung |
| **Stärken** | schnell erstellt, ohne Werkzeug lesbar, auch für Fachfremde verständlich, gute Grundlage für Dokumentation, Absprachen und Sollkonzepte, Pflicht z. B. für Zertifizierungen | erkennt Engpässe und Leerlauf, vergleicht Varianten in Zahlen, deckt Verklemmungen und Überläufe auf, erlaubt „Was wäre, wenn" ohne Eingriff in den echten Betrieb |
| **Schwächen** | **kennt keine Zeit und keine Mengen**, Engpässe und Warteschlangen bleiben unsichtbar, Wechselwirkungen zwischen Stationen nicht darstellbar, Aussagen über Kapazität nur geraten | aufwändiger, braucht belastbare Daten (Zeiten, Kapazitäten, Mengen) und ein Programm, Gefahr der Scheingenauigkeit: Das Ergebnis ist nur so gut wie die eingegebenen Werte |
| **Gut für** | Verstehen, Dokumentieren, Kommunizieren, Schulung | Bewerten, Dimensionieren, Investitionsentscheidungen |

**Kurz:** Das statische Modell beantwortet „**Was** passiert in welcher Reihenfolge?",
das dynamische „**Wie lange** dauert es und **wo** klemmt es?". Beides gehört
zusammen – das statische Modell ist der Bauplan, das dynamische der Belastungstest.
Aufgabe 3 ist das Beispiel dafür: Beide Verbesserungen sehen im statischen Modell
gleich gut aus, in Wahrheit bringt eine davon null.

---

## 5 Wie Digitalisierung die Abläufe am Flughafen effizienter macht (M3)

**Bild 1 – Ticketbuchung über einen Chatbot:** Die Buchung läuft ohne Mitarbeiter
und ohne Öffnungszeiten, rund um die Uhr und in vielen Sprachen gleichzeitig.
Die Daten entstehen sofort in der richtigen Form im System – kein Abtippen,
kein Medienbruch, keine Hörfehler am Telefon.

**Bild 2 – Check-in-Automat:** Viele Automaten arbeiten parallel, der Passagier
übernimmt die Arbeit selbst. Aus einer Warteschlange vor wenigen besetzten
Schaltern werden viele kurze. Personal wird frei für die Fälle, die wirklich
Beratung brauchen.

**Bild 3 – Gepäckförderanlage:** Die Koffer werden automatisch sortiert und zum
richtigen Flugzeug gesteuert, erkennbar an den Markierungen im Bild. Das geht
schneller als von Hand, ist rund um die Uhr gleich zuverlässig und jedes Stück
ist jederzeit auffindbar.

**Bild 4 – Gesichtserkennung:** Die Identität wird einmal erfasst und danach
an Kontrolle, Gepäckabgabe und Gate automatisch wiedererkannt. Das spart das
mehrfache Vorzeigen von Pass und Bordkarte und beseitigt Staus an den Übergängen.

**Das gemeinsame Muster:** Digitalisierung wirkt, indem sie **Wartezeiten und
Medienbrüche entfernt**, Arbeit **parallelisiert** (viele Automaten statt weniger
Schalter) und Tätigkeiten auf den Kunden oder die Maschine **verlagert**. Die
einzelne Tätigkeit wird dabei oft nur wenig schneller – gewonnen wird die Zeit
*zwischen* den Tätigkeiten.

---

## 6 Risiken einer fortschreitenden Digitalisierung von Flugreisen

- **Datenschutz:** Biometrische Daten sind besonders schützenswert. Einmal
  abgeflossen, lassen sie sich nicht ändern wie ein Passwort. Wer sie erhebt,
  braucht eine echte Einwilligung und eine zumutbare Alternative.
- **Überwachung:** Aus Buchung, Gesicht und Bewegungsdaten entsteht ein lückenloses
  Bewegungsprofil. Wer darauf zugreifen darf – Behörden, Airlines, Dritte – ist
  oft nicht transparent.
- **Ausfall und Angriff:** Fällt die IT aus, steht der ganze Flughafen. Ein
  Cyberangriff auf die Gepäcksteuerung legt mehr lahm als jeder Personalausfall.
  Es braucht Rückfallwege von Hand und geübte Notfallpläne.
- **Fehler der Technik:** Gesichtserkennung arbeitet nicht bei allen Menschen
  gleich zuverlässig; bei bestimmten Gruppen sind die Fehlerquoten messbar höher.
  Eine Fehlentscheidung kann die Reise kosten, ohne dass jemand sie erklärt.
- **Ausgrenzung:** Wer kein Smartphone hat, die Sprache nicht spricht oder
  schlecht sieht, kommt am Automaten nicht weiter. Digitalisierung darf keine
  Zugangshürde werden.
- **Kein Ansprechpartner:** Wenn alles automatisch läuft, fehlt bei Störungen,
  Umbuchungen oder verlorenem Gepäck der Mensch, der Verantwortung übernimmt.
- **Arbeitsplätze:** Einfache Tätigkeiten fallen weg, die neuen Stellen verlangen
  andere Qualifikationen. Der Übergang trifft nicht dieselben Menschen.
- **Abhängigkeit vom Anbieter:** Wer sein ganzes System auf eine Plattform stützt,
  kann Preise und Bedingungen später kaum noch verhandeln.

---

## 7 Geschäftsprozessanalyse und Modellierung als Grundlage der Digitalisierung

**Man kann nur digitalisieren, was man verstanden hat.** Ein Programm bildet
immer einen Ablauf ab. Ist der Ablauf nicht beschrieben, wird er beim Programmieren
unbewusst erfunden – und passt dann nicht zur Wirklichkeit.

1. **Die Ist-Analyse legt offen, was wirklich passiert**, nicht was im Handbuch
   steht: doppelte Erfassung, Medienbrüche (Papier → Bildschirm), Rückfragen,
   Wartezeiten. Genau diese Stellen sind die lohnenden Ansatzpunkte.
2. **Das Modell ist die gemeinsame Sprache** zwischen Fachabteilung und IT. Ohne
   es reden beide über verschiedene Dinge und merken es erst bei der Abnahme.
3. **Das Soll-Modell ist die Vorgabe für die Software:** Es legt fest, welche
   Schritte automatisch laufen, wo ein Mensch entscheidet, welche Daten an welcher
   Schnittstelle gebraucht werden. Workflow- und ERP-Systeme werden direkt daraus
   eingerichtet.
4. **Erst die Modellierung macht Erfolg messbar.** Nur wer Durchlaufzeit und
   Auslastung vorher kennt, kann nachher belegen, dass die Investition gewirkt hat.
5. **Die dynamische Modellierung prüft die Wirtschaftlichkeit vor dem Kauf.**
   Aufgabe 3 zeigt es: Dieselbe Investitionssumme bringt einmal 0 % und einmal
   49 % Zeitgewinn. Diesen Unterschied erkennt man am Modell, nicht am Prospekt.

**Der Kernsatz:** Wer einen schlechten Prozess digitalisiert, bekommt einen
schnellen schlechten Prozess – und meist einen teuren dazu. Analyse und
Modellierung sorgen dafür, dass zuerst der Ablauf stimmt und erst danach die
Technik kommt. Deshalb stehen sie am Anfang jedes Digitalisierungsvorhabens.
