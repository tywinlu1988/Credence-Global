# WP-X-02 Execution Contract — Multi-Role Parallel Assessment

**Status**: ✅ active · **Role**: meta · **Object**: single-issuer · **Depth**: L2

> This playbook is the execution contract for WP-X-02. Read it fully before starting.
> AGENTS.md Non-Negotiables apply. Everything forbidden below is forbidden; anything
> the engine documents do not define is `engine_undefined`.

## 1. Trigger & Scope

Use when: one subject should be assessed from several buy-side roles in parallel ("compare the credit-selector and risk-officer views on X", "multi-role matrix").
Do not use when: a single-role answer suffices (→ the role's own path), portfolio-level risk (→ WP-RO-*).

## 2. Required Reading Order

1. `dev/engine/multi-stakeholder.md` — role definitions (§1), role deep-dives (§2), cross-role matrix (§3), five-step parallel process (§4)
2. `dev/engine/industry-framework.md` — per-role underlying analysis basis
3. `dev/engine/mosaic-engine.md` — completeness and density rules

## 3. Procedure

Follow the five-step parallel process (`multi-stakeholder.md` §4.1):

1. **Shared Data Inventory (SDI)** — one agreed data set with completeness states per dimension; every role works from the same inventory and the same gap list.
2. **Parallel role assessments** — run each requested role using its §2 deep-dive framework (Credit Selector §2.1 / Portfolio Manager §2.2-§2.2b / Risk Officer §2.3 / Trader §2.4 / Advisor §2.5 / Individual Investor §2.6). Each role uses only its own decision logic and horizon.
3. **Cross-role matrix** — build the consensus/divergence matrix per `multi-stakeholder.md` §3 (pairwise tensions; consensus reinforces, divergence triggers deeper investigation).
4. **Divergence handling** — per §3.2: name the divergent dimensions explicitly, identify which role's blind spot each divergence compensates (divergence is not a bug).
5. **Output** — multi-role score matrix + consensus/divergence report + shared completeness report.

## 4. Dimension Vocabulary

- Roles: the six roles of `multi-stakeholder.md` §1 only (no other personas).
- Per-role frameworks: §2.1-§2.6 (PM has two distinct four-dimensions: §2.2 construction assessment vs §2.2b instrument dashboard — name which one is used).
- Matrix semantics: `multi-stakeholder.md` §3 only.

## 5. Output Shape

Analysis Artifact per `dev/engine/pipeline-contract.md` §2.2.
Path outputs (registry): multi-role score matrix + consensus/divergence report.

## 6. Templates

- `dev/templates/template-type4.html` — Multi-Role Matrix

Render via `credit-report-builder` using exactly this file; no ad-hoc matrices.

## 7. Quality Gates (all must pass)

- `Multi-Role Parallel (dev/engine/multi-stakeholder.md §4)`
- `Cross-Role Comparison (dev/engine/multi-stakeholder.md §3)`

## 8. Drift Blacklist (forbidden)

- Inventing roles, role logics, or matrix dimensions — anything not in the engine documents is `engine_undefined`.
- Letting roles use different data inventories (SDI is mandatory).
- Conflating the two PM four-dimension frameworks without naming which is used.
- Numeric claims without a `doc §section` citation.
- Designing ad-hoc HTML/matrices/templates.
- Invoking Mode B without an explicit user-provided data source.
- Delivering before `credit-qa-verifier` issues a passing QA Verdict.
