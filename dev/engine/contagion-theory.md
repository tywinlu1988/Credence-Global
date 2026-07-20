# Contagion Theory -- Credit Risk Transmission Pathways and Sector Exposure Framework

**Version**: v0.0.2 | **Date**: 2026-07-10

---

## Table of Contents

1. [Introduction: Why Contagion Theory](#1-introduction-why-contagion-theory)
2. [Four Contagion Types](#2-four-contagion-types)
3. [Seven Standard Transmission Pathways](#3-seven-standard-transmission-pathways)
4. [Paradigm Contagion Exposure Mapping (P1-P6)](#4-paradigm-contagion-exposure-mapping-p1-p6)
5. [Contagion Intensity Escalation Factors](#5-contagion-intensity-escalation-factors)
6. [Practical Application Guide](#6-practical-application-guide)

---

## 1. Introduction: Why Contagion Theory

### 1.1 Background

Traditional credit analysis assumes **issuer-level standalone assessment** -- analysts evaluate each entity's credit quality independently through financial statements, industry position, governance, and other firm-specific factors. This assumption holds in normal market conditions but fails systematically during **periods of concentrated credit events**.

History demonstrates that credit risk is never an independent event:

| Event | Apparent Default Cause | Contagion Path | Affected Scope |
|---|---|---|---|
| Lehman Brothers (2008) | Subprime MBS losses | Counterparty chain + confidence collapse | Global financial system freeze, interbank lending halt |
| Greece sovereign downgrade (2010) | Fiscal deficit under-reporting | Sovereign-bank nexus + regional resonance | GIIPS sovereign spreads jumped 300-800bp, Eurozone crisis |
| Petrobras (2014-2015) | Corruption + oil price crash | Supply chain + sector concentration | Brazilian upstream suppliers, oil & gas sector-wide re-pricing |
| Vale dam collapse (2019) | Operational disaster | Financial linkage + sector concentration | Global mining sector liability re-pricing, iron ore price shock |
| Wirecard (2020) | Fraud exposure | Financial linkage + confidence collapse | German fintech sector freeze, auditor liability cascade |
| Evergrande (2021) | Liquidity crisis | Supply chain + sector concentration | Global high-yield property selloff, construction material suppliers |
| Credit Suisse (2023) | Repeated scandals + deposit run | Liquidity squeeze + confidence collapse | Global bank AT1 bond wipeout, regional bank contagion (US) |
| SVB / Signature Bank (2023) | Duration mismatch + deposit run | Liquidity squeeze + common creditor | US regional banking crisis, sector-wide deposit flight |

**Core thesis: In periods of concentrated credit events, the question "who else will be affected" is more important than "who will default first."**

### 1.2 Role of Contagion Theory in the Engine

Contagion theory does not replace fundamental analysis -- it adds a **systemic risk overlay layer** on top of fundamental assessment:

```
Existing Engine Output (Standalone Assessment)
            |
       +----+----+
       |Contagion |  <- This document defines the theoretical foundation
       |Analysis  |
       +----+----+
            |
       +----+----+
       |Contagion |  <- Each pathway x each entity's exposure score
       |Matrix   |
       +----+----+
            |
            v
   Contagion Risk Report
   "If X defaults, who is most likely to be affected?"
```

### 1.3 Key Terminology

| Term | Definition |
|---|---|
| **Contagion Source** | The entity that first experiences a credit event (default / downgrade / fraud exposure) |
| **Contagion Receptor** | An entity affected due to direct or indirect linkage to the source |
| **Transmission Pathway** | The specific channel through which contagion travels from source to receptor |
| **Decay Distance** | The number of steps along a pathway after which the impact materially diminishes |
| **Escalation Factor** | Market, regulatory, or leverage conditions that amplify transmission intensity non-linearly |
| **Exposure Score** | The expected degree of contagion impact on a specific receptor via a specific pathway (scale 1-5) |

---

## 2. Four Contagion Types

### 2.1 Type Overview

| Type | Definition | Trigger | Transmission Speed | Historical Amplitude | Decay Distance | Predictability |
|---|---|---|---|---|---|---|
| **Credit Chain (C)** | Transmission through upstream/downstream receivables, guarantees, and cash pooling | Core enterprise default or downgrade | Moderate (1-3 months via financial statements and payment behavior) | High (direct creditor losses) | 1-2 layers (direct counterparty, counterparty's counterparty) | Medium-High (supply chain relationships can be mapped in advance) |
| **Regional Resonance (R)** | Shared sovereign / regional credit backing, intra-region mutual guarantees, deterioration of regional funding conditions | First regional SOE default or shift in government support stance | Fast (days-weeks, rapid financial market reaction) | Very High (GIIPS sovereign spread widening 300-800bp) | Same jurisdiction, adjacent region, same economic bloc | Medium (government support willingness hard to predict) |
| **Liquidity Squeeze (L)** | Collective withdrawal from same funding channel, bond type, or investor base | Issuer default, investor redemption, forced fund selling of similar assets | Very Fast (intraday-days) | High (valuation shock + liquidity dry-up) | Same asset class, similar class, whole market | Low (depends on market sentiment and leverage levels) |
| **Confidence Collapse (S)** | Narrative-driven irrational contagion -- "who is next" panic | Unexpected default breaking implicit guarantee beliefs | Very Fast (hours-days) | Very High (indiscriminate selling) | No clear boundary, can affect unrelated sectors | Extremely Low |

### 2.2 Credit Chain Contagion

**Definition:** Credit risk propagates through **debtor-creditor relationships**, **guarantee arrangements**, and **operational cash flows** along supply chains or capital structures.

**Triggers:**
- Core enterprise default or credit rating downgrade
- Large-scale accounts payable delinquency by core enterprise
- Debt restructuring by core enterprise (discount repayment, debt-for-equity swaps)
- Guarantor insufficient to cover, triggering chain-compensation

**Transmission Speed: Moderate (1-3 months):**
- Phase 1 (1-2 weeks): News-driven shock -- supplier share price decline, valuation pressure
- Phase 2 (1-2 months): Supplier confirms receivables as unrecoverable, impairment recognized
- Phase 3 (2-3 months): Supplier's own liquidity tightens, cross-default clauses triggered

**Historical Amplitude: High**
- Lehman Brothers (2008): Money market fund "breaking the buck" (Reserve Primary Fund) triggered chain reaction across commercial paper market; counterparty losses cascaded through AIG, Bear Stearns
- Wirecard (2020): Partner banks and acquirers (NatWest, BNP Paribas, Citibank) faced contingent liability exposure from the fraud; softPOS/Fintech credit chain temporarily froze
- Evergrande (2021): Over 1,000 suppliers across construction materials, interior finishing, and home appliances faced bad debts at peak exposure

**Decay Distance: 1-2 layers**

| Layer | Impact Level | Description |
|---|---|---|
| Layer 1 (Direct Counterparty) | Severe (direct receivable loss) | Entities supplying goods/services directly to the defaulted enterprise |
| Layer 2 (Counterparty's Counterparty) | Moderate (indirect business volume reduction) | Entities supplying Layer 1, affected by its liquidity tightening |
| Layer 3+ | Limited (through indirect channels) | Impact largely attenuated |

**Predictability: Medium-High**
- Supply chain relationships can be pre-mapped through trade data, public filings, customer/supplier concentration disclosures
- Receivable aging analysis and concentration analysis identify most vulnerable receptors

### 2.3 Regional Resonance

**Definition:** Entities within the same jurisdiction experience synchronous credit risk elevation due to shared government credit backing, intra-region mutual guarantee networks, and common funding conditions.

**Triggers:**
- First regional sovereign/SOE default or rating downgrade
- Shift in government support stance (from "guaranteed bailout" toward "market discipline")
- Regional fiscal / economic data deterioration (GDP growth, fiscal revenue, land sales)
- Core node default in regional mutual guarantee network

**Transmission Speed: Fast (days-weeks):**
- Phase 1 (hours-1 day): Defaulted bond price crash, same-region credit spreads jump
- Phase 2 (days-1 week): Regional funding environment deteriorates (primary market issuance cancelled / rates surge)
- Phase 3 (1-4 weeks): Weak entities in region face rating downgrades

**Historical Amplitude: Very High**

| Event | Source | Scope | Amplitude |
|---|---|---|---|
| Greece downgrade (2010) | Greece sovereign | GIIPS (Portugal, Ireland, Italy, Spain) sovereign spreads | Greek 10Y spread from 400bp to >1,200bp; Ireland/Portugal spreads >600bp |
| Spain caja crisis (2011-2012) | Regional savings banks (cajas) | Spanish autonomous community debt re-pricing | Regional government bond yields differential opened 200-400bp vs central govt |
| Italian banking crisis (2016) | Monte dei Paschi, Veneto banks | Italian regional bank sector | All Italian bank CDS surged; regional cooperation banks sector-wide funding freeze |
| Credit Suisse collapse (2023) | CS AT1 wipeout | Global bank AT1 notes | AT1 market repriced 100-200bp across all European banks |

**Decay Distance: Same jurisdiction -> Adjacent region -> Same economic bloc**

| Layer | Impact Level | Description |
|---|---|---|
| Layer 1 (Same jurisdiction) | Extreme | Direct re-assessment of government credit support |
| Layer 2 (Adjacent/similar region) | Severe | e.g., Greece crisis -> Ireland/Portugal bond selloff |
| Layer 3 (Same economic bloc) | Moderate | Market analogizes to regions with similar economic structure |
| Layer 4 (Global same-type entities) | Limited | Only affects during extreme panic |

**Predictability: Medium**
- Government support willingness can be assessed through: historical bailout record, official policy statements, regional fiscal health
- Regional mutual guarantee networks can be mapped through corporate registry information and cross-shareholding disclosures

### 2.4 Liquidity Squeeze

**Definition:** When an issuer or asset class defaults, investors facing redemption pressure or risk-control limits are forced to mass-sell similar assets, causing a **self-fulfilling** price crash and liquidity dry-up.

**Triggers:**
- Issuer default -> funds / wealth management products holding the bond face redemptions
- Funds forced to sell similar-type assets (same sector/rating/funding channel) from portfolios
- Selling causes price declines -> more funds hit stop-loss -> forced additional selling

**Transmission Speed: Very Fast (intraday-days):**

| Phase | Time | Phenomenon |
|---|---|---|
| Phase 1 | T+0 to T+1 | Source defaults, related fund NAV drops, large redemption requests |
| Phase 2 | T+1 to T+3 | Funds forced to sell similar assets, valuation shock spreads |
| Phase 3 | T+3 to T+10 | Liquidity dry-up, primary and secondary markets freeze for the asset class |
| Phase 4 | T+10 to T+30 | High-leverage investors margin-called, selling spills to unrelated assets |

**Historical Amplitude: High**

| Event | Trigger | Liquidity Squeeze Process | Impact |
|---|---|---|---|
| GFC 2008 (Lehman) | Investment bank default | Prime brokerage assets frozen -> hedge funds redemption -> forced asset fire sale across all asset classes | Credit markets froze for 6+ months; interbank lending virtually halted; money market funds experienced "breaking the buck" |
| COVID crash (Mar 2020) | Pandemic-driven panic | Corporate bond ETFs liquidated -> forced selling of IG and HY bonds -> Treasury selloff (dash for cash) | IG credit spreads jumped from 100bp to 400bp; HY from 400bp to 1,100bp; Fed forced to intervene in corporate bond market for first time |
| Gilt crisis (UK, Sep 2022) | Fiscal event (mini-budget) | LDI (Liability-Driven Investment) funds hit margin calls -> forced gilt selling -> gilt yields surged 100bp in days | UK pension funds near systemic failure; BoE forced into emergency gilt purchase |
| US regional banking crisis (Mar 2023) | SVB failure | Uninsured deposit run -> sector-wide deposit flight -> forced asset sales of HTM bond portfolios | SVB, Signature, First Republic collapsed; regional bank CDS spreads surged 200-400bp |

**Decay Distance: Same asset class -> Similar class -> Whole market**

| Layer | Impact Level | Description |
|---|---|---|
| Layer 1 (Same asset class) | Extreme | e.g., SVB failure -> all regional bank stocks/bonds sold off indiscriminately |
| Layer 2 (Similar asset class) | Moderate-Severe | e.g., IG credit selloff spills into HY; bank stress spills into insurance CDS |
| Layer 3 (Whole market) | Limited-Moderate | Only during extreme liquidity shocks affecting even safe-haven assets |

**Predictability: Low**
- Depends on market sentiment and leverage -- same event in high-leverage/pessimistic market can trigger panic, while in low-leverage/optimistic market impact is limited
- Potential squeeze intensity can be estimated through fund concentration metrics, fund holding overlap ratios, and market leverage indicators

### 2.5 Confidence Collapse

**Definition:** Narrative-driven irrational contagion not based on real economic linkages. When an unexpected credit event breaks the market's "implicit guarantee" belief in a certain entity class, investors enter "who is next" panic mode and indiscriminately sell all potentially affected entities.

**Triggers:**
- **"Too big to fail" entity default** (Lehman 2008, breaking investment bank guarantee belief)
- **Systemically important financial institution failure** (Credit Suisse 2023, breaking "systemic bank protection" belief)
- **Sovereign default in developed economy** (Greece 2012, breaking Eurozone sovereign safety belief)
- **Regulatory "no bailout" stance** (breaking implicit guarantee expectations)

**Transmission Speed: Very Fast (hours-days)**
- T+0: Default news breaks, relevant entity bonds fall 50-80% (e.g., Lehman CDS spreads jumped from 150bp to >600bp intraday)
- T+1 to T+2: Indiscriminate selling extends to all entities in same region/sector/rating category
- T+3 to T+7: Liquidity crisis propagates to primary market, new issue cancellations surge

**Historical Amplitude: Very High**
- Lehman collapse (Sep 2008): Global financial system froze; interbank lending stopped; AIG required $182bn bailout; money market funds "broke the buck"
- Credit Suisse AT1 wipeout (Mar 2023): $17bn of AT1 bonds written to zero, breaking the AT1 "high coupon for slightly more risk" narrative; all European bank AT1s repriced 100-200bp
- Greece sovereign restructuring (2012): Largest ever sovereign debt restructuring ($200bn+); broke Eurozone "no sovereign default" assumption; contagion spread to Italy/Spain/Portugal

**Decay Distance: No clear boundary**
- Unlike credit chain or regional resonance, confidence collapse has no decay mechanism based on economic relationships or geography
- Theoretically can affect any entity that the market "labels" as belonging to the same category

**Predictability: Extremely Low**
- Confidence collapse is a **narrative-driven behavioral finance event** that cannot be predicted with traditional credit analysis frameworks
- Evolution can be tracked through market sentiment indicators (credit spreads, CDS prices, VIX) and media narrative analysis, but trigger timing and boundary cannot be pre-determined

### 2.6 Four Contagion Types Comparison Matrix

| Dimension | Credit Chain (C) | Regional Resonance (R) | Liquidity Squeeze (L) | Confidence Collapse (S) |
|---|---|---|---|---|
| **Driving Mechanism** | Real economy cash flow linkages | Government credit binding | Leverage -> forced liquidation chain | Market narrative and herd psychology |
| **Decay Mechanism** | Length of commercial relationship chain | Geographic distance + administrative tier | Asset class substitution elasticity | No defined decay mechanism |
| **Trigger Predictability** | Medium-High (supply chain mappable) | Medium (fragile regions identifiable) | Low (requires market sentiment) | Extremely Low (black swan) |
| **Transmission Traceability** | High (traceable via payment data) | Medium (traceable via spread changes) | Low (too fast to trace) | Medium (traceable via media narrative) |
| **Risk Mitigation** | Check top 5 customer/supplier concentration | Check regional exposure and mutual guarantee network | Check fund overlap in same asset class | Check overall market sentiment and leverage |
| **Trigger Frequency** | High (multiple inter-enterprise events per year) | Medium (1-2 regional-level events per year) | Medium (several liquidity shocks per year) | Low (0-1 systemic shock per year) |

---

## 3. Seven Standard Transmission Pathways

### Pathway 1: Supply Chain

**Transmission Mechanism:**
Core enterprise default -> accounts payable unpaid -> upstream supplier receivables become bad debts -> supplier liquidity tightens -> supplier reduces output/workforce -> second-tier supplier business volume declines

```
Core Enterprise (Source)
    | Accounts payable default
    v
Tier-1 Supplier (direct receivable loss)
    | Receivables deteriorate -> own liquidity tightens
    v
Tier-2 Supplier (indirect -- order reduction)
    |
    v
Tier-3 Supplier (limited impact)
```

**Primary Contagion Type:** Credit Chain (C)

**Historical Cases:**

| Year | Event | Transmission Path | Loss Magnitude |
|---|---|---|---|
| 2008 | Lehman collapse | Lehman -> hedge funds (prime brokerage assets frozen) -> fund-of-funds chain | Global hedge fund redemptions >$100bn; several funds liquidated |
| 2014-2015 | Petrobras corruption crisis | Petrobras -> upstream oilfield service providers (Sete Brasil, OSX, etc.) | Brazilian oil & gas supplier sector collapse; OSX bankruptcy; Sete Brasil bankruptcy |
| 2020 | Wirecard fraud | Wirecard -> acquiring banks (NatWest, BNP Paribas) -> merchant chain | Partner banks faced joint liability; German fintech ecosystem funding freeze |
| 2021 | Evergrande liquidity | Evergrande -> construction materials suppliers -> residential project subcontractors | Tier-1 suppliers booked large bad debts; regional construction SMEs bankrupt |
| 2022-2023 | European energy crisis | Energy utility default -> upstream gas/electricity supplier chain hedging collapse | Fortum, Uniper, and others needed state bailouts; energy derivative CCP margin calls |

**Identification Methods (Public Data for Pre-Mapping):**
- **Concentration Disclosures**: Listed company top-5 customer/supplier ratio; >30% concentration is a warning threshold
- **Receivable Aging Analysis**: Concentrated aging >12 months suggests counterparty may already be in distress but impairment not yet recognized
- **Prepayment Anomalies**: Large prepayments to secure supply from a single customer indicate over-dependence
- **Trade Flow Data**: Cross-border trade statistics, customs data for mapping global supply chains
- **Contract Award Data**: Long-term supply agreements tracked through public procurement and contract disclosures
- **Sector Reports**: Industry association publications on supply chain concentration
- **Commercial Paper Discount Rates**: Rising discount rates on trade acceptances signal core enterprise credit deterioration

**Paradigm-Level Risk Ranking (1=Highest, 6=Lowest):**

| Paradigm | Risk Level | Rationale |
|---|---|---|
| P2 (Technology Moat) | 1 | Highly specialized supply chains; strong customer stickiness; hard to replace; losses almost un-recoverable |
| P5 (Brand + Channel) | 2 | OEM/ODM dependent on brand orders; brand default directly idles factory capacity |
| P4 (Asset Lease) | 3 | Data centers depend on large tenant leases; tenant default hits NOI and DSCR directly |
| P3 (Zero-Sum Game) | 4 | Cyclical sectors with dispersed supply chains; single customer default has limited impact |
| P6 (Network + Traffic) | 5 | Platform enterprises have low individual supplier dependence; limited contagion |
| P1 (Policy-Driven) | 6 | Procurement often diversified (e.g., solar modules sold to multiple utilities); single counterparty risk limited |

---

### Pathway 2: Financial Linkage

**Transmission Mechanism:**
A defaults -> banks call on guarantor B for compensation -> B forced to cover -> B's own liquidity tightens -> B defaults, pursuing C -> chain effect

```
A (Borrower -> Defaults)
    | A defaults -> bank pursues guarantor B
    v
B (Guarantor -> forced compensation -> liquidity tightens)
    | B also defaults (or defaults after pursuit) -> pursues C
    v
C (Guarantor -> forced compensation -> default probability surges)
    |
    v
D ... (chain compensation continues, forming inter-entity liability network)
```

**Variation -- Mutual Guarantee Circuit:**
```
A --guarantee-- B --guarantee-- C --guarantee-- D --guarantee-- A (circular)
Any node default -> compensation pressure propagates along the chain -> ultimately all default
```

**Primary Contagion Type:** Credit Chain (C) + Regional Resonance (R) (e.g., regional guarantee networks)

**Historical Cases:**

| Year | Event | Guarantee Network Structure | Consequence |
|---|---|---|---|
| 2008 | AIG bailout | AIG wrote CDS on RMBS/CMBS for multiple counterparties | $182bn federal rescue; cascade of counterparty losses in global banking system |
| 2011-2012 | European sovereign-bank "doom loop" | Eurozone banks held large sovereign debt; sovereign default risk -> bank capitalization risk | Ireland, Spain, Cyprus banking crises; EU banking union creation |
| 2016 | Italian banking crisis | Italian regional banks (Monte dei Paschi, Popolari) cross-held sovereign bonds + local loans | 17bn EUR state bailout of Monte dei Paschi; Veneto banks resolution cost 5bn EUR |
| 2020 | COVID cross-border guarantee chains | Airlines cross-guarantee and alliance liability sharing | Lufthansa, Air France-KLM required state recapitalization; airline mutual guarantee networks strained |
| 2023 | SVB / Signature Bank deposit contagion | Regional banks share uninsured deposit base + HTM bond portfolios | Second-largest US bank failure; Fed launch of BTFP (Bank Term Funding Program) |

**Identification Methods (Public Data for Pre-Mapping):**
- **Guarantee Disclosures**: Listed companies must disclose off-balance sheet guarantees (amount and counterparty)
- **High Guarantee Ratio**: Guarantee / Net Assets >50% is "watch", >100% is "danger"
- **Large Non-Related Party Guarantees**: Significant guarantees to uncontrolled entities = external credit exposure
- **Circular Guarantee Networks (A -> B -> C -> A)**: Identified through cross-shareholding and guarantee disclosures
- **Sector Guarantee Mapping**: Network analysis of guarantee relationships within the same industry/region
- **Derivative Counterparty Exposure**: Notional CDS exposure, cross-border swap lines, derivative central clearing membership

**Paradigm-Level Risk Ranking:**

| Paradigm | Risk Level | Rationale |
|---|---|---|
| P1 (Policy-Driven) | 1 | Banks/sovereigns with high cross-exposure; circular guarantee risk among regulated entities |
| P3 (Zero-Sum Game) | 2 | Overcapacity sectors (auto, metals) use mutual guarantees to obtain rolling financing |
| P6 (Network + Traffic) | 3 | Commercial services with cross-corporate guarantee structures |
| P2 (Technology Moat) | 4 | Some pre-revenue biotech firms use guarantee facilities; less common |
| P5 (Brand + Channel) | 5 | Light-asset consumer companies have low guarantee needs |
| P4 (Asset Lease) | 6 | Asset-backed financing (project finance, ABS) is collateral-based; mutual guarantee is minimal |

---

### Pathway 3: Regional / Sector Concentration

**Transmission Mechanism:**
First default in a region -> market re-assesses regional government support willingness and capacity -> all other entities in that region sold off indiscriminately -> regional funding environment deteriorates (primary market freeze, refinancing difficulties) -> weak entities in region follow into default

```
First regional/SOE default (Source)
    | Market questions: will the government backstop?
    v
All other region-based bonds sold off (spreads widen 200-600bp)
    | Funding environment deteriorates (banks tighten credit, primary cancellation)
    v
Weak entities in region face liquidity strain (refinancing difficulty)
    |
    v
High-risk entities follow into default
    | Contagion extends to similar economies
    v
Pan-region same-type entities re-priced
```

**Primary Contagion Type:** Regional Resonance (R) + Confidence Collapse (S)

**Historical Cases:**

| Year | Event | Transmission Path | Consequence |
|---|---|---|---|
| 2010-2012 | Greece crisis -> GIIPS | Greece -> Ireland, Portugal, Italy, Spain sovereign spreads | Contagion spread 200-800bp across Eurozone periphery; Ireland/Portugal required bailouts |
| 2011 | Spanish caja crisis | CCM (Caja Castilla-La Mancha) -> all regional savings banks | Spanish autonomous community bond re-pricing; regional bank sector restructuring (from 45 to 15 entities) |
| 2016 | Italian banking crisis | Monte dei Paschi di Siena -> Italian regional banks | 17bn EUR state bailout; Veneto Banca and Popolare di Vicenza resolution; sector-wide NPE disposal |
| 2023 | US regional banking crisis | SVB (California) -> Signature (NY) -> First Republic (SF) -> all regional banks | KBW Regional Banking Index fell 30%+; deposit flight from smaller banks to money center banks |
| 2023 | Credit Suisse bail-in | Swiss systemic bank failure -> European bank sector | AT1 bond structure re-priced globally; Swiss regulator credibility questioned |

**Identification Methods (Public Data for Pre-Mapping):**
- **Sovereign Fiscal Data**: GDP growth, fiscal revenue trend, debt/GDP ratio, primary surplus -- assess government backstop capacity
- **Regional Debt Outstanding**: Total outstanding bonds of regionally-linked entities -- estimate funding gap post-default
- **Historical Bailout Record**: Government treatment of past defaults (full guarantee, market resolution, haircut)
- **Policy Stance**: Official statements regarding support for systemically important entities
- **Inter-Region Guarantee Networks**: Cross-regional guarantee relationship mapping
- **CDS Spread Monitoring**: After first default, closely monitor CDS changes for peer entities

**Paradigm-Level Risk Ranking:**

| Paradigm | Risk Level | Rationale |
|---|---|---|
| P1 (Policy-Driven) | 1 | Sovereigns, utilities, regulated financials are the core of regional concentration risk |
| P2 (Technology Moat) | 2 | Biotech/tech clusters (Bay Area, Boston, Cambridge) can create regional concentration despite technology differentiation |
| P4 (Asset Lease) | 3 | Telcos and utilities have region-specific infrastructure but moderate regional credit binding |
| P6 (Network + Traffic) | 4 | Transportation and retail have regional clusters but limited government credit linkage |
| P3 (Zero-Sum Game) | 5 | Automobile manufacturing is globalized; regional concentration less pronounced |
| P5 (Brand + Channel) | 6 | Consumer brand companies are dispersed; regional resonance not significant |

---

### Pathway 4: Common Creditor

**Transmission Mechanism:**
A high-credit entity (or a group of entities sharing a common creditor) defaults -> the creditor (bank, insurance company, asset manager) faces unexpected losses -> the creditor de-leverages by reducing exposure to other borrowers in the same sector/category -> those borrowers face credit tightening -> follow-on defaults

```
Entity A defaults (borrower from Bank X)
    | Bank X takes unexpected loss on A
    v
Bank X reduces risk appetite -> reduces lending to all similarly-rated borrowers
    (especially those with high correlation to A)
    | Credit supply contraction
    v
Entity B, C, D (similar profile to A) face refinancing difficulty
    |
    v
Weak entities among B, C, D default -> further losses at Bank X
```

**Primary Contagion Type:** Liquidity Squeeze (L) + Credit Chain (C)

**Historical Cases:**

| Year | Event | Creditor Channel | Contagion Scope |
|---|---|---|---|
| 2008 | Lehman default -> money market fund freeze | Reserve Primary Fund "broke the buck" -> all money funds faced redemptions | Commercial paper market (CP) completely froze; non-financial CP outstanding fell 50% in weeks |
| 2011-2012 | European bank sovereign exposure | Banks holding GIIPS sovereign bonds -> losses -> reduced lending to all borrowers | SME lending in Southern Europe contracted 20-30%; creditless recovery |
| 2020 COVID | Energy sector bank concentration | Banks with large energy sector loan books -> Energy defaults -> reduced lending across all sectors | Oil & gas loan portfolio losses; bank energy sector exposure reduction |
| 2023 | US regional bank deposit concentration | Concentrated uninsured deposits at SVB/Signature/First Republic -> run on all banks with similar deposit profiles | Regional bank stock decline 30-50%; deposit outflows from all smaller banks |

**Identification Methods:**
- **Bank Loan Exposure Concentration**: Which banks have largest exposure to which industries/regions
- **Syndicated Loan Participation**: Lender group composition for large borrowers
- **Common Asset Manager Holdings**: Fund overlap analysis across portfolios
- **Insurance Company Bond Portfolios**: Common holdings in insurance general account portfolios
- **Derivative Counterparty Networks**: CDS netting and counterparty concentration analysis

---

### Pathway 5: Index Inclusion

**Transmission Mechanism:**
A default (or significant credit deterioration) of an Index constituent -> the index experiences tracking error / rebalancing pressure -> asset managers tracking the index are forced to adjust their portfolios -> selling pressure propagates to other Index constituents, especially those with similar characteristics

```
Constituent A in Index X defaults
    | Index weight is redistributed; passive funds must rebalance
    v
All remaining Index constituents experience rebalancing flows
    (positive for some, negative on relative weight)
    | Active managers preemptively short similar constituents
    v
Weak constituents of same Index face disproportionate selling
    |
    v
Index-level credit spread widens; new entrants to Index face tighter conditions
```

**Primary Contagion Type:** Liquidity Squeeze (L) + Confidence Collapse (S)

**Historical Cases:**

| Year | Event | Index Channel | Contagion Scope |
|---|---|---|---|
| 2008 | Lehman removed from S&P 500 | S&P 500 index rebalancing; passive funds sold all Lehman positions | Active speculators shorted similar investment banks; Bear Stearns and Merrill Lynch were acquired under pressure |
| 2018 | FTSE Russell / MSCI EM bond index changes | Argentina, Turkey bonds downgraded -> removed from EM bond indices | $10bn+ in passive outflow from affected countries; spreads widened across EM index peer group |
| 2020 | Oil price crash -> IG to HY "fallen angels" | ExxonMobil, Occidental, Ford downgraded from IG to HY -> forced selling by IG-only mandates | Fallen angel wave: $200bn+ bonds downgraded; HY market spread surged 600bp |
| 2022 | Russia sanctions -> index exclusion | MSCI, FTSE Russell removed Russia from all indices | $5bn passive outflows; Russia bond/equity market effectively locked; EM fund liquidity crisis |
| 2023 | Credit Suisse AT1 wipeout -> index reconstitution | AT1 bond indices excluded CS AT1 -> passive AT1 fund forced selling | All AT1 bond indices rebalanced; remaining AT1 bonds absorbed disproportionate selling |

**Identification Methods:**
- **Index Membership Analysis**: Which indices each entity belongs to; index weight percentage
- **Passive Asset Tracking Estimates**: Total AUM tracking each index; implied forced flow amount
- **Index Rebalancing Calendar**: Scheduled rebalancing dates; unscheduled rebalancing triggers
- **Fallen Angel Risk**: IG bonds at risk of downgrade to HY; estimated forced selling volume
- **Index Inclusion Criteria**: Size, liquidity, rating requirements for membership

---

### Pathway 6: Rating Cliff Effects

**Transmission Mechanism:**
A rating downgrade (especially multi-notch) of a major entity -> market re-assesses the rating agency's criteria for that sector -> other entities in the same sector are re-rated by the market -> rating triggers (investment-grade mandates, collateral thresholds, regulatory constraints) force selling

```
AAA/AA entity downgraded (multi-notch downgrade)
    | Market reassesses: are other similarly-rated entities at risk?
    v
Market anticipates further downgrades in the same sector
    | Trading desks preemptively reduce exposure to comparable entities
    v
Rating agency reviews others under same sector/criteria
    | Additional downgrades follow (the "rating cascade")
    v
Investment mandates triggered -> forced selling by IG-only / buy-rated-only fund mandates
```

**Primary Contagion Type:** Confidence Collapse (S) + Liquidity Squeeze (L)

**Historical Cases:**

| Year | Event | Rating Cliff Cascade | Impact |
|---|---|---|---|
| 2001-2002 | Enron/WorldCom accounting scandals | Both were IG -> default/CCC within weeks | S&P, Moody's methodology changed; corporate governance rating created; market trust in ratings permanently damaged |
| 2008 | Monoline insurer downgrades | MBIA, Ambac downgraded from AAA -> below IG | All municipal bonds wrapped by monolines immediately re-priced; muni market disruption |
| 2010 | Greek sovereign downgrade cascade | Greek debt downgraded A- (Jan 2010) -> CCC (Dec 2010) -> SD (2012) | Multiple-notch downgrades triggered CDS settlements; ECB collateral haircuts; Greek bonds became ineligible for ECB operations |
| 2020 | Fallen angel wave (Oil & Gas) | ExxonMobil, Chevron, Occidental, Ford -> multi-notch downgrades | $200bn+ bonds forced out of IG indices; HY market absorbed 40% more supply than normal |
| 2023 | Credit Suisse AT1 write-down to zero | CS AT1 rated IG -> zero recovery in days | Moody's downgraded CS subordinated debt 4 notches; AT1 rating methodology under review across all European banks |

**Identification Methods:**
- **Rating Headroom Analysis**: Distance to downgrade threshold for each notch (e.g., S&P: how many notches from BBB-)
- **Watch/Negative Outlook Count**: Ratio of negative outlooks to total rated universe in a sector
- **Methodology Change Risk**: When rating agencies revise criteria for a sector, watch for cascade
- **Cross-Agency Correlation**: When Moody's/S&P/Fitch all converge in their review, follow-on downgrades cluster
- **Investment Mandate Triggers**: Regulatory and contractual rating thresholds (IG vs HY, eligible collateral status)

---

### Pathway 7: Sovereign-Bank Nexus

**Transmission Mechanism:**
Sovereign credit deterioration -> banks holding sovereign bonds incur mark-to-market losses -> bank capitalization weakens -> banks reduce lending to the real economy -> economic contraction -> further sovereign fiscal deterioration (the "doom loop")

Conversely: Bank default -> government bailout costs -> sovereign debt/GDP rises -> sovereign credit downgrade -> further bank losses

```
Sovereign downgrade / credit event
    | Banks holding sovereign bonds -> MtM losses
    v
Bank capitalization deteriorates -> lending capacity constrained
    | Credit supply contraction to real economy
    v
Economic growth slows -> fiscal revenue declines
    | Social / bailout spending increases
    v
Fiscal deficit widens -> sovereign debt/GDP rises
    | Further sovereign downgrade risk -> loop continues
```

**Primary Contagion Type:** Regional Resonance (R) + Liquidity Squeeze (L) + Confidence Collapse (S)

**Historical Cases:**

| Year | Event | Sovereign-Bank Loop | Impact |
|---|---|---|---|
| 2011-2012 | Eurozone sovereign-bank "doom loop" | Greek/PIIGS sovereign downgrades -> bank losses -> lending freeze -> deeper recessions | Required EU banking union, ESM bailout funds, ECB OMT program to break loop |
| 2013 | Cyprus banking crisis | Greek sovereign debt losses -> Cyprus banks (Greek exposure) -> bank failure -> sovereign bailout | First euro-area capital controls; bank restructuring triggering bail-in of uninsured depositors |
| 2017-2018 | Italian sovereign-bank nexus | Italian banks held 350bn+ EUR in BTPs -> sovereign risk -> bank risk -> sovereign risk | Monte dei Paschi bailout; EU approval of precautionary recapitalization |
| 2023 | Swiss Credit Suisse failure -> sovereign guarantee | CS failure required Swiss government guarantee ($109bn backstop) | Swiss sovereign contingent liability exposure; sovereign CDS spread widened ~20bp |
| 2023-2024 | US regional banking crisis -> fiscal cost | SVB, Signature, First Republic -> FDIC deposit insurance fund (DIF) depleted | FDIC special assessment on all banks; DIF restoration cost $16bn+; sovereign contingent liability |

**Identification Methods:**
- **Sovereign Debt Holdings**: Banks' holdings of domestic sovereign bonds as % of Tier 1 capital
- **Sovereign-Bank Correlation**: Rolling correlation between bank CDS and sovereign CDS spreads
- **Government Guarantee Exposure**: Size and scope of explicit/implicit government guarantees to banking sector
- **Bailout Fiscal Capacity**: Sovereign fiscal space (Debt/GDP, primary surplus) to absorb banking sector losses
- **Cross-Border Exposure**: Domestic banks' exposure to foreign sovereign debt (e.g., German banks to Greek bonds)

---

## 4. Paradigm Contagion Exposure Mapping (P1-P6)

### 4.1 Paradigm Overview

For the international industry classification used in the Contagion Matrix (19 GICS-based industries), the following six analytical paradigms define shared risk-driver characteristics.

| Paradigm | Description | Core Industries (Primary) |
|---|---|---|
| **P1: Policy-Driven** | Sectors where government policy, regulation, geopolitics, or fiscal/tax regimes determine the demand cycle and profitability | Energy (Oil & Gas), Chemicals, Metals & Mining, Construction Materials, Utilities (Regulated), Financials (Banks/Insurance), Sovereigns & GSEs |
| **P2: Technology Moat** | R&D-intensive sectors where intellectual property, patents, and proprietary technology create durable competitive advantage | Technology Hardware (Semis), Software & Services, Biotech & Pharma, Healthcare Equipment, Capital Goods (advanced manufacturing) |
| **P3: Zero-Sum Game** | Cyclical, commoditized sectors where price competition erodes margins; one player's gain is another's loss | Automobiles, Consumer Durables, Metals & Mining (secondary), Construction Materials (secondary) |
| **P4: Asset Lease** | Infrastructure-heavy sectors where cash flows are driven by physical asset utilization; NOI and DSCR are the key metrics | Utilities (Regulated), Telecommunications, Transportation |
| **P5: Brand + Channel** | Consumer sectors where brand equity, distribution networks, and consumer trust are the primary value drivers | Consumer Staples, Consumer Durables, Retail (branded) |
| **P6: Network + Traffic** | Platform and network-effect sectors where scale, user base, and data generate increasing returns | Commercial Services, Retail (e-commerce), Transportation (logistics platforms), Telecommunications (data) |

### 4.2 Paradigm Contagion Characteristics

| Characteristic | P1: Policy-Driven | P2: Technology Moat | P3: Zero-Sum Game | P4: Asset Lease | P5: Brand + Channel | P6: Network + Traffic |
|---|---|---|---|---|---|---|
| **Primary Contagion Type** | R + S | C + L | C + S | C + L | S + C | C + L |
| **Contagion Speed** | Fast (days-weeks) | Moderate (1-3 months) | Moderate (1-3 months) | Fast (weeks) | Moderate-Variable | Fast (days-weeks) |
| **Decay Distance** | Region-bound | Supply chain depth | Market-wide | Asset class-bound | Brand-loyalty bound | Network depth |
| **Historical Amplitude** | Very High | High | High | Moderate | High | High |
| **Predictability** | Medium | Medium-High | Medium | Medium-High | Low-Medium | Medium |
| **Trigger Frequency** | Medium | Low-Medium | High | Medium | Low | Medium |

### 4.3 Paradigm x Pathway Exposure Grid

| Paradigm | Most Exposed 3 Pathways | Secondary Exposed Pathways | Least Exposed |
|---|---|---|---|
| **P1 (Policy-Driven)** | 3-Regional/Sector, 7-Sovereign-Bank, 6-Rating Cliff | 4-Common Creditor, 2-Financial Linkage | 1-Supply Chain |
| **P2 (Technology Moat)** | 1-Supply Chain, 5-Index Inclusion, 4-Common Creditor | 6-Rating Cliff, 3-Regional/Sector | 7-Sovereign-Bank |
| **P3 (Zero-Sum Game)** | 2-Financial Linkage, 1-Supply Chain, 5-Index Inclusion | 6-Rating Cliff, 4-Common Creditor | 3-Regional/Sector, 7-Sovereign-Bank |
| **P4 (Asset Lease)** | 4-Common Creditor, 5-Index Inclusion, 1-Supply Chain | 3-Regional/Sector, 2-Financial Linkage | 7-Sovereign-Bank |
| **P5 (Brand + Channel)** | 1-Supply Chain, 5-Index Inclusion, 6-Rating Cliff | 3-Regional/Sector | 7-Sovereign-Bank, 2-Financial Linkage |
| **P6 (Network + Traffic)** | 1-Supply Chain, 4-Common Creditor, 2-Financial Linkage | 5-Index Inclusion, 3-Regional/Sector | 7-Sovereign-Bank |

---

## 5. Contagion Intensity Escalation Factors

### 5.1 Escalation Factor Overview

Contagion intensity is not static -- the same credit event can produce materially different contagion outcomes depending on market conditions.

| Escalation Factor | Base State (Level 1-2) | Elevated State (Level 3-4) | Extreme State (Level 5) | Trigger Condition | Observable Indicators |
|---|---|---|---|---|---|
| **Market Panic** | VIX < 20, credit spreads normal | VIX 20-35, spreads widen 30-50bp | VIX > 35, spreads double | Market shifts from "risk-off" to "panic" | VIX index, credit spreads, CDS prices, implied correlation |
| **Regulatory Vacuum** | Regulator explicitly states support | Regulator silent / "no comment" | Regulator declares "market solution" / no bailout | Government withholds policy response to a credit event | Policy meeting minutes, official statements, financial stability reports |
| **High Leverage** | Market margin debt < 80% of baseline / repo outstanding moderate | Leverage 80-110% of historical baseline | Leverage > 110% + forced liquidations triggered | Large number of institutions using same asset class as collateral | Margin debt, repo outstanding, prime brokerage leverage, fund net leverage |
| **Information Asymmetry** | Issuer maintains communication | Issuer silent / vague statements | Issuer completely unreachable / management missing | Post-default issuer chooses silence | Filings frequency, earnings call participation, management accessibility |
| **Year-End Effect** | Non-quarter-end period | 1-2 weeks before quarter-end | Last 2 weeks of calendar year | Regulatory/reporting deadline approaches | Calendar date + interbank liquidity metrics |

### 5.2 Detailed Factor Mechanisms

#### 5.2.1 Market Panic

**Mechanism:** Panic amplifies contagion through the following chain:

```
Market panic rises
    -> Investor behavior converges (everyone reduces high-risk positions simultaneously)
    -> Liquidity demand spikes
    -> Asset prices crash (not due to fundamentals, but selling pressure)
    -> More investors hit risk limits (stop-loss, margin call)
    -> Forced additional selling -> further price decline
    -> Panic becomes self-fulfilling
```

**Historical Cases:**

| Year | Panic Background | VIX Level | Contagion Escalation |
|---|---|---|---|
| 2008 (GFC) | Global financial system near collapse | VIX > 80 | Credit spreads across all sectors jumped 200-600bp; interbank lending halted; TARP/TALF/SMCCP emergency programs required |
| Mar 2020 (COVID) | Global pandemic-driven panic | VIX > 80 (peak 82.69) | IG spreads from 100bp to 400bp; HY from 400bp to 1,100bp; Fed entered corporate bond market for first time ever |
| Sep 2022 (UK gilt crisis) | Fiscal event (mini-budget) | VIX ~ 35, UK gilt vol > 2 stdev | LDI fund margin calls -> forced gilt selling -> gilt yields surged 100bp in 3 days -> BoE emergency purchase program |
| Mar 2023 (US regional banking) | SVB failure -> sector-wide deposit flight | VIX ~ 25-30 | Regional bank stock index fell 30%+; all regional bank HTM bond portfolios re-priced; BTFP facility created |

**Monitoring Indicators:**
- VIX / VSTOXX (European) / VNKY (Japan) volatility indices
- CDX.IG / CDX.HY (North America) and iTraxx Main / iTraxx Crossover (Europe) indices
- Primary market issuance cancellation rate (>20% = panic)
- Money market fund flow data
- Central bank USD swap line utilization

#### 5.2.2 Regulatory Vacuum

**Mechanism:** Regulatory stance anchors market expectations. When a credit event occurs, whether and how the regulator responds directly determines market expectations of "how many more defaults will follow":

| Regulatory Stance | Market Reaction | Contagion Level |
|---|---|---|
| Explicit support ("ensure financial stability," "coordinate resolution") | Market expects contained outcome | Base (Level 1-2) |
| Silence / "no comment" | Market fills void with worst-case scenario | Elevated (Level 3-4) |
| "Market solution" / explicit no-bailout | Implicit guarantee faith broken; panic response | Extreme (Level 5) |

**Historical Cases:**

| Year | Event | Regulatory Stance | Escalation Magnitude |
|---|---|---|---|
| 2008 (Lehman) | Fed allowed Lehman to fail (initially) | Initial stance: no bailout -> then reversed for AIG | System-wide panic; money market funds broke the buck; entire financial system at risk |
| 2010-2012 (Eurozone crisis) | Initial policy confusion | EU divided between bailout vs austerity; ECB delayed intervention | Spreads widened 300-800bp across GIIPS; eventually resolved through OMT/ESM |
| Mar 2020 (COVID) | Central banks acted decisively | Fed announced QE unlimited, then corporate bond purchases; ECB announced PEPP | Market bottomed March 23; credit spreads recovered significantly within weeks |
| Sep 2022 (UK gilt) | BoE initially silent | BoE initially said "monitoring" -> then emergency gilt purchases | Gilt yields surged 100bp in 3 days; pension fund sector near failure |
| Mar 2023 (SVB) | US regulators acted initially | Weekend resolution + full deposit guarantee (systemic risk exception) -> then BTFP | Regional bank stress contained after initial SVB/Signature/First Republic failures |

**Monitoring Indicators:**
- Central bank / treasury / regulator statements on financial stability
- Policy meeting minutes (FOMC, ECB Governing Council, BoE MPC)
- Financial Stability Reports (FSB, IMF Global Financial Stability Report)
- Media narrative analysis (bailout vs market resolution language)

#### 5.2.3 High Leverage

**Mechanism:** High-leverage environment amplifies transmission through:

```
Market-wide leverage high
    -> Most institutions have highly-pledged assets
    -> A bond defaults -> its collateral value declines
    -> Haircut triggers -> institutions must post additional collateral or margin
    -> Institutions forced to sell cash (other assets)
    -> Selling pressure propagates to previously unrelated asset classes
    -> More margin calls -> full market liquidity stress
```

**Historical Cases:**

| Year | Leverage Environment | Contagion Event | Escalation |
|---|---|---|---|
| 2008 (GFC) | Investment banks leverage > 30:1 | Lehman, Bear Stearns, Merrill Lynch | Forced deleveraging caused asset fire sales across all markets; repo market froze |
| 2015 (Swiss franc shock) | High FX carry leverage | SNB removed EUR/CHF floor | FX carry trade forced unwinding; several FX brokers (Alpari, FXCM) bankrupt; global FX vol spike |
| 2020 (COVID oil crash) | High energy sector leverage | Oil price negative (Apr 2020) | Leveraged oil ETFs liquidated; energy MLP sector restructured; some producers bankruptcy |
| 2022 (UK LDI crisis) | High pension fund leverage via derivatives | Gilt yield spike | LDI fund margin calls >300bn GBP; BoE emergency gilt purchase; LDI regulation overhauled |
| 2023 (US regional banks) | High HTM bond portfolio leverage (duration) | SVB HTM losses | Unrealized HTM losses >600bn across all US banks; deposit flight from similar banks |

**Monitoring Indicators:**
- Total margin debt as % of GDP or market cap
- Repo outstanding (US tri-party repo, EU repo market)
- Hedge fund net/gross leverage (Prime Broker surveys)
- Bank leverage ratio (Tier 1 / Total Assets)
- Derivative notional to GDP ratio

#### 5.2.4 Information Asymmetry

**Mechanism:** Information asymmetry determines how much of the "worst possible assumption" the market uses to replace missing facts:

```
Default event occurs
    -> Issuer goes silent (no filings, no calls, management missing)
    -> Market cannot access actual risk exposure information
    -> Investors replace missing information with "worst-case" assumption
    -> Related entities' credit assessments sharply downgraded
    -> Even if impacts prove limited, damage is already done
```

**Historical Cases:**

| Year | Event | Asymmetry Level | Escalation |
|---|---|---|---|
| 2001-2002 | Enron, WorldCom, Tyco | Extreme | Companies had falsified financials for years; counterparty exposure completely unquantifiable -> cascade of accounting-related credit tightening |
| 2008 | Lehman counterparty exposure | Very High | Lehman's derivative book was a black box -> AIG, money market funds, CDS counterparties all assumed worst -> systemic freeze |
| 2020 | Wirecard fraud | Extreme | Absence of auditable financials for years -> partner banks could not quantify liability -> entire German fintech ecosystem penalty |
| 2023 | First Republic before failure | High | Market could not assess true deposit outflow + HTM loss -> trading at 90% discount to book before FDIC resolution |

**Monitoring Indicators:**
- Filing timeliness (whether expected filings are made)
- Audit opinion quality (going concern / material weakness)
- Management accessibility (earnings call attendance, analyst day frequency)
- Media investigation volume (critical reporting intensity)
- Short interest (as a proxy for hidden risk market perception)

#### 5.2.5 Year-End Effect

**Mechanism:** At year-end or quarter-end, financial institutions face regulatory/compliance deadlines, reducing risk appetite systematically:

```
Year-end / quarter-end approaching
    -> Financial institutions' risk appetite systematically declines
    -> Credit event sensitivity rises ("avoid mistakes > make money")
    -> Any credit event is over-reacted
    -> Institutions reduce non-core positions
    -> Contagion spreads from specific entities to broader market
```

**Historical Cases:**

| Year | Period | Event | Amplification |
|---|---|---|---|
| 2008 | Sep-Nov | GFC full crisis | Year-end panic intensified: Lehman (Sep), Reserve Fund (Sep), AIG (Sep), TARP vote (Oct) |
| 2010 | Dec | Irish bailout | Year-end sovereign funding stress across Eurozone periphery |
| 2018 | Dec | US equity + credit selloff | Bond market illiquidity contributed to 4th Q selloff; IG spreads widened 30bp |
| 2020 | Dec | COVID year-end liquidity stress | Credit markets still fragile; year-end repo rate volatility |
| 2022 | Dec | LDI/Gilt crisis aftermath | Year-end pension rebalancing + LDI restructuring constraints |

**Monitoring Indicators:**
- Calendar date (effect increases from Oct, peaks Dec)
- Interbank rates (LIBOR/OIS spread, EURIBOR-OIS) at quarter-ends
- Year-end repo specialness and GC repo rate volatility
- Regulatory deadline impact (LCR, NSFR compliance)

### 5.3 Escalation Factor Synergy

Escalation factors exhibit **positive synergy** -- when multiple factors trigger simultaneously, contagion intensity amplifies multiplicatively rather than additively:

| Factor Combination | Synergy Coefficient | Historical Case |
|---|---|---|
| Market Panic + Information Asymmetry | 1.5x - 2.0x | 2008 (Lehman failure in opaque derivatives market); 2023 (SVB deposit concentration unknown to market) |
| High Leverage + Market Panic | 2.0x - 3.0x | 2008 (investment bank leverage 30:1 + panic); 2022 (UK LDI leverage + gilt panic) |
| Regulatory Vacuum + Year-End | 1.5x | 2010 (Eurozone year-end funding stress with policy confusion); 2022 (UK gilt year-end with delayed BoE response) |
| Three or more simultaneously | 3.0x+ | Global systemic crisis threshold: 2008 (panic + leverage + regulatory vacuum + information asymmetry all active) |

### 5.4 Escalation Factor Weights by Contagion Type

| Factor | Credit Chain (C) | Regional Resonance (R) | Liquidity Squeeze (L) | Confidence Collapse (S) |
|---|---|---|---|---|
| **Market Panic** | Moderate (emotion affects receivable recovery willingness but not actual cash loss) | High (panic accelerates regional indiscriminate selling) | **Extreme** (panic is the core fuel of liquidity squeeze) | **Extreme** (confidence collapse is the extreme form of panic) |
| **Regulatory Vacuum** | Low (governments do not intervene in commercial debt relationships) | **Extreme** (government stance directly determines regional credit trajectory) | Moderate (regulator can inject liquidity but cannot change preferences) | Extreme (regulatory stance is the "on/off switch" for confidence collapse) |
| **High Leverage** | Low (supply chain relationships unrelated to leverage) | Moderate (leveraged funds also participate in regional bond selling) | **Extreme** (leverage is a precondition for liquidity squeeze) | High (deleveraging amplification of confidence crash) |
| **Information Asymmetry** | Medium-High (asymmetry prevents suppliers from assessing receivable recovery probability) | High (asymmetry -> investors use "blanket" de-risking strategy) | Moderate (fund holding transparency limited) | **Extreme** (information vacuum is the breeding ground for confidence collapse) |
| **Year-End Effect** | Low (year-end billing does not change actual cash recovery) | Moderate (year-end reduces regional exposure) | High (year-end liquidity tightness amplifies squeeze) | High (year-end risk appetite decline amplifies panic) |

---

## 6. Practical Application Guide

### 6.1 Analytical Framework Process

Recommended process for incorporating contagion risk assessment into credit analysis:

```
Step 1: Identify Contagion Source (Who might default?)
    +-- High leverage / weak credit / concentrated maturity entities
    +-- Distinguish internal (operational deterioration) vs external (contagion receptor)

Step 2: Map Contagion Pathways (Which channels will the source transmit through?)
    +-- Supply Chain -> check top 5 customer/supplier concentration
    +-- Financial Linkage -> check guarantee and derivative exposure
    +-- Regional/Sector Concentration -> check regional bond map
    +-- Common Creditor -> check shared bank/asset manager concentration
    +-- Index Inclusion -> check index membership and passive fund ownership
    +-- Rating Cliff Effects -> check rating headroom and sector outlook
    +-- Sovereign-Bank Nexus -> check government bond exposure

Step 3: Assess Escalation Factors (Will current market conditions amplify contagion?)
    +-- Market Panic -> VIX, credit spreads
    +-- Regulatory Vacuum -> policy stance
    +-- High Leverage -> repo outstanding, margin debt
    +-- Information Asymmetry -> issuer disclosure quality
    +-- Year-End Effect -> calendar date + liquidity

Step 4: Output Contagion Exposure Score
    +-- Each pathway exposure score (1-5)
    +-- Overall contagion risk level (Low / Medium / High / Extreme)
    +-- Key monitoring indicators (which data to track continuously)
```

### 6.2 Contagion Exposure Scorecard Template

| Assessment Dimension | Score 1 (Very Low) | Score 2 (Low) | Score 3 (Medium) | Score 4 (High) | Score 5 (Very High) |
|---|---|---|---|---|---|
| **Pathway Coverage** | No direct/indirect connection to source | Indirect connection, distant (>= 3 layers) | Indirect connection (2 layers) | Direct connection (1 layer) | Direct + high exposure + no substitute |
| **Pathway Concentration** | Diversified (no single pathway >10%) | Moderately diversified (<20%) | Moderate concentration (20-30%) | Concentrated (30-50%) | Extremely concentrated (>50% exposed to one source) |
| **Asset Liquidity** | Immediately realizable (treasuries/rates) | Short-term realizable (AAA credit) | Moderate realizable (AA+ credit) | Realizable with significant haircut | Nearly non-realizable (private debt, loans, equity) |
| **Information Transparency** | Regular detailed disclosure + proactive communication | Regular disclosure + normal communication | Average disclosure timeliness and detail | Delayed disclosure / evasive | No disclosure / management unreachable |
| **External Support** | Central/sovereign government explicit support | Government has support capacity and track record | Support probability uncertain | Weak support capacity / unclear willingness | Explicit no-bailout / no support |

### 6.3 Integration with Existing Engine Documents

| Engine Document | Integration Method | Specific Operation |
|---|---|---|
| [Contagion Matrix](contagion-matrix.md) | 19x19 International Industry Contagion Matrix | Map theoretical pathways to inter-industry contagion intensities |
| **Industry Framework** | Add D11 "Contagion Exposure" dimension to ten-dimension scoring | Each industry type annotated with contagion exposure rating |
| **Paradigm Documents** | Reference this document in each paradigm's "Special Risks" section | Add "Contagion Risk Exposure under This Paradigm" subsection |
| **Qualitative Analysis** | Include "Information Asymmetry Level" in information source assessment | Make entity disclosure transparency a standard dimension |
| **Quantitative Analysis** | Incorporate contagion factors in spread analysis and stress testing | Include escalation factors in stress test parameter sensitivity analysis |
| **Dual-Track Method** | Add contagion risk Track A/Track B divergence assessment | Track A (fundamental view of contagion risk) vs Track B (market pricing implied contagion risk) |
| **Mosaic Engine** | Add contagion signal extraction function | Extract contagion pathway signals, escalation factor signals from public data |

### 6.4 Limitation Statement

Contagion theory has the following inherent limitations:

1. **Confidence collapse cannot be predicted in advance** -- it is fundamentally a behavioral finance event whose trigger point and transmission path depend on market narrative and herd psychology, beyond fundamental or model prediction
2. **Escalation factor quantification is preliminary** -- the "multiplicative synergy" of multiple concurrent escalation factors is difficult to quantify precisely; historical data reference value is limited
3. **Private company data gap** -- contagion analysis relies heavily on public supply chain, guarantee, and related-party information; significant gaps exist for non-public entities
4. **Framework applicability** -- this framework is calibrated on global systemic events (GFC 2008, Eurozone 2011-12, COVID 2020). Application to specific jurisdictions may require parameter adjustment
5. **Not investment advice** -- contagion theory provides a risk analysis framework; it does not constitute buy/sell/hold recommendations

---

## Appendix

### A. Historical Contagion Event Timeline (2000-2025)

| Year | Source | Scope | Primary Type | Primary Pathway |
|---|---|---|---|---|
| 2001 | Enron | Energy sector, audit/accounting | Confidence Collapse | Financial Linkage |
| 2002 | WorldCom | Telecom sector | Confidence Collapse | Rating Cliff |
| 2007 | BNP Paribas (subprime fund freeze) | Structured credit, global banking | Liquidity Squeeze | Common Creditor |
| 2008.03 | Bear Stearns | Investment banking, prime brokerage | Liquidity Squeeze | Common Creditor |
| 2008.09 | **Lehman Brothers** | **Global financial system** | **Confidence Collapse + Liquidity Squeeze** | **Common Creditor + Supply Chain** |
| 2008.09 | AIG | Insurance, global banking | Credit Chain | Financial Linkage |
| 2009-2010 | Greece sovereign | Eurozone sovereign debt | Regional Resonance | Sovereign-Bank Nexus |
| 2010-2012 | **GIIPS sovereigns** | **Eurozone periphery** | **Regional Resonance + Confidence Collapse** | **Sovereign-Bank Nexus** |
| 2011 | Spanish cajas | Spanish regional banking | Regional Resonance | Regional/Sector Concentration |
| 2013 | Cyprus banking crisis | Cypriot banking system | Sovereign-Bank Nexus | Regional/Sector Concentration |
| 2015 | Petrobras | Brazilian oil & gas | Credit Chain | Supply Chain |
| 2016 | Monte dei Paschi | Italian banking | Regional Resonance | Regional/Sector Concentration |
| 2018 | EM index exclusion (Argentina/Turkey) | Emerging market bonds | Liquidity Squeeze | Index Inclusion |
| 2020.03 | **COVID crash** | **Global financial markets** | **Liquidity Squeeze + Confidence Collapse** | **All pathways** |
| 2020.04 | Negative oil price | Energy sector | Liquidity Squeeze | Index Inclusion |
| 2020 | Wirecard | German fintech | Credit Chain | Supply Chain + Financial Linkage |
| 2021 | Evergrande | Global HY property, China | Confidence Collapse | Supply Chain + Regional/Sector |
| 2022 | LDI/Gilt crisis (UK) | UK pension, gilt market | Liquidity Squeeze | Index Inclusion + Common Creditor |
| 2023.03 | **SVB / Signature / First Republic** | **US regional banking** | **Liquidity Squeeze + Confidence Collapse** | **Common Creditor + Sovereign-Bank** |
| 2023.03 | Credit Suisse | Global banking, AT1 market | Confidence Collapse | Sovereign-Bank Nexus + Index Inclusion |
| 2023-2024 | US commercial real estate stress | Regional bank + CRE debt | Liquidity Squeeze | Common Creditor + Sovereign-Bank |

**Bold = systemic shock events affecting scope beyond a single entity and sector**

### B. Contagion Signal Quick Checklist

**Step 1: Are YOU a contagion source?**
- [ ] Do you have high customer concentration (top 5 > 30% of revenue)? -> Your default would infect these customers
- [ ] Do you have significant off-balance-sheet guarantees (guarantee / net assets > 50%)? -> Compensation pressure infects you
- [ ] Are you a major counterparty in derivative contracts? -> Your default infects counterparties
- [ ] Are you in a sector/region with previous default history? -> Your default may trigger regional/sector re-rating

**Step 2: Are YOU a contagion receptor?**
- [ ] Are your receivables aging long / concentrated in few customers? -> Customer default infects you
- [ ] Is your funding channel concentrated (single bond type / bank relationship)? -> Channel freeze infects you
- [ ] Are you categorized into a "labeled" market group (distressed sector, weak region)? -> Label risk infects you
- [ ] Are you part of an interconnected corporate group with prior default history? -> Related-party risk infects you

**Step 3: Escalation Warning**
- [ ] Is VIX / credit spread at elevated levels?
- [ ] What is the regulatory stance on the most recent credit event (supportive / silent / no bailout)?
- [ ] Is market leverage above historical baseline?
- [ ] Is the defaulted entity in an information vacuum?
- [ ] Is the current date near quarter-end / year-end?

**Scoring Reference:** Step 1 + Step 2 combined hit > 3 "Yes" -> High / Very High contagion risk; hit 2 "Yes" -> Medium risk; hit 1 "Yes" -> Low risk. Any "Yes" in Step 3 increases risk level by 1-2 notches.

### C. Version History

| Version | Date | Changes | Author |
|---|---|---|---|
| v0.0.1 | 2026-07-10 | Initial creation: Four contagion types / Seven pathways / Six-paradigm mapping / Escalation factors (China market focused) | Engine Team |
| v0.0.1 | 2026-07-10 | Systemic intelligence layer integration: engine version unified to v0.0.1, forming complete contagion framework with contagion matrix | Engine Team |
| v0.0.1 | 2026-07-10 | Internationalization: replaced China-specific examples with global systemic events (GFC 2008, Eurozone 2011-12, COVID 2020); converted six paradigms to international P1-P6 framework; harmonized seven pathways to global financial transmission channels | Engine Team |
