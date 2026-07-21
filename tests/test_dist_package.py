"""Dist installable package integrity tests (v0.0.1, T12.1-T12.7).

`scripts/build_dist.py` assembles the dev/ sources into a `dist/credence/`
installable agent package. These tests build the artifact into ``tmp_path``
(without touching the working tree), asserting layout contracts one by one:
no absolute paths, no residual `dev/` references, links resolvable, skills
are a strict subset of the spec, engine docs complete, src locatable in dist
layout, excluded items absent, no parent-directory escape, provenance pointers
scrubbed and neighboring content intact, generated files complete, and builds
deterministic. The builder's own ``validate`` covers (a)(b)(c)(d)(e) plus
layout/exclusions; this file supplements the remaining (f)-(l).
"""

import hashlib
import importlib.util
import re
import sys
import zipfile
from pathlib import Path

import pytest

from src.path_sheet import (
    Depth,
    Mode,
    Object,
    engine_dir,
    load_registry_paths,
    templates_dir,
    validate_path_sheet,
)

ROOT = Path(__file__).resolve().parent.parent
BUILD_DIST = ROOT / "scripts" / "build_dist.py"

SKILL_NAMES = [
    "credit-analysis-router",
    "fixed-income-credit-analysis",
    "credit-report-builder",
    "credit-qa-verifier",
]
GENERATED_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "INSTALL.md",
    "README.md",
    ".claude-plugin/plugin.json",
    "adapters/codex.md",
]
ABS_PATH_RE = re.compile(r"(?<![A-Za-z])[A-Za-z]:[\\/]")
DEV_TOKEN_RE = re.compile(r"(?<![\w/.-])dev[/\\]")


def _load_builder():
    spec = importlib.util.spec_from_file_location("build_dist", BUILD_DIST)
    module = importlib.util.module_from_spec(spec)
    sys.modules["build_dist"] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def builder():
    return _load_builder()


def test_validate_flags_crlf_in_dist(builder, tmp_path):
    """P0: validate must loudly complain when dist output contains CRLF (guard against _write_text regression)."""
    out = tmp_path / "credence"
    builder.build(out_dir=out)
    target = out / "engine" / "engine-overview.md"
    target.write_bytes(target.read_bytes().replace(b"\n", b"\r\n"))
    errors = builder.validate(out_dir=out)
    assert any("CRLF:" in e and "engine-overview.md" in e for e in errors)


@pytest.fixture(scope="module")
def dist(builder, tmp_path_factory):
    out = tmp_path_factory.mktemp("dist") / "credence"
    builder.build(out)
    return out


def _texts(base):
    for f in sorted(base.rglob("*")):
        if f.is_file() and f.suffix in (".md", ".py", ".html", ".css", ".yaml", ".json"):
            yield f, f.read_text(encoding="utf-8")


# T12.1 — builder's own validate passes all checks (covers a: zero absolute paths / b: zero dev tokens / c: links resolvable /
#          d: 4 skills + strict frontmatter / e: 28 CORE_DOCS / layout / excluded items absent)
def test_t12_1_builder_validate_passes(builder, dist):
    assert builder.validate(dist) == []


# T12.2 — (f) src locatable in dist layout: engine_dir/templates_dir hit the flattened directories,
#          and for the dist root, validate_path_sheet passes for all active paths (templates actually on disk).
def test_t12_2_src_resolves_in_dist(dist):
    assert engine_dir(dist) == dist / "engine"
    assert templates_dir(dist) == dist / "templates"

    reg = load_registry_paths(dist / "engine" / "work-path-registry.md")
    active = sorted(pid for pid, p in reg.items() if str(p.get("status")) == "active")
    assert active, "no active paths parsed from dist registry"
    for pid in active:
        entry = reg[pid]
        sheet = {
            "role": str(entry.get("role", "meta")),
            "object": str((entry.get("trigger") or {}).get("object", Object.SINGLE_ISSUER.value)),
            "depth": str(entry.get("depth", Depth.L1.value)),
            "mode": Mode.A.value,
            "path_id": pid,
            "engine_reading_order": list(entry.get("engine_sequence") or []),
            "quality_gates": ["g"],
        }
        assert validate_path_sheet(sheet, reg, root=dist) == [], pid


# T12.3 — (h) no parent-directory escape: any .md in dist must not contain `](../../` (two levels up from
#           flattened engine/ escapes the package root).
def test_t12_3_no_parent_escape(dist):
    for f, text in _texts(dist):
        assert "](../../" not in text, f"{f.relative_to(dist)} contains a ../../ escape link"


# T12.4 — (g)+(i) excluded items absent and no audits//validation/ references.
def test_t12_4_excluded_and_pointer_tokens_absent(dist):
    for f in sorted(dist.rglob("*")):
        if f.is_dir():
            continue
        rel = f.relative_to(dist)
        assert "__pycache__" not in f.parts and f.suffix != ".pyc", rel
        assert f.name != "settings.local.json", rel
        assert "audits" not in f.parts, rel
    for f, text in _texts(dist / "engine"):
        assert "audits/" not in text, f"{f.name} still references audits/"
        assert "validation/" not in text, f"{f.name} still references validation/"


# T12.5 — (j) provenance pointers scrubbed, neighboring content intact.
def test_t12_5_pointers_scrubbed_neighbors_intact(dist):
    eo = (dist / "engine" / "engine-overview.md").read_text(encoding="utf-8")
    # audit table rows removed, non-audit nav rows survive
    assert "financial-analysis-audit" not in eo
    assert "rating-agency-benchmark-audit" not in eo
    assert "work-path-registry.md" in eo and "pipeline-contract.md" in eo
    # no dev/ path tokens remain (rewrite rules applied)
    assert "dev/engine/" not in eo and "dev/.claude/" not in eo

    es = (dist / "engine" / "external-support-framework.md").read_text(encoding="utf-8")
    # inline bracket fragments stripped, sentence retained
    assert "external support assessment was identified as a critical component" in es.lower()
    assert "rating-agency-benchmark-audit" not in es

    nc = (dist / "engine" / "non-credit-risk-overlay.md").read_text(encoding="utf-8")
    assert "risk-management-standards-audit" not in nc

    dt = (dist / "engine" / "dual-track-methodology.md").read_text(encoding="utf-8")
    assert "Risk Mitigation Recommendation" in dt  # neighboring content survives


# T12.6 — (k) generated entry/install files complete and carry version stamps.
def test_t12_6_generated_files_present(dist):
    for rel in GENERATED_FILES:
        assert (dist / rel).exists(), f"missing generated file {rel}"
    agents = (dist / "AGENTS.md").read_text(encoding="utf-8")
    assert "Engine Version" in agents and ".claude/skills/" in agents
    for name in SKILL_NAMES:
        assert f"skills/{name}/SKILL.md" in agents, f"AGENTS.md does not index {name}"


# T12.7 — (l) deterministic rebuild: two builds produce identical bytes.
def test_t12_7_deterministic_rebuild(builder, tmp_path):
    a = tmp_path / "a" / "credence"
    b = tmp_path / "b" / "credence"
    builder.build(a)
    builder.build(b)
    files_a = {f.relative_to(a): f.read_bytes() for f in sorted(a.rglob("*")) if f.is_file()}
    files_b = {f.relative_to(b): f.read_bytes() for f in sorted(b.rglob("*")) if f.is_file()}
    assert files_a.keys() == files_b.keys()
    diff = [str(k) for k in files_a if files_a[k] != files_b[k]]
    assert not diff, f"non-deterministic outputs: {diff[:5]}"


# T12.8 — release zip: single credence/ root, named <v>-release.zip, sha256 sidecar
#          matches the actual digest, and zip output is byte-deterministic.
def test_t12_8_release_zip(builder, tmp_path):
    out = tmp_path / "dist" / "credence"
    builder.build(out)
    assert builder.validate(out) == []
    zip_path, sha_path = builder.build_release_zip(out, tmp_path / "version")

    v = builder._version()
    assert zip_path.name == f"{v}-release.zip"
    assert sha_path.name == f"{v}-release.zip.sha256"

    with zipfile.ZipFile(zip_path) as zf:
        names = zf.namelist()
    assert names, "empty release zip"
    assert all(n.startswith("credence/") for n in names), "zip must have a single credence/ root"
    assert "credence/AGENTS.md" in names
    assert "credence/engine/pipeline-contract.md" in names
    assert "credence/templates/template-base.css" in names
    assert "credence/src/pipeline.py" in names

    digest = hashlib.sha256(zip_path.read_bytes()).hexdigest()
    assert sha_path.read_text(encoding="utf-8").split()[0] == digest

    zip2, _ = builder.build_release_zip(out, tmp_path / "version2")
    assert zip2.read_bytes() == zip_path.read_bytes(), "release zip is not deterministic"
