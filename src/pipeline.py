"""Four-stage chain executable orchestrator (v0.7.8 — executable orchestrator + wired engines).

This module is a **thin orchestrator** for the four-stage chain (intake -> analysis -> report -> qa).
It parses the path sheet produced by the router into an ordered stage plan, and invokes the
corresponding **coded engine** only when the path is wired; remaining paths/stages are gracefully
left for the LLM to orchestrate via engine documentation.

Design constraints (single source of truth):

- **Stage definitions are not hardcoded**: the four stage names, hosting skills, and artifact labels
  are all parsed from the stage overview table in `dev/engine/pipeline-contract.md`
  (see load_contract). Chaining edges are likewise read from that contract's yaml block for
  endpoint cross-reference integrity validation.
- **No new engine coding**: engine documentation is the normative source; `src/sri_calculator.py`,
  `src/concentration_scorer.py`, `src/contagion_engine.py` and `src/outlook_engine.py` are its
  **executable implementations**. The orchestrator only calls them when the path is wired
  (EXECUTABLE_ENGINES) and does not duplicate any threshold/weight/level semantics.
- **Reuses path_sheet.py**: path sheet validation, registry parsing, planned-path determination,
  and "under development" notices all reuse `src/path_sheet.py` without reimplementation.
"""

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from src.concentration_scorer import concentration_risk_score, rating_adjustment
from src.contagion_engine import (
    apply_escalation,
    high_intensity_links,
    load_matrix,
    portfolio_exposure,
)
from src.outlook_engine import (
    migration_range,
    outlook_assessment,
    watchlist_check,
)
from src.path_sheet import (
    YAML_BLOCK_RE,
    is_planned,
    sheet_notice,
    validate_path_sheet,
)
from src.sri_calculator import sri, thermometer_level

ROOT = Path(__file__).resolve().parent.parent

# Data row from the contract stage overview table: ``| S1 intake | Path Sheet | `credit-analysis-router` | ... |``.
# The name (intake/analysis/...) and hosting skill are parsed from this row; stage names are never hardcoded here.
_STAGE_ROW_RE = re.compile(
    r"^\|\s*(S\d+)\s+([A-Za-z][A-Za-z0-9_-]*)\s*\|([^|]*)\|\s*`?([A-Za-z0-9_-]+)`?\s*\|",
    re.MULTILINE,
)

# Positional semantics of the four-stage chain: the intake/analysis/report/qa order is the fixed
# topology of the chain contract (S1->S2->S3->S4). What a stage *does* is assigned by position;
# what a stage *is called / who hosts it* comes from the contract document, so renaming a stage
# in the contract is reflected in the plan while chain semantics remain unchanged.
_INTAKE, _ANALYSIS, _REPORT, _QA = 0, 1, 2, 3


@dataclass
class Stage:
    """One stage in the four-stage chain.

    ``name``/``skill`` come from the contract stage overview table; ``inputs``/``outputs`` are
    resolved from the path sheet and registry by positional semantics; ``executable`` is True
    only when the position is analysis and the path has a wired coded engine.
    """

    name: str
    skill: str
    inputs: list = field(default_factory=list)
    outputs: list = field(default_factory=list)
    executable: bool = False
    path_id: str = ""

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "skill": self.skill,
            "inputs": list(self.inputs),
            "outputs": list(self.outputs),
            "executable": self.executable,
            "path_id": self.path_id,
        }


def load_contract(contract_md_path) -> dict:
    """Parse pipeline-contract.md and return stage definitions, artifact schemas, and chaining edges.

    Returns ``{"stages": [...], "artifacts": [...], "chaining_edges": [...]}``:

    - ``stages``: ordered list ``[{"id","name","skill","artifact"}]`` parsed from the stage
      overview table, in S1->S2->S3->S4 order. The **sole source** of stage name/skill;
      the orchestrator names stages from this data.
    - ``artifacts``: 4 artifact schemas (yaml blocks containing ``path_id``) from section 2,
      in document order.
    - ``chaining_edges``: edge list (``id/from/to/trigger/...``) parsed from the chaining-edges
      yaml block in section 3.
    """
    text = Path(contract_md_path).read_text(encoding="utf-8")

    stages = [
        {
            "id": m.group(1),
            "name": m.group(2),
            "artifact": m.group(3).strip(),
            "skill": m.group(4),
        }
        for m in _STAGE_ROW_RE.finditer(text)
    ]

    artifacts: list[dict] = []
    chaining_edges: list[dict] = []

    for block in YAML_BLOCK_RE.findall(text):
        data = yaml.safe_load(block)
        if not isinstance(data, dict):
            continue
        if "chaining_edges" in data:
            chaining_edges = list(data.get("chaining_edges") or [])
        elif "path_id" in data:
            artifacts.append(data)

    return {"stages": stages, "artifacts": artifacts, "chaining_edges": chaining_edges}


def load_stage_plan(path_sheet: dict, registry_paths: dict, contract: dict) -> list[Stage]:
    """Parse a path sheet into an ordered four-stage plan.

    First validates the path sheet via `validate_path_sheet` (invalid enums / unknown path_id /
    dangling templates -> ValueError); then emits four stages by contract stage overview (positional):
    intake (path sheet itself), analysis (engine docs, ``executable=True`` only when the path has a
    wired coded engine), report (registry templates), qa (quality gates).
    Stage names and hosting skills come from ``contract["stages"]``, not hardcoded here.
    """
    errors = validate_path_sheet(path_sheet, registry_paths)
    if errors:
        raise ValueError("invalid path sheet: " + "; ".join(errors))

    pid = str(path_sheet.get("path_id", "")).strip()
    registry_path = registry_paths.get(pid, {})

    contract_stages = contract.get("stages", [])
    if len(contract_stages) != 4:
        raise ValueError(
            f"contract must define exactly 4 stages, got {len(contract_stages)}"
        )
    # Positional semantics depend on the fixed S1->S2->S3->S4 topology. If the contract
    # reorders or mislabels stages, this loudly fails rather than silently misassigning
    # executable semantics to the wrong stage (review #1).
    stage_ids = [cs.get("id") for cs in contract_stages]
    if stage_ids != ["S1", "S2", "S3", "S4"]:
        raise ValueError(
            f"contract stages must be S1->S2->S3->S4 in order, got {stage_ids}"
        )

    # Positional semantics -> inputs/outputs/executable for each stage. Name and skill come from the contract.
    positional = {
        _INTAKE: {
            "inputs": [path_sheet],
            "outputs": ["path_sheet"],
            "executable": False,
        },
        _ANALYSIS: {
            "inputs": list(path_sheet.get("engine_reading_order") or []),
            "outputs": ["analysis_artifact"],
            "executable": pid in EXECUTABLE_ENGINES,
        },
        _REPORT: {
            "inputs": list(registry_path.get("templates") or []),
            "outputs": list(registry_path.get("outputs") or []),
            "executable": False,
        },
        _QA: {
            "inputs": list(path_sheet.get("quality_gates") or []),
            "outputs": ["qa_verdict"],
            "executable": False,
        },
    }

    plan: list[Stage] = []
    for idx, cs in enumerate(contract_stages):
        sem = positional[idx]
        plan.append(
            Stage(
                name=cs["name"],
                skill=cs["skill"],
                inputs=sem["inputs"],
                outputs=sem["outputs"],
                executable=sem["executable"],
                path_id=pid,
            )
        )
    return plan


def run_executable_stages(plan: list[Stage], inputs: dict) -> dict:
    """Execute stages marked as executable in the plan and return a run manifest.

    For stages with ``executable=True``, looks up the wired coded engine via ``stage.path_id``
    in EXECUTABLE_ENGINES and runs it with ``inputs``, marking ``mode="code"``; remaining stages
    are left for LLM orchestration, gracefully skipped with ``mode="llm-orchestrated"``.
    The manifest has the shape ``{"path_id": ..., "stages": [{"name","mode","outputs"}]}``.
    """
    path_id = plan[0].path_id if plan else ""
    stages_manifest = []
    for stage in plan:
        if stage.executable and stage.path_id in EXECUTABLE_ENGINES:
            engine = EXECUTABLE_ENGINES[stage.path_id]
            stages_manifest.append(
                {"name": stage.name, "mode": "code", "outputs": engine(inputs)}
            )
        else:
            stages_manifest.append(
                {"name": stage.name, "mode": "llm-orchestrated", "outputs": None}
            )
    return {"path_id": path_id, "stages": stages_manifest}


def planned_path_notice(path_sheet: dict, registry_paths: dict) -> str | None:
    """Return an "under development" notice for a path sheet pointing to a planned path, else None.

    Reuses `path_sheet.sheet_notice`/`is_planned`; the orchestrator **does not execute** planned
    paths, only passes the notice upward (the router should recommend an active path instead).
    """
    pid = str(path_sheet.get("path_id", "")).strip() if isinstance(path_sheet, dict) else ""
    if pid and is_planned(pid, registry_paths):
        return sheet_notice(path_sheet, registry_paths)
    return None


def _run_sri(inputs: dict) -> dict:
    """Executable implementation of WP-RO-03 -> systemic-warning-framework (SRI + thermometer)."""
    value = sri(inputs["industries"], inputs["weights"])
    return {"sri": value, "thermometer": thermometer_level(value)}


def _run_concentration(inputs: dict) -> dict:
    """Executable implementation of WP-RO-01 -> concentration-framework (5-dimension score + rating adjustment)."""
    metrics = inputs["metrics"]
    adj = rating_adjustment(metrics)
    return {
        "score": concentration_risk_score(metrics),
        "adjustment": adj["adjustment"],
        "levels": adj["levels"],
        "bb_cap_triggered": adj["bb_cap_triggered"],
    }


def _run_contagion(inputs: dict) -> dict:
    """Executable implementation of WP-RO-02 -> contagion-matrix (portfolio exposure + high-intensity links + escalation)."""
    m = load_matrix()
    factors = list(inputs.get("escalation_factors") or [])
    if factors:
        m = apply_escalation(m, factors)
    holdings = inputs["holdings"]
    return {
        "exposure": portfolio_exposure(m, holdings),
        "links": [
            {
                "source": c.source,
                "target": c.target,
                "intensity": c.intensity,
                "types": list(c.types),
                "bidirectional": c.bidirectional,
            }
            for c in high_intensity_links(m, list(holdings))
        ],
        "factors_applied": factors,
    }


def _run_outlook(inputs: dict) -> dict:
    """Executable implementation of WP-X-05 -> outlook-monitoring-framework (outlook + watchlist + migration matrix)."""
    assessment = outlook_assessment(inputs["signals"])
    watchlist = watchlist_check(inputs.get("watchlist_triggers") or [])
    migration = migration_range(inputs["rating"], inputs.get("paradigm"))
    return {
        "outlook": assessment["outlook"],
        "confidence": assessment["confidence"],
        "net_score": assessment["net_score"],
        "watchlist": watchlist,
        "migration": migration,
    }


# Wired coded engine registry: path_id -> callable that runs the engine for that path.
# Kept explicit and minimal -- this series wires WP-RO-01 (concentration), WP-RO-02 (contagion),
# WP-RO-03 (SRI), and WP-X-05 (outlook monitoring).
EXECUTABLE_ENGINES = {
    "WP-RO-03": _run_sri,
    "WP-RO-01": _run_concentration,
    "WP-RO-02": _run_contagion,
    "WP-X-05": _run_outlook,
}
