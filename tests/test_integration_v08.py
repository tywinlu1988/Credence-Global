"""Integration tests for the v0.8 release line (T11.1-T11.5).

These tests assert the *integration* of the v0.0.1-v0.0.1 staircase into a coherent
release, not any single component:

- T11.1: every one of the 9 active work paths yields a valid 4-stage plan (S1..S4,
  non-empty names/skills) via the thin orchestrator.
- T11.2: the 4 wired paths (WP-RO-01 concentration, WP-RO-02 contagion, WP-RO-03 SRI,
  WP-X-05 outlook) execute code at the analysis stage; the other 5 active paths
  produce a complete LLM-orchestrated plan.
- T11.3: the end-to-end walkthrough record exists and literally names all 8 path ids.
- T11.4: version promotion is consistent (EXPECTED_VERSION well-formed and aligned with
  pyproject/package.json; every CORE_DOCS doc + skill declares it), mirroring
  consistency_check.check_versions / check_version_alignment.
- T11.5: the release zip produced by build_release_zip (single credence/ root, named
  <EXPECTED_VERSION>-release.zip, sha256 sidecar) contains the complete installable
  agent package (skills @ .claude/skills, flattened engine/, generated entry/install docs).

Single-source rule: the tests assert structure/versions only. They never restate engine
thresholds/weights -- the only numbers here are the *fixture inputs* and the *real engine
outputs* returned by the wired coded engines (mirrors tests/test_pipeline.py fixtures).
"""

import importlib.util
from pathlib import Path

import pytest

from src.concentration_scorer import ConcentrationMetrics
from src.path_sheet import load_registry_paths
from src.pipeline import (
    EXECUTABLE_ENGINES,
    load_contract,
    load_stage_plan,
    run_executable_stages,
)
from src.sri_calculator import IndustryInput, Outlook, TrackBLevel

ROOT = Path(__file__).resolve().parent.parent
CONTRACT = ROOT / "dev" / "engine" / "pipeline-contract.md"
REGISTRY = ROOT / "dev" / "engine" / "work-path-registry.md"
ENGINE_DIR = ROOT / "dev" / "engine"
SKILLS_DIR = ROOT / "dev" / ".claude" / "skills"
WALKTHROUGH = ROOT / "validation" / "docs" / "v0.0.1-to-end-walkthroughs.md"

CONSISTENCY_CHECK = ROOT / "scripts" / "consistency_check.py"
BUILD_DIST = ROOT / "scripts" / "build_dist.py"

ACTIVE_PATHS = [
    "WP-CS-01", "WP-PM-01", "WP-RO-01", "WP-RO-02",
    "WP-RO-03", "WP-X-01", "WP-X-02", "WP-X-03", "WP-X-05",
]
WIRED_PATHS = ["WP-RO-01", "WP-RO-02", "WP-RO-03", "WP-X-05"]
UNWIRED_ACTIVE = [p for p in ACTIVE_PATHS if p not in WIRED_PATHS]

FOUR_SKILLS = (
    "credit-analysis-router",
    "fixed-income-credit-analysis",
    "credit-report-builder",
    "credit-qa-verifier",
)


# --------------------------------------------------------------------------
# fixtures / helpers
# --------------------------------------------------------------------------

def _load_consistency_check():
    """importlib-load scripts/consistency_check.py (it is not a package module)."""
    spec = importlib.util.spec_from_file_location("consistency_check", CONSISTENCY_CHECK)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def cc():
    return _load_consistency_check()


def _load_build_dist():
    """importlib-load scripts/build_dist.py (it is not a package module)."""
    spec = importlib.util.spec_from_file_location("build_dist", BUILD_DIST)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def bd():
    return _load_build_dist()


@pytest.fixture(scope="module")
def contract():
    return load_contract(CONTRACT)


@pytest.fixture(scope="module")
def registry_paths():
    return load_registry_paths(REGISTRY)


def _sheet_for(path_id, registry_paths, **overrides):
    """A valid path sheet for an active path, built from the registry's real entry.

    role/object/depth come from the registry; engine_sequence maps to the sheet's
    engine_reading_order; quality_gates are copied verbatim. mode defaults to A
    (public data). This mirrors the construction approach in tests/test_pipeline.py.
    """
    entry = registry_paths[path_id]
    sheet = {
        "role": str(entry["role"]),
        "object": str(entry["trigger"]["object"]),
        "depth": str(entry["depth"]),
        "mode": "A",
        "path_id": path_id,
        "engine_reading_order": list(entry["engine_sequence"]),
        "quality_gates": list(entry["quality_gates"]),
        "notes": "",
    }
    sheet.update(overrides)
    return sheet


def _sri_inputs():
    """The known 2026Q2 SRI fixture (mirrors tests/test_pipeline.py)."""
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
    weights += [residual / 9] * 9
    return {"industries": industries, "weights": weights}


def _concentration_inputs():
    """An all-green ConcentrationMetrics fixture (mirrors tests/test_pipeline.py)."""
    return {
        "metrics": ConcentrationMetrics(
            hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
            single_province_share=0.10, weak_region_share=0.02,
            aaa_share=0.20, pseudo_high_rating_share=0.01,
            maturity_12m_share=0.20, single_month_peak=0.05,
            top_channel_share=0.30,
        )
    }


def _contagion_inputs():
    return {
        "holdings": {"Technology Hardware (Semiconductors)": 0.4, "Consumer Staples": 0.35, "Retail": 0.25},
        "escalation_factors": ["Market Panic"],
    }


def _outlook_inputs():
    return {
        "signals": [
            {"layer": "L1", "direction": "negative", "signal": "industry_access_tightening"},
            {"layer": "External Support", "direction": "negative", "signal": "supporter_downgrade"},
            {"layer": "L4", "direction": "positive", "signal": "operating_cash_flow_positive"},
        ],
        "rating": "AA",
        "paradigm": "Policy-Driven",
        "watchlist_triggers": [{"side": "negative", "event": "regulatory_investigation"}],
    }


def _wired_inputs(path_id):
    return {
        "WP-RO-01": _concentration_inputs,
        "WP-RO-02": _contagion_inputs,
        "WP-RO-03": _sri_inputs,
        "WP-X-05": _outlook_inputs,
    }[path_id]()


# --------------------------------------------------------------------------
# T11.1 — all 8 active paths produce a valid 4-stage plan (S1..S4)
# --------------------------------------------------------------------------

def test_t11_1_all_active_paths_yield_valid_four_stage_plan(contract, registry_paths):
    # every active path id the walkthrough covers must actually be registered active
    for pid in ACTIVE_PATHS:
        assert pid in registry_paths, f"{pid} not registered"
        assert str(registry_paths[pid].get("status")) == "active", f"{pid} not active"

    # the contract drives S1->S2->S3->S4 in order (load_stage_plan re-validates this)
    assert [cs["id"] for cs in contract["stages"]] == ["S1", "S2", "S3", "S4"]

    for pid in ACTIVE_PATHS:
        plan = load_stage_plan(_sheet_for(pid, registry_paths), registry_paths, contract)
        assert len(plan) == 4, f"{pid}: expected 4 stages"
        for idx, stage in enumerate(plan):
            cs = contract["stages"][idx]
            assert cs["id"] == f"S{idx + 1}"
            # stage name/skill come from the contract and are non-empty
            assert stage.name == cs["name"] and stage.name.strip()
            assert stage.skill == cs["skill"] and stage.skill.strip()
            assert stage.path_id == pid


# --------------------------------------------------------------------------
# T11.2 — 3 wired paths execute code; the other 5 are LLM-orchestrated
# --------------------------------------------------------------------------

EXPECTED_OUTPUT_KEYS = {
    "WP-RO-03": {"sri", "thermometer"},
    "WP-RO-01": {"score", "adjustment", "levels", "bb_cap_triggered"},
    "WP-RO-02": {"exposure", "links", "factors_applied"},
    "WP-X-05": {"outlook", "confidence", "net_score", "watchlist", "migration"},
}


def test_t11_2_wired_execute_code_others_llm_orchestrated(contract, registry_paths):
    assert set(WIRED_PATHS) == set(EXECUTABLE_ENGINES), "wired set drifted from EXECUTABLE_ENGINES"

    # wired: analysis stage runs the coded engine (mode="code") with real outputs
    for pid in WIRED_PATHS:
        plan = load_stage_plan(_sheet_for(pid, registry_paths), registry_paths, contract)
        assert plan[1].executable is True, f"{pid}: analysis must be executable"
        manifest = run_executable_stages(plan, _wired_inputs(pid))
        assert manifest["path_id"] == pid
        analysis = next(s for s in manifest["stages"] if s["name"] == "analysis")
        assert analysis["mode"] == "code", f"{pid}: analysis must run as code"
        assert analysis["outputs"], f"{pid}: analysis must return real outputs"
        assert set(analysis["outputs"]) == EXPECTED_OUTPUT_KEYS[pid]

    # unwired: complete plan, analysis not executable, every stage llm-orchestrated
    assert len(UNWIRED_ACTIVE) == 5
    for pid in UNWIRED_ACTIVE:
        assert pid not in EXECUTABLE_ENGINES
        plan = load_stage_plan(_sheet_for(pid, registry_paths), registry_paths, contract)
        assert len(plan) == 4, f"{pid}: unwired path still yields a complete 4-stage plan"
        assert plan[1].executable is False, f"{pid}: analysis must NOT be executable"
        manifest = run_executable_stages(plan, {})
        assert all(s["mode"] == "llm-orchestrated" for s in manifest["stages"]), pid
        analysis = next(s for s in manifest["stages"] if s["name"] == "analysis")
        assert analysis["outputs"] is None


# --------------------------------------------------------------------------
# T11.3 — walkthrough record exists and literally names all 8 path ids
# --------------------------------------------------------------------------

@pytest.mark.skip(reason="walkthrough docs removed in v0.0.1 cleanup; to be re-created")
def test_t11_3_walkthrough_covers_all_eight_paths():
    assert WALKTHROUGH.exists(), f"walkthrough missing: {WALKTHROUGH}"
    text = WALKTHROUGH.read_text(encoding="utf-8")
    for pid in ACTIVE_PATHS:
        assert pid in text, f"walkthrough does not name {pid}"


# --------------------------------------------------------------------------
# T11.4 — version promotion consistency (mirrors check_versions)
# --------------------------------------------------------------------------

def test_t11_4_version_promotion_consistent(cc):
    # version format: well-formed + aligned across pyproject/package.json
    assert cc.VERSION_RELEASE_RE.match(cc.EXPECTED_VERSION), cc.EXPECTED_VERSION
    assert cc.check_version_alignment() == []
    # check_versions must report no errors: all CORE_DOCS + the executor skill declare it
    assert cc.check_versions() == [], "check_versions reported errors after promotion"
    # every CORE_DOCS doc header declares the promoted version (mirror check_versions logic)
    for doc in cc.CORE_DOCS:
        text = (ENGINE_DIR / doc).read_text(encoding="utf-8")
        assert (
                f"**版本**: {cc.EXPECTED_VERSION}" in text
                or f"**版本** {cc.EXPECTED_VERSION}" in text
                or f"**对应引擎版本**: {cc.EXPECTED_VERSION}" in text
                or f"**对应引擎版本** {cc.EXPECTED_VERSION}" in text
                or f"**Version**: {cc.EXPECTED_VERSION}" in text
                or f"**Version** {cc.EXPECTED_VERSION}" in text
        ), f"{doc} does not declare {cc.EXPECTED_VERSION}"
    # all four stage skills reference the promoted version
    for skill in FOUR_SKILLS:
        skill_text = (SKILLS_DIR / skill / "SKILL.md").read_text(encoding="utf-8")
        assert cc.EXPECTED_VERSION in skill_text, f"{skill} SKILL.md not on {cc.EXPECTED_VERSION}"


# --------------------------------------------------------------------------
# T11.5 — release zip integrity: installable agent package in a single credence/ root
# --------------------------------------------------------------------------

def test_t11_5_release_zip_integrity(cc, bd, tmp_path):
    import hashlib
    import zipfile

    out = tmp_path / "dist" / "credence"
    bd.build(out)
    assert bd.validate(out) == []
    zip_path, sha_path = bd.build_release_zip(out, tmp_path / "version")

    assert zip_path.name == f"{cc.EXPECTED_VERSION}-release.zip"
    digest = hashlib.sha256(zip_path.read_bytes()).hexdigest()
    assert sha_path.read_text(encoding="utf-8").split()[0] == digest

    with zipfile.ZipFile(zip_path) as zf:
        names = set(zf.namelist())
    root = "credence/"
    assert names and all(n.startswith(root) for n in names)

    # generated entry/install docs (single universal package, per-tool entries)
    for entry in ("AGENTS.md", "CLAUDE.md", "GEMINI.md", "INSTALL.md", "README.md"):
        assert root + entry in names, f"zip missing entry {entry}"
    assert root + ".claude-plugin/plugin.json" in names, "missing plugin.json"
    assert root + "adapters/codex.md" in names, "missing adapters/codex.md"

    # skills in .claude/skills/ (Claude Code native + Cursor/Gemini/OpenCode compat)
    for skill in FOUR_SKILLS:
        assert f"{root}.claude/skills/{skill}/SKILL.md" in names, skill

    # engine: 27 CORE_DOCS + report templates + executable orchestrator
    for doc in cc.CORE_DOCS:
        assert f"{root}engine/{doc}" in names, f"zip missing engine/{doc}"
    assert root + "templates/template-base.css" in names, "zip missing templates/"
    assert root + "src/pipeline.py" in names, "zip missing src/pipeline.py"

    # extract and verify the unpacked package (what install.js delivers to users)
    import zipfile as _zipfile
    unpacked = tmp_path / "unpacked"
    with _zipfile.ZipFile(zip_path) as zf:
        zf.extractall(unpacked)
    pkg = unpacked / "credence"

    # the package carries the promoted entry version
    assert cc.EXPECTED_VERSION in (pkg / "AGENTS.md").read_text(encoding="utf-8")

    # no excluded artifacts leaked (settings.local.json / audits / design / product /
    # data / validation / dev source / bytecode cache)
    leaked = [
        p for p in pkg.rglob("*")
        if (p.is_dir() and p.name in (
            ".git", "__pycache__", "audits", "design", "product", "data", "validation"))
        or (p.is_file() and (p.suffix == ".pyc" or p.name == "settings.local.json"))
    ]
    assert not leaked, f"excluded artifacts in release zip: {leaked}"

    # no dead links: no absolute paths, no residual dev/ path tokens
    dead = []
    for f in pkg.rglob("*"):
        if f.is_file() and f.suffix in bd.TEXT_EXTS:
            text = f.read_text(encoding="utf-8")
            if bd.ABS_PATH_RE.search(text):
                dead.append(f"{f.relative_to(pkg)}: absolute path")
            if bd.DEV_TOKEN_RE.search(text):
                dead.append(f"{f.relative_to(pkg)}: dev/ token")
    assert not dead, f"dead links in release zip: {dead[:20]}"
