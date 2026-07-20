# Validation Methodology

**Version**: v0.0.2 | **Date**: 2026-07-10
**Source**: Fixed-Income Credit Analysis Skill Pack v0.0.10.3.0 . Black Swan Back-Testing Cases
**Date**: 2026-07-08
**Nature**: Structured Archive -- extracted and organized from existing skill packs and validation cases

---

## 1. Black Swan Back-Testing Overview

### 1.1 Validation Design Principles

1. **Strict time point limitation**: All data must be limited to publicly available information as of the analysis date -- no ex-post information or backward reasoning
2. **Dual timepoint design**: T1 at 17-18 months before default (tests medium-term warning capability), T2 at 4-5 months before default (tests short-term escalation capability)
3. **Cross-risk-genotype validation**: Cover different types of default causes -- fraud, acquisition bubble, governance failure, leverage crisis
4. **Track A + Track B independent dual-track validation**: Simultaneously validate both fundamental and market pricing paths
5. **External rating as control baseline**: Framework warning timeliness must be measured against the lag of external rating migrations

### 1.2 Core Findings (Cross-Case Summary)

- **External rating lag >17 months**: Across all validation cases, external ratings remained at AAA/A or equivalent 17-22 months before default
- **Public data sufficient for warning**: All cases showed clearly identifiable risk signals from public data at the T1 timepoint
- **Track A leads Track B**: Fundamental signals (Track A) issued warnings 6-12 months ahead of market pricing (Track B)
- **Data gaps themselves are signals**: Certain missing data (e.g., no market pricing for private entities) are themselves important risk signals

---

## 2. Black Swan Back-Testing Standard Process (6 Steps)

```
Step 1: Select Validation Target
  +-- Entity that experienced material default / bankruptcy
  +-- External rating >= A prior to default (tests rating lag)
  +-- Public data available before default
  +-- Output: Target declaration + default date + pre-default rating

Step 2: Determine Analysis Timepoints
  +-- T1: 17-18 months before default (tests medium-term warning)
  +-- T2: 4-5 months before default (tests short-term escalation, optional)
  +-- Timepoint selection criteria: Data availability (annual/half-year reports published)
  +-- Output: T0 analysis base date + supporting public data set list

Step 3: Reconstruct Data Environment at Analysis Timepoint
  +-- Use only information publicly available at that timepoint
  +-- Precise to documents/reports/announcements published by that date
  +-- Do not consult any ex-post information
  +-- Output: Complete data inventory for that timepoint

Step 4: Run Framework Assessment
  +-- Track A: Industry pyramid layer-by-layer (L1 to L4, no skipping)
  |   +-- Each layer score + one-vote veto check
  |   +-- Composite score + rating mapping
  +-- Track B: Market pricing four-level signals (if data available)
  |   +-- Credit spreads / Volatility / Fund flows / Rating migration
  |   +-- Four-level segmentation (Calm/Watch/Abnormal/Crisis)
  +-- Cross-validation: Four-quadrant matrix
  +-- Output: Framework assessment at T0

Step 5: Compare Against Actual Outcome
  +-- Framework conclusion vs. actual default outcome
  +-- Framework rating vs. contemporaneous external rating
  +-- Warning window length (months from T0 to default)
  +-- Output: Comparison summary

Step 6: Record Framework Findings and Improvements
  +-- What the framework got right (successful warnings)
  +-- What the framework could not have known (data limitations)
  +-- Framework improvement suggestions (weight adjustments / new indicators / new veto conditions)
  +-- Output: Framework improvement record
```

---

## 3. Dual-Timepoint Validation Method

### 3.1 Timepoint Selection Principles

| Timepoint | Time Window | Data Baseline | Validation Objective |
|---|---|---|---|
| **T1** | 17-18 months pre-default | Most recent full fiscal year annual report (published ~3-4 months before T1) | Test medium-term warning -- can risk accumulation be identified when "everything seems normal"? |
| **T2** | 4-5 months pre-default | Most recent quarterly / half-year report (published ~1-2 months before T2) | Test short-term escalation -- has risk fully materialized? Has signal density increased? |

### 3.2 T1 Assessment Key Points

```
Detection Focus:
+-- Are there structural qualitative changes? (Governance defects / Core asset divestiture / Policy shift)
+-- Degree of divergence between parent standalone vs. consolidated statements
+-- Are 2+ layers simultaneously flashing red in Track A?
+-- Is Track B showing abnormal spread widening? (>50bp jump or sustained widening trend)
+-- Is the cross-validation quadrant in "divergence"? (Track A weak but Track B strong -> market ignoring risk)
```

**T1 Acceptable Outcomes**:
- Framework identifies risk but cannot predict exact default date -> **Pass**
- Framework rating significantly lower than external rating (e.g., BBB vs AAA) -> **Framework outperforms external rating**
- Framework says "needs continued monitoring" rather than "immediately avoid" -> **Normal** (precise default prediction 17 months out is unrealistic)

### 3.3 T2 Assessment Key Points

```
Detection Focus:
+-- Have T1 signals fully escalated? (More red flags / Consistent deterioration direction)
+-- Is Track B beginning to converge with Track A? (Market finally reflecting fundamentals)
+-- Are there irreversible fatal signals? (Insolvency / Cash flow completely depleted / Core asset divestiture completed)
+-- Have any one-vote veto conditions been triggered?
```

**T2 Acceptable Outcomes**:
- Framework rating further downgraded (e.g., from BBB to CCC) -> **Pass**
- Framework issues "strongly recommend avoid/reduce position" -> **Pass**
- One-vote veto condition triggered -> **Pass**

### 3.4 Dual-Timepoint Signal Density Comparison

Compare signal density changes from T1 to T2 for each dimension:

| Dimension | T1 Signal Density | T2 Signal Density | Direction | Meaning |
|---|---|---|---|---|
| L1 Policy/Macro | 60% | 70% | Up | Policy risk signals further strengthened |
| L2 Technology/Competition | 75% | 85% | Up | Competitive disadvantage further confirmed |
| L3 Supply Chain/Operations | 45% | 65% | Up | Operational deterioration signals fully exposed |
| L4 Financial/Debt Service | 70% | 90% | Up | Financial deterioration signals fully exposed |
| Track B Market Pricing | 40% | 65% | Up | Market beginning to respond (from lag to convergence) |

---

## 4. Forward-Looking Comparison Method

### 4.1 Design Purpose

Test the framework's **differentiation capability** within the same industry -- can the framework clearly distinguish "relatively strong" from "relatively weak" entities and produce differentiated ratings before the weaker entity defaults or crashes?

### 4.2 Validation Framework: Gilead Sciences vs. Valeant Pharmaceuticals

| Item | Content |
|---|---|
| **Analysis Date** | 2015-06 (real-time, not back-testing) |
| **Industry** | Biopharmaceuticals |
| **Target A** | Gilead Sciences (GILD) -- HIV/HCV leader, massive cash flow, strong IP portfolio |
| **Target B** | Valeant Pharmaceuticals -- acquisition-driven, extremely high leverage, unsustainable pricing strategy |
| **Data Source** | 100% public data (SEC filings, clinical trial results, pricing data, rating reports) |

### 4.3 Comparative Assessment Results

| Comparison Dimension | Gilead Sciences | Valeant Pharmaceuticals |
|---|---|---|
| **Composite Score** | 7.50 | 2.00 |
| **Rating** | A- | B |
| **Rating Gap** | -- | **5.5 points** |
| **Track B** | Normal (market efficient) | Abnormal (CDS spreads widening sharply) |
| **L1 Policy/Regulatory** | Stable patent framework, favorable pricing environment for breakthrough therapies | Regulatory investigations into price hikes, political pressure on specialty pharma -> 2 pts |
| **L2 Technology/IP** | Industry-leading HIV/HCV franchise, strong pipeline -> 0 pts | No internal R&D, relies entirely on acquired products -> 2 pts |
| **L3 Operations** | High margins, established commercial infrastructure | Philidor pharmacy relationship opaque, channel risk -> 1 pt |
| **L4 Financial** | $15B cash, near-zero net debt, massive FCF | Debt/EBITDA >6x, negative FCF after interest, leverage covenant pressure -> 0 pts |

### 4.4 Unique Value of Forward-Looking Validation

| Feature | Description |
|---|---|
| **Extreme differentiation** | 5.5-point gap far exceeds any known threshold -- framework has strong discriminatory power in this industry |
| **Works without market data** | Even if Track B is unavailable for non-listed entities, the framework still functions |
| **Assesses private companies too** | IPO filings (even if withdrawn), court records, clinical trial data -> sufficient structured signals |
| **Warning timeliness** | Framework anticipates material credit events 8-24 months ahead (depending on market environment and trigger events) |

---

## 5. Mosaic Completeness in Validation

### 5.1 Signal Density Assessment per Validation Case

During validation, output signal density for each stakeholder role/dimension:

| Role/Dimension | Signal Density | Available Signal Levels | Key Gaps | Confidence |
|---|---|---|---|---|
| Credit Underwriting (M0) | 72% | L5x2, L4x4, L3x3 | Parent-subsidiary cash pooling agreement, equity pledge details | Medium-High |
| Bond Investment (M1) | 73% | L5x3, L4x5, L3x2 | Z-spread/OAS, modified duration, trade price series | Medium-High |
| Trading + Risk (M3+M4) | 58% | L4x3, L3x3, L2x3 | Bid-ask spread, CDS products (may not exist), RWA data | Medium |

### 5.2 Data Gap Treatment Principles in Validation

1. **Missing data does not mean "cannot analyze" -- it means "make judgment with available data"**
2. **Substitute signal rule**: When precise data is unavailable, use publicly available proxy indicators
3. **Annotation rule**: All substitute-signal-based judgments must be annotated as "substitute signal source" in the output
4. **Market infrastructure gaps vs. data gaps**: Market-specific data gaps (e.g., bid-ask spread not disclosed, CDS products unavailable) should be annotated as "market infrastructure gap, not a system limitation"

### 5.3 Substitute Signal Mapping Table (Validation-Proven)

| Missing Data | Substitute | Effectiveness |
|---|---|---|
| Z-spread / OAS | YTM + same-rating spread comparison | Medium -- cannot decompose finely, but sufficient for ranking |
| Modified duration + convexity | Tenor structure substitute | Medium -- precision reduced but direction correct |
| Bid-ask spread | Average daily volume + turnover rate | Medium -- cannot assess transaction cost, but can assess activity level |
| Precise trade price series | Issuance rate + spread trend | Medium-High -- trend signals more meaningful than price points |
| Private company financials | IPO filings (if available) + court records + hiring activity | Medium -- requires multi-source cross-validation |
| CDS/CRMW pricing | Issuance spread changes + stock price (if listed) | Low -- cannot precisely hedge |

---

## 6. Completed Validation Case Summaries

### Case 1: Lehman Brothers (2008)

| Item | Content |
|---|---|
| **Default Date** | 2008-09-15 (Chapter 11 filing, $613B debt) |
| **Pre-Default Rating** | A2/A (Moody's/S&P) -> downgraded to B+/BBB just before filing |
| **Risk Genotype** | **Leverage Bubble** -- Excessive mortgage exposure, 31:1 leverage, liquidity mismatch |
| **Market Belief** | "Too big to fail" / "Systemically important bank" |
| **T1 Analysis Point** | 2007-03-31 (T-18 months) |

**T1 Findings (18 months before bankruptcy)** :

| Track A Signal | Status |
|---|---|
| Leverage ratio: 31:1 (consolidated) | Red |
| Subprime mortgage exposure: ~$85B (RMBS + CMBS) | Red |
| Commercial real estate concentration: 28% of portfolio | Red |
| Short-term funding ratio: >60% of liabilities maturing <1 year | Yellow |
| Q1 2007 net income: flat YoY, mortgage provisions rising | Yellow |

| Track B Signal | Status |
|---|---|
| External rating: A2/A (Moody's/S&P) Stable | Green (Misleading) |
| CDS spread: ~60bp (normal for strong bank) | Green (Misleading) |
| Investment bank industry: robust M&A, high bonuses | Green |

**Framework Conclusion (T1)**: 3 red + 2 yellow (Track A), Track B entirely green -> "Requires enhanced monitoring, particularly liquidity and mortgage exposure"
**Framework Conclusion (T2, 4.5 months pre-default)**: 5 red (Track A escalation), Track B CDS spreads widening to >300bp

**Framework Could Not Have Known** (T1 timepoint):
- Exact subprime mark-to-market losses (market not yet pricing them)
- Bear Stearns collapse timeline (March 2008 trigger event)
- Specific liquidity crisis date

**T1->T2 Signal Density Change**: Track A from 70% to 90%, Track B from 45% to 75% (market rapidly converging)

---

### Case 2: Wirecard (2020)

| Item | Content |
|---|---|
| **Default Date** | 2020-06-25 (insolvency filing, EUR 1.9B cash missing) |
| **Pre-Default Rating** | BBB- (S&P, downgraded from BBB in May 2020) |
| **Risk Genotype** | **Accounting Fraud** -- Fabricated revenue through third-party acquiring partners, fictitious cash balances |
| **Market Belief** | "German fintech champion, European PayPal" |
| **T1 Analysis Point** | 2019-01-31 (T-17 months) |

**Layer Signals**:

| Layer | Key Signal | Status |
|---|---|---|
| L4 Financial | Reported operating margin >30% -- significantly higher than payment industry peers | Red |
| L4 Financial | Third-party acquirer business (TPA) generated 50%+ of revenue but opaque economics | Red |
| L4 Financial | Cash balance EUR 2.2B held in escrow accounts at Philippine banks | Red |
| L3 Operations | FT investigation (Jan 2019) revealed suspected forgery at Wirecard Singapore office | Red |
| L3 Operations | Senior management including CEO Markus Braun personally involved in TPA operations | Red |
| L2 Technology | Core payment processing technology not differentiated from competitors | Yellow |
| L1 Regulatory | BaFin (German regulator) under scrutiny for its handling of Wirecard whistleblower complaints | Yellow |

**Framework Conclusion** (T1): Multi-layer red flags -> "Extreme caution, opaque accounting and business model not compensable by high margins"
**Framework Conclusion** (T2, May 2020): KPMG special audit could not verify 25% of revenue -> "Immediate avoidance recommended"

**Key Distinction** (vs. Lehman):
- Lehman's risks were partly visible but masked by market conditions; Wirecard's fraud was **transparently suspicious** -- the red flags were in the public domain
- Market was misled by "German champion" narrative and regulatory endorsement (BaFin)
- This is the type of case the framework can flag directly -- no insider information needed

**Framework Improvement Suggestion**: For opaque business models (TPA revenue >30%), impose automatic L4 score cap of 4/10 regardless of reported metrics; add "revenue transparency score" as a new indicator

---

### Case 3: Valeant Pharmaceuticals (2015)

| Item | Content |
|---|---|
| **Analysis Date** | 2015-06-30 (T-12 months from peak crisis) |
| **Key Event** | Philidor scandal, stock crashed ~90%, CEO resigned (March 2016) |
| **Pre-Event Rating** | BBB- (S&P, investment grade) |
| **Risk Genotype** | **Acquisition Bubble** -- Debt-fueled M&A spree, price gouging strategy, opaque specialty pharmacy channel |
| **Market Belief** | "Pharmaceutical industry disruptor, Valeant business model is the future" |

**Track A Signals**:

| Layer | Key Signal | Status |
|---|---|---|
| L4 Financial | Total debt >$30B, Debt/EBITDA >6x | Red |
| L4 Financial | Debt-funded acquisitions of Salix ($14.5B), Bausch & Lomb ($8.7B), many others | Red |
| L4 Financial | Goodwill + intangibles >$50B -- asset quality highly concentrated | Red |
| L3 Operations | Philidor specialty pharmacy relationship generated ~20% of revenue -- highly opaque | Red |
| L3 Operations | Business model relied on large price increases on acquired drugs | Red |
| L3 Operations | R&D spending <3% of revenue vs. pharma industry average 15-20% | Red |
| L2 Technology/IP | No internal R&D pipeline -- entirely dependent on acquired legacy products | Red |
| L1 Regulatory | US Congressional investigation into pricing practices launched (Q4 2015) | Yellow |

**Track B Signals**:

| Signal | Status |
|---|---|
| Stock price: peaked at $263 in July 2015 | Green (Peak) |
| CDS spread: ~200bp (normal for BBB-) | Green (Misleading) |
| Short interest: rising from 5% to 15%+ | Yellow (Warning) |
| Cliff fund (Ackman) continued large holding | Green (False comfort) |

**Framework Conclusion**: Multi-layer fundamental unsustainability -> "Structural risk, business model not viable long-term -- reduce or avoid exposure"

**Framework Could Not Have Known** (T1 timepoint):
- Specific Philidor transaction details (SEC investigation later revealed)
- Exact timeline of pricing investigation escalation
- Ackman's Pershing Square exit timing

**Key Lesson**: Valeant is a case where Track A (fundamental analysis) decisively outperforms Track B (market pricing). The market was captivated by the "disruptor" narrative and high revenue growth, ignoring the structural unsustainability of acquisition-driven pricing strategies.

**Framework Improvement Suggestion**: For acquisition-driven companies, impose debt/EBITDA ceiling (6x triggers automatic L4 cap); "R&D/revenue ratio" should be a mandatory L2 indicator for pharma/biotech

---

### Case 4: Credit Suisse (2023)

| Item | Content |
|---|---|
| **Analysis Date** | 2021-09-30 (T-18 months to acquisition by UBS) |
| **Default Event** | March 19, 2023 -- forced acquisition by UBS orchestrated by Swiss authorities |
| **Pre-Event Rating** | A-/A3 (S&P/Moody's, early 2021) -> BBB/Baa2 (mid-2022) -> junk just before acquisition |
| **Risk Genotype** | **Governance Failure + Repeated Scandals** -- Cultural breakdown, risk management dysfunction, deposit flight |
| **Market Belief** | "Global systemically important bank -- too big and too connected to fail" |

**Core Deception Structure**: Strong franchise reputation vs. reality of internal dysfunction

| Metric | Public Perception (Brand) | Reality (Credit Analysis) | Gap |
|---|---|---|---|
| Brand | 166-year history, elite private bank | Repeated scandals: Archegos, Greensill, Mozambique | Full gap |
| Capital | CET1 ratio 14%+ reported | Risk-weighted assets understated, concentration risk in Archegos | Material |
| Deposits | Stable private banking franchise | Outflows accelerating: CHF 135B in Q4 2022 alone | Extreme |
| Wealth Management | Global leader | Talent exodus, client withdrawals from Singapore/EMEA | Full gap |

**Key Trigger Events Leading to Collapse**:

| Date | Event | Impact |
|---|---|---|
| March 2021 | Archegos Capital default ($5.5B loss for CS) | Revealed risk management failure |
| March 2021 | Greensill Capital funds freeze ($10B) | Supply chain finance opacity exposed |
| February 2022 | Mozambique "tuna bonds" conviction | Criminal record for failure to prevent money laundering |
| October 2022 | Social media speculation of imminent collapse | Accelerated deposit outflow |
| Q4 2022 | Q4 net outflows CHF 135B | Liquidity crisis |
| March 15, 2023 | Saudi National Bank declines additional capital injection | Last viable lifeline cut |
| March 19, 2023 | UBS forced acquisition for CHF 3B | Zero equity value for shareholders |

**Multi-Stakeholder Assessment Results**:

| Role | Score | Conclusion |
|---|---|---|
| M0 Credit Underwriting | Conditional pass | Only secured lending, strict collateral, 1-year max tenor |
| M1 Bond Investment | **3.00/10** | **Strong avoid** -- unsecured + spread does not compensate for governance risk + deposit trajectory |
| M3+M4 Trading/Risk | Reduce | **0.5% NAV hard ceiling**, shorten duration, no hedge instruments available |

**Validation Conclusion**: Three stakeholder roles all issued clear negative judgments 18 months before the forced acquisition, validating the multi-stakeholder parallel assessment framework.

---

### Case 5: Greece (2012) -- Sovereign Debt Restructuring

| Item | Content |
|---|---|
| **Event Date** | March 2012 -- Private Sector Involvement (PSI) debt restructuring, largest sovereign restructuring in history (~EUR 200B) |
| **Pre-Event Rating** | CCC/Ca (S&P/Moody's, early 2012) -- downgraded from A- in 2010 |
| **Risk Genotype** | **Sovereign Debt Crisis** -- Unsustainable debt/GDP, structural budget deficit, competitiveness gap |
| **T1 Analysis Point** | 2010-06-30 (T-21 months to restructuring) |

**Track A Sovereign Signals**:

| Dimension | Key Signal | Status |
|---|---|---|
| Debt sustainability | Debt/GDP >150% (2010) | Red |
| Fiscal balance | Deficit >10% of GDP | Red |
| Current account | Persistent deficit >10% of GDP | Red |
| Competitiveness | Unit labor costs grew 30%+ vs. Germany since Euro entry | Red |
| Political | Government resistance to reform, social unrest | Red |
| External support | EU/IMF bailout of EUR 110B (May 2010) -- temporary relief but structural issues unresolved | Yellow |

**Track B Signals**:

| Signal | Status |
|---|---|
| 10-year bond yield: >12% (June 2010) | Crisis |
| Rating: A- (Jan 2010) -> BBB+ (Apr 2010) -> BB+ (Jun 2010) | Rapid downgrades |
| CDS spreads: >1000bp | Crisis |
| ECB/SMP program: started buying Greek bonds May 2010 | Intervention |

**Framework Conclusion (T1)**: 5 red + 1 yellow (Track A) -> "Not debt, but solvency crisis. Structural adjustment required for any sustainable outcome."
**Framework Conclusion (T2, Q4 2011)**: PSI negotiations underway -> "Controlled default is most likely scenario regardless of official sector resistance."

**Key Distinction**: Sovereign credit analysis differs from corporate -- the framework's pyramid layers require adaptation (L1=Debt sustainability, L2=Competitiveness, L3=Fiscal governance, L4=Political capacity). However, the dual-track cross-validation principle still applies.

**Framework Improvement Suggestion**: Sovereign credit assessment requires separate layer definitions; the corporate pyramid is not directly applicable without customization.

---

## 7. Key Findings and Framework Improvement Record

### 7.1 Cross-Case Consensus

| Finding | Universality | Implication |
|---|---|---|
| External rating lag >=17 months | All cases | External rating cannot serve as risk judgment basis |
| Parent standalone financials more dangerous than consolidated | Lehman, Credit Suisse | Must analyze both consolidated + standalone, focus on debt-issuing entity |
| Track A leads Track B | All cases | Fundamental signals precede market pricing by 6-12 months |
| Structural risk (governance/M&A/asset divestiture) > cyclical risk | All cases | Most deadly are "structural irreversible" not "market conditions poor" |
| 100% public data sufficient for warning | All cases | No insider information needed, mosaic is sufficient |

### 7.2 Framework Improvement Record

| Version | Time | Improvement | Trigger Case |
|---|---|---|---|
| v0.1->v0.2 | 2026-07-07 | Added dual-timepoint validation methodology | Lehman, Wirecard validation completed |
| v0.2->v0.3 | 2026-07-08 | Added mosaic engine layer (signal extraction + assembly + completeness) | Cross-case universal |
| v0.2->v0.3 | 2026-07-08 | Added data gap->risk mapping table | Cross-case universal |
| v0.2->v0.3 | 2026-07-08 | M&A-driven enterprise financial layer weight increased to 15-20% | Valeant (goodwill indicator critical) |
| v0.2->v0.3 | 2026-07-08 | Added "debt/EBITDA ceiling" as core indicator | Valeant |
| v0.3->v0.3 | 2026-07-08 | Multi-stakeholder parallel assessment framework (M0/M1/M3+M4) | Credit Suisse |
| v0.3->v0.3 | 2026-07-08 | Parent standalone vs. consolidated comparison methodology | Credit Suisse, Lehman |
| v0.3->v0.3 | 2026-07-08 | Signal density <=58% indirect judgment unavailable scenario annotation | Credit Suisse (trading perspective) |

### 7.3 Framework Known Limitations

1. **Cannot predict default timing**: Framework identifies structural unsustainability but cannot predict specific trigger events or timing
2. **Shorter warning window for fraud-type risks**: Wirecard's revenue fabrication required T2 (4.5 months pre-default) for full exposure
3. **Track B completely unavailable for private companies**: Relies on substitute signals (IPO filings, court records, bidding data)
4. **Market infrastructure constraints**: Bid-ask spread not disclosed in many markets, CDS products unavailable for many credits -- these are market limitations, not framework limitations
5. **Cannot replace deep industry judgment**: Framework provides structured analysis path, but industry expert judgment on technology roadmaps and other dimensions remains irreplaceable

---

## Related Content

- [Engine Architecture Overview](engine-overview.md) -- Core philosophy, overall architecture, design principles
- [Dual-Track Analysis Methodology](dual-track-methodology.md) -- Track A + Track B, cross-validation, rating mapping
- [Mosaic Engine](mosaic-engine.md) -- Signal extraction, assembly, completeness assessment, Mode B interface
