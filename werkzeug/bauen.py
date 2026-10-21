"""Erzeugt die .hps-Dateien zur Gepaeckaufgabe (Schulbuch S. 27, M1).

Aufruf:  python3 bauen.py <Zielordner>
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hps
from simulieren import simuliere

Y = 300          # Hoehe der Hauptreihe
Y2 = 400         # Hoehe der parallelen zweiten Station
X0, DX = 100, 120

# ---------------------------------------------------------------- Buchmodell

PLACES = [
    # Name,              x,            y, Marken, Kapazitaet
    ('Passagiere',       X0 + 0 * DX, Y, 50, 50),
    ('Schalterbereich',  X0 + 2 * DX, Y,  0,  5),
    ('Gepäcklager',      X0 + 4 * DX, Y,  0, 50),
    ('Flugzeug',         X0 + 6 * DX, Y,  0, 50),
]
TRANS = [
    # Name,       x,            y, Zeitbedarf
    ('aufgeben',  X0 + 1 * DX, Y, 2),
    ('wiegen',    X0 + 3 * DX, Y, 1),
    ('verladen',  X0 + 5 * DX, Y, 5),
]
ARCS = [
    ('Passagiere', 'aufgeben', 1),
    ('aufgeben', 'Schalterbereich', 1),
    ('Schalterbereich', 'wiegen', 1),
    ('wiegen', 'Gepäcklager', 1),
    ('Gepäcklager', 'verladen', 1),
    ('verladen', 'Flugzeug', 1),
]

# ------------------------------------------- Verbesserung: zweiter Schalter,
#                                              zweiter Verlader, groesserer Puffer

PLACES_V = [
    ('Passagiere',       X0 + 0 * DX, Y, 50, 50),
    ('Schalterbereich',  X0 + 2 * DX, Y,  0, 10),
    ('Gepäcklager',      X0 + 4 * DX, Y,  0, 50),
    ('Flugzeug',         X0 + 6 * DX, Y,  0, 50),
]
TRANS_V = [
    ('aufgeben',    X0 + 1 * DX, Y,  2),
    ('aufgeben 2',  X0 + 1 * DX, Y2, 2),
    ('wiegen',      X0 + 3 * DX, Y,  1),
    ('verladen',    X0 + 5 * DX, Y,  5),
    ('verladen 2',  X0 + 5 * DX, Y2, 5),
]
ARCS_V = [
    ('Passagiere', 'aufgeben', 1),
    ('aufgeben', 'Schalterbereich', 1),
    ('Passagiere', 'aufgeben 2', 1),
    ('aufgeben 2', 'Schalterbereich', 1),
    ('Schalterbereich', 'wiegen', 1),
    ('wiegen', 'Gepäcklager', 1),
    ('Gepäcklager', 'verladen', 1),
    ('verladen', 'Flugzeug', 1),
    ('Gepäcklager', 'verladen 2', 1),
    ('verladen 2', 'Flugzeug', 1),
]

DATEIEN = [
    ('gepaeckaufgabe.hps', 'Buchmodell M1', PLACES, TRANS, ARCS),
    ('gepaeckaufgabe-verbessert.hps', 'zwei Schalter, zwei Verlader', PLACES_V, TRANS_V, ARCS_V),
]


if __name__ == '__main__':
    ziel = sys.argv[1] if len(sys.argv) > 1 else '.'
    for name, titel, pl, tr, ar in DATEIEN:
        daten = hps.write_hps(pl, tr, ar)
        with open(os.path.join(ziel, name), 'wb') as f:
            f.write(daten)
        objs, rest = hps.read_hps(daten)          # sofort gegenlesen
        ende, marken, _ = simuliere(pl, tr, ar)
        print('%-32s %s' % (name, titel))
        print('   %d Bytes, %d Objekte, Abspann %d Bytes' % (len(daten), len(objs), len(rest)))
        print('   Simulation: %d von %d Gepäckstücken im Flugzeug nach %d Zeiteinheiten'
              % (marken[pl[-1][0]], pl[0][3], ende))
