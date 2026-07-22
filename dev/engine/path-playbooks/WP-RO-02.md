# WP-RO-02 Execution Contract — Cross-Industry Contagion

**Status**: ✅ active · **Role**: risk-officer · **Object**: portfolio · **Depth**: special

> This playbook is the execution contract for WP-RO-02. Read it fully before starting.
> AGENTS.md Non-Negotiables apply. This path is **wired**: the coded engine is the
> primary executor; manual execution follows the same documents.

## 1. Trigger & Scope

Use when: mapping contagion exposure across industries ("what does X's stress infect", "contagion path map for this portfolio").
Do not use when: concentration level alone (→ WP-RO-01), single market-wide SRI reading (→ WP-RO-03).

## 2. Required Reading Order

1. `dev/engine/contagion-matrix.md` — the 19x19 matrix, clusters, escalation rules (single source for all matrix values)
2. `dev/engine/contagion-theory.md` — contagion types and transmission pathways

## 3. Procedure (coded engine)

**Primary executor**: `src/pipeline.py` with path WP-RO-02 → `src/contagion_engine.py`.

1. **Load the matrix** — parsed at runtime from `contagion-matrix.md` §2.1 (heatmap) + §2.4 (annotations); never copy matrix values into prompts or code.
2. **Escalation (optional)** — when escalation factors are triggered, apply `contagion-matrix.md` §6.2 jump rules (explicit pair jumps + generic type bumps + Financials broad rows) and §6.3 synergy multipliers (Panic+Vacuum 1.5x / Panic+Leverage 2.0x / Vacuum+Year-End 1.5x / 3+ factors 3.0x, cap 5).
3. **Portfolio exposure** — compute inbound/outbound exposure per holding industry against the (possibly stressed) matrix.
4. **High-intensity links** — list links ≥ threshold (default 4) touching the portfolio's industries.
5. **Output** — exposure list, contagion path map (high-intensity links), factors applied, and adjustment recommendations (clusters per §5.4).

## 4. Dimension Vocabulary

- Industries: the 19 GICS industries of `contagion-matrix.md` §1.2 only.
- Paradigms: P1-P6 per `industry-framework.md` §2 (assignments per `contagion-matrix.md` §1.2).
- Contagion types/pathways: per `contagion-theory.md` (4 types, 7 pathways).
- Escalation factors: the five in `contagion-matrix.md` §6.1 only.

## 5. Output Shape

Analysis Artifact per `dev/engine/pipeline-contract.md` §2.2.
Path outputs (registry): contagion path map + adjustment recommendations.

## 6. Templates

- `dev/templates/template-type13.html` — Contagion Map

Render via `credit-report-builder` using exactly this file; no ad-hoc maps.

## 7. Quality Gates (all must pass)

- `Contagion Matrix (dev/engine/contagion-matrix.md §2)`
- `Escalation Factor (dev/engine/contagion-matrix.md §6)`
- `Transmission Path (dev/engine/contagion-theory.md §3)`

## 8. Drift Blacklist (forbidden)

- Hand-copying or paraphrasing matrix intensities anywhere (the matrix is parsed from the document; derived tables are machine-generated).
- Escalation factors outside §6.1's five, or synergy rules other than §6.3's documented combinations.
- Inventing industries, clusters, thresholds, or jump values — anything not in the engine documents is `engine_undefined`.
- Numeric claims without a `doc §section` citation.
- Designing ad-hoc HTML/maps/templates.
- Invoking Mode B without an explicit user-provided data source.
- Delivering before `credit-qa-verifier` issues a passing QA Verdict.
