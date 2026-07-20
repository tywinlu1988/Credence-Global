# Multi-Stakeholder Coverage & Path-Sheet Consumption

**Version**: v0.0.2

> This document is derived from `fixed-income-credit-analysis` SKILL.md, organizing multi-stakeholder coverage and M1 dashboard content, supplemented with Work-Path Sheet consumption guidance. The single sources of truth are `dev/engine/multi-stakeholder.md` and `dev/engine/work-path-registry.md`.

## Multi-Stakeholder Coverage

| # | Stakeholder | Core Question | Status |
|---|---|---|---|
| M0 | Credit Approval (Bank) | Can we lend? At what price? | Covered (Track A+B) |
| M1 | Bond Investment | Cheap or expensive? Terms protective? Liquid? | P0 Complete |
| M2 | Bond Underwriting (DCM) | Can we sell this? To whom? Best window? | Complete |
| M3 | Market Trading | Rate/credit/liquidity environment? | Complete |
| M4 | Portfolio Risk | Concentration? Stress scenario? | Complete |
| M5 | Corporate Finance | How to finance? Which channel? When? | Complete |

## M1: Bond Investment Dashboard (P0)

Four dimensions for evaluating individual bonds:

1. **Relative Value (30%):** YTM, conversion premium, Z-spread (if available), same-industry peer comparison, same-rating comparison
2. **Terms Protection (25%):** Conversion price adjustment history, put option triggers, cross-default clauses, redemption terms
3. **Liquidity (20%):** Daily volume, turnover rate, abnormal volume events, bid-ask spread (if available)
4. **Event Calendar (25%):** Next 3 months of macro events, industry events, company events, terms triggers

Output: Integrated ranking table + individual bond assessment + data gap report.

## Work-Path Sheet Consumption Guide

When executing this skill, determine the reading and verification order by the following priority:

1. **Received the Work-Path Sheet from router**: Strictly read engine documents in the order listed by the `engine_reading_order` field, and verify each quality gate listed in the `quality_gates` field. The sheet's fields align with the schema of `dev/engine/work-path-registry.md`.
2. **No path sheet (user directly named a specific task)**: Fall back to the core set of the Invocation Protocol — `dev/engine/engine-overview.md` + `dev/engine/dual-track-methodology.md` + the specific topic document requested.
3. **Ambiguous request, not routed**: First clarify the path via the `credit-analysis-router` skill, or ask Q1-Q4 (role / object / depth / data) and select a path from the registry, then begin execution.
