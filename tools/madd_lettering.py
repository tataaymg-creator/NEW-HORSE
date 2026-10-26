"""Arabic lettering with long curved مدّ strokes, built as vector outlines for After Effects.

Each line is shaped with HarfBuzz (so joins, ligatures and marks are exactly what the font draws), with a
single tatweel at every place marked ـ in the text. Each tatweel is then replaced by a custom stroke of any
length that dips gently below the baseline and rises back into the next letter, like the references.

Outputs, per line, in em units (1 em = font size), centred on 0,0, y down (After Effects coordinates):
  elements in reading order (right to left): letter runs ("s") with their outline contours as
  vertices / in-tangents / out-tangents, and مدّ strokes ("m") as a centre-line path plus stroke width.

Usage:
  madd_lettering.py preview FONT OUT.svg "line one" "line two" ...
  madd_lettering.py jsx FONT TEMPLATE.jsx OUT.jsx
"""
import json
import sys

import uharfbuzz as hb
from fontTools.pens.basePen import BasePen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.ttLib import TTFont

TATWEEL = "ـ"

# مدّ shape, in em
STRETCH = 5.0          # length of each stretch
STRETCH_MIN = 1.6      # shortest a stretch may become when a long line is fitted
DEPTH = 0.032          # how far the stroke dips below the baseline, as a share of its length
DEPTH_MAX = 0.16       # cap on the dip, em
LOW_POINT = 0.55       # where the lowest point sits, from the right end (0.5 = middle)
OVERLAP = 0.012        # how far the stroke runs into the letters at each end, em


class OutlinePen(BasePen):
    """Collects glyph contours as After Effects shapes: vertices, in-tangents, out-tangents (font units)."""

    def __init__(self, glyph_set, dx, dy):
        super().__init__(glyph_set)
        self.dx, self.dy = dx, dy
        self.contours = []
        self.cur = None

    def _p(self, pt):
        return (pt[0] + self.dx, pt[1] + self.dy)

    def _moveTo(self, pt):
        self.cur = {"v": [self._p(pt)], "i": [(0.0, 0.0)], "o": [(0.0, 0.0)]}

    def _lineTo(self, pt):
        self.cur["v"].append(self._p(pt))
        self.cur["i"].append((0.0, 0.0))
        self.cur["o"].append((0.0, 0.0))

    def _curveToOne(self, c1, c2, pt):
        p0 = self.cur["v"][-1]
        c1, c2, p3 = self._p(c1), self._p(c2), self._p(pt)
        self.cur["o"][-1] = (c1[0] - p0[0], c1[1] - p0[1])
        self.cur["v"].append(p3)
        self.cur["i"].append((c2[0] - p3[0], c2[1] - p3[1]))
        self.cur["o"].append((0.0, 0.0))

    def _closePath(self):
        c = self.cur
        v = c["v"]
        if len(v) > 1 and abs(v[-1][0] - v[0][0]) < 1e-6 and abs(v[-1][1] - v[0][1]) < 1e-6:
            c["i"][0] = c["i"][-1]
            v.pop(); c["i"].pop(); c["o"].pop()
        self.contours.append(c)
        self.cur = None

    _endPath = _closePath


class Lettering:
    def __init__(self, font_path):
        self.tt = TTFont(font_path)
        self.upm = self.tt["head"].unitsPerEm
        self.glyph_set = self.tt.getGlyphSet()
        self.order = self.tt.getGlyphOrder()
        self.hb_font = hb.Font(hb.Face(hb.Blob.from_file_path(font_path)))
        tat = self.tt.getBestCmap()[ord(TATWEEL)]
        self.tatweel_gid = self.order.index(tat)
        bp = BoundsPen(self.glyph_set)
        self.glyph_set[tat].draw(bp)
        _, ymin, _, ymax = bp.bounds
        self.stroke_y = (ymin + ymax) / 2.0      # height of the joining stroke, font units
        self.stroke_w = ymax - ymin              # its thickness

    def shape(self, marked):
        """Shape a line with one tatweel per ـ mark. Returns glyphs in visual order and the segment map."""
        text = marked
        while TATWEEL * 2 in text:
            text = text.replace(TATWEEL * 2, TATWEEL)
        buf = hb.Buffer()
        buf.add_codepoints([ord(ch) for ch in text])
        buf.direction = "rtl"
        buf.script = "Arab"
        buf.language = "ar"
        hb.shape(self.hb_font, buf, {})
        # logical segmentation: letter runs split at spaces and at مدّ marks
        seg_of_char, runs, madds = [], 0, 0
        current = None
        for ch in text:
            if ch == TATWEEL:
                madds += 1
                seg_of_char.append(("m", madds - 1))
                current = None
            elif ch.isspace():
                seg_of_char.append(("space", None))
                current = None
            else:
                if current is None:
                    current = runs
                    runs += 1
                seg_of_char.append(("s", current))
        return text, buf.glyph_infos, buf.glyph_positions, seg_of_char, runs, madds

    def layout(self, marked, stretch_units):
        """Outlines and مدّ strokes for one line, with every stretch stretch_units long (font units)."""
        text, infos, poss, seg_of_char, runs, madds = self.shape(marked)
        x = 0.0
        run_contours = [[] for _ in range(runs)]
        run_x = [[None, None] for _ in range(runs)]
        madd_x = [None] * madds
        for info, pos in zip(infos, poss):
            kind, idx = seg_of_char[info.cluster]
            if info.codepoint == self.tatweel_gid and kind == "m":
                madd_x[idx] = (x, x + stretch_units)
                x += stretch_units
                continue
            if kind == "s":
                name = self.order[info.codepoint]
                pen = OutlinePen(self.glyph_set, x + pos.x_offset, pos.y_offset)
                self.glyph_set[name].draw(pen)
                run_contours[idx].extend(pen.contours)
                lo, hi = x + pos.x_offset, x + pos.x_offset + max(pos.x_advance, 1)
                run_x[idx][0] = lo if run_x[idx][0] is None else min(run_x[idx][0], lo)
                run_x[idx][1] = hi if run_x[idx][1] is None else max(run_x[idx][1], hi)
            x += pos.x_advance
        width = x
        return {"width": width, "runs": run_contours, "run_x": run_x, "madds": madd_x, "n_madds": madds}

    def line(self, marked, max_width_em):
        """Fit the stretches to the line width, then convert to em, centred, y down, reading order."""
        upm = self.upm
        bare = self.layout(marked, 0.0)
        k = bare["n_madds"]
        stretch = STRETCH * upm
        scale = 1.0
        if k:
            fits = (max_width_em * upm - bare["width"]) / k
            stretch = max(min(stretch, fits), STRETCH_MIN * upm)
        geo = self.layout(marked, stretch if k else 0.0)
        if geo["width"] > max_width_em * upm:
            scale = max_width_em * upm / geo["width"]
        cx = geo["width"] / 2.0
        cy = (self.stroke_y + 0.30 * upm)     # centre the line a little above the joining stroke

        def P(px, py):
            return [round((px - cx) / upm, 4), round(-(py - cy) / upm, 4)]

        def T(tx, ty):
            return [round(tx / upm, 4), round(-ty / upm, 4)]

        elements = []
        for r, contours in enumerate(geo["runs"]):
            if not contours:
                continue
            x0, x1 = geo["run_x"][r]
            elements.append({
                "t": "s",
                "x": [round((x0 - cx) / upm, 4), round((x1 - cx) / upm, 4)],
                "c": [[[P(*v) for v in c["v"]], [T(*t) for t in c["i"]], [T(*t) for t in c["o"]]]
                      for c in contours],
            })
        for m, span in enumerate(geo["madds"]):
            xl, xr = span
            elements.append({
                "t": "m",
                "x": [round((xl - cx) / upm, 4), round((xr - cx) / upm, 4)],
                "y": P(0, self.stroke_y)[1],
                "w": round(self.stroke_w / upm, 4),
            })
        elements.sort(key=lambda e: -(e["x"][0] + e["x"][1]) / 2.0)   # reading order: right to left
        ys = [pt[1] for e in elements if e["t"] == "s" for c in e["c"] for pt in c[0]]
        return {"scale": round(scale, 4), "width": round(geo["width"] / upm, 4),
                "top": round(min(ys), 4), "bottom": round(max(ys), 4),
                "stretch": round(stretch / upm, 3) if k else 0, "elements": elements}


def madd_path(e, depth=DEPTH, depth_max=DEPTH_MAX, low=LOW_POINT, overlap=OVERLAP):
    """Centre line of a مدّ stroke, right end to left end (the writing direction), y down, em units.
    Two cubics with level tangents at both ends and at the lowest point. Mirrored in the JSX."""
    xl, xr = e["x"]
    y = e["y"]
    length = xr - xl
    d = min(depth * length, depth_max)
    xm = xr - low * length
    a1, a2 = 0.55 * (xr + overlap - xm), 0.55 * (xm - (xl - overlap))
    vertices = [[xr + overlap, y], [xm, y + d], [xl - overlap, y]]
    in_t = [[0, 0], [a1, 0], [a2, 0]]
    out_t = [[-a1, 0], [-a2, 0], [0, 0]]
    return vertices, in_t, out_t


def svg_path(contour, size, ox, oy):
    v, i, o = contour
    d = "M%.2f %.2f" % (ox + v[0][0] * size, oy + v[0][1] * size)
    n = len(v)
    for k in range(n):
        a, b = v[k], v[(k + 1) % n]
        c1 = (a[0] + o[k][0], a[1] + o[k][1])
        c2 = (b[0] + i[(k + 1) % n][0], b[1] + i[(k + 1) % n][1])
        d += " C%.2f %.2f %.2f %.2f %.2f %.2f" % (ox + c1[0] * size, oy + c1[1] * size, ox + c2[0] * size,
                                                  oy + c2[1] * size, ox + b[0] * size, oy + b[1] * size)
    return d + " Z"


def preview(font, out_svg, lines, size=48, width=1280, row=110):
    L = Lettering(font)
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" style="background:#000">'
             % (width, row * len(lines))]
    for n, text in enumerate(lines):
        g = L.line(text, (width * 0.86) / size)
        s = size * g["scale"]
        ox, oy = width / 2.0, row * n + row / 2.0
        for e in g["elements"]:
            if e["t"] == "s":
                d = " ".join(svg_path(c, s, ox, oy) for c in e["c"])
                parts.append('<path d="%s" fill="#fff" fill-rule="nonzero"/>' % d)
            else:
                v, i, o = madd_path(e)
                d = "M%.2f %.2f" % (ox + v[0][0] * s, oy + v[0][1] * s)
                for k in range(len(v) - 1):
                    d += " C%.2f %.2f %.2f %.2f %.2f %.2f" % (
                        ox + (v[k][0] + o[k][0]) * s, oy + (v[k][1] + o[k][1]) * s,
                        ox + (v[k + 1][0] + i[k + 1][0]) * s, oy + (v[k + 1][1] + i[k + 1][1]) * s,
                        ox + v[k + 1][0] * s, oy + v[k + 1][1] * s)
                parts.append('<path d="%s" fill="none" stroke="#fff" stroke-width="%.2f"/>' % (d, e["w"] * s))
    parts.append("</svg>")
    open(out_svg, "w", encoding="utf-8").write("\n".join(parts))


if __name__ == "__main__":
    if sys.argv[1] == "preview":
        preview(sys.argv[2], sys.argv[3], sys.argv[4:])
