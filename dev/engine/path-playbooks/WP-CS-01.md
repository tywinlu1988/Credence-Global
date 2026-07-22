# WP-CS-01 Execution Contract — Single-Issuer Rating

**Status**: ✅ active · **Role**: credit-selector · **Object**: single-issuer · **Depth**: L2

> This playbook is the execution contract for WP-CS-01. Read it fully before starting.
> AGENTS.md Non-Negotiables apply. Everything forbidden below is forbidden; anything
> the engine documents do not define is `engine_undefined`.

## 1. Trigger & Scope

Use when: a single issuer needs a credit rating ("analyze company X", "can we lend to X", "rate this issuer").
Do not use when: portfolio-level questions (→ WP-RO-*), instrument-level investment questions (→ WP-PM-01), multi-role comparisons (→ WP-X-02).

## 2. Required Reading Order

1. `dev/engine/industry-framework.md` — paradigm determination, pyramid, veto
2. `dev/engine/mosaic-engine.md` — signal extraction, completeness, density rules
3. `dev/engine/dual-track-methodology.md` — Track A/B, cross-validation, rating mapping

## 3. Procedure

1. **Paradigm determination** — assign the issuer's industry to exactly one paradigm (P1-P6) per `industry-framework.md` §3 (GICS mapping §3.1, bridge §3.1a, decision tree §3.2, conflict resolution §3.3, special structures §3.4).
2. **Ten-dimension scoring** — score D1-D10 (1-5 each) per `industry-framework.md` §1 definitions; use the paradigm's weight template (`industry-framework.md` §2.1-§2.6).
3. **Pyramid scoring** — apply the paradigm's four-layer pyramid L1→L4 in order (no layer skipping; the financial layer validates upper layers). Special structures use §4.4 (e.g., semiconductors five-layer).
4. **Mosaic completeness** — assemble public-data signals and compute per-dimension signal density per `mosaic-engine.md` §4.3 (density floors are mandatory; sub-floor dimensions are `insufficient information to evaluate`).
5. **Track B market signals** — evaluate the four signal tiers per `dual-track-methodology.md` (credit spreads / volatility / fund flows / rating migration).
6. **Cross-validation** — place Track A vs Track B in the four-quadrant matrix per `dual-track-methodology.md` §4; on conflict, Track A takes priority.
7. **Veto check** — evaluate one-vote veto conditions per `industry-framework.md` §5; when triggered, lock the composite ceiling at CCC.
8. **Rating mapping** — map the composite score to the 18-notch scale per `dual-track-methodology.md` §6 (higher score = higher rating). Never invent notches.
9. **Completeness report** — attach the completeness score and explicit gap list per `mosaic-engine.md` §5 (mandatory output).

## 4. Dimension Vocabulary

- Paradigms: P1-P6 only (`industry-framework.md` §2) — no other industry types.
- Dimensions: D1-D10 only (`industry-framework.md` §1).
- Layers: L1-L4 per the paradigm's pyramid (§4.4 five-layer for special structures).
- Track B tiers: the four tiers in `dual-track-methodology.md` only.
- Rating notches: the 18-notch scale (`dual-track-methodology.md` §6) only.

## 5. Output Shape

Analysis Artifact per `dev/engine/pipeline-contract.md` §2.2, carrying: path_id (unchanged), mode, findings (rating + outlook + signals), completeness (score + gap list), veto, system_readouts, mode_b_gaps.
Path outputs (registry): rating + signals, completeness report.

## 6. Templates

- `dev/templates/template-type1.html` — Single-Issuer Deep Dive
- `dev/templates/template-type6.html` — Rating Summary Card

Render via `credit-report-builder` using exactly these files; no ad-hoc layouts.

## 7. Quality Gates (all must pass)

- `Signal Density (dev/engine/mosaic-engine.md §4.3)`
- `Veto (dev/engine/industry-framework.md §5)`
- `Cross-Validation (dev/engine/dual-track-methodology.md §4)`

## 8. Drift Blacklist (forbidden)

- Designing ad-hoc HTML/dashboards/templates (templates come from §6 only).
- Inventing dimensions, metrics, industries, paradigms, thresholds, weights, or rating notches — anything not in the engine documents is `engine_undefined`.
- Numeric claims without a `doc §section` citation.
- Skipping the completeness report or reporting density-violating scores.
- Invoking Mode B without an explicit user-provided data source.
- Delivering before `credit-qa-verifier` issues a passing QA Verdict.
