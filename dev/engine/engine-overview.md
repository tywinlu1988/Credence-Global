# Fixed Income Credit Analysis Engine — Architecture Overview

**Version**: v0.0.1 | **Date**: 2026-07-18

---

## Engine Documentation Navigation

| Document | Content | When to Consult |
|---|---|---|
| **engine-overview.md** | Architecture overview, design principles, document navigation | First time understanding the engine |
| **industry-framework.md** | 10-dimension scoring, 4 industry paradigms, 7-industry pyramid, veto rules | Determining the analysis framework |
| **qualitative-analysis.md** | Information source grading, policy interpretation, mosaic assembly, narrative decomposition | Qualitative analysis guidance |
| **quantitative-analysis.md** | Spread analysis, volatility, multi-factor models, stress testing, market-implied signals | Quantitative analysis guidance |
| **dual-track-methodology.md** | Track A+B methodology, cross-validation, rating mapping, complete worked examples | Understanding dual-track integration logic |
| **mosaic-engine.md** | Signal extraction, puzzle assembly, completeness assessment, Mode B interface | Understanding the data-to-assessment pipeline |
| **multi-stakeholder.md** | M0-M5 identity types, multi-perspective cross-comparison | Multi-identity parallel analysis |
| **validation-methodology.md** | Black swan backtesting, dual-point validation, forward-looking comparison | Validating methodology effectiveness |
| **lgd-recovery-framework.md** | LGD 5-tier classification, collateral valuation, recovery path | Recovery rate assessment |
| **external-support-framework.md** | Government/group/strategic investor support, support capability vs. willingness, upgrade rules, trap signals | External support assessment |
| **outlook-monitoring-framework.md** | Rating outlook, watch list, ongoing monitoring, transition matrix | Forward-looking monitoring mechanism |
| **financial-deep-dive.md** | Three-statement linkage, working capital, FCF, scenario sensitivity, stress testing upgrade | Financial deep dive analysis |
| **governance-fraud-risk.md** | 20+ fraud signals, default evasion detection, high deposit & high debt, governance assessment | Financial fraud detection |
| **non-credit-risk-overlay.md** | Market/operational/reputational/strategic/liquidity risk overlay | Non-credit risk assessment |
| **output-layered-framework.md** | L0 signal card, L1 snapshot, L2 deep dive, three-layer output, workflow embedding | Product output specifications |
| **contagion-matrix.md** | 13x13 industry contagion matrix, transmission intensity, industry clustering, escalation factors | Cross-industry contagion risk assessment |
| **concentration-framework.md** | 5-dimension concentration analysis, threshold system, rating adjustment mapping, stress testing | Portfolio concentration risk assessment |
| **systemic-warning-framework.md** | SRI signal aggregation, 4-level thermometer, historical backtesting, real-time calculation | Systemic risk readings |
| **contagion-theory.md** | Contagion types, transmission mechanisms, escalation factors (System Intelligence Layer) | Understanding contagion theory |
| **financial-bond-framework.md** | Financial institution bond analysis framework | Financial bond analysis |
| **holding-company-framework.md** | Holding company credit analysis framework | Holding company credit analysis |
| **esg-framework.md** | ESG and governance risk framework | ESG analysis |
| **paradigm-brand-channel.md** | Brand + channel paradigm specification | Brand + channel paradigm |
| **paradigm-network-traffic.md** | Network + traffic paradigm specification | Network + traffic paradigm |
| **work-path-registry.md** | Work path registry, role x direction x depth x report path definitions | Confirming which path to follow |
| **dimension-registry.md** | Dimension registry, addressable index of 7 paradigms and M0-M5 roles (single-source pointer layer) | Dimension routing and retrieval |
| **pipeline-contract.md** | Four-stage pipeline I/O contracts, four product schemas, chain edges (machine-readable) | Pipeline stage handoff specifications |

---

## 1. Core Philosophy: Why Traditional Financial Analysis Is Not Enough

Traditional financial analysis rests on an implicit assumption — **that a firm's credit risk can be read from its financial statements**. This assumption systematically fails in the following three industry types:

| Industry Type | Why Financial Analysis Fails | Heaviest Factor Location |
|---|---|---|
| **Policy-Driven** (Solar, Semiconductors) | Policy cycles determine industry demand ceilings and profitability; sudden policy shifts can devastate an industry within weeks | Industrial policy / Geopolitics (not on balance sheet) |
| **Technology-Moat** (Advanced Equipment, Biopharma, Medical Devices) | Core assets (IP, pipeline, regulatory certifications) are not on the balance sheet; many pre-revenue firms cannot be valued by PE/PB | Technology roadmap / Core assets (not on balance sheet) |
| **Asset-Lease** (Data Centers, Infrastructure REITs) | REIT-like profile; core metrics are NOI/DSCR rather than traditional financial indicators | Customer lease quality (not on balance sheet) |

**Core conclusion: the heaviest credit factors are never on the balance sheet.**

### Problems with External Ratings

Historical case evidence consistently shows that external credit ratings systematically lag real credit deterioration:

| Case | Pre-Default Rating | Post-Default Rating | Lag Window |
|---|---|---|---|
| Enron (2001) | BBB+/Stable | D (Default) | 18+ months |
| Lehman Brothers (2008) | A+/Stable | D (Default) | 12+ months |
| Wirecard (2020) | BBB/Stable | D (Default) | 17+ months |
| Greece Sovereign (2009) | A+/Stable | SD (Selective Default) | 17+ months |

### Two Theoretical Foundations

| Theory | Implication | Implementation in the Engine |
|---|---|---|
| **Mosaic Theory** | Individual public data fragments are meaningless in isolation; assembled together they form a complete picture | Multi-source data aggregation, signal stacking, confidence weighting |
| **Information Completeness Theory** | Data gaps are not defects — they are risk signals. "We do not have this data" itself tells the user that a dimension carries uncertainty | Every analysis conclusion is accompanied by a data completeness score and a gap list |

---

## 2. Overall Architecture

```
System Intelligence Layer (Layer 4 *NEW)
  ┌──────────────────────────────────────────────┐
  │ Contagion Map x Concentration Dashboard x    │
  │ Early Warning Thermometer (SRI)              │
  │ Cross-Industry   Multi-Dimension  Systemic   │
  │ Contagion       Concentration    Risk Index  │
  └────────────────────┬─────────────────────────┘
                       │ Aggregate single-issuer results
                       ▼
Input: Industry + Entity + Analysis Date
        │
   ┌────┴────┐
   │ Mosaic  │  ← Signal extraction + assembly + completeness
   │ Engine  │
   │ (Mode A)│
   └────┬────┘
        │
   ┌────┼──────────────────────────┐
   │    │                          │
   ▼    ▼                          ▼
Track A          Track B       Track C+: Multi-Stakeholder
Fundamental    Market Pricing  (M0-M6, implemented by priority)
Analysis       Signals
(Industry      (Four-tier
Pyramid)       signals)
        │           │
        └────┬──────┘
             ▼
     Cross-Validation Matrix
     Consensus → Mutual reinforcement
     Divergence → Most valuable insight
             │
             ▼
      Integrated Output
  Rating + Signals + Completeness Report
```

### Four-Layer Architecture

| Layer | Name | Function | Status |
|---|---|---|---|
| **Layer 1** | Mosaic Engine (Mode A) | Extract signals from unstructured public data, assemble, assess completeness | Implemented (v0.3.0) |
| **Layer 2** | Dual-Track Analysis (Track A + B) | Fundamental pyramid scoring + market pricing signal cross-validation | Implemented (v0.1.0) |
| **Layer 3** | Multi-Stakeholder Perspective (M0-M6) | Coverage across credit approval, bond investment, underwriting, trading, portfolio risk management roles | M0-M5 implemented, M6 planned |
| **Layer 4** | System Intelligence Layer (Aggregation) *NEW | Contagion mapping, concentration dashboard, early warning thermometer; cross-industry and cross-issuer systemic risk perception | Implemented (v0.7.0) |

### Dual-Track Parallel Structure

```
Track A: Fundamental Analysis          Track B: Market Pricing Signals
(Qualitative + Scoring)                (Quantitative Signals)
  L1 (Heaviest)                          Credit Spreads
  L2                                     Volatility
  L3                                     Fund Flows
  L4 (Lightest)                          Rating Migration
        │                                │
        └────────────┬───────────────────┘
                     ▼
           Cross-Validation Matrix
  Consensus → Mutual reinforcement
  Divergence → Most valuable insight
```

---

## 3. Key Design Principles

| # | Principle | Meaning |
|---|---|---|
| 1 | **Financial Analysis is Not the Heaviest Layer** | The heaviest factors are always structural or external, not on the balance sheet |
| 2 | **Industry Determines Weights** | Each industry's heaviest factors are determined by the 10-dimension scoring (D1-D10); different industries use different weight templates |
| 3 | **Layer-by-Layer Progression** | L1 must pass before L2 analysis is meaningful; layers cannot be skipped |
| 4 | **L4 as Validation Layer** | The financial layer (lowest layer) is used to validate upper-layer judgments. Strong finance + weak upper layers = more dangerous (cycle top or fraud); weak finance + strong upper layers = flagged risk but not overturned |
| 5 | **Public Data is Sufficient** | POC validated across 3 black swan cases and 3 industries; public data provides sufficient support for effective analysis |
| 6 | **Track B is Independent and Non-Subordinate** | Market pricing signals are independent from fundamental analysis; divergence between the two tracks generates the most valuable questions |
| 7 | **Track A Takes Priority on Conflict** | Auditable public financial facts take priority over external ratings |
| 8 | **Data Gaps = Risk Signals** | Every analysis must include a completeness report, noting what data is missing and what risk that implies |
| 9 | **Identifying Structural Unsustainability** | The framework can identify structurally unsustainable credit quality but cannot predict the precise timing or trigger event of default |

---

## 4. Data Source Architecture

**Hard constraint: zero internal data, zero non-public data, zero paid data (POC phase).**

| Data Layer | Source | Collection Method |
|---|---|---|
| Macro Policy | Central bank websites, government portals | WebSearch + LLM parsing |
| Industry Data | Industry associations, international research reports | WebSearch |
| Supply Chain Pricing | Free data platforms (SMM, TrendForce, PVInfoLink free tiers) | WebSearch |
| Corporate Information | SEC EDGAR, stock exchange filings, Companies House | WebSearch |
| Litigation / Regulatory | PACER, ECB registers, regulatory enforcement databases | WebSearch |
| Bond Data | TRACE, exchange announcements, BIS debt securities statistics | WebSearch |
| Macroeconomic | IMF data portal, FRED (Federal Reserve Economic Data) | WebSearch |

**Four data availability checks must be completed before analysis:** policy data, entity risk data, industry data, and market pricing data.

---

## 5. Scoring Engine and Rating Mapping

### Scoring Formula

```
Composite Score = Sigma(Layer Score x Layer Weight)
Layer Weight = f(Industry 10-Dimension Score)
Layer Score = Sigma(Indicator Score x Indicator Weight)
Indicator Score = f(Raw Value, Threshold, Direction)
```

### Rating Mapping

> The rating mapping table references S&P, Moody's, and Fitch nomenclature and is detailed in [dual-track-methodology.md](dual-track-methodology.md) (Rating Mapping section).

---

## 6. Version History

| Version | Date | Changes |
|---|---|---|
| v0.0.1 | 2026-07-17 | Initial release: international fixed-income credit analysis engine |

---

## 7. Version Management Strategy

### 7.1 Version Numbering System

The engine documentation system uses two parallel version numbering schemes:

| Version Scheme | Scope | Example | Description |
|---|---|---|---|
| **Engine Version** | Core methodology documents | v0.0.1 | Reflects the overall iteration stage of engine methodology; all core methodology documents are uniformly labeled with this version |
| **Review Report Version** | Audit, self-assessment, final review documents | v1.0, v1.1 | Independent versioning for review reports; document headers note "Corresponding engine version: v0.8.0-release" |

### 7.2 Core Methodology Document Version Mapping

| Document | Current Version | Description |
|---|---|---|
| engine-overview.md | v0.0.1 | Engine architecture overview |
| dual-track-methodology.md | v0.0.1 | Dual-track analysis methodology |
| industry-framework.md | v0.0.1 | Industry classification and analysis framework |
| qualitative-analysis.md | v0.0.1 | Qualitative analysis methodology |
| quantitative-analysis.md | v0.0.1 | Quantitative analysis methodology |
| mosaic-engine.md | v0.0.1 | Mosaic engine |
| output-layered-framework.md | v0.0.1 | Layered output framework |
| contagion-theory.md | v0.0.1 | Contagion theory foundations (System Intelligence Layer) |
| contagion-matrix.md | v0.0.1 | 13-industry contagion matrix |
| concentration-framework.md | v0.0.1 | 5-dimension concentration analysis framework |
| systemic-warning-framework.md | v0.0.1 | Systemic early warning framework |
| validation-methodology.md | v0.0.1 | Black swan backtesting validation methodology |
| financial-bond-framework.md | v0.0.1 | Financial bond analysis framework |
| holding-company-framework.md | v0.0.1 | Holding company credit analysis framework |
| non-credit-risk-overlay.md | v0.0.1 | Non-credit risk overlay |
| external-support-framework.md | v0.0.1 | External support assessment framework |
| esg-framework.md | v0.0.1 | ESG and governance risk framework |
| governance-fraud-risk.md | v0.0.1 | Governance and fraud risk framework |
| outlook-monitoring-framework.md | v0.0.1 | Outlook and ongoing monitoring framework |
| lgd-recovery-framework.md | v0.0.1 | LGD and recovery analysis framework |
| multi-stakeholder.md | v0.0.1 | Multi-stakeholder framework |
| financial-deep-dive.md | v0.0.1 | Financial deep dive analysis framework |
| paradigm-brand-channel.md | v0.0.1 | Brand + channel paradigm specification |
| paradigm-network-traffic.md | v0.0.1 | Network + traffic paradigm specification |
| work-path-registry.md | v0.0.1 | Work path registry |
| dimension-registry.md | v0.0.1 | Dimension registry |
| pipeline-contract.md | v0.0.1 | Four-stage pipeline product contracts |

**Responsibility boundary note:** The original M4 portfolio risk control framework (multi-stakeholder.md section 5) handles single-issuer and single-portfolio risk control (concentration limits, stress testing, rating adjustments). The System Intelligence Layer (contagion-matrix.md, concentration-framework.md, systemic-warning-framework.md) adds cross-issuer and cross-portfolio systemic risk analysis on top of M4 — the contagion matrix covers full-market industry pair transmission, the concentration framework covers 5-dimension portfolio concentration, and the early warning framework provides market-wide SRI readings. The division is clear: M4 handles single-issuer risk control; the System Intelligence Layer handles cross-issuer systemic risk.

### 7.3 Version Management Principles

1. **Unified methodology document version**: All core methodology documents (non-review) uniformly carry the same engine version number
2. **Version upgrade triggers**:
   - New functional modules or industry coverage — increment minor version (e.g., v0.5.x)
   - Major methodology restructuring or rating system changes — increment major version (e.g., v1.0.0)
   - Consistency fixes, terminology unification, threshold alignment — increment patch version (e.g., v0.5.x)
3. **Independent review report versioning**: Audit and self-assessment documents use an independent versioning system but must note "Corresponding engine version"
4. **Centralized version history**: All engine version upgrade records are maintained centrally in this section (Section 6); individual documents only carry their own version number and date

---

## Related Content

- [Industry Classification and Analysis Framework](industry-framework.md) — 10-dimension scoring, industry types, 7-industry pyramid specification
- [Dual-Track Analysis Methodology](dual-track-methodology.md) — Track A + Track B, cross-validation, rating mapping, complete worked examples
- [Mosaic Engine](mosaic-engine.md) — Signal extraction, assembly, completeness assessment, Mode B interface definition
- [13-Industry Contagion Matrix](contagion-matrix.md) — 13x13 industry contagion pathways, transmission intensity, industry clustering
- [Contagion Theory Foundations](contagion-theory.md) — Contagion types, transmission mechanisms, escalation factor theory
- [5-Dimension Concentration Analysis Framework](concentration-framework.md) — Industry, region, rating, tenor, funding channel concentration assessment
- [Systemic Early Warning Framework](systemic-warning-framework.md) — SRI signal aggregation algorithm, 4-level thermometer, historical backtesting
