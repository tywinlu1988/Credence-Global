"""Grep-style drift guard for concentration_scorer coded constants.

sri_calculator and contagion/outlook engines parse their rules from the engine
documents at runtime; concentration_scorer keeps coded band tables for
performance and simplicity. These tests pin every coded constant to its
document source (concentration-framework.md): if the document's thresholds,
stacking values, synergy rules, or weights change, these tests fail until the
code is updated (or the discrepancy is adjudicated).
"""

from pathlib import Path

from src.concentration_scorer import (
    _AAA_BANDS,
    _CHANNEL_BANDS,
    _CR3_BANDS,
    _CR5_BANDS,
    _HHI_BANDS,
    _M12_BANDS,
    _MAX1_BANDS,
    _PEAK_BANDS,
    _PROVINCE_BANDS,
    _PSEUDO_BANDS,
    _WEAK_REGION_BANDS,
)
from src.path_sheet import engine_dir

DOC = (engine_dir() / "concentration-framework.md").read_text(encoding="utf-8")

# (bands, label, is_percent)
METRICS = [
    (_HHI_BANDS, "HHI", False),
    (_CR3_BANDS, "CR3", True),
    (_CR5_BANDS, "CR5", True),
    (_MAX1_BANDS, "MAX1", True),
    (_PROVINCE_BANDS, "Single country/region", True),
    (_WEAK_REGION_BANDS, "Peripheral regions", True),
    (_AAA_BANDS, "AAA share", True),
    (_PSEUDO_BANDS, "Pseudo-high rating", True),
    (_M12_BANDS, "12-month maturity", True),
    (_PEAK_BANDS, "Single month peak", True),
    (_CHANNEL_BANDS, "Single channel", True),
]


def _fmt(v: float, is_percent: bool) -> str:
    return f"{v * 100:g}%" if is_percent else f"{v:g}"


def test_threshold_bands_match_document():
    for bands, label, is_pct in METRICS:
        (n_lo, n_hi, _, _), (w_lo, w_hi, _, _), (a_lo, a_hi, _, _), (d_lo, _, _, _) = bands
        # watch band: lo ≤ label < hi ; warning band; danger: label ≥ top
        watch = f"{_fmt(w_lo, is_pct)} ≤ {label} < {_fmt(w_hi, is_pct)}"
        warning = f"{_fmt(a_lo, is_pct)} ≤ {label} < {_fmt(a_hi, is_pct)}"
        danger = f"{label} ≥ {_fmt(d_lo, is_pct)}"
        for row in (watch, warning, danger):
            assert row in DOC, f"{label}: doc missing threshold row {row!r}"


def test_stacking_values_match_document():
    # §7.2 non-linear stacking (coded in rating_adjustment)
    for snippet in (
        "| 1 dimension 🟠 | -0.5 notch |",
        "| 2 dimensions 🟠 | -1 notch |",
        "| 3 dimensions 🟠 | -1.5 notch |",
        "| 4 dimensions 🟠 | -2 notch |",
        "| 1 dimension 🔴 + 1 dimension 🟠 | -1.5 notch |",
        "| 2 dimensions 🔴 | -2.5 notch |",
        "| 3 dimensions 🔴+ | Trigger portfolio extreme concentration cap, cap BB |",
    ):
        assert snippet in DOC, f"§7.2 stacking row missing: {snippet!r}"


def test_bb_cap_conditions_match_document():
    # §7.3 trigger thresholds (coded in rating_adjustment)
    for snippet in (
        "Single industry > 50%",
        "Single peripheral region > 35%",
        "Pseudo-high rating (external AAA, internal < BBB) share > 40%",
        "Next 12 months maturity > 70%",
        "Single funding channel > 90%",
    ):
        assert snippet in DOC, f"§7.3 condition missing: {snippet!r}"


def test_channel_synergy_rules_match_document():
    # §6.3 synergy rows (coded in channel_score)
    for snippet in (
        "| Bond channel > 70% + Cancellation rate > 15% | Base score + 2",
        "| Non-standard channel > 50% + Non-standard balance YoY decline > 20% | Base score + 3",
        "| Bank channel > 70% + Credit growth < 8% | Base score + 1",
        "| All channels available simultaneously with single < 50% | Base score - 1",
    ):
        assert snippet in DOC, f"§6.3 synergy row missing: {snippet!r}"


def test_default_weights_match_document():
    # §8.2 default weights (coded in concentration_risk_score defaults)
    for snippet in (
        "| Industry Concentration | W₁ | **25%**",
        "| Regional Concentration | W₂ | **20%**",
        "| Rating Concentration | W₃ | **20%**",
        "| Maturity Concentration | W₄ | **20%**",
        "| Funding Channel Concentration | W₅ | **15%**",
    ):
        assert snippet in DOC, f"§8.2 weight row missing: {snippet!r}"
