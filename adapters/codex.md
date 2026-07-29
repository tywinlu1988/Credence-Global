# Codex Deep Adaptation — Credence

**Engine Version**: v0.0.9 · **Entry**: Repository root `AGENTS.md`

Codex natively reads the repository root `AGENTS.md`, but **will not automatically discover** `.claude/skills/`. Therefore, Codex's access pattern is: first read `AGENTS.md` to locate the skill corresponding to the current task, then **manually read the `SKILL.md` content**, and then execute according to the content. The single source of truth for thresholds, weights, and rating mapping remains `${CLAUDE_PLUGIN_ROOT}/engine/*.md`; this file does not duplicate any values.

## 1. Access Sequence

1. Read the root `AGENTS.md`, locate the skill corresponding to the current task in the "Skill Index."
2. Manually open the `SKILL.md` content for that skill — Codex will not automatically load skills under `.claude/skills`.
3. Execute according to the `SKILL.md` content; when involving numerical judgments, reference `${CLAUDE_PLUGIN_ROOT}/engine/<doc>.md Section`. If the document is undefined, output "engine undefined."

## 2. Four-Question Intake Protocol

Ambiguous or composite requests first go through the `credit-analysis-router` four-question protocol, clarifying question by question, allowing skipping, multiple answers, or stating all at once:

- **Q1 Role**: M0 Credit Approval / M1 Investment / M2 Underwriting / M3 Trading / M4 Risk Control / M5 Financing / Uncertain.
- **Q2 Object**: Single issuer / Bond portfolio / Industry / Full market / Methodology development or engine validation.
- **Q3 Depth**: L0 Quick Signal / L1 Decision Snapshot / L2 Deep Report / Special Report.
- **Q4 Data**: Public data only (Mode A) / User explicitly provides external data sources (CSV/API/MCP -> Mode B).

Default strategy for uncertainty: start from L0/L1 when information is insufficient, do not jump directly to L2; when object is unclear, treat as single issuer first; when role is unclear, present candidate paths for user selection, do not arbitrarily set the path. Protocol details take `.claude/skills/credit-analysis-router/SKILL.md` as the single source of truth. When the user has already specified a concrete task or engine path, skip the four questions and go directly to `fixed-income-credit-analysis`.

## 3. Path Sheet Handoff (router -> fixed-income)

After the four questions converge, the router produces a "Work Path Sheet," whose `path_id` must exist in `${CLAUDE_PLUGIN_ROOT}/engine/work-path-registry.md`. Codex completes the router -> fixed-income handoff in the following order:

1. Read the path sheet produced by the router, take its `engine_reading_order` and `quality_gates`.
2. Switch to the `fixed-income-credit-analysis` skill, read and execute engine documents in `engine_reading_order` order.
3. Validate against `quality_gates` one by one; each entry format is `rule name (${CLAUDE_PLUGIN_ROOT}/engine/<doc>.md Section)`.

`${CLAUDE_PLUGIN_ROOT}/engine/work-path-registry.md` (16 work paths, 8 active) is the routing baseline: when recommending a planned path, must truthfully inform "under development" and provide an alternative active path, and must not fabricate capabilities.

## 4. Notes

This adapter targets **install package** users. The installable package is a runtime artifact and does not include tests or consistency-check scripts. To run the regression gate (`pytest` + `consistency_check.py`) or modify the methodology, clone the full source repository.
