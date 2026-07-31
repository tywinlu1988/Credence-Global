# Five-Dimensional Concentration Analysis Framework — Appendix

> Appendix to `concentration-framework.md` — version tracks the parent document; reference
> material (worked examples, derivations, historical validation) moved here in
> the 2026-07 restructure. Read on demand.

---

## 10. Integration with Existing Engine

### 10.1 Integration into M4 (Portfolio Risk Control) Framework

This framework is the core component of the M4 Portfolio Risk Control Layer (see [Contagion Matrix](contagion-matrix.md) §7.1 M4 Integration). Integration points with the existing engine:

| Framework Position | Integration Method | Specific Operation |
|-------------------|------------------|-------------------|
| **M4 Portfolio Risk Control** | Concentration Stress Test | Use this framework's five-dimensional scoring to replace the existing single industry concentration metric |
| **M4 Limit Management** | Five-dimensional Limit System | Set independent exposure limits for each dimension, linked to the contagion matrix for pathway limits |
| **M4 Trigger-Based Management** | Three-Level Alert Mechanism | Composite score ≥ 4.5 triggers Watch · ≥ 6.5 triggers Warning · ≥ 8.5 triggers Danger |
| **Contagion Matrix Stress Test** | Input Parameter | Five-dimensional composite score as initial condition for contagion matrix stress testing |
| **Output Layered Framework** | L1 Snapshot · L2 Deep Dive | Five-dimensional scores displayed as "concentration radar chart" in L1 snapshot · Full reasoning chain in L2 Deep Dive |

### 10.2 Cross-References with Related Documents

| Related Document | Referenced Content | Usage in This Framework |
|-----------------|-------------------|------------------------|
| [Contagion Matrix](contagion-matrix.md) | 13-industry classification · Contagion pathways · Escalation factors | Dimension 1 (Industry Concentration) §2.3 · Dimension 2 (Regional Concentration) §3.4 · Stress Test §9 |
| [Financial Deep Dive](financial-deep-dive.md) | Debt maturity scheduling method (C.1-C.3) | Dimension 4 (Maturity Concentration) §5.2 |
| [Engine Architecture Overview](engine-overview.md) | Three-layer architecture · M4 Portfolio Risk Control positioning | Preface · §10.1 |
| [Output Layered Framework](output-layered-framework.md) | L1/L2 output specifications | §10.1 Integration method |
| [Systemic Warning Framework](systemic-warning-framework.md) | SRI thermometer as trigger for composite score dynamic weight adjustment; composite score linked to SRI determination | §8.4 Dynamic weight adjustment rules · §10.1 Integration method |

### 10.3 Recommended New Concentration-Related Output Metrics

The following metrics are recommended for addition to the [Output Layered Framework](output-layered-framework.md):

| Output Layer | New Metric | Format | Use Case |
|-------------|-----------|--------|----------|
| L1 Signal Card | Five-dimensional concentration composite score | 🔴 7.15 · Highest dimension: Funding Channel (8) | Overview — 30-second portfolio concentration assessment |
| L1 Signal Card | Concentration Radar Chart | Pentagon radar · Threshold lines marked | Visualization — intuitive comparison across dimensions |
| L2 Deep Dive | Threshold rationale per dimension | Expandable table · Trigger metrics marked | Compliance — retrospective risk decision basis |
| L2 Deep Dive | Stress test results | Scenario → Jump → Composite score | Forward-looking — worst-case concentration |
| L2 Deep Dive | Triple concentration alert | "D₁ Industry + D₂ Region + D₄ Maturity" | Risk — multi-dimensional resonant concentration crisis |

---


---

## 11. Limitations Statement

1. **Static Threshold Risk:** This framework's threshold system is based on July 2026 market structure and historical validation data. As industry structures evolve (e.g., new industries emerging, regional economic restructuring, rating system reforms) and market conditions change, thresholds require periodic recalibration. It is recommended to review threshold parameters at least quarterly.

2. **Subjectivity of Weights:** The recommended weights (25%/20%/20%/20%/15%) are based on the engine team's judgment and retrospective calibration against 5 historical cases, not derived through statistical optimization. Optimal weights may differ significantly across market environments — users are advised to adjust weights according to their own portfolio characteristics.

3. **Pseudo-High Rating Metric Dependency on Engine:** This metric relies entirely on the accuracy of the engine's internal ratings. If internal ratings themselves have systematic bias (e.g., being too conservative or too aggressive toward specific industries), the pseudo-high rating share metric will produce misleading results. It is recommended to perform internal rating calibration and comparison with external ratings at least quarterly.

4. **Second-Order Interactions Among Dimensions Not Fully Captured:** There are complex second-order interaction effects among the five dimensions — for example, the triangular combination of "high industry concentration + high regional concentration + high maturity concentration" may produce systemic risk far exceeding the simple weighted sum. This framework uses linear weighting and does not fully capture such higher-order interactions. For "triple concentration" portfolios, an additional -2 penalty score is recommended.

5. **Non-Concentration Risk Factors Not Included:** This framework focuses on concentration risk (portfolio level) and does not cover issuer-level individual credit risk (covered by dual-track analysis and industry pyramid), liquidity risk (covered by liquidity risk assessment), or market risk (covered by non-credit risk overlay). Concentration risk is an important dimension of portfolio risk control, but not the entirety.

6. **Funding Channel Data Availability Limitations:** Data for non-standard financing, lease financing, and other channels relies on annual report note disclosures; data availability is poor for some non-listed entities. For entities with incomplete data, the confidence of funding channel concentration assessment will be significantly reduced.

7. **"One-Size-Fits-All" Risk of Regional Classification:** Classifying markets into four tiers (Major financial hubs / Major economic centers / Mid-tier cities / Peripheral regions) sacrifices intra-regional differentiation. For example, within a single country, major economic centers may have vastly different fiscal health characteristics than peripheral regions. Two-tier (national and sub-national) analysis is recommended for regional concentration analysis, but the current framework provides only national-level guidance for portfolios with broad holdings.

---


---

## Appendix

### Appendix A: Five-Dimensional Composite Score Quick Reference

Use the following table to quickly estimate the composite risk score:

| Composite Score | D₁ Industry | D₂ Region | D₃ Rating | D₄ Maturity | D₅ Funding Channel |
|----------------|-----------|---------|----------|------------|-------------------|
| ≈ 2.0 🟢 | 🟢 HHI<1000 | 🟢 Country<20% · Peripheral<10% | 🟢 AAA<30% · Pseudo<5% | 🟢 12m<30% · Peak<10% | 🟢 Single<50% · Balanced |
| ≈ 3.5 🟡 | 🟡 HHI~1200 | 🟡 Country~28% · Peripheral~15% | 🟡 AAA~40% · Pseudo~10% | 🟡 12m~40% · Peak~15% | 🟡 Single~60% |
| ≈ 5.5 🟠 | 🟠 HHI~2000 | 🟠 Country~42% · Peripheral~28% | 🟠 AAA~60% · Pseudo~22% | 🟠 12m~60% · Peak~25% | 🟠 Single~80% · Contracting |
| ≈ 7.5 🔴 | 🔴 HHI>2500 | 🔴 Country>50% · Peripheral>35% | 🔴 AAA>70% · Pseudo>30% | 🔴 12m>70% · Peak>30% | 🔴 Single>90% · or non-standard dominant |

### Appendix B: Version Change Log

| Version | Date | Change Content | Author |
|---------|------|---------------|--------|
| v0.0.1 | 2026-07-10 | Initial creation: Five-dimensional concentration analysis framework · Threshold system · Weighted scoring · Stress test integration | Engine Team |
| v0.0.1 | 2026-07-10 | System intelligence layer integration: engine version unified to v0.0.1, forming complete M4 portfolio risk control system with contagion matrix and warning framework | Engine Team |

---

*This document should be used in conjunction with the Contagion Matrix (v0.2.0) and Financial Deep Dive (v0.2.0). The Concentration Analysis Framework is the core component of the M4 Portfolio Risk Control Layer and forms a complete risk control loop with the Industry Pyramid (M1-M2) and Dual-Track Analysis (M3).*
