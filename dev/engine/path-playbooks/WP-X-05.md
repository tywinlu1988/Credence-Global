# WP-X-05 Execution Contract — Outlook & Continuous Monitoring

**Status**: ✅ active · **Role**: meta · **Object**: single-issuer · **Depth**: special

> This playbook is the execution contract for WP-X-05. Read it fully before starting.
> AGENTS.md Non-Negotiables apply. This path is **wired**: the coded engine is the
> primary executor; manual execution follows the same documents.

## 1. Trigger & Scope

Use when: a rating outlook, watchlist entry, or migration-matrix estimate is needed ("outlook for X", "put X on watch", "what's the downgrade probability").
Do not use when: current rating (→ WP-CS-01), market-wide SRI (→ WP-RO-03).

## 2. Required Reading Order

1. `dev/engine/outlook-monitoring-framework.md` — trigger factors, scoring, watchlist, migration matrix (single source for all rule values)

## 3. Procedure (coded engine)

**Primary executor**: `src/pipeline.py` with path WP-X-05 → `src/outlook_engine.py`.

1. **Signal collection** — map observed signals to the trigger factor matrix (`outlook-monitoring-framework.md` §2.2, parsed at runtime); each signal carries a pyramid layer and direction.
2. **Outlook scoring** — layer-weighted net direction per §2.3 (layer weights from the document): developing → positive → negative → stable judgment order; confidence tier per §2.3.
3. **Watchlist check** — 90-day watchlist logic per §3 (side, window, review cadence; negative takes priority on two-sided triggers).
4. **Migration range** — §5.1 base interval by current rating (BB+/BB-/B+/B- are interpolated between adjacent rows; AAA cannot upgrade; D is terminal) plus §5.3 paradigm adjustment (P1-P4 direct; P5/P6 delegated to dedicated frameworks).
5. **Output** — outlook + confidence + net score, watchlist state, migration range.

## 4. Dimension Vocabulary

- Trigger signals and layers: `outlook-monitoring-framework.md` §2.2 only.
- Outlook states: positive / stable / negative / developing (no others).
- Ratings: the 18-notch scale (`dual-track-methodology.md` §6); migration rows per §5.1 + interpolation rule.
- Paradigm adjustment: §5.3 rows only (P5/P6 delegated).

## 5. Output Shape

Analysis Artifact per `dev/engine/pipeline-contract.md` §2.2.
Path outputs (registry): rating outlook + watchlist.

## 6. Templates

- `dev/templates/template-type18.html` — Outlook Monitoring

Render via `credit-report-builder` using exactly this file; no ad-hoc layouts.

## 7. Quality Gates (all must pass)

- `Rating Outlook (dev/engine/outlook-monitoring-framework.md §2)`
- `Watchlist (dev/engine/outlook-monitoring-framework.md §3)`
- `Rating Migration Matrices (dev/engine/outlook-monitoring-framework.md §5)`

## 8. Drift Blacklist (forbidden)

- Hardcoding layer weights, thresholds, watchlist windows, or migration probabilities (all parsed from the document).
- Migration estimates for ratings outside the 18-notch scale, or AAA upgrade paths (prohibited by §2.5).
- Inventing signals, factors, or adjustment percentages — anything not in the engine documents is `engine_undefined`.
- Numeric claims without a `doc §section` citation.
- Designing ad-hoc HTML/templates.
- Invoking Mode B without an explicit user-provided data source.
- Delivering before `credit-qa-verifier` issues a passing QA Verdict.
