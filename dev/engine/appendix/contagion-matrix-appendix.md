# International Industry Contagion Matrix — Appendix

> Appendix to `contagion-matrix.md` — version tracks the parent document; reference
> material (worked examples, derivations, historical validation) moved here in
> the 2026-07 restructure. Read on demand.

---

## 3. Contagion Pathways and Graph Representation

### 3.1 High-Intensity Links (Score >= 4)

The following links form the structural backbone of the global industry contagion network:

<!-- GENERATED:high-intensity-links -->
```
Score 5 (Very Strong):
  Energy (Oil & Gas) ↔ Chemicals  (C+R, H)
  Financials (Banks/Insurance) ↔ Sovereigns & GSEs  (R+L+S, H)

Score 4 (Strong):
  Automobiles ↔ Technology Hardware (Semiconductors)  (C, H)
  Biotech & Pharma ↔ Healthcare Equipment  (C+S, H)
  Capital Goods ↔ Technology Hardware (Semiconductors)  (C, H)
  Chemicals ↔ Biotech & Pharma  (C, H)
  Chemicals ↔ Consumer Staples  (C, H)
  Energy (Oil & Gas) ↔ Transportation  (C, H)
  Energy (Oil & Gas) ↔ Utilities (Regulated)  (C, H)
  Metals & Mining ↔ Capital Goods  (C, H)
  Metals & Mining ↔ Construction Materials  (C, H)
  Software & Services ↔ Telecommunications  (C+S, H)
  Technology Hardware (Semiconductors) ↔ Software & Services  (C+S, H)
  Transportation ↔ Retail  (C, H)

Total: 14 unique high-intensity pairs (28 directed links, score >= 4), including 2 pairs at score 5
```
<!-- /GENERATED -->

### 3.2 Moderate-Intensity Links (Score = 3)

Score-3 links form the secondary transmission network. In total there are 62 unique moderate-intensity directed links connecting industries across all paradigms. Key clusters:

**P1 (Cyclical) Cluster:**
- Chemicals ↔ Automobiles, Chemicals ↔ Consumer Durables, Automobiles ↔ Consumer Durables
- Metals & Mining ↔ Energy, Metals & Mining ↔ Construction Materials
- Construction Materials ↔ Capital Goods

**P3 (Growth) Cluster:**
- Tech Hardware ↔ Software & Services (also score 4)
- Tech Hardware ↔ Capital Goods (also score 4), Tech Hardware ↔ Healthcare Equipment
- Software ↔ Commercial Services, Software ↔ Retail
- Biotech ↔ Financials, Healthcare Equipment ↔ Capital Goods

**P4 (Regulated Utility) Cluster:**
- Construction Materials ↔ Utilities
- Transportation ↔ Capital Goods, Transportation ↔ Commercial Services
- Telecommunications ↔ Software & Services (also score 4)

**P5/P6 Financial–Sovereign Nexus (cross-paradigm):**
- Financials ↔ Sovereigns (score 5 — the strongest link in the matrix)
- Financials ↔ Energy, Financials ↔ Capital Goods, Financials ↔ Commercial Services, Financials ↔ Transportation, Financials ↔ Tech Hardware, Financials ↔ Software
- Sovereigns ↔ Energy, Sovereigns ↔ Metals & Mining, Sovereigns ↔ Construction Materials, Sovereigns ↔ Utilities
- Telecommunications ↔ Financials, Utilities ↔ Financials

**Consumer (P1/P2) Cluster:**
- Consumer Staples ↔ Retail, Consumer Durables ↔ Retail, Retail ↔ Commercial Services
- Consumer Durables ↔ Chemicals, Consumer Staples ↔ Chemicals
- Consumer Durables ↔ Technology Hardware

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


---

## 4. Matrix Construction Logic

### 4.1 Five Construction Principles

#### Principle 1: Shared Paradigm Elevates Coupling

Industries under the same analytical paradigm exhibit systematically higher contagion intensity due to shared risk factors:

| Paradigm | Example Pair | Intensity | Rationale |
|---|---|---|---|
| P1 (Cyclical) | Automobiles ↔ Consumer Durables | 3 | Shared consumer discretionary spending; replacement cycle correlation |
| P2 (Defensive) | Consumer Staples ↔ Healthcare Equipment | 1 | Only two member industries; intra-paradigm coupling is weak — defensive sectors decouple idiosyncratically |
| P3 (Growth) | Tech Hardware ↔ Software | 4 | Ecosystem lock-in (Apple, Wintel, ARM); AI/GPU dependency |
| P4 (Regulated Utility) | Transportation ↔ Utilities | 2 | Both are infrastructure-intensive but serve different end-markets |
| P5 (Financial) | — (single-industry paradigm) | — | Coupling manifests cross-paradigm: Financials ↔ Sovereigns (5) via the sovereign-bank nexus |
| P6 (Sovereign-Linked) | — (single-industry paradigm) | — | Coupling manifests cross-paradigm: Sovereigns ↔ Energy / Metals & Mining / Utilities (3) via fiscal-commodity transmission |

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

### 4.2 Symmetry Analysis

The base matrix is **fully symmetric**: every off-diagonal pair is assigned the same intensity in both directions (verified at parse time by `src/contagion_engine.py`). This reflects the design principle that the matrix captures linkage **existence** and **magnitude** rather than unidirectional flow:

| Type | Example | Explanation |
|---|---|---|
| **Supply Chain Symmetry** | Energy ↔ Transportation (4) | Fuel cost impact on transportation (input) and transport demand impact on energy (output) are both strong |
| **Sovereign-Bank Nexus** | Financials ↔ Sovereigns (5) | The doom loop is inherently bidirectional — the strongest link in the matrix |
| **Financial Hub Reach** | Financials ↔ All (3 avg) | Financials have broad diversified exposure to all sectors, in both directions |

**Where asymmetry lives instead:** directional nuance is captured in (a) the §2.4 cell annotations (one-way arrows and channel types), and (b) the §6 stress escalation rules, which apply factor-specific jumps to specific directions (e.g., "Financials → All") and therefore break symmetry under stress. CNER (§5.3) is 1.00 for every industry at base and only discriminates once escalation is applied.

### 4.3 Channels Not Exhaustively Captured

1. **Multi-step cascade**: The matrix captures direct (A→B) transmission only. Second-order (A→B→C) cascades — e.g., Energy default → Chemical producer slowdown → Consumer Staples packaging shortage — require multi-step simulation beyond the pairwise matrix
2. **Common ownership / institutional investor overlap**: Two sectors with no direct economic linkage can co-move if owned by the same leveraged investor base (e.g., cross-sector ETF rebalancing)
3. **Geopolitical event-driven correlation**: A single geopolitical event (sanctions, trade war, conflict) can simultaneously affect multiple paradigm-unrelated sectors (e.g., Russia-Ukraine 2022 simultaneously hit Energy, Chemicals, Agriculture/Consumer Staples, and Metals & Mining)
4. **Liquidity-driven path**: In extreme stress, liquidity squeeze can transmit between any pair regardless of economic linkage — the matrix does not attribute score-5 liquidity contagion to all cells, but users should be aware of this limitation (see Section 6 for stress escalation)

---


---

## 5. Derived Metrics — Super-Spreaders, Vulnerability, and Coefficients

### 5.1 Super-Spreader Industries (Top 3 Row Sums)

Super-spreaders are industries whose default or distress causes the widest contagion to other sectors. Measured by **row sum** (total outgoing contagion intensity).

<!-- GENERATED:super-spreaders -->
| Rank | Industry | Row Sum | Key Targets (Score >= 3) |
|---|---|---|---|
| 1 | **Financials (Banks/Insurance)** | **47** | Sovereigns & GSEs(5), Capital Goods(3), Commercial Services(3), Energy (Oil & Gas)(3), Software & Services(3), Technology Hardware (Semiconductors)(3), Telecommunications(3), Transportation(3), Utilities (Regulated)(3) |
| 2 | **Capital Goods** | **43** | Metals & Mining(4), Technology Hardware (Semiconductors)(4), Automobiles(3), Construction Materials(3), Energy (Oil & Gas)(3), Financials (Banks/Insurance)(3), Healthcare Equipment(3), Transportation(3) |
| 3 | **Chemicals** | **42** | Energy (Oil & Gas)(5), Biotech & Pharma(4), Consumer Staples(4), Automobiles(3), Construction Materials(3), Consumer Durables(3), Technology Hardware (Semiconductors)(3) |
| 3 | **Technology Hardware (Semiconductors)** | **42** | Automobiles(4), Capital Goods(4), Software & Services(4), Chemicals(3), Consumer Durables(3), Financials (Banks/Insurance)(3), Healthcare Equipment(3), Telecommunications(3) |
| 5 | **Energy (Oil & Gas)** | **41** | Chemicals(5), Transportation(4), Utilities (Regulated)(4), Automobiles(3), Capital Goods(3), Financials (Banks/Insurance)(3), Metals & Mining(3), Sovereigns & GSEs(3) |
<!-- /GENERATED -->

**Core logic:** Financials (Banks/Insurance) is the central credit intermediary — credit supply contraction affects all sectors, and the sovereign-bank nexus is the highest-intensity link in the matrix. Capital Goods sits at the manufacturing hub: equipment demand is the first casualty of credit tightening across every downstream sector. Chemicals and Technology Hardware tie at rank 3 — petrochemical feedstock reaches virtually all manufacturing, while chips are essential inputs to virtually all technology and advanced manufacturing. Energy (rank 5) remains the primary economy-wide cost channel.

### 5.2 Vulnerable Industries (Top 3 Column Sums)

Vulnerable industries are those most exposed to incoming contagion from other sectors. Measured by **column sum** (total incoming contagion exposure). Because the base matrix is symmetric (§4.2), column sums equal row sums at base; the ranking below mirrors §5.1 and diverges only once §6 escalation is applied.

<!-- GENERATED:vulnerable-industries -->
| Rank | Industry | Column Sum | Key Sources (Score >= 3) |
|---|---|---|---|
| 1 | **Financials (Banks/Insurance)** | **47** | Sovereigns & GSEs(5), Capital Goods(3), Commercial Services(3), Energy (Oil & Gas)(3), Software & Services(3), Technology Hardware (Semiconductors)(3), Telecommunications(3), Transportation(3), Utilities (Regulated)(3) |
| 2 | **Capital Goods** | **43** | Metals & Mining(4), Technology Hardware (Semiconductors)(4), Automobiles(3), Construction Materials(3), Energy (Oil & Gas)(3), Financials (Banks/Insurance)(3), Healthcare Equipment(3), Transportation(3) |
| 3 | **Chemicals** | **42** | Energy (Oil & Gas)(5), Biotech & Pharma(4), Consumer Staples(4), Automobiles(3), Construction Materials(3), Consumer Durables(3), Technology Hardware (Semiconductors)(3) |
| 3 | **Technology Hardware (Semiconductors)** | **42** | Automobiles(4), Capital Goods(4), Software & Services(4), Chemicals(3), Consumer Durables(3), Financials (Banks/Insurance)(3), Healthcare Equipment(3), Telecommunications(3) |
| 5 | **Energy (Oil & Gas)** | **41** | Chemicals(5), Transportation(4), Utilities (Regulated)(4), Automobiles(3), Capital Goods(3), Financials (Banks/Insurance)(3), Metals & Mining(3), Sovereigns & GSEs(3) |
<!-- /GENERATED -->

**Key finding:** Financials is simultaneously the #1 super-spreader and the #1 vulnerable industry — the most "central" node, exposed to every sector through loan books, investment portfolios, and derivative counterparty risk. Capital Goods and Chemicals share the same hub property at ranks 2-3. This "central node" property means credit events in these sectors can trigger **systemic contagion** not limited to local pathways.

### 5.3 Contagion Coefficients

#### Contagion Force Coefficient (CFC)

Measures the relative contagion transmission capacity of each industry:

```
CFC_i = Row_Sum_i / Max(Row_Sum)
```

<!-- GENERATED:cfc-table -->
| Rank | Industry | Row Sum | Coefficient |
|---|---|---|---|
| 1 | Financials (Banks/Insurance) | 47 | 1.00 |
| 2 | Capital Goods | 43 | 0.91 |
| 3 | Chemicals | 42 | 0.89 |
| 3 | Technology Hardware (Semiconductors) | 42 | 0.89 |
| 5 | Energy (Oil & Gas) | 41 | 0.87 |
| 6 | Transportation | 39 | 0.83 |
| 7 | Sovereigns & GSEs | 37 | 0.79 |
| 8 | Metals & Mining | 35 | 0.74 |
| 9 | Software & Services | 34 | 0.72 |
| 10 | Automobiles | 33 | 0.70 |
| 11 | Construction Materials | 32 | 0.68 |
| 11 | Utilities (Regulated) | 32 | 0.68 |
| 13 | Commercial Services | 31 | 0.66 |
| 13 | Consumer Durables | 31 | 0.66 |
| 13 | Retail | 31 | 0.66 |
| 16 | Telecommunications | 29 | 0.62 |
| 17 | Biotech & Pharma | 28 | 0.60 |
| 17 | Consumer Staples | 28 | 0.60 |
| 19 | Healthcare Equipment | 27 | 0.57 |
<!-- /GENERATED -->

#### Contagion Vulnerability Coefficient (CVC)

Measures the relative contagion reception vulnerability of each industry:

```
CVC_i = Col_Sum_i / Max(Col_Sum)
```

<!-- GENERATED:cvc-table -->
| Rank | Industry | Col Sum | Coefficient |
|---|---|---|---|
| 1 | Financials (Banks/Insurance) | 47 | 1.00 |
| 2 | Capital Goods | 43 | 0.91 |
| 3 | Chemicals | 42 | 0.89 |
| 3 | Technology Hardware (Semiconductors) | 42 | 0.89 |
| 5 | Energy (Oil & Gas) | 41 | 0.87 |
| 6 | Transportation | 39 | 0.83 |
| 7 | Sovereigns & GSEs | 37 | 0.79 |
| 8 | Metals & Mining | 35 | 0.74 |
| 9 | Software & Services | 34 | 0.72 |
| 10 | Automobiles | 33 | 0.70 |
| 11 | Construction Materials | 32 | 0.68 |
| 11 | Utilities (Regulated) | 32 | 0.68 |
| 13 | Commercial Services | 31 | 0.66 |
| 13 | Consumer Durables | 31 | 0.66 |
| 13 | Retail | 31 | 0.66 |
| 16 | Telecommunications | 29 | 0.62 |
| 17 | Biotech & Pharma | 28 | 0.60 |
| 17 | Consumer Staples | 28 | 0.60 |
| 19 | Healthcare Equipment | 27 | 0.57 |
<!-- /GENERATED -->

#### Contagion Net Exposure Ratio (CNER)

```
CNER_i = Row_Sum_i / Col_Sum_i
```

<!-- GENERATED:cner-table -->
| Industry | Row Sum | Col Sum | CNER | Interpretation |
|---|---|---|---|---|
| Financials (Banks/Insurance) | 47 | 47 | 1.00 | Balanced |
| Capital Goods | 43 | 43 | 1.00 | Balanced |
| Chemicals | 42 | 42 | 1.00 | Balanced |
| Technology Hardware (Semiconductors) | 42 | 42 | 1.00 | Balanced |
| Energy (Oil & Gas) | 41 | 41 | 1.00 | Balanced |
| Transportation | 39 | 39 | 1.00 | Balanced |
| Sovereigns & GSEs | 37 | 37 | 1.00 | Balanced |
| Metals & Mining | 35 | 35 | 1.00 | Balanced |
| Software & Services | 34 | 34 | 1.00 | Balanced |
| Automobiles | 33 | 33 | 1.00 | Balanced |
| Construction Materials | 32 | 32 | 1.00 | Balanced |
| Utilities (Regulated) | 32 | 32 | 1.00 | Balanced |
| Commercial Services | 31 | 31 | 1.00 | Balanced |
| Consumer Durables | 31 | 31 | 1.00 | Balanced |
| Retail | 31 | 31 | 1.00 | Balanced |
| Telecommunications | 29 | 29 | 1.00 | Balanced |
| Biotech & Pharma | 28 | 28 | 1.00 | Balanced |
| Consumer Staples | 28 | 28 | 1.00 | Balanced |
| Healthcare Equipment | 27 | 27 | 1.00 | Balanced |
<!-- /GENERATED -->

**Note on symmetry:** The CNER for all industries is 1.00 because the matrix is structurally symmetric (each off-diagonal pair is assigned the same intensity in both directions). This reflects the design principle that the matrix captures linkage **existence** and **magnitude** rather than unidirectional flow. Directional asymmetries (e.g., upstream → downstream) are captured in the detailed annotations (Section 2.4) and in practical application (Section 6 stress scenario design), but the base matrix is symmetric. Future calibrated versions may introduce asymmetry coefficients based on empirical directional default correlation data.

### 5.4 Industry Clustering

<!-- GENERATED:clusters -->
#### High-Contagion Cluster (Intra-cluster average intensity >= 3.0)

| Cluster | Industries | Core Links | Intra Avg |
|---|---|---|---|
| **A: Energy-Chemicals-Transport-Utilities** | Energy (Oil & Gas), Chemicals, Transportation, Utilities (Regulated) | Energy↔Chemicals(5), Energy↔Transport(4), Energy↔Utilities(4), Chemicals↔Transport(2) | 3.0 |
| **B: Tech-Auto-Capital Goods** | Technology Hardware (Semiconductors), Software & Services, Automobiles, Capital Goods | Tech HW↔Software(4), Tech HW↔Autos(4), Cap Goods↔Tech HW(4), Cap Goods↔Autos(3) | 3.2 |
| **C: Sovereign-Financial Hub** | Sovereigns & GSEs, Financials (Banks/Insurance) | Sovereigns↔Financials(5) | 5.0 |
| **D: Bio-Healthcare** | Biotech & Pharma, Healthcare Equipment | Biotech↔Healthcare Equip(4), Chemicals↔Biotech(4) | 4.0 |
| **F: Infrastructure-Construction** | Construction Materials, Metals & Mining, Capital Goods, Utilities (Regulated) | Metals↔Const Mat(4), Metals↔Cap Goods(4), Const Mat↔Utilities(3) | 3.0 |
| **G: Telecom-Software** | Telecommunications, Software & Services | Telecom↔Software(4) | 4.0 |
| **H: Commercial Services-Network** | Commercial Services, Retail, Transportation, Software & Services | ComServ↔Retail(3), ComServ↔Transport(3), ComServ↔Software(3) | 3.0 |

#### Moderate-Contagion Cluster (Intra-cluster average intensity 2.0-2.9)

| Cluster | Industries | Core Links | Intra Avg |
|---|---|---|---|
| **E: Retail-Consumer-Logistics** | Retail, Consumer Staples, Consumer Durables, Transportation | Retail↔Transport(4), Retail↔Consumer Staples(3), Retail↔Consumer Durables(3), Consumer Staples↔Chemicals(4) | 2.7 |
<!-- /GENERATED -->

---


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


---

## 9. Appendix

### 9.1 Intensity Distribution Summary (342 Directed Off-Diagonal Links)

<!-- GENERATED:intensity-distribution -->
| Intensity | Directed Links | Unique Pairs | Share of Directed |
|---|---|---|---|
| 1 | 150 | 75 | 43.9% |
| 2 | 96 | 48 | 28.1% |
| 3 | 68 | 34 | 19.9% |
| 4 | 24 | 12 | 7.0% |
| 5 | 4 | 2 | 1.2% |
| **Total** | **342** | **171** | 100.0% |
<!-- /GENERATED -->

**High-intensity links (>= 4)** form the structural backbone of the contagion network (see §3.1).

### 9.2 Complete Row/Column Sums

<!-- GENERATED:row-col-sums -->
| Rank | Industry | Row Sum | Col Sum | CFC (Row/Max) |
|---|---|---|---|---|
| 1 | Financials (Banks/Insurance) | 47 | 47 | 1.00 |
| 2 | Capital Goods | 43 | 43 | 0.91 |
| 3 | Chemicals | 42 | 42 | 0.89 |
| 3 | Technology Hardware (Semiconductors) | 42 | 42 | 0.89 |
| 5 | Energy (Oil & Gas) | 41 | 41 | 0.87 |
| 6 | Transportation | 39 | 39 | 0.83 |
| 7 | Sovereigns & GSEs | 37 | 37 | 0.79 |
| 8 | Metals & Mining | 35 | 35 | 0.74 |
| 9 | Software & Services | 34 | 34 | 0.72 |
| 10 | Automobiles | 33 | 33 | 0.70 |
| 11 | Construction Materials | 32 | 32 | 0.68 |
| 11 | Utilities (Regulated) | 32 | 32 | 0.68 |
| 13 | Commercial Services | 31 | 31 | 0.66 |
| 13 | Consumer Durables | 31 | 31 | 0.66 |
| 13 | Retail | 31 | 31 | 0.66 |
| 16 | Telecommunications | 29 | 29 | 0.62 |
| 17 | Biotech & Pharma | 28 | 28 | 0.60 |
| 17 | Consumer Staples | 28 | 28 | 0.60 |
| 19 | Healthcare Equipment | 27 | 27 | 0.57 |
| | **Total / Mean** | **662** | **662** | mean 34.84 |
<!-- /GENERATED -->

### 9.3 Version History

| Version | Date | Changes | Author |
|---|---|---|---|
| v0.7.x (legacy) | 2026-07-10 | Initial creation: 13x13 contagion matrix (China industry classification), industry clustering, escalation factor mapping, engine integration | Engine Team |
| v0.0.1 | 2026-07-18 | **Internationalization rewrite**: replaced 13 China-specific industries with 19 GICS-based international industries; full 19x19 annotated matrix; derived metrics (CFC, CVC, CNER); stress escalation jump tables | Engine Team |
| v0.0.2 | 2026-07-21 | Paradigm taxonomy unified on industry-framework P1-P6 (SS1.1-SS1.3); derived tables machine-generated from the SS2.1 heatmap (build_contagion_derived.py); symmetry analysis corrected (base matrix fully symmetric); cluster tiers recomputed | Engine Team |

---

*This document is the operational extension of [Contagion Theory](contagion-theory.md) (v0.2.0). The two documents must be used together.*
