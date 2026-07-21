"""Tests for the WP-X-05 outlook engine.

Single-source discipline: drift-gate expected values are parsed from documents
at runtime (SS2.2 row counts, SS3.1 row counts, SS5.1 rating rows, SS5.3 industry rows).
Computation-layer tests use fixture signals/triggers.
"""

import re

import pytest

from src.outlook_engine import (
    LAYER_WEIGHTS,
    load_factor_matrix,
    load_migration_table,
    migration_range,
    outlook_assessment,
    watchlist_check,
)
from src.path_sheet import engine_dir

DOC = engine_dir() / "outlook-monitoring-framework.md"


def _text():
    return DOC.read_text(encoding="utf-8")


# ---------------- parsing layer (real document) ----------------

def test_factor_matrix_counts():
    fm = load_factor_matrix(DOC)
    pos = [k for k, v in fm.items() if v[1] == "positive"]
    neg = [k for k, v in fm.items() if v[1] == "negative"]
    text = _text()
    pos_sec = re.search(r"#### Positive Outlook Trigger Signals\n(.*?)(?=\n#### |\Z)", text, re.DOTALL).group(1)
    neg_sec = re.search(r"#### Negative Outlook Trigger Signals\n(.*?)(?=\n### |\Z)", text, re.DOTALL).group(1)
    assert len(pos) == len(re.findall(r"^\|\s*\*\*(?:L[1-4]|External Support)", pos_sec, re.MULTILINE))
    assert len(neg) == len(re.findall(r"^\|\s*\*\*(?:L[1-4]|External Support)", neg_sec, re.MULTILINE))
    assert len(pos) > 0 and len(neg) > 0
    assert all(v[0] in LAYER_WEIGHTS for v in fm.values())


def test_watchlist_trigger_counts_in_doc():
    """SS3.1 trigger table row count drift gate (negative 21 / positive 6, doc truth source)."""
    text = _text()
    neg = re.search(r"#### Negative Watch Trigger Conditions\n(.*?)(?=\n#### |\Z)", text, re.DOTALL).group(1)
    pos = re.search(r"#### Positive Watch Trigger Conditions\n(.*?)(?=\n### |\Z)", text, re.DOTALL).group(1)
    assert len(re.findall(r"^\|\s*\*\*(Event-Driven|Financial Mutation|Policy Shock|Market Signal)\*\*", neg, re.MULTILINE)) == 21
    assert len(re.findall(r"^\|\s*\*\*(Event-Driven|Financial Mutation|Policy Shock|Market Signal)\*\*", pos, re.MULTILINE)) == 6


def test_migration_table_structure():
    table, adj, delegated = load_migration_table(DOC)
    assert {"P5 Financial", "P6 Sovereign-Linked"} <= delegated
    assert len(table) == 12
    for rating in ("AAA", "AA+", "D"):
        assert rating in table
    assert "A / A-" in table and "BBB / BBB-" in table
    for cells in table.values():
        assert all(cells[k] for k in ("upgrade", "maintain", "downgrade", "default"))
    text = _text()
    assert len(adj) == len(re.findall(r"^\|\s*\*\*.+?\*\*\s*\|\s*(?:upgrade|downgrade).*?\+", text, re.MULTILINE | re.IGNORECASE))


# ---------------- outlook scoring (SS2.3) ----------------

def test_outlook_positive():
    r = outlook_assessment([
        {"layer": "L1", "direction": "positive"},
        {"layer": "L2", "direction": "positive"},
        {"layer": "L3", "direction": "negative"},
    ])
    # +1.5 +1.2 -1.0 = +1.7 < 2.0 -> stable (single direction below threshold)
    assert r["outlook"] == "stable"
    assert abs(r["net_score"] - 1.7) < 1e-9


def test_outlook_negative_and_counts():
    r = outlook_assessment([
        {"layer": "L1", "direction": "negative"},
        {"layer": "L4", "direction": "negative"},
        {"layer": "L4", "direction": "positive"},
    ])
    # -1.5 -0.8 +0.8 = -1.5 not reaching -2.0 -> stable
    assert r["outlook"] == "stable"
    assert r["counts"] == {"positive": 1, "negative": 2}
    r2 = outlook_assessment([
        {"layer": "L1", "direction": "negative"},
        {"layer": "External Support", "direction": "negative"},
    ])
    # -1.5 -1.2 = -2.7 <= -2.0 and negative >= 2 -> negative
    assert r2["outlook"] == "negative"


def test_outlook_developing_precedence():
    sigs = [{"layer": "L1", "direction": "positive"}] * 3 + [
        {"layer": "L1", "direction": "negative"}] * 3
    r = outlook_assessment(sigs)
    assert r["outlook"] == "developing"  # positive >= 3 and negative >= 3 and |net| < 2.0


def test_outlook_confidence_tiers():
    high = outlook_assessment(
        [{"layer": "L1", "direction": "positive"},
         {"layer": "L2", "direction": "positive"},
         {"layer": "L3", "direction": "positive"},
         {"layer": "L4", "direction": "positive"}])
    assert high["confidence"] == "high"
    low = outlook_assessment([{"layer": "L1", "direction": "positive"}])
    assert low["confidence"] == "low"
    none = outlook_assessment([])
    assert none["confidence"] == "very low" and none["outlook"] == "stable"


def test_outlook_layer_weights_values():
    assert LAYER_WEIGHTS["L1"] > LAYER_WEIGHTS["L2"] > LAYER_WEIGHTS["L3"] > LAYER_WEIGHTS["L4"]
    # cross-check with doc SS2.3 text
    for layer, w in LAYER_WEIGHTS.items():
        assert f"{layer}={w}" in _text()


# ---------------- watchlist (SS3.1/SS3.2) ----------------

def test_watchlist_negative_priority_and_windows():
    r = watchlist_check([
        {"side": "positive", "event": "group_capital_injection"},
        {"side": "negative", "event": "regulatory_investigation"},
    ])
    assert r["entered"] and r["side"] == "negative watchlist"  # both triggered -> negative priority
    assert r["review"]["initial_review_days"] == 30 and r["review"]["full_review_days"] == 60
    assert r["window_days"] == 90 and r["extension_max_days"] == 60


def test_watchlist_positive_and_empty():
    r = watchlist_check([{"side": "positive", "event": "government_bailout"}])
    assert r["side"] == "positive watchlist" and r["review"]["full_review_days"] == 60
    assert watchlist_check([])["entered"] is False


# ---------------- migration matrix (SS5.1/SS5.3) ----------------

def test_migration_range_base_and_merged():
    r = migration_range("AA+")
    assert set(("upgrade", "maintain", "downgrade", "default", "paradigm_note")) <= set(r)
    a = migration_range("A")
    am = migration_range("A-")
    assert a["upgrade"] == am["upgrade"]  # merged row "A / A-" accepts either child
    with pytest.raises(ValueError, match="[Uu]nknown rating"):
        migration_range("CC")


def test_migration_range_interpolated_ratings():
    # §5.1 has no BB+/BB-/B+/B- rows; those tiers interpolate between the
    # nearest existing rows (midpoint of the two rows' probability ranges).
    bb_plus = migration_range("BB+")
    # midpoint of "BBB / BBB-" (3-5 / 65-70 / 20-30 / 8-10) and "BB" (3-5 / 60 / 25-30 / 10-15)
    assert bb_plus["upgrade"] == "3-5%"
    assert bb_plus["maintain"] == "62.5-65%"
    assert bb_plus["downgrade"] == "22.5-30%"
    assert bb_plus["default"] == "9-12.5%"

    bb_minus = migration_range("BB-")
    # midpoint of "BB" and "B" (<3 / 50-55 / 30-35 / 15-20)
    assert bb_minus["upgrade"] == "1.5-4%"
    assert bb_minus["maintain"] == "55-57.5%"
    assert bb_minus["downgrade"] == "27.5-32.5%"
    assert bb_minus["default"] == "12.5-17.5%"

    b_minus = migration_range("B-")
    # midpoint of "B" and "CCC" (<2 / 30-40 / 30-40 / 30+)
    assert b_minus["maintain"] == "40-47.5%"
    assert b_minus["downgrade"] == "30-37.5%"


def test_migration_range_aaa_upgrade_capped():
    # §2.5: AAA has no upgrade path; paradigm upgrade shifts must not create one.
    base = migration_range("AAA")
    shifted = migration_range("AAA", paradigm="P3 Growth")
    assert base["upgrade"] == "0%"
    assert shifted["upgrade"] == "0%"
    assert "cannot upgrade" in shifted["paradigm_note"]


def test_migration_range_terminal_d_unchanged():
    # D is the terminal state: no migration, paradigm shifts are inert.
    row = migration_range("D", paradigm="P1 Cyclical")
    assert row["default"] == "100%"
    assert row["downgrade"] == "--"
    assert "terminal" in row["paradigm_note"]


def test_migration_range_paradigm_shift():
    base = migration_range("AA")
    shifted = migration_range("AA", paradigm="P1 Cyclical")
    assert shifted["paradigm_note"]
    # base downgrade "10%" -> P1 Cyclical +5-10% -> 15-20%
    assert base["downgrade"] == "10%" and shifted["downgrade"] == "15-20%"
    with pytest.raises(ValueError, match="Unknown industry paradigm"):
        migration_range("AA", paradigm="nonexistent_type")


def test_migration_range_delegated_paradigm():
    # P5 Financial / P6 Sovereign-Linked carry no generic adjustment; the dedicated
    # frameworks govern. The engine returns the base row with a delegation note.
    base = migration_range("AA")
    delegated = migration_range("AA", paradigm="P5 Financial")
    assert delegated["upgrade"] == base["upgrade"]
    assert delegated["downgrade"] == base["downgrade"]
    assert "dedicated framework" in delegated["paradigm_note"]
    delegated6 = migration_range("AA", paradigm="P6 Sovereign-Linked")
    assert delegated6["downgrade"] == base["downgrade"]
    assert "dedicated framework" in delegated6["paradigm_note"]
