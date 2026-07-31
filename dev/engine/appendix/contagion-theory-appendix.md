# Contagion Theory -- Credit Risk Transmission Pathways and Sector Exposure Framework — Appendix

> Appendix to `contagion-theory.md` — version tracks the parent document; reference
> material (worked examples, derivations, historical validation) moved here in
> the 2026-07 restructure. Read on demand.

---

## 4. Paradigm Contagion Exposure Mapping (P1-P6)

### 4.1 Paradigm Overview

For the international industry classification used in the Contagion Matrix (19 GICS-based industries), the following six analytical paradigms define shared risk-driver characteristics.

| Paradigm | Description | Core Industries (Primary) |
|---|---|---|
| **P1: Cyclical** | Sectors where commodity prices, freight rates, capacity utilization, or cyclical business/consumer spending determine demand and margins | Energy (Oil & Gas), Chemicals, Metals & Mining, Construction Materials, Capital Goods, Commercial Services, Automobiles, Consumer Durables, Retail |
| **P2: Defensive** | Sectors with inelastic demand where brand moats and pricing power stabilize margins through the cycle | Consumer Staples, Healthcare Equipment |
| **P3: Growth** | R&D-intensive sectors where technology roadmaps, IP, and pipelines drive revenue growth | Technology Hardware (Semis), Software & Services, Biotech & Pharma |
| **P4: Regulated Utility** | License- or concession-based sectors where the regulated asset base and tariff frameworks drive cash flows (NOI/DSCR) | Utilities (Regulated), Telecommunications, Transportation |
| **P5: Financial** | Financial institutions where capital adequacy, asset quality, and funding structure are the core risk drivers | Financials (Banks/Insurance) |
| **P6: Sovereign-Linked** | Sovereigns, sub-sovereigns, GSEs, and DFIs where fiscal capacity and institutional strength determine credit | Sovereigns & GSEs |

> Paradigm codes follow the single source of truth in [industry-framework.md](industry-framework.md) §2-§3; the legacy-to-current mapping is recorded in its Appendix C.

### 4.2 Paradigm Contagion Characteristics

| Characteristic | P1: Cyclical | P2: Defensive | P3: Growth | P4: Regulated Utility | P5: Financial | P6: Sovereign-Linked |
|---|---|---|---|---|---|---|
| **Primary Contagion Type** | C + S | S + C | C + L | C + L | R + L | R + S |
| **Contagion Speed** | Moderate (1-3 months) | Moderate-Variable | Moderate (1-3 months) | Fast (weeks) | Very Fast (days) | Fast (days-weeks) |
| **Decay Distance** | Market-wide | Brand-loyalty bound | Supply chain depth | Asset class-bound | System-wide | Sovereign-bank nexus |
| **Historical Amplitude** | High | High | High | Moderate | Very High | Very High |
| **Predictability** | Medium | Low-Medium | Medium-High | Medium-High | Medium | Medium |
| **Trigger Frequency** | High | Low | Low-Medium | Medium | Medium | Medium |

### 4.3 Paradigm x Pathway Exposure Grid

| Paradigm | Most Exposed 3 Pathways | Secondary Exposed Pathways | Least Exposed |
|---|---|---|---|
| **P1 (Cyclical)** | 2-Financial Linkage, 1-Supply Chain, 5-Index Inclusion | 6-Rating Cliff, 4-Common Creditor | 3-Regional/Sector, 7-Sovereign-Bank |
| **P2 (Defensive)** | 1-Supply Chain, 5-Index Inclusion, 6-Rating Cliff | 3-Regional/Sector | 7-Sovereign-Bank, 2-Financial Linkage |
| **P3 (Growth)** | 1-Supply Chain, 5-Index Inclusion, 4-Common Creditor | 6-Rating Cliff, 3-Regional/Sector | 7-Sovereign-Bank |
| **P4 (Regulated Utility)** | 4-Common Creditor, 5-Index Inclusion, 1-Supply Chain | 3-Regional/Sector, 2-Financial Linkage | 7-Sovereign-Bank |
| **P5 (Financial)** | 2-Financial Linkage, 4-Common Creditor, 7-Sovereign-Bank | 6-Rating Cliff, 5-Index Inclusion | 1-Supply Chain |
| **P6 (Sovereign-Linked)** | 7-Sovereign-Bank, 3-Regional/Sector, 6-Rating Cliff | 4-Common Creditor, 2-Financial Linkage | 1-Supply Chain |

---


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
