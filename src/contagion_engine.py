"""WP-M4-02 re-executable implementation of contagion-matrix.md (contagion matrix + portfolio exposure + stress escalation).

Single source of truth: matrix data (Section 2.1 intensity heatmap + Section 2.4 full annotation
table) is parsed from the engine document at runtime, not duplicated; derived semantics follow
contagion-matrix.md Sections 5.5/5.6 (super-spreaders = row-sum top 3, vulnerable industries =
column-sum top 3) and systemic-warning-framework.md Section 2.3 (contagion coefficient =
row-sum / mean of all industry row-sums, industry weight = debt share x coefficient then
normalized). Section 6.2 stress escalation rules are encoded as code logic (following the
sri_calculator precedent), with each explicit jump pair covered by a documentation parity test
(tests/test_contagion_engine.py).
"""

import re
from dataclasses import dataclass
from pathlib import Path

from src.path_sheet import engine_dir

INTENSITY_MIN, INTENSITY_MAX = 1, 5
CONTAGION_TYPES = frozenset("CRLS")  # Credit Chain / Regional Resonance / Liquidity Squeeze / Confidence Collapse (Section 2.2)
N_INDUSTRIES = 19

ESCALATION_FACTORS = ("Market Panic", "Regulatory Vacuum", "High Leverage", "Information Asymmetry", "Year-End Effect")

# Section 6.2 explicit jump table: (source, target, base intensity, stressed intensity, document pair label).
# Only encodes base intensities that match the matrix table directions (e.g., Tech HW -> Software base 4).
_EXPLICIT_JUMPS = {
    "Market Panic": [
        ("Technology Hardware (Semiconductors)", "Software & Services", 4, 5, "Technology Hardware → Software"),
        ("Technology Hardware (Semiconductors)", "Automobiles", 4, 5, "Technology Hardware → Automobiles"),
        ("Consumer Staples", "Retail", 3, 4, "Consumer Staples ↔ Retail"),
        ("Retail", "Consumer Staples", 3, 4, "Consumer Staples ↔ Retail"),
    ],
    "Regulatory Vacuum": [
        ("Sovereigns & GSEs", "Utilities (Regulated)", 3, 4, "Sovereigns → Utilities"),
        ("Sovereigns & GSEs", "Energy (Oil & Gas)", 3, 4, "Sovereigns → Energy"),
        ("Sovereigns & GSEs", "Metals & Mining", 3, 4, "Sovereigns → Metals & Mining"),
        ("Sovereigns & GSEs", "Construction Materials", 3, 4, "Sovereigns → Construction Materials"),
    ],
    "High Leverage": [
        ("Financials (Banks/Insurance)", "Technology Hardware (Semiconductors)", 3, 4, "Financials → Technology Hardware"),
        ("Financials (Banks/Insurance)", "Software & Services", 3, 4, "Financials → Software & Services"),
        ("Financials (Banks/Insurance)", "Capital Goods", 3, 4, "Financials → Capital Goods"),
    ],
    "Information Asymmetry": [],
    "Year-End Effect": [],
}

# Section 6.2 generic type-bump rules: factor -> affected contagion-type set (matches get +1, cap 5).
# Market Panic = S/L (Rule 1); Information Asymmetry = C/R (Rule 4); High Leverage = L (Rule 3's
# "All pairs with 'L' mark -> Base + 1"). Rule 2 specifies "+0~+1" and Rule 5 "all +0~+1" as fuzzy
# ranges left to LLM judgment, encoded as +0.
_GENERIC_TYPE_BUMP = {
    "Market Panic": frozenset("SL"),
    "Information Asymmetry": frozenset("CR"),
    "High Leverage": frozenset("L"),
}

# Section 6.2 Rules 1/2 "Financials → All 3 (avg) → 4 (avg)": deterministic encoding lifts
# Financials-source cells with base intensity exactly 3 to 4. Rule 3's broad row (3→3.5 avg) is
# fuzzy (half-point) and left to LLM judgment, not coded.
_BROAD_FINANCIALS_LIFT = {"Market Panic", "Regulatory Vacuum"}

# Section 6.3 synergy multipliers: when the triggered factor set forms a documented
# combination, the TOTAL increment (boosted - base) on every touched cell is multiplied.
# Three or more simultaneous factors -> 3.0x (dominates any pair combination).
_SYNERGY_MULTIPLIERS = {
    frozenset({"Market Panic", "Regulatory Vacuum"}): 1.5,
    frozenset({"Market Panic", "High Leverage"}): 2.0,
    frozenset({"Regulatory Vacuum", "Year-End Effect"}): 1.5,
}
_SYNERGY_THREE_OR_MORE = 3.0


@dataclass(frozen=True)
class ContagionCell:
    source: str
    target: str
    intensity: int
    types: tuple = ()
    confidence: str = "-"
    bidirectional: bool = False


class ContagionMatrix:
    """19-industry directed contagion matrix (parsed from contagion-matrix.md, immutable)."""

    def __init__(self, industries, cells):
        self.industries = list(industries)
        self._cells = dict(cells)

    def cell(self, source, target) -> ContagionCell:
        try:
            return self._cells[(source, target)]
        except KeyError:
            raise ValueError(
                f"Unknown industry pair: {source!r} -> {target!r} (known {len(self.industries)} industries)"
            ) from None

    def intensity(self, source, target) -> int:
        if source == target:
            return 0
        return self.cell(source, target).intensity

    def itercells(self):
        return iter(self._cells.values())

    def with_intensities(self, overrides) -> "ContagionMatrix":
        cells = dict(self._cells)
        for (s, t), n in overrides.items():
            c = self.cell(s, t)
            cells[(s, t)] = ContagionCell(s, t, n, c.types, c.confidence, c.bidirectional)
        return ContagionMatrix(self.industries, cells)


# ---------------------------------------------------------------------------
# Parsing layer (Section 2.1 heatmap + Section 2.4 full annotation; doc = single source of truth)
# ---------------------------------------------------------------------------

def _parse_heatmap(text: str):
    """Section 2.1 code block -> 19x19 intensity grid {(i,j): int} (0-based index)."""
    sec = re.search(r"### 2\.1 .*?(?=### 2\.2 )", text, re.DOTALL)
    if not sec:
        raise ValueError("Section 2.1 heatmap paragraph missing")
    block = re.search(r"```\n(.*?)```", sec.group(0), re.DOTALL)
    if not block:
        raise ValueError("Section 2.1 code block missing")
    lines = [ln for ln in block.group(1).splitlines() if "│" in ln]
    if len(lines) != N_INDUSTRIES + 1:
        raise ValueError(f"Section 2.1 heatmap should have {N_INDUSTRIES + 1} lines with │, got {len(lines)}")
    abbrevs = lines[0].split("│", 1)[1].split()
    if len(abbrevs) != N_INDUSTRIES:
        raise ValueError(f"Section 2.1 column headers should have {N_INDUSTRIES} industry abbreviations, got {len(abbrevs)}")
    grid = {}
    for i, ln in enumerate(lines[1:]):
        _name, _, rest = ln.partition("│")
        cells = rest.split()
        if len(cells) != N_INDUSTRIES:
            raise ValueError(f"Section 2.1 row {i + 1} should have {N_INDUSTRIES} cells, got {len(cells)}")
        for j, v in enumerate(cells):
            if i == j:
                if v != "-":
                    raise ValueError(f"Section 2.1 diagonal ({i},{j}) should be '-', got {v!r}")
            else:
                n = int(v)
                if not INTENSITY_MIN <= n <= INTENSITY_MAX:
                    raise ValueError(f"Section 2.1 intensity out of range ({i},{j}): {n}")
                grid[(i, j)] = n
    return grid


def _parse_full_matrix(text: str):
    """Section 2.4 row blocks -> (19 canonical names, {(i,j): (types, confidence, bidirectional, intensity)}).

    Only annotated cells (intensity >= 3) are documented in Section 2.4.
    """
    blocks = list(re.finditer(
        r"#### Row (\d+): (.+?)\s*\n(.*?)(?=\n#### |\n## |\Z)", text, re.DOTALL
    ))
    if len(blocks) != N_INDUSTRIES:
        raise ValueError(f"Section 2.4 should have {N_INDUSTRIES} row blocks, got {len(blocks)}")
    full_names, marks = [], {}
    for bm in blocks:
        i = int(bm.group(1))
        if i != len(full_names) + 1:
            raise ValueError(f"Section 2.4 row block sequence non-contiguous: row {i}")
        name = bm.group(2).strip()
        full_names.append(name)
        for row in re.finditer(
            r"^\|\s*(\d+)→(\d+)\s+[^|]*?\|\s*([CRLS+\-]+)\s*\|\s*(\d+)\s*\|"
            r"\s*([HML-])\s*\|\s*(↔|→|-)\s*\|",
            bm.group(3), re.MULTILINE,
        ):
            bi, bj = int(row.group(1)), int(row.group(2))
            if bi != i:
                raise ValueError(f"Section 2.4 row {i} block has {bi}->{bj}")
            types = tuple(ch for ch in row.group(3) if ch in CONTAGION_TYPES)
            marks[(bi, bj)] = (types, row.group(5), row.group(6) == "↔", int(row.group(4)))
    return full_names, marks


def load_matrix(matrix_md_path=None) -> ContagionMatrix:
    """Parse 19x19 contagion matrix from contagion-matrix.md (Sections 2.1 and 2.4 cross-validated).

    Section 2.4 only annotates cells with intensity >= 3; unannotated cells receive
    default values (empty types, confidence "-", not bidirectional).
    """
    path = Path(matrix_md_path) if matrix_md_path else engine_dir() / "contagion-matrix.md"
    text = path.read_text(encoding="utf-8")
    grid = _parse_heatmap(text)
    full_names, marks = _parse_full_matrix(text)
    cells = {}
    for (i, j), n in grid.items():
        s, t = full_names[i], full_names[j]
        m = marks.get((i + 1, j + 1))  # Section 2.4 labels are 1-based
        if m is not None:
            types, conf, bidir, mn = m
            if mn != n:
                raise ValueError(f"Section 2.1 vs Section 2.4 intensity mismatch ({i}->{j}): {n} vs {mn}")
        else:
            types, conf, bidir = (), "-", False
        cells[(s, t)] = ContagionCell(s, t, n, types, conf, bidir)
    return ContagionMatrix(full_names, cells)


# ---------------------------------------------------------------------------
# Derived computation (Sections 5.5/5.6 + systemic Section 2.3)
# ---------------------------------------------------------------------------

def row_sums(matrix) -> dict:
    """Row sum = outgoing contagion force (Section 5.5 super-spreader score)."""
    return {s: sum(matrix.intensity(s, t) for t in matrix.industries if t != s)
            for s in matrix.industries}


def col_sums(matrix) -> dict:
    """Column sum = incoming contagion exposure (Section 5.6 vulnerable industry score)."""
    return {t: sum(matrix.intensity(s, t) for s in matrix.industries if s != t)
            for t in matrix.industries}


def _top(scores: dict, n: int) -> list:
    return sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))[:n]


def super_spreaders(matrix, top=3) -> list:
    return _top(row_sums(matrix), top)


def vulnerable_industries(matrix, top=3) -> list:
    return _top(col_sums(matrix), top)


def contagion_coefficients(matrix) -> dict:
    """Contagion coefficient = row sum / mean of all industry row sums (systemic Section 2.3)."""
    sums = row_sums(matrix)
    mean = sum(sums.values()) / len(sums)
    return {k: v / mean for k, v in sums.items()}


def sri_weights(debt_shares: dict, coefficients: dict) -> dict:
    """Industry weight = debt share x contagion coefficient, normalized (systemic Section 2.3)."""
    if set(debt_shares) != set(coefficients):
        raise ValueError("debt_shares and coefficients industry sets do not match")
    if any(v < 0 for v in debt_shares.values()):
        raise ValueError("debt_shares does not allow negative values")
    raw = {k: debt_shares[k] * coefficients[k] for k in debt_shares}
    total = sum(raw.values())
    if total <= 0:
        raise ValueError("weighted sum must be positive")
    return {k: v / total for k, v in raw.items()}


# ---------------------------------------------------------------------------
# Portfolio analysis (WP-M4-02 output)
# ---------------------------------------------------------------------------

def portfolio_exposure(matrix, holdings: dict) -> list:
    """Each holding's inbound contagion exposure and outbound contagion force (other industry intensity x
    its weight), sorted by exposure descending."""
    if not holdings:
        raise ValueError("holdings cannot be empty")
    for ind, w in holdings.items():
        if ind not in matrix.industries:
            raise ValueError(f"Unknown industry: {ind!r}")
        if w < 0:
            raise ValueError(f"Weight does not allow negative values: {ind}={w}")
    out = []
    for h in holdings:
        inbound = sum(matrix.intensity(s, h) * w
                      for s, w in holdings.items() if s != h)
        outbound = sum(matrix.intensity(h, t) * w
                       for t, w in holdings.items() if t != h)
        out.append({"industry": h, "inbound": inbound, "outbound": outbound})
    out.sort(key=lambda e: (-e["inbound"], e["industry"]))
    return out


def high_intensity_links(matrix, industries=None, threshold=4) -> list:
    """(Within portfolio) directed contagion edges with intensity >= threshold, sorted descending by intensity
    (Section 3.1 graph data morphology)."""
    inds = list(industries) if industries is not None else matrix.industries
    links = [
        matrix.cell(s, t)
        for s in inds for t in inds
        if s != t and matrix.intensity(s, t) >= threshold
    ]
    links.sort(key=lambda c: (-c.intensity, c.source, c.target))
    return links


# ---------------------------------------------------------------------------
# Stress escalation (Section 6.2)
# ---------------------------------------------------------------------------

def apply_escalation(matrix, factors) -> ContagionMatrix:
    """Given a set of triggered escalation factors, return a stressed matrix (explicit pair jumps + generic
    type +1, cap 5; original matrix unchanged). Duplicate factors are deduplicated at entry — the same
    factor never applies its generic bump twice.

    §6.3 synergy: when the triggered set forms a documented combination (Panic+Vacuum 1.5x,
    Panic+Leverage 2.0x, Vacuum+Year-End 1.5x, any 3+ factors 3.0x), the TOTAL increment on every
    touched cell is multiplied (cap 5). Rule 3's "Financials → All (broad) 3→3.5 (avg)" half-point
    row is fuzzy and left to LLM judgment, not coded."""
    unknown = sorted(set(factors) - set(ESCALATION_FACTORS))
    if unknown:
        raise ValueError(f"Unknown escalation factors: {unknown}, available: {list(ESCALATION_FACTORS)}")
    boosts = {}
    for f in dict.fromkeys(factors):
        for (s, t, base, stressed, _label) in _EXPLICIT_JUMPS.get(f, []):
            if s not in matrix.industries or t not in matrix.industries:
                continue  # explicit jump pair not present in a subset/fixture matrix
            cur = matrix.intensity(s, t)
            if cur != base:
                raise ValueError(
                    f"Section 6.2 jump base drift: {f} {s}->{t} document base intensity={base}, matrix actual={cur}"
                )
            key = (s, t)
            boosts[key] = max(boosts.get(key, cur), stressed)
        if f in _BROAD_FINANCIALS_LIFT:
            for c in matrix.itercells():
                if c.source == "Financials (Banks/Insurance)" and c.intensity == 3:
                    key = (c.source, c.target)
                    boosts[key] = max(boosts.get(key, c.intensity), 4)
        types = _GENERIC_TYPE_BUMP.get(f)
        if types:
            for c in matrix.itercells():
                if set(c.types) & types:
                    key = (c.source, c.target)
                    cur = boosts.get(key, c.intensity)
                    boosts[key] = min(cur + 1, INTENSITY_MAX)
        if f == "Year-End Effect":  # Rule 5: "Financials → All" +1, source direction only
            # ("all +0~+1" fuzzy range left to LLM judgment, encoded as +0)
            for c in matrix.itercells():
                if c.source == "Financials (Banks/Insurance)":
                    key = (c.source, c.target)
                    cur = boosts.get(key, c.intensity)
                    boosts[key] = min(cur + 1, INTENSITY_MAX)

    # §6.3 synergy: documented factor combinations multiply the total increment on
    # touched cells (cap 5). Three or more simultaneous factors -> 3.0x.
    triggered = set(factors)
    if len(triggered) >= 3:
        multiplier = _SYNERGY_THREE_OR_MORE
    else:
        multiplier = _SYNERGY_MULTIPLIERS.get(frozenset(triggered))
    if multiplier and len(triggered) >= 2:
        for key, boosted in boosts.items():
            base = matrix.intensity(*key)
            delta = boosted - base
            if delta > 0:
                boosts[key] = min(base + round(delta * multiplier), INTENSITY_MAX)
    return matrix.with_intensities(boosts)
