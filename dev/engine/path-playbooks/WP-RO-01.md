# WP-RO-01 Execution Contract — Concentration Assessment

**Status**: ✅ active · **Role**: risk-officer · **Object**: portfolio · **Depth**: special

> This playbook is the execution contract for WP-RO-01. Read it fully before starting.
> AGENTS.md Non-Negotiables apply. This path is **wired**: the coded engine is the
> primary executor; manual execution follows the same documents.

## 1. Trigger & Scope

Use when: a portfolio's concentration risk needs assessment ("is this portfolio too concentrated", "five-dimension concentration check").
Do not use when: single-issuer rating (→ WP-CS-01), cross-industry transmission (→ WP-RO-02), market-wide systemic level (→ WP-RO-03), stress scenarios (→ WP-RO-04).

## 2. Required Reading Order

1. `dev/engine/concentration-framework.md` — the entire definition of this path

## 3. Procedure (coded engine)

**Primary executor**: `src/pipeline.py` with path WP-RO-01 → `src/concentration_scorer.py`.

1. **Collect metrics** for the portfolio: HHI / CR3 / CR5 / MAX1; single country-region & weak-region shares; AAA & pseudo-high-rating shares; 12-month maturity share & single-month peak; top channel share (+ §6.3 typed indicators and §7.3 conjunct inputs where relevant).
2. **Score five dimensions** — each raw metric maps via §1.3 linear interpolation within its threshold bands (industry §2.2 / region §3 / rating §4 / maturity §5 / channel §6); worst metric governs per dimension.
3. **Channel synergy** — apply §6.3 typed rules only (bond >70% + cancellation >15% → +2; non-standard >50% + decline >20% → +3; bank >70% + credit growth <8% → +1; diversified → −1).
4. **Composite score** — §8.2 default weights (industry 25 / region 20 / rating 20 / maturity 20 / channel 15).
5. **Rating adjustment** — §7.2 non-linear stacking from the five traffic-light levels; 5×🟠 → systemic risk alert (individual adjustment not applicable).
6. **BB-cap check** — §7.3 five conditions exactly as documented (no extra triggers): 3+ 🔴; single industry >50% AND down-cycle AND super-spreader; weak region >35% AND SOE default in region within 12 months; pseudo-high >40%; 12-month maturity >70% AND channel dependency >70%; single channel >90% AND freezing.
7. **Output** — score, adjustment, levels, bb_cap_triggered, systemic_risk_alert + adjustment recommendations.

## 4. Dimension Vocabulary

- Five dimensions only (industry / region / rating / maturity / funding channel) with metrics per `concentration-framework.md` §2-§6.
- Threshold bands, stacking values, BB-cap conditions, and weights only per that document (drift-guarded by tests/test_concentration_doc_drift.py).

## 5. Output Shape

Analysis Artifact per `dev/engine/pipeline-contract.md` §2.2.
Path outputs (registry): five-dimension concentration score + adjustment recommendations.

## 6. Templates

- `dev/templates/template-type14.html` — Concentration Dashboard

Render via `credit-report-builder` using exactly this file; no ad-hoc dashboards.

## 7. Quality Gates (all must pass)

- `Five-Dimensional Concentration (dev/engine/concentration-framework.md §1)`
- `Threshold System (dev/engine/concentration-framework.md §2)`

## 8. Drift Blacklist (forbidden)

- Extra BB-cap triggers beyond §7.3's five conditions, or loosening the conjuncts (e.g., single industry alone).
- Representative-value scoring instead of §1.3 interpolation.
- Inventing dimensions, metrics, thresholds, or weights — anything not in the engine documents is `engine_undefined`.
- Numeric claims without a `doc §section` citation.
- Designing ad-hoc HTML/dashboards/templates.
- Invoking Mode B without an explicit user-provided data source.
- Delivering before `credit-qa-verifier` issues a passing QA Verdict.
