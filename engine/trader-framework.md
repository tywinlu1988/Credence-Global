# Trader Execution Framework

**Version**: v0.3.1 | **Date**: 2026-07-31 | **Status**: Published

**Module**: Fixed Income Credit Analysis Engine · Multi-Stakeholder Layer

---

> This document is the single source of truth for WP-TR-01 (Trader Market Watch Signal Card)
> execution methodology. It defines how the Trader converts analytical signals into an
> execution posture — execution dimensions, spread-vs-fair-value bands, liquidity tiers,
> thermometer overlay, and the Execution Decision Matrix. All thresholds, weights, and
> decision rules in this document are the canonical reference; downstream skills and
> playbooks reference them by section number.

---

> **Reading guide**: §§1-5 contain the executable methodology — dimensions,
> weights, scoring rules, thermometer overlay, and the Execution Decision Matrix.
> These sections are required reading before executing WP-TR-01.
> §§6-7 contain execution tactics and divergence handling — read when
> constructing the trade plan. §§8-9 contain quality gates and limitations —
> read before delivery.


## Table of Contents

- [1. Positioning in the Engine](#1-positioning-in-the-engine)
- [2. Execution Dimensions](#2-execution-dimensions)
- [3. Track B Signal Input Mapping](#3-track-b-signal-input-mapping)
- [4. Thermometer Overlay](#4-thermometer-overlay)
- [5. Execution Decision Matrix](#5-execution-decision-matrix)
- [6. Execution Tactics](#6-execution-tactics)
- [7. Divergence Handling](#7-divergence-handling)
- [8. Quality Gates](#8-quality-gates)
- [9. Integration and Limitations](#9-integration-and-limitations)

---

## 1. Positioning in the Engine

### 1.1 Role

The Trader asks: *"Given the engine's signals, is today the right day to act — and how?"*
It is the shortest-horizon role in the engine (intraday to 2 weeks). The Trader does not
re-rate credits and does not construct portfolios; it converts completed analysis
(a WP-CS-01 rating, the L0 signal stream, the SRI thermometer) into an **execution
posture** — a one-line actionable statement embedded in the L0 signal card.

### 1.2 Relationship to Other Paths

| Path | Relationship |
|---|---|
| WP-CS-01 (Single-Issuer Rating) | **Prerequisite** — the Trader inherits the current rating + outlook; never recalculates |
| WP-RO-03 (SRI Reading) | **Input** — the current thermometer tier drives the §4 overlay |
| WP-PM-01 (Investment Dashboard) | Escalation target — when L0 shows a red high-priority signal, escalate to L1 depth |
| WP-X-02 (Multi-Role Parallel) | Trader posture is one of six role outputs; divergences resolved per §7 |
| WP-AD-01 / WP-II-01 | Sibling role frameworks (origination / financing channel) — independent, no data flow |

### 1.3 Elevation Declaration

The Trader assessment framework previously lived in `multi-stakeholder.md` as a role
deep-dive. **The following are elevated to this document as the single source of truth:**
- §2.4 four-dimension weights (35/25/25/15) → this document §2
- §2.4 Execution Decision Matrix (±10bp fair-value bands) → this document §5
- §5.4 alert thresholds (z-score > 2, liquidity < 20th percentile, bid-ask > 3x normal)
  → this document §§2.3-2.4

`multi-stakeholder.md` retains the role-definition summary (horizon, constraints,
tension matrix). In case of any discrepancy, **this document takes precedence** for
execution methodology.

---

## 2. Execution Dimensions

### 2.1 Four Dimensions and Weights

Every execution assessment scores four dimensions. Each dimension is scored 1-10;
the weighted composite determines the base execution posture before the §4 overlay.

| Dimension | Weight | Key Question |
|---|---|---|
| **L0 Signal Card** | 35% | What is the engine's current signal? Buy/sell/hold, with what conviction? |
| **Real-Time Spreads** | 25% | Are current spreads favorable relative to fair value and recent history? |
| **Liquidity Conditions** | 25% | Can the trade be executed without moving the market? Estimated slippage? |
| **Market Context** | 15% | Do macro events, news flow, or technical factors create favorable windows? |

### 2.2 L0 Signal Card Input

The L0 card (specification: `output-layered-framework.md` §3) provides the signal set.
Map to a dimension score:

| Card State | Score | Notes |
|---|---|---|
| Red signal(s) present (priority > 100, veto-class) | 1-3 | Direction depends on signal polarity (sell-side red = 1-3 for buying posture) |
| 1-3 qualifying signals (priority > 30) | 4-7 | Score by net signal direction and conviction |
| Silent card (no qualifying signals) | 5 | Neutral by design — "nothing is happening" is a valid input |
| Completeness lamp red (severely lacking data) | cap at 4 | Low-confidence input; do not score above 4 regardless of signals |

### 2.3 Real-Time Spreads

Compare the current spread against the fair-value (FV) estimate from the most recent
WP-PM-01 / WP-CS-01 analysis:

| Band | Definition | Score |
|---|---|---|
| **Cheap** | spread > FV + 10bp | 7-10 (attractive entry for buyers) |
| **Fair** | within FV ± 10bp | 4-6 |
| **Rich** | spread < FV − 10bp | 1-3 (attractive exit for sellers) |

**Opportunity flag**: when the spread deviates from FV by more than 2 z-scores
(20-trading-day window), flag the card — this is a highlight condition, not an
automatic trade trigger.

### 2.4 Liquidity Conditions

| Condition | Rule | Score Impact |
|---|---|---|
| Liquidity score < 20th percentile (of the bond's own 1-year history) | **Limit orders only** | cap at 4 |
| Bid-ask spread > 3x normal | **Reduce order size** | deduct 2 |
| Normal conditions | No constraint | 5-10 by depth assessment |

**Data-gap rule**: if liquidity data is unavailable, the absence itself is a signal
(mosaic-engine posture). Score the dimension at the cautious end (3), declare the gap
explicitly in the card, and apply the limit-orders-only constraint.

### 2.5 Market Context

Score from event calendar and technical factors: macro releases within 24h (central
bank decisions, CPI, payrolls), issuer news flow, sector rotation, and the §3 Track B
mapping. Event-imminent conditions cap the score at 5 (wait for the event rather than
trade into binary risk).

---

## 3. Track B Signal Input Mapping

Track B market pricing signals (four-tier system: Calm / Watch / Abnormal / Crisis —
definitions and thresholds at `dual-track-methodology.md` §3, single source of truth,
not restated here) feed the execution dimensions as follows:

| Track B Signal | Feeds Dimension | Mapping |
|---|---|---|
| Credit Spread tier | §2.3 Real-Time Spreads | Tier qualifies the FV band reading: Abnormal/Crisis widening overrides a "Cheap" band to "distressed, not cheap" |
| Volatility tier | §2.5 Market Context | Abnormal/Crisis volatility caps Market Context at 3 |
| Fund Flows tier | §2.5 Market Context | Accelerating outflow deducts 2 from Market Context |
| Rating Events tier | §2.2 L0 Signal Input | Watch-list / downgrade events force the signal score toward the cautious end |

---

## 4. Thermometer Overlay

The SRI thermometer tier (definitions: `systemic-warning-framework.md` §3, single
source of truth) modifies the execution posture **after** the §5 matrix row is selected:

| Tier | SRI Range | Execution Posture Modification |
|---|---|---|
| 🟢 Normal | SRI < 0.5 | No modification |
| 🟡 Watch | 0.5 ≤ SRI < 1.0 | Execution proceeds; alert thresholds tightened (opportunity flag at z > 1.5 instead of z > 2) |
| 🟠 Alert | 1.0 ≤ SRI < 1.8 | **Risk-reduction trades only; new longs suspended** — any Buy matrix row is overridden to "suspended" |
| 🔴 Danger | SRI ≥ 1.8 | Risk-reduction trades only; the card must carry the tier and the mandated action recommendation from `systemic-warning-framework.md` §3 |

The thermometer reading comes from the most recent WP-RO-03 run (computed by
`src/sri_calculator.py`). Never fabricate an SRI reading; if none is available,
declare the gap and treat the overlay as Watch.

---

## 5. Execution Decision Matrix

### 5.1 The Matrix

The core deliverable. Signal direction (from §2.2) × spread band (§2.3) × liquidity
(§2.4) selects the action:

| Signal | Spread vs FV | Liquidity | Action |
|---|---|---|---|
| Buy | Cheap (spread > FV + 10bp) | Good | Execute at market |
| Buy | Cheap | Poor | Use limit orders, split over sessions |
| Buy | Fair | Any | Wait for better entry |
| Sell | Rich (spread < FV − 10bp) | Good | Execute at market |
| Sell | Rich | Poor | Start selling early |
| Hold | Any | Any | Do nothing, await signal change |

### 5.2 Selection Procedure

1. Score the four dimensions (§2) and form the weighted composite.
2. Derive the signal direction: composite 6.5-10 → Buy; 3.5-6.4 → Hold; 1.0-3.4 → Sell.
3. Read the spread band (§2.3) and liquidity constraint (§2.4).
4. Select the matrix row (§5.1).
5. Apply the thermometer overlay (§4) as a filter — Alert/Danger overrides any Buy
   row to "suspended".
6. Apply the divergence check (§7) — on unresolved divergence, default to the more
   conservative action.

### 5.3 Output Shape

The matrix output is a **one-line execution posture** embedded in the L0 signal card,
e.g. *"Buy — cheap vs FV, good liquidity: execute at market"*. It stays within the
L0 card's 5-second consumption scope. It is not a trade plan; order-level detail
belongs to §6 tactics, produced only on request.

---

## 6. Execution Tactics

Reference depth for converting the posture into orders (produced on request, not part
of the L0 card):

- **Order type**: market orders only when liquidity is unconstrained (§2.4); otherwise
  limit orders with the limit set at the FV band boundary.
- **Order splitting**: liquidity score < 20th percentile → split across sessions,
  typical participation ≤ 20% of the bond's average daily volume estimate.
- **Timing windows**: avoid executing within 2 hours before scheduled macro releases;
  avoid the first 15 minutes after a rating-event headline (spread discovery in progress).
- **Slippage posture**: estimate slippage from the bid-ask multiple and participation
  rate; disclose the estimate and its inputs; never fabricate market-depth data
  (Mode B rules — no external data values unless the user explicitly provides sources).

---

## 7. Divergence Handling

When the Trader posture conflicts with other roles, resolve per
`multi-stakeholder.md` §3 (tension matrix, single source of truth for cross-role rules):

- **Trader negative vs CS/PM positive** (market conditions unfavorable for execution):
  delay 5 trading days; if conditions persist, escalate to desk head
  (`multi-stakeholder.md` §3.2).
- **Trader vs Risk Officer**: risk-reduction trades and opportunistic trades use
  separate limit buckets; RO-mandated reductions take precedence over Trader timing
  (`multi-stakeholder.md` §3.1).
- **Unresolved divergence**: default to the more conservative action and record the
  divergence in the Analysis Artifact.

---

## 8. Quality Gates

The following quality gates are defined for WP-TR-01 and are the single source of
truth for QA verification (alongside the two pre-existing gates from
`output-layered-framework.md` §3 and `systemic-warning-framework.md` §3):

- **Execution Dimensions (${CLAUDE_PLUGIN_ROOT}/engine/trader-framework.md §2)** — all four dimensions
  scored or gap-declared; weights 35/25/25/15 applied; data-gap rule honored
- **Execution Decision Matrix (${CLAUDE_PLUGIN_ROOT}/engine/trader-framework.md §5)** — matrix row
  selected via the §5.2 procedure with documented inputs; thermometer overlay applied;
  output is a one-line posture within L0 scope

---

## 9. Integration and Limitations

- **Analytical framework, not trading advice**: this document provides an execution
  assessment methodology. It does not provide investment or trading advice, and it
  does not guarantee execution outcomes (same posture as
  `quantitative-analysis.md` scope disclaimer).
- **Methodology-only**: LLM-executed; no coded engine, no intraday data feed. Market
  data values must come from the user or declared sources (Mode B guardrail,
  `mosaic-engine.md` §6).
- **No HTML template**: the L0 signal card remains a structured text block per
  `output-layered-framework.md` §3; this framework adds no rendering layer.
- **Data gaps are signals**: missing liquidity or spread data downgrades the
  assessment per §2.4 — never fill gaps with assumed values.

---

## Related Content

- [Engine Architecture Overview](engine-overview.md) — Core philosophy, overall architecture
- [Work Path Registry](work-path-registry.md) — WP-TR-01 path definition and routing
- [Output Layered Framework](output-layered-framework.md) — L0 Signal Card specification (§3), priority sorting (§6)
- [Systemic Warning Framework](systemic-warning-framework.md) — SRI thermometer tiers and mandated actions (§3)
- [Dual-Track Methodology](dual-track-methodology.md) — Track B market pricing signals (§3)
- [Multi-Stakeholder Framework](multi-stakeholder.md) — Role definitions, cross-role tension matrix (§3)
- [Mosaic Engine](mosaic-engine.md) — Data-gap posture, Mode B guardrail (§6)
