"""Tests for the v0.7.8 executable orchestrator (src/pipeline.py).

T9.1-T9.7 cover the thin orchestrator: stage-plan construction from the contract doc,
end-to-end execution of the two wired coded engines (WP-M4-03 SRI, WP-M4-01 concentration),
graceful LLM-orchestrated skipping for unwired paths, planned-path 待开发 notices,
contract-sourced stage names, and invalid-sheet rejection. Deliverable 3 (chaining-edge
endpoint referential integrity) is also covered here.
"""

from pathlib import Path

import pytest

from src.concentration_scorer import ConcentrationMetrics
from src.path_sheet import load_registry_paths
from src.pipeline import (
    EXECUTABLE_ENGINES,
    load_contract,
    load_stage_plan,
    planned_path_notice,
    run_executable_stages,
)
from src.sri_calculator import IndustryInput, Outlook, TrackBLevel

ROOT = Path(__file__).resolve().parent.parent
CONTRACT = ROOT / "dev" / "engine" / "pipeline-contract.md"
REGISTRY = ROOT / "dev" / "engine" / "work-path-registry.md"


# --------------------------------------------------------------------------
# fixtures
# --------------------------------------------------------------------------

@pytest.fixture(scope="module")
def contract():
    return load_contract(CONTRACT)


@pytest.fixture(scope="module")
def registry_paths():
    return load_registry_paths(REGISTRY)


def _sheet(path_id, **overrides) -> dict:
    """A valid sheet for an M4 wired path; overridable per-test."""
    base = {
        "WP-M4-03": {
            "role": "M4",
            "object": "market",
            "depth": "专项",
            "mode": "A",
            "path_id": "WP-M4-03",
            "engine_reading_order": ["dev/engine/systemic-warning-framework.md"],
            "quality_gates": ["温度计四级 (dev/engine/systemic-warning-framework.md §三)"],
            "notes": "",
        },
        "WP-M4-01": {
            "role": "M4",
            "object": "portfolio",
            "depth": "专项",
            "mode": "A",
            "path_id": "WP-M4-01",
            "engine_reading_order": ["dev/engine/concentration-framework.md"],
            "quality_gates": ["五维集中度 (dev/engine/concentration-framework.md §一)"],
            "notes": "",
        },
        "WP-M0-01": {
            "role": "M0",
            "object": "single-issuer",
            "depth": "L2",
            "mode": "A",
            "path_id": "WP-M0-01",
            "engine_reading_order": ["dev/engine/industry-framework.md"],
            "quality_gates": ["一票否决 (dev/engine/industry-framework.md §五)"],
            "notes": "",
        },
        "WP-M2-01": {
            "role": "M2",
            "object": "single-issuer",
            "depth": "专项",
            "mode": "A",
            "path_id": "WP-M2-01",
            "engine_reading_order": [],
            "quality_gates": [],
            "notes": "",
        },
    }[path_id]
    base.update(overrides)
    return base


def _sri_2026q2_inputs() -> dict:
    """The known 2026Q2 SRI fixture (mirrors test_sri_matches_2026q2_example)."""
    industries = [
        IndustryInput("LGV", 5.25, TrackBLevel.YELLOW, Outlook.STABLE),
        IndustryInput("PV", 5.0, TrackBLevel.YELLOW, Outlook.NEGATIVE),
        IndustryInput("NEV", 5.5, TrackBLevel.YELLOW, Outlook.NEGATIVE),
        IndustryInput("Retail", 5.5, TrackBLevel.YELLOW, Outlook.NEGATIVE),
    ] + [
        IndustryInput(f"other_{i}", 7.0, TrackBLevel.GREEN, Outlook.STABLE)
        for i in range(9)
    ]
    weights = [0.25, 0.0233, 0.0222, 0.04]
    residual = 1.0 - sum(weights)
    valid_weights = weights + [residual / 9] * 9
    return {"industries": industries, "weights": valid_weights}


def _concentration_inputs() -> dict:
    """An all-green ConcentrationMetrics fixture (low concentration)."""
    return {
        "metrics": ConcentrationMetrics(
            hhi=500,
            cr3=0.30,
            cr5=0.50,
            max1=0.15,
            single_province_share=0.10,
            weak_region_share=0.02,
            aaa_share=0.20,
            pseudo_high_rating_share=0.01,
            maturity_12m_share=0.20,
            single_month_peak=0.05,
            top_channel_share=0.30,
        )
    }


# --------------------------------------------------------------------------
# T9.1 — WP-M4-03 yields 4 ordered stages; analysis is executable
# --------------------------------------------------------------------------

def test_t9_1_stage_plan_order_and_executable(contract, registry_paths):
    plan = load_stage_plan(_sheet("WP-M4-03"), registry_paths, contract)
    assert [s.name for s in plan] == ["intake", "analysis", "report", "qa"]
    analysis = plan[1]
    assert analysis.executable is True
    # the other three stages are never executable
    assert all(not s.executable for s in (plan[0], plan[2], plan[3]))
    # analysis reads the sheet's engine_reading_order
    assert analysis.inputs == ["dev/engine/systemic-warning-framework.md"]


# --------------------------------------------------------------------------
# T9.2 — SRI stage runs end-to-end against the 2026Q2 fixture
# --------------------------------------------------------------------------

def test_t9_2_sri_end_to_end_matches_2026q2(contract, registry_paths):
    plan = load_stage_plan(_sheet("WP-M4-03"), registry_paths, contract)
    manifest = run_executable_stages(plan, _sri_2026q2_inputs())
    assert manifest["path_id"] == "WP-M4-03"
    analysis = next(s for s in manifest["stages"] if s["name"] == "analysis")
    assert analysis["mode"] == "code"
    sri_value = analysis["outputs"]["sri"]
    assert 0.54 <= sri_value <= 0.60
    assert analysis["outputs"]["thermometer"] == "watch"


# --------------------------------------------------------------------------
# T9.3 — WP-M4-01 wired: concentration score + rating_adjustment
# --------------------------------------------------------------------------

def test_t9_3_concentration_wired(contract, registry_paths):
    plan = load_stage_plan(_sheet("WP-M4-01"), registry_paths, contract)
    assert plan[1].executable is True
    manifest = run_executable_stages(plan, _concentration_inputs())
    analysis = next(s for s in manifest["stages"] if s["name"] == "analysis")
    assert analysis["mode"] == "code"
    out = analysis["outputs"]
    assert out["score"] <= 4.0  # all-green fixture → low concentration
    assert out["adjustment"] == 0.0
    assert out["bb_cap_triggered"] is False
    assert set(out["levels"]) == {"industry", "region", "rating", "maturity", "channel"}


# --------------------------------------------------------------------------
# T9.4 — unwired path (WP-M0-01): analysis not executable, graceful skip
# --------------------------------------------------------------------------

def test_t9_4_unwired_path_skips_gracefully(contract, registry_paths):
    assert "WP-M0-01" not in EXECUTABLE_ENGINES
    plan = load_stage_plan(_sheet("WP-M0-01"), registry_paths, contract)
    assert plan[1].executable is False
    manifest = run_executable_stages(plan, {})
    analysis = next(s for s in manifest["stages"] if s["name"] == "analysis")
    assert analysis["mode"] == "llm-orchestrated"
    assert analysis["outputs"] is None
    # every stage of an unwired path is LLM-orchestrated
    assert all(s["mode"] == "llm-orchestrated" for s in manifest["stages"])


# --------------------------------------------------------------------------
# T9.5 — planned path (WP-M2-01): 待开发 notice, no execution
# --------------------------------------------------------------------------

def test_t9_5_planned_path_notice(registry_paths):
    notice = planned_path_notice(_sheet("WP-M2-01"), registry_paths)
    assert notice is not None
    assert "待开发" in notice
    assert "WP-M2-01" in notice
    # an active path yields no notice
    assert planned_path_notice(_sheet("WP-M4-03"), registry_paths) is None


# --------------------------------------------------------------------------
# T9.6 — stage names come from the contract doc, not hardcoded
# --------------------------------------------------------------------------

def test_t9_6_stage_names_sourced_from_contract(tmp_path, registry_paths):
    renamed = tmp_path / "contract.md"
    renamed.write_text(
        "# contract fixture\n\n"
        "| 阶段 | 产物 | 承载 skill | 上游 | 下游 |\n"
        "|---|---|---|---|---|\n"
        "| S1 ingest | 工作路径单 | `credit-analysis-router` | — | S2 |\n"
        "| S2 deep-analysis | 分析产物 | `fixed-income-credit-analysis` | S1 | S3 |\n"
        "| S3 render | 交付单 | `credit-report-builder` | S2 | S4 |\n"
        "| S4 verify | 质检裁决 | `credit-qa-verifier` | S1+S2+S3 | — |\n",
        encoding="utf-8",
    )
    renamed_contract = load_contract(renamed)
    plan = load_stage_plan(_sheet("WP-M4-03"), registry_paths, renamed_contract)
    # names reflect the renamed contract, not hardcoded intake/analysis/report/qa
    assert [s.name for s in plan] == ["ingest", "deep-analysis", "render", "verify"]
    # ... while positional chain semantics are preserved (analysis still executable)
    assert plan[1].executable is True


# --------------------------------------------------------------------------
# T9.7 — invalid sheet rejected via validate_path_sheet
# --------------------------------------------------------------------------

def test_t9_7_invalid_sheet_rejected(contract, registry_paths):
    # illegal enum value
    with pytest.raises(ValueError):
        load_stage_plan(_sheet("WP-M4-03", mode="C"), registry_paths, contract)
    # unknown path_id
    bad = _sheet("WP-M4-03")
    bad["path_id"] = "WP-M9-99"
    with pytest.raises(ValueError):
        load_stage_plan(bad, registry_paths, contract)


# --------------------------------------------------------------------------
# Deliverable 3 — chaining-edge endpoint referential integrity (v0.7.7 carryover)
# --------------------------------------------------------------------------

def test_chaining_edge_endpoints_resolve(contract, registry_paths):
    edges = contract["chaining_edges"]
    assert edges, "contract must define chaining_edges"
    for edge in edges:
        # every `from` endpoint resolves to a registered path_id
        assert edge["from"] in registry_paths, f"{edge['id']}: unknown from {edge['from']}"
        to = edge.get("to") or []
        if not to:
            # open set: must carry a to_ref pointer instead of enumerated ids
            assert edge.get("to_ref"), f"{edge['id']}: open `to` set missing to_ref"
            continue
        # every enumerated `to` endpoint resolves to a registered path_id
        for target in to:
            assert target in registry_paths, f"{edge['id']}: unknown to {target}"
