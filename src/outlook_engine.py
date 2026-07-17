"""WP-X-05 re-executable implementation of outlook-monitoring-framework.md (outlook scoring + watchlist + migration matrix).

Single source of truth: Section 2.2 trigger factor matrix, Section 5.1 migration matrix, Section 5.3
industry adjustment parsed from the engine document at runtime; Section 2.3 scoring logic (layer weight
values v0.8.4 approved and written into the document), confidence tiers, Section 3.2 watchlist management
rules encoded as code logic (following sri_calculator / contagion_engine precedent).

Disambiguation notes (coding decisions where the document overlaps or is not explicit):
- Confidence "medium" and "low" description overlap -> coherent semantics: High = >=4 same-direction and >=3 layers,
  Medium-High = >=3 same-direction and >=2 layers, Medium = >=2 same-direction and >=2 layers, Low = remaining
  with signal, Very Low = 0 signals (counted by dominant direction).
- Both sides trigger watchlist -> negative takes priority (Section 3.2 not specified, conservative default).
- Developing outlook: "intensity close" interpreted as |net direction| < threshold (2.0).
"""

import re
from pathlib import Path

from src.path_sheet import engine_dir

LAYER_WEIGHTS = {"L1": 1.5, "L2": 1.2, "L3": 1.0, "L4": 0.8, "External Support": 1.2}  # Section 2.3
OUTLOOK_THRESHOLD = 2.0          # Section 2.3: net direction +/-2.0 and same-direction signals >=2
MIN_DIRECTION_SIGNALS = 2
DEVELOPING_MIN_SIGNALS = 3       # Developing: positive/negative each >=3 and |net| < threshold

_LAYER_ROW_RE = re.compile(r"^\|\s*\*\*(L[1-4]|External Support)[^|]*\*\*\s*\|\s*([^|]+?)\s*\|", re.MULTILINE)


def load_factor_matrix(matrix_md_path=None) -> dict:
    """Parse Section 2.2 -> {signal_text: (layer, direction)}, direction in {"positive","negative"}."""
    path = Path(matrix_md_path) if matrix_md_path else engine_dir() / "outlook-monitoring-framework.md"
    text = path.read_text(encoding="utf-8")
    out = {}
    for sec_name, direction in (("Positive Outlook Trigger Signals", "positive"), ("Negative Outlook Trigger Signals", "negative")):
        sec = re.search(r"#### " + sec_name + r"\n(.*?)(?=\n#### |\n### |\Z)", text, re.DOTALL)
        if not sec:
            raise ValueError(f"Section 2.2 missing subsection: {sec_name}")
        for row in _LAYER_ROW_RE.finditer(sec.group(1)):
            out[row.group(2).strip()] = (row.group(1), direction)
    return out


def outlook_assessment(signals: list) -> dict:
    """Section 2.3: net direction scoring -> outlook determination + confidence
    (judgment order: developing -> positive -> negative -> stable)."""
    pos = neg = 0.0
    pos_items, neg_items = [], []
    for s in signals:
        layer, direction = s["layer"], s["direction"]
        if layer not in LAYER_WEIGHTS:
            raise ValueError(f"Unknown layer: {layer!r} (available {sorted(LAYER_WEIGHTS)})")
        if direction == "positive":
            pos += LAYER_WEIGHTS[layer]
            pos_items.append(s)
        elif direction == "negative":
            neg += LAYER_WEIGHTS[layer]
            neg_items.append(s)
        else:
            raise ValueError(f"Unknown direction: {direction!r}")
    net = pos - neg
    if (len(pos_items) >= DEVELOPING_MIN_SIGNALS
            and len(neg_items) >= DEVELOPING_MIN_SIGNALS
            and abs(net) < OUTLOOK_THRESHOLD):
        outlook = "developing"
    elif net >= OUTLOOK_THRESHOLD and len(pos_items) >= MIN_DIRECTION_SIGNALS:
        outlook = "positive"
    elif net <= -OUTLOOK_THRESHOLD and len(neg_items) >= MIN_DIRECTION_SIGNALS:
        outlook = "negative"
    else:
        outlook = "stable"
    dominant = pos_items if pos >= neg else neg_items
    return {
        "outlook": outlook,
        "net_score": round(net, 4),
        "positive_score": round(pos, 4),
        "negative_score": round(neg, 4),
        "confidence": _confidence_tier(dominant),
        "counts": {"positive": len(pos_items), "negative": len(neg_items)},
    }


def _confidence_tier(dominant_items) -> str:
    n = len(dominant_items)
    layers = {s["layer"] for s in dominant_items}
    if n >= 4 and len(layers) >= 3:
        return "high"
    if n >= 3 and len(layers) >= 2:
        return "medium-high"
    if n >= 2 and len(layers) >= 2:
        return "medium"
    if n >= 1:
        return "low"
    return "very low"


def watchlist_check(triggers: list) -> dict:
    """Section 3.1/3.2: trigger -> watchlist side + timeframe; both sides triggered -> negative takes priority."""
    sides = set()
    for t in triggers:
        side = t["side"]
        if side not in ("negative", "positive"):
            raise ValueError(f"Unknown watchlist side: {side!r}")
        sides.add(side)
    if not triggers:
        return {"entered": False, "side": None, "window_days": 0,
                "review": {}, "extension_max_days": 0, "note": ""}
    if "negative" in sides:
        note = "Negative watchlist conditions triggered"
        if "positive" in sides:
            note += "; positive triggers also present, negative takes priority"
        return {"entered": True, "side": "negative watchlist", "window_days": 90,
                "review": {"initial_review_days": 30, "full_review_days": 60},
                "extension_max_days": 60, "note": note}
    return {"entered": True, "side": "positive watchlist", "window_days": 90,
            "review": {"full_review_days": 60},
            "extension_max_days": 60, "note": "Positive watchlist conditions triggered"}


def load_migration_table(migration_md_path=None):
    """Parse Section 5.1 -> {rating: {upgrade, maintain, downgrade, default}};
    Section 5.3 -> {paradigm: (target, low_pp, high_pp)}."""
    path = Path(migration_md_path) if migration_md_path else engine_dir() / "outlook-monitoring-framework.md"
    text = path.read_text(encoding="utf-8")
    sec51 = re.search(r"### 5\.1 .*?(?=\n### |\Z)", text, re.DOTALL)
    if not sec51:
        raise ValueError("Section 5.1 paragraph missing")
    table = {}
    for row in re.finditer(
        r"^\|\s*\*\*(.+?)\*\*\s*\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|",
        sec51.group(0), re.MULTILINE,
    ):
        rating = row.group(1).strip()
        if rating == "Current Rating":
            continue
        table[rating] = {
            "upgrade": row.group(2).strip(), "maintain": row.group(3).strip(),
            "downgrade": row.group(4).strip(), "default": row.group(5).strip(),
        }
    if len(table) != 12:
        raise ValueError(f"Section 5.1 should have 12 rating rows, got {len(table)}")
    sec53 = re.search(r"### 5\.3 .*?(?=\n### |\n## |\Z)", text, re.DOTALL)
    if not sec53:
        raise ValueError("Section 5.3 paragraph missing")
    adj = {}
    for row in re.finditer(
        r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(upgrade|downgrade) probability\+(\d+)(?:-(\d+))?",
        sec53.group(0), re.MULTILINE,
    ):
        adj[row.group(1).strip()] = (row.group(2), int(row.group(3)), int(row.group(4) or row.group(3)))
    return table, adj


def _shift_range(range_text: str, low: int, high: int) -> str:
    """Shift interval bounds by pp (cap 100); '<N%' -> '<N+high%'; other non-numeric text returned as-is."""
    t = range_text.strip()
    m = re.match(r"^(\d+)(?:-(\d+))?%$", t)
    if m:
        lo, hi = int(m.group(1)), int(m.group(2) or m.group(1))
        lo2, hi2 = min(lo + low, 100), min(hi + high, 100)
        return f"{lo2}-{hi2}%" if lo2 != hi2 else f"{lo2}%"
    m = re.match(r"^<(\d+(?:\.\d+)?)%$", t)
    if m:
        v = float(m.group(1)) + high
        return f"<{v:g}%"
    return range_text


def migration_range(rating: str, paradigm: str = None, path=None) -> dict:
    """Section 5.1 base interval + Section 5.3 industry adjustment; merged rows ("A / A-") accept either sub-grade."""
    table, adj = load_migration_table(path)
    row = table.get(rating)
    if row is None:
        for key, cells in table.items():
            if "/" in key and rating in [p.strip() for p in key.split("/")]:
                row = cells
                break
    if row is None:
        raise ValueError(f"Unknown rating: {rating!r}")
    out = dict(row)
    note = ""
    if paradigm:
        if paradigm not in adj:
            raise ValueError(f"Unknown industry paradigm: {paradigm!r} (available {sorted(adj)})")
        target, low, high = adj[paradigm]
        out[target] = _shift_range(row[target], low, high)
        note = f"{paradigm}: {target} probability+{low}%" if low == high else f"{paradigm}: {target} probability+{low}-{high}%"
    out["paradigm_note"] = note
    return out
