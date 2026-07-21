# AGENTS.md — Credence Cross-CLI Universal Entry

**Project**: Credence (Fixed-Income Credit Analysis Engine)
**Engine Version**: v0.0.6
**One-liner**: A methodology-first credit analysis engine; the portable unit is `SKILL.md`.

> Start here from any agent CLI: read your instructions file first, then the `SKILL.md` for your current task.

## What This Repository Is

A credit analysis engine for global fixed-income markets, organized in four layers:

1. **Mosaic Engine** — Assembles fragmented public data into coherent signals; data gaps are themselves risk signals.
2. **Dual-Track Engine** — Industry multi-tier pyramids (fundamentals) and market pricing signals run in parallel, then cross-validate.
3. **Multi-Stakeholder** — Credit Selector / Portfolio Manager / Risk Officer / Trader / Advisor / Individual Investor perspectives.
4. **System-Intelligence Layer (SRI)** — Cross-industry contagion, five-dimension concentration, Systemic Risk Index (SRI).

**Thresholds, weights, and rating mappings live only in `dev/engine/*.md`.** This file and all skills reference engine documents by path + section; never duplicate numeric values.

## How to Use in Your Agent CLI

Skills are stored in `dev/.claude/skills/`. Discovery mechanisms differ by CLI:

| Agent CLI | How to Access |
|-----------|---------------|
| **Claude Code** | Auto-discovers `dev/.claude/skills/` when working under `dev/` — no manual config needed. |
| **Codex** | Reads this `AGENTS.md` natively; then manually load the relevant `SKILL.md` body. Deep-dive adapter: `docs/adapters/codex.md`. |
| **Cursor** | Read this `AGENTS.md`, then manually load the relevant `SKILL.md`. |
| **Gemini** | Read this `AGENTS.md`, then manually load the relevant `SKILL.md`. |
| **OpenCode** | Read this `AGENTS.md`, then manually load the relevant `SKILL.md`. |

Universal posture: **read your instructions file first, then the `SKILL.md` for the task at hand.**

## Skill Index

| Skill | Use When… | Path |
|-------|-----------|------|
| `credit-analysis-router` | The request is vague or compound ("analyze this company", "what analysis should I run", "where do I start") — requires four-question routing to a work path | `dev/.claude/skills/credit-analysis-router/SKILL.md` |
| `fixed-income-credit-analysis` | A concrete methodology task or engine path has been named — execute analysis per the path sheet or core document set | `dev/.claude/skills/fixed-income-credit-analysis/SKILL.md` |
| `credit-report-builder` | Turn a completed credit analysis into a deliverable report — select template (Type 1–18), map to L0/L1/L2 tiers, assemble dashboard; requires upstream analysis artifact, does NOT perform analysis | `dev/.claude/skills/credit-report-builder/SKILL.md` |
| `credit-qa-verifier` | Pre-delivery quality gate review of a report/analysis — signal-density rules, one-shot-veto ceiling, Mode B guardrails, single-source compliance; terminal QA in the four-stage chain | `dev/.claude/skills/credit-qa-verifier/SKILL.md` |

## Four-Stage Pipeline

The engine decomposes each credit analysis into a four-stage chained contract, with `path_id` as the join key across stages:

| Stage | Responsibility | Skill | Status |
|-------|---------------|-------|--------|
| ① intake | Four-question routing, produces a **Path Sheet** | `credit-analysis-router` | ✅ Delivered |
| ② analysis | Execute analysis per path sheet `engine_reading_order` | `fixed-income-credit-analysis` | ✅ Delivered |
| ③ report | Assemble completed analysis into a deliverable report | `credit-report-builder` | ✅ Delivered |
| ④ qa | Pre-delivery quality gate verification | `credit-qa-verifier` | ✅ Delivered |

The single source of truth for the four artifacts (path sheet / analysis artifact / delivery note / qa verdict) and their chaining edges is `dev/engine/pipeline-contract.md`.

**Executable Orchestrator**: `src/pipeline.py` drives the four-stage chain in code. It reads stage definitions from `pipeline-contract.md` (never hardcodes stage names), and calls coded engines only for wired paths — **WP-RO-03 → SRI (`src/sri_calculator.py`), WP-RO-01 → Five-Dimension Concentration (`src/concentration_scorer.py`), WP-RO-02 → Contagion Matrix (`src/contagion_engine.py`), WP-X-05 → Outlook Monitoring (`src/outlook_engine.py`)**. All other paths/stages remain LLM-orchestrated per engine docs.

## Single Source of Truth Rule

**Never duplicate thresholds, weights, SRI tiers, rating mappings, or tier time budgets.** Every numeric judgment references `dev/engine/<doc>.md §section`; if the engine document does not define it, output `engine_undefined` — never invent values.

## Routing Baseline (Work Path Registry)

`dev/engine/work-path-registry.md` is the single source of truth for routing: **16 work paths (9 active / 5 partial / 2 planned)**. The router maps vague requests to concrete work paths using this registry; when a planned path is recommended, it MUST honestly state "under development" and offer an alternative active path.

## Validation Commands

After changes, both gates must stay green:

```
python -m pytest tests/ -q
python scripts/consistency_check.py
```

## Platform-Neutral Note

This file and all skills uniformly refer to "your instructions file" — each agent CLI has its own project-level instruction filename, and this repository assumes no specific product filename. The literal path `dev/.claude/skills` is permitted: it is a path, not a behavioral directive.
