# WP-RO-03 Execution Contract — Systemic Risk Reading (SRI)

**Status**: ✅ active · **Role**: risk-officer · **Object**: market · **Depth**: special

> This playbook is the execution contract for WP-RO-03. Read it fully before starting.
> AGENTS.md Non-Negotiables apply. This path is **wired**: the coded engine is the
> primary executor; manual execution follows the same documents.

## 1. Trigger & Scope

Use when: a market-wide systemic risk reading is needed ("what's the SRI today", "systemic thermometer level", monthly SRI cycle).
Do not use when: single-issuer outlook (→ WP-X-05), portfolio concentration (→ WP-RO-01), contagion paths (→ WP-RO-02).

## 2. Required Reading Order

1. `dev/engine/systemic-warning-framework.md` — the entire definition of this path

## 3. Procedure (coded engine)

**Primary executor**: `src/pipeline.py` with path WP-RO-03 → `src/sri_calculator.py`.

1. **Collect per-industry inputs** for the 19 GICS industries: Track A score (0-10), Track B level (green/yellow/orange/red), outlook (positive/stable/negative), veto flag.
2. **Industry risk scores** — per `systemic-warning-framework.md` §2.2.1 (base bands + outlook penalty + Track B penalty; veto forces the forced score; cap per Appendix A). All rule values are parsed from the document by the engine — never restate them manually.
3. **Weights** — bond outstanding weights × contagion coefficients (§2.3.1 machine-generated from the heatmap; §4.1 illustrative structure — live runs use current benchmark sector weights; single-industry cap 25%).
4. **SRI** — Σ(industry risk score × weight); the scale is continuous 0-3+ (percentage scales are prohibited, §2.2 dimension note).
5. **Thermometer** — map to the four tiers per §3.1 (parsed from the document).
6. **Linkages** — note §10.1 M2/M4 effects (individual downgrade, concentration multiplier) and §10.2 escalation linkage; SRI output feeds the L0 signal card.

## 4. Dimension Vocabulary

- Industries: the 19 GICS industries of `contagion-matrix.md` §1.2 only.
- Signals: Track A score / Track B four levels / outlook three directions / veto — no other input types.
- Scale and tiers: §2.2 (0-3+) and §3.1 only.

## 5. Output Shape

Analysis Artifact per `dev/engine/pipeline-contract.md` §2.2.
Path outputs (registry): SRI reading + thermometer tier.

## 6. Templates

- `dev/templates/template-type15.html` — SRI Thermometer

Render via `credit-report-builder` using exactly this file; no ad-hoc thermometers.

## 7. Quality Gates (all must pass)

- `Signal Aggregation (dev/engine/systemic-warning-framework.md §2)`
- `Four-Level Thermometer (dev/engine/systemic-warning-framework.md §3)`

## 8. Drift Blacklist (forbidden)

- Hardcoding SRI thresholds, penalties, weights, or tiers anywhere (all parsed from the document at load time).
- Percentage-scale SRI (0-100) in any output — prohibited by §2.2.
- Inventing industries, weights, or adjustment factors — anything not in the engine documents is `engine_undefined`.
- Numeric claims without a `doc §section` citation.
- Designing ad-hoc HTML/thermometers/templates.
- Invoking Mode B without an explicit user-provided data source.
- Delivering before `credit-qa-verifier` issues a passing QA Verdict.
