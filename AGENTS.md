# AGENTS.md — Credence Cross-CLI Universal Entry

**Project**: Credence (Fixed-Income Credit Intelligent Analysis Engine)
**Engine Version**: v0.2.0
**Tagline**: Methodology-first credit analysis engine; portable unit is `SKILL.md`.

> Any agent CLI starts here: read your instructions file first, then the `SKILL.md` for the current task.
> For installation and tool-specific setup, see `INSTALL.md`.

## What This Package Is

A credit analysis engine for international fixed-income markets, organized into four layers:

1. **Mosaic Engine** — Assembles fragmented public data into coherent signals; data gaps are themselves risk signals.
2. **Dual-Track Engine** — Industry multi-layer pyramids (fundamentals) and market pricing signals run in parallel, then cross-validated.
3. **Multi-Stakeholder** — Credit Selector / Portfolio Manager / Trader / Risk Officer / Advisor / Individual Investor viewpoints.
4. **System-Intelligence Layer (SRI)** — Cross-industry contagion, five-dimension concentration, Systemic Risk Index (SRI).

**Thresholds, weights, and rating maps live only in `engine/*.md`.** This file and every skill never duplicate these values; any numerical judgment must reference the engine document and section.

## Path Resolution

Paths written as `${CLAUDE_PLUGIN_ROOT}/engine/...` and `${CLAUDE_PLUGIN_ROOT}/templates/...` resolve to the package root:

- **Plugin install** (Claude Code plugin/marketplace): `${CLAUDE_PLUGIN_ROOT}` is the package root inside the plugins directory — all references resolve automatically.
- **Opened as a project** (downloaded zip / Model A): treat `${CLAUDE_PLUGIN_ROOT}` as the package root you opened (the directory holding the engine and templates folders).


## How to Use in Your Agent CLI

This package is a self-contained installable agent package, with skills under `.claude/skills/`. **Simplest approach (Model A)**: Open the package root as your project and all references resolve automatically.

| Agent CLI | How to Access |
|---|---|
| **Claude Code** | Auto-discovers `.claude/skills/` (open the package root as project); `CLAUDE.md` points here. Distribution channel: plugin/marketplace (see `.claude-plugin/plugin.json`). |
| **Codex** | Natively reads `AGENTS.md`; then manually read the current task's `SKILL.md`. Deep adapter guidance in `adapters/codex.md`. |
| **Cursor** | Reads `AGENTS.md` and compatibly reads `.claude/skills/`. |
| **Gemini** | Reads `GEMINI.md` and compatibly reads `.claude/skills/`. |
| **OpenCode** | Reads `AGENTS.md` and compatibly reads `.claude/skills/`. |

Uniform approach: **Read your instructions file first, then the `SKILL.md` for the current task.** For integrating into an existing project (Model B) or global installation paths, see `INSTALL.md`.

## Skill Index

| Skill | Use When... | Path |
|---|---|---|
| `credit-analysis-router` | Requirements are vague or composite: route to a work path via four-question protocol | `.claude/skills/credit-analysis-router/SKILL.md` |
| `fixed-income-credit-analysis` | Concrete methodology task or engine path: execute analysis per path sheet or core doc set | `.claude/skills/fixed-income-credit-analysis/SKILL.md` |
| `credit-report-builder` | Assemble completed credit analysis into deliverables (select template Type 1-15, map L0/L1/L2 layers, dashboard); needs upstream analysis output | `.claude/skills/credit-report-builder/SKILL.md` |
| `credit-qa-verifier` | Pre-delivery review of report/analysis (quality gates, density rules, veto ceiling, Mode B guardrails, single-source compliance); terminal QA for four-stage chain | `.claude/skills/credit-qa-verifier/SKILL.md` |

## Four-Stage Pipeline

The engine decomposes each credit analysis into a four-stage chained contract, with `path_id` as the join key across stages:

| Stage | Responsibility | Carrying Skill |
|---|---|---|
| 1 intake | Four-question routing, produces Path Sheet | `credit-analysis-router` |
| 2 analysis | Execute analysis per `engine_reading_order` | `fixed-income-credit-analysis` |
| 3 report | Assemble analysis into deliverable report | `credit-report-builder` |
| 4 qa | Pre-delivery quality gate review | `credit-qa-verifier` |

Four-stage artifacts (Path Sheet / Analysis Artifact / Delivery Note / QA Verdict) field shapes and chaining edges are single-sourced in `engine/pipeline-contract.md`.

**Executable Orchestrator**: `src/pipeline.py` drives the four-stage chain as code, reading stage definitions from `pipeline-contract.md`. It calls coded engines only for wired paths -- **WP-RO-01 -> Concentration (`src/concentration_scorer.py`), WP-RO-02 -> Contagion (`src/contagion_engine.py`), WP-RO-03 -> SRI (`src/sri_calculator.py`), WP-X-05 -> Outlook (`src/outlook_engine.py`)**; remaining paths are LLM-orchestrated via engine documents.

## Single Source of Truth Rule

**Never duplicate thresholds, weights, SRI tiers, rating maps, or layer time budgets.** Any numerical judgment must reference `engine/<doc>.md SS<section>`; if the engine document does not define it, output `engine_undefined` -- do not fabricate values.

## Routing Baseline (Work Path Registry)

`engine/work-path-registry.md` is the single source of truth for routing: **16 work paths (all active in v0.1.0)**. The router maps ambiguous requirements to concrete work paths; when recommending a planned path, honestly state "not yet implemented" and suggest an active alternative.

## Platform Neutrality Note

This file and each skill uniformly refer to "your instructions file" -- every agent CLI has a different project-level instruction filename, and this package does not assume any specific product filename. Literal path references to `.claude/skills` are allowed: that is a path, not a behavioral instruction.

## Developer Regression Gate (Full Source Repository Required)

This installable package is a **runtime artifact** and does not include tests or consistency-check scripts. To run the regression gate (`pytest` + `consistency_check.py`) or modify the methodology itself, clone the full source repository.
