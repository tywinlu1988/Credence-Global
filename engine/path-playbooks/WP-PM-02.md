# WP-PM-02 Execution Contract — Comparative Analysis

**Status**: ✅ active · **Role**: portfolio-manager · **Object**: single-issuer · **Depth**: L2

> This playbook is the execution contract for WP-PM-02. Read it fully before starting.
> AGENTS.md Non-Negotiables apply. This path compares two issuers or bonds side-by-side;
> each side must have a completed analysis (at minimum WP-CS-01 or equivalent for each).

## 1. Trigger & Scope

Use when: comparing two bonds or issuers ("which is better", "compare X vs Y for a 5-year hold", "differentiation analysis between A and B"), forward-looking relative-value assessment.
Do not use when: single-issuer rating (→ WP-CS-01 per issuer), portfolio-level dashboard (→ WP-PM-01), multi-issuer systemic view (→ WP-RO-01/02/03).

## 2. Required Reading Order

**Must read (core rules):**
1. `${CLAUDE_PLUGIN_ROOT}/engine/dual-track-methodology.md` §§1-4, §6 — Track A (fundamentals) and Track B (market pricing) cross-validation framework, rating mapping
2. `${CLAUDE_PLUGIN_ROOT}/engine/validation-methodology.md` §§1-5 — forward comparison and differentiation analysis (§4, §4.2 are this path's core)

**Reference (read on demand):**
- `${CLAUDE_PLUGIN_ROOT}/engine/dual-track-methodology.md` §5, §§7-11 — examples and extended discussion
- `${CLAUDE_PLUGIN_ROOT}/engine/validation-methodology.md` §§6-7 — case summaries, improvement record

## 3. Procedure

1. **Verify prerequisites** — each of the two issuers must have a completed base analysis (at minimum Track A fundamentals + Track B market pricing, or a full WP-CS-01 rating). This skill does not perform the base analyses itself.
2. **Align dimensions** — Map both issuers to their respective paradigms (P1-P6 per `industry-framework.md` §2). If the paradigms differ, note paradigm-contextual adjustment factors per `dual-track-methodology.md`.
3. **Comparative scoring** — For each shared dimension (Track A fundamentals D1-D10, Track B market signals), score both issuers on the same scale. Use the cross-validation matrix from `dual-track-methodology.md` §4 to detect mutual reinforcement vs. divergence.
4. **Differentiation analysis** — Per `validation-methodology.md` §4.2, identify the dimensions where the two issuers diverge most (top 3 differentiating factors). These are the most decision-relevant insights.
5. **Forward-looking conclusion** — Per `validation-methodology.md` §4, produce a forward comparison: which issuer is positioned better for the stated time horizon, based on trajectory (not just snapshot). Include the comparison score.
6. **Output** — comparison score, differentiation conclusion with top diverging dimensions.

## 4. Dimension Vocabulary

- Track A fundamentals: D1-D10 per `industry-framework.md` and `dual-track-methodology.md` §2.
- Track B market signals: credit spreads, volatility, fund flows, rating migration per `dual-track-methodology.md` §3.
- Paradigms: P1-P6 per `industry-framework.md` §2 (six paradigms only).
- Rating scale: the 18-notch internal scale per `dual-track-methodology.md` §6 — no fabricated mappings.

## 5. Output Shape

Analysis Artifact per `${CLAUDE_PLUGIN_ROOT}/engine/pipeline-contract.md` §2.2 (dual-issuer, with per-issuer findings arrays).
Path outputs (registry): comparison score, differentiation conclusion.

## 6. Templates

- `${CLAUDE_PLUGIN_ROOT}/templates/template-type2.html` — Comparative Analysis

Render via `credit-report-builder` using exactly this file; no ad-hoc comparison tables.

## 7. Quality Gates (all must pass)

- `Forward-Looking Comparison Method (${CLAUDE_PLUGIN_ROOT}/engine/validation-methodology.md §4)`
- `Comparative Assessment Results (${CLAUDE_PLUGIN_ROOT}/engine/validation-methodology.md §4.3)`

## 8. Drift Blacklist (forbidden)

- Running comparison without completed base analyses for both sides.
- Mixing scales (e.g., applying P1 weights to a P4 issuer without paradigm adjustment).
- Concluding "X is better" without naming the top 3 differentiating dimensions.
- Fabricating market pricing data (spreads, volatilities, fund flows) — Mode B values require an explicit user-provided data source per `mosaic-engine.md` §6.
- Inventing comparison dimensions, rating mappings, or differentiation factors — anything not in the engine documents is `engine_undefined`.
- Numeric claims without a `doc §section` citation.
- Designing ad-hoc HTML/comparison layouts/templates.
- Delivering before `credit-qa-verifier` issues a passing QA Verdict.
