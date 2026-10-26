"""Convert the lettering SVG (Illustrator export) into After Effects shape data for HH_Lyrics_SVG_AE.jsx.

Reads every <path>, <rect> and <polygon> with its transforms, converts all curves to After Effects shape
vertices / in-tangents / out-tangents, and sorts the artwork into blocks (title, credit, 13 lyric lines),
each split into its rows. Blocks are the SVG's top-level groups; shapes outside any group are the title.

Usage:
  svg_to_ae.py report LYRICS.svg            print blocks and rows
  svg_to_ae.py jsx LYRICS.svg SCRIPT.jsx    put the shape data into the After Effects script
  svg_to_ae.py jsx LYRICS.svg SCRIPT.jsx 11,12,14,8s
                                            only these blocks, in this order (0 title, 1 credit, n+1 line n);
                                            a trailing s sets that line on one straight line
"""
import json
import math
import re
import sys
import xml.etree.ElementTree as ET

NUM = r"[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?"


def mat_mul(a, b):
    """3x2 affine matrices as (a, b, c, d, e, f) = [[a c e], [b d f]]."""
    return (a[0] * b[0] + a[2] * b[1], a[1] * b[0] + a[3] * b[1],
            a[0] * b[2] + a[2] * b[3], a[1] * b[2] + a[3] * b[3],
            a[0] * b[4] + a[2] * b[5] + a[4], a[1] * b[4] + a[3] * b[5] + a[5])


IDENTITY = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)


def parse_transform(s):
    m = IDENTITY
    for name, args in re.findall(r"(\w+)\s*\(([^)]*)\)", s or ""):
        v = [float(x) for x in re.findall(NUM, args)]
        if name == "translate":
            t = (1, 0, 0, 1, v[0], v[1] if len(v) > 1 else 0)
        elif name == "scale":
            t = (v[0], 0, 0, v[1] if len(v) > 1 else v[0], 0, 0)
        elif name == "rotate":
            a = math.radians(v[0])
            r = (math.cos(a), math.sin(a), -math.sin(a), math.cos(a), 0, 0)
            if len(v) == 3:
                t = mat_mul(mat_mul((1, 0, 0, 1, v[1], v[2]), r), (1, 0, 0, 1, -v[1], -v[2]))
            else:
                t = r
        elif name == "matrix":
            t = tuple(v)
        elif name == "skewX":
            t = (1, 0, math.tan(math.radians(v[0])), 1, 0, 0)
        elif name == "skewY":
            t = (1, math.tan(math.radians(v[0])), 0, 1, 0, 0)
        else:
            raise ValueError("unsupported transform " + name)
        m = mat_mul(m, t)
    return m


def apply(m, p):
    return (m[0] * p[0] + m[2] * p[1] + m[4], m[1] * p[0] + m[3] * p[1] + m[5])


def apply_vec(m, v):
    return (m[0] * v[0] + m[2] * v[1], m[1] * v[0] + m[3] * v[1])


def path_segments(d):
    """SVG path data -> list of subpaths; each is (start, [segments], closed); a segment is (c1, c2, end)."""
    tokens = re.findall(r"[MmLlHhVvCcSsQqTtAaZz]|" + NUM, d)
    subpaths, segs, start, cur, closed = [], None, None, (0.0, 0.0), False
    prev_c2, prev_q, cmd, i = None, None, None, 0

    def num():
        nonlocal i
        v = float(tokens[i]); i += 1
        return v

    def line(p):
        return (cur, p, p)          # a straight segment as a cubic with control points on its ends

    while i < len(tokens):
        t = tokens[i]
        if re.match(r"[A-Za-z]", t):
            cmd = t; i += 1
            if cmd in "Zz":
                if segs is not None:
                    subpaths.append((start, segs, True))
                cur, segs, prev_c2, prev_q = start, None, None, None
                continue
        rel = cmd.islower()
        c = cmd.upper()
        ox, oy = (cur if rel else (0.0, 0.0))
        if c == "M":
            if segs is not None:
                subpaths.append((start, segs, False))
            cur = (ox + num(), oy + num()); start = cur; segs = []
            cmd = "l" if rel else "L"          # further pairs are implicit lineto
            prev_c2 = prev_q = None
        elif c == "L":
            p = (ox + num(), oy + num()); segs.append(line(p)); cur = p; prev_c2 = prev_q = None
        elif c == "H":
            p = ((cur[0] if rel else 0.0) + num(), cur[1]); segs.append(line(p)); cur = p; prev_c2 = prev_q = None
        elif c == "V":
            p = (cur[0], (cur[1] if rel else 0.0) + num()); segs.append(line(p)); cur = p; prev_c2 = prev_q = None
        elif c == "C":
            c1 = (ox + num(), oy + num()); c2 = (ox + num(), oy + num()); p = (ox + num(), oy + num())
            segs.append((c1, c2, p)); cur = p; prev_c2, prev_q = c2, None
        elif c == "S":
            c1 = (2 * cur[0] - prev_c2[0], 2 * cur[1] - prev_c2[1]) if prev_c2 else cur
            c2 = (ox + num(), oy + num()); p = (ox + num(), oy + num())
            segs.append((c1, c2, p)); cur = p; prev_c2, prev_q = c2, None
        elif c == "Q" or c == "T":
            if c == "Q":
                q = (ox + num(), oy + num())
            else:
                q = (2 * cur[0] - prev_q[0], 2 * cur[1] - prev_q[1]) if prev_q else cur
            p = (ox + num(), oy + num())
            c1 = (cur[0] + 2 / 3 * (q[0] - cur[0]), cur[1] + 2 / 3 * (q[1] - cur[1]))
            c2 = (p[0] + 2 / 3 * (q[0] - p[0]), p[1] + 2 / 3 * (q[1] - p[1]))
            segs.append((c1, c2, p)); cur = p; prev_q, prev_c2 = q, None
        else:
            raise ValueError("unsupported path command " + cmd)
    if segs:
        subpaths.append((start, segs, False))
    return subpaths


def element_subpaths(el, tag):
    if tag == "path":
        return path_segments(el.get("d", ""))
    if tag == "polygon" or tag == "polyline":
        v = [float(x) for x in re.findall(NUM, el.get("points", ""))]
        pts = list(zip(v[0::2], v[1::2]))
        segs = [(pts[k - 1], pts[k], pts[k]) for k in range(1, len(pts))]
        return [(pts[0], segs, tag == "polygon")]
    if tag == "rect":
        x, y = float(el.get("x", 0)), float(el.get("y", 0))
        w, h = float(el.get("width")), float(el.get("height"))
        if el.get("rx") or el.get("ry"):
            raise ValueError("rounded rect not supported")
        pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
        segs = [(pts[k - 1], pts[k], pts[k]) for k in range(1, 4)]
        return [(pts[0], segs, True)]
    raise ValueError("unsupported element " + tag)


def to_ae(subpath, m):
    """One subpath -> After Effects shape: vertices, inTangents, outTangents (tangents relative), closed."""
    start, segs, closed = subpath
    v, i_t, o_t = [apply(m, start)], [(0.0, 0.0)], [(0.0, 0.0)]
    p = start
    for c1, c2, end in segs:
        o_t[-1] = apply_vec(m, (c1[0] - p[0], c1[1] - p[1]))
        v.append(apply(m, end))
        i_t.append(apply_vec(m, (c2[0] - end[0], c2[1] - end[1])))
        o_t.append((0.0, 0.0))
        p = end
    if closed and len(v) > 1 and math.hypot(v[-1][0] - v[0][0], v[-1][1] - v[0][1]) < 1e-6:
        i_t[0] = i_t[-1]
        v.pop(); i_t.pop(); o_t.pop()
    return {"v": v, "i": i_t, "o": o_t, "closed": closed or True}


def bbox_of(shapes):
    """Tight-enough bounds: vertices plus control points (a curve stays inside its control hull)."""
    xs, ys = [], []
    for s in shapes:
        for k, pt in enumerate(s["v"]):
            xs += [pt[0], pt[0] + s["i"][k][0], pt[0] + s["o"][k][0]]
            ys += [pt[1], pt[1] + s["i"][k][1], pt[1] + s["o"][k][1]]
    return [min(xs), min(ys), max(xs), max(ys)]


def load(svg_path):
    tree = ET.parse(svg_path)
    root = tree.getroot()
    ns = lambda tag: tag.split("}")[-1]
    blocks = []                     # each: list of elements (dicts with shapes + bbox)

    def walk(node, m, out):
        for ch in node:
            tag = ns(ch.tag)
            mm = mat_mul(m, parse_transform(ch.get("transform")))
            if tag == "g":
                walk(ch, mm, out)
            elif tag in ("path", "rect", "polygon", "polyline"):
                shapes = [to_ae(sp, mm) for sp in element_subpaths(ch, tag)]
                out.append({"tag": tag, "shapes": shapes, "bbox": bbox_of(shapes)})

    loose = []
    for ch in root:
        tag = ns(ch.tag)
        m = parse_transform(ch.get("transform"))
        if tag == "g":
            els = []
            walk(ch, m, els)
            if els:
                blocks.append(els)
        elif tag in ("path", "rect", "polygon", "polyline"):
            shapes = [to_ae(sp, m) for sp in element_subpaths(ch, tag)]
            loose.append({"tag": tag, "shapes": shapes, "bbox": bbox_of(shapes)})
    if loose:
        blocks.append(loose)
    return blocks


def union_bbox(els):
    b = [e["bbox"] for e in els]
    return [min(x[0] for x in b), min(x[1] for x in b), max(x[2] for x in b), max(x[3] for x in b)]


def flatten(shape, steps=10):
    """Polygon approximation of one closed shape (for measuring ink, not for output)."""
    v, i_t, o_t = shape["v"], shape["i"], shape["o"]
    pts, n = [], len(v)
    for k in range(n):
        p0, p3 = v[k], v[(k + 1) % n]
        c1 = (p0[0] + o_t[k][0], p0[1] + o_t[k][1])
        c2 = (p3[0] + i_t[(k + 1) % n][0], p3[1] + i_t[(k + 1) % n][1])
        for s in range(steps):
            t = s / steps
            a, b, c, d = (1 - t) ** 3, 3 * t * (1 - t) ** 2, 3 * t * t * (1 - t), t ** 3
            pts.append((a * p0[0] + b * c1[0] + c * c2[0] + d * p3[0], a * p0[1] + b * c1[1] + c * c2[1] + d * p3[1]))
    return pts


def ink_profile(els, box, scale):
    """Ink per pixel row of the block, rasterised at `scale` pixels per SVG unit."""
    from PIL import Image, ImageDraw
    w = max(1, int((box[2] - box[0]) * scale) + 2)
    h = max(1, int((box[3] - box[1]) * scale) + 2)
    img = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(img)
    for e in els:
        for sh in e["shapes"]:
            pts = [((x - box[0]) * scale, (y - box[1]) * scale) for x, y in flatten(sh)]
            if len(pts) > 2:
                draw.polygon(pts, fill=255)
    import numpy as np
    return (np.asarray(img) > 0).sum(axis=1)


def row_baselines(els, scale=0.5):
    """Row baselines of a block: the strong horizontal ink bands drawn by each row's letters and مدّ strokes."""
    import numpy as np
    box = union_bbox(els)
    prof = ink_profile(els, box, scale).astype(float)
    smooth = np.convolve(prof, np.ones(9) / 9, mode="same")
    peaks = []
    for y in np.argsort(-smooth):
        if smooth[y] < 0.30 * smooth.max():
            break
        if all(abs(y - p) >= 55 * scale for p in peaks):
            peaks.append(int(y))
    return [box[1] + p / scale for p in sorted(peaks)]


def units(e):
    """Split one SVG element into units: each outer contour with the contours inside it (its holes and marks).
    Units of one element stay one After Effects group when they land in the same row."""
    shapes = sorted(e["shapes"], key=lambda s: -(bbox_of([s])[2] - bbox_of([s])[0]) * (bbox_of([s])[3] - bbox_of([s])[1]))
    out = []
    for s in shapes:
        b = bbox_of([s])
        host = None
        for u in out:
            ob = u["bbox"]
            if ob[0] <= b[0] and ob[1] <= b[1] and ob[2] >= b[2] and ob[3] >= b[3]:
                host = u
                break
        if host:
            host["shapes"].append(s)
        else:
            out.append({"shapes": [s], "bbox": b})
    return out


def split_rows(els):
    """Each unit goes to the row band holding most of its ink; small marks go to the nearest letter shape."""
    import numpy as np
    bases = row_baselines(els)
    box = union_bbox(els)
    pitch = float(np.median(np.diff(bases))) if len(bases) > 1 else box[3] - box[1]
    bands = [(b - 0.65 * pitch, b + 0.35 * pitch) for b in bases]
    pieces = []                                   # (element index, unit)
    for n, e in enumerate(els):
        for u in units(e):
            pieces.append((n, u))
    size = lambda u: max(u["bbox"][2] - u["bbox"][0], u["bbox"][3] - u["bbox"][1])
    small = 0.22 * pitch
    row_of = {}
    for k, (n, u) in enumerate(pieces):
        if size(u) < small:
            continue
        scale = 0.5
        prof = ink_profile([u], u["bbox"], scale)
        ys = u["bbox"][1] + np.arange(len(prof)) / scale
        ink = [prof[(ys >= lo) & (ys < hi)].sum() for lo, hi in bands]
        row_of[k] = int(np.argmax(ink))

    def dist(u, f):
        cx, cy = (u["bbox"][0] + u["bbox"][2]) / 2, (u["bbox"][1] + u["bbox"][3]) / 2
        dx = max(f["bbox"][0] - cx, 0, cx - f["bbox"][2])
        dy = max(f["bbox"][1] - cy, 0, cy - f["bbox"][3])
        return math.hypot(dx, dy)

    for k, (n, u) in enumerate(pieces):
        if k not in row_of:
            j = min(row_of, key=lambda j: dist(u, pieces[j][1]))
            row_of[k] = row_of[j]
    rows = [{} for _ in bases]                    # row -> element index -> shapes
    for k, (n, u) in enumerate(pieces):
        rows[row_of[k]].setdefault(n, []).extend(u["shapes"])
    return [[{"shapes": shapes, "bbox": bbox_of(shapes)} for shapes in r.values()] for r in rows], bases


def build(svg_path):
    blocks = load(svg_path)
    blocks.sort(key=lambda els: union_bbox(els)[1])           # top to bottom
    out = []
    for n, els in enumerate(blocks):
        rows, bases = split_rows(els)
        out.append({"bbox": union_bbox(els),
                    "rows": [{"bbox": union_bbox(r), "base": bases[k], "elements": [e["shapes"] for e in r]}
                             for k, r in enumerate(rows)]})
    return out


def moved(shapes, dx, dy):
    return [{"v": [(x + dx, y + dy) for x, y in s["v"]], "i": s["i"], "o": s["o"], "closed": s["closed"]} for s in shapes]


def straight(block, gap=0.3):
    """The rows of a block laid out as one straight line: all on the first row's baseline, chained right to
    left in reading order, gap x the median row height between them. Rows stay separate (written in turn)."""
    heights = sorted(r["bbox"][3] - r["bbox"][1] for r in block["rows"])
    space = gap * heights[len(heights) // 2]
    base = block["rows"][0]["base"]
    right = block["rows"][0]["bbox"][2]
    rows = []
    for r in block["rows"]:
        dx, dy = right - r["bbox"][2], base - r["base"]
        els = [moved(shapes, dx, dy) for shapes in r["elements"]]
        bb = r["bbox"]
        rows.append({"bbox": [bb[0] + dx, bb[1] + dy, bb[2] + dx, bb[3] + dy], "base": base, "elements": els})
        right = bb[0] + dx - space
    allb = [r["bbox"] for r in rows]
    return {"bbox": [min(b[0] for b in allb), min(b[1] for b in allb), max(b[2] for b in allb), max(b[3] for b in allb)],
            "rows": rows, "chain": True}


def compact(data, digits=1):
    """Shape data for the JSX: per block its size and rows; coordinates relative to the block centre, in SVG
    units, flattened [x0, y0, x1, y1, ...] per vertex list."""
    out = []
    for b in data:
        bx = b["bbox"]
        cx, cy = (bx[0] + bx[2]) / 2, (bx[1] + bx[3]) / 2
        rows = []
        for r in b["rows"]:
            rb = r["bbox"]
            els = []
            for shapes in r["elements"]:
                el = []
                for sh in shapes:
                    el.append([[round(c, digits) for p in sh["v"] for c in (p[0] - cx, p[1] - cy)],
                               [round(c, digits) for p in sh["i"] for c in p],
                               [round(c, digits) for p in sh["o"] for c in p]])
                els.append(el)
            rows.append({"box": [round(rb[0] - cx, digits), round(rb[1] - cy, digits),
                                 round(rb[2] - cx, digits), round(rb[3] - cy, digits)], "els": els})
        entry = {"w": round(bx[2] - bx[0], digits), "h": round(bx[3] - bx[1], digits), "rows": rows}
        if b.get("chain"):
            entry["chain"] = True
        out.append(entry)
    return out


def select(full, spec):
    """Blocks picked by a spec like "11,12,14,8s": block indices top to bottom (0 title, 1 credit, n+1 lyric
    line n); a trailing s lays that block out as one straight line."""
    out = []
    for item in spec.split(","):
        item = item.strip()
        flat = item.endswith("s")
        b = full[int(item.rstrip("s"))]
        out.append(straight(b) if flat else b)
    return out


def write_jsx(svg_path, jsx_path, spec=None):
    """Put the shape data between the DATA markers of the After Effects script. DATA_REF is the width of the
    widest lyric line in the whole artwork, so every script draws the lettering at the same size."""
    full = build(svg_path)
    ref = max(b["bbox"][2] - b["bbox"][0] for b in full[2:])
    data = json.dumps(compact(select(full, spec) if spec else full), separators=(",", ":"))
    src = open(jsx_path, encoding="utf-8-sig").read()
    a, b = src.index("// <DATA>"), src.index("// </DATA>")
    src = (src[:a] + "// <DATA>\n    var DATA_REF = " + str(round(ref, 1)) + ";\n    var DATA = " + data + ";\n    "
           + src[b:])
    open(jsx_path, "w", encoding="utf-8-sig").write(src)
    return len(data)


if __name__ == "__main__":
    if sys.argv[1] == "report":
        data = build(sys.argv[2])
        for n, b in enumerate(data):
            bx = b["bbox"]
            print(f"block {n:2d}: {len(b['rows'])} rows  bbox w {bx[2]-bx[0]:7.1f} h {bx[3]-bx[1]:6.1f} at y {bx[1]:8.1f}  "
                  + "  ".join(f"[{len(r['elements'])} el, w {r['bbox'][2]-r['bbox'][0]:.0f} h {r['bbox'][3]-r['bbox'][1]:.0f}]" for r in b["rows"]))
    elif sys.argv[1] == "jsx":
        spec = sys.argv[4] if len(sys.argv) > 4 else None
        print("wrote", write_jsx(sys.argv[2], sys.argv[3], spec), "characters of shape data into", sys.argv[3])
