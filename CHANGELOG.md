# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.8] - 2026-07-22

### Added
- `plugin.json` manifest now carries author / homepage / repository / license / keywords.
- LICENSE now ships inside the dist package.
- CHANGELOG version gate in consistency_check.

### Changed
- LICENSE switched from custom Source-Available Non-Commercial to **MIT**.
- Skill and engine-document references in the dist package are prefixed with `${CLAUDE_PLUGIN_ROOT}` so they resolve under plugin installs (Model B) as well as open-as-project (Model A).
- All 4 SKILL.md now carry a Path Resolution note explaining both install modes.

### Removed
- Non-English README variants (zh / ja / ko / fr) — repository is now English-only.

## [0.0.7] - 2026-07-22

### Added
- Execution contracts (path-playbooks) for all 9 active work paths, with drift blacklist and quality gates.
- QA process-compliance checks (template / citation / dimension / chain) and a hard no-verdict-no-delivery mandate.
- `templates/index.yaml` machine-generated template manifest with drift guard.
- AGENTS.md + all SKILL.md: Non-Negotiables block (path sheet required, citations required, templates-only, QA required, no invented dimensions).

### Changed
- Fixed-income skill now refuses analysis without a Path Sheet (knowledge questions exempt).

### Fixed
- promote.py auto-regenerates template index after version promotion (stale `TEMPLATE_INDEX` CI failure).

## [0.0.6] - 2026-07-21

### Fixed
- Installer unzip fallback chain — GNU tar (Linux) cannot extract zip; install.js now tries unzip → tar → PowerShell.

## [0.0.5] - 2026-07-21

### Added
- SRI rules parsed from the engine document at load time (zero hardcoded thresholds).
- Concentration drift guard; input validation hardened (invalid enums/ranges fail loudly, per-stage error isolation).
- Path sheet semantic validation against registry entries.
- Release-artifact + dependency-completeness gates in consistency_check.
- CI: installer smoke on ubuntu+windows, full windows matrix, pip-install check, skip-count gate.

## [0.0.4] - 2026-07-21

### Changed
- Interpolation switched to round (band values fully reachable); §8.5 worked example re-derived.
- PM four-dimension frameworks disambiguated by name (§2.2 Portfolio Construction vs §2.2b Single-Instrument Dashboard).

### Added
- §6.3 multi-factor synergy multipliers implemented (Panic+Vacuum 1.5x / Panic+Leverage 2.0x / Vacuum+Year-End 1.5x / 3+ factors 3.0x).
- systemic-warning worked examples fully re-derived under the 19-industry GICS composition.

## [0.0.3] - 2026-07-21

### Changed
- Paradigm taxonomy unified on industry-framework P1-P6 (adjudication).
- 13→19-industry GICS migration across systemic-warning / concentration docs.

### Added
- Contagion derived tables machine-generated with drift guard.
- Skills ghost references purged; work-path status and artifact naming converged.

## [0.0.2] - 2026-07-20

### Fixed
- npx install chain (was deterministically failing); zip-based release distribution with checksum-verified installer.
- watch-band concentration scoring, SRI M4 adjustment factors, dict-input coercion.
- pyproject: declare src package and pyyaml dependency.

### Changed
- README methodology errors and unverifiable claims corrected in 5 languages (rating map direction, SRI 0-3+ scale, concentration thresholds).

## [0.0.1] - 2026-07-18

### Added
- Initial international release: 19-industry GICS contagion matrix, six international paradigms (P1-P6), six buy-side roles, S&P/Moody's/Fitch rating alignment, IFRS/US GAAP financial framework, four-stage agent skill chain.
