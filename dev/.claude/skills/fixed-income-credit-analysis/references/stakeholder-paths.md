# Multi-Stakeholder Coverage & Path-Sheet Consumption

**Version**: v0.0.7

> This document is derived from `fixed-income-credit-analysis` SKILL.md, organizing multi-stakeholder coverage and dashboard content, supplemented with Work-Path Sheet consumption guidance. The single sources of truth are `dev/engine/multi-stakeholder.md` and `dev/engine/work-path-registry.md`.

## Multi-Stakeholder Coverage

| Role | Core Question | Work Paths | Status |
|---|---|---|---|
| Credit Selector | "Does this credit belong in the book?" — single-issuer rating, default probability | WP-CS-01 (active), WP-CS-02 (partial) | Covered (Track A+B) |
| Portfolio Manager | "Is this the best risk/reward?" — relative value, sector allocation | WP-PM-01 (active), WP-PM-02 (partial) | Covered |
| Risk Officer | "Where are concentration/contagion hotspots?" — portfolio risk monitoring | WP-RO-01/02/03 (active), WP-RO-04 (partial) | Covered |
| Trader | "Is today the day to act?" — execution, market timing | WP-TR-01 (partial) | Partial |
| Advisor | "What should my client do?" — allocation advice, suitability | WP-AD-01 (planned) | Planned |
| Individual Investor | "Should I own this bond?" — personal investment decision | WP-II-01 (planned) | Planned |

## Portfolio Manager: Single-Instrument Dashboard (WP-PM-01)

The WP-PM-01 dashboard (Type 5 template) evaluates a single bond on four dimensions (weights and metric anchors single-sourced in `dev/engine/multi-stakeholder.md` §2.2b):

1. **Relative Value (30%)** — yield/premium/spread vs same-industry and same-rating comparables
2. **Covenant Protection (25%)** — adjustment history, put triggers, cross-default, redemption structure
3. **Liquidity (20%)** — volume, turnover, abnormal volume, bid-ask spread, pledgeability
4. **Event Calendar (25%)** — upcoming macro/industry/issuer events and covenant triggers

Note the separate PM Portfolio-Construction Assessment (Relative Value / Sector Allocation Fit / Curve Positioning / Event & Calendar) in `multi-stakeholder.md` §2.2 — a different lens answering "does this position improve the portfolio?"

Output: integrated ranking table + individual bond assessment + data gap report.

## Work-Path Sheet Consumption Guide

When executing this skill, determine the reading and verification order by the following priority:

1. **Received the Work-Path Sheet from router**: Strictly read engine documents in the order listed by the `engine_reading_order` field, and verify each quality gate listed in the `quality_gates` field. The sheet's fields align with the schema of `dev/engine/work-path-registry.md`.
2. **No path sheet (user directly named a specific task)**: Fall back to the core set of the Invocation Protocol — `dev/engine/engine-overview.md` + `dev/engine/dual-track-methodology.md` + the specific topic document requested.
3. **Ambiguous request, not routed**: First clarify the path via the `credit-analysis-router` skill, or ask Q1-Q4 (role / object / depth / data) and select a path from the registry, then begin execution.
