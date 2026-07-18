"""promote.py promotion script tests (Recommendation 4: version declaration single-sourcing)."""

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
PROMOTE = ROOT / "scripts" / "promote.py"


def _load_promote():
    spec = importlib.util.spec_from_file_location("promote", PROMOTE)
    module = importlib.util.module_from_spec(spec)
    sys.modules["promote"] = module
    spec.loader.exec_module(module)
    return module


OLD = "v0.0.1"
NEW = "v0.0.2"


def _fake_tree(tmp_path: Path) -> None:
    """Representative fake tree covering every rule: declaration points + historical references that must be immune."""
    (tmp_path / "dev" / "engine").mkdir(parents=True)
    (tmp_path / "dev" / "engine" / "engine-overview.md").write_text(
        "# Overview\n\n**Version**: v0.0.1 | **Date**: 2026-07-10\n"
        "| **Engine Version** | Core Methodology Document | v0.0.1 | Description |\n"
        '| Independent system; header declares "Corresponding Engine Version: v0.0.1" |\n'
        "| engine-overview.md | v0.0.1 | Engine Architecture Overview |\n"
        "| **v1.0.0** | **2026-07-16** | historical row stays untouched |\n",
        encoding="utf-8",
    )
    (tmp_path / "dev" / "engine" / "industry-framework.md").write_text(
        "**Version**: v0.0.1 | **Paradigm Version**: v1.0.0 | **Date**: 2026-07-10\n"
        "Narrative from v0.0.1 stays untouched\n"
        "Paradigm mapping defined per Contagion Theory Foundation (v0.0.1)\n"
        "confidence is not quantitatively consumed in the current v0.0.1 computation\n"
        "| v0.0.1 (current) | own historical table row stays untouched |\n",
        encoding="utf-8",
    )
    skills = tmp_path / "dev" / ".claude" / "skills"
    (skills / "fixed-income-credit-analysis" / "references").mkdir(parents=True)
    (skills / "fixed-income-credit-analysis" / "SKILL.md").write_text(
        "# Fixed Income Credit Analysis Engine v0.0.1\n", encoding="utf-8"
    )
    (skills / "fixed-income-credit-analysis" / "references" / "ref.md").write_text(
        "**Version**: v0.0.1\n", encoding="utf-8"
    )
    (skills / "credit-qa-verifier").mkdir(parents=True)
    (skills / "credit-qa-verifier" / "SKILL.md").write_text(
        "**Corresponding Engine Version**: v0.0.1\n", encoding="utf-8"
    )
    (tmp_path / "dev").mkdir(exist_ok=True)
    (tmp_path / "dev" / "README.md").write_text(
        "**Version**: v0.0.1\n| **v0.0.1** | **2026-07-16** | historical row stays untouched |\n",
        encoding="utf-8",
    )
    (tmp_path / "AGENTS.md").write_text("**Engine Version**：v0.0.1\n", encoding="utf-8")
    (tmp_path / "README.md").write_text(
        "**Version** `v0.0.1`\nRelease package at `version/v0.0.1/`.\n",
        encoding="utf-8",
    )
    (tmp_path / "pyproject.toml").write_text('version = "0.0.1"\n', encoding="utf-8")
    (tmp_path / "package.json").write_text('{"version": "0.0.1"}\n', encoding="utf-8")
    (tmp_path / "scripts").mkdir(exist_ok=True)
    (tmp_path / "scripts" / "consistency_check.py").write_text(
        'EXPECTED_VERSION = "v0.0.1"\n', encoding="utf-8"
    )
    (tmp_path / "scripts" / "build_dist.py").write_text(
        '    return m.group(1) if m else "v0.0.1"\n', encoding="utf-8"
    )
    (tmp_path / ".gitignore").write_text(
        "# Only current installable package version/v0.0.1/ is committed\nversion/*\n!version/v0.0.1/\n",
        encoding="utf-8",
    )
    (tmp_path / "dev" / "templates").mkdir(exist_ok=True)
    (tmp_path / "dev" / "templates" / "template-type13.html").write_text(
        "<!-- @engine-version: v0.0.1 -->\n"
        "<span>Report Version: v0.0.1 · Type 13 Contagion Analysis</span>\n",
        encoding="utf-8",
    )
    (tmp_path / "docs" / "adapters").mkdir(parents=True, exist_ok=True)
    (tmp_path / "docs" / "adapters" / "codex.md").write_text(
        "**Engine Version**：v0.0.1 · **Entry**：Repository Root Level `AGENTS.md`\n",
        encoding="utf-8",
    )
    (tmp_path / "docs").mkdir(exist_ok=True)
    (tmp_path / "docs" / "VERSION-MANAGEMENT.md").write_text(
        "**Corresponding Engine Version**: v0.0.1\n"
        "(now at `version/v0.0.1/`)\n"
        "(now at `v0.0.1`)\n"
        "Narrative from **v0.0.1** stays untouched\n",
        encoding="utf-8",
    )


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_apply_rules_rewrites_all_declaration_points(tmp_path):
    pm = _load_promote()
    _fake_tree(tmp_path)
    changes = pm.apply_rules(tmp_path, OLD, NEW, apply=True)
    assert changes, "no changes reported"
    overview = _read(tmp_path / "dev" / "engine" / "engine-overview.md")
    assert "**Version**: v0.0.2" in overview
    assert "| engine-overview.md | v0.0.2 |" in overview
    assert "**Engine Version** | Core Methodology Document | v0.0.2" in overview
    industry = _read(tmp_path / "dev" / "engine" / "industry-framework.md")
    assert industry.startswith("**Version**: v0.0.2")
    assert "Paradigm mapping defined per Contagion Theory Foundation (v0.0.2)" in industry, "cross-document reference not rewritten"
    assert "is not quantitatively consumed in the current v0.0.2 computation" in industry, "current version narrative not rewritten"
    assert "# Fixed Income Credit Analysis Engine v0.0.2" in _read(
        tmp_path / "dev" / ".claude" / "skills" / "fixed-income-credit-analysis" / "SKILL.md"
    )
    assert "**Version**: v0.0.2" in _read(
        tmp_path / "dev" / ".claude" / "skills" / "fixed-income-credit-analysis" / "references" / "ref.md"
    )
    assert "**Corresponding Engine Version**: v0.0.2" in _read(
        tmp_path / "dev" / ".claude" / "skills" / "credit-qa-verifier" / "SKILL.md"
    )
    assert _read(tmp_path / "dev" / "README.md").startswith("**Version**: v0.0.2")
    assert "**Engine Version**：v0.0.2" in _read(tmp_path / "AGENTS.md")
    readme = _read(tmp_path / "README.md")
    assert "`v0.0.2`" in readme and "version/v0.0.2/" in readme
    assert 'version = "0.0.2"' in _read(tmp_path / "pyproject.toml")
    assert '{"version": "0.0.2"}' in _read(tmp_path / "package.json")
    assert 'EXPECTED_VERSION = "v0.0.2"' in _read(
        tmp_path / "scripts" / "consistency_check.py"
    )
    assert 'else "v0.0.2"' in _read(tmp_path / "scripts" / "build_dist.py")
    assert "!version/v0.0.2/" in _read(tmp_path / ".gitignore")
    assert "Only current installable package version/v0.0.2/ is committed" in _read(tmp_path / ".gitignore")
    templates = _read(tmp_path / "dev" / "templates" / "template-type13.html")
    assert "@engine-version: v0.0.2" in templates
    assert "Report Version: v0.0.2" in templates
    assert "**Engine Version**：v0.0.2" in _read(tmp_path / "docs" / "adapters" / "codex.md")
    vm = _read(tmp_path / "docs" / "VERSION-MANAGEMENT.md")
    assert "**Corresponding Engine Version**: v0.0.2" in vm
    assert "`version/v0.0.2/`" in vm
    assert "(now at `v0.0.2`)" in vm


def test_apply_rules_preserves_historical_references(tmp_path):
    pm = _load_promote()
    _fake_tree(tmp_path)
    pm.apply_rules(tmp_path, OLD, NEW, apply=True)
    overview = _read(tmp_path / "dev" / "engine" / "engine-overview.md")
    assert "| **v1.0.0** |" in overview, "historical table row wrongfully altered"
    assert "Corresponding Engine Version: v0.0.1" in overview, "audits convention example wrongfully altered"
    industry = _read(tmp_path / "dev" / "engine" / "industry-framework.md")
    assert "**Paradigm Version**: v1.0.0" in industry, "paradigm version wrongfully altered"
    assert "Narrative from v0.0.1 stays untouched" in industry, "narrative line wrongfully altered"
    assert "| v0.0.1 (current) |" in industry, "own historical table row wrongfully altered"
    dev_readme = _read(tmp_path / "dev" / "README.md")
    assert "| **v0.0.1** | **2026-07-16** |" in dev_readme, "dev historical table row wrongfully altered"
    vm = _read(tmp_path / "docs" / "VERSION-MANAGEMENT.md")
    assert "Narrative from **v0.0.1** stays untouched" in vm, "bold historical narrative wrongfully altered"


def test_dry_run_reports_but_writes_nothing(tmp_path):
    pm = _load_promote()
    _fake_tree(tmp_path)
    before = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    changes = pm.apply_rules(tmp_path, OLD, NEW, apply=False)
    assert changes, "dry-run should also report changes"
    after = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    assert before == after, "dry-run wrote to disk"


def test_semver_derivation_and_validation():
    pm = _load_promote()
    assert pm.derive_semver("v0.0.1") == "0.0.1"
    assert pm.derive_semver("v1.0.0-alpha") == "1.0.0"
    for bad in ("0.0.1", "v0.8", "v0.0.2-RELEASE", ""):
        assert pm.derive_semver(bad) is None, bad


def test_detect_old_version_from_checker(tmp_path):
    pm = _load_promote()
    (tmp_path / "scripts").mkdir()
    (tmp_path / "scripts" / "consistency_check.py").write_text(
        'EXPECTED_VERSION = "v0.0.1"\n', encoding="utf-8"
    )
    assert pm.detect_old_version(tmp_path) == "v0.0.1"


def test_real_tree_dry_run_reports_changes_and_stays_clean():
    pm = _load_promote()
    old = pm.detect_old_version(ROOT)
    if pm.derive_semver(old) is None:
        pytest.skip(f"current EXPECTED_VERSION {old!r} is not a release format")

    def _status():
        return subprocess.run(
            ["git", "status", "--porcelain"], cwd=ROOT,
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        ).stdout

    before = _status()
    changes = pm.apply_rules(ROOT, old, "v9.9.9-release", apply=False)
    assert len(changes) > 30, f"real tree changes count abnormal: {len(changes)}"
    assert _status() == before, "dry-run altered the working tree"
