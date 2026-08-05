# International Industry Contagion Matrix

**Version**: v0.3.2 | **Date**: 2026-07-10

> **[PRELIMINARY]** Matrix intensities are initial methodological estimates pending empirical calibration against international default correlation data. All scores are theoretical constructs based on economic linkage analysis and historical precedent mapping, not statistical estimation. Users should treat these as directional indicators rather than precise measures.

---

## Table of Contents

1. [Industry Classification and Paradigm Mapping](#1-industry-classification-and-paradigm-mapping)
2. [Contagion Matrix — 19x19 Intensity Grid](#2-contagion-matrix--19x19-intensity-grid)
6. [Stress Escalation — Factor-Specific Intensity Jumps](#6-stress-escalation--factor-specific-intensity-jumps)

---

> **Reading guide**: §§1-2 (classification, the 19x19 grid) and §6 (stress escalation) contain the
> executable core — required reading before executing any work path that
> references this document.
> §§3-5 and §§7-9 (pathways, construction logic, derived metrics, integration,
> limitations) live in `appendix/contagion-matrix-appendix.md` — read on demand.


- [Appendix (moved sections, on-demand)](appendix/contagion-matrix-appendix.md)
## 1. Industry Classification and Paradigm Mapping

### 1.1 Paradigm Framework

Based on [Contagion Theory](contagion-theory.md) Section 4, each international industry is mapped to a primary and secondary analytical paradigm. Industries sharing the same paradigm exhibit **higher intrinsic contagion coupling** due to shared risk drivers, funding characteristics, and market narrative logic.

| Paradigm | Description | Core Characteristics |
|---|---|---|
| **P1: Cyclical** | Sectors where commodity prices, freight rates, capacity utilization, or cyclical business/consumer spending determine demand and margins | Cycle amplitude, capacity utilization, inventory cycles, overcapacity risk |
| **P2: Defensive** | Sectors with inelastic demand where brand moats and pricing power stabilize margins through the cycle | Gross-margin stability, repeat purchase rate, channel density |
| **P3: Growth** | R&D-intensive sectors where technology roadmaps, IP, and pipelines drive revenue growth | High R&D intensity, patent concentration, skilled labor dependence |
| **P4: Regulated Utility** | License- or concession-based sectors where the regulated asset base and tariff frameworks drive cash flows (NOI/DSCR) | High fixed assets, long-duration contracts, infrastructure financing |
| **P5: Financial** | Financial institutions where capital adequacy, asset quality, and funding structure are the core risk drivers | Capital ratios, funding stability, regulatory cycle |
| **P6: Sovereign-Linked** | Sovereigns, sub-sovereigns, GSEs, and DFIs where fiscal capacity and institutional strength determine credit | Fiscal balance, debt sustainability, institutional credibility |

> Paradigm codes follow the single source of truth in [industry-framework.md](industry-framework.md) §2-§3. Legacy archetype names (Policy-Driven, Technology Moat, Zero-Sum Game, Asset Lease, Brand + Channel, Network + Traffic) survive only as descriptive language; the official legacy-to-current mapping is recorded in industry-framework.md Appendix C.

### 1.2 Industry-to-Paradigm Mapping Table

| # | Industry | Primary Paradigm | Secondary Paradigm | Financial Intensity | Rationale |
|---|---|---|---|---|---|
| 1 | **Energy (Oil & Gas)** | P1 (Cyclical) | P4 (Regulated Utility) | High | Geopolitical commodity, OPEC+ policy dependence, E&P infrastructure-heavy |
| 2 | **Chemicals** | P1 (Cyclical) | P3 (Growth) | Medium | Commodity/specialty price cycles, specialty chemicals IP, energy cost dependence |
| 3 | **Metals & Mining** | P1 (Cyclical) | P6 (Sovereign-Linked) | Medium | Commodity price cycle dominance, resource nationalism, trade policy |
| 4 | **Construction Materials** | P1 (Cyclical) | P4 (Regulated Utility) | Medium | Infrastructure demand cycle, quarries/plants as fixed assets |
| 5 | **Capital Goods** | P1 (Cyclical) | P2 (Defensive) | Medium-High | Business investment cycle; brand/aftermarket moats in select sub-industries |
| 6 | **Commercial Services** | P1 (Cyclical) | P3 (Growth) | Low-Medium | Corporate spending cycle; platform-scaled sub-industries, fragmented |
| 7 | **Transportation (Air/Rail/Shipping)** | P4 (Regulated Utility) | P1 (Cyclical) | High | Fleet/network infrastructure, regulated access pricing, fuel/demand cycle |
| 8 | **Automobiles** | P1 (Cyclical) | P3 (Growth) | High | Big-ticket consumer cycle, overcapacity/price war risk, EV/autonomous disruption |
| 9 | **Consumer Durables** | P1 (Cyclical) | P2 (Defensive) | Low-Medium | Deferrable purchases, replacement cycle, brand provides partial cushion |
| 10 | **Consumer Staples** | P2 (Defensive) | P3 (Growth) | Low | Brand loyalty, inelastic demand, product innovation overlay |
| 11 | **Retail** | P1 (Cyclical) | P2 (Defensive) | Medium | Consumer spending cycle; staples-anchored formats defensive, omnichannel scale |
| 12 | **Technology Hardware (Semis)** | P3 (Growth) | P1 (Cyclical) | High | Moore's Law IP, fab capex, memory/commodity-chip cycle, export controls |
| 13 | **Software & Services** | P3 (Growth) | P2 (Defensive) | Medium | SaaS/IP, switching-cost moats, cloud platform economies |
| 14 | **Biotech & Pharma** | P3 (Growth) | P2 (Defensive) | Medium-High | Patent cliff, pipeline value dependence; marketed-drug cash flows defensive |
| 15 | **Healthcare Equipment** | P2 (Defensive) | P3 (Growth) | Medium | Device IP, FDA clearance, procedure-volume stability |
| 16 | **Utilities (Regulated)** | P4 (Regulated Utility) | P2 (Defensive) | High | Regulated asset base (RAB), tariff policy, long-lived infrastructure |
| 17 | **Telecommunications** | P4 (Regulated Utility) | P3 (Growth) | High | Licensed spectrum, regulated networks, 5G capex cycle |
| 18 | **Financials (Banks/Insurance)** | P5 (Financial) | P6 (Sovereign-Linked) | Very High | Capital regulation, asset quality, sovereign exposure |
| 19 | **Sovereigns & GSEs** | P6 (Sovereign-Linked) | — (Special: Gov't Credit Binding) | Very High | Fiscal capacity, monetary control, quasi-government guarantee |

### 1.3 Paradigm Clusters

| Paradigm | Industries | Intra-Paradigm Contagion Characteristics |
|---|---|---|
| **P1 (Cyclical)** | Energy, Chemicals, Metals & Mining, Construction Materials, Capital Goods, Commercial Services, Automobiles, Consumer Durables, Retail; secondary for Transportation, TechHW | Commodity/freight cycles synchronize across sectors; overcapacity and price-war phases spread across similar end-markets; shared macro-demand sensitivity |
| **P2 (Defensive)** | Consumer Staples, Healthcare Equipment; secondary for Capital Goods, Consumer Durables, Retail, Software, Biotech (pharma), Utilities | Consumer confidence resonance; brand-crisis demonstration effects; defensive cash flows co-move in risk-off episodes |
| **P3 (Growth)** | Technology Hardware, Software & Services, Biotech & Pharma; secondary for Chemicals, Commercial Services, Automobiles, Consumer Staples, Telecom, Healthcare Equipment | Supply chain tight coupling (chip → equipment → software); IPO/venture capital funding channels shared; talent market co-dependence |
| **P4 (Regulated Utility)** | Transportation, Utilities, Telecommunications; secondary for Energy, Construction Materials | Infrastructure funding channels (project finance, green bonds); interest rate sensitivity; regulatory concession risk |
| **P5 (Financial)** | Financials (Banks/Insurance); no secondary members | Single-industry paradigm: coupling manifests through cross-paradigm channels — common creditor, financial linkage, and the sovereign-bank nexus |
| **P6 (Sovereign-Linked)** | Sovereigns & GSEs; secondary for Metals & Mining, Financials | Fiscal-policy transmission; sovereign-bank doom loop; quasi-government guarantee repricing |

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


> **Appendix**: §3 (pathways), §4 (construction logic), §5 (derived metrics), §7 (integration), §8 (limitations), §9 (appendix) moved to `appendix/contagion-matrix-appendix.md` — read on demand.

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

When multiple escalation factors trigger simultaneously, intensity amplification follows **multiplicative stacking** rather than additive. Deterministic rule (implemented by `src/contagion_engine.py`):

```
For each documented combination in the triggered factor set:
  Multiplier = per-combination value from the table below
  (any 3+ simultaneous factors -> 3.0x, dominating pair combinations)

For every cell touched by the combined factors:
  Δ         = (intensity after all per-factor §6.2 rules) - base intensity
  intensity = min(5, base + round(Δ × Multiplier))
```

| Factor Combination | Synergy Multiplier | Worked Example |
|---|---|---|
| Market Panic + Regulatory Vacuum | 1.5x | Base 3, Panic broad row +1 and Vacuum broad row +1 → Δ=2 → 3 + round(2×1.5) = 5 |
| Market Panic + High Leverage | 2.0x | Base 3, Panic broad row +1 (explicit Leverage jump co-applies via max) → Δ=1 → 3 + round(1×2.0) = 5 |
| Regulatory Vacuum + Year-End Effect | 1.5x | Base 3, Vacuum explicit jump +1 → Δ=1 → 3 + round(1×1.5) = 5 |
| Three or more simultaneously | 3.0x | Systemic crisis threshold: most base-3 pairs jump to 4-5 (Δ=1 → 3+3=6 → capped at 5) |

**Interpretation note:** the multiplier applies to the total increment produced by the combined §6.2 rules, not to the final intensity. Cells untouched by every triggered factor (no explicit jump, no generic bump, no broad row) are unaffected by synergy.

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