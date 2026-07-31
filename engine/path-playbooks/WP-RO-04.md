# WP-RO-04 Execution Contract — Portfolio Stress Test

**Status**: ✅ active · **Role**: risk-officer · **Object**: portfolio · **Depth**: special

> This playbook is the execution contract for WP-RO-04. Read it fully before starting.
> AGENTS.md Non-Negotiables apply. This path applies stress scenarios to a portfolio;
> it requires a completed concentration assessment (WP-RO-01) as input.

## 1. Trigger & Scope

Use when: the user needs stress-testing of a portfolio ("stress test this portfolio under a recession", "what happens to these holdings if spreads widen 200bp", "extreme scenario loss estimate").
Do not use when: baseline concentration assessment (→ WP-RO-01 first), systemic risk reading (→ WP-RO-03), single-issuer analysis (→ WP-CS-01).

## 2. Required Reading Order

**Must read (core rules):**
1. `${CLAUDE_PLUGIN_ROOT}/engine/concentration-framework.md` §9 — stress scenario definitions; §§7-8 — five-dimension thresholds as stress inputs
2. `${CLAUDE_PLUGIN_ROOT}/engine/financial-deep-dive.md` §§A-D — core financial methodology; §E — scenario sensitivity matrix, stress effects on financial statements

**Reference (read on demand):**
- `${CLAUDE_PLUGIN_ROOT}/engine/concentration-framework.md` §§2-6, §§10-11 — dimension details, integration notes
- `${CLAUDE_PLUGIN_ROOT}/engine/financial-deep-dive.md` §§F-G — worked examples and derivations

## 3. Procedure

1. **Verify prerequisite** — WP-RO-01 concentration assessment must be complete. The stress test uses the portfolio's current five-dimension concentration profile as its baseline.
2. **Define stress scenarios** — Per `concentration-framework.md` §9, construct stress scenarios by selecting threshold-jump parameters for each of the five dimensions (industry concentration CR3/HHI jump, regional exposure shock, rating migration shock, maturity concentration spike, funding channel freeze). At least 2 scenarios: a moderate scenario and a severe scenario.
3. **Apply scenario jumps** — For each scenario, apply the threshold-jump rules to the portfolio's baseline scores. Each dimension's post-jump score is computed per the interpolation rules in §1.3; the jumped scores feed the composite per §8.2.
4. **Financial sensitivity overlay** — Per `financial-deep-dive.md` §E, apply the scenario sensitivity matrix to the portfolio's holdings: for each issuer, assess how the stress scenario affects its key financial ratios (leverage, coverage, liquidity). Aggregate issuer-level stress effects to portfolio-level loss estimates.
5. **Loss estimation** — Compute: (a) stressed composite concentration score, (b) stressed rating adjustments per §7.2 stacking, (c) issuer-level financial impact aggregated to portfolio estimated loss, (d) BB-cap re-check under stressed conditions.
6. **Output** — stress scenario loss, threshold jump results for each scenario.

## 4. Dimension Vocabulary

- Five concentration dimensions: industry / region / rating / maturity / funding channel per `concentration-framework.md` §2-§6.
- Threshold bands and interpolation: per §1.3.
- Stress scenario parameters: per §9 — threshold jumps, not invented shock values.
- Financial sensitivity: per `financial-deep-dive.md` §E — ratio impact definitions, not invented multipliers.

## 5. Output Shape

Analysis Artifact per `${CLAUDE_PLUGIN_ROOT}/engine/pipeline-contract.md` §2.2 (multi-scenario, with per-scenario findings arrays).
Path outputs (registry): stress scenario loss, threshold jump results.

## 6. Templates

- `${CLAUDE_PLUGIN_ROOT}/templates/template-type11.html` — Stress Test

Render via `credit-report-builder` using exactly this file; no ad-hoc stress layouts.

## 7. Quality Gates (all must pass)

- `Stress Test (${CLAUDE_PLUGIN_ROOT}/engine/concentration-framework.md §9)`
- `Scenario Sensitivity (${CLAUDE_PLUGIN_ROOT}/engine/financial-deep-dive.md §E)`

## 8. Drift Blacklist (forbidden)

- Running stress test without a completed WP-RO-01 concentration baseline.
- Single-scenario only — at least a moderate and a severe scenario are required.
- Inventing stress parameters (shock magnitudes, threshold jumps) not defined in `concentration-framework.md` §9.
- Fabricating issuer-level financial ratio sensitivities not defined in `financial-deep-dive.md` §E.
- Extending the scenario impact to dimensions outside the five in `concentration-framework.md`.
- Numeric claims without a `doc §section` citation.
- Designing ad-hoc HTML/dashboards/templates.
- Invoking Mode B without an explicit user-provided data source.
- Delivering before `credit-qa-verifier` issues a passing QA Verdict.
