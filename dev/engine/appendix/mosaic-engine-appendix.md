# Mosaic Engine — Appendix

> Appendix to `mosaic-engine.md` — version tracks the parent document; reference
> material (worked examples, derivations, historical validation) moved here in
> the 2026-07 restructure. Read on demand.

---

## 7. Example: How the Mosaic Theory Works

### Case: Assessing Tesla's Debt Servicing Capacity

**Five Fragments -- each insufficient alone:**

| Fragment | Signal | Problem Alone |
|---|---|---|
| Tesla 2028 bond yield tightened from 5.2% to 4.8% in Jan-Jun 2025 | Market sees risk decreasing | Could be general monetary easing |
| Tesla 2028 bond yield widened from 4.8% to 5.1% in Jul 2025 | Market starts repricing risk | Small move, could be noise |
| Tesla 2025 operating income fell 22% YoY in H1 2025 | Fundamentals significantly deteriorated | Loss could be one-time (Cybertruck ramp costs) |
| Tesla accounts receivable jumped 35% from Q1 to Q2 2025 | Collection capacity deteriorating | Could be seasonal timing |
| S&P maintains BBB-/Stable rating | Rating agency sees risk as manageable | Rating lag is a known issue |

**Assembled Complete Picture:**

```
Fragment 1 (spread tightening) + Fragment 2 (spread reversal) = Spread inflection signal (weak->moderate)
Fragment 2 (spread reversal) + Fragment 3 (profit decline) = Market starting to reflect fundamentals (upgrade)
Fragment 3 (profit decline) + Fragment 4 (AR jump) = Not just losses, but worsening collection (dual negative)
Fragment 5 (BBB- maintained) + Fragments 1-4 = Rating lag confirmed (rating signal unreliable)

Mosaic Conclusion:
Tesla's debt servicing capacity is deteriorating; market pricing (spread reversal) is beginning to reflect
this trend, but the BBB- rating still lags behind.

Information Completeness Assessment: Moderate
Gap: Tesla parent-level standalone financial data not fully separable from consolidated
-> Cannot precisely assess parent-level true debt servicing capacity
```

### Mosaic Assembly Process Demonstration

| Step | Operation | Result |
|---|---|---|
| 1 | Extract 5 raw signals | Each signal individually at L2-L4 confidence |
| 2 | Same-direction signal stacking | Spread first down then up -> inflection signal (L3->L4 upgrade) |
| 3 | Cross-dimension validation | Loss (L3) + AR jump (L3) = dual negative (L4 upgrade) |
| 4 | Contradiction handling | BBB- rating vs other 4 signals -> rating signal unreliable |
| 5 | Signal density calculation | 4 of 5 dimensions with available signals -> 80% (moderate-high) |
| 6 | Gap identification | Parent financial data missing -> affects L4 score confidence +/-1 |

---


---

## 8. Implementation Priorities

| Priority | Module | Description |
|---|---|---|
| **P0** | Signal Extraction Layer + Mosaic Assembly Layer | Foundation for all P0/P1/P2 analyses |
| **P0** | Completeness Assessment Layer | **Core differentiator** -- gap annotation engine |
| **P1** | Gap->Risk Mapping Table (industry-customized) | What risk each missing data type implies per industry |
| **P1** | Mode B: CSV Upload Adapter | Lowest-cost "external data" entry point |
| **P2** | Mode B: REST API Adapter | Bloomberg / Refinitiv professional terminals |
| **P3** | Mode B: MCP Adapter | User-built data services |

---
