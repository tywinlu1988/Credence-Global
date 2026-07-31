# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-07-31

### Added
- **Trader Execution Framework** (`dev/engine/trader-framework.md`) — the final
  development-backlog item. Four execution dimensions (L0 Signal 35% / Spreads
  25% / Liquidity 25% / Market Context 15%), spread-vs-fair-value bands
  (±10bp), liquidity tiers with a data-gap rule, SRI thermometer overlay
  (Alert/Danger suspends new longs), and the Execution Decision Matrix —
  elevated from `multi-stakeholder.md` §2.4/§5.4 as the single source of truth.
- **WP-TR-01 completion**: `engine_sequence` gains trader-framework.md; two new
  quality gates (Execution Dimensions §2, Execution Decision Matrix §5);
  playbook procedure rewritten (score dimensions → matrix row → thermometer
  overlay → one-line execution posture in the L0 card); drift blacklist +4.

### Fixed
- `engine-overview.md`: duplicated navigation rows removed; §6 history backfilled
  (v0.1.1); §7.2 version-mapping table backfilled (advisor-origination,
  financing-channel — missing since v0.0.8).
- `dev/README.md` version history backfilled (v0.0.8–v0.1.1).
- Skill reference files: stale WP-TR-01 (partial) and WP-AD-01/WP-II-01
  (planned) statuses corrected to active.
- `multi-stakeholder.md` §2.4 gains an Authoritative Source Reference pointer
  to trader-framework.md (no dual-source drift).

## [0.1.1] - 2026-07-31

### Added
- **Playbook reading-order layering** (slimming Part C completion): all 16
  path-playbooks' Required Reading Order now separates must-read core sections
  from on-demand reference material; enforced by new gate T2.8.
- **Isolated-sandbox E2E audit fixes** (from the v0.1.0 Andritz walkthrough):
  report-index threshold lowered to >1 reports; CSS self-containment,
  relative-paths-only, and `<issuer-slug>-type<NN>.html` naming rules added to
  the report builder's Assembly Protocol; QA gains `css_self_contained` /
  `relative_paths` checks; dual-track §7.5 unrated & thinly-traded issuer
  proxy-signal methodology; AGENTS.md headless-mode invocation note.

### Fixed
- **Reading-guide accuracy**: 8 engine docs re-derived against actual section
  content (dual-track §6 Rating Mapping and mosaic §5 Completeness had been
  misclassified as reference material); 5 broken guide sentence artifacts and
  1 self-contradiction removed.
- Registry `Engine document ()` empty parentheses filled (WP-AD-01, WP-II-01).

## [0.1.0] - 2026-07-29

### Changed
- **Template CSS deduplication**: 4 inline-CSS templates (type1, type16, type17,
  report-index) converted to shared `template-base.css` via external `<link>`. CSS
  inlined at build time by `build_dist.py` — dist HTMLs remain self-contained.
  ~800 lines of duplicated CSS eliminated.
- **Boilerplate consolidation**: new `dev/engine/agent-protocol.md` (shared Path
  Resolution + Non-Negotiables); 4 SKILL.md inline Path Resolution blocks replaced
  with 1-line references (~24 lines eliminated); CLAUDE.md/GEMINI.md generators
  merged into a single parameterized function.
- **Engine doc reading guides**: 28 engine documents annotated with reading-guide
  metadata blocks separating core methodology (required reading) from reference
  material (worked examples, derivations, history — read on demand).
- **Version bump**: v0.0.9 → v0.1.0 (minor — architecture change, not just content).

## [0.0.9] - 2026-07-29

### Added
- 5 partial paths completed to active: WP-CS-02 (LGD + External Support), WP-PM-02
  (Comparative Analysis), WP-TR-01 (Trader L0 Signal Card), WP-RO-04 (Portfolio
  Stress Test), WP-X-04 (ESG/Governance Risk Scan) — each with playbook, quality
  gates, and drift blacklist.
- 2 planned paths completed to active: WP-AD-01 (Advisor Origination Assessment —
  new engine doc `advisor-origination-framework.md` + template-type16) and WP-II-01
  (Individual Investor Decision Support — new engine doc
  `financing-channel-framework.md` + template-type17).
- `report-index.html` navigation page auto-generated when an engagement produces
  more than 2 reports (new template + report-builder Assembly Protocol step 5 +
  QA index_compliance check).
- CHANGELOG date-ordering gate in consistency_check.
- End-to-end walkthrough: Siemens AG four-stage chain in validation/reports/industrial/.
- All 16 work paths active (0 partial, 0 planned).

### Changed
- Registry status distribution: 9→14→16 active over three v0.0.8 batches.
- Master README: badges, plugin install route, current architecture, stale-content purge.
- AGENTS.md Non-Negotiable #3: report-index sub-rule.

## [0.0.8] - 2026-07-27

### Added
- `plugin.json` manifest now carries author / homepage / repository / license / keywords.
- LICENSE now ships inside the dist package.
- CHANGELOG version gate in consistency_check.
- `scripts/publish_plugin.py` — publishes the dist package to the orphan `plugin-dist` branch (package root = branch root), the stable git location used as the marketplace source.
- `.claude-plugin/marketplace.json` at the repo root — `/plugin marketplace add tywinlu1988/Credence-Global` entry point.

### Changed
- LICENSE switched from custom Source-Available Non-Commercial to **MIT**.
- Skill and engine-document references in the dist package are prefixed with `${CLAUDE_PLUGIN_ROOT}` so they resolve under plugin installs (Model B) as well as open-as-project (Model A).
- All 4 SKILL.md now carry a Path Resolution note explaining both install modes.
- Dist README rewritten as a storefront page (positioning, architecture, four-stage chain, install routes, disclaimer).

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
