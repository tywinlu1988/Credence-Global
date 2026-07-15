"""Regression tests for cross-document coherence of the v0.7.0-alpha engine."""

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
ENGINE_DIR = ROOT / "dev" / "engine"
SKILL_FILE = ROOT / "dev" / ".claude" / "skills" / "fixed-income-credit-analysis" / "SKILL.md"

# Authoritative 12-notch rating map from dual-track-methodology.md §六.
# Each tuple is (low_score, high_score, rating_label).
CANONICAL_RATING_INTERVALS = [
    (9.5, 10.0, "AAA"),
    (9.0, 9.4, "AA+"),
    (8.5, 8.9, "AA"),
    (8.0, 8.4, "AA-"),
    (7.5, 7.9, "A+"),
    (7.0, 7.4, "A"),
    (6.5, 6.9, "A-"),
    (6.0, 6.4, "BBB+"),
    (5.5, 5.9, "BBB"),
    (5.0, 5.4, "BBB-"),
    (4.5, 4.9, "BB+"),
    (4.0, 4.4, "BB"),
    (3.5, 3.9, "BB-"),
    (3.0, 3.4, "B+"),
    (2.5, 2.9, "B"),
    (2.0, 2.4, "B-"),
    (1.0, 1.9, "CCC"),
    (0.0, 0.9, "D"),
]

RATING_INTERVAL_RE = re.compile(
    r"\|\s*(\d+(?:\.\d+)?)\s*[-–—]\s*(\d+(?:\.\d+)?)\s*\|\s*([A-D]{1,3}[+-]?)\s*\|"
)


def _read_engine_doc(name: str) -> str:
    return (ENGINE_DIR / name).read_text(encoding="utf-8")


def _parse_rating_table(text: str, start_marker: str, end_marker: str | None = None) -> list[tuple[float, float, str]]:
    """Extract score-range -> rating rows from a Markdown table section."""
    start = text.find(start_marker)
    if start == -1:
        return []
    section = text[start:]
    if end_marker:
        end = section.find(end_marker, len(start_marker))
        if end != -1:
            section = section[:end]

    intervals = []
    for match in RATING_INTERVAL_RE.finditer(section):
        low = float(match.group(1))
        high = float(match.group(2))
        label = match.group(3)
        intervals.append((low, high, label))
    return intervals


def test_rating_map_consistency_in_systemic_warning_framework():
    """The SRI input table must use the same canonical 12-notch map as the rest of the engine."""
    text = _read_engine_doc("systemic-warning-framework.md")
    intervals = _parse_rating_table(
        text,
        start_marker="**信号A：轨道A行业评分**",
        end_marker="**信号B：轨道B市场信号**",
    )
    assert intervals, "No rating intervals parsed from systemic-warning-framework.md"
    assert intervals == CANONICAL_RATING_INTERVALS, (
        f"Rating intervals in systemic-warning-framework.md do not match the canonical map.\n"
        f"Expected: {CANONICAL_RATING_INTERVALS}\n"
        f"Found: {intervals}"
    )


def test_issuer_survival_veto_ceiling_is_ccc():
    """Every document defining one-shot veto must cap the issuer rating at CCC."""
    docs = ["dual-track-methodology.md", "industry-framework.md", "governance-fraud-risk.md"]
    for doc in docs:
        text = _read_engine_doc(doc)
        assert "一票否决" in text, f"{doc} no longer mentions one-shot veto (一票否决)"
        assert "上限锁定为CCC" in text, (
            f"{doc} does not state the CCC ceiling for veto (上限锁定为CCC)"
        )


def test_thermometer_thresholds_consistent():
    """The SRI thermometer thresholds must be stable across engine and skill docs."""
    engine_text = _read_engine_doc("systemic-warning-framework.md")
    skill_text = SKILL_FILE.read_text(encoding="utf-8")

    # Engine §3.1 explicit band boundaries.
    assert "SRI < 0.5" in engine_text
    assert "0.5 ≤ SRI < 1.0" in engine_text
    assert "1.0 ≤ SRI < 1.8" in engine_text
    assert "SRI ≥ 1.8" in engine_text

    # Skill summary uses the same numeric cutoffs.
    assert "<0.5" in skill_text
    assert "0.5–1.0" in skill_text
    assert "1.0–1.8" in skill_text
    assert "≥1.8" in skill_text


def test_thermometer_full_band_definitions_present():
    """Explicit band boundaries must exist in the engine thermometer definition."""
    text = _read_engine_doc("systemic-warning-framework.md")
    assert "SRI < 0.5" in text
    assert "0.5 ≤ SRI < 1.0" in text
    assert "1.0 ≤ SRI < 1.8" in text
    assert "SRI ≥ 1.8" in text


def test_skill_has_no_validation_result_sections():
    """Validation results are test evidence, not skill documentation.

    The skill documents engine capabilities. Validation outcome tables and case
    lists are archived in the root-level ``validation/`` directory and must not
    reappear as skill content.
    """
    skill = SKILL_FILE.read_text(encoding="utf-8")
    assert "## Validated Industries & Cases" not in skill, (
        "Skill lists validated industries/cases; these belong to validation/, not the skill"
    )
    assert "## Black-Swan Retrospective Validation" not in skill, (
        "Skill documents black-swan retrospective results; these belong to validation/, not the skill"
    )
    assert "Forward Test" not in skill, (
        "Skill contains a 'Forward Test' validation table header"
    )
    assert "Retrospective Test" not in skill, (
        "Skill contains a 'Retrospective Test' validation table header"
    )


def test_skill_md_slimmed_and_retains_mandatory_guardrails():
    """T4.2: SKILL.md is slimmed to <=150 lines while retaining the three mandatory
    guardrails (Mandatory Density Rules / Mode B / one-shot veto)."""
    skill = SKILL_FILE.read_text(encoding="utf-8")
    line_count = len(skill.splitlines())
    assert line_count <= 150, (
        f"SKILL.md is {line_count} lines; must be <=150 after the navigator slim-down"
    )
    for keyword in ["Mandatory Density Rules", "Mode B", "一票否决"]:
        assert keyword in skill, f"SKILL.md lost mandatory guardrail keyword: {keyword}"


def test_invocation_protocol_is_path_sheet_driven():
    """T4.3: the Invocation Protocol consumes the router's work-path sheet
    (engine_reading_order) instead of a hardcoded fixed document list as its sole entry."""
    skill = SKILL_FILE.read_text(encoding="utf-8")
    assert "engine_reading_order" in skill, (
        "Invocation Protocol must read per the path sheet's engine_reading_order"
    )
    assert "credit-analysis-router" in skill, (
        "Invocation Protocol must reference the router skill for path-sheet handoff"
    )
    assert "Read the canonical engine documents in this order" not in skill, (
        "Invocation Protocol still uses the fixed canonical-document list as its entry"
    )


def test_lgv_framework_renamed_to_lgfv():
    """T4.4: LGV is unified to LGFV — the framework file is renamed and no current
    doc references the retired filename."""
    retired = "lgv" + "-framework.md"  # split so the repo-wide residual grep stays clean
    assert (ENGINE_DIR / "lgfv-framework.md").exists(), (
        "dev/engine/lgfv-framework.md must exist"
    )
    assert not (ENGINE_DIR / retired).exists(), (
        f"dev/engine/{retired} must be renamed away"
    )
    for path in [SKILL_FILE, ENGINE_DIR / "engine-overview.md"]:
        text = path.read_text(encoding="utf-8")
        assert retired not in text, f"{path.name} still references {retired}"
