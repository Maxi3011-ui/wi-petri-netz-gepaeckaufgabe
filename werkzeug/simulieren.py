"""Zeitbewertete Simulation eines Petri-Netzes, wie HPSim sie ausfuehrt.

Regeln (Einzelbediener je Transition, wie in HPSim):
- Eine Transition schaltet, wenn jede Eingangsstelle genug Marken hat UND
  jede Ausgangsstelle noch Platz hat (Kapazitaet).
- Beim Schalten werden die Eingangsmarken sofort entnommen; die Ausgangsmarken
  erscheinen nach der hinterlegten Zeit.
- Eine Transition, die gerade arbeitet, kann nicht erneut schalten.
"""


def simuliere(places, transitions, arcs, bis=10000):
    marken = {p[0]: p[3] for p in places}
    kapaz = {p[0]: (p[4] if p[4] else 10 ** 9) for p in places}
    zeit_je = {t[0]: t[3] for t in transitions}

    ein = {t[0]: [] for t in transitions}      # (Platz, Gewicht)
    aus = {t[0]: [] for t in transitions}
    for frm, to, g in arcs:
        if frm in zeit_je:
            aus[frm].append((to, g))
        else:
            ein[to].append((frm, g))

    laeuft = {}            # Transition -> Endzeit
    t = 0
    durchsatz = []         # (Zeit, Marken im letzten Platz)
    letzter = places[-1][0]

    while t <= bis:
        # 1. fertige Arbeitsgaenge abliefern
        for name in [n for n, ende in laeuft.items() if ende <= t]:
            for pl, g in aus[name]:
                marken[pl] += g
            del laeuft[name]

        # 2. schaltbereite Transitionen starten
        gestartet = True
        while gestartet:
            gestartet = False
            for name, _, _, dauer in transitions:
                if name in laeuft:
                    continue
                if all(marken[p] >= g for p, g in ein[name]) and \
                   all(marken[p] + g <= kapaz[p] for p, g in aus[name]):
                    for p, g in ein[name]:
                        marken[p] -= g
                    laeuft[name] = t + max(dauer, 1)
                    gestartet = True

        durchsatz.append((t, marken[letzter]))

        if not laeuft:
            break
        t = min(laeuft.values())

    return t, marken, durchsatz


def bericht(titel, places, transitions, arcs):
    ende, marken, verlauf = simuliere(places, transitions, arcs)
    gesamt = places[0][3]
    print('%s' % titel)
    print('  Ende nach %d Zeiteinheiten, %d von %d Gepaeckstuecken im Flugzeug'
          % (ende, marken[places[-1][0]], gesamt))
    for grenze in (10, 25, 50):
        treffer = [z for z, n in verlauf if n >= grenze]
        if treffer:
            print('     %2d Stueck verladen nach %d Zeiteinheiten' % (grenze, treffer[0]))
    print('  Restbestaende:', {k: v for k, v in marken.items() if v})
    return ende
