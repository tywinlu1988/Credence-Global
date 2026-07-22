# WP-X-01 Execution Contract — Black Swan Backtest Validation

**Status**: ✅ active · **Role**: meta · **Object**: meta · **Depth**: special

> This playbook is the execution contract for WP-X-01. Read it fully before starting.
> AGENTS.md Non-Negotiables apply. Everything forbidden below is forbidden; anything
> the engine documents do not define is `engine_undefined`.

## 1. Trigger & Scope

Use when: validating the framework against historical defaults ("would the engine have caught X", "backtest the framework on case Y").
Do not use when: live analysis (→ role paths), single-issuer rating (→ WP-CS-01).

## 2. Required Reading Order

1. `dev/engine/validation-methodology.md` — backtest methodology, dual-timepoint protocol, case library

## 3. Procedure

1. **Case selection** — choose from the documented case library (`validation-methodology.md` §6: Lehman Brothers, Wirecard, Valeant, Credit Suisse, Greece) or a user-named event with the same protocol.
2. **Dual-timepoint reconstruction** — reconstruct the information state at T-event and at the earlier validation point per `validation-methodology.md` §3 (only information publicly available at each timepoint may be used — no hindsight leakage).
3. **Framework replay** — run the analysis under test (industry pyramid / dual-track / system-intelligence layer as applicable) on the T-validation information state.
4. **Verdict comparison** — compare the replay's signals/ratings against the actual outcome; record hit / early-warning-lead-time / false positives per `validation-methodology.md` §1-§3.
5. **Conclusion + improvements** — produce the validation conclusion and concrete framework improvement recommendations (with honest statements where the framework would NOT have warned).

## 4. Dimension Vocabulary

- Validation protocol vocabulary per `validation-methodology.md` §1-§4 (dual-point, forward comparison, lead time).
- Case library: `validation-methodology.md` §6 (no other "official" cases; user-named events follow the same protocol).

## 5. Output Shape

Analysis Artifact per `dev/engine/pipeline-contract.md` §2.2.
Path outputs (registry): validation conclusion + framework improvements.

## 6. Templates

- `dev/templates/template-type3.html` — Backtest Validation

Render via `credit-report-builder` using exactly this file; no ad-hoc layouts.

## 7. Quality Gates (all must pass)

- `Black Swan Back-Testing (dev/engine/validation-methodology.md §1)`
- `Dual-Timepoint (dev/engine/validation-methodology.md §3)`

## 8. Drift Blacklist (forbidden)

- Hindsight leakage (using information not public at the validation timepoint).
- Declaring success only where the framework warned; skipped negative results are mandatory content.
- Inventing thresholds, cases, or evaluation criteria — anything not in the engine documents is `engine_undefined`.
- Numeric claims without a `doc §section` citation.
- Designing ad-hoc HTML/templates.
- Invoking Mode B without an explicit user-provided data source.
- Delivering before `credit-qa-verifier` issues a passing QA Verdict.
