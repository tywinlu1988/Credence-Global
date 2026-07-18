"""Work path sheet schema and validator (v0.0.1 -- pipeline foundation).

The credit-analysis-router skill produces a work-path sheet after the four-question
protocol converges, routing the "role x object x depth x data mode" to a registered
work-path in dev/engine/work-path-registry.md. This module is the machine-readable
single source of truth for the work-path sheet:

- Defines the path-sheet four-tuple (role/object/depth/mode) and registry path-status
  enums;
- Provides the PathSheet data class and validate_path_sheet validator (structural
  validity + referential integrity);
- Provides the registry ```yaml block parser load_registry_paths, shared by the
  validator and tests.

Single-source-of-truth principle: this module validates only the sheet's structure and
references; it does not duplicate any engine thresholds, weights, or layer semantics.
L0/L1/L2 layering definitions are in dev/engine/output-layered-framework.md; SRI
thermometer bands are in dev/engine/systemic-warning-framework.md.
"""

import re
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

# Registry ```yaml fence block (same parsing approach as tests/test_work_path_registry.py).
YAML_BLOCK_RE = re.compile(r"```yaml\s*\n(.*?)```", re.DOTALL)


def engine_dir(root=None) -> Path:
    """Locate the engine methodology documents directory, adapting to two layouts.

    The dist package uses a flat layout (``<root>/engine``); the dev repo uses a
    nested layout (``<root>/dev/engine``). ``root`` defaults to the repo/package root
    (two levels above ``__file__``). This enables end users to locate contracts/registry
    in dist, and is reused by dist integrity test assertions.
    """
    base = Path(root) if root is not None else ROOT
    flat = base / "engine"
    return flat if flat.is_dir() else base / "dev" / "engine"


def templates_dir(root=None) -> Path:
    """Locate the report template directory, adapting to flat (``<root>/templates``) and nested (``<root>/dev/templates``)."""
    base = Path(root) if root is not None else ROOT
    flat = base / "templates"
    return flat if flat.is_dir() else base / "dev" / "templates"


class Role(str, Enum):
    """Q1 Role: stakeholder identity (Credit Selector, Portfolio Manager, Risk Officer,
    Trader, Advisor, Individual Investor) or cross-role meta/specialized path."""

    CREDIT_SELECTOR = "credit-selector"
    PORTFOLIO_MANAGER = "portfolio-manager"
    RISK_OFFICER = "risk-officer"
    TRADER = "trader"
    ADVISOR = "advisor"
    INDIVIDUAL_INVESTOR = "individual-investor"
    META = "meta"


class Object(str, Enum):
    """Q2 Object: analysis target."""

    SINGLE_ISSUER = "single-issuer"
    PORTFOLIO = "portfolio"
    INDUSTRY = "industry"
    MARKET = "market"
    META = "meta"


class Depth(str, Enum):
    """Q3 Depth: three output layers (output-layered-framework SS2) + special."""

    L0 = "L0"
    L1 = "L1"
    L2 = "L2"
    SPECIAL = "special"


class Mode(str, Enum):
    """Q4 Data mode: A = public data only; B = user explicitly provides external data sources."""

    A = "A"
    B = "B"


class PathStatus(str, Enum):
    """Registry path status (work-path-registry SS1)."""

    ACTIVE = "active"
    PARTIAL = "partial"
    PLANNED = "planned"


# Required scalar fields on a path sheet (must exist and be non-empty).
REQUIRED_SCALAR_FIELDS = ["role", "object", "depth", "mode", "path_id"]
# Required list fields on a path sheet (must exist and be list; planned paths allow empty lists).
REQUIRED_LIST_FIELDS = ["engine_reading_order", "quality_gates"]
# All required fields (notes is optional).
REQUIRED_SHEET_FIELDS = REQUIRED_SCALAR_FIELDS + REQUIRED_LIST_FIELDS

_ENUM_FIELDS = {
    "role": Role,
    "object": Object,
    "depth": Depth,
    "mode": Mode,
}

# Non-file marker values allowed in ``templates`` (consistent with registry SSschema).
TEMPLATE_MARKERS = ("planned", "L0-spec")


@dataclass
class PathSheet:
    """Structured work path sheet produced by the router (fields aligned with registry schema)."""

    role: str
    object: str
    depth: str
    mode: str
    path_id: str
    engine_reading_order: list[str] = field(default_factory=list)
    quality_gates: list[str] = field(default_factory=list)
    notes: str = ""

    @classmethod
    def from_dict(cls, data: dict) -> "PathSheet":
        """Construct from a yaml dict produced by the router (known fields only; omitted fields default to empty)."""
        return cls(
            role=str(data.get("role", "")),
            object=str(data.get("object", "")),
            depth=str(data.get("depth", "")),
            mode=str(data.get("mode", "")),
            path_id=str(data.get("path_id", "")),
            engine_reading_order=list(data.get("engine_reading_order") or []),
            quality_gates=list(data.get("quality_gates") or []),
            notes=str(data.get("notes", "")),
        )

    def to_dict(self) -> dict:
        """Export as a dict isomorphic to the router yaml."""
        return {
            "role": self.role,
            "object": self.object,
            "depth": self.depth,
            "mode": self.mode,
            "path_id": self.path_id,
            "engine_reading_order": list(self.engine_reading_order),
            "quality_gates": list(self.quality_gates),
            "notes": self.notes,
        }


def is_template_marker(entry: object) -> bool:
    """Return True when a templates entry is a non-file marker (``planned`` / ``L0-spec: ...``)."""
    s = str(entry).strip()
    return any(s == m or s.startswith(m + ":") or s.startswith(m + " ") for m in TEMPLATE_MARKERS)


def load_registry_paths(registry_md_path) -> dict[str, dict]:
    """Parse ```yaml blocks from a registry markdown file, returning ``{path_id: parsed dict}``.

    Parsing is consistent with tests/test_work_path_registry.py: regex to extract fence
    blocks + yaml.safe_load, keeping only dicts that declare an ``id`` key. This is the
    single source of truth for registry parsing, shared by the validator and tests.
    """
    text = Path(registry_md_path).read_text(encoding="utf-8")
    paths: dict[str, dict] = {}
    for block in YAML_BLOCK_RE.findall(text):
        data = yaml.safe_load(block)
        if isinstance(data, dict) and "id" in data:
            paths[str(data["id"]).strip()] = data
    return paths


def is_planned(path_id: str, registry_paths: dict) -> bool:
    """Return True when path_id exists and its status is ``planned`` (not yet implemented)."""
    path = registry_paths.get(str(path_id).strip())
    if path is None:
        return False
    return str(path.get("status", "")).strip() == PathStatus.PLANNED.value


def _is_empty(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return value.strip() == ""
    if isinstance(value, (list, tuple, dict, set)):
        return len(value) == 0
    return False


def _enum_values(enum_cls) -> list[str]:
    return [member.value for member in enum_cls]


def validate_path_sheet(sheet: dict, registry_paths: dict, root=None) -> list[str]:
    """Validate a work path sheet, returning a list of human-readable error strings (empty = valid).

    Validation items:

    - Required fields exist and are non-empty (scalar non-empty; list must be list and
      non-empty, only planned paths allow empty lists);
    - ``role``/``object``/``depth``/``mode`` each fall within their valid enum (reports
      field name and illegal value);
    - ``path_id`` exists in the registry (reports unknown id);
    - If the resolved path is ``active``, each non-marker entry in its ``templates``
      must be a real file on disk.

    A planned path does not fail validation just because it is not yet implemented —
    callers should use is_planned / sheet_notice to surface a "not yet implemented"
    notice to the user instead of a template invocation instruction. ``root`` is used
    to resolve template relative paths, defaulting to the repo root.
    """
    if isinstance(sheet, PathSheet):
        sheet = sheet.to_dict()
    if not isinstance(sheet, dict):
        return [f"path sheet must be a mapping, got {type(sheet).__name__}"]

    base = Path(root) if root is not None else ROOT
    errors: list[str] = []

    # Required scalar fields: must exist and be non-empty.
    for name in REQUIRED_SCALAR_FIELDS:
        if name not in sheet:
            errors.append(f"missing required field: {name!r}")
        elif _is_empty(sheet[name]):
            errors.append(f"required field {name!r} is empty")

    # Resolve path_id once, reused for both "empty-list gate" and "template on disk" checks.
    pid_value = sheet.get("path_id")
    pid = "" if _is_empty(pid_value) else str(pid_value).strip()
    path = registry_paths.get(pid) if pid else None
    path_status = "" if path is None else str(path.get("status", "")).strip()
    planned = path_status == PathStatus.PLANNED.value

    # Required list fields: must exist and be a list. Non-planned paths (active/partial)
    # must be executable non-empty sequences -- empty lists are only allowed for planned
    # paths (not yet implemented; no engine/quality gate to register).
    for name in REQUIRED_LIST_FIELDS:
        if name not in sheet:
            errors.append(f"missing required field: {name!r}")
        elif not isinstance(sheet[name], (list, tuple)):
            errors.append(
                f"required field {name!r} must be a list, got {type(sheet[name]).__name__}"
            )
        elif len(sheet[name]) == 0 and path is not None and not planned:
            errors.append(
                f"required field {name!r} must not be empty for non-planned path {pid!r}"
            )

    # Enum validity (only checked when field exists and is non-empty, to avoid duplicate errors).
    for name, enum_cls in _ENUM_FIELDS.items():
        if name not in sheet or _is_empty(sheet[name]):
            continue
        raw = sheet[name].value if isinstance(sheet[name], Enum) else sheet[name]
        value = str(raw).strip()
        if value not in _enum_values(enum_cls):
            allowed = "|".join(_enum_values(enum_cls))
            errors.append(f"field {name!r} has illegal value {value!r} (allowed: {allowed})")

    # path_id referential integrity + active path template on-disk check.
    if pid:
        if path is None:
            errors.append(f"unknown path_id {pid!r}: not found in work-path registry")
        elif path_status == PathStatus.ACTIVE.value:
            for tmpl in path.get("templates") or []:
                if is_template_marker(tmpl):
                    continue
                if not (base / str(tmpl)).exists():
                    errors.append(f"active path {pid!r} template missing on disk: {tmpl}")

    return errors


def sheet_notice(sheet: dict, registry_paths: dict) -> str | None:
    """Return a "not yet implemented" notice for a planned-path sheet (non-fatal); None if no notice.

    A sheet pointing to a planned path should not trigger template invocation instructions
    -- the router should honestly inform the user that the path is planned and recommend
    an active path instead. Active/partial paths and unknown ids return None.
    """
    if isinstance(sheet, PathSheet):
        sheet = sheet.to_dict()
    if not isinstance(sheet, dict):
        return None
    pid_value = sheet.get("path_id")
    if _is_empty(pid_value):
        return None
    pid = str(pid_value).strip()
    if is_planned(pid, registry_paths):
        name = str(registry_paths[pid].get("name", "")).strip()
        label = f"{pid} ({name})" if name else pid
        return (
            f"Path {label} is planned (not yet implemented): engine/templates not yet available. "
            "Inform the user honestly and switch to an active path instead; "
            "do not fabricate template invocation instructions."
        )
    return None
