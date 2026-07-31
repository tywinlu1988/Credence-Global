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
1. `${CLAUDE_PLUGIN_ROOT}/engine/trader-framework.md` §§1-5 — Execution Dimensions, Track B mapping, Thermometer Overlay, Execution Decision Matrix (this path's own methodology)
2. `${CLAUDE_PLUGIN_ROOT}/engine/output-layered-framework.md` §§1-3 — L0 Signal Card specification (§3), three-tier overview; §6 — information priority sorting rules
3. `${CLAUDE_PLUGIN_ROOT}/engine/systemic-warning-framework.md` §§1-4 — SRI four-tier thermometer (§3), signal aggregation, escalation trigger definitions

**Reference (read on demand):**
- `${CLAUDE_PLUGIN_ROOT}/engine/trader-framework.md` §§6-9 — execution tactics, divergence handling, quality gates, limitations
- `${CLAUDE_PLUGIN_ROOT}/engine/output-layered-framework.md` §§4-5 — L1/L2 specs

## 3. Procedure

1. **Collect daily signals** — Gather the current day's key signals for the issuer. L0 scope is maximum 3 signals (per `output-layered-framework.md` §3 priority scoring: Urgency × Importance × Confidence > 30 qualifies for L0).
2. **Read rating + outlook** — Inherit the current issuer rating and outlook from the most recent completed analysis (WP-CS-01 or equivalent). Do not recalculate.
3. **Score Execution Dimensions** — Score the four dimensions (L0 Signal Card 35% / Real-Time Spreads 25% / Liquidity Conditions 25% / Market Context 15%) per `${CLAUDE_PLUGIN_ROOT}/engine/trader-framework.md` §2; apply the Track B input mapping (§3) and the liquidity data-gap rule (§2.4).
4. **Select Execution Decision Matrix row** — Follow the selection procedure in `${CLAUDE_PLUGIN_ROOT}/engine/trader-framework.md` §5.2: composite → signal direction → spread band → liquidity → matrix row.
5. **Read SRI thermometer + apply overlay** — Read the current systemic risk thermometer tier from `systemic-warning-framework.md` §3 (🟢 Normal <0.5 / 🟡 Watch 0.5-1.0 / 🟠 Alert 1.0-1.8 / 🔴 Danger ≥1.8; most recent WP-RO-03 reading). Apply the overlay per `${CLAUDE_PLUGIN_ROOT}/engine/trader-framework.md` §4 — Alert/Danger overrides any Buy row to "suspended".
6. **Compose L0 signal card** — Assemble per `output-layered-framework.md` §3: Rating + Outlook + max 3 key signals + completeness lamp + one-line execution posture (from step 4-5). This is a 5-second scan, not a report. Do not expand beyond the L0 boundaries — if the user needs more depth, escalate to L1 (→ WP-PM-01) or L2 (→ WP-CS-01).
7. **Link thermometer** — If the SRI tier is 🟠 or 🔴, the signal card must include the current tier and the mandated action recommendation from `systemic-warning-framework.md` §3.
8. **Output** — L0 signal card, thermometer reading, execution posture.

## 4. Dimension Vocabulary

- L0 dimensions: Rating, Outlook, 3 signals max per `output-layered-framework.md` §3.
- Execution Dimensions: L0 Signal Card 35% / Real-Time Spreads 25% / Liquidity Conditions 25% / Market Context 15% per `${CLAUDE_PLUGIN_ROOT}/engine/trader-framework.md` §2 only.
- Spread bands: Cheap > FV+10bp / Fair ±10bp / Rich < FV−10bp per `${CLAUDE_PLUGIN_ROOT}/engine/trader-framework.md` §2.3 only.
- Execution posture: one line, from the Execution Decision Matrix (`${CLAUDE_PLUGIN_ROOT}/engine/trader-framework.md` §5) after the §4 thermometer overlay.
- Signal priority scoring: Urgency (1-5) × Importance (1-5) × Confidence (1-5) range 1-125 per §6.
- SRI thermometer tiers: 🟢/🟡/🟠/🔴 with ranges per `systemic-warning-framework.md` §3 only.
- Paradigm/router: if issuer paradigm is unknown, route through `credit-analysis-router` first.

## 5. Output Shape

Analysis Artifact per `${CLAUDE_PLUGIN_ROOT}/engine/pipeline-contract.md` §2.2 (L0 — lightest artifact, signals-only).
Path outputs (registry): L0 signal card, thermometer reading, execution posture.
Template: L0 signal card has no standalone .html file; its specification is defined in `output-layered-framework.md` §3. The signal card is a structured text block, not an HTML page.

## 6. Templates

- `"L0-spec: ${CLAUDE_PLUGIN_ROOT}/engine/output-layered-framework.md §3"` — L0 Signal Card (specification-defined, no standalone .html file)

Do not fabricate an HTML template for the L0 signal card. Deliver as a structured text block per the specification.

## 7. Quality Gates (all must pass)

- `L0 Signal Card (${CLAUDE_PLUGIN_ROOT}/engine/output-layered-framework.md §3)`
- `Thermometer (${CLAUDE_PLUGIN_ROOT}/engine/systemic-warning-framework.md §3)`
- `Execution Dimensions (${CLAUDE_PLUGIN_ROOT}/engine/trader-framework.md §2)`
- `Execution Decision Matrix (${CLAUDE_PLUGIN_ROOT}/engine/trader-framework.md §5)`

## 8. Drift Blacklist (forbidden)

- Expanding the L0 signal card beyond its 5-second scope (no L1 radar charts, no L2 deep-dive panels); the execution posture is one line, not a trade plan.
- Emitting more than 3 key signals on the L0 card (per priority scoring floor of >30).
- Inventing execution thresholds, weights, or matrix rows not defined in `${CLAUDE_PLUGIN_ROOT}/engine/trader-framework.md`.
- Fabricating liquidity, spread, or market-depth data — missing data triggers the data-gap rule (`${CLAUDE_PLUGIN_ROOT}/engine/trader-framework.md` §2.4), never assumed values; Mode B guardrail applies (`mosaic-engine.md` §6).
- Issuing trading advice instead of an analytical execution posture (`${CLAUDE_PLUGIN_ROOT}/engine/trader-framework.md` §9 posture).
- Inventing a standalone HTML template for the L0 signal card (the spec is `output-layered-framework.md` §3, not a .html file).
- Fabricating SRI readings or thermometer tier values — the SRI is computed by `src/sri_calculator.py` from the monthly WP-RO-03 run.
- Assigning thermometer-tier action recommendations that don't appear in `systemic-warning-framework.md` §3.
- Numeric claims without a `doc §section` citation.
- Delivering before `credit-qa-verifier` issues a passing QA Verdict.
