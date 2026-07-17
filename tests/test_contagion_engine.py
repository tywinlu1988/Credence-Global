"""Tests for the WP-RO-02 contagion engine (internationalized matrix).

Single-source discipline: drift-gate expected values are parsed from documents
at runtime (SS2.3.1 coefficient table, SS5.5/5.6 top3, SS3.1 link list, SS3.3 count).
Tests do not replicate any matrix values; computation-layer tests use small fixture
matrices.
"""

import re
from pathlib import Path

import pytest

from src.contagion_engine import (
    ContagionCell,
    ContagionMatrix,
    apply_escalation,
    contagion_coefficients,
    col_sums,
    high_intensity_links,
    load_matrix,
    portfolio_exposure,
    row_sums,
    sri_weights,
    super_spreaders,
    vulnerable_industries,
)
from src.path_sheet import engine_dir

MATRIX_MD = engine_dir() / "contagion-matrix.md"
SYSTEMIC_MD = engine_dir() / "systemic-warning-framework.md"


@pytest.fixture(scope="module")
def matrix():
    return load_matrix(MATRIX_MD)


def _doc_text(path=MATRIX_MD):
    return path.read_text(encoding="utf-8")


# ---------------- parsing layer (real document) ----------------

def test_load_matrix_structure(matrix):
    assert len(matrix.industries) == 19
    cells = list(matrix.itercells())
    assert len(cells) == 19 * 18
    assert all(1 <= c.intensity <= 5 for c in cells)
    for ind in matrix.industries:
        assert matrix.intensity(ind, ind) == 0  # diagonal


def test_load_matrix_unknown_pair_raises(matrix):
    with pytest.raises(ValueError, match="unknown industry pair"):
        matrix.cell("NonExistent", "Energy")


# ---------------- drift gates (values from documents at runtime) ----------------

def _systemic_coefficient_table():
    """Parse systemic SS2.3.1: {industry: row_total_score}."""
    text = _doc_text(SYSTEMIC_MD)
    sec = re.search(r"#### 2\.3\.1.*?(?=####|\Z)", text, re.DOTALL).group(0)
    out = {}
    for m in re.finditer(r"^\|\s*\d+\s*\|\s*(.+?)\s*\|\s*(\d+)\s*\|", sec, re.MULTILINE):
        out[m.group(1).strip()] = int(m.group(2))
    return out


def test_row_sums_match_systemic_table(matrix):
    assert row_sums(matrix) == _systemic_coefficient_table()


def _section_top3(header_regex):
    text = _doc_text()
    sec = re.search(header_regex + r".*?(?=###|\Z)", text, re.DOTALL).group(0)
    return [
        m.group(1).strip()
        for m in re.finditer(r"^\|\s*\*\*\d+\*\*\s*\|\s*\*\*(.+?)\*\*\s*\|", sec, re.MULTILINE)
    ]


def test_super_spreaders_match_doc(matrix):
    doc_top3 = _section_top3(r"### 5\.5")
    assert [name for name, _ in super_spreaders(matrix)] == doc_top3


def test_vulnerable_industries_match_doc(matrix):
    doc_top3 = _section_top3(r"### 5\.6")
    assert [name for name, _ in vulnerable_industries(matrix)] == doc_top3


def _doc_high_intensity_pairs():
    """Parse SS3.1 code block link list -> {frozenset({a, b}): bidirectional}."""
    text = _doc_text()
    sec = re.search(r"### 3\.1.*?```\n(.*?)```", text, re.DOTALL).group(1)
    pairs = {}
    for ln in sec.splitlines():
        m = re.match(r"\s*(.+?)\s*(↔|→)\s*(.+?)\s*\(", ln)
        if m:
            a, arrow, b = m.group(1).strip(), m.group(2), m.group(3).strip()
            pairs[frozenset((a, b))] = arrow == "↔"
    return pairs


def test_high_intensity_links_match_doc(matrix):
    links = high_intensity_links(matrix, threshold=4)
    computed = {}
    for c in links:
        key = frozenset((c.source, c.target))
        computed.setdefault(key, []).append(c)
    doc_pairs = _doc_high_intensity_pairs()
    assert set(computed) == set(doc_pairs)
    for key, cells in computed.items():
        assert (len(cells) == 2) == doc_pairs[key], (
            f"directionality mismatch for {sorted(key)}"
        )


def test_low_intensity_count_matches_doc(matrix):
    n = sum(1 for c in matrix.itercells() if c.intensity <= 2)
    m = re.search(r"industries with intensity ≤2, total (\d+) pairs", _doc_text())
    assert n == int(m.group(1))


# ---------------- derived calculations (real matrix + fixture) ----------------

def test_contagion_coefficients_normalized(matrix):
    coefs = contagion_coefficients(matrix)
    assert len(coefs) == 19
    mean = sum(coefs.values()) / len(coefs)
    assert abs(mean - 1.0) < 1e-9  # coefficient mean is always 1.0 (row_total/mean)
    # verify against systemic SS2.3.1 coefficient column (tolerance: doc retains 3 decimals)
    text = _doc_text(SYSTEMIC_MD)
    for m in re.finditer(
        r"^\|\s*\d+\s*\|\s*(.+?)\s*\|\s*\d+\s*\|\s*\d+\s*/\s*[\d.]+\s*=\s*([\d.]+)\s*\|",
        text, re.MULTILINE,
    ):
        assert abs(coefs[m.group(1).strip()] - float(m.group(2))) < 5e-4


def test_sri_weights():
    coefs = {"A": 1.2, "B": 0.8}
    w = sri_weights({"A": 0.5, "B": 0.5}, coefs)
    assert abs(sum(w.values()) - 1.0) < 1e-9
    assert w["A"] > w["B"]  # higher coefficient -> higher weight
    with pytest.raises(ValueError):
        sri_weights({"A": 0.5}, coefs)  # key mismatch


# ---------------- portfolio analysis (fixture mini matrix) ----------------

def _mini():
    inds = ["A", "B", "C"]
    cells = {}
    vals = {("A", "B"): 4, ("B", "A"): 2, ("A", "C"): 1,
            ("C", "A"): 5, ("B", "C"): 3, ("C", "B"): 2}
    for (s, t), n in vals.items():
        cells[(s, t)] = ContagionCell(s, t, n, types=("C",), confidence="M", bidirectional=n >= 4)
    return ContagionMatrix(inds, cells)


def test_portfolio_exposure_math():
    m = _mini()
    exp = portfolio_exposure(m, {"A": 0.5, "B": 0.3, "C": 0.2})
    by_ind = {e["industry"]: e for e in exp}
    # A inbound exposure = B->A(2)x0.3 + C->A(5)x0.2 = 1.6
    assert abs(by_ind["A"]["inbound"] - 1.6) < 1e-9
    # A outbound = A->B(4)x0.3 + A->C(1)x0.2 = 1.4
    assert abs(by_ind["A"]["outbound"] - 1.4) < 1e-9
    assert exp[0]["inbound"] >= exp[-1]["inbound"]  # descending
    with pytest.raises(ValueError):
        portfolio_exposure(m, {})


def test_high_intensity_links_threshold():
    m = _mini()
    links = high_intensity_links(m, threshold=4)
    assert {(c.source, c.target) for c in links} == {("A", "B"), ("C", "A")}
    assert links[0].intensity >= links[-1].intensity
    subset = high_intensity_links(m, industries=["A", "B"], threshold=1)
    assert {(c.source, c.target) for c in subset} == {("A", "B"), ("B", "A")}


# ---------------- stress escalation (SS6.2) ----------------

def test_apply_escalation_explicit_and_generic(matrix):
    stressed = apply_escalation(matrix, ["Market Panic"])
    # explicit pair (doc SS6.2 rule1): Semis -> Autos
    assert stressed.intensity("Technology Hardware (Semis)", "Automobiles") == 5
    # generic rule: S-flagged +1 (Biotech -> Financials, C+S flag, non-explicit: 2->3)
    assert stressed.intensity("Biotech & Pharma", "Financials (Banks/Insurance)") == 3
    # non S/L and non-explicit pair unchanged (Capital Goods -> Autos, C flag, stays 3)
    assert stressed.intensity("Capital Goods", "Automobiles") == 3
    # original matrix unchanged
    assert matrix.intensity("Technology Hardware (Semis)", "Automobiles") == 4


def test_apply_escalation_year_end_lgfv_and_cap(matrix):
    stressed = apply_escalation(matrix, ["Year-End Effect"])
    assert stressed.intensity("Sovereigns & GSEs", "Transportation (Air/Rail/Shipping)") == 5  # 4+1 cap at 5
    assert stressed.intensity("Sovereigns & GSEs", "Consumer Staples") == 2  # 1+1
    assert stressed.intensity("Energy (Oil & Gas)", "Consumer Staples") == 2  # non-Sov pair +0
    with pytest.raises(ValueError, match="unknown escalation factor"):
        apply_escalation(matrix, ["nonexistent_factor"])


def test_apply_escalation_stacks(matrix):
    stressed = apply_escalation(matrix, ["Market Panic", "Regulatory Vacuum"])
    assert stressed.intensity("Sovereigns & GSEs", "Transportation (Air/Rail/Shipping)") == 5


def test_escalation_rules_covered_in_doc():
    """Every coded explicit jump pair must be greppable in SS6.2 text (silent drift guard)."""
    from src.contagion_engine import _EXPLICIT_JUMPS

    text = _doc_text()
    sec = re.search(r"### 6\.2.*?(?=### 6\.3|\Z)", text, re.DOTALL).group(0)
    for factor, jumps in _EXPLICIT_JUMPS.items():
        assert factor in sec, f"SS6.2 missing factor paragraph: {factor}"
        for (_s, _t, base, stressed, label) in jumps:
            assert label in sec, f"SS6.2 missing jump pair: {factor}/{label}"
            row = next(ln for ln in sec.splitlines() if label in ln)
            assert f"| {base} |" in row and f"| {stressed} |" in row, row


def test_strength3_links_match_doc(matrix):
    """SS3.2 list cross-checks matrix: intensity=3 directed set + unique pair count."""
    text = _doc_text()
    sec = re.search(r"### 3\.2.*?```\n(.*?)```", text, re.DOTALL).group(1)
    doc_edges = set()
    for ln in sec.splitlines():
        m = re.match(r"\s*(.+?)\s*(↔|→)\s*(.+?)\s*\(", ln)
        if m:
            doc_edges.add((m.group(1).strip(), m.group(3).strip()))
    computed = {(c.source, c.target) for c in matrix.itercells() if c.intensity == 3}
    assert doc_edges == computed
    assert len(doc_edges) == 24
    assert len({frozenset(e) for e in doc_edges}) == 12
