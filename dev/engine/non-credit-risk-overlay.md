# Non-Credit Risk Overlay

**Version**: v0.0.6 | **Date**: 2026-07-10 | **Position**: Independent adjustment layer above the credit pyramid baseline rating

---

## Table of Contents

- [1. Methodological Gap: Risk Coverage Scope](#1-methodological-gap-risk-coverage-scope)
- [2. Positioning of Non-Credit Risk in the Engine](#2-positioning-of-non-credit-risk-in-the-engine)
- [3. Market Risk Transmission to Credit](#3-market-risk-transmission-to-credit)
- [4. Operational Risk Signals](#4-operational-risk-signals)
- [5. Reputational Risk Signals](#5-reputational-risk-signals)
- [6. Strategic Risk Signals](#6-strategic-risk-signals)
- [7. Liquidity Risk Signals](#7-liquidity-risk-signals)
- [8. Overlay Adjustment Rules](#8-overlay-adjustment-rules)
- [9. Signal Aggregation and Scoring Rules](#9-signal-aggregation-and-scoring-rules)
- [10. Integration with Existing Frameworks](#10-integration-with-existing-frameworks)
- [11. Honest Labeling Under Public Data Constraints](#11-honest-labeling-under-public-data-constraints)
- [Appendix A: Data Source Inventory by Risk Dimension](#appendix-a-data-source-inventory-by-risk-dimension)

---

## 1. Methodological Gap: Risk Coverage Scope

### 1.1 Audit Findings

The engine's coverage of risk types is benchmarked against the Basel capital accord and the COSO ERM 2017 framework, covering the following areas:

| Basel Risk Type | Engine Coverage Status | Coverage Level | Gap Description |
|---|---|---|---|
| **Credit Risk** | Track A Fundamental Pyramid + Track B Market Pricing + FCF/Interest Coverage + Rating Mapping | Full Coverage | Core engine capability, no major improvement needed |
| **Market Risk** | Track B partially covers credit spread/volatility; interest rate duration/convexity marked as paid data | Partial Coverage | Interest rate/forex/commodity price risk completely uncovered |
| **Operational Risk** | L4 Financial layer implicitly covers some fraud signals; FCF Ponzi financing suspicion detection | Weak Coverage | Internal process deficiencies/system failures/legal compliance risk/management fraud not systematically covered |
| **Liquidity Risk** | Debt maturity schedule + FCF/Interest Coverage + M1.3 Bond Liquidity Assessment | Partial Coverage | Funding channel concentration/credit facility utilization/bond issuance failure history not covered |
| **Reputational Risk** | Completely uncovered | Uncovered | ESG controversies/negative media coverage/client termination not incorporated into analysis |
| **Strategic Risk** | L1 Industry Pyramid implicitly covers some structural factors | Weak Coverage | Business model sustainability/technological disruption/management strategic execution not explicitly assessed |
| **Concentration Risk** | L3 Supply Chain covers customer concentration | Weak Coverage | Industry/geographic/funding channel concentration not systematically covered |

### 1.2 Scope of This Module

This module covers the dimensions within the first six Basel risk types where the engine's coverage is insufficient. Concentration risk is already partially addressed through the L3 supply chain layer of each industry pyramid and the M4 portfolio risk management perspective, and is therefore not within the core scope of this module.

---

## 2. Positioning of Non-Credit Risk in the Engine

### 2.1 Design Philosophy: Overlay, Not Replacement

The non-credit risk layer does **not replace** the existing four-layer credit analysis pyramid. The credit pyramid produces a "baseline rating," and the non-credit risk overlay adjusts it up or down from that baseline.

```
Standard Analysis Process (with Non-Credit Risk Overlay):

Step 1: Industry Classification -> Select Pyramid Template
Step 2: Pyramid Scoring -> L1-L4/L5 Layer-by-Layer Scoring -> Weighted Composite Score -> Baseline Credit Rating
Step 3: External Support Assessment (if needed) -> Upgrade Baseline Rating (0-3 notches)
Step 4: ★ Non-Credit Risk Overlay (New)
   ├── 4a: Market Risk Assessment -> Transmission Path Identification
   ├── 4b: Operational Risk Assessment -> Red Flag Signal Detection
   ├── 4c: Reputational Risk Assessment -> Negative Event Scanning
   ├── 4d: Strategic Risk Assessment -> Business Model Sustainability Judgment
   └── 4e: Liquidity Risk Assessment -> Funding Channel Health
Step 5: ★ Overlay Adjustment -> Apply ±0 to ±1 notch adjustment on baseline rating
Step 6: Track B Market Pricing Cross-Validation
Step 7: Output Composite Rating + Non-Credit Risk Overlay Annotation
```

### 2.2 Analogy with External Support Framework

The design mechanism of this module is consistent with the "upgrade" logic in external-support-framework.md — both are independent adjustment layers applied after baseline pyramid scoring and before the final rating output.

| Adjustment Layer | Direction | Magnitude | Trigger Condition |
|---|---|---|---|
| External Support Overlay | Upgrade only (+) | 0-3 notches | Clear supporting entity with sufficient capability + willingness |
| Non-Credit Risk Overlay | Can adjust up or down (±) | 0-1 notches | Non-credit risk signals detected and impact threshold reached |

Order of application: External support upgrade is applied first, followed by the non-credit risk overlay adjustment (which can offset the external support upgrade or amplify downside risk).

### 2.3 Position of the Overlay in the Engine Architecture

```
Engine Architecture (Full Version v0.0.1+):
                                                                        ┌───────────────────────────┐
                                                                        │ Non-Credit Risk Overlay   │
Input -> Mosaic Engine -> Track A Pyramid Scoring -> External Support ->│ ★ This Document           │-> Cross-Collision -> Composite Output
                                                                        │ Market/Operational/       │
                                                                        │ Reputational/Strategic/   │
                                                                        │ Liquidity Risk            │
                                                                        │ ±0-1 notch adjustment     │
                                                                        └───────────────────────────┘
```

---

## 3. Market Risk Transmission to Credit

### 3.1 Definition of Market Risk in Credit Analysis

Market Risk refers to the risk that a company's debt-servicing capacity deteriorates due to adverse movements in market price factors such as interest rates, exchange rates, and commodity prices. This module does not assess portfolio-level VaR (that is the responsibility of M3/M4), but rather evaluates the **transmission pathways** from market risk to credit quality.

### 3.2 Interest Rate Risk Transmission Path

| Transmission Factor | Indicator | Formula/Data Source | Data Accessibility |
|---|---|---|---|
| **Interest Coverage Deterioration** | Floating Rate Debt Ratio | Annual report notes "Borrowings" classification: Floating rate borrowings / Total interest-bearing debt | Annual report notes accessible |
| **Refinancing Cost Increase** | Average coupon rate on outstanding bonds vs current market rate | Prospectus + Central bond pricing (free public) | Bond issuance info free, central bond pricing partially free |
| **Debt Structure Lock-in Effect** | Fixed Rate Debt Ratio | Annual report notes "Borrowings" classification: Fixed rate borrowings / Total interest-bearing debt | Annual report notes accessible |
| **Duration Exposure** | Weighted Average Debt Duration (approximate) | Weighted average of bond maturities (based on reporting year) | Estimated value; precise duration requires paid terminal |

**Interest Rate Risk Transmission Path**:

```
Rising Interest Rates
  ├── Floating Rate Debt Interest Increases -> Interest Expense Rises -> Interest Coverage Declines
  ├── New Bond/Loan Refinancing Cost Rises -> Financing Cost Increases -> FCF Declines
  ├── Bond Prices Fall -> Unrealized Losses on Asset Side -> Net Assets Decline -> Leverage Ratio Increases
  └── Highly Leveraged Enterprises Face Refinancing Difficulty -> Liquidity Squeeze -> Default Risk Increases
```

**Signal Detection**:

| Signal | Detection Condition | Severity | Data Source |
|---|---|---|---|
| Floating rate debt ratio > 40% | Annual report notes "short-term borrowings + long-term borrowings" floating rate proportion | Medium | Annual report notes (borrowings classification) |
| Interest coverage < 2x and total debt/EBITDA > 5x | (EBITDA / Interest Expense) < 2x | High | Annual report income statement + notes |
| Debt maturing in next 12 months > 40% and currently in a rising rate cycle | Debt maturity schedule + Central bank benchmark rate trends | Medium | financial-deep-dive.md C.3 + Central bank open market operations announcements |
| Short-term borrowings ratio jumped > 10pp (YoY) | Short-term borrowings / Total interest-bearing debt YoY change | Medium | Annual report balance sheet |

**Data Limitation Note**: Precise duration (Macaulay Duration / Modified Duration) requires bond valuation models or paid financial terminals (Bloomberg/Refinitiv). This module uses an approximate substitute — weighted average based on remaining years to maturity.

### 3.3 Exchange Rate Risk Transmission Path

**Applicable to**: Issuers with foreign currency revenue/foreign currency debt/overseas operations.

| Transmission Factor | Indicator | Formula/Data Source | Data Accessibility |
|---|---|---|---|
| Foreign Currency Revenue Exposure | Foreign currency revenue / Total revenue | Annual report geographic revenue breakdown (overseas revenue proportion) | Annual report notes accessible |
| Foreign Currency Debt Exposure | Foreign currency debt / Total interest-bearing debt | Annual report notes "borrowings" classification — foreign currency borrowings | Annual report notes accessible |
| Net Foreign Exchange Exposure | Foreign currency assets - Foreign currency liabilities (simplified) | Annual report notes "foreign currency monetary items" | Annual report notes accessible |
| FX Hedge Ratio | FX derivative notional principal / Net FX exposure | Annual report derivative transaction notes (forwards/options/swaps) | Annual report notes accessible |

**Exchange Rate Risk Transmission Path**:

```
Local Currency Depreciation
  ├── Imported Raw Material/Equipment Costs Rise -> Gross Margin Compression -> Profitability Declines
  ├── Foreign Debt Principal & Interest Repayment Costs Rise -> Debt Service Burden Increases -> Interest Coverage Declines
  ├── [Positive] Export Revenue in Local Currency Value Rises -> Revenue Increases (depends on invoicing currency)
  └── [Liability Side] Foreign Currency Debt Revaluation Loss -> FX Translation Loss -> Net Profit Declines
```

**Signal Detection**:

| Signal | Detection Condition | Severity | Data Source |
|---|---|---|---|
| Foreign currency revenue proportion > 30% and insufficiently hedged | High overseas revenue proportion + derivative notional/net exposure < 30% | Medium | Annual report geographic revenue + derivative notes |
| Foreign currency debt proportion > 20% and local currency depreciation cycle | Foreign currency debt / total debt > 20% + currency trend | Medium | Annual report notes borrowings classification + central bank exchange rate fix |
| FX gain-loss / net profit > 10% | FX gains/losses in annual report finance costs / net profit | Medium | Annual report finance cost details |
| Net FX exposure > 20% of net assets | (Foreign currency assets - Foreign currency liabilities) / Net assets | High | Annual report foreign currency monetary items notes |

**Data Limitation Note**: Specific terms of FX hedges (strike prices, maturities, counterparty credit) are typically not fully disclosed in annual reports — only notional principal and fair value are visible. Precise exchange rate risk exposure requires internal management reports — not publicly accessible.

### 3.4 Commodity Price Risk Transmission Path

**Applicable to**: Impact of upstream raw material price volatility on margins and cash flow.

| Transmission Factor | Indicator | Formula/Data Source | Data Accessibility |
|---|---|---|---|
| Cost Pass-Through Ability | Correlation coefficient between gross margin and raw material price index | Annual gross margin change / Industry raw material price index change | Industry price data (SMM/LME/Mysteel and other free data platforms) |
| Raw Material Cost Ratio | Raw material cost / Operating cost | Annual report cost analysis notes (materials/labor/overhead breakdown) | Annual report notes accessible |
| Price Lock-In Degree | Long-term contract coverage ratio / Inventory coverage months | Annual report procurement contract section / Inventory turnover days | Some annual reports disclose supply chain management |

**Commodity Price Risk Transmission Path**:

```
Rising Raw Material Prices
  ├── Costs Rise -- Can be passed to customers? -- Yes -> Gross Margin Stable
  │                                             └── No -> Gross Margin Compression -> FCF Declines
  ├── Inventory Value Increases (positive, but unsustainable)
  └── Additional Working Capital Required -> Capital Tie-Up Increases -> Liquidity Pressure
```

**Signal Detection**:

| Signal | Detection Condition | Severity | Data Source |
|---|---|---|---|
| Gross margin negatively correlated with raw material prices > 0.7 | Gross margin movement direction opposite to raw material price index for 3 consecutive years | High | Annual report gross margin + SMM/LME price indices |
| Raw material cost ratio > 60% with no long-term contract protection | Raw material proportion high in materials/labor/overhead breakdown | Medium | Annual report cost analysis notes |
| Inventory turnover days continuously rising + gross margin declining | DIO rising + gross margin declining simultaneously (double hit of slow sales + price impairment) | High | Annual report + financial-deep-dive.md B.3 |

### 3.5 Market Risk Composite Assessment

| Assessment | Condition |
|---|---|
| **Low** | Purely domestic sales + no foreign currency debt + predominantly fixed rate + raw material cost ratio < 30% |
| **Medium** | Any single dimension has moderate exposure (foreign currency revenue > 20% or floating rate debt > 20% or raw material ratio > 40%) |
| **High** | Two or more dimensions simultaneously have large exposure + unhedged |
| **Very High** | Large exposure across 2+ dimensions + poor financial flexibility (interest coverage < 1.5x) |

---

## 4. Operational Risk Signals

### 4.1 Definition of Operational Risk in Credit Analysis

Under the Basel capital accord, operational risk is defined as "the risk of loss resulting from inadequate or failed internal processes, people, and systems or from external events." In credit analysis, operational risk signals indicate a breakdown in management controls — a direct reflection of management capability and integrity.

### 4.2 Four-Quadrant Classification of Operational Risk

| Category | Examples | Transmission Path to Credit | Public Data Observability |
|---|---|---|---|
| **Internal Process Deficiencies** | Financial statement restatements, internal control audit failures, accounting error corrections | Data credibility impaired -> All financial-statement-based analysis must be discounted | **Partially observable** — Financial statement restatements and internal control audit reports are publicly released |
| **People Risk** | Sudden departure of CEO/CFO, compliance officer change, key personnel uncontactable | Management continuity disrupted -> Strategic execution uncertainty rises | **Observable** — Company announcements, business registration changes |
| **System Risk** | Core information system failure, data breach, cybersecurity incident | Business interruption -> Revenue loss + reputational damage + regulatory penalties | **Partially observable** — Major system failures/data breaches become public through regulatory announcements or media reports |
| **External Events** | Fraud/misconduct, regulatory penalties, legal proceedings | Direct financial loss + indirect reputational damage + increased financing costs | **Observable** — Securities regulator penalties/exchange sanctions/court judgments are all public |

### 4.3 Operational Risk Red Flag Signal Checklist

#### 4.3.1 Major System Failures / Cybersecurity Incidents

| Red Flag Signal | Detection Condition | Signal Severity | Data Source | Observability |
|---|---|---|---|---|
| **Core system major failure causing business interruption** | Media reports/company announcement confirms system failure causing business suspension exceeding 24 hours | Medium | News databases, industry media, company announcements | **Observable** — Major system failures typically have media coverage |
| **Data breach / cybersecurity incident** | Company announcement confirms data breach or regulatory interview/notification | High | Company announcements, cyber administration disclosures, industry regulatory notices | **Observable** — Major data breaches must be publicly announced per regulations |
| **Cloud service / IT infrastructure disruption** | Core provider (e.g., AWS/Azure/GCP) outage causing business shutdown | Medium | Industry news, provider status pages | **Partially observable** — Only major events are reported |

**Data Limitation Note**: Internal process deficiencies (such as approval process loopholes, employee misconduct) are **completely unobservable** when they do not trigger a public event. This module only captures operational risk events that have already become externalized (e.g., have caused losses, have been penalized by regulators) — which inherently involves a lag.

#### 4.3.2 Regulatory Penalties

| Red Flag Signal | Detection Condition | Signal Severity | Data Source |
|---|---|---|---|
| **Securities regulator investigation** | Company announcement "received notice of investigation from securities regulator" | Strong | Company announcements, securities regulator official website |
| **Exchange public censure / notice of criticism** | Stock exchange issues "public censure" or "notice of criticism" sanction | Strong | Stock exchange regulatory information disclosure sections |
| **Banking/financial regulator administrative penalty** | Banking/financial regulator imposes administrative penalty on banks/insurance/financial companies | Medium-Strong | Financial/banking regulator official website, central bank website |
| **Environmental administrative penalty** | Environmental protection agency or provincial environmental department penalty exceeding threshold | Medium | Environmental protection agency website "administrative penalties" section |
| **Market regulation authority penalty** | Penalty for product quality/advertising violations/antitrust from market regulation authority | Medium | National market regulation authority disclosure system |
| **Tax penalty** | Tax evasion detected by tax audit and penalized | Strong | Tax authority major tax violation case disclosures |

**Fraud signals extracted from governance-fraud-risk.md are a subset of operational risk**: The financial fraud red flags (revenue quality anomalies, profit quality anomalies, asset/liability quality anomalies, audit opinion anomalies) and management governance red flags (share pledge ratio, ultimate controller risk, management stability, board independence) covered in that document are essentially specific manifestations of "internal processes + people risk" within operational risk. These signals are reused in this module and are not redefined.

#### 4.3.3 Key Personnel Risk

| Red Flag Signal | Detection Condition | Signal Severity | Data Source |
|---|---|---|---|
| **Sudden departure of CEO/CFO** | Company announcement confirms abnormal departure of CEO/CFO/finance director (not term expiration, not retirement) | Strong | Company announcements, exchange announcements |
| **Departure of CTO/key technical leader** | Departure of core technical leader in technology companies (e.g., R&D VP at semiconductor firms, Chief Scientific Officer at biopharma) | Medium-Strong | Company announcements, industry media, business registration changes |
| **Concentrated resignations of independent directors** | Resignation of 2+ independent directors within the same financial reporting period | Strong | Company announcements |
| **Resignation of supervisor/audit committee member** | Resignation of audit committee chair or supervisor (weakening of internal control oversight) | Medium | Company announcements |
| **Core management placed under coercive measures** | Announcement confirms senior executive detained/investigated/under bail pending investigation | Strong | Company announcements, court judgment databases, enforcement information disclosure platforms |
| **Collective share reduction by core management** | Multiple senior executives collectively reduce holdings within 30 days before financial disclosure | Medium | Director/supervisor/senior management shareholding change announcements |

**Data Limitation Note**: The underlying reasons for key personnel departures (personal reasons, performance inadequacy, or discovery of major issues) are typically not fully disclosed. "Personal reasons" is the most common standard formulation, making it impossible to distinguish the true cause. Only when the company subsequently experiences other irregularities after the departure can a reverse inference be made — which involves a time lag.

#### 4.3.4 Legal Litigation Risk

| Red Flag Signal | Detection Condition | Signal Severity | Data Source |
|---|---|---|---|
| **Material pending litigation amount > 10% of net assets** | Amount of pending litigation disclosed in annual report "Material Litigation and Arbitration" section | Medium-Strong | Annual report, interim reports |
| **Party as defendant with potential adverse judgment** | Litigation status "accepted" or "first instance judgment" and enterprise is defendant | Medium | Annual report, court judgment databases, business information platforms |
| **Involvement in class action / investor claims** | Securities misrepresentation liability dispute lawsuit due to information disclosure violations / false statements | Strong | Company announcements, court announcements |
| **Major intellectual property litigation** | Core technology/core product involved in patent infringement litigation | Medium-Strong | Company announcements, court judgment databases |

### 4.4 Operational Risk Composite Judgment

| Assessment | Condition |
|---|---|
| **No Signal** | No disclosed regulatory penalties, litigation, or abnormal personnel changes |
| **Weak Signal** | 1-2 medium-severity signals (e.g., single environmental penalty, single independent director resignation) |
| **Moderate Signal** | 1 strong signal OR 2-3 medium signals |
| **Strong Signal** | 2 or more strong signals (e.g., securities regulator investigation + sudden CFO departure) |
| **Extreme Signal** | Confirmed financial fraud (qualified audit opinion + securities regulator confirmation) or collective loss of contact with management |

---

## 5. Reputational Risk Signals

### 5.1 Definition of Reputational Risk in Credit Analysis

Reputational Risk refers to the risk that negative public perception causes a company's financing costs to rise, customers to leave, and business opportunities to decrease, thereby indirectly impairing credit quality. Reputational risk does not typically lead directly to default — but it acts as an "accelerator," exponentially magnifying the speed of deterioration on top of existing credit problems.

### 5.2 Transmission Path of Reputational Risk to Credit

```
Negative Event (ESG controversy / Scandal / Penalty)
  |
  ├-- Media Exposure / Public Attention -> Brand Value Impaired
  |     ├-- Customer Attrition -> Revenue Decline
  |     └-- Suppliers Demand Shortened Payment Terms / Prepayment -> Working Capital Pressure
  |
  ├-- Funding Channels
  |     ├-- Banks Tighten Credit Lines -> Financing Flexibility Declines
  |     ├-- Bond Investors Sell Off -> Spread Widening + Bond Issuance Difficulty
  |     └-- Equity Financing Hindered -> Capital Replenishment Capacity Declines
  |
  └-- Regulatory Scrutiny
        ├-- Special Inspections -> Compliance Costs Rise
        └-- Business Restrictions -> Growth Constrained
```

### 5.3 Reputational Risk Signal Checklist

#### 5.3.1 ESG Controversy Events

| Red Flag Signal | Detection Condition | Signal Severity | Data Source | Observability |
|---|---|---|---|---|
| **Major environmental accident** | Chemical leak, explosion, excessive emissions subject to environmental protection agency supervision | Strong | Environmental protection agency website "supervision" section, provincial environmental department disclosures | **Observable** — Environmental accidents are officially disclosed |
| **Labor dispute / strike** | Media reports or union announcements confirm large-scale strike / labor conflict | Medium-Strong | News databases, local labor inspection department disclosures | **Observable** — Large-scale labor disputes have media coverage |
| **Product quality scandal** | Product recalled / deemed to have safety hazards by regulators / subject to collective consumer complaints | Strong | National market regulation authority product defect management center, consumer associations, news | **Observable** — Product recalls require public announcement |
| **Data privacy controversy** | Regulatory investigation or media exposure due to illegal collection/use of user data | Medium | Cyber administration disclosures, industry regulatory notices | **Partially observable** — Only becomes public after regulatory intervention |
| **Supply chain ESG violation** | Core supplier found to have severe environmental pollution/child labor/forced labor exposed by international organizations | Medium | International NGO reports (e.g., Greenpeace, HRW), ESG rating agency reports | **Partially observable** — Requires third-party report to trigger |

#### 5.3.2 Media and Market Sentiment

| Red Flag Signal | Detection Condition | Signal Severity | Data Source |
|---|---|---|---|
| **Rating agency negative action** | Rating outlook changed from stable to negative / placed on negative watch list / rating downgraded | Strong | Rating agency announcements (S&P/Moody's/Fitch) |
| **Concentrated negative media coverage** | More than 3 in-depth negative reports targeting the same issue within 30 consecutive days | Medium | WebSearch news monitoring |
| **Social media sentiment outbreak** | Hot discussion on social media platforms (negative topic with significant readership) | Medium | Social media monitoring (publicly accessible influencer posts) |
| **Analysts collectively downgrade earnings forecasts** | Three or more covering analysts from different firms downgrade earnings forecasts > 15% in the same quarter | Medium | Broker research reports (public summaries) |
| **Short seller issues short report** | Short seller (e.g., Muddy Waters / Citron / GMT Research) issues short report targeting the company | Strong | Short seller websites, news |

#### 5.3.3 Client / Supplier Relationships

| Red Flag Signal | Detection Condition | Signal Severity | Data Source |
|---|---|---|---|
| **Core client publicly terminates partnership** | Procurement contract of one of top 5 clients confirmed not renewed upon expiration | Strong | Company announcements, client announcements (e.g., large enterprise procurement notices) |
| **Core supplier stops supply** | Raw material / key component supplier announces cessation of supply | Strong | Company announcements, industry media |
| **Channel partners / distributors collectively boycott** | Multiple distributors simultaneously stop purchasing / demand terms adjustment | Medium-Strong | Industry media, distributor association announcements |
| **Industry association expulsion / public censure** | Membership revoked or public censure issued by industry association | Medium | Industry association official website announcements |

**Data Limitation Note**: Changes in client and supplier relationships are **not publicly disclosed** in most cases. They can only be learned from announcements when they involve a material contract (meeting information disclosure standards) or when both parties are listed companies. For non-listed enterprises or entities without mandatory disclosure obligations, the detection capability for such signals is extremely low.

### 5.4 Reputational Risk Composite Judgment

| Assessment | Condition |
|---|---|
| **No Signal** | No ESG controversy, no negative media coverage, stable ratings |
| **Weak Signal** | Single minor ESG event (e.g., minor environmental fine) or 1-2 negative reports |
| **Moderate Signal** | Rating outlook downgraded to negative + one in-depth negative report, or moderate ESG event |
| **Strong Signal** | Rating downgrade + product recall / major environmental pollution + media coverage persisting for 3+ weeks |
| **Extreme Signal** | Short report + rating downgrade + client termination occurring simultaneously |

---

## 6. Strategic Risk Signals

### 6.1 Definition of Strategic Risk in Credit Analysis

Strategic Risk refers to the risk that a company loses its ability to continue as a going concern due to business model failure, flawed competitive strategy, technological disruption, or structural industry decline. This is the most difficult to quantify yet the most critical non-credit risk dimension — once triggered, all other analyses (financial health, supply chain quality, external support) become secondary.

### 6.2 Technology Disruption Risk

**Migration from Industry Pyramid L2 Technology Layer**: The L2 layer of the industry pyramid assesses "the competitive position of the current technology pathway," while technology disruption risk assesses whether "the current technology pathway **is being replaced**" — the difference is one of time dimension. When technology disruption signals are confirmed, the assessment should migrate from the L2 layer to this layer as a strategic risk.

| Disruption Mode | Historical Example | Impact on Credit | Warning Window |
|---|---|---|---|
| **Technology Pathway Replacement** | PERC -> TOPCon (Solar PV 2023-2025) | PERC capacity becomes sunk cost -> Asset impairment -> Losses -> Negative FCF | 12-18 months |
| **Product Replacement** | Internal combustion engine vehicles -> New energy vehicles (Automotive 2018-2025) | ICE vehicle supply chain revenue collapses -> Layoffs/plant closures -> Debt burden unsustainable | 24-36 months |
| **Business Model Disruption** | Traditional retail -> E-commerce (2010-2020) | Fixed costs of physical stores + personnel rigid -> Losses -> Debt default | 36-60 months |
| **Technology Paradigm Shift** | Feature phones -> Smartphones (2007-2013) | Legacy technology ecosystem completely abandoned -> Zero | 12-24 months |
| **Geopolitical Supply Cutoff** | Chip supply cut off after sanctions (2019) | Core product production halted -> Revenue zero | Immediate (no warning) |

**Signal Detection**:

| Signal | Detection Condition | Severity | Data Source |
|---|---|---|---|
| **Core product technology pathway deemed obsolete by mainstream market** | Product from that technology pathway no longer appears in procurement technical specifications | Strong | Central enterprise/state procurement announcements, industry technology white papers, procurement platforms |
| **Major competitors have all shifted to new technology pathway** | 3+ of top 5 industry players have fully transitioned to new technology | Strong | Industry technology forums, company announcement capacity plans, equipment procurement announcements |
| **R&D investment direction diverges from industry** | Company R&D investment concentrated on the obsolete pathway | Medium | Annual report R&D investment disclosures, patent office patent classifications |
| **Core product price falls below company cash cost** | Market price < Company cash cost (variable cost + necessary fixed cost allocation) | High | Price data (PVInfoLink/TrendForce) + Annual report cost data |
| **Core product market size continuously shrinking** | Market size for that product declined > 10% for 2 consecutive years | Medium-Strong | Industry association data, broker research reports |

**Industry-Specific Technology Disruption Signals** (refer to industry technology pathways in industry-framework.md):

| Industry | Current Mainstream Pathway | Potential Disruptive Pathway | Disruption Warning Source |
|---|---|---|---|
| Solar PV | TOPCon / BC | HJT + Perovskite Tandem (still in pre-production efficiency record stage) | PVInfoLink + BloombergNEF procurement efficiency requirement changes |
| Semiconductors | FinFET (3nm/5nm/7nm) | GAAFET (Gate-All-Around, Samsung 3nm already in production), Chiplet architecture | ISSCC/IEDM papers + tape-out data + equipment supplier ASML/AMAT announcements |
| Biopharmaceuticals | Small molecule + monoclonal antibody | ADC (Antibody-Drug Conjugates) / Bispecific antibodies / CAR-T / Cell and gene therapy | FDA NMPA new drug approval announcements + clinical trial results + Nature Biotechnology |
| New Energy Vehicles | BEV + PHEV | Solid-state batteries (if mass production breakthrough occurs), hydrogen fuel cells (commercial vehicles) | Battery technology announcements + range/safety independent testing |
| Data Centers | Air cooling | Liquid cooling (liquid cooling penetration accelerates beyond 30kW per rack) | PUE requirements + major technology company data center technical white papers |

### 6.3 Business Model Risk

| Signal | Detection Condition | Severity | Data Source |
|---|---|---|---|
| **Single product dependence > 60% facing substitution threat** | Revenue/gross profit of top 1 product > 60% | High | Annual report segment reporting, prospectus product composition |
| **Single client dependence > 40%** | Revenue from top 1 client > 40% (referencing L3 supply chain layer threshold) | High | Annual report client information disclosure |
| **Business model inherently structurally flawed** | E.g., P2P platforms, rental models with structural mismatch, prepayment model where funds are misappropriated | Strong | Industry analysis, regulatory policy documents |
| **Profit model dependent on unsustainable arbitrage** | E.g., subsidy arbitrage, regulatory arbitrage, tax arbitrage | Medium-Strong | Annual report government subsidy notes, industry policy documents |
| **Frequent strategy shifts (more than 1 major strategic change per year on average)** | More than 3 core business changes / major asset restructurings in the past 3 years | Medium | Company announcements, annual report board report |
| **Insufficient management strategic execution** | Target vs. actual results deviation > 30% for 2 consecutive years (e.g., capacity commissioning delays, revenue targets missed) | Medium | Annual report management discussion & analysis, forecast vs actual comparison |

### 6.3.1 Business Model Failure Trigger Conditions

| Trigger Condition | Detection Method | Warning Window | Severity |
|---|---|---|---|
| **Market share declining for 3 consecutive years while industry is shrinking** | Market share data (industry association / company announcements) declining for 3 years + total industry negative growth for 3 consecutive years | 6-12 months | Strong — dual-confirmed existential crisis |
| **Technology replacement window < 3 years** | Core product technology pathway deemed a "transitional technology" by mainstream market and competitors have fully shifted to new technology | 12-18 months | Strong — fatal time window confirmed by Harvard Business School "disruptive innovation" framework |
| **Core product price falls below cash cost** | Market price persistently below enterprise cash cost (variable cost + necessary fixed cost allocation) for more than 2 quarters | 3-6 months | Extreme — every unit of production consumes cash, FCF negative with no reversal possible |
| **Funding channels systematically close due to business model concerns** | Banks / bond market / equity financing simultaneously and explicitly tighten, and enterprise has no alternative funding channels available | Immediate | Extreme — funding cutoff means even good assets cannot sustain operations |
| **Operating cash flow negative for 2 consecutive years and cash runway < 12 months** | Annual report CFO negative for 2 consecutive years + cash runway less than 12 months | 3-6 months | Strong — dual risk of impaired cash-generating function + limited safety margin |

**Business Model Failure Cascade Effect**:
```
Persistent Market Share Decline
  └---> Diseconomies of Scale (fixed costs cannot be spread)
       └---> Gross Margin Persistent Compression
            └---> R&D/Sales Investment Forced to Cut
                 └---> Product Competitiveness Further Declines
                      └---> Accelerated Market Share Decline (vicious cycle)
                           └---> Funding Channels Close -> Debt Default
```

**Correspondence with COSO ERM 2017**:
The COSO ERM 2017 framework requires "strategic objectives and business model viability" as the starting point for enterprise risk assessment. This trigger condition directly corresponds to COSO ERM's "Strategy & Objective-Setting" principle — when the business model itself is unsustainable, all strategic objectives based on that model are invalid.

### 6.4 Structural Industry Decline

| Signal | Detection Condition | Severity | Data Source |
|---|---|---|---|
| **Total industry size persistently shrinking (negative growth for 3 consecutive years)** | Industry size declining YoY for 3 consecutive years | Strong | National statistics bureau industry data, industry association annual reports |
| **Policy designates the industry as "restricted/eliminated"** | Listed in the Industrial Structure Adjustment Guidance Catalog as restricted or eliminated category | Strong | National development/reform authority industry guidance catalog, ministry of industry access conditions |
| **Systemic industry losses (> 50% of companies loss-making)** | Loss-making enterprises among listed peers > 50% | Strong | Listed company quarterly/annual reports (industry comparable companies) |
| **Large-scale industry exits / bankruptcies** | Number of enterprises in the industry persistently declining (exit rate > 10% for 2 consecutive years) | Medium-Strong | Business deregistration data, industry association statistics |
| **Systematic tightening of funding channels for the industry** | Banks/bond market explicitly tightening credit policies for the industry | Medium | Central bank / financial regulator window guidance documents, broker industry research reports |

### 6.5 Strategic Risk Composite Judgment

| Assessment | Condition |
|---|---|
| **No Signal** | Business model clear and sustainable, industry in growth or mature stage |
| **Weak Signal** | High single product dependence but substitution threat not yet clear, or industry growth slowing but not shrinking |
| **Moderate Signal** | Technology disruption trend has emerged but not yet large-scale replacement, or high single client dependence with emerging substitution threats |
| **Strong Signal** | Technology pathway confirmed obsolete (e.g., PERC post-2024) + enterprise has not completed transition |
| **Extreme Signal (triggers veto)** | Core business model completely disrupted with no possibility of transition (e.g., feature phone maker still committed to Symbian in 2012) |

**Strategic Risk Veto Trigger Conditions**:

> When the following conditions are simultaneously met, the strategic risk signal triggers a veto, and the composite rating ceiling is capped at CCC:
> 1. The core product/technology pathway has been **confirmed obsolete** by market consensus (industry procurement tenders no longer feature products on this pathway)
> 2. The enterprise has **not completed** the transition to the new technology pathway and the transition window has largely closed (no technology reserves, no R&D plan, no relevant patents or personnel allocation)
> 3. No clear external support party (such as government/parent company) can provide the capital and resources needed for transition

**Summary of Non-Credit Risk Dimension Veto Ceilings**:

| Risk Dimension | Veto / Hard Cap Type | Rating Ceiling | Description |
|---|---|---|---|
| Market Risk | To be defined | To be defined | No veto conditions currently defined for market risk |
| Operational Risk | To be defined | To be defined | No veto conditions currently defined for operational risk; governance/fraud risk veto covered by governance-fraud-risk.md (CCC) |
| Reputational Risk | To be defined | To be defined | No veto conditions currently defined for reputational risk |
| Strategic Risk | One-vote veto | **CCC** | Triggered when core business model is completely disrupted with no possibility of transition (see Section 6.5) |
| Liquidity Risk | To be defined | To be defined | No veto conditions currently defined for liquidity risk |

> **Note**: This table clarifies whether each non-credit risk dimension can trigger a veto and the corresponding ceiling. Undefined types are uniformly marked as "to be defined" to avoid confusion with issuer-level one-vote veto (CCC).

**Honest Labeling**: The judgment of technology disruption time windows carries the risk of "premature determination" — before disruption actually occurs, the market may continue using older technology for extended periods (referencing "semiconductor lithography: 193nm immersion lithography was used for nearly 20 years before being replaced by EUV"). This framework uses **observable industry signals** (changes in procurement technical specifications, competitor capacity conversion, national/industry technical standards revisions) as trigger bases, rather than predictive judgment.

---

## 7. Liquidity Risk Signals

### 7.1 Definition of Liquidity Risk in Credit Analysis

Liquidity Risk in this module specifically refers to **Funding Liquidity Risk** — the risk that a company cannot obtain sufficient funds at a reasonable cost to meet its maturing debt obligations. This content is **partially extracted and expanded** from the debt maturity schedule (C.3) and bank credit facility coverage ratio (C.4) in financial-deep-dive.md.

### 7.2 Transmission Path of Liquidity Risk to Credit

```
Funding Channel Tightening
  ├-- Bank credit facilities withdrawn/limits reduced -> Backup liquidity declines
  ├-- Bond issuance failure/delayed -> Expected funding falls through
  ├-- Equity (private placement/rights offering) fails -> Capital replenishment interrupted
  |
  Maturing Debt Pressure
  ├-- Short-term debt concentrated maturities -> High refinancing demand
  ├-- Bank credit facility utilization near ceiling -> Flexible capacity exhausted
  |
  Trigger Scenario
  └-- Any negative market event
        └-- Funding channels simultaneously close -> Liquidity crisis -> Default
```

### 7.3 Liquidity Risk Signal Checklist

#### 7.3.1 Funding Channel Concentration

| Red Flag Signal | Detection Condition | Signal Severity | Data Source |
|---|---|---|---|
| **Excessive reliance on a single funding channel** | Single funding channel (e.g., bank borrowings only or bond issuance only) accounts for > 80% | Medium | Annual report notes borrowings classification + financing structure analysis |
| **High dependence on bond market** | Bonds payable / total interest-bearing debt > 50% (especially when bond market conditions deteriorate) | Medium | Annual report bonds payable notes |
| **Excessively high related-party financing proportion** | Related-party borrowings / total interest-bearing debt > 30% | Medium-Strong | Annual report related-party transaction notes |
| **Historically narrow funding channels** | Only 1-2 financing methods used in the past 3 years (e.g., only bank borrowings + shareholder loans, never issued bonds or equity) | Medium | Annual report financing activity analysis, prospectus |

#### 7.3.2 Bank Credit Facility Utilization

| Red Flag Signal | Detection Condition | Signal Severity | Data Source |
|---|---|---|---|
| **Credit facility utilization > 80%** | Utilized credit limit / total credit limit > 80% | Medium-Strong | Annual report "bank credit facilities" notes (usually disclosed in board report or management discussion) |
| **Credit facility utilization > 95%** | Approaching ceiling, financing flexibility nearly zero | Strong | Same as above |
| **Credit limit reduced > 20% in the year** | Total credit limit for current year decreased > 20% compared to prior year | Strong | Annual report comparing credit limits across periods |
| **High credit concentration** | Top 3 credit banks account for > 70% of total credit facilities | Medium | Annual report bank credit facility notes (some companies disclose bank distribution) |

**Data Limitation Note**: Disclosure of bank credit facility utilization and credit bank distribution is not mandatory. Among exchange-listed companies, approximately 60-70% disclose credit limits in the annual report's "Management Discussion & Analysis" or "Notes to Financial Statements," but non-listed companies and some listed companies may not disclose fully. When this data is missing, this module marks it as "Data unavailable (not disclosed)" rather than "No risk."

#### 7.3.3 Bond Issuance Cancellation / Delay Records

| Red Flag Signal | Detection Condition | Signal Severity | Data Source |
|---|---|---|---|
| **Bond issuance cancelled / postponed** | Company announcement "cancellation of issuance" or "postponement of issuance" (due to market conditions / insufficient investor subscription / price disagreement) | Strong | Bond market information platform, clearing house, exchange bond announcements |
| **Issuance rate significantly higher than expected** | Actual issuance rate exceeds upper end of initial price inquiry range by > 50bp | Medium-Strong | Issuance result announcement vs. initial price inquiry announcement comparison |
| **Issuance size significantly reduced** | Actual issuance size < 70% of planned issuance size | Medium-Strong | Issuance result announcement |
| **No recent successful financing record** | No bonds successfully issued or no new loans obtained in the past 6 months | Medium | No public financing announcement = potential financing difficulty signal (requires combination with other signals) |
| **Investment-grade issuer issuance rate abnormally high** | AAA/AA+ rated issuer issuance rate exceeds same-rating same-tenor average by > 100bp | Medium-Strong | Issuance result announcement + central bond yield curve |

#### 7.3.4 Short-Term Debt Maturity Concentration

**Extracted and expanded from financial-deep-dive.md C.3**:

| Red Flag Signal | Detection Condition | Signal Severity | Data Source |
|---|---|---|---|
| **More than 50% of total debt maturing in the next 12 months** | Refer to financial-deep-dive.md C.3 hazard classification | High | financial-deep-dive.md C.3 + annual report notes debt maturity schedule |
| **Single-month concentrated maturity > 20%** | Debt maturing in a single month accounts for > 20% of total debt | High | Same as above |
| **Short-term debt / total interest-bearing debt > 60%** | Short-term borrowings + current portion of non-current liabilities / total interest-bearing debt | Medium-Strong | Annual report balance sheet + notes |
| **High rollover reliance** | > 50% of debt maturing in the next 12 months is bonds that need to be rolled over in the bond market | Medium-Strong | Debt maturity schedule + bond market condition assessment |

#### 7.3.5 Cash Reserves and Resilience

| Red Flag Signal | Detection Condition | Signal Severity | Data Source |
|---|---|---|---|
| **Cash runway < 6 months** | (Cash + cash equivalents + trading financial assets) / (monthly cash operating costs + average monthly maturing debt) < 6 | Strong | financial-deep-dive.md E.4/E.5 + annual report cash flow statement |
| **Restricted cash ratio > 50%** | Restricted cash / total cash > 50% (margin deposits / escrow accounts / pledged deposits) | Medium-Strong | Annual report cash notes (restricted cash details) |
| **Cash / short-term debt < 0.5x** | Cash / (short-term borrowings + current portion of non-current liabilities) < 0.5x | Strong | Annual report balance sheet |
| **Undrawn credit / short-term debt < 1.0x** | Undrawn credit facilities / debt maturing in next 12 months < 1.0x | Strong | financial-deep-dive.md C.4 + annual report credit disclosure |

**Liquidity-Related Sections Extracted from financial-deep-dive.md**:

| Section | Extracted Content | Position in This Module |
|---|---|---|
| C.3 Hazard Classification | Proportion of debt maturing in next 12 months assessment (green/yellow/orange/red) | 7.3.4 Short-Term Debt Maturity Concentration |
| C.4 Bank Credit Facility Coverage Ratio | Undrawn credit / debt maturing in next 12 months | 7.3.2 Bank Credit Facility Utilization + 7.3.5 Cash Reserves |
| D.2 FCF Classification Matrix | Persistently negative FCF = dependent on external financing | 7.3.5 Cash Runway (negative FCF affects runway length) |

### 7.4 Liquidity Risk Composite Judgment

| Assessment | Condition |
|---|---|
| **Low** | Credit facility utilization < 50% + next 12 months maturities < 30% + cash runway > 12 months |
| **Medium** | Any single dimension reaches watch threshold (utilization 50-80% / maturities 30-50% / cash runway 6-12 months) |
| **High** | Two dimensions reach danger threshold (utilization > 80% or maturities > 50% or cash runway < 6 months) |
| **Very High** | Utilization > 95% + maturities > 50% + cash runway < 6 months + bond issuance cancellation record |

---

## 8. Overlay Adjustment Rules

### 8.1 General Adjustment Principles

| Non-Credit Risk Signal Severity | Adjustment Magnitude | Trigger Condition |
|---|---|---|
| **No Signal** | 0 | All dimensions normal (all dimension composite ratings are "Low" or "No Signal") |
| **Weak Signal (single dimension, low impact)** | **0** | Only 1 dimension shows weak signal (e.g., single minor environmental fine); note the risk but do not adjust rating |
| **Moderate Signal (1-2 dimensions, moderate impact)** | **±0.5 notch** | 1-2 dimensions reach "Moderate" risk rating (e.g., market risk elevated but manageable + minor reputational event) |
| **Strong Signal (2+ dimensions, high impact)** | **±1 notch** | 2 or more dimensions reach "Strong/High" risk rating (e.g., reputational event + regulatory penalty triggered simultaneously) |
| **Extreme Signal** | **Triggers veto** | Core business model completely disrupted with no possibility of transition (strategic risk extreme signal trigger conditions in Section 6.5) |

**Adjustment Direction**:

- **Downgrade (negative adjustment)**: Applies in the vast majority of scenarios. The existence of non-credit risk almost always increases credit risk, so the rating is typically downgraded when signals are detected.
- **Upgrade (positive adjustment)**: Very rare scenarios. Considered only when the following conditions are simultaneously met:
  1. A previously downgraded entity due to non-credit risk, where that risk has been clearly eliminated (e.g., regulatory penalty closed, management stabilized)
  2. The external support framework has confirmed "capability + willingness both strong" and no signals from non-credit risk dimensions

### 8.2 Step Size and Operational Rules

| Rule | Content |
|---|---|
| **Unit** | Adjustments use 0.5 notch as the minimum step size (1 notch = one rating step, e.g., BB+ to BB-) |
| **Single Adjustment Cap** | Non-credit risk overlay adjustment does not exceed ±1 notch (single trigger) |
| **Cumulative Cap** | Cumulative adjustments from non-credit risk overlay for the same entity within 12 consecutive months do not exceed ±2 notches |
| **Minimum Trigger Condition** | At least 1 risk dimension must reach "Moderate" rating to trigger adjustment (single "Weak Signal" does not trigger adjustment) |
| **Order of Application** | External support upgrade applied first -> then non-credit risk overlay adjustment (final rating = baseline rating + external support adjustment + non-credit risk adjustment) |
| **Minimum Rating Constraint** | Rating after non-credit risk overlay adjustment is subject to the veto ceiling of each dimension; defined strategic risk one-vote veto ceiling is CCC, other dimension veto ceilings to be defined (see Section 6.5 summary table) |
| **Adjustment Annotation** | Each adjustment must be accompanied by a "Non-Credit Risk Adjustment Explanation" in the analysis conclusion |

### 8.3 Adjustment Output Example

```yaml
# Non-Credit Risk Adjustment Explanation
base_rating: BB+                     # Pyramid baseline rating
external_support_adjustment: +1      # External support upgrade by 1 notch (to BBB-)
non_credit_risk_adjustment: -0.5     # Non-credit risk overlay downgrade by 0.5 notch

final_rating: BB+                    # Baseline BB+ +1 notch -0.5 notch = effectively BB+ unchanged
non_credit_risk_detail:
  market_risk: "Moderate (foreign currency revenue 35% + floating rate borrowings 25% + FX unhedged)"
  operational_risk: "Weak signal (single environmental fine)"
  reputation_risk: "No signal"
  strategic_risk: "No signal (technology pathway tracking normal)"
  liquidity_risk: "Low (credit utilization 35% + even maturity schedule + cash runway 14 months)"
adjustment_rationale: "Market risk moderate (FX exposure + floating rate debt) triggers -0.5 adjustment, but ample liquidity and external support form a buffer"
```

### 8.4 Rating Adjustment Example: LONGi Green Energy Non-Credit Risk Overlay

> **Context**: LONGi Green Energy (601012) faced multi-dimensional non-credit risk signals in 2025-2026, but each had clear mitigating factors.

```yaml
# Non-Credit Risk Adjustment Explanation · LONGi Green Energy 2026 Q1
base_rating: BBB-                    # Pyramid baseline rating (cycle resilience confirmed, but cyclical losses weigh)
external_support_adjustment: 0       # No clear government/parent company support (listed private enterprise)
non_credit_risk_adjustment: -0.5     # Non-credit risk overlay downgrade by 0.5 notch

final_rating: BB+                    # BBB- + 0 - 0.5 = BB+/BBB- boundary, take BB+
 
non_credit_risk_detail:
  market_risk: "Moderate (overseas revenue 44.7% + FX risk partially hedged + commodity price risk buffered by vertical integration)"
  operational_risk: "Weak signal (industry overcapacity leading to partial PERC line idling, but not a management deficiency)"
  reputation_risk: "Weak signal (rating agencies maintain stable outlook, but market questions credit quality after persistent losses)"
  strategic_risk: "Moderate (BC technology pathway faces long-term substitution pressure from HJT+Perovskite tandem, but transition window > 5 years, not a short-term risk)"
  liquidity_risk: "Low (52.6 billion cash reserve covers interest-bearing debt 3.5x / CFO turned positive in 2025 at +4.359 billion / ample credit facilities)"

adjustment_rationale: >
  Strategic risk moderate triggers -0.5 notch adjustment. Although BC technology is currently
  leading (mass production efficiency 24.8% / 50.3GW awarded in central enterprise procurement),
  HJT+Perovskite tandem efficiency record has reached 33.7% (2025), suggesting a technology
  replacement window of approximately 5-8 years — not an imminent fatality, but within the
  scope of COSO ERM's "strategic objective viability assessment." Ample liquidity
  (52.6 billion cash + 4.359 billion positive CFO) forms a buffer, preventing a larger
  downgrade. If BC technology premium disappears or technology substitution accelerates
  in the next 2 years, the adjustment magnitude should be reassessed.
  
adjustment_likely_reversal: >
  The driver of the -0.5 notch downgrade is "long-term technology substitution uncertainty,"
  not short-term liquidity or profitability deterioration.
  Possible reversal triggers: (1) BC technology iteration proves a smooth transition to the next
  generation; (2) the company initiates Perovskite tandem R&D and achieves verifiable progress;
  (3) the industry cycle bottoms out and gross margin recovers above 5%.
  Estimated reversal window: 12-18 months.
```

**Key Design Notes**:
1. This example demonstrates the complete logic chain of "moderate risk triggering -0.5 notch adjustment" — the most common scenario in overlay adjustments
2. The buffering/amplifying relationships between independent risk dimensions are explicitly evaluated (ample liquidity buffers the magnitude of the strategic risk downgrade)
3. "Reversibility assessment" of the adjustment is included in the output — the downgrade is not permanent, and reversal conditions are explicitly listed
4. Consistent with LONGi Green Energy's actual financial characteristics (52.6 billion cash, 4.359 billion positive CFO, technology improvement expectations)

### 8.5 Linkage with Baseline Rating Confidence

The confidence level of the non-credit risk overlay adjustment should be reflected in the final rating's confidence annotation:

| Data Completeness of Overlay Adjustment | Final Rating Confidence |
|---|---|
| All dimension data available (full annual reports, market data accessible) | No reduction in confidence |
| 1-2 dimensions partially missing | Confidence reduced by one level (e.g., High -> Medium-High) |
| 3 or more dimensions severely missing | Confidence reduced by two levels, annotated as "Due to missing non-credit risk data, the adjustment judgment carries uncertainty" |

---

## 9. Signal Aggregation and Scoring Rules

### 9.1 Non-Credit Risk Scorecard

| Risk Dimension | Scoring Factors | Weight | Data Source Dependence | Data Availability |
|---|---|---|---|---|
| **Market Risk** | Interest rate exposure, FX exposure, commodity price exposure; take the highest risk level among the three | 20% | Annual report notes + macro data | Relatively high (annual report notes + public price indices) |
| **Operational Risk** | Regulatory penalties, key personnel, legal litigation, fraud signals; scored by signal severity | 30% | Company announcements + regulatory disclosures + judicial public records | Medium (only externalized events measurable) |
| **Reputational Risk** | ESG event severity, media negative density, rating agency actions; composite score | 15% | News + rating agency announcements + ESG data | Medium (depends on media and public ratings) |
| **Strategic Risk** | Technology disruption severity, business model sustainability, industry trends; composite score | 25% | Procurement tenders + industry technology reports + policy documents | Relatively high (technology pathway and industry trend data accessible) |
| **Liquidity Risk** | Funding channel concentration, credit facility utilization, cash runway, maturity concentration | 10% | Annual report notes + bond market information platform | Medium (credit data partially undisclosed) |

**Weight Note**: Operational risk and strategic risk carry the highest weights because these two types of risk have the most profound and irreversible impact on credit quality (referencing the default genotypes of Yongmei/Ziguang/Brilliance Auto). Market risk and reputational risk affect credit more through intermediary transmission pathways, while liquidity risk is "the straw that breaks the camel's back" — already partially covered in credit risk analysis through the L4 financial layer and debt maturity schedule.

### 9.2 Composite Signal Strength Calculation

```
Non-Credit Risk Composite Score = Σ(Each Dimension Risk Score × Dimension Weight)

Dimension Risk Scores:
  No Signal     = 0
  Weak Signal   = 1
  Moderate Signal = 2
  Strong Signal = 3
  Extreme Signal = 4 (triggers veto)

Composite Score Thresholds:
  0 - 0.5     -> No Signal (no adjustment)
  0.5 - 1.5   -> Weak Signal (no adjustment, mark risk)
  1.5 - 2.5   -> Moderate Signal (±0.5 notch adjustment)
  2.5 - 3.5   -> Strong Signal (±1 notch adjustment)
  > 3.5       -> Extreme Signal (triggers veto)
```

### 9.3 Cross-Validation of Signal Overlap

When the same event triggers signals across multiple dimensions simultaneously, the following stacking rules apply:

| Scenario | Processing Rule | Example |
|---|---|---|
| **Same event triggers multi-dimensional signals** | Count as 1 event, but select the most severe dimension direction for scoring | Product quality scandal simultaneously triggers reputational risk (strong) + operational risk (product quality regulatory penalty = medium); take strong signal as adjustment basis |
| **Cross-dimensional signal intensity stacking** | When 2+ dimensions simultaneously reach "Moderate," take one step higher than single dimension signal intensity | Operational risk (moderate) + market risk (moderate) + liquidity risk (moderate) = composite "Strong signal" |
| **Conflicting signals (opposite directions on same dimension)** | Whichever signal is most recent prevails (time-weighted) | Company had operational risk penalty in 2025 (strong signal), but has rectified by 2026 with no new violations; take 2026 status |
| **Repeated signals** | Repeated occurrence of same nature of events counts as severity escalation, not count accumulation | Second environmental penalty -> signal severity upgraded from moderate to strong |

---

## 10. Integration with Existing Frameworks

### 10.1 Integration in dual-track-methodology.md

Insert a new "Non-Credit Risk Overlay" section between "7. Decision Rules" and "8. Risk Mitigation Recommendation Framework."

**New Position**: After Step 4 (Rating Mapping), before Step 5 (Cross-Collision).

**Reference Text for New Section**:

```
## [New] Non-Credit Risk Overlay

After the baseline credit rating (including external support adjustment) is completed, run the non-credit risk overlay:

1. Scan all signals across the five non-credit risk dimensions (market/operational/reputational/strategic/liquidity)
2. Calculate composite signal strength (scoring rules in Section 9.2)
3. Trigger overlay adjustment based on signal strength (adjustment rules in Section 8.1)
4. Output adjusted final rating + adjustment explanation

The post-overlay rating enters the cross-collision matrix for cross-validation with Track B market pricing signals:
  - If Track B spreads/prices already reflect the non-credit risk signals -> Overlay adjustment is consistent with market pricing, confidence enhanced
  - If Track B has not reflected the non-credit risk signals -> Market may not yet have priced in the risk, overlay adjustment retained
  - If Track B reflects non-credit risk signals but the overlay layer did not detect them -> There may be risks not covered by the engine
```

### 10.2 Integration in mosaic-engine.md

**Add non-credit risk gaps to the "Gap -> Risk Mapping Table" (Section 5.2)**:

| Gap Type | Typical Missing Data | Corresponding Information Risk | Alternative Signal |
|---|---|---|---|
| **Operational Risk** | Internal process deficiencies (approval loopholes/undisclosed employee misconduct) | May overestimate actual management control level | Audit opinion type + internal control audit report + exposed incident records; annotate "internal deficiencies unobservable" |
| **Reputational Risk** | Reputation perception changes of non-listed companies / non-public figures | Cannot track reputation changes in real time | Only rely on observable ESG events + regulatory penalties + rating agency actions; annotate "reputational risk detection only covers publicly disclosed events" |
| **Market Risk** | Precise duration/convexity data | Estimation error in interest rate sensitivity | Substitute using remaining debt maturity approximation; annotate "estimated value" |
| **Liquidity Risk** | Bank distribution and maturity of credit facilities | Cannot assess credit concentration and remaining tenor | Only rely on aggregated disclosed data; annotate "partial bank credit data not disclosed" |
| **Strategic Risk** | Internal company technology roadmaps / R&D pipelines | Disruption signals may have 3-12 months of information lag | Industry technology forums + procurement technical specifications + competitor capacity announcements; annotate "inference based on public industry signals" |

**Add a "Non-Credit Risk" dimension to the signal density bar chart in the completeness assessment layer (Section 5.1)**:

```
Signal Density Bar Chart (Updated):
+---------------------------------------------------+
| L1 Policy/Macro        ████████░░ 82%             |
| L2 Technology/Competition ██████░░░░ 75%          |
| L3 Supply Chain/Operations ████░░░░░░ 48% ⚠️      |
| L4 Financial/Debt Service █████████░ 89%          |
| L5 External Support     ████░░░░░░ 45% ⚠️         |
| Market Pricing (Track B) ███░░░░░░░ 35% ⚠️        |
| ★Non-Credit Risk Overlay ███░░░░░░░ 38% ⚠️        |  <- Added
+---------------------------------------------------+
```

### 10.3 Integration in outlook-monitoring-framework.md

**Add non-credit risk event trigger conditions to the monitoring matrix**:

| New Monitoring Item | Frequency | Data Source | Trigger for Reassessment | Priority |
|---|---|---|---|---|
| **Market Risk Signals** | Quarterly | Central bank benchmark rate announcements + exchange rate fix + industry raw material price indices | Rate increase > 100bp / local currency depreciation > 5% / raw material price jump > 20% with enterprise exposure | P1 |
| **Operational Risk Events** | Real-time | Company announcements + securities regulator / financial regulator / exchange disclosures | Securities regulator investigation / CFO departure / major administrative penalty | P0 |
| **Reputational Risk Events** | Weekly | WebSearch news monitoring + rating agency announcements | Rating outlook downgrade / product quality recall / major environmental accident / short report published | P1 |
| **Strategic Risk Events** | Monthly | Industry technology forums + procurement announcements + policy documents | Top 3 industry players simultaneously shift to new technology / core product restricted by policy / breakthrough technology substitution | P1 |
| **Liquidity Risk Events** | Real-time | Bond market information platform + exchange announcements | Bond issuance cancelled / credit facility withdrawn / short-term debt ratio jumps > 10pp | P0 |

**Expand the scope of "trigger conditions for reassessment" in the monitoring matrix**: Add "rating downgrade after non-credit risk overlay" as one of the trigger conditions for reassessment, in addition to existing P0 monitoring items.

### 10.4 Integration Annotation in governance-fraud-risk.md

**Add the following explanation at the beginning of that document or at relevant sections**:

> **Relationship with This Module**: The fraud signals and management governance red flags detected by the Governance and Financial Fraud Risk Analysis module (governance-fraud-risk.md) are classified in this module as a **subset of operational risk**. These signals are extracted from the specialized detection framework of governance-fraud-risk.md and then aggregated into the operational risk dimension of this module (Section 4.3), where they are combined with regulatory penalties, key personnel risk, legal litigation, and other signals to calculate the operational risk composite score.

### 10.5 Integration in industry-framework.md

**Add a reference to "Strategic Risk - Technology Disruption Signals" in the L1 layer or a standalone annotation of each industry pyramid**:

```
At the end of the L2 Technology layer of each industry pyramid, add the following annotation:
  ⚠️ Linkage between L2 Technology Layer Signals and Strategic Risk (Non-Credit Risk Overlay Layer):
    When the risk of "technology pathway obsolescence" assessed by the L2 Technology Layer
    reaches a critical point, the signal should be simultaneously relayed to the non-credit risk
    overlay layer (strategic_risk dimension).
    See non-credit-risk-overlay.md Section 6.2 for details.
```

---

## 11. Honest Labeling Under Public Data Constraints

### 11.1 Fundamental Limitations of Non-Credit Risk Detection

| Risk Dimension | Observable Proportion (Estimated) | Unobservable Portion | Impact on Assessment |
|---|---|---|---|
| **Market Risk** | 60-70% | Precise duration/convexity, complete hedging strategy, internal stress test results | Estimation error within acceptable range, does not affect directional judgment |
| **Operational Risk** | 30-40% | Internal process deficiencies (not externalized), employee misconduct (not disclosed), fraud attempts (undetected) | **Weakest detection capability dimension** — most operational risk events are only observable after losses have materialized |
| **Reputational Risk** | 40-50% | Gradually accumulating but not yet erupted negative sentiment, non-media channel reputation deterioration, privately deteriorating B2B client relationships | Only captures publicly disclosed events, may miss silent reputation deterioration |
| **Strategic Risk** | 55-65% | Internal technology roadmaps, R&D pipelines (unfiled patents), management's true strategic intent | Technology disruption signals have 3-12 months of information lag (from internal decision to public observability) |
| **Liquidity Risk** | 50-60% | Bank distribution and maturity of credit facilities, changes in bank internal ratings, financing arrangements with non-financial institutions | Aggregated data accessible but detail insufficient |

### 11.2 Detection Capability by Entity Type

| Entity Type | Market Risk | Operational Risk | Reputational Risk | Strategic Risk | Liquidity Risk | Overall Detection Capability |
|---|---|---|---|---|---|---|
| **Listed company (with bonds)** | Relatively High | Medium-High | Medium-High | Relatively High | Medium-High | **Best** |
| **Listed company (without bonds)** | Relatively High | Medium-High | Medium-High | Relatively High | Medium | **Good** |
| **Non-listed bond-issuing company** | Medium | Medium | Medium | Medium | Medium | **Moderate** (no share price/market sentiment signals) |
| **Non-listed, non-bond-issuing company** | Low | Low | Low | Medium | Low | **Weak** (heavily reliant on annual reports + industry inference) |
| **Single-purpose entity (SPV)** | Low | Low | Low | Low | Medium | **Weak** (barely any public data) |

### 11.3 Honest Disclosure

> **Non-Credit Risk Overlay Disclosure**: The non-credit risk assessment (Market Risk / Operational Risk / Reputational Risk / Strategic Risk / Liquidity Risk) for [Entity Name] in this module is based on signal detection and inference from publicly available data. The following limitations have been identified:
>
> 1. **Only externalized signals are captured**: A substantial number of undisclosed internal deficiencies in operational and reputational risk cannot be detected. This module's detection capability is limited to events that have been externalized through channels such as regulatory penalties, company announcements, media reports, or judicial disclosures.
>
> 2. **Signals inherently lag**: There is a time gap between the occurrence of a risk and the availability of an observable public signal (regulatory penalties typically lag by 3-12 months, legal litigation by 6-24 months). This module cannot provide real-time early warnings.
>
> 3. **Significantly reduced detection capability for non-listed entities**: For companies that are not listed and do not issue bonds, non-credit risk data sources are limited, and detection capability may drop to 30-50% of that for publicly listed companies.
>
> 4. **Force majeure is outside the scope**: External shocks such as earthquakes, war, pandemics, systemic financial crises are not within the scope of this module's non-credit risk assessment.
>
> 5. **This module is an overlay, not an independent rating framework**: Non-credit risk signals do not replace the analytical conclusions of the credit pyramid; they can only make ±1 notch adjustments to the baseline rating. The final judgment on credit quality should primarily rely on the credit pyramid's baseline rating.

### 11.4 Comparison with Other "Honest Labeling" Sections

| Existing Framework | Honest Labeling | Corresponding Section in This Module |
|---|---|---|
| external-support-framework.md 10.3 | "External support illusion" — support is not always guaranteed | Non-credit risk illusion — unexposed risk does not equal nonexistent risk |
| dual-track-methodology.md 5.3 | Data completeness report | Non-credit risk data completeness annotation |
| outlook-monitoring-framework.md 7.1 | Inherent limitations of outlook | Inherent limitations of non-credit risk signal detection |
| mosaic-engine.md 5.1 | Signal density indicator | Signal density for each non-credit risk dimension |

---

## Appendix A: Data Source Inventory by Risk Dimension

### Market Risk

| Data Item | Specific Data Source | Free/Paid | Update Frequency |
|---|---|---|---|
| Central bank benchmark interest rate | Central bank official website | Free | Real-time |
| Benchmark lending rate quotes | National interbank lending center | Free | Monthly (20th) |
| RMB exchange rate fix | China Foreign Exchange Trade System | Free | Daily |
| SMM non-ferrous metal prices | Shanghai Metals Market (smm.cn) | Partially free | Daily |
| LME metal prices | London Metal Exchange | Free | Daily |
| PVInfoLink solar pricing | PVInfoLink | Partially free | Weekly |
| TrendForce pricing | TrendForce | Partially free | Weekly |
| Mysteel steel pricing | Mysteel | Partially free | Daily |

### Operational Risk

| Data Item | Specific Data Source | Free/Paid | Update Frequency |
|---|---|---|---|
| Securities regulator investigation | Securities regulator official website, company announcements | Free | Real-time |
| Exchange regulatory sanctions | Stock exchange regulatory information disclosure sections | Free | Real-time |
| Environmental administrative penalties | Environmental protection agency website "administrative penalties" section | Free | Real-time |
| Court judgments | National court judgment database | Free | Real-time |
| Enforcement information | National enforcement information disclosure platform | Free | Real-time |
| Company announcements | Company filing platform, clearing house, bond market information platform | Free | Real-time |
| Business registration changes | National enterprise credit information disclosure system, business information platforms | Basic free | Real-time |

### Reputational Risk

| Data Item | Specific Data Source | Free/Paid | Update Frequency |
|---|---|---|---|
| Rating agency announcements | S&P/Moody's/Fitch official websites | Free | Real-time |
| Product recalls | National market regulation authority product defect management center | Free | Real-time |
| ESG data | ESG rating agencies | Partially paid | Quarterly |
| News monitoring | WebSearch / news databases | Free (basic) | Real-time |
| Environmental accidents | Environmental protection agency website "supervision" section | Free | Real-time |

### Strategic Risk

| Data Item | Specific Data Source | Free/Paid | Update Frequency |
|---|---|---|---|
| Industry technical standards | National standardization authority | Free | Annually |
| Procurement technical specifications | Central/state procurement platforms | Free | Real-time |
| Capacity planning announcements | Listed company announcements, industry media | Free | Real-time |
| Industrial policy | National development/reform authority, ministry of industry official websites | Free | Real-time |
| Competitor technology pathways | Industry white papers, conference proceedings (SNEC solar/ISSCC semiconductor/ESMO medical) | Partially paid | Annual/semi-annual |

### Liquidity Risk

| Data Item | Specific Data Source | Free/Paid | Update Frequency |
|---|---|---|---|
| Debt maturity schedule | Annual report notes "current portion of non-current liabilities / short-term borrowings / bonds payable" | Free | Semi-annual/annual |
| Bank credit facilities | Annual report "bank credit facilities" notes (not mandatory disclosure) | Free | Annual |
| Bond issuance announcements | Bond market information platform, clearing house, exchange | Free | Real-time |
| Issuance cancellation announcements | Bond market information platform | Free | Real-time |
| Company cash data | Annual report / quarterly report cash flow statement | Free | Quarterly |

---

## Related Content

- [Engine Architecture Overview](engine-overview.md) — Core concepts, overall architecture, design principles
- [Dual-Track Analysis Methodology](dual-track-methodology.md) — Track A + Track B, cross-collision, rating mapping
- [Mosaic Engine](mosaic-engine.md) — Signal extraction, mosaic assembly, completeness assessment
- [Governance and Financial Fraud Risk Analysis Module](governance-fraud-risk.md) — Operational risk subset (fraud signals + management governance red flags)
- [Financial Deep Dive](financial-deep-dive.md) — Debt maturity schedule, bank credit facility coverage ratio, FCF analysis (liquidity risk sources)
- [External Support Assessment Framework](external-support-framework.md) — Similar overlay layer design pattern
- [Rating Outlook and Continuous Monitoring Framework](outlook-monitoring-framework.md) — Monitoring trigger conditions for non-credit risk events
- Risk Management Standards — Basel/COSO alignment for non-credit risk coverage
- [Industry Classification and Analysis Framework](industry-framework.md) — Technology pathways and disruption risk reference by industry
