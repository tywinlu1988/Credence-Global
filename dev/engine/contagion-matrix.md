# International Industry Contagion Matrix

**Version**: v0.0.1 | **Date**: 2026-07-10

> **[PRELIMINARY]** Matrix intensities are initial methodological estimates pending empirical calibration against international default correlation data. All scores are theoretical constructs based on economic linkage analysis and historical precedent mapping, not statistical estimation. Users should treat these as directional indicators rather than precise measures.

---

## Table of Contents

1. [Industry Classification and Paradigm Mapping](#1-industry-classification-and-paradigm-mapping)
2. [Contagion Matrix — 19x19 Intensity Grid](#2-contagion-matrix--19x19-intensity-grid)
3. [Contagion Pathways and Graph Representation](#3-contagion-pathways-and-graph-representation)
4. [Matrix Construction Logic](#4-matrix-construction-logic)
5. [Derived Metrics — Super-Spreaders, Vulnerability, and Coefficients](#5-derived-metrics--super-spreaders-vulnerability-and-coefficients)
6. [Stress Escalation — Factor-Specific Intensity Jumps](#6-stress-escalation--factor-specific-intensity-jumps)
7. [Integration with Engine Components](#7-integration-with-engine-components)
8. [Limitations](#8-limitations)
9. [Appendix](#9-appendix)

---

## 1. Industry Classification and Paradigm Mapping

### 1.1 Paradigm Framework

Based on [Contagion Theory](contagion-theory.md) Section 4, each international industry is mapped to a primary and secondary analytical paradigm. Industries sharing the same paradigm exhibit **higher intrinsic contagion coupling** due to shared risk drivers, funding characteristics, and market narrative logic.

| Paradigm | Description | Core Characteristics |
|---|---|---|
| **P1: Policy-Driven** | Sectors where government policy, regulation, geopolitics, or fiscal/tax regimes determine demand cycles and profitability | Regulatory sensitivity, policy cycle dependence, geopolitical exposure |
| **P2: Technology Moat** | R&D-intensive sectors where IP, patents, and proprietary technology create durable competitive advantage | High R&D intensity, patent concentration, skilled labor dependence |
| **P3: Zero-Sum Game** | Cyclical, commoditized sectors where price competition erodes margins; one player's gain is another's loss | Overcapacity risk, price elasticity, cyclical demand |
| **P4: Asset Lease** | Infrastructure-heavy sectors where cash flows are asset-utilization driven; NOI and DSCR are key metrics | High fixed assets, long-duration contracts, infrastructure financing |
| **P5: Brand + Channel** | Consumer sectors where brand equity, distribution networks, and consumer trust are primary value drivers | Brand intangible value, channel dependency, consumer trust sensitivity |
| **P6: Network + Traffic** | Platform and network-effect sectors where scale, user base, and data generate increasing returns | Network effects, multi-sided platforms, scale economics |

### 1.2 Industry-to-Paradigm Mapping Table

| # | Industry | Primary Paradigm | Secondary Paradigm | Financial Intensity | Rationale |
|---|---|---|---|---|---|
| 1 | **Energy (Oil & Gas)** | P1 (Policy-Driven) | P4 (Asset Lease) | High | Geopolitical commodity, OPEC+ policy dependence, E&P infrastructure-heavy |
| 2 | **Chemicals** | P1 (Policy-Driven) | P2 (Technology Moat) | Medium | Environmental regulation, specialty chemicals IP, energy cost dependence |
| 3 | **Metals & Mining** | P3 (Zero-Sum Game) | P1 (Policy-Driven) | Medium | Commodity price cycle dominance, resource nationalism, trade policy |
| 4 | **Construction Materials** | P4 (Asset Lease) | P1 (Policy-Driven) | Medium | Infrastructure corridor-dependent, quarries/plants as fixed assets |
| 5 | **Capital Goods** | P2 (Technology Moat) | P4 (Asset Lease) | Medium-High | Engineering IP, manufacturing plant as asset, defense/industrial policy |
| 6 | **Commercial Services** | P6 (Network + Traffic) | P3 (Zero-Sum Game) | Low-Medium | B2B service platform effects, labor-intensive, fragmented |
| 7 | **Transportation (Air/Rail/Shipping)** | P4 (Asset Lease) | P6 (Network + Traffic) | High | Fleet/network infrastructure, fuel leverage, network economies |
| 8 | **Automobiles** | P3 (Zero-Sum Game) | P2 (Technology Moat) | High | Overcapacity, price war risk, EV/autonomous tech disruption |
| 9 | **Consumer Durables** | P5 (Brand + Channel) | P3 (Zero-Sum Game) | Low-Medium | Brand differentiation, replacement cycle, price competition |
| 10 | **Consumer Staples** | P5 (Brand + Channel) | P2 (Technology Moat) | Low | Brand loyalty, stable demand, R&D in food/CPG innovation |
| 11 | **Retail** | P6 (Network + Traffic) | P5 (Brand + Channel) | Medium | Omnichannel network, platform scale, private label brand leverage |
| 12 | **Technology Hardware (Semis)** | P2 (Technology Moat) | P1 (Policy-Driven) | High | Moore's Law IP, fab capex, chip policy (CHIPS Act), export controls |
| 13 | **Software & Services** | P2 (Technology Moat) | P6 (Network + Traffic) | Medium | SaaS/IP, network effects, cloud platform economies |
| 14 | **Biotech & Pharma** | P2 (Technology Moat) | P1 (Policy-Driven) | Medium-High | Patent cliff, FDA/EMA regulation, pipeline value dependence |
| 15 | **Healthcare Equipment** | P2 (Technology Moat) | P1 (Policy-Driven) | Medium | Device IP, FDA clearance, hospital procurement sensitivity |
| 16 | **Utilities (Regulated)** | P4 (Asset Lease) | P1 (Policy-Driven) | High | Regulated asset base (RAB), tariff policy, long-lived infrastructure |
| 17 | **Telecommunications** | P4 (Asset Lease) | P6 (Network + Traffic) | High | Spectrum/network assets, subscriber base, 5G capex cycle |
| 18 | **Financials (Banks/Insurance)** | P1 (Policy-Driven) | P6 (Network + Traffic) | Very High | Capital regulation, sovereign exposure, payment network effects |
| 19 | **Sovereigns & GSEs** | P1 (Policy-Driven) | — (Special: Gov't Credit Binding) | Very High | Fiscal capacity, monetary control, quasi-government guarantee |

### 1.3 Paradigm Clusters

| Paradigm | Industries | Intra-Paradigm Contagion Characteristics |
|---|---|---|
| **P1 (Policy-Driven)** | Energy, Chemicals, Financials, Sovereigns & GSEs; secondary for Metals, Construction Materials, TechHW, Biotech, Utilities, Telecom | Policy shifts synchronize across sectors; regulatory change can affect multiple P1 industries simultaneously; geopolitical risk is shared |
| **P2 (Technology Moat)** | Capital Goods, TechHW, Software, Biotech, Healthcare Equipment; secondary for Chemicals, Automobiles, Consumer Staples | Supply chain tight coupling (chip → equipment → software); IPO/venture capital funding channels shared; talent market co-dependence |
| **P3 (Zero-Sum Game)** | Metals & Mining, Automobiles, Consumer Durables; secondary for Commercial Services | Commodity price cycle; overcapacity risk; price war contagion across similar end-markets |
| **P4 (Asset Lease)** | Construction Materials, Transportation, Utilities, Telecom; secondary for Energy, Capital Goods | Infrastructure funding channels (project finance, green bonds); interest rate sensitivity; regulatory concession risk |
| **P5 (Brand + Channel)** | Consumer Durables, Consumer Staples; secondary for Retail | Consumer confidence resonance; brand crisis demonstration effects; advertising and distribution cost linkage |
| **P6 (Network + Traffic)** | Commercial Services, Retail, Transportation (secondary), Telecom (secondary), Software (secondary), Financials (secondary) | Platform interdependence (e-commerce + shipping + payments); data flow integration; user base cross-pollination |

---

## 2. Contagion Matrix — 19x19 Intensity Grid

### 2.1 Intensity Heatmap

The table below presents the 19x19 contagion intensity scoring matrix. Values indicate: 1 = Very Weak, 2 = Weak, 3 = Moderate, 4 = Strong, 5 = Very Strong. Rows = contagion source industry, Columns = contagion receptor industry. Diagonal is marked "-" (self).

```
         │ Ene Che Met Cst Cap Com Trn Aut Cdu Cst Ret Tec Sft Btp Hce Uti Tel Fin Sov
─────────┼─────────────────────────────────────────────────────────────────────────────────
Energy   │  -   5   3   2   3   2   4   3   1   2   1   1   1   1   1   4   1   3   3
Chemicals│  5   -   2   3   2   1   2   3   3   4   1   3   1   4   2   1   1   2   2
Metals   │  3   2   -   4   4   1   2   2   2   1   1   2   1   1   1   2   1   2   3
ConstMat │  2   3   4   -   3   1   2   1   1   1   1   1   1   1   1   3   1   2   3
CapGoods │  3   2   4   3   -   2   3   3   2   1   1   4   2   2   3   2   1   3   2
ComServ  │  2   1   1   1   2   -   3   1   1   2   3   2   3   1   1   1   2   3   1
Transp   │  4   2   2   2   3   3   -   2   2   2   4   1   2   1   1   2   1   3   2
Autos    │  3   3   2   1   3   1   2   -   3   1   1   4   2   1   1   1   1   2   1
ConsDur  │  1   3   2   1   2   1   2   3   -   2   3   3   1   1   1   1   1   2   1
ConsStap │  2   4   1   1   1   2   2   1   2   -   3   1   1   1   1   1   1   2   1
Retail   │  1   1   1   1   1   3   4   1   3   3   -   1   3   1   1   1   2   2   1
TechHW   │  1   3   2   1   4   2   1   4   3   1   1   -   4   2   3   2   3   3   2
Soft&Srv │  1   1   1   1   2   3   2   2   1   1   3   4   -   1   1   1   4   3   2
BioPharm │  1   4   1   1   2   1   1   1   1   1   1   2   1   -   4   1   1   2   2
HlthEquip│  1   2   1   1   3   1   1   1   1   1   1   3   1   4   -   1   1   2   1
Utilities│  4   1   2   3   2   1   2   1   1   1   1   2   1   1   1   -   2   3   3
Telecom  │  1   1   1   1   1   2   1   1   1   1   2   3   4   1   1   2   -   3   2
Financ   │  3   2   2   2   3   3   3   2   2   2   2   3   3   2   2   3   3   -   5
Sov&GSEs │  3   2   3   3   2   1   2   1   1   1   1   2   2   2   1   3   2   5   -
```

### 2.2 Cell Annotation Scheme

Each matrix cell can be enriched with five dimensions. For table readability, the grid above shows only the intensity score. Full annotations for scores >= 3 follow in Section 2.4.

**Contagion Type Code:**
- C = Credit Chain
- R = Regional Resonance
- L = Liquidity Squeeze
- S = Confidence Collapse
- - = No significant transmission path

**Confidence Level:**
- H = High — validated by historical cases
- M = Medium — logic-based with partial evidence
- L = Low — theoretical inference, no historical precedent

**Direction:**
- ↔ = Bidirectional transmission significant
- → = Unidirectional transmission
- - = No significant transmission

**Example:** `C+R(4,H,↔)` = Credit Chain + Regional Resonance, intensity 4, high confidence, bidirectional.

### 2.3 Downstream Consumption Rules

Each matrix cell output fields are consumed by upstream modules as follows:

| Field | Consumer | Purpose |
|---|---|---|
| `intensity` | Contagion SRI | Calculate contagion force coefficient, weight industry risk scores |
| `intensity` | Concentration Framework | Identify super-spreader industries and cluster risk |
| `direction` | Concentration Framework | Determine unidirectional vs bidirectional contagion, affects cluster partitioning |
| `confidence` | Current version not consumed | Reserved for future confidence-weighted aggregation |
| `historical_cases` | Current version not consumed | Reserved for backtesting and narrative explanation |

### 2.4 Full Annotated Matrix (Scores >= 3)

#### Row 1: Energy (Oil & Gas)

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 1→2 Chemicals | C+R | 5 | H | ↔ | 2014-2015 oil price crash → petrochemical margin compression (naphtha vs gas advantage shift); 2020 negative oil → chemical inventory losses |
| 1→3 Metals & Mining | C | 3 | M | → | Oil price volatility affects mining fuel costs; energy-linked metals (uranium, lithium brine costs) |
| 1→5 Capital Goods | C | 3 | M | → | 2015-2016 oil crash → oilfield service (OFS) capex collapse → equipment makers (SLB, HAL, BHI) revenue down 40-70% |
| 1→7 Transportation | C | 4 | H | ↔ | 2008 oil spike → airline fuel cost surge (30% of OpEx); 2020 oil price collapse benefited transport but signaled demand destruction |
| 1→8 Automobiles | C | 3 | M | → | 2008 oil price spike → shift to small cars hurt Detroit 3; 2011-2014 high oil boosted EV/ hybrid adoption narrative |
| 1→16 Utilities | C | 4 | H | ↔ | 2021-2022 European gas crisis → utility margin squeeze (Uniper, Fortum require bailout); coal/gas plant fuel cost pass-through |
| 1→18 Financials | C+S | 3 | M | ↔ | 2015-2016 energy loan losses (US E&P bank exposure $200bn+); 2008 oil price spike → sovereign wealth fund losses |
| 1→19 Sovereigns & GSEs | R | 3 | M | ↔ | 2014-2015 oil crash → Gulf sovereign wealth drawdowns; Venezuela/Ecuador fiscal collapse; Russia ruble crisis |

#### Row 2: Chemicals

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 2→1 Energy | C+R | 5 | H | ↔ | Feedstock price pass-through; 2014 naphtha vs ethane advantage shift; 2020 negative oil → chemical inventory losses |
| 2→4 Construction Materials | C | 3 | M | → | Specialty chemicals (admixtures, coatings) supply to construction; building chemical demand correlation |
| 2→8 Automobiles | C | 3 | M | → | Automotive coatings, plastics, battery chemicals supply; auto demand shock → chemical orders reduction |
| 2→9 Consumer Durables | C | 3 | M | → | Plastic resins, coatings for appliances and electronics; housing downturn → durables slowdown → chemical demand |
| 2→10 Consumer Staples | C | 4 | H | ↔ | 2022 fertilizer price spike (nutrien, CF, Yara) → food inflation; agricultural chemical supply chain (Syngenta, Bayer, Corteva) |
| 2→12 Technology Hardware | C | 3 | M | → | Semiconductor chemicals (photoresists, specialty gases) supply chain; chemical supply disruption → chip production slowdown |
| 2→14 Biotech & Pharma | C | 4 | H | ↔ | Pharma intermediates (Lonza, Catalent, DSM) supply active ingredients; 2022 supply chain disruption → generic drug shortages |

#### Row 3: Metals & Mining

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 3→1 Energy | C | 3 | M | ↔ | Mining energy cost dependence; coal/metallurgical coal price linkage; lithium/copper as "energy transition metals" |
| 3→4 Construction Materials | C | 4 | H | ↔ | Steel, aluminum, copper input to construction; 2008 construction collapse → steel price crash; 2022 infrastructure stimulus → metals demand |
| 3→5 Capital Goods | C | 4 | H | ↔ | Steel, aluminum, specialty alloys as capital goods inputs; 2008-2009 industrial collapse → metals price collapse |
| 3→19 Sovereigns & GSEs | R | 3 | M | ↔ | Resource-rich sovereign fiscal dependence on mining royalties (Chile copper, Australia iron ore, DRC cobalt) |

#### Row 4: Construction Materials

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 4→2 Chemicals | C | 3 | M | ↔ | Construction chemical inputs (admixtures, sealants, adhesives); cement chemical additive supply chain |
| 4→3 Metals & Mining | C | 4 | H | ↔ | Steel, aluminum, copper primary inputs to construction; construction PMI a leading indicator for metals demand |
| 4→5 Capital Goods | C | 3 | M | → | Construction equipment (Caterpillar, Komatsu) demand from building activity; infrastructure spending linkage |
| 4→16 Utilities | C+R | 3 | M | ↔ | Utility infrastructure construction (transmission, pipelines, renewables) as demand driver; regulatory approval linkage |
| 4→19 Sovereigns & GSEs | R | 3 | M | ↔ | Infrastructure spending is a primary demand driver for construction materials; fiscal policy → construction cycle |

#### Row 5: Capital Goods

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 5→3 Metals & Mining | C | 4 | H | ↔ | Mining equipment demand pull; 2010-2014 mining capex super-cycle → equipment maker revenue boom |
| 5→4 Construction Materials | C | 3 | M | ↔ | Construction equipment demand (excavators, cranes) tied to infra/build cycle |
| 5→7 Transportation | C | 3 | M | → | Rail equipment, aircraft manufacturing, shipbuilding; transportation industry capital expenditure cycle |
| 5→8 Automobiles | C | 3 | M | → | Industrial robots and automation equipment for auto manufacturing; 2019 auto capex slowdown → equipment orders decline |
| 5→12 Technology Hardware | C | 4 | H | ↔ | Semiconductor manufacturing equipment (ASML, AMAT, TEL, LAM) is the most critical capital goods segment; chip cycle drives equipment orders |
| 5→15 Healthcare Equipment | C | 3 | M | → | Medical device manufacturing equipment; precision engineering supply chain |
| 5→18 Financials | C+S | 3 | M | ↔ | Capital goods leveraged to industrial loan books and project finance; trade finance interdependence |

#### Row 6: Commercial Services

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 6→7 Transportation | C | 3 | M | ↔ | Logistics and freight brokerage services integration; 2020 COVID → both services and transportation demand collapsed |
| 6→11 Retail | C+S | 3 | M | ↔ | B2B services to retail (facility management, staffing, payment processing); retail downturn → services demand reduction |
| 6→13 Software & Services | C | 3 | M | ↔ | Professional services (Accenture, Infosys) and IT consulting to enterprise; commercial services digitization demand |
| 6→18 Financials | C | 3 | M | → | Commercial services dependent on SME lending, factoring, trade finance; financial sector tightening → services cash flow pressure |

#### Row 7: Transportation

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 7→1 Energy | C | 4 | H | ↔ | Transportation accounts for ~60% of global oil demand; 2020 COVID → transport fuel demand collapse → oil price crash |
| 7→6 Commercial Services | C | 3 | M | ↔ | Logistics/transportation as input to B2B services supply chain |
| 7→11 Retail | C | 4 | H | ↔ | Retail logistics backbone (trucking, last-mile, container shipping); 2021 supply chain crisis → retail inventory disruption |
| 7→18 Financials | C+S | 3 | M | ↔ | Transportation leveraged to asset-backed finance, aircraft/truck/ship leases; 2020 airline crisis → leasing company losses ($40bn+) |

#### Row 8: Automobiles

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 8→2 Chemicals | C | 3 | M | → | Automotive coatings, plastics, battery chemicals; EV transition reshaping chemical demand (lithium, cobalt, nickel) |
| 8→5 Capital Goods | C | 3 | M | → | Auto manufacturing equipment, industrial robots; 2019-2020 auto downturn → robotics orders decline |
| 8→9 Consumer Durables | S | 3 | M | ↔ | Shared "big-ticket consumer spend" category; auto + durables both sensitive to consumer confidence and rates |
| 8→12 Technology Hardware | C | 4 | H | ↔ | Auto chip content (infotainment, ADAS, powertrain, EV) rising from $500 to $1,500+/vehicle; 2021 global chip shortage → auto production loss of $200bn+ |

#### Row 9: Consumer Durables

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 9→2 Chemicals | C | 3 | M | → | Plastics, coatings, synthetic materials in durable goods production |
| 9→8 Automobiles | S | 3 | M | ↔ | Shared consumer confidence exposure; recession impact on big-ticket purchases |
| 9→11 Retail | C | 3 | M | ↔ | Durable goods sold through retail channels; 2020-2021 home improvement boom → appliance retailer surge |
| 9→12 Technology Hardware | C | 3 | M | → | Smart home devices, IoT appliances; durable goods incorporating semis and connectivity |

#### Row 10: Consumer Staples

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 10→2 Chemicals | C | 4 | H | ↔ | Agrochemicals supply to food production; 2022 fertilizer crisis → food inflation spike |
| 10→11 Retail | C+S | 3 | M | ↔ | CPG brands sold through retail channels; private label vs brand dynamics; 2022 inflation → consumer staple price sensitivity |

#### Row 11: Retail

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 11→6 Commercial Services | C | 3 | M | ↔ | Retail demands B2B services (logistics, payments, staffing); retail downturn → services revenue decline |
| 11→7 Transportation | C | 4 | H | ↔ | E-commerce-driven demand for logistics; 2021 holiday season shipping capacity crisis; retail inventory cycles drive freight demand |
| 11→9 Consumer Durables | C+S | 3 | M | ↔ | Retail channel performance directly affects consumer durables manufacturers; retail bankruptcy (Sears, Toys R Us) → supplier losses |
| 11→10 Consumer Staples | C+S | 3 | M | ↔ | Retail distribution is essential for CPG reach; private label competition; 2020 panic buying → shelf stockout — retail-CPG coordination pressure |
| 11→13 Software & Services | C+S | 3 | M | ↔ | E-commerce platform software (Shopify, BigCommerce); retail technology spending; 2022 online sales normalization → SaaS downgrades |

#### Row 12: Technology Hardware (Semiconductors)

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 12→2 Chemicals | C | 3 | M | ↔ | Semiconductor-grade chemicals (photoresists, gases) supply chain; 2021 Texas freeze → chemical plant outage → chip shortage |
| 12→5 Capital Goods | C | 4 | H | ↔ | Semiconductor equipment is the most critical capital goods segment; 2023 AI-driven HBM demand → equipment order boom |
| 12→8 Automobiles | C | 4 | H | ↔ | Auto chip content rising; 2021 global chip shortage caused $200bn+ auto production loss |
| 12→9 Consumer Durables | C | 3 | M | → | Smart home, IoT, appliance chip content; durable goods incorporating semiconductor components |
| 12→13 Software & Services | C+S | 4 | H | ↔ | Cloud computing, AI infrastructure dependent on GPU/CPU supply; 2023 NVIDIA GPU shortage → cloud service capacity constraint |
| 12→15 Healthcare Equipment | C | 3 | M | → | Medical device chip content (CT, MRI, monitoring); 2021 chip shortage → medical equipment delivery delays |
| 12→17 Telecommunications | C | 3 | M | ↔ | Network infrastructure chips (5G, optical, baseband); telecom capex cycle drives semiconductor demand |
| 12→18 Financials | C+S | 3 | M | ↔ | Semis are large market-cap sector with significant institutional ownership; sector-wide selloffs (2018, 2022) affect portfolio values |

#### Row 13: Software & Services

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 13→6 Commercial Services | C | 3 | M | ↔ | Enterprise SaaS replacing traditional B2B services; disruption risk for legacy service providers |
| 13→11 Retail | C+S | 3 | M | ↔ | E-commerce platform dependence; 2022 e-commerce normalization → Shopify/Salesforce retail-facing software demand slowdown |
| 13→12 Technology Hardware | C+S | 4 | H | ↔ | Cloud and AI software driving hardware demand; 2023 AI revolution → GPU demand surge; software ecosystem lock-in to specific hardware |
| 13→17 Telecommunications | C+S | 4 | H | ↔ | Cloud infrastructure converging with telecom; 5G core network software; Verizon/AT&T cloud migration → IT services demand |
| 13→18 Financials | C+S | 3 | M | ↔ | Fintech disrupting traditional banking; financial software (FIS, Fiserv, SS&C) exposure to bank consolidation and tech spending cycles |

#### Row 14: Biotech & Pharma

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 14→2 Chemicals | C | 4 | H | ↔ | Pharma intermediates and CDMO supply chain (Lonza, Catalent, WuXi); 2022 supply chain disruption → generic drug shortages |
| 14→15 Healthcare Equipment | C+S | 4 | H | ↔ | Integrated healthcare sector; 2023 GLP-1 drug success → weight loss device/equipment re-assessment; joint hospital purchasing |
| 14→18 Financials | C+S | 2 | M | → | Biotech venture capital / IPO funding cycles; 2022 biotech bear market → sector IPO freeze |

#### Row 15: Healthcare Equipment

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 15→5 Capital Goods | C | 3 | M | ↔ | Medical device manufacturing equipment; precision engineering and supply chain integration |
| 15→12 Technology Hardware | C | 3 | M | ↔ | Medical device chip content; 2021 chip shortage → CT/MRI delivery delays; Medtronic, Siemens Healthineers chip supply chain |
| 15→14 Biotech & Pharma | C+S | 4 | H | ↔ | 2023 medical device + pharma regulatory convergence; hospital group procurement bundling; shared FDA/EMA regulatory exposure |

#### Row 16: Utilities (Regulated)

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 16→1 Energy | C | 4 | H | ↔ | Fuel input cost (gas, coal, nuclear) pass-through but timing lag; 2021-2022 European gas crisis → utility margin squeeze |
| 16→4 Construction Materials | C+R | 3 | M | ↔ | Utility infrastructure construction demand (transmission, renewables); regulated asset base growth dependent on construction |
| 16→18 Financials | C+R | 3 | M | ↔ | Utility project finance debt; regulated utility as infrastructure investment vehicle; interest rate sensitivity → utility valuation and financing |
| 16→19 Sovereigns & GSEs | R | 3 | M | ↔ | Regulated utilities often government-owned (EDF, Enel, KEPCO); sovereign credit directly impacts utility funding costs |

#### Row 17: Telecommunications

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 17→11 Retail | C | 2 | M | ↔ | Telecom retail distribution; mobile virtual network operator (MVNO) relationships |
| 17→13 Software & Services | C+S | 4 | H | ↔ | Cloud computing and telecom convergence; AWS/Azure/GCP network dependency; software-defined networking displacing legacy telecom |
| 17→18 Financials | C | 3 | M | ↔ | Telecom infrastructure financing (tower companies, fiber networks); large telecom debt issuance absorbed by banks/insurance |

#### Row 18: Financials (Banks/Insurance)

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 18→1 Energy | C+S | 3 | M | ↔ | Energy loan book (US bank E&P exposure $200bn+ in 2015); project finance for oil & gas |
| 18→5 Capital Goods | C | 3 | M | ↔ | Industrial and equipment finance; trade credit insurance; supply chain finance |
| 18→6 Commercial Services | C | 3 | M | ↔ | SME lending; factoring; commercial mortgages for service sector properties |
| 18→7 Transportation | C+S | 3 | M | ↔ | Transportation asset finance (aircraft, ships, railcars); 2020 airline crisis → aircraft lessor/ bank exposure |
| 18→12 Technology Hardware | C+S | 3 | M | ↔ | Tech lending (SVB model focused on tech/VC); 2023 SVB failure specifically tied to tech sector concentration |
| 18→13 Software & Services | C+S | 3 | M | ↔ | Software company debt and deposit concentration; SVB 2023: large uninsured deposits from VC-backed tech firms |
| 18→16 Utilities | C+R | 3 | M | ↔ | Utility project finance and infrastructure debt |
| 18→17 Telecommunications | C | 3 | M | ↔ | Telco infrastructure loans, tower REIT, spectrum financing |
| 18→19 Sovereigns & GSEs | R+L+S | 5 | H | ↔ | The sovereign-bank nexus: banks hold government bonds, government guarantees banks; 2008 GFC → sovereign rescues; 2011 Eurozone → bank-sovereign doom loop; 2023 Credit Suisse → government backstop |

#### Row 19: Sovereigns & GSEs

| Receptor | Type | Intensity | Confidence | Direction | Historical Precedent |
|---|---|---|---|---|---|
| 19→1 Energy | R | 3 | M | ↔ | Sovereign fiscal dependence on oil revenue; OPEC+ policy coordination; resource-backed loans |
| 19→3 Metals & Mining | R | 3 | M | ↔ | Mining royalties and sovereign exposure; Chile copper, DRC cobalt, Australia iron ore fiscal dependence |
| 19→4 Construction Materials | R | 3 | M | ↔ | Sovereign infrastructure spending drives construction materials demand; fiscal stimulus → construction activity |
| 19→16 Utilities | R | 3 | M | ↔ | State-owned utilities (EDF, Enel, KEPCO, CEPALCO); sovereign credit directly affects utility funding and tariff policy |
| 19→18 Financials | R+L+S | 5 | H | ↔ | The sovereign-bank nexus in full force: sovereign default → bank balance sheet destruction → credit contraction; 2011-2012 Eurozone crisis is the definitive case |

---

## 3. Contagion Pathways and Graph Representation

### 3.1 High-Intensity Links (Score >= 4)

The following links form the structural backbone of the global industry contagion network:

```
Score 5 (Very Strong):
  Energy (1)       ↔    Chemicals (2)                  (C+R, H)
  Financials (18)  ↔    Sovereigns & GSEs (19)           (R+L+S, H)

Score 4 (Strong):
  Energy (1)       ↔    Transportation (7)               (C, H)
  Energy (1)       ↔    Utilities (16)                   (C, H)
  Chemicals (2)    →    Consumer Staples (10)             (C, H)
  Chemicals (2)    →    Biotech & Pharma (14)             (C, H)
  Metals & Mining (3) ↔  Construction Materials (4)       (C, H)
  Metals & Mining (3) ↔  Capital Goods (5)                (C, H)
  Capital Goods (5) ↔    Technology Hardware (12)         (C, H)
  Transportation (7) ↔   Retail (11)                      (C, H)
  Automobiles (8)  ↔    Technology Hardware (12)          (C, H)
  Technology Hardware↔   Software & Services (13)         (C+S, H)
  Biotech & Pharma↔     Healthcare Equipment (15)         (C+S, H)
  Software & Services↔  Telecommunications (17)          (C+S, H)
  Sovereigns & GSEs↔    Financials (18)                   (R+L+S, H)
  Chemicals (2)    ↔    Technology Hardware (12)          (C, M)
  Capital Goods (5) ↔   Automobiles (8)                   (C, M)
  Technology Hardware↔  Healthcare Equipment (15)         (C, M)

Total: 17 high-intensity links (score >= 4), including 2 at score 5
```

### 3.2 Moderate-Intensity Links (Score = 3)

Score-3 links form the secondary transmission network. In total there are 62 unique moderate-intensity directed links connecting industries across all paradigms. Key clusters:

**P1 (Policy-Driven) Cluster:**
- Energy ↔ Financials, Energy ↔ Sovereigns
- Chemicals ↔ Automobiles, Chemicals ↔ Consumer Durables
- Financials ↔ Capital Goods, Financials ↔ Commercial Services
- Financials ↔ Transportation, Financials ↔ Tech Hardware, Financials ↔ Software
- Sovereigns ↔ Energy, Sovereigns ↔ Metals & Mining, Sovereigns ↔ Construction Materials, Sovereigns ↔ Utilities

**P2 (Technology Moat) Cluster:**
- Tech Hardware ↔ Capital Goods (also score 4), Tech Hardware ↔ Healthcare
- Software ↔ Commercial Services, Software ↔ Retail
- Biotech ↔ Financials, Healthcare Equipment ↔ Capital Goods
- Capital Goods ↔ Transportation, Capital Goods ↔ Healthcare Equipment

**P3 (Zero-Sum Game) Cluster:**
- Automobiles ↔ Chemicals, Automobiles ↔ Consumer Durables
- Metals & Mining ↔ Energy, Metals & Mining ↔ Construction Materials

**P4 (Asset Lease) Cluster:**
- Construction Materials ↔ Capital Goods, Construction Materials ↔ Utilities
- Transportation ↔ Capital Goods, Transportation ↔ Commercial Services
- Telecommunications ↔ Software & Services (also score 4), Telecom ↔ Financials
- Utilities ↔ Financials, Utilities ↔ Sovereigns

**P5 (Brand + Channel) Cluster:**
- Consumer Staples ↔ Retail, Consumer Durables ↔ Retail
- Consumer Durables ↔ Chemicals, Consumer Staples ↔ Chemicals
- Consumer Durables ↔ Technology Hardware

**P6 (Network + Traffic) Cluster:**
- Retail ↔ Commercial Services, Retail ↔ Software & Services
- Commercial Services ↔ Transportation, Commercial Services ↔ Software
- Commercial Services ↔ Financials

### 3.3 Low-Intensity Links (Score <= 2)

Score-2 or 1 links (222 out of 342 off-diagonal pairs, 64.9%) represent pairs with minimal or negligible direct contagion risk. Typical patterns:

1. **Cross-paradigm unrelated sectors**: e.g., Consumer Staples ↔ Technology Hardware (1); Metals & Mining ↔ Software (1)
2. **Purely financial channel without sector linkage**: e.g., Telecom ↔ Consumer Durables (1)
3. **Theoretical but unproven channels**: e.g., Biotech ↔ Transportation (1); Healthcare Equipment ↔ Retail (1)

### 3.4 Graph Centrality Summary

| Measure | Top 3 Industries | Interpretation |
|---|---|---|
| **Degree Centrality** | Tech Hardware (12), Financials (18), Energy (1) | Most connected — highest number of intensity >= 3 links |
| **Betweenness Centrality** | Financials (18), Technology Hardware (12), Chemicals (2) | Key bridges between otherwise disconnected sector clusters |
| **Closeness Centrality** | Financials (18), Energy (1), Technology Hardware (12) | Fastest transmission path to any other sector |
| **Eigenvector Centrality** | Financials (18), Sovereigns (19), Technology Hardware (12) | Connected to the most highly-connected sectors |

---

## 4. Matrix Construction Logic

### 4.1 Five Construction Principles

#### Principle 1: Shared Paradigm Elevates Coupling

Industries under the same analytical paradigm exhibit systematically higher contagion intensity due to shared risk factors:

| Paradigm | Example Pair | Intensity | Rationale |
|---|---|---|---|
| P1 (Policy-Driven) | Energy ↔ Sovereigns | 3 | Resource fiscal policy, geopolitical risk, regulatory cycle synchronization |
| P2 (Technology Moat) | Tech Hardware ↔ Software | 4 | Ecosystem lock-in (Apple, Wintel, ARM); AI/GPU dependency |
| P3 (Zero-Sum Game) | Automobiles ↔ Consumer Durables | 3 | Shared consumer discretionary spending; replacement cycle correlation |
| P4 (Asset Lease) | Transportation ↔ Utilities | 2 | Both are infrastructure-intensive but serve different end-markets |
| P5 (Brand + Channel) | Consumer Staples ↔ Consumer Durables | 2 | Share "consumer trust" attribute but fundamentally different demand drivers |
| P6 (Network + Traffic) | Retail ↔ Software & Services | 3 | E-commerce platform ecosystem; cloud → omnichannel integration |

#### Principle 2: Upstream-Downstream Supply Chain

Vertical supply chain relationships drive direct credit chain contagion:

| Upstream | Downstream | Intensity | Basis |
|---|---|---|---|
| Energy | Chemicals | 5 | Direct feedstock; ~60% of chemical production is petrochemical-based |
| Energy | Transportation | 4 | Fuel is ~25-30% of airline OpEx, ~20% of trucking |
| Energy | Utilities | 4 | Fuel (gas/coal) = ~40-60% of thermal generation cost |
| Chemicals | Consumer Staples | 4 | Fertilizer, food additives, packaging — essential inputs |
| Chemicals | Biotech & Pharma | 4 | Pharma intermediates are specialty chemicals |
| Metals & Mining | Construction Materials | 4 | Primary steel, aluminum, copper inputs |
| Metals & Mining | Capital Goods | 4 | Equipment manufacturing uses 25-30% of global steel |
| Technology Hardware | Automobiles | 4 | Chip content per vehicle rising exponentially |
| Technology Hardware | Software & Services | 4 | Cloud/AI hardware enables software ecosystem |
| Technology Hardware | Capital Goods | 4 | Semiconductor equipment is the highest-value capital goods segment |

#### Principle 3: Common Creditor / Financial Intermediation

Financials and Sovereigns serve as the "hub" sectors transmitting contagion across the real economy through credit channels:

| Path | Intensity | Mechanism |
|---|---|---|
| Financials → All sectors | 3 (avg) | Credit supply contraction affects all borrowers simultaneously |
| Sovereigns → Financials | 5 | Government bond holdings at banks; fiscal guarantee of banking system |
| Financials → Sovereigns | 5 | Bank bailout costs = sovereign contingent liability |

#### Principle 4: Consumer Confidence Resonance

Consumer-facing sectors share exposure to household confidence, disposable income trends, and spending cycles — but the transmission is primarily through Confidence Collapse (S) rather than Credit Chain (C):

| Path | Intensity | Mechanism |
|---|---|---|
| Consumer Staples ↔ Retail | 3 | CPG retail exposure; private label competition |
| Consumer Durables ↔ Retail | 3 | Durable goods retail distribution channel |
| Consumer Staples ↔ Consumer Durables | 2 | Weak — different spending categories, supply chains do not overlap |
| Consumer Durables ↔ Automobiles | 3 | Both share "big-ticket discretionary" category; interest rate sensitivity |

#### Principle 5: Higher Financial Intensity Amplifies Contagion Reach

Industries with higher financial intensity (larger debt markets, more leveraged balance sheets, higher institutional ownership) have broader contagion reach:

| Industry | Financial Intensity | Row Sum (Contagion Force) | Rank |
|---|---|---|---|
| Financials | Very High | 48 | 1 |
| Technology Hardware | High | 44 | 2 |
| Energy | High | 43 | 3 |
| Sovereigns & GSEs | Very High | 42 | 4 |
| Chemicals | Medium | 40 | 5 |
| Capital Goods | Medium-High | 39 | 6 |
| Transportation | High | 38 | 7 |
| Software & Services | Medium | 36 | 8 |
| Automobiles | High | 34 | 9 |
| Retail | Medium | 33 | 10 |
| Biotech & Pharma | Medium-High | 30 | 11 |
| Utilities | High | 30 | 12 |
| Metals & Mining | Medium | 29 | 13 |
| Healthcare Equipment | Medium | 28 | 14 |
| Construction Materials | Medium | 27 | 15 |
| Consumer Durables | Low-Medium | 27 | 16 |
| Telecommunications | High | 25 | 17 |
| Consumer Staples | Low | 25 | 18 |
| Commercial Services | Low-Medium | 24 | 19 |

### 4.2 Asymmetry Analysis

The matrix is not perfectly symmetric; key asymmetries include:

| Type | Example | Explanation |
|---|---|---|
| **Supply Chain Asymmetry** | Energy → Transportation (4) vs Transportation → Energy (4) | Symmetric: fuel cost impact on transportation (input) AND transport demand impact on energy (output) are both strong |
| **Vertical Asymmetry** | Chemicals → Consumer Staples (4) vs Consumer Staples → Chemicals (1) | Chemicals are upstream input for CPG, but CPG demand has limited reverse impact on chemical production |
| **Financial Hub Asymmetry** | Sovereigns → Financials (5) vs Financials → Sovereigns (5) | Symmetric in the sovereign-bank nexus: the doom loop is bidirectional |
| **Scale/Concentration Asymmetry** | Financials → All (3 avg) vs Individual sector → Financials (1-3) | Financials have broad diversified exposure to all sectors; individual sector stress has limited impact on diversified bank portfolios |

### 4.3 Channels Not Exhaustively Captured

1. **Multi-step cascade**: The matrix captures direct (A→B) transmission only. Second-order (A→B→C) cascades — e.g., Energy default → Chemical producer slowdown → Consumer Staples packaging shortage — require multi-step simulation beyond the pairwise matrix
2. **Common ownership / institutional investor overlap**: Two sectors with no direct economic linkage can co-move if owned by the same leveraged investor base (e.g., cross-sector ETF rebalancing)
3. **Geopolitical event-driven correlation**: A single geopolitical event (sanctions, trade war, conflict) can simultaneously affect multiple paradigm-unrelated sectors (e.g., Russia-Ukraine 2022 simultaneously hit Energy, Chemicals, Agriculture/Consumer Staples, and Metals & Mining)
4. **Liquidity-driven path**: In extreme stress, liquidity squeeze can transmit between any pair regardless of economic linkage — the matrix does not attribute score-5 liquidity contagion to all cells, but users should be aware of this limitation (see Section 6 for stress escalation)

---

## 5. Derived Metrics — Super-Spreaders, Vulnerability, and Coefficients

### 5.1 Super-Spreader Industries (Top 3 Row Sums)

Super-spreaders are industries whose default or distress causes the widest contagion to other sectors. Measured by **row sum** (total outgoing contagion intensity).

| Rank | Industry | Row Sum | Key Targets (Score >= 3) | Core Logic |
|---|---|---|---|---|
| **1** | **Financials (Banks/Insurance)** | **48** | Sovereigns(5), TechHW(3), Software(3), Energy(3), Transport(3), CapGoods(3), ComServ(3), Utilities(3), Telecom(3), Chemicals(2) | Central credit intermediary; credit supply contraction affects all sectors; sovereign-bank nexus is the highest-intensity link in the matrix |
| **2** | **Technology Hardware (Semis)** | **44** | Software(4), Automobiles(4), CapGoods(4), Chemicals(3), Healthcare(3), Consumer Durables(3), Telecom(3), Financials(3) | "Industrial rice" — chips are essential inputs to virtually all manufacturing and technology sectors |
| **3** | **Energy (Oil & Gas)** | **43** | Chemicals(5), Transportation(4), Utilities(4), Automobiles(3), CapGoods(3), Metals(3), Financials(3), Sovereigns(3) | Primary commodity with economy-wide cost impact; petrochemical feedstock; fuel for transport and power generation |

**Note:** Sovereigns & GSEs rank 4th (row sum 42), just outside top 3.

### 5.2 Vulnerable Industries (Top 3 Column Sums)

Vulnerable industries are those most exposed to incoming contagion from other sectors. Measured by **column sum** (total incoming contagion exposure).

| Rank | Industry | Column Sum | Key Sources (Score >= 3) | Core Logic |
|---|---|---|---|---|
| **1** | **Financials (Banks/Insurance)** | **48** | Sovereigns(5), Energy(3), CapGoods(3), ComServ(3), Transport(3), TechHW(3), Software(3), Utilities(3), Telecom(3) | The most "central" node: exposed to every sector through loan books, investment portfolios, and derivative counterparty risk |
| **2** | **Energy (Oil & Gas)** | **43** | Chemicals(5), Transport(4), Utilities(4), Capital Goods(3), Automobiles(3), TechHW(3), Financials(3), Sovereigns(3) | Dual vulnerability: input cost side (chemicals → energy) and demand side (transport, utilities, industrial) |
| **3** | **Technology Hardware (Semis)** | **44** | CapGoods(4), Software(4), Automobiles(4), Chemicals(3), Healthcare(3), Retail(3), Telecom(3), Financials(3) | Technology hardware is simultaneously a super-spreader AND a highly vulnerable industry — a "central hub" property with dual risk |

**Key finding:** Technology Hardware (Semis) is simultaneously the #2 super-spreader (row sum 44) and #3 vulnerable industry (column sum 44). This "central node" property means semiconductor sector credit events may trigger **systemic contagion** not limited to local pathways.

### 5.3 Contagion Coefficients

#### Contagion Force Coefficient (CFC)

Measures the relative contagion transmission capacity of each industry:

```
CFC_i = Row_Sum_i / Max(Row_Sum)
```

| Rank | Industry | Row Sum | CFC |
|---|---|---|---|
| 1 | Financials | 48 | 1.00 |
| 2 | Technology Hardware | 44 | 0.92 |
| 3 | Energy | 43 | 0.90 |
| 4 | Sovereigns & GSEs | 42 | 0.88 |
| 5 | Chemicals | 40 | 0.83 |
| 6 | Capital Goods | 39 | 0.81 |
| 7 | Transportation | 38 | 0.79 |
| 8 | Software & Services | 36 | 0.75 |
| 9 | Automobiles | 34 | 0.71 |
| 10 | Retail | 33 | 0.69 |
| 11 | Biotech & Pharma | 30 | 0.63 |
| 12 | Utilities | 30 | 0.63 |
| 13 | Metals & Mining | 29 | 0.60 |
| 14 | Healthcare Equipment | 28 | 0.58 |
| 15 | Consumer Durables | 27 | 0.56 |
| 16 | Construction Materials | 27 | 0.56 |
| 17 | Telecommunications | 25 | 0.52 |
| 18 | Consumer Staples | 25 | 0.52 |
| 19 | Commercial Services | 24 | 0.50 |

#### Contagion Vulnerability Coefficient (CVC)

Measures the relative contagion reception vulnerability of each industry:

```
CVC_i = Col_Sum_i / Max(Col_Sum)
```

| Rank | Industry | Col Sum | CVC |
|---|---|---|---|
| 1 | Financials | 48 | 1.00 |
| 2 | Technology Hardware | 44 | 0.92 |
| 3 | Energy | 43 | 0.90 |
| 4 | Sovereigns & GSEs | 42 | 0.88 |
| 5 | Chemicals | 40 | 0.83 |
| 6 | Capital Goods | 39 | 0.81 |
| 7 | Transportation | 38 | 0.79 |
| 8 | Software & Services | 36 | 0.75 |
| 9 | Automobiles | 34 | 0.71 |
| 10 | Retail | 33 | 0.69 |
| 11 | Biotech & Pharma | 30 | 0.63 |
| 12 | Utilities | 30 | 0.63 |
| 13 | Metals & Mining | 29 | 0.60 |
| 14 | Healthcare Equipment | 28 | 0.58 |
| 15 | Consumer Durables | 27 | 0.56 |
| 16 | Construction Materials | 27 | 0.56 |
| 17 | Telecommunications | 25 | 0.52 |
| 18 | Consumer Staples | 25 | 0.52 |
| 19 | Commercial Services | 24 | 0.50 |

#### Contagion Net Exposure Ratio (CNER)

```
CNER_i = Row_Sum_i / Col_Sum_i
```

| Industry | Row Sum | Col Sum | CNER | Interpretation |
|---|---|---|---|---|
| Commercial Services | 24 | 24 | 1.00 | Balanced |
| Telecommunications | 25 | 25 | 1.00 | Balanced |
| Metals & Mining | 29 | 29 | 1.00 | Balanced |
| Construction Materials | 27 | 27 | 1.00 | Balanced |
| Technology Hardware | 44 | 44 | 1.00 | Balanced (central hub) |
| Energy | 43 | 43 | 1.00 | Balanced |
| Financials | 48 | 48 | 1.00 | Balanced (central hub) |
| Consumer Durables | 27 | 27 | 1.00 | Balanced |
| Consumer Staples | 25 | 25 | 1.00 | Balanced |
| Healthcare Equipment | 28 | 28 | 1.00 | Balanced |
| Capital Goods | 39 | 39 | 1.00 | Balanced |
| Chemicals | 40 | 40 | 1.00 | Balanced |
| Utilities | 30 | 30 | 1.00 | Balanced |
| Transportation | 38 | 38 | 1.00 | Balanced |
| Retail | 33 | 33 | 1.00 | Balanced |
| Automobiles | 34 | 34 | 1.00 | Balanced |
| Software & Services | 36 | 36 | 1.00 | Balanced |
| Biotech & Pharma | 30 | 30 | 1.00 | Balanced |
| Sovereigns & GSEs | 42 | 42 | 1.00 | Balanced |

**Note on symmetry:** The CNER for all industries is 1.00 because the matrix is structurally symmetric (each off-diagonal pair is assigned the same intensity in both directions). This reflects the design principle that the matrix captures linkage **existence** and **magnitude** rather than unidirectional flow. Directional asymmetries (e.g., upstream → downstream) are captured in the detailed annotations (Section 2.4) and in practical application (Section 6 stress scenario design), but the base matrix is symmetric. Future calibrated versions may introduce asymmetry coefficients based on empirical directional default correlation data.

### 5.4 Industry Clustering

#### High-Contagion Cluster (Intra-cluster average intensity >= 3.0)

| Cluster | Industries | Core Links | Dominant Contagion Type |
|---|---|---|---|
| **A: Energy-Chemicals-Transport-Utilities** | Energy, Chemicals, Transportation, Utilities | Energy↔Chemicals(5), Energy↔Transport(4), Energy↔Utilities(4), Chemicals↔Transport(2) | Credit Chain |
| **B: Tech-Auto-Capital Goods** | Technology Hardware, Software & Services, Automobiles, Capital Goods | Tech HW↔Software(4), Tech HW↔Autos(4), Cap Goods↔Tech HW(4), Cap Goods↔Autos(3) | Credit Chain + Confidence Collapse |
| **C: Sovereign-Financial Hub** | Sovereigns & GSEs, Financials | Sovereigns↔Financials(5) | All types (each contaminated through the nexus) |
| **D: Bio-Healthcare** | Biotech & Pharma, Healthcare Equipment | Biotech↔Healthcare Equip(4), Chemicals↔Biotech(4) | Credit Chain + Confidence Collapse |

#### Moderate-Contagion Cluster (Intra-cluster average intensity 2.0-2.9)

| Cluster | Industries | Key Links |
|---|---|---|
| **E: Retail-Consumer-Logistics** | Retail, Consumer Staples, Consumer Durables, Transportation | Retail↔Transport(4), Retail↔Consumer Staples(3), Retail↔Consumer Durables(3), Consumer Staples↔Chemicals(4) |
| **F: Infrastructure-Construction** | Construction Materials, Metals & Mining, Capital Goods, Utilities | Metals↔Const Mat(4), Metals↔Cap Goods(4), Const Mat↔Utilities(3) |
| **G: Telecom-Software** | Telecommunications, Software & Services | Telecom↔Software(4) |
| **H: Commercial Services-Network** | Commercial Services, Retail, Transportation, Software | ComServ↔Retail(3), ComServ↔Transport(3), ComServ↔Software(3) |

---

## 6. Stress Escalation — Factor-Specific Intensity Jumps

### 6.1 Escalation Factor Mapping

Based on the five escalation factors defined in [Contagion Theory](contagion-theory.md) Section 5, each factor affects specific matrix linkages:

| Escalation Factor | Applicable Contagion Types | Most Affected Industry Pairs | Max Jump |
|---|---|---|---|
| **Market Panic** | Confidence Collapse (S), Liquidity Squeeze (L) | All pairs with "S" or "L" annotation; especially Financials ↔ All, Tech HW ↔ Software | +1 ~ +2 |
| **Regulatory Vacuum** | Regional Resonance (R), Confidence Collapse (S) | Sovereigns & GSEs → Financials; Sovereigns → Utilities; Financials → All | +1 ~ +3 |
| **High Leverage** | Liquidity Squeeze (L) | Financials → All (especially Capital Goods, Technology Hardware, Real Estate proxy pairs) | +1 ~ +2 |
| **Information Asymmetry** | Confidence Collapse (S), Credit Chain (C) | All pairs including Technology Hardware, Biotech, and other R&D-intensive/opaque sectors | +1 |
| **Year-End Effect** | All types | All pairs (systemic but moderate effect) | +0 ~ +1 |

### 6.2 Factor-Specific Jump Tables

#### Jump Rule 1: Market Panic Trigger

**Trigger condition:** VIX > 20 (elevated state) or credit spread widening > 50bp or primary market cancellation rate > 20%

| Affected Pair | Base Intensity | Panic Intensity | Jump Logic |
|---|---|---|---|
| Financials → Sovereigns | 5 | 5 | Already at ceiling; transmission speed multiplies |
| Technology Hardware → Software | 4 | 5 | Panic amplifies tech ecosystem de-rating; forced ETF selling |
| Technology Hardware → Automobiles | 4 | 5 | Chip supply panic + demand pessimism amplify auto sector risk |
| Energy → Chemicals | 5 | 5 | Already at ceiling; contagion speed increases |
| Financials → All real economy | 3 (avg) | 4 (avg) | Broad credit supply contraction accelerates |
| All pairs with "S" mark | Base | Base + 1 | Confidence collapse becomes self-fulfilling in panic |
| All pairs with "L" mark | Base | Base + 1 | Liquidity squeeze accelerates in panic environment |
| Consumer Staples ↔ Retail | 3 | 4 | Consumption panic → indiscriminate consumer sector selling |

#### Jump Rule 2: Regulatory Vacuum Trigger

**Trigger condition:** 72 hours post-default with no clear regulatory stance, or ambiguous / "market solution" language

| Affected Pair | Base Intensity | Regulatory Vacuum Intensity | Jump Logic |
|---|---|---|---|
| Sovereigns → Financials | 5 | 5 | Already at ceiling; sovereign default risk becomes unanchored |
| Financials → Sovereigns | 5 | 5 | Same; bank bailout expectations lose anchor |
| Sovereigns → Utilities | 3 | 4 | State-owned utility credit re-pricing |
| Sovereigns → Energy | 3 | 4 | Resource-backed fiscal risk re-pricing |
| Sovereigns → Metals & Mining | 3 | 4 | Mining royalty / nationalization risk rises |
| Financials → All | 3 (avg) | 4 (avg) | Banking sector re-pricing flows to all borrowers |
| Sovereigns → Construction Materials | 3 | 4 | Infrastructure spending uncertainty |

#### Jump Rule 3: High Leverage Trigger

**Trigger condition:** Repo outstanding > 90th percentile of historical level, or hedge fund net leverage > 110% of baseline

| Affected Pair | Base Intensity | High Leverage Intensity | Jump Logic |
|---|---|---|---|
| Financials → Technology Hardware | 3 | 4 | Tech sector has high institutional leverage exposure |
| Financials → Software & Services | 3 | 4 | SaaS/subscription finance leverage = forced liquidation risk |
| Financials → Capital Goods | 3 | 4 | Capital goods project finance leveraged |
| Financials → All (broad) | 3 (avg) | 3.5 (avg) | Systematic forced deleveraging across sectors |
| All pairs with "L" mark | Base | Base + 1 | Liquidity-induced forced selling propagates regardless of sector logic |

#### Jump Rule 4: Information Asymmetry Trigger

**Trigger condition:** Defaulted entity does not publish filings within 24 hours, or management goes missing, or key financial data previously unavailable

| Affected Pair | Base Intensity | Info Asymmetry Intensity | Jump Logic |
|---|---|---|---|
| All pairs with "C" (Credit Chain) mark | Base | Base + 1 | Market fills supply chain exposure gaps with worst-case assumptions |
| Technology Hardware → All | Base | Base + 1 | Tech sector supply chains are opaque; chip inventory data not public |
| Biotech & Pharma → All | Base | Base + 1 | Pipeline data opacity; CDMO supply chain unobservable |
| Financials → All | Base | Base + 1 | Counterparty derivative exposure is a "black box" in crisis |
| All pairs with "R" (Regional Resonance) mark | Base | Base + 1 | Unobservable regional exposure → blanket de-risking |

#### Jump Rule 5: Year-End Effect Trigger

**Trigger condition:** Within 2 weeks of quarter-end or 4 weeks of calendar year-end

| Affected Pair | Base Intensity | Year-End Intensity | Jump Logic |
|---|---|---|---|
| All matrix pairs | Base | Base + 0 ~ +1 | Systematic risk appetite decline; credit events overreacted |
| Financials → All | Base | Base + 1 | Bank balance sheet window-dressing; new credit origination slows |

### 6.3 Synergy Effects (Multi-Factor Escalation)

When multiple escalation factors trigger simultaneously, intensity amplification follows **multiplicative stacking** rather than additive:

| Factor Combination | Synergy Multiplier | Hardest-Hit Pairs | Example Calculation |
|---|---|---|---|
| Market Panic + Regulatory Vacuum | 1.5x | Sovereigns → Financials, Financials → All | Base 3 → +1 (Panic) → 4 → +1x1.5 (Vacuum) → 5 (capped) |
| Market Panic + High Leverage | 2.0x | Financials → Technology Hardware, Financials → Software | Base 3 → +1 (Panic) → 4 → +2 (Leverage) → 6 → capped at 5 |
| Regulatory Vacuum + Year-End | 1.5x | Sovereigns → Financials, Sovereigns → Utilities | Base 3 → +1 (Vacuum) → 4 → +1x1.5 (Year-End) → 5 |
| Three or more simultaneously | 3.0x | All matrix pairs | Systemic crisis threshold: most base-3 pairs jump to 4-5 |

**Synergy ceiling:** Regardless of the number of simultaneous escalation factors, no individual cell can exceed the maximum intensity of 5.

### 6.4 Factor Trigger Probability and Monitoring

| Factor | Annual Trigger Prob. | Primary Season | Core Monitoring Indicators | Warning Threshold |
|---|---|---|---|---|
| Market Panic | 15-20% | Mar, Aug, Nov | VIX/VSTOXX, CDX/iTraxx spreads, primary cancellation rate | VIX > 35, IG spreads > 200bp |
| Regulatory Vacuum | 5-10% | Post-major-default, year-end | Central bank/treasury statements, financial stability reports | 48 hours with no formal statement post-default |
| High Leverage | 20-30% | Post-easing cycles | Repo outstanding, prime broker leverage surveys, margin debt | Repo volume > 90th percentile |
| Information Asymmetry | 10-15% | Post-sudden default | Filing timeliness, audit opinion, management accessibility | 24 hours post-default with no filing |
| Year-End Effect | 100% (periodic) | Mar/Jun/Sep quarter-ends, Dec | Calendar date, interbank rates (LIBOR/OIS), repo specials | Within 2 weeks of quarter-end |

---

## 7. Integration with Engine Components

### 7.1 Analysis Pyramid Integration

The contagion matrix is consumed across the four-layer analysis pyramid:

#### M1 (Industry Fundamentals)

| Layer Component | Integration Method | Operation |
|---|---|---|
| Industry Boundary Definition | Add **contagion exposure node** to industry ecosystem map | Each industry analysis must annotate contagion coupling strength to upstream/downstream industries |
| Industry Supply/Demand | Incorporate **downstream credit risk transmission** in demand drivers | High-debt downstream sector demand fluctuation → contagion mechanism to own industry |
| Industry Policy Analysis | Add **policy co-frequency contagion** to policy sensitivity assessment | Sectors sharing policy drivers (e.g., Energy+Chemicals under environmental regulation) must be co-analyzed |

#### M2 (Individual Credit Analysis)

| Layer Component | Integration Method | Operation |
|---|---|---|
| Supply Chain Analysis | Reference matrix in customer/supplier concentration check | If customer industry is high-contagion (e.g., Technology Hardware), focus assessment |
| Funding Channel Analysis | Check if entity's funding channel overlaps with vulnerable industries | e.g., entity relying on the same bank syndicate as counterparty in high-contagion pair |
| Regional Analysis | Reference Sovereigns & GSEs row for regional contagion factors | Entity's region has sovereign default history → regional resonance assessment |

#### M3 (Industry Comparison and Ranking)

| Layer Component | Integration Method | Operation |
|---|---|---|
| Industry Priority Ranking | Add **contagion risk adjustment factor** to ranking weights | High-contagion cluster industries (A/B/C/D) receive additional risk deduction in cross-industry comparison |
| Industry Rotation Analysis | Add **contagion trigger thresholds** to rotation logic | Monitor whether high-intensity matrix links show escalation signals |

#### M4 (Portfolio Risk Management)

| Layer Component | Integration Method | Operation |
|---|---|---|
| Concentration Stress Testing | Run **portfolio contagion simulation** via matrix (see 7.2) | Input hypothetical default → matrix-driven propagation → output portfolio impact |
| Industry Concentration Limits | Add **contagion-linked concentration** to limits management | Not only single-industry concentration but Cluster A+B+C+D total exposure cap |
| Limit Management System | Add **contagion path limits** triggered by SRI thresholds | Additional limit deductions on high-contagion industry pairs |
| Systemic Risk Monitoring | Reference [Systemic Warning Framework](systemic-warning-framework.md) SRI thermometer | M4 portfolio dashboard with SRI reading driving dynamic limit adjustment |

### 7.2 M4 Concentration Stress Test Process

The core application of the contagion matrix: **concentration-driven contagion stress testing** under the M4 portfolio framework.

```
Step 1: Set Stress Scenario
  ├── Select 1-3 trigger industries for hypothetical default (e.g., Financials + Energy)
  └── Select escalation factor combination (e.g., Market Panic + Year-End)

Step 2: Load Contagion Matrix
  ├── Read 19x19 matrix baseline intensities
  ├── Apply escalation jumps per Section 6 rules
  └── Generate "stressed matrix"

Step 3: Calculate Portfolio Contagion Exposure
  ├── Tag each holding with its 19-industry classification
  ├── Compute contagion paths from trigger industries to portfolio holdings
  └── Output "Portfolio Contagion Impact Score"

Step 4: Assess Concentration Breaches
  ├── Single industry concentration > threshold (e.g., 15%) → warning
  ├── Cluster A+B+C total exposure > threshold (e.g., 30%) → high warning
  └── Exposure to super-spreader industries (Financials / Tech HW / Energy) > single threshold → constraint

Step 5: Output Stress Test Report
  ├── Worst-case portfolio contagion loss estimate
  ├── High-contagion link exposure matrix (which industry pairs co-exist in portfolio)
  ├── Recommendation: reduce weak-credit holdings in high-contagion clusters or add hedges
  └── Recommendation: set additional exposure caps for super-spreader industries
```

**Example: Technology Hardware Default Stress Test**

```
Scenario: Major semiconductor manufacturer default
Active escalation: Market Panic (VIX > 35) + High Leverage

Stressed matrix affected paths:
  Tech HW → Software:       4 → 5 (Market Panic jump)
  Tech HW → Automobiles:    4 → 5 (Market Panic jump)
  Tech HW → Capital Goods:  4 → 5 (Market Panic jump)
  Tech HW → Healthcare Eq:  3 → 4 (Market Panic jump)
  Tech HW → Telecom:        3 → 4 (Market Panic + Leverage)
  Tech HW → Consumer Dur:   3 → 4 (Market Panic jump)
  Tech HW → Financials:     3 → 4 (Market Panic + Leverage)

Portfolio Impact:
  If portfolio holds Tech HW + Software + Automobiles + Capital Goods
  → Total cluster exposure must be < 25% threshold
  → Recommend treating these four industries as "one contagion cluster"
```

### 7.3 Industry Methodology "Contagion Exposure" Section Template

Each industry methodology document should include a "Contagion Exposure" chapter with the following template:

```
### X. Contagion Exposure

#### X.1 Matrix Position
- Paradigm: [Primary Paradigm] + [Secondary Paradigm]
- Super-Spreader Rank: [Rank/19]
- Vulnerable Rank: [Rank/19]
- Cluster Membership: [Cluster Name]

#### X.2 As Contagion Source
- Primary targets (intensity >= 3): List industry pairs and scores
- Strongest transmission pathway: [Pathway description]
- Historical validation: [Cases or explanation]

#### X.3 As Contagion Receptor
- Primary sources (intensity >= 3): List industry pairs and scores
- Most vulnerable pathway: [Pathway description]
- Critical contagion threshold: [Conditions for transmission]

#### X.4 Stress Escalation
- Most dangerous factor combination: [Factor combination + stressed intensity]
- Industry-specific vulnerability: [e.g., "Tech HW is most vulnerable to High Leverage + Market Panic combination"]

#### X.5 Concentration Management
- Linked super-spreader (Financials/Tech HW/Energy) combined exposure cap recommendation
- Cluster total exposure cap recommendation
```

---

## 8. Limitations

1. **Matrix is a static snapshot**: This matrix reflects international industry structure as of mid-2026. As the global economy evolves (AI infrastructure expansion, energy transition, deglobalization), matrix intensities and directions require periodic recalibration.

2. **Confidence collapse cannot be fully matrixed**: Confidence Collapse (S) as a boundaryless contagion type is constrained to moderate intensities (max 4, only for historically validated pairs). In reality, extreme confidence collapse events can cross any industry boundary (e.g., 2008 GFC affected sectors entirely unrelated to subprime). The matrix cannot capture these "black swan" contagion events.

3. **Indirect paths not captured**: The matrix only evaluates direct transmission (source → receptor). In practice, contagion propagates through A → B → C cascades (e.g., Energy default → Chemical sector slowdown → Consumer Staples packaging cost increase). Such chain transmission may produce higher effective intensity than pairwise direct links suggest. Multi-step simulation is required to capture this.

4. **[PRELIMINARY] data quality**: As noted in the header, all matrix intensities are **initial methodological estimates** before empirical calibration against international default correlation data. Users should treat scores as directional indicators. The current version prioritizes structural logic and historical precedent over statistical precision.

5. **Escalation factor quantification is preliminary**: The jump tables in Section 6 are based on historical experience and logical reasoning, not statistical models. Synergy effects (Section 6.3) are simplified and actual dynamics are more complex.

6. **Industry boundary blur**: Real companies may span multiple industries (e.g., Siemens spans Capital Goods + Technology Hardware + Software; Amazon spans Retail + Software & Services + Transportation). A single industry label understates contagion coupling for such multi-industry entities.

7. **Sovereigns & GSEs as a special class**: Sovereigns are not "industries" in the conventional sense. Their inclusion reflects their outsized role in credit contagion (sovereign-bank nexus, fiscal policy transmission). However, sovereign credit analysis follows a fundamentally different framework from corporate industry analysis.

8. **Geo-political and regional dimensions are compressed**: A single global matrix cannot capture region-specific contagion patterns (e.g., European sovereign-bank dynamics differ from emerging market sovereign risk). Regional sub-matrices may be needed for jurisdiction-specific applications.

9. **Non-market sectors not covered**: Government, non-profit, education, healthcare delivery (as opposed to equipment/pharma), and other non-market sectors are not included. Their contagion patterns follow different logic (political budget cycles, grant funding, etc.).

---

## 9. Appendix

### 9.1 Intensity Distribution Summary (342 Off-Diagonal Pairs)

| Intensity | Count | Percentage | Cumulative |
|---|---|---|---|
| 5 (Very Strong) | 2 | 0.6% | 0.6% |
| 4 (Strong) | 15 | 4.4% | 5.0% |
| 3 (Moderate) | 62 | 18.1% | 23.1% |
| 2 (Weak) | 48 | 14.0% | 37.1% |
| 1 (Very Weak) | 215 | 62.9% | 100.0% |

**Total high-intensity links (>= 4):** 17 (5.0%) — these form the structural backbone of the contagion network.

### 9.2 Complete Row/Column Sums

| # | Industry | Row Sum | Col Sum | Average Intensity |
|---|---|---|---|---|
| 1 | Energy (Oil & Gas) | 43 | 43 | 2.39 |
| 2 | Chemicals | 40 | 40 | 2.22 |
| 3 | Metals & Mining | 29 | 29 | 1.61 |
| 4 | Construction Materials | 27 | 27 | 1.50 |
| 5 | Capital Goods | 39 | 39 | 2.17 |
| 6 | Commercial Services | 24 | 24 | 1.33 |
| 7 | Transportation | 38 | 38 | 2.11 |
| 8 | Automobiles | 34 | 34 | 1.89 |
| 9 | Consumer Durables | 27 | 27 | 1.50 |
| 10 | Consumer Staples | 25 | 25 | 1.39 |
| 11 | Retail | 33 | 33 | 1.83 |
| 12 | Technology Hardware | 44 | 44 | 2.44 |
| 13 | Software & Services | 36 | 36 | 2.00 |
| 14 | Biotech & Pharma | 30 | 30 | 1.67 |
| 15 | Healthcare Equipment | 28 | 28 | 1.56 |
| 16 | Utilities (Regulated) | 30 | 30 | 1.67 |
| 17 | Telecommunications | 25 | 25 | 1.39 |
| 18 | Financials (Banks/Insurance) | 48 | 48 | 2.67 |
| 19 | Sovereigns & GSEs | 42 | 42 | 2.33 |

### 9.3 Version History

| Version | Date | Changes | Author |
|---|---|---|---|
| v0.0.1 | 2026-07-10 | Initial creation: 13x13 contagion matrix (China industry classification), industry clustering, escalation factor mapping, engine integration | Engine Team |
| v0.0.1 | 2026-07-10 | Systemic intelligence layer integration: engine version unified to v0.0.1, forming complete contagion framework with contagion theory | Engine Team |
| v0.0.1 | 2026-07-10 | **Internationalization rewrite**: replaced 13 China-specific industries with 19 GICS-based international industries; new paradigm mapping via P1-P6 framework; full 19x19 annotated matrix; derived metrics (CFC, CVC, CNER); stress escalation jump tables; harmonized with international contagion theory | Engine Team |

---

*This document is the operational extension of [Contagion Theory](contagion-theory.md) (v0.0.1). The two documents must be used together.*
