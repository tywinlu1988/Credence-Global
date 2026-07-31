# WP-TR-01 Execution Contract — Trader Market Watch Signal Card

**Status**: ✅ active · **Role**: trader · **Object**: single-issuer · **Depth**: L0

> This playbook is the execution contract for WP-TR-01. Read it fully before starting.
> AGENTS.md Non-Negotiables apply. This path is the lightest-weight output in the system:
> a 5-second L0 signal card linked to the SRI systemic-warning thermometer.

## 1. Trigger & Scope

Use when: the user needs a fast market-watch signal ("daily alert for this bond", "intraday warning check", "what's the signal card for X today", "is this bond flashing red").
Do not use when: full credit analysis (→ WP-CS-01), portfolio dashboard (→ WP-PM-01), systemic risk reading for the whole market (→ WP-RO-03), outlook monitoring over weeks (→ WP-X-05).

## 2. Required Reading Order

**Must read (core rules):**
1. `${CLAUDE_PLUGIN_ROOT}/engine/output-layered-framework.md` §§1-3 — L0 Signal Card specification (§3), three-tier overview; §6 — information priority sorting rules
2. `${CLAUDE_PLUGIN_ROOT}/engine/systemic-warning-framework.md` §§1-4 — SRI four-tier thermometer (§3), signal aggregation, escalation trigger definitions

**Reference (read on demand):**
- `${CLAUDE_PLUGIN_ROOT}/engine/output-layered-framework.md` §§4-5, §§7-10 — L1/L2 specs, workflow embedding, integration notes
- `${CLAUDE_PLUGIN_ROOT}/engine/systemic-warning-framework.md` §§5-12 — backtests, worked example, sensitivity analysis

## 3. Procedure

1. **Collect daily signals** — Gather the current day's key signals for the issuer. L0 scope is maximum 3 signals (per `output-layered-framework.md` §3 priority scoring: Urgency × Importance × Confidence > 30 qualifies for L0).
2. **Read rating + outlook** — Inherit the current issuer rating and outlook from the most recent completed analysis (WP-CS-01 or equivalent). Do not recalculate.
3. **Read SRI thermometer** — Read the current systemic risk thermometer tier from `systemic-warning-framework.md` §3 (🟢 Normal <0.5 / 🟡 Watch 0.5-1.0 / 🟠 Alert 1.0-1.8 / 🔴 Danger ≥1.8). Use the most recent SRI reading (WP-RO-03 monthly or event-driven re-run).
4. **Compose L0 signal card** — Assemble per `output-layered-framework.md` §3: Rating + Outlook + max 3 key signals + completeness lamp. This is a 5-second scan, not a report. Do not expand beyond the L0 boundaries — if the user needs more depth, escalate to L1 (→ WP-PM-01) or L2 (→ WP-CS-01).
5. **Link thermometer** — If the SRI tier is 🟠 or 🔴, the signal card must include the current tier and the mandated action recommendation from `systemic-warning-framework.md` §3.
6. **Output** — L0 signal card, thermometer reading.

## 4. Dimension Vocabulary

- L0 dimensions: Rating, Outlook, 3 signals max per `output-layered-framework.md` §3.
- Signal priority scoring: Urgency (1-5) × Importance (1-5) × Confidence (1-5) range 1-125 per §6.
- SRI thermometer tiers: 🟢/🟡/🟠/🔴 with ranges per `systemic-warning-framework.md` §3 only.
- Paradigm/router: if issuer paradigm is unknown, route through `credit-analysis-router` first.

## 5. Output Shape

Analysis Artifact per `${CLAUDE_PLUGIN_ROOT}/engine/pipeline-contract.md` §2.2 (L0 — lightest artifact, signals-only).
Path outputs (registry): L0 signal card, thermometer reading.
Template: L0 signal card has no standalone .html file; its specification is defined in `output-layered-framework.md` §3. The signal card is a structured text block, not an HTML page.

## 6. Templates

- `"L0-spec: ${CLAUDE_PLUGIN_ROOT}/engine/output-layered-framework.md §3"` — L0 Signal Card (specification-defined, no standalone .html file)

Do not fabricate an HTML template for the L0 signal card. Deliver as a structured text block per the specification.

## 7. Quality Gates (all must pass)

- `L0 Signal Card (${CLAUDE_PLUGIN_ROOT}/engine/output-layered-framework.md §3)`
- `Thermometer (${CLAUDE_PLUGIN_ROOT}/engine/systemic-warning-framework.md §3)`

## 8. Drift Blacklist (forbidden)

- Expanding the L0 signal card beyond its 5-second scope (no L1 radar charts, no L2 deep-dive panels).
- Emitting more than 3 key signals on the L0 card (per priority scoring floor of >30).
- Inventing a standalone HTML template for the L0 signal card (the spec is `output-layered-framework.md` §3, not a .html file).
- Fabricating SRI readings or thermometer tier values — the SRI is computed by `src/sri_calculator.py` from the monthly WP-RO-03 run.
- Assigning thermometer-tier action recommendations that don't appear in `systemic-warning-framework.md` §3.
- Numeric claims without a `doc §section` citation.
- Delivering before `credit-qa-verifier` issues a passing QA Verdict.
