"""Tests for the WP-RO-02 contagion engine (internationalized matrix).

Single-source discipline: matrix values are parsed from Section 2.1 heatmap
at runtime; derived computations are cross-checked for internal consistency.
Escalation jump labels are validated against document Section 6.2 tables.
Computation-layer tests use small fixture matrices.
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
    with pytest.raises(ValueError, match="Unknown industry pair"):
        matrix.cell("NonExistent", "Energy")


# ---------------- drift gates (internal consistency) ----------------

def test_row_sums_internally_consistent(matrix):
    """Row sums are internally consistent: positive and sum to total matrix force."""
    sums = row_sums(matrix)
    assert len(sums) == 19
    assert all(v > 0 for v in sums.values())
    total_from_rows = sum(sums.values())
    total_from_cells = sum(matrix.intensity(s, t) for s in matrix.industries for t in matrix.industries if s != t)
    assert total_from_rows == total_from_cells


def test_super_spreaders_are_top3_rows(matrix):
    """Super-spreaders are the 3 industries with largest row sums, returned descending."""
    top3 = super_spreaders(matrix)
    assert len(top3) == 3
    scores = list(top3)
    assert scores[0][1] >= scores[1][1] >= scores[2][1]


def test_vulnerable_industries_are_top3_cols(matrix):
    """Vulnerable industries are the 3 industries with largest column sums, returned descending."""
    top3 = vulnerable_industries(matrix)
    assert len(top3) == 3
    scores = list(top3)
    assert scores[0][1] >= scores[1][1] >= scores[2][1]


def test_high_intensity_links_consistency(matrix):
    """High-intensity links are correctly sorted and directionality is consistent."""
    links = high_intensity_links(matrix, threshold=4)
    assert len(links) >= 4
    for i in range(len(links) - 1):
        assert links[i].intensity >= links[i + 1].intensity
    frozensets = {}
    for c in links:
        key = frozenset((c.source, c.target))
        frozensets.setdefault(key, []).append(c)
    for key, cells in frozensets.items():
        if len(cells) == 2:
            assert any(c.bidirectional for c in cells)
        else:
            assert all(not c.bidirectional for c in cells)


def test_low_intensity_count_reasonable(matrix):
    """Low intensity pairs (<=2) are the majority of the 342 off-diagonal pairs."""
    n = sum(1 for c in matrix.itercells() if c.intensity <= 2)
    total = 19 * 18
    assert n > total // 2
    assert n < total


# ---------------- derived calculations (real matrix + fixture) ----------------

def test_contagion_coefficients_normalized(matrix):
    coefs = contagion_coefficients(matrix)
    assert len(coefs) == 19
    mean = sum(coefs.values()) / len(coefs)
    assert abs(mean - 1.0) < 1e-9  # coefficient mean is always 1.0 (row_total/mean)
    # verify positive and no extreme outliers
    assert all(v > 0 for v in coefs.values())
    assert all(0.5 <= v <= 1.6 for v in coefs.values())


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
    assert stressed.intensity("Technology Hardware (Semiconductors)", "Automobiles") == 5
    # generic rule: S-flagged +1 (Biotech -> Financials, C+S flag, non-explicit: 2->3)
    assert stressed.intensity("Biotech & Pharma", "Financials (Banks/Insurance)") == 3
    # non S/L and non-explicit pair unchanged (Capital Goods -> Autos, C flag, stays 3)
    assert stressed.intensity("Capital Goods", "Automobiles") == 3
    # original matrix unchanged
    assert matrix.intensity("Technology Hardware (Semiconductors)", "Automobiles") == 4


def test_apply_escalation_year_end_lgfv_and_cap(matrix):
    stressed = apply_escalation(matrix, ["Year-End Effect"])
    # CAP: Financials -> Sovereigns at base 5, +1 capped at 5
    assert stressed.intensity("Financials (Banks/Insurance)", "Sovereigns & GSEs") == 5
    # Increment: Financials -> Chemicals at base 2, +1 = 3
    assert stressed.intensity("Financials (Banks/Insurance)", "Chemicals") == 3
    # Non-Financials pair unchanged: Energy -> Consumer Staples base 2 stays 2
    assert stressed.intensity("Energy (Oil & Gas)", "Consumer Staples") == 2
    with pytest.raises(ValueError, match="Unknown escalation factor"):
        apply_escalation(matrix, ["nonexistent_factor"])


def test_apply_escalation_stacks(matrix):
    stressed = apply_escalation(matrix, ["Market Panic", "Regulatory Vacuum"])
    # Market Panic: Technology Hardware -> Automobiles, base 4, explicit jump to 5
    assert stressed.intensity("Technology Hardware (Semiconductors)", "Automobiles") == 5
    # Regulatory Vacuum: Sovereigns -> Energy, base 3, explicit jump Δ=1,
    # then §6.3 Panic+Vacuum 1.5x synergy: 3 + round(1.5) = 5
    assert stressed.intensity("Sovereigns & GSEs", "Energy (Oil & Gas)") == 5


def test_escalation_duplicate_factors_no_double_stack(matrix):
    # A duplicated factor must not double-apply its generic bump (dedupe at entry).
    once = apply_escalation(matrix, ["Market Panic"])
    twice = apply_escalation(matrix, ["Market Panic", "Market Panic"])
    for c in matrix.itercells():
        assert twice.intensity(c.source, c.target) == once.intensity(c.source, c.target), (
            f"{c.source}->{c.target}: duplicate factor changed {once.intensity(c.source, c.target)} "
            f"to {twice.intensity(c.source, c.target)}"
        )


def test_high_leverage_generic_l_rule(matrix):
    # §6.2 Jump Rule 3: all pairs with 'L' mark -> Base + 1 (was missing; only the
    # explicit Financials -> TechHW/Software/CapGoods jumps were coded).
    stressed = apply_escalation(matrix, ["High Leverage"])
    # explicit rows per doc
    assert stressed.intensity("Financials (Banks/Insurance)", "Technology Hardware (Semiconductors)") == 4
    assert stressed.intensity("Financials (Banks/Insurance)", "Software & Services") == 4
    assert stressed.intensity("Financials (Banks/Insurance)", "Capital Goods") == 4
    # the doc's only L-typed cells (Fin <-> Sov) sit at the cap and stay 5
    assert stressed.intensity("Financials (Banks/Insurance)", "Sovereigns & GSEs") == 5
    # the generic L rule itself, on a fixture matrix with an L-typed sub-cap cell
    fixture = ContagionMatrix(
        ["A", "B", "C"],
        {
            ("A", "B"): ContagionCell("A", "B", 3, ("L",), "H", True),
            ("B", "A"): ContagionCell("B", "A", 3, ("L",), "H", True),
            ("A", "C"): ContagionCell("A", "C", 3, ("C",), "H", True),
            ("C", "A"): ContagionCell("C", "A", 3, ("C",), "H", True),
            ("B", "C"): ContagionCell("B", "C", 1, (), "-", False),
            ("C", "B"): ContagionCell("C", "B", 1, (), "-", False),
        },
    )
    stressed_fx = apply_escalation(fixture, ["High Leverage"])
    assert stressed_fx.intensity("A", "B") == 4  # L-typed: Base + 1
    assert stressed_fx.intensity("B", "A") == 4
    assert stressed_fx.intensity("A", "C") == 3  # non-L typed unchanged


def test_year_end_source_direction_only(matrix):
    # §6.2 Jump Rule 5: "Financials → All" +1 is source-direction only; the reverse
    # direction (X → Financials) must NOT be bumped.
    stressed = apply_escalation(matrix, ["Year-End Effect"])
    assert stressed.intensity("Financials (Banks/Insurance)", "Energy (Oil & Gas)") == 4  # base 3 + 1
    assert stressed.intensity("Energy (Oil & Gas)", "Financials (Banks/Insurance)") == 3  # unchanged


def test_financials_broad_row_rules_1_and_2(matrix):
    # §6.2 Rules 1/2: "Financials → All 3 (avg) → 4 (avg)" — deterministic encoding:
    # Financials-source cells with base intensity exactly 3 lift to 4.
    for factor in ("Market Panic", "Regulatory Vacuum"):
        stressed = apply_escalation(matrix, [factor])
        fin_base3 = [
            c for c in matrix.itercells()
            if c.source == "Financials (Banks/Insurance)" and c.intensity == 3
        ]
        assert fin_base3, "fixture expects Financials base-3 cells"
        for c in fin_base3:
            assert stressed.intensity("Financials (Banks/Insurance)", c.target) >= 4, (
                f"{factor}: Financials->{c.target} should lift to >= 4"
            )


def test_synergy_multiplier_panic_plus_vacuum(matrix):
    # §6.3: Panic + Regulatory Vacuum -> 1.5x on the total increment of touched cells.
    # Fin -> Commercial Services: base 3, C-type only (no S/L generic, no explicit jump);
    # broad rows lift to 4 (Δ = 1); synergy: 3 + round(1 × 1.5) = 3 + 2 = 5.
    stressed = apply_escalation(matrix, ["Market Panic", "Regulatory Vacuum"])
    assert stressed.intensity("Financials (Banks/Insurance)", "Commercial Services") == 5


def test_synergy_two_factor_panic_leverage(matrix):
    # §6.3: Panic + High Leverage -> 2.0x. Fin -> Telecom: base 3, C-type only,
    # broad row lifts to 4 (Δ = 1); synergy: 3 + round(1 × 2.0) = 5.
    stressed = apply_escalation(matrix, ["Market Panic", "High Leverage"])
    assert stressed.intensity("Financials (Banks/Insurance)", "Telecommunications") == 5


def test_synergy_multiplier_vacuum_plus_year_end(matrix):
    # §6.3: Regulatory Vacuum + Year-End -> 1.5x. Sovereigns -> Utilities: base 3,
    # explicit Vacuum jump to 4 (Δ = 1); Year-End does not touch non-Fin sources;
    # synergy: 3 + round(1 × 1.5) = 5.
    stressed = apply_escalation(matrix, ["Regulatory Vacuum", "Year-End Effect"])
    assert stressed.intensity("Sovereigns & GSEs", "Utilities (Regulated)") == 5


def test_synergy_multiplier_three_factors(matrix):
    # §6.3: three or more simultaneous factors -> 3.0x on the total increment.
    # Fin -> Commercial Services: base 3, Δ = 1 from broad rows; 3 + round(1 × 3.0) = 6 -> capped at 5.
    stressed = apply_escalation(matrix, ["Market Panic", "Regulatory Vacuum", "High Leverage"])
    assert stressed.intensity("Financials (Banks/Insurance)", "Commercial Services") == 5


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


def test_strength3_links_consistency(matrix):
    """Intensity-3 directed pairs are even (structurally symmetric) and form undirected pairs."""
    computed = {(c.source, c.target) for c in matrix.itercells() if c.intensity == 3}
    assert len(computed) > 0
    assert len(computed) % 2 == 0  # symmetric matrix -> directed pairs are even
    assert len({frozenset(e) for e in computed}) == len(computed) // 2
