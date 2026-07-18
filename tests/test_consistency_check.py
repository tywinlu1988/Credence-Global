import re
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
CHECKER = ROOT / "scripts" / "consistency_check.py"
ENGINE_DIR = ROOT / "dev" / "engine"


def _import_checker():
    import importlib.util

    spec = importlib.util.spec_from_file_location("consistency_check", CHECKER)
    module = importlib.util.module_from_spec(spec)
    sys.modules["consistency_check"] = module
    spec.loader.exec_module(module)
    return module


def run_checker(*args):
    return subprocess.run(
        [sys.executable, str(CHECKER), *args],
        capture_output=True,
        text=True,
    )


def test_checker_runs():
    result = run_checker()
    print(result.stdout)
    print(result.stderr, file=sys.stderr)
    assert result.returncode == 0, "Consistency checker reported issues"
    assert "PASSED" in result.stdout


def test_only_links_skips_content_checks(tmp_path, monkeypatch):
    fake_engine = tmp_path / "engine"
    fake_engine.mkdir()
    (fake_engine / "systemic-warning-framework.md").write_text(
        "**Version**: v0.0.1\n\nSRI: 38/100\n", encoding="utf-8"
    )

    cc = _import_checker()
    monkeypatch.setattr(cc, "ENGINE_DIR", fake_engine)
    monkeypatch.setattr(cc, "TEMPLATES_DIR", tmp_path / "templates")
    monkeypatch.setattr(cc, "SKILL_FILE", tmp_path / "SKILL.md")

    full = cc.collect_errors(only_links=False)
    assert any("SRI_PCT" in e for e in full)

    links_only = cc.collect_errors(only_links=True)
    assert not any("SRI_PCT" in e for e in links_only)
    assert not links_only


def test_sri_pct_pattern_detects_percentage_scale():
    cc = _import_checker()
    assert cc.SRI_PCT_PATTERN.search("SRI: 38/100")
    assert cc.SRI_PCT_PATTERN.search("SRI 38/100") is None


def test_old_notch_patterns_detect_artifacts():
    cc = _import_checker()
    sample = "old 6-notch system (AAA/AA/A/BBB/BB/B/CCC/D)"
    assert any(p.search(sample) for p in cc.OLD_NOTCH_PATTERNS)


def test_check_rating_map_consistency_flags_deviation(tmp_path, monkeypatch):
    cc = _import_checker()
    fake_engine = tmp_path / "engine"
    fake_engine.mkdir()
    (fake_engine / "dual-track-methodology.md").write_text(
        "## 6. Rating Map\n| Score Range | New Rating |\n|---|---|\n| 9.5 - 10.0 | AAA |\n",
        encoding="utf-8",
    )
    (fake_engine / "systemic-warning-framework.md").write_text(
        "## 2. Signal Aggregation\n| Score Range | Corresponding Rating |\n|---|---|\n| 9.0 - 10.0 | AAA |\n",
        encoding="utf-8",
    )
    (fake_engine / "consistency-audit-v0.5.2.md").write_text(
        "| 9.0 - 10.0 | AAA |\n", encoding="utf-8"
    )
    monkeypatch.setattr(cc, "ENGINE_DIR", fake_engine)
    errors = cc.check_rating_map_consistency()
    assert any("systemic-warning-framework.md" in e and "9-10" in e for e in errors)
    assert not any("dual-track-methodology.md" in e for e in errors)
    assert not any("consistency-audit" in e for e in errors)


def test_check_sri_track_b_consistency_flags_contradiction(tmp_path, monkeypatch):
    cc = _import_checker()
    fake_engine = tmp_path / "engine"
    fake_engine.mkdir()
    (fake_engine / "systemic-warning-framework.md").write_text(
        "trackB_penalty:\n  yellow = 0.5 for watch\n  yellow = 0 for calm\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(cc, "ENGINE_DIR", fake_engine)
    errors = cc.check_sri_track_b_consistency()
    assert errors
    assert all("yellow penalty" in e for e in errors)


def test_check_sri_track_b_consistency_allows_single_rule(tmp_path, monkeypatch):
    cc = _import_checker()
    fake_engine = tmp_path / "engine"
    fake_engine.mkdir()
    (fake_engine / "systemic-warning-framework.md").write_text(
        "trackB_penalty:\n  yellow = 0 for calm\n", encoding="utf-8"
    )
    monkeypatch.setattr(cc, "ENGINE_DIR", fake_engine)
    assert cc.check_sri_track_b_consistency() == []


def test_check_sri_track_b_consistency_flags_orange_contradiction(tmp_path, monkeypatch):
    cc = _import_checker()
    fake_engine = tmp_path / "engine"
    fake_engine.mkdir()
    (fake_engine / "systemic-warning-framework.md").write_text(
        "trackB_penalty:\n  orange = 0.5 for elevated\n  orange = 1.0 for warning\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(cc, "ENGINE_DIR", fake_engine)
    errors = cc.check_sri_track_b_consistency()
    assert errors
    assert any("orange penalty" in e for e in errors)


def test_check_sri_track_b_consistency_flags_red_contradiction(tmp_path, monkeypatch):
    cc = _import_checker()
    fake_engine = tmp_path / "engine"
    fake_engine.mkdir()
    (fake_engine / "systemic-warning-framework.md").write_text(
        "trackB_penalty:\n  red = 1.0 for severe\n  red = 1.5 for critical\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(cc, "ENGINE_DIR", fake_engine)
    errors = cc.check_sri_track_b_consistency()
    assert errors
    assert any("red penalty" in e for e in errors)


def test_check_skill_references_flags_stale_version(tmp_path, monkeypatch):
    cc = _import_checker()
    fake_engine = tmp_path / "engine"
    fake_engine.mkdir()
    (fake_engine / "industry-framework.md").write_text(
        "**Version**: v0.0.1\n", encoding="utf-8"
    )
    fake_refs = tmp_path / "skills" / "some-skill" / "references"
    fake_refs.mkdir(parents=True)
    (fake_refs / "industry-pyramids.md").write_text(
        "**Version**: v0.0.2\n", encoding="utf-8"
    )
    monkeypatch.setattr(cc, "ENGINE_DIR", fake_engine)
    monkeypatch.setattr(cc, "SKILLS_DIR", tmp_path / "skills")
    errors = cc.check_skill_references()
    assert any("industry-pyramids.md" in e and "v0.0.2" in e for e in errors)


def test_check_skill_references_flags_missing_version(tmp_path, monkeypatch):
    cc = _import_checker()
    fake_engine = tmp_path / "engine"
    fake_engine.mkdir()
    (fake_engine / "mosaic-engine.md").write_text(
        "**Version**: v0.0.1\n", encoding="utf-8"
    )
    fake_refs = tmp_path / "skills" / "some-skill" / "references"
    fake_refs.mkdir(parents=True)
    (fake_refs / "mosaic-engine-architecture.md").write_text(
        "# Mosaic engine\n", encoding="utf-8"
    )
    monkeypatch.setattr(cc, "ENGINE_DIR", fake_engine)
    monkeypatch.setattr(cc, "SKILLS_DIR", tmp_path / "skills")
    errors = cc.check_skill_references()
    assert any("mosaic-engine-architecture.md" in e and "missing version header" in e for e in errors)


def test_skill_references_version_headers_in_sync():
    """T4.1: every skill references/ file's version header matches its engine counterpart
    on the real dev tree (checker SKILL_REFERENCES mechanism activated by references/)."""
    cc = _import_checker()
    errors = cc.check_skill_references()
    assert errors == [], f"Skill reference version headers out of sync: {errors}"


def test_check_paradigm_coverage_flags_missing_industry(tmp_path, monkeypatch):
    cc = _import_checker()
    fake_engine = tmp_path / "engine"
    fake_engine.mkdir()
    (fake_engine / "contagion-matrix.md").write_text(
        "### 1.2 Industry-to-Paradigm Mapping Table\n"
        "| # | Industry | Primary Paradigm | Secondary Paradigm | Financial Intensity |\n"
        "|---|---|---|---|---|\n"
        "| 1 | Solar/Storage | P1 | P4 | Medium |\n"
        "| 2 | LGFV/Municipal | Special | -- | Very High |\n"
        "### 1.3 Paradigm Clusters\n",
        encoding="utf-8",
    )
    (fake_engine / "industry-framework.md").write_text(
        "## Industry Pyramid Specifications\n### 4.1 Solar/Storage\n| D1 | ... |\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(cc, "ENGINE_DIR", fake_engine)
    errors = cc.check_paradigm_coverage()
    assert any("LGFV/Municipal" in e for e in errors)
    assert not any("Solar/Storage" in e for e in errors)


def test_check_paradigm_coverage_accepts_judgmental_note(tmp_path, monkeypatch):
    cc = _import_checker()
    fake_engine = tmp_path / "engine"
    fake_engine.mkdir()
    (fake_engine / "contagion-matrix.md").write_text(
        "### 1.2 Industry-to-Paradigm Mapping Table\n"
        "| # | Industry | Primary Paradigm | Typical Entity | Financial Intensity | Contagion Severity |\n"
        "|---|---|---|---|---|---|\n"
        "| 1 | Food/Beverage | Brand+Channel | B+/B/CCC | Low | High |\n"
        "### 1.3 Paradigm Clusters\n",
        encoding="utf-8",
    )
    (fake_engine / "industry-framework.md").write_text(
        "## Paradigm Boundary Notes\nFood/Beverage: judgmental assignment (Brand+Channel paradigm)\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(cc, "ENGINE_DIR", fake_engine)
    assert cc.check_paradigm_coverage() == []


def test_check_rating_map_consistency_accepts_legitimate_12_notch(tmp_path, monkeypatch):
    cc = _import_checker()
    fake_engine = tmp_path / "engine"
    fake_engine.mkdir()
    (fake_engine / "some-framework.md").write_text(
        "## Rating Tiers\n"
        "Investment grade includes AA+/AA/AA- and BBB+/BBB/BBB- etc., 12 tiers total.\n"
        "| Score Range | New Rating |\n"
        "|---|---|\n"
        "| 9.5 - 10.0 | AAA |\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(cc, "ENGINE_DIR", fake_engine)
    assert cc.check_rating_map_consistency() == []


def test_check_links_resolves_sibling_in_archived_subdir(tmp_path, monkeypatch):
    """A doc inside an archived subdir links to a same-dir sibling: resolves directly."""
    cc = _import_checker()
    fake_engine = tmp_path / "engine"
    archived = fake_engine / "audits"
    archived.mkdir(parents=True)
    (archived / "target.md").write_text("# target\n", encoding="utf-8")
    (archived / "source.md").write_text("See [target](target.md)\n", encoding="utf-8")
    monkeypatch.setattr(cc, "ENGINE_DIR", fake_engine)
    assert cc.check_links() == []


def test_check_links_falls_back_to_engine_root(tmp_path, monkeypatch):
    """A doc inside a subdir links to a file present only at the engine root: fallback resolves."""
    cc = _import_checker()
    fake_engine = tmp_path / "engine"
    archived = fake_engine / "audits"
    archived.mkdir(parents=True)
    (fake_engine / "engine-overview.md").write_text("# overview\n", encoding="utf-8")
    (archived / "source.md").write_text(
        "See [overview](engine-overview.md)\n", encoding="utf-8"
    )
    monkeypatch.setattr(cc, "ENGINE_DIR", fake_engine)
    assert cc.check_links() == []


def test_check_links_flags_target_missing_everywhere(tmp_path, monkeypatch):
    """A link whose target exists neither beside the source nor at the engine root still breaks."""
    cc = _import_checker()
    fake_engine = tmp_path / "engine"
    archived = fake_engine / "audits"
    archived.mkdir(parents=True)
    (archived / "source.md").write_text(
        "See [missing](no-such-file.md)\n", encoding="utf-8"
    )
    monkeypatch.setattr(cc, "ENGINE_DIR", fake_engine)
    errors = cc.check_links()
    assert any("BROKEN_LINK" in e and "no-such-file.md" in e for e in errors)


def test_check_skill_template_drift_flags_skill_templates_dir(tmp_path, monkeypatch):
    cc = _import_checker()
    skill_templates = tmp_path / "templates"
    skill_templates.mkdir()
    monkeypatch.setattr(cc, "SKILL_TEMPLATES_DIR", skill_templates)
    errors = cc.check_skill_template_drift()
    assert any("SKILL_TEMPLATE_DRIFT" in e for e in errors)


def test_check_skill_template_drift_absent_is_clean(tmp_path, monkeypatch):
    cc = _import_checker()
    monkeypatch.setattr(cc, "SKILL_TEMPLATES_DIR", tmp_path / "templates")
    assert cc.check_skill_template_drift() == []


def _expected_semver(cc):
    """Derive X.Y.Z from checker's EXPECTED_VERSION; test auto-adapts on promotion."""
    return cc.VERSION_RELEASE_RE.match(cc.EXPECTED_VERSION).group(1)


def test_check_version_alignment_passes_on_real_tree():
    cc = _import_checker()
    assert cc.check_version_alignment() == []


def test_check_version_alignment_flags_pyproject_mismatch(tmp_path, monkeypatch):
    cc = _import_checker()
    want = _expected_semver(cc)
    (tmp_path / "pyproject.toml").write_text('version = "0.0.0"\n', encoding="utf-8")
    (tmp_path / "package.json").write_text(
        '{"version": "%s"}\n' % want, encoding="utf-8"
    )
    monkeypatch.setattr(cc, "ROOT", tmp_path)
    errors = cc.check_version_alignment()
    assert any("pyproject.toml" in e for e in errors)
    assert not any("package.json" in e for e in errors)


def test_check_version_alignment_flags_package_json_mismatch(tmp_path, monkeypatch):
    cc = _import_checker()
    want = _expected_semver(cc)
    (tmp_path / "pyproject.toml").write_text(
        'version = "%s"\n' % want, encoding="utf-8"
    )
    (tmp_path / "package.json").write_text('{"version": "0.0.0"}\n', encoding="utf-8")
    monkeypatch.setattr(cc, "ROOT", tmp_path)
    errors = cc.check_version_alignment()
    assert any("package.json" in e for e in errors)
    assert not any("pyproject.toml" in e for e in errors)


def _fake_registry(tmp_path):
    """Minimum valid registry: 1 path with configurable templates/quality_gates."""
    (tmp_path / "dev" / "engine").mkdir(parents=True)
    registry = tmp_path / "dev" / "engine" / "work-path-registry.md"
    registry.write_text(
        "```yaml\n"
        "id: WP-T-01\n"
        "templates:\n"
        "  - dev/templates/template-type1.html\n"
        "quality_gates:\n"
        '  - "Example Gate (dev/engine/foo.md §2)"\n'
        "```\n",
        encoding="utf-8",
    )
    return registry


def test_check_registry_templates_flags_missing(tmp_path, monkeypatch):
    cc = _import_checker()
    _fake_registry(tmp_path)
    (tmp_path / "dev" / "engine" / "foo.md").write_text("## 2. Example\n", encoding="utf-8")
    monkeypatch.setattr(cc, "ENGINE_DIR", tmp_path / "dev" / "engine")
    monkeypatch.setattr(cc, "ROOT", tmp_path)
    errors = cc.check_registry_templates()
    assert any("template-type1.html" in e for e in errors)


def test_check_registry_templates_accepts_markers(tmp_path, monkeypatch):
    cc = _import_checker()
    (tmp_path / "dev" / "engine").mkdir(parents=True)
    registry = tmp_path / "dev" / "engine" / "work-path-registry.md"
    registry.write_text(
        "```yaml\n"
        "id: WP-T-01\n"
        "templates:\n"
        "  - planned\n"
        '  - "L0-spec: dev/engine/foo.md §3"\n'
        "quality_gates: []\n"
        "```\n",
        encoding="utf-8",
    )
    (tmp_path / "dev" / "engine" / "foo.md").write_text("# foo\n", encoding="utf-8")
    monkeypatch.setattr(cc, "ENGINE_DIR", tmp_path / "dev" / "engine")
    monkeypatch.setattr(cc, "ROOT", tmp_path)
    assert cc.check_registry_templates() == []


def test_check_registry_quality_gates_flags_bad_section(tmp_path, monkeypatch):
    cc = _import_checker()
    _fake_registry(tmp_path)
    (tmp_path / "dev" / "templates").mkdir(parents=True)
    (tmp_path / "dev" / "templates" / "template-type1.html").write_text("x", encoding="utf-8")
    (tmp_path / "dev" / "engine" / "foo.md").write_text("## 3. Other\n", encoding="utf-8")
    monkeypatch.setattr(cc, "ENGINE_DIR", tmp_path / "dev" / "engine")
    monkeypatch.setattr(cc, "ROOT", tmp_path)
    errors = cc.check_registry_quality_gates()
    assert any("§2" in e for e in errors)


def test_check_migration_matrix_structure_real_tree():
    cc = _import_checker()
    assert cc.check_migration_matrix_structure() == []


def test_check_migration_matrix_structure_flags_missing_rating(tmp_path, monkeypatch):
    cc = _import_checker()
    fake_engine = tmp_path / "engine"
    fake_engine.mkdir()
    (fake_engine / "outlook-monitoring-framework.md").write_text(
        "### 5.1 China Credit Bond Market Migration Probability Reference\n"
        "| Current Rating | Upgrade Probability | Stable Probability | Downgrade Probability | Default Probability | Note |\n"
        "|---|---|---|---|---|---|\n"
        "| **AAA** | 0% | 95%+ | <5% | <0.5% | x |\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(cc, "ENGINE_DIR", fake_engine)
    errors = cc.check_migration_matrix_structure()
    assert any("AA+" in e for e in errors)
    assert any("D" in e for e in errors)
