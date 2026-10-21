"""Leser und Schreiber fuer das binaere .hps-Format (HPSim / HOldPetriSim, MFC CArchive).

Format rekonstruiert aus echten .hps-Dateien und aus dem offenen Quellcode von
github.com/jeremybacher/hpsim (src/lib/hpsParser.ts, src/lib/hpsWriter.ts).
"""
import struct

DRAW_VERSION = 0x2712
UNLIMITED = 1874919423  # Wert, den HPSim selbst fuer "unbegrenzt" schreibt


# ---------------------------------------------------------------- Leser

class Reader:
    def __init__(self, data):
        self.d = data
        self.o = 0

    def byte(self):
        v = self.d[self.o]
        self.o += 1
        return v

    def word(self):
        v = struct.unpack_from('<H', self.d, self.o)[0]
        self.o += 2
        return v

    def dword(self):
        v = struct.unpack_from('<I', self.d, self.o)[0]
        self.o += 4
        return v

    def int32(self):
        v = struct.unpack_from('<i', self.d, self.o)[0]
        self.o += 4
        return v

    def double(self):
        v = struct.unpack_from('<d', self.d, self.o)[0]
        self.o += 8
        return v

    def skip(self, n):
        self.o += n

    def cstring(self):
        n = self.byte()
        if n < 0xFF:
            s = self.d[self.o:self.o + n].decode('latin-1')
            self.o += n
            return s
        n = self.word()
        if n == 0xFFFE:          # Unicode-Markierung
            n = self.byte()
            if n == 0xFF:
                n = self.word()
                if n == 0xFFFF:
                    n = self.dword()
            s = self.d[self.o:self.o + 2 * n].decode('utf-16-le')
            self.o += 2 * n
            return s
        if n == 0xFFFF:
            n = self.dword()
        s = self.d[self.o:self.o + n].decode('latin-1')
        self.o += n
        return s

    def points(self):
        n = self.word()
        if n == 0xFFFF:
            n = self.dword()
        return [(self.int32(), self.int32()) for _ in range(n)]

    def rect(self):
        return (self.int32(), self.int32(), self.int32(), self.int32())


def read_hps(data):
    r = Reader(data)
    count = r.word()
    if count == 0xFFFF:
        count = r.dword()

    classes = {}        # Tag-Index -> Klassenname
    next_tag = 1
    objects = []

    for _ in range(count):
        tag = r.word()
        if tag == 0xFFFF:                      # neue Klasse
            r.word()                           # Schema-Version
            n = r.word()
            name = r.d[r.o:r.o + n].decode('latin-1')
            r.o += n
            classes[next_tag] = name
            next_tag += 2                      # Klassen-Tag + Objekt-Tag
        elif tag & 0x8000:                     # Rueckverweis
            name = classes[tag & 0x7FFF]
            next_tag += 1
        else:
            raise ValueError('unbekanntes Tag 0x%04x bei Offset %d' % (tag, r.o))

        if name == 'CHPosition':
            tokens, tmax, tstart = r.dword(), r.dword(), r.dword()
            r.dword()
            rect = r.rect()
            r.dword()
            ident = r.dword()
            r.dword()
            r.skip(7)
            r.double()
            objects.append(dict(cls=name, tokens=tokens, max=tmax, start=tstart,
                                rect=rect, ident=ident))
        elif name == 'CHTransition':
            r.dword()
            rect = r.rect()
            ident = r.dword()
            r.dword()
            delay = r.dword()
            r.dword()
            rng = r.dword()
            r.dword(); r.dword()
            r.byte(); r.byte()
            mode = r.byte()
            r.skip(6)
            r.double()
            objects.append(dict(cls=name, rect=rect, ident=ident, delay=delay,
                                mode=mode, range=rng))
        elif name == 'CHConnector':
            rect = r.rect()
            r.int32(); r.int32(); r.int32(); r.int32()
            ident, frm, to, weight = r.dword(), r.dword(), r.dword(), r.dword()
            r.dword()
            r.word()
            typ = r.word()
            r.word(); r.word(); r.word()
            r.skip(5)
            r.double()
            pts = r.points()
            objects.append(dict(cls=name, rect=rect, ident=ident, frm=frm, to=to,
                                weight=weight, typ=typ, points=pts))
        elif name == 'CHLabel':
            text = r.cstring()
            top, left, bottom, right = r.int32(), r.int32(), r.int32(), r.int32()
            owner, sub = r.dword(), r.dword()
            vis, border, empty = r.byte(), r.byte(), r.byte()
            objects.append(dict(cls=name, text=text, rect=(top, left, bottom, right),
                                owner=owner, sub=sub, vis=vis, border=border, empty=empty))
        else:
            raise ValueError('unbekannte Klasse %r' % name)

    rest = r.d[r.o:]
    return objects, rest


# ------------------------------------------------------------- Schreiber

class Writer:
    def __init__(self):
        self.b = bytearray()
        self.classes = {}
        self.next_tag = 1

    def byte(self, v):
        self.b += struct.pack('<B', v & 0xFF)

    def word(self, v):
        self.b += struct.pack('<H', v & 0xFFFF)

    def dword(self, v):
        self.b += struct.pack('<I', v & 0xFFFFFFFF)

    def int32(self, v):
        self.b += struct.pack('<i', int(round(v)))

    def double(self, v):
        self.b += struct.pack('<d', v)

    def zeros(self, n):
        self.b += b'\0' * n

    def cstring(self, s):
        raw = s.encode('latin-1', 'replace')
        if len(raw) < 0xFF:
            self.byte(len(raw))
        else:
            self.byte(0xFF)
            self.word(len(raw))
        self.b += raw

    def rect(self, left, top, right, bottom):
        self.int32(left); self.int32(top); self.int32(right); self.int32(bottom)

    def cls(self, name):
        if name in self.classes:
            self.word(0x8000 | self.classes[name])
            self.next_tag += 1
        else:
            self.word(0xFFFF)
            self.word(DRAW_VERSION)
            raw = name.encode('latin-1')
            self.word(len(raw))
            self.b += raw
            self.classes[name] = self.next_tag
            self.next_tag += 2


R_PLACE = 12       # Halbmesser des Kreises, wie in echten Dateien (24 px Durchmesser)
TR_W, TR_H = 24, 12


def write_hps(places, transitions, arcs, grid=10, sim_speed=500, sample=1):
    """places:      [(name, x, y, tokens, capacity)]
       transitions: [(name, x, y, delay)]
       arcs:        [(von, nach, gewicht)]  - Namen aus places/transitions
    """
    w = Writer()

    p_ident = {}
    t_ident = {}
    for i, p in enumerate(places):
        p_ident[p[0]] = 1000000 + i
    for i, t in enumerate(transitions):
        # ab 1 nummeriert: echte HPSim-Dateien beginnen bei 0, aber manche Leser
        # deuten die Besitzer-Nummer 0 als "kein Besitzer" und verlieren dann die
        # Beschriftung. 1 ist fuer beide Seiten gueltig.
        t_ident[t[0]] = i + 1
    pos = {p[0]: (p[1], p[2]) for p in places}
    pos.update({t[0]: (t[1], t[2]) for t in transitions})

    total = len(places) * 3 + len(transitions) * 3 + len(arcs) * 2
    w.word(total)

    for name, x, y, tokens, cap in places:
        ident = p_ident[name]
        left, top, right, bottom = x - R_PLACE, y - R_PLACE, x + R_PLACE, y + R_PLACE
        w.cls('CHPosition')
        w.dword(tokens)
        w.dword(cap if cap else UNLIMITED)
        w.dword(tokens)
        w.dword(0)
        w.rect(left, top, right, bottom)
        w.dword(25)
        w.dword(ident)
        w.dword(0)
        w.zeros(7)
        w.double(0.0)

        # Beschriftung A: Name, ueber dem Kreis
        w.cls('CHLabel')
        w.cstring(name)
        w.int32(top - 20); w.int32(left - 32); w.int32(top - 4); w.int32(right + 32)
        w.dword(ident); w.dword(0)
        w.byte(1); w.byte(0); w.byte(1)

        # Beschriftung B: Kapazitaet, unter dem Kreis
        w.cls('CHLabel')
        w.cstring(str(cap if cap else UNLIMITED))
        w.int32(bottom + 4); w.int32(left - 32); w.int32(bottom + 20); w.int32(right + 32)
        w.dword(ident); w.dword(1)
        w.byte(0); w.byte(0); w.byte(1)

    for name, x, y, delay in transitions:
        ident = t_ident[name]
        left, top, right, bottom = x - TR_W // 2, y - TR_H // 2, x + TR_W // 2, y + TR_H // 2
        w.cls('CHTransition')
        w.dword(25)
        w.rect(left, top, right, bottom)
        w.dword(ident)
        w.dword(delay)
        w.dword(delay)
        w.dword(0)
        w.dword(0)
        w.dword(0); w.dword(0)
        w.byte(0); w.byte(0)
        w.byte(1 if delay > 0 else 0)
        w.zeros(6)
        w.double(0.0)

        w.cls('CHLabel')
        w.cstring(name)
        w.int32(top - 20); w.int32(left - 32); w.int32(top - 4); w.int32(right + 32)
        w.dword(ident); w.dword(0)
        w.byte(1); w.byte(0); w.byte(1)

        w.cls('CHLabel')
        w.cstring(str(delay))
        w.int32(bottom + 4); w.int32(left - 32); w.int32(bottom + 20); w.int32(right + 32)
        w.dword(ident); w.dword(1)
        w.byte(0); w.byte(0); w.byte(1)

    for i, (frm, to, weight) in enumerate(arcs):
        ident = 2000000 + i
        fx, fy = pos[frm]
        tx, ty = pos[to]
        w.cls('CHConnector')
        w.rect(min(fx, tx), min(fy, ty), max(fx, tx), max(fy, ty))
        w.int32(tx - 5); w.int32(ty - 5); w.int32(tx + 5); w.int32(ty + 5)
        w.dword(ident)
        w.dword(p_ident.get(frm, t_ident.get(frm, 0)))
        w.dword(p_ident.get(to, t_ident.get(to, 0)))
        w.dword(weight)
        w.dword(0)
        w.word(0)
        w.word(0)          # 0 = normale Kante
        w.word(0); w.word(0); w.word(0)
        w.zeros(5)
        w.double(0.0)
        w.word(2)
        w.int32(fx); w.int32(fy)
        w.int32(tx); w.int32(ty)

        mx, my = (fx + tx) // 2, (fy + ty) // 2
        w.cls('CHLabel')
        w.cstring(str(weight))
        w.int32(my - 18); w.int32(mx - 16); w.int32(my - 2); w.int32(mx + 16)
        w.dword(ident); w.dword(0)
        w.byte(0); w.byte(0); w.byte(1)

    w.dword(1000)                      # Zeichenflaeche Breite
    w.dword(1500)                      # Zeichenflaeche Hoehe
    w.dword(2000000 + len(arcs))       # naechste freie Kanten-Nummer
    w.dword(1000000 + len(places))     # naechste freie Platz-Nummer
    w.dword(len(transitions) + 1)      # naechste freie Transitions-Nummer
    w.dword(grid)                      # Raster
    w.dword(0)                         # Schrittzaehler
    w.dword(1000)                      # Stoppzeit
    w.dword(1000)                      # Stoppschritt
    w.dword(sim_speed)                 # Geschwindigkeit
    w.dword(0)                         # Simulationszeit
    w.dword(sample)                    # Abtastzeit
    w.dword(0x00FFFFFF)                # Hintergrund weiss
    for _ in range(7):
        w.dword(0)
    for v in (1, 1, 1, 0, 1, 1, 0, 0, 0, 0):
        w.byte(v)
    return bytes(w.b)
