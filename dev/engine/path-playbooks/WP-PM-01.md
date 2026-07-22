# WP-PM-01 Execution Contract — Investment Dashboard

**Status**: ✅ active · **Role**: portfolio-manager · **Object**: single-issuer · **Depth**: L2

> This playbook is the execution contract for WP-PM-01. Read it fully before starting.
> AGENTS.md Non-Negotiables apply. Everything forbidden below is forbidden; anything
> the engine documents do not define is `engine_undefined`.

## 1. Trigger & Scope

Use when: evaluating a single bond's investment merit ("is this bond worth buying", "cheap or expensive", dashboard for instrument X).
Do not use when: issuer-level rating only (→ WP-CS-01), two-issuer comparison (→ WP-PM-02), portfolio-level risk (→ WP-RO-*).

## 2. Required Reading Order

1. `dev/engine/multi-stakeholder.md` — §2.2b Single-Instrument Dashboard (this path's definition) and §2.2 Portfolio Construction Assessment (distinct lens, do not conflate)
2. `dev/engine/dual-track-methodology.md` — Track A/B foundations for relative value
3. `dev/engine/mosaic-engine.md` — completeness and density rules

## 3. Procedure

1. **Confirm the framework** — use the Single-Instrument Dashboard four-dimension definition (`multi-stakeholder.md` §2.2b): Relative Value 30% / Covenant Protection 25% / Liquidity 20% / Event Calendar 25%. The §2.2 Portfolio-Construction Assessment is a different lens and is NOT this path.
2. **Relative Value (30%)** — YTM, conversion premium, Z-spread (if available), same-industry peer comparison, same-rating comparison (`multi-stakeholder.md` §2.2b metric anchors; spread context per `dual-track-methodology.md`).
3. **Covenant Protection (25%)** — adjustment history, put triggers, cross-default clauses, redemption terms, guarantee/collateral structure (§2.2b).
4. **Liquidity (20%)** — daily volume, turnover, abnormal volume events, bid-ask spread (if available), pledgeability (§2.2b).
5. **Event Calendar (25%)** — next 3 months of macro/industry/issuer events and covenant triggers (§2.2b).
6. **Completeness report** — signal density per dimension per `mosaic-engine.md` §4.3; sub-floor dimensions are `insufficient information to evaluate`.
7. **Dashboard assembly** — integrated ranking + individual bond assessment + data gap report.

## 4. Dimension Vocabulary

- Four dimensions exactly as `multi-stakeholder.md` §2.2b (no additional dimensions, no weight changes).
- Completeness/density vocabulary per `mosaic-engine.md` §4.3.

## 5. Output Shape

Analysis Artifact per `dev/engine/pipeline-contract.md` §2.2 (findings: four-dimension scores + investment recommendation; completeness; mode_b_gaps).
Path outputs (registry): four-dimension score + investment recommendation.

## 6. Templates

- `dev/templates/template-type5.html` — PM Dashboard

Render via `credit-report-builder` using exactly this file; no ad-hoc dashboards.

## 7. Quality Gates (all must pass)

- `Four-Dimension (dev/engine/multi-stakeholder.md §2)`
- `Relative Value (dev/engine/multi-stakeholder.md §2.2)`

## 8. Drift Blacklist (forbidden)

- Designing ad-hoc HTML/dashboards/templates (template comes from §6 only).
- Conflating this path with the §2.2 Portfolio-Construction Assessment dimensions (Sector Allocation Fit / Curve Positioning).
- Inventing dimensions, metrics, thresholds, or weights — anything not in the engine documents is `engine_undefined`.
- Numeric claims without a `doc §section` citation.
- Invoking Mode B without an explicit user-provided data source.
- Delivering before `credit-qa-verifier` issues a passing QA Verdict.
