# Industry Classification & Analysis Framework

**Version**: v0.0.5 | **Date**: 2026-07-17 | **Status**: Internationalized (Phase 2)

---

## 1 Ten-Dimension Scoring (D1-D10)

Each dimension is scored on a 1-5 scale to quantify the structural characteristics of an industry. 1 = lowest / least significant; 5 = highest / most significant.

| D# | Dimension | Key Question | Scoring Guide |
|----|-----------|-------------|---------------|
| D1 | Industry Lifecycle & Cyclicality | Where is the industry in its cycle? | 1=Declining / 5=Nascent or high-growth |
| D2 | Competitive Intensity (Porter's 5 Forces) | How fierce is competition? | 1=Fragmented / 5=Monopsony or hyper-competitive |
| D3 | Regulatory & Policy Risk | What regulatory frameworks govern this industry? | 1=Stable, light-touch / 5=Frequent, disruptive changes |
| D4 | Technology Disruption Risk | How exposed is the industry to tech disruption? | 1=Minimal disruption risk / 5=Existential tech threat |
| D5 | Capital Intensity & Financing Dependency | How much capital does this industry consume? | 1=Low CapEx, self-funding / 5=Massive, continuous CapEx |
| D6 | Customer Concentration & Bargaining Power | Who holds pricing power? | 1=Dispersed customers / 5=Single or oligopsony customer |
| D7 | Supply Chain Vulnerability | How resilient is the supply chain? | 1=Fully autonomous / 5=Critical external dependencies |
| D8 | Geographic & Sovereign Exposure | Which jurisdictions matter? | 1=Domestic only / 5=Multi-jurisdictional, sanction-sensitive |
| D9 | ESG & Climate Transition Risk | How exposed to ESG/transition risks? | 1=Negligible / 5=Core to business model |
| D10 | Barriers to Entry / Moat Durability | How defensible is the moat? | 1=Commoditized / 5=Unassailable moat |

---

## 2 Six International Paradigms (P1-P6)

Every industry covered by the engine is assigned one of six analysis paradigms. Each paradigm defines:
- **GICS mapping**: indicative sector/industry group coverage
- **Ten-dimension weight template**: which D1-D10 carry the most weight
- **Four-layer pyramid** (L1-L4): layer weights and key indicators
- **Paradigm-specific veto triggers**: one-vote veto conditions

### 2.1 P1 Cyclical

**GICS Mapping**: Energy (GICS 10), Materials (GICS 15), Capital Goods (2010), Chemicals (1510), Shipping (GICS sub-industry 203050), Commodity-focused sub-industries.

**Key Signals**: Commodity prices, capacity utilization rates, freight rates, inventory cycles, PMI indicators.

**Ten-Dimension Weight Template** (heaviest first):
- D10 (Cyclicality) > D7 (Supply Chain) > D2 (Competitive Intensity) > D1 (Lifecycle) > D5 (Capital Intensity)

| Layer | Weight | Focus | Key Indicators | Veto Trigger |
|-------|--------|-------|----------------|--------------|
| L1 Market Cycle Position | 35% | Commodity price trend, capacity utilization, inventory-to-sales ratio, order backlog | Commodity price collapse > 40% from cycle peak with no recovery in sight |
| L2 Cost & Supply Chain | 25% | Input cost structure, supply chain concentration, freight cost exposure, energy cost sensitivity | Critical input supply permanently disrupted (e.g., mine closure, refinery outage) |
| L3 Competitive Positioning | 20% | Cost curve position (decile rank), market share trend, product differentiation, vertical integration | Negative unit economics at mid-cycle prices |
| L4 Financial Resilience | 20% | Debt/EBITDA through cycle, interest coverage at trough, liquidity runway, dividend/capex flexibility | Debt/EBITDA > 6x at mid-cycle + no committed financing |

**Paradigm-Specific Veto Triggers**:
- **V-CYC-1**: Commodity price collapse > 40% from cycle peak with no recovery path
- **V-CYC-2**: Debt/EBITDA > 8x at mid-cycle prices (terminal over-leverage)
- **V-CYC-3**: Critical input supply permanently severed (sanctions, mine depletion, force majeure)

### 2.2 P2 Defensive

**GICS Mapping**: Consumer Staples (GICS 30), Healthcare Equipment & Supplies (3510), Select Utilities (GICS 5510 with regulated tariffs), Food & Beverage (3020), Household & Personal Products (3030).

**Key Signals**: Brand moat depth, pricing power track record, channel density, repeat purchase rate, gross margin stability.

**Ten-Dimension Weight Template** (heaviest first):
- D10 (Barriers to Entry) > D6 (Customer Bargaining) > D1 (Lifecycle) > D4 (Tech Risk) > D2 (Competitive Intensity)

| Layer | Weight | Focus | Key Indicators | Veto Trigger |
|-------|--------|-------|----------------|--------------|
| L1 Brand & Pricing Power | 35% | Gross margin level and stability, pricing authority (annual price change vs. volume change), market share trend, brand equity score | Core brand/product permanently impaired by safety/quality scandal |
| L2 Channel & Distribution | 25% | Channel breadth (outlet count, geographic penetration), distribution network health, inventory turnover, customer retention | Channel collapse > 30% dealer loss in a single year |
| L3 Product Portfolio | 20% | Category lifecycle stage, product diversification, SKU productivity, innovation pipeline, single-product concentration | Single product > 70% revenue + category in structural decline |
| L4 Financial Quality | 20% | Operating cash flow / net income, net debt/EBITDA, ROIC, working capital efficiency (DSO/DIO/DPO/CCC), debt maturity profile | Operating cash flow negative for 3 consecutive years + cash runway < 6 months |

**Paradigm-Specific Veto Triggers**:
- **V-DEF-1**: Major safety/quality scandal leading to national recall or regulatory action (brand value destruction)
- **V-DEF-2**: Single product > 70% revenue + category terminal decline (structural product death)
- **V-DEF-3**: Distributor network collapse (> 30% loss in one year)

### 2.3 P3 Growth

**GICS Mapping**: Semiconductors & Semiconductor Equipment (4530), Software (4510), Biotechnology (3520), Clean Energy Technology (renewable energy equipment, hydrogen, battery tech), Health Care Technology (351030), Electronic Components (4520).

**Key Signals**: Technology roadmap credibility, IP portfolio strength, R&D conversion efficiency, financing runway, product pipeline.

**Ten-Dimension Weight Template** (heaviest first):
- D4 (Technology Disruption) > D5 (Capital Intensity) > D2 (Competitive Intensity) > D1 (Lifecycle) > D9 (ESG)

| Layer | Weight | Focus | Key Indicators | Veto Trigger |
|-------|--------|-------|----------------|--------------|
| L1 Technology & IP | 30% | Technology roadmap credibility, IP portfolio quality (patent strength, grant rate, citation), R&D efficiency, talent concentration, product moat | Key technology pathway becomes obsolete (technical death) |
| L2 Market Position & Pipeline | 25% | Pipeline stage distribution (Phase I/II/III, design wins, product backlog), TAM penetration, competitive differentiation, customer adoption | Critical clinical trial / regulatory filing fails |
| L3 Commercialization & Operations | 20% | Path to profitability, unit economics, revenue growth quality, partnership/licensing quality, supply chain (for hardware) | Cash runway < 6 months + no committed financing |
| L4 Financial Resilience | 25% | Cash burn rate, financing runway, access to capital markets, quality of investors, revenue visibility (backlog, recurring) | No financing path beyond current cash runway |

**Paradigm-Specific Veto Triggers**:
- **V-GRW-1**: Key clinical trial failure / regulatory rejection (product death)
- **V-GRW-2**: Core technology pathway rendered obsolete by competing standard/paradigm
- **V-GRW-3**: Cash runway < 6 months with no committed follow-on financing (liquidity death)

### 2.4 P4 Regulated Utility

**GICS Mapping**: Electric Utilities (5510), Gas Utilities (5520), Multi-Utilities (5530), Water Utilities (5540), Toll Roads, Airports, Regulated Rail Networks, Regulated Pipelines.

**Key Signals**: Regulatory framework quality (independent regulator, tariff formula, allowed ROE), capex plan clarity, rate case outcomes, regulatory asset base (RAB) growth.

**Ten-Dimension Weight Template** (heaviest first):
- D3 (Regulatory Risk) > D5 (Capital Intensity) > D9 (ESG/Climate) > D1 (Lifecycle) > D10 (Moats)

| Layer | Weight | Focus | Key Indicators | Veto Trigger |
|-------|--------|-------|----------------|--------------|
| L1 Regulatory Framework | 35% | Regulatory independence, tariff formula clarity, allowed ROE stability, cost pass-through mechanism, rate case track record | Regulatory license revoked or tariff methodology fundamentally restructured to disallow cost recovery |
| L2 Asset Quality & Capex | 25% | Asset age and condition, RAB growth trajectory, capex plan credibility (regulatory vs. actual), maintenance capex ratio, technology modernization | Asset failure causing prolonged service disruption (safety/regulatory death) |
| L3 Revenue Stability | 20% | Demand volume stability (GDP-linked, weather normalization), tariff escalation history, customer mix (regulated vs. unregulated), off-take agreements | Structural demand decline > 15% p.a. with no tariff adjustment mechanism |
| L4 Financial Structure | 20% | Gearing level, interest coverage (FFO/interest), DSCR, debt maturity profile (average tenor), refinancing risk, credit rating headroom | Gearing > 75% + interest coverage < 1.5x + no equity injection plan |

**Paradigm-Specific Veto Triggers**:
- **V-REG-1**: License revoked or not renewed by regulator
- **V-REG-2**: Fundamental tariff methodology change that disallows cost recovery (regulatory expropriation)
- **V-REG-3**: Catastrophic asset failure (nuclear incident, dam breach, pipeline explosion) leading to nationalization

### 2.5 P5 Financial

**GICS Mapping**: Banks (GICS 4010), Diversified Financials (4020), Insurance (4030), Asset Managers & Custody Banks, REITs (GICS 6010), Mortgage Finance, Consumer Finance.

**Key Signals**: Capital adequacy (CET1, Solvency II ratio), asset quality (NPL ratio, provisioning coverage), liquidity coverage (LCR, NSFR), net interest margin trend, ROE.

**Ten-Dimension Weight Template** (heaviest first):
- D3 (Regulatory Risk) > D2 (Competitive Intensity) > D9 (ESG/Climate) > D5 (Capital Intensity) > D10 (Moats)

| Layer | Weight | Focus | Key Indicators | Veto Trigger |
|-------|--------|-------|----------------|--------------|
| L1 Capital Adequacy & Asset Quality | 35% | CET1 ratio (banks), Solvency ratio (insurance), NPL ratio, provisioning coverage, asset concentration, loan-to-value distribution | CET1 < regulatory minimum (Pillar 1 + buffers) or NPL ratio > 10% without adequate provisioning |
| L2 Funding & Liquidity | 25% | LCR, NSFR, deposit funding ratio, wholesale funding dependence, debt maturity profile, access to central bank facilities | Deposit run > 10% in one quarter or wholesale funding access severed |
| L3 Earnings Capacity | 20% | Net interest margin trend, fee income diversification, cost/income ratio, ROE vs. cost of equity, earnings volatility through cycle | ROE < cost of equity for 3 consecutive years with no turnaround plan |
| L4 Risk Management & Governance | 20% | Risk governance framework, underwriting standards track record, credit risk concentration, market risk VaR, operational risk incidents | Major fraud, sanction violation, or AML breach leading to regulatory enforcement |

**Paradigm-Specific Veto Triggers**:
- **V-FIN-1**: Capital ratio falls below regulatory minimum (Pillar 1 + conservation buffer)
- **V-FIN-2**: Deposit run or wholesale funding freeze
- **V-FIN-3**: Regulatory enforcement action for capital adequacy or AML/sanctions violations that restricts operations

### 2.6 P6 Sovereign-Linked

**GICS Mapping**: Sovereigns (national governments), Sub-Sovereigns (provinces, states, municipalities), Government-Sponsored Enterprises (GSEs), Development Finance Institutions (DFIs), Supranational Organizations, Public Sector Entities.

**Key Signals**: Fiscal space (debt/GDP, fiscal deficit/GDP, interest/revenue), external balances (current account, FX reserves, external debt), institutional strength (World Bank governance indicators, rule of law), political stability.

**Ten-Dimension Weight Template** (heaviest first):
- D8 (Geographic/Sovereign Exposure) > D3 (Regulatory/Policy Risk) > D5 (Capital Intensity) > D9 (ESG) > D1 (Lifecycle)

| Layer | Weight | Focus | Key Indicators | Veto Trigger |
|-------|--------|-------|----------------|--------------|
| L1 Fiscal & Debt Sustainability | 35% | Debt/GDP, fiscal deficit/GDP, interest expense/revenue, primary balance, contingent liabilities (PPP, SOEs) | Debt/GDP > 100% with persistent primary deficit + no credible adjustment path |
| L2 External Position & Monetary Flexibility | 25% | Current account balance/GDP, FX reserves (months of imports), external debt/GDP, exchange rate regime flexibility, reserve currency access | External debt > 200% of FX reserves + no IMF/IFI program in place |
| L3 Institutional & Governance Strength | 20% | Rule of law (WGI), government effectiveness, regulatory quality, control of corruption, political stability, debt repayment history | Sovereign default or restructuring within past 10 years without policy reform |
| L4 Contingent Liability & SOE Risk | 20% | SOE sector size (SOE assets/GDP), SOE financial health (debt/EBITDA, subsidy dependence), PPP guarantee exposure, sub-sovereign debt risk | SOE sector requiring fiscal transfer > 2% of GDP annually with no restructuring |

**Paradigm-Specific Veto Triggers**:
- **V-SOV-1**: Sovereign default, restructuring, or coercive exchange (redenomination)
- **V-SOV-2**: International sanctions restricting access to global capital markets (e.g., SDN listing)
- **V-SOV-3**: Hyperinflation > 50% per month or currency collapse > 40% in one quarter
- **V-SOV-4**: Sovereign credit rating downgraded to default (SD/RD) by at least one major agency

---

## 3 Paradigm Determination Logic

### 3.1 GICS Industry-to-Paradigm Mapping

| GICS Sector | GICS Industry Group | Primary Paradigm | Secondary Attribute | Determination Rationale |
|-------------|---------------------|------------------|-------------------|------------------------|
| 10 Energy | 1010 Energy | P1 Cyclical | — | Commodity-driven, freight/price cycle dependent |
| 15 Materials | 1510 Materials | P1 Cyclical | — | Commodity price cycle primary risk driver |
| 2010 Capital Goods | 201010 Aerospace & Defense, 201020 Building Products, 201030 Construction & Engineering, 201040 Electrical Equipment, 201050 Industrial Conglomerates, 201060 Machinery, 201070 Trading Companies & Distributors | P1 Cyclical | P2 Defensive (select sub-industries) | Demand tied to business investment cycle; some sub-industries have brand/aftermarket moats |
| 15 Chemicals | 151010 Chemicals | P1 Cyclical | — | Commodity or specialty chemical price cycles |
| 20 Transportation | 2030 Transportation (select: Shipping 203050) | P1 Cyclical | — | Freight rate cycle, capacity utilization |
| 20 Industrials | 2020 Commercial & Professional Services | P1 Cyclical | P3 Growth (platform-scaled services) | Corporate spending cycle primary; platform sub-industries have growth attributes |
| 50 Communication Services | 5010 Telecommunication Services | P4 Regulated Utility | P3 Growth (5G/digital services) | Licensed spectrum, regulated networks, infrastructure capex |
| 25 Consumer Discretionary | 2510 Automobiles & Components | P1 Cyclical | P3 Growth (EV/autonomous transition) | Big-ticket consumer cycle; technology disruption overlay |
| 25 Consumer Discretionary | 2520/2530 Consumer Durables & Apparel / Leisure Products | P1 Cyclical | P2 Defensive (brand moats) | Deferrable purchases, replacement cycle; brand provides partial cushion |
| 25 Consumer Discretionary | 2550 Retailing (discretionary & multiline) | P1 Cyclical | P2 Defensive (staples-anchored retail) | Consumer spending cycle; staples-anchored formats are defensive |
| 30 Consumer Staples | 3010 Retailing (Food & Staples), 3020 Food & Beverage, 3030 Household & Personal Products | P2 Defensive | — | Inelastic demand, brand moat, pricing power |
| 35 Healthcare | 3510 Healthcare Equipment & Supplies | P2 Defensive / P3 Growth | — | MedTech=Defensive; Biotech=Growth; Pharma=mixed |
| 55 Utilities | 5510 Electric, 5520 Gas, 5530 Multi, 5540 Water | P4 Regulated Utility | P2 Defensive (vertically integrated IPP) | Regulated tariff, license-based |
| 45 Information Technology | 4510 Software & Services, 4520 Technology Hardware & Equipment, 4530 Semiconductors | P3 Growth | P1 Cyclical (hardware, memory) | Technology-driven revenue growth, IP core |
| 35 Healthcare | 3520 Biotechnology, 352010 Pharmaceuticals | P3 Growth | P2 Defensive (Pharma) | Pipeline-dependent, patent cliff, R&D heavy |
| 40 Financials | 4010 Banks, 4020 Diversified Financials, 4030 Insurance | P5 Financial | — | Capital adequacy and asset quality core |
| 60 Real Estate | 6010 REITs, 6020 Real Estate Management | P5 Financial | — | Cap rate, LTV, rent roll |
| — | Sovereigns, Sub-Sovereigns, GSEs, DFIs | P6 Sovereign-Linked | — | Fiscal capacity, institutional strength |
| Infrastructure | Toll Roads, Airports, Regulated Networks | P4 Regulated Utility | P1 Cyclical (traffic-dependent) | Concession/regulatory framework core |
| 2030 Transportation | Transport Infrastructure (Rail, Ports, Airports) | P4 Regulated Utility | P1 Cyclical | Regulated access pricing, traffic cycle |

### 3.1a Bridge to the 19-Industry Contagion Matrix

The contagion matrix ([contagion-matrix.md](contagion-matrix.md) §1.2) uses 19 canonical industry names. The bridge below maps each matrix industry to its primary paradigm and its §3.1 GICS row, so that every matrix industry has exactly one framework home:

| Contagion-Matrix Industry | Primary Paradigm | §3.1 GICS Row |
|---|---|---|
| **Energy (Oil & Gas)** | P1 Cyclical | 10 Energy / 1010 Energy |
| **Chemicals** | P1 Cyclical | 15 Chemicals / 151010 Chemicals |
| **Metals & Mining** | P1 Cyclical | 15 Materials / 1510 Materials |
| **Construction Materials** | P1 Cyclical | 15 Materials / 1510 Materials |
| **Capital Goods** | P1 Cyclical | 2010 Capital Goods |
| **Commercial Services** | P1 Cyclical | 2020 Commercial & Professional Services |
| **Transportation (Air/Rail/Shipping)** | P4 Regulated Utility | 2030 Transportation / Transport Infrastructure (shipping sub-industry carries P1 secondary) |
| **Automobiles** | P1 Cyclical | 2510 Automobiles & Components |
| **Consumer Durables** | P1 Cyclical | 2520/2530 Consumer Durables & Apparel / Leisure Products |
| **Consumer Staples** | P2 Defensive | 30 Consumer Staples / 3010-3030 |
| **Retail** | P1 Cyclical | 2550 Retailing (discretionary & multiline) |
| **Technology Hardware (Semis)** | P3 Growth | 45 Information Technology / 4520-4530 |
| **Software & Services** | P3 Growth | 4510 Software & Services |
| **Biotech & Pharma** | P3 Growth | 3520 Biotechnology / 352010 Pharmaceuticals |
| **Healthcare Equipment** | P2 Defensive | 3510 Healthcare Equipment & Supplies |
| **Utilities (Regulated)** | P4 Regulated Utility | 55 Utilities / 5510-5540 |
| **Telecommunications** | P4 Regulated Utility | 5010 Telecommunication Services |
| **Financials (Banks/Insurance)** | P5 Financial | 40 Financials / 4010-4030 |
| **Sovereigns & GSEs** | P6 Sovereign-Linked | Sovereigns, Sub-Sovereigns, GSEs, DFIs |

### 3.2 Paradigm Determination Decision Tree

```
Step 1: Is the obligor a sovereign, sub-sovereign, GSE, or DFI?
  YES → P6 Sovereign-Linked
  NO  → Step 2

Step 2: Is the obligor a regulated utility (electric/gas/water, toll road, airport, regulated pipeline)?
  YES → P4 Regulated Utility
  NO  → Step 3

Step 3: Is the obligor a financial institution (bank, insurance, asset manager, REIT)?
  YES → P5 Financial
  NO  → Step 4

Step 4: Does the obligor operate in a structurally growing industry driven by technology/IP?
  (e.g., Semiconductors, Software, Biotech, Clean Energy Tech)
  YES → P3 Growth
  NO  → Step 5

Step 5: Is demand for the obligor's product/service relatively inelastic to economic cycles?
  (e.g., Consumer Staples, Healthcare Equipment, Select Utilities)
  YES → P2 Defensive
  NO  → Step 6

Step 6: Is the obligor's revenue primarily driven by commodity prices, freight rates, capacity utilization,
  or cyclical business/consumer spending?
  (e.g., Energy, Materials, Chemicals, Capital Goods, Shipping, Automobiles,
   Consumer Durables, discretionary Retail, Commercial Services)
  YES → P1 Cyclical
  NO  → Re-evaluate industry classification or mark as "Special Structure" per Section 3.4
```

### 3.3 Paradigm Conflict Resolution

When an industry triggers conditions for multiple paradigms, the following priority rules apply:

1. **P6 Sovereign-Linked** > all others (sovereign credit path is disjoint)
2. **P5 Financial** > all others (financial institutions require dedicated capital adequacy framework)
3. **P4 Regulated Utility** > P1/P2/P3 (license-based revenue stream dominates)
4. **P3 Growth** > P1/P2 when technology/IP is the primary value driver (e.g., Biotech > Defensive)
5. **P1 Cyclical** and **P2 Defensive** conflict: resolve by demand elasticity; if demand drop > 20% in a recession, default to P1 Cyclical

### 3.4 Special Structure Notes

| Industry | Special Structure | Notes |
|----------|-----------------|-------|
| **Pharmaceuticals (Large Cap)** | Dual-track (P2+P3) | P3 for pipeline assessment, P2 for defensive cash flows from marketed drugs |
| **Semiconductors** | Layered (P3 + P1 overlay) | P3 (technology roadmap) primary; P1 (cyclical demand from memory/commodity chips) secondary overlay |
| **Automobiles** | Layered (P1 + P3 overlay) | P1 (demand cycle, input costs) primary; P3 (EV/autonomous technology roadmap) secondary overlay |
| **Clean Energy** | Dual-track (P3 + P4) | Technology development → P3; infrastructure/project finance → P4 |
| **Airports / Ports** | Hybrid (P4 + P1) | Regulatory framework primary (P4); traffic/volume cycle secondary (P1) |
| **Multi-line Insurers** | Mixed (P5 + P2) | Life insurance → P5; P&C with defensive characteristics → P2 overlay |
| **Large Cap Oil & Gas** | P1 primary + P9 overlay | Commodity cycle dominates (P1); ESG transition risk overlay (P4/D9 weights elevated) |

---

## 4 Industry Pyramids

### 4.1 Four-Layer Pyramid Architecture

Each paradigm uses a weighted pyramid with four layers. The weight distribution governs how strongly each layer contributes to the final credit score.

| Paradigm | L1 (Heaviest) | L2 | L3 | L4 (Lightest) |
|----------|---------------|-----|-----|----------------|
| **P1 Cyclical** | 35% Market Cycle Position | 25% Cost & Supply Chain | 20% Competitive Positioning | 20% Financial Resilience |
| **P2 Defensive** | 35% Brand & Pricing Power | 25% Channel & Distribution | 20% Product Portfolio | 20% Financial Quality |
| **P3 Growth** | 30% Technology & IP | 25% Market Position & Pipeline | 20% Commercialization & Operations | 25% Financial Resilience |
| **P4 Regulated Utility** | 35% Regulatory Framework | 25% Asset Quality & Capex | 20% Revenue Stability | 20% Financial Structure |
| **P5 Financial** | 35% Capital Adequacy & Asset Quality | 25% Funding & Liquidity | 20% Earnings Capacity | 20% Risk Management & Governance |
| **P6 Sovereign-Linked** | 35% Fiscal & Debt Sustainability | 25% External Position & Monetary Flexibility | 20% Institutional & Governance Strength | 20% Contingent Liability & SOE Risk |

### 4.2 Key Dimension Weights per Paradigm

| Paradigm | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 |
|----------|----|----|----|----|----|----|----|----|----|-----|
| **P1 Cyclical** | 15% | 10% | 5% | 5% | 15% | 5% | 15% | 10% | 5% | 15% |
| **P2 Defensive** | 10% | 5% | 5% | 10% | 5% | 15% | 5% | 5% | 10% | 30% |
| **P3 Growth** | 15% | 10% | 5% | 25% | 15% | 5% | 5% | 5% | 10% | 5% |
| **P4 Regulated Utility** | 10% | 5% | 30% | 5% | 15% | 5% | 5% | 5% | 15% | 5% |
| **P5 Financial** | 5% | 15% | 25% | 5% | 15% | 5% | 5% | 10% | 10% | 5% |
| **P6 Sovereign-Linked** | 10% | 5% | 20% | 5% | 15% | 5% | 5% | 20% | 10% | 5% |

### 4.3 Weight Adjustment Rules

| Adjustment Condition | Adjustment | Applicable Paradigm(s) | Scenario |
|---------------------|------------|------------------------|----------|
| Commodity price volatility > 40% YoY | L4 Financial up to 25%, L1 down to 30% | P1 Cyclical | Extreme cycle amplitude |
| Regulatory framework change imminent | L1 Regulatory up to 40%, L3 down to 15% | P4 Regulated Utility | Rate case uncertainty |
| Pre-revenue / pre-profit stage | L4 Financial up to 30%, L1 down to 25% | P3 Growth | Early-stage biotech or pre-revenue tech |
| Deposit-funded > 70% liabilities | L2 Liquidity weight up to 30% | P5 Financial | Retail-heavy bank |
| External debt in foreign currency > 50% | L2 External up to 30%, L1 down to 30% | P6 Sovereign-Linked | Hard-currency debt reliance |
| Brand revenue > 40% of sales | L1 Brand up to 40%, L3 down to 15% | P2 Defensive | Luxury goods, premium brands |
| Single regulator / unscheduled rate review | P4: add 5% regulatory layer | P4 Regulated Utility | Non-independent regulator risk |

### 4.4 Five-Layer Special Structures

A small number of industries require five-layer pyramids due to structural complexity.

**Semiconductors (P3 Growth + P1 Cyclical overlay)**

| Layer | Weight | Focus | Key Indicators |
|-------|--------|-------|----------------|
| L1 Geopolitical / Trade | 25% | Export control risk (EAR/ITAR), entity list/SDN exposure, equipment supply chain security, IP licensing restrictions, foundry dependence | Entity list / SDN listing |
| L2 Technology & Roadmap | 25% | Process node position (nm), roadmap credibility (tape-out success rate), IP portfolio quality, R&D conversion efficiency, talent depth, design win pipeline | — |
| L3 Market Position | 20% | Market share trend, end-customer quality, design win pipeline, ASP/gross margin trend, substitution threat | — |
| L4 Capital & Financing | 15% | Access to capital markets, government support/grants, capex intensity, cash runway, R&D tax credits | — |
| L5 Financial | 15% | Cash runway, working capital efficiency, AR quality, goodwill/assets ratio, related-party exposure, debt maturity profile | Goodwill/assets > 20% + interest coverage < 2x |

---

## 5 Veto Mechanism

### 5.1 Core Principles

Every veto across all paradigms shares three common characteristics:

1. **Survival risks, not performance risks** — The concern is not "underperformance" but "the entity may cease to exist"
2. **Irreversible or near-irreversible** — Technology obsolescence, regulatory license revocation, clinical trial failure, and default are all effectively irreversible
3. **Rating ceiling of CCC upon trigger** — Financial analysis becomes moot; recovery assessment begins

### 5.2 Paradigm Veto Summary Table

| Paradigm | Veto Code | Condition | Risk Type | Waivable? |
|----------|-----------|-----------|-----------|-----------|
| **P1 Cyclical** | V-CYC-1 | Commodity price collapse > 40% from cycle peak + no recovery path | Market death | No |
| | V-CYC-2 | Debt/EBITDA > 8x at mid-cycle prices | Leverage death | Analyst Committee |
| | V-CYC-3 | Critical input supply permanently severed | Supply chain death | No |
| **P2 Defensive** | V-DEF-1 | Major safety/quality scandal (national recall, regulatory action) | Brand death | No |
| | V-DEF-2 | Single product > 70% revenue + category structural decline | Product death | Analyst Committee |
| | V-DEF-3 | Distributor network collapse (> 30% loss in one year) | Channel death | Analyst Committee |
| **P3 Growth** | V-GRW-1 | Key clinical trial / regulatory filing failure | Product death | No |
| | V-GRW-2 | Core technology pathway rendered obsolete | Technological death | No |
| | V-GRW-3 | Cash runway < 6 months + no committed financing | Liquidity death | No |
| **P4 Regulated Utility** | V-REG-1 | License revoked or not renewed | Regulatory death | No |
| | V-REG-2 | Fundamental tariff restructuring disallowing cost recovery | Economic expropriation | No |
| | V-REG-3 | Catastrophic asset failure (nuclear, dam, pipeline) | Operational death | No |
| **P5 Financial** | V-FIN-1 | Capital ratio below regulatory minimum (Pillar 1 + buffers) | Capital death | No |
| | V-FIN-2 | Deposit run > 10% in one quarter or wholesale funding freeze | Liquidity death | No |
| | V-FIN-3 | Major regulatory enforcement action restricting operations | Regulatory death | Analyst Committee |
| **P6 Sovereign-Linked** | V-SOV-1 | Sovereign default, restructuring, or coercive exchange | Credit death | No |
| | V-SOV-2 | International sanctions restricting capital market access | Sanctions death | No |
| | V-SOV-3 | Hyperinflation (> 50%/month) or currency collapse (> 40%/quarter) | Monetary death | No |
| | V-SOV-4 | Sovereign downgraded to default (SD/RD) by major agency | Rating death | No |

### 5.3 Veto Trigger Process Flow

```
Veto condition triggered
    |
    v
Rating ceiling automatically locked at CCC
    |
    v
Analyst Committee convenes within 48 hours
    |--- Confirms trigger: Maintain CCC or below, initiate exit/recovery process
    |--- Grants waiver (waivable conditions only): Document rationale, ceiling raised to B-
    |
    v
Notify relevant stakeholders (creditors, bondholders, regulators)
    |
    v
Add to credit event monitoring list, monthly update required
```

### 5.4 Veto Waiver Criteria

Only explicitly marked "Analyst Committee" conditions in Section 5.2 are eligible for waiver. The committee must document:

1. The specific mitigating factor (e.g., pending equity injection, government support commitment, binding offtake agreement)
2. The expected timeline for resolution (maximum 12 months)
3. A downside scenario and contingency plan if the resolution fails
4. The rationale for raising the rating ceiling to B- (not higher)

### 5.5 Cross-Paradigm Veto Interactions

When a dual-track industry (Section 3.4) triggers a veto in one track but not the other:

- **Both tracks must be vetoed** for the combined rating to be locked at CCC
- If only one track triggers a veto, the rating ceiling is capped at B (not CCC)
- Exception: P6 Sovereign-Linked vetoes always override all other paradigm vetoes (Sovereign ceiling applies)

---

## Appendix A: D1-D10 Score Definitions by Paradigm

Each paradigm interprets the ten dimensions differently:

| Dimension | P1 Cyclical | P2 Defensive | P3 Growth | P4 Regulated Utility | P5 Financial | P6 Sovereign-Linked |
|-----------|-------------|--------------|-----------|---------------------|--------------|---------------------|
| D1 Lifecycle | Commodity super-cycle position | Category maturity (growth/stable/decline) | Technology S-curve stage | Infrastructure age & demand saturation | Sector penetration (banked vs. unbanked) | Demographic & development stage |
| D2 Competitive Intensity | Global capacity share concentration | Brand/concentration ratios (HHI) | Patent landscape concentration | Concession exclusivity | Market structure (oligopoly vs. fragmented) | Multipolar vs. unipolar system |
| D3 Regulatory Risk | Trade policy, tariffs, export controls | Food safety, labeling, advertising | Clinical trial regulation, data privacy, FDA/EMA | Tariff methodology, license terms | Basel/Solvency, capital requirements | Sovereign credit framework |
| D4 Technology Disruption | Automation, substitution threat | E-commerce disruption, DTC | Competing technology standards | Grid modernization, smart grid, renewables | Fintech, digital banking disruption | Digital currency, CBDC |
| D5 Capital Intensity | Sustaining + maintenance capex | Low/working capital only | R&D intensity, prototyping capex | Network RAB growth, grid replacement | Regulatory capital, CET1 | Debt servicing capacity, access to capital |
| D6 Customer Bargaining Power | Offtake concentration (single buyer) | Consumer repeat purchase | Early adopter concentration | Captive customer base (no alternative) | Depositor vs. borrower power | IFI/concessional lender leverage |
| D7 Supply Chain Vulnerability | Input concentration, shipping route risk | Agricultural input, packaging | Equipment/chemical supply (semicon, bioprocess) | Fuel supply (gas/coal for power) | Wholesale funding concentration | Import dependency, trade route block |
| D8 Geographic Exposure | Jurisdictional production/refining mix | Domestic vs. international revenue | Cross-border IP enforcement | Service territory exclusivity | Cross-border lending exposure | Sanctions, FX regime, reserve currency |
| D9 ESG / Climate | Carbon intensity, methane, water | Packaging waste, scope 3 emissions | E-waste, energy intensity of compute | Coal phase-out, renewable mandate, CBAM | Climate loan exposure, green finance | Paris alignment, climate vulnerability |
| D10 Barriers to Entry | Resource access, scale, cost curve | Brand equity, distribution density | IP, patents, regulatory exclusivity | Natural monopoly, license exclusivity | Charter value, regulatory license | Sovereignty, hard currency status |

---

## Appendix B: Ten-Dimension Score Summary Matrix

> Representative scores for illustrative credit-covered industries (mapped to international paradigms).

| Dimension | Semiconductors | Software | Pharmaceuticals | Banking | Electric Utilities | Electric Vehicles | Sovereign (IG) | Sovereign (HY) |
|-----------|---------------|----------|-----------------|---------|-------------------|-------------------|----------------|-----------------|
| D1 Lifecycle | 4 | 5 | 4 | 4 | 4 | 3 | 4 | 3 |
| D2 Competitive Intensity | 3 | 3 | 3 | 3 | 2 | 4 | 2 | 3 |
| D3 Regulatory Risk | 5 | 2 | 4 | 5 | 4 | 3 | 4 | 4 |
| D4 Technology Disruption | 4 | 4 | 3 | 3 | 3 | 5 | 1 | 2 |
| D5 Capital Intensity | 5 | 2 | 4 | 4 | 5 | 4 | 3 | 4 |
| D6 Customer Bargaining Power | 3 | 2 | 3 | 2 | 2 | 4 | 2 | 2 |
| D7 Supply Chain Vulnerability | 5 | 1 | 3 | 2 | 3 | 3 | 3 | 4 |
| D8 Geographic Exposure | 4 | 3 | 3 | 3 | 2 | 4 | 5 | 4 |
| D9 ESG / Climate | 3 | 2 | 2 | 3 | 5 | 3 | 3 | 3 |
| D10 Barriers to Entry | 4 | 3 | 4 | 3 | 5 | 2 | 4 | 3 |
| **Paradigm** | **P3 Growth** | **P3 Growth** | **P3/P2** | **P5 Financial** | **P4 Regulated** | **P1 Cyclical** | **P6 Sovereign** | **P6 Sovereign** |

---

## Appendix C: Comparison with Legacy (v0.7) Paradigm Mapping

| Legacy Paradigm (v0.7, Chinese) | International Paradigm (v0.8, English) | Key Differences |
|--------------------------------|----------------------------------------|-----------------|
| Policy-Driven | Mapped to P4 Regulated Utility + P6 Sovereign-Linked | Geographic relevance split: regulated infrastructure vs. sovereign credit |
| Technology-Barrier | Mapped to P3 Growth | Broadened from China-specific tech dependency to global tech/IP analysis |
| Consolidation / Zero-Sum | Absorbed into P1 Cyclical + P2 Defensive | Sector-specific: cyclical saturation -> P1; brand consolidation -> P2 |
| Asset-Lease | Distributed into P4 (concession/regulated assets) + P5 (REITs) | Physical lease assets -> P4; financial lease/reit -> P5 |
| Brand+Channel | Absorbed into P2 Defensive | Broader defensive framework with L1 brand and L2 channel layers |
| Network+Traffic | Distributed into P4 (regulated infrastructure) + P1 (cyclical transport) | Regulated network -> P4; cyclical volume -> P1 |

---

## Related Content

- [Engine Architecture Overview](engine-overview.md) -- Core philosophy, architecture, design principles
- [Dual-Track Methodology](dual-track-methodology.md) -- Track A + Track B scoring logic, cross-collision, rating mapping
- [Mosaic Engine](mosaic-engine.md) -- Signal extraction, puzzle assembly, completeness assessment
- [Dimension Registry](dimension-registry.md) -- Machine-readable index of paradigms and stakeholder roles
- [Brand & Channel Paradigm](paradigm-brand-channel.md) -- Legacy P2/Defensive application for consumer industries
- [Network & Traffic Paradigm](paradigm-network-traffic.md) -- Legacy application for transport and platform industries

---

*This document replaces the v0.7 Chinese industry-framework.md. The six-international-paradigm architecture aligns the engine with GICS-based global standards while preserving all veto and pyramid analysis capabilities.*
