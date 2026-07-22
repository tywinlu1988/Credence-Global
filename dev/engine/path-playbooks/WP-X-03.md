# WP-X-03 Execution Contract — Industry Framework Builder

**Status**: ✅ active · **Role**: meta · **Object**: industry · **Depth**: special

> This playbook is the execution contract for WP-X-03. Read it fully before starting.
> AGENTS.md Non-Negotiables apply. Everything forbidden below is forbidden; anything
> the engine documents do not define is `engine_undefined`.

## 1. Trigger & Scope

Use when: building an industry analysis framework for a new/unfamiliar industry ("build the pyramid for industry X", "how should I analyze X sector").
Do not use when: the industry already maps to a registered paradigm and matrix industry (→ use its paradigm pyramid directly, WP-CS-01).

## 2. Required Reading Order

1. `dev/engine/industry-framework.md` — D1-D10, paradigms, determination logic, pyramids, veto
2. `dev/engine/dimension-registry.md` — paradigm/role pointer index
3. `dev/engine/mosaic-engine.md` — completeness and density rules

## 3. Procedure

1. **Ten-dimension profile** — score the industry's D1-D10 (1-5 each) per `industry-framework.md` §1 definitions, with evidence per dimension (public data only; gaps recorded).
2. **Paradigm determination** — assign exactly one paradigm per `industry-framework.md` §3 (mapping §3.1, bridge §3.1a, decision tree §3.2, conflict rules §3.3); if the industry fits none, document the special-structure reasoning per §3.4 rather than inventing a seventh paradigm.
3. **Pyramid construction** — derive the four-layer pyramid (weights + key indicators per layer) from the chosen paradigm's template (`industry-framework.md` §2.1-§2.6 and §4); special structures follow §4.4's five-layer pattern.
4. **Veto definition** — identify paradigm-specific one-vote veto candidates per `industry-framework.md` §5 (only conditions consistent with the paradigm's logic).
5. **Completeness statement** — signal density and gap list per `mosaic-engine.md` §4.3 (the framework must state which dimensions cannot yet be evidenced).
6. **Output** — industry pyramid + D1-D10 scores + determination rationale + completeness report.

## 4. Dimension Vocabulary

- Dimensions: D1-D10 only (`industry-framework.md` §1).
- Paradigms: P1-P6 only (`industry-framework.md` §2) — never invent a seventh.
- Layers: L1-L4 (L5 for special structures, §4.4).

## 5. Output Shape

Analysis Artifact per `dev/engine/pipeline-contract.md` §2.2.
Path outputs (registry): industry pyramid + D1-D10 scores.

## 6. Templates

- `dev/templates/template-type7.html` — Industry Framework

Render via `credit-report-builder` using exactly this file; no ad-hoc layouts.

## 7. Quality Gates (all must pass)

- `Ten-Dimension (dev/engine/industry-framework.md §1)`
- `Pyramid (dev/engine/industry-framework.md §4)`
- `Veto (dev/engine/industry-framework.md §5)`

## 8. Drift Blacklist (forbidden)

- Inventing dimensions, paradigms, layer weights, or veto conditions — anything not in the engine documents is `engine_undefined`.
- Force-fitting an industry into a paradigm without applying §3's determination logic and recording the rationale.
- Numeric claims without a `doc §section` citation.
- Designing ad-hoc HTML/templates.
- Invoking Mode B without an explicit user-provided data source.
- Delivering before `credit-qa-verifier` issues a passing QA Verdict.
