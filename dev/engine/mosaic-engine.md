# Mosaic Engine

**Version**: v0.0.7 | **Date**: 2026-07-10
**Core Principle**: Data is always incomplete -- turn "incompleteness" from a weakness into a product feature

---

## 1. Core Concept

### 1.1 Two Fundamental Theories

| Theory | Meaning | Application in Engine |
|---|---|---|
| **Mosaic Theory** | Individual public data fragments are meaningless alone; assembled together they form a complete picture. Each piece of public information -- SEC filing, court record, bidding result, price report -- means nothing in isolation but forms a judgment when aggregated. | Multi-source data aggregation -> Signal stacking -> Confidence weighting |
| **Information Completeness Theory** | Answer not only "what we know" but also "what we don't know." Information gaps are not defects but sources of risk signals -- "we don't have this data" itself tells the user "uncertainty exists in this dimension." | Every conclusion includes completeness score and gap list |

### 1.2 Mosaic Engine Position in Overall Architecture

```
Skill Pack v0.0.1
  +-- Industry Classification (10-dimension scoring)
  +-- Track A: Fundamental Analysis (Pyramid Framework)
  +-- Track B: Market Pricing (4-Level Signals)
  +-- Cross-Validation Matrix (4-Quadrant)
  +-- Black Swan Back-Testing
  |
  +-- Mosaic Engine Layer <- This Document
        +-- Signal Extraction Layer
        +-- Mosaic Assembly Layer
        +-- Completeness Assessment Layer
        +-- Mode B Interface Definition (Placeholder)
```

---

## 2. Mode A: Mosaic Engine (Current Implementation) -- System Architecture

```
                        User Input
                    Industry + Entity Name
                         |
            +------------+------------+
            |            |            |
      Policy/Industry   Public Corp   Market Data
         (WebSearch)   (WebSearch)   (WebSearch)
            |            |            |
            +------------+------------+
                         |
                  +------+----------+
                  |  Signal         |  <- LLM: Extract structured signals from
                  |  Extraction     |     unstructured text
                  |  Layer          |
                  |  Each data      |
                  |  -> signal+     |
                  |  source+stamp+confidence |
                  +------+----------+
                         |
                  +------+----------+
                  |  Mosaic         |  <- Rules Engine: Aggregate signals by
                  |  Assembly       |     industry pyramid framework
                  |  Layer          |
                  |  Same-dimension stacking |
                  |  Cross-dimension validation |
                  |  Contradiction annotation |
                  +------+----------+
                         |
                  +------+----------+
                  |  Completeness   |  <- Core Differentiator
                  |  Assessment     |
                  |  Layer          |
                  |  Score per      |
                  |  dimension      |
                  |  "Enough data?" |
                  |  Gap->Risk      |
                  |  signal         |
                  |  mapping        |
                  +------+----------+
                         |
            +------------+------------+
            |            |            |
      Track A:       Track B:       Track C+:
      Fundamentals   Market Pricing Multi-stakeholder
      (Pyramid)      (4-level)     (P0/P1/P2 Modules)
            |            |            |
            +------------+------------+
                         |
                  +------+----------+
                  |  Combined       |
                  |  Output         |
                  |  Assessment     |
                  |  + Completeness Report |
                  |  + Gap List      |
                  |  + Confidence Annotation |
                  +-----------------+
```

---

## 3. Signal Extraction Layer

### 3.1 Function

**Input**: WebSearch results (titles + summaries + URLs)
**Output**: Structured signal objects

### 3.2 Signal Data Structure

```yaml
signal:
  id: "sig-001"
  source_url: "https://..."
  source_type: "sec_filing" | "court_record" | "bidding_result" | "industry_report" | "news" | "central_bank_data"
  timestamp: "2026-06-15"  # Time of source information, not crawl time
  dimension: "L2_technology"  # Which pyramid layer
  content: "Company achieved 24.8% production efficiency on next-gen technology"
  direction: "positive" | "negative" | "neutral"
  strength: 1-5  # 1=weak directional signal, 5=explicit quantitative signal
  cross_validated: false  # Set to true if >=2 independent sources confirm in assembly layer
```

### 3.3 Extraction Rules

- LLM extracts signals from each search result title + summary
- **No judgment, only structuring**
- Max 3 signals per source
- Each data piece annotated with its signal confidence level

---

## 4. Mosaic Assembly Layer

### 4.1 Core Logic

```
For each analysis dimension (e.g., L1 Policy Environment):
  1. Aggregate all signals for that dimension
  2. Same-direction signals stack -> increase confidence
  3. Contradictory signals appear -> label "divergence" and reduce confidence
  4. Cross-source validation -> upgrade signal level
  5. Calculate "signal density" = effective signals / estimated required signals
```

### 4.2 Five-Level Signal Confidence

| Level | Type | Description |
|---|---|---|
| **L5** | Multi-source cross-validated | Same fact confirmed by >=2 independent sources |
| **L4** | Single-source direct | One reliable source explicitly states |
| **L3** | Derived inference | Inferred from multiple fragments |
| **L2** | Directional weak signal | Direction only, no magnitude |
| **L1** | Missing signal (gap) | Data that should exist doesn't -- risk signal |

**Level priority**: L5 multi-source cross-validated > L4 single-source direct > L3 derived inference > L2 directional weak signal > L1 gap (annotated separately).

### 4.3 Signal Density Metric

Signal density is the **most critical output** of the mosaic assembly layer -- it directly answers "how much do we know about this dimension?"

| Signal Density | Meaning | Impact on Final Score |
|---|---|---|
| **>80%** | Information sufficient -- key signals largely complete | High confidence, direct scoring possible |
| **50-80%** | Information moderate -- main signals present but details lacking | Medium confidence, score with +/-1 error range |
| **20-50%** | Information insufficient -- only fragments | Low confidence, mark as "pending supplement," directional judgment only |
| **<20%** | Information severely lacking | No score for this dimension, mark as "insufficient data to evaluate" |

---

## 5. Completeness Assessment Layer (Core Differentiator)

This is the product differentiator. Not only telling users "what we saw" but also "what we didn't see and what risk that implies."

### 5.1 Three-Element Output Per Dimension

```
Dimension: L2 Technology Roadmap & Competitive Position
+-- Signal Density: 75% (Moderate)
+-- Key Signals Obtained:
|   +-- Module production efficiency (Leader 24.8% vs Follower ~23.5%)
|   +-- Central procurement qualification (59GW data available)
|   +-- Patent count (Leader 510 vs Competitors)
|   +-- Warning Capacity utilization (Industry estimate, not company disclosed)
+-- Missing Signals:
|   +-- Yield data by company (not individually disclosed)
|   +-- Non-silicon cost comparison (public estimates only)
|   +-- Independent third-party performance testing
+-- Gap Risk Assessment:
    -> Yield data missing -> Cannot precisely assess cost competitiveness -> Score range +/-1.5
    -> But procurement qualification and efficiency gap constitute sufficient differentiating signals
```

### 5.2 Data Gap -> Risk Mapping Table (General Template)

| Gap Type | Typical Missing Data | Associated Risk | Substitute Signal |
|---|---|---|---|
| Competitive data | Precise cost comparison by company | Over- or under-estimating cost advantage | Central procurement winning prices (market-accepted premium) |
| Financial data | No public filings (private companies) | Unable to assess financial health entirely | Enforcement records, litigation history, hiring trends |
| Market pricing | No stock/bond data (private companies) | Track B completely unavailable | Public funding events, equity transfer prices |
| Terms data | No terminal access for duration/Z-spread | Unable to perform fine interest rate risk analysis | YTM approximation, same-rating spread comparison |
| Liquidity data | Bid-ask spread not disclosed | Unable to assess true transaction cost | Average daily volume, turnover rate, abnormal volume events |
| External support | True scale of government implicit debt | Over- or under-estimating government support capacity | Explicit debt ratio + estimated sub-sovereign debt, annotate "implicit debt estimation error" |
| External support | Government rescue commitment (non-public) | Overestimating support willingness certainty | Historical support record + ownership structure + strategic positioning inference, annotate "non-public commitment" |
| External support | Group internal cash pooling policy and execution | Unable to assess group's actual support to subsidiaries | Related-party transactions + guarantee balance + business synergy, annotate "inferred from public info" |
| External support | Strategic investor actual support willingness (non-public stance) | Overestimating enforceability of strategic support | Public investment agreement terms + lock-up period + board composition |

### 5.3 Completeness Assessment Report Structure

Every analysis output **must** include the following structure:

```
1. Composite Rating & Key Findings
   +-- Confidence Annotation (High/Medium/Low)

2. Data Completeness Report (Signal Density Bar Chart)
   +--------------------------------------------------+
   | L1 Policy/Macro        ########.. 82%            |
   | L2 Technology/Competition ######.. 75%           |
   | L3 Supply Chain/Operations ####.... 48% Warning  |
   | L4 Financial/Debt      #########. 89%            |
   | L5 External Support    ######.... 60% Warning    |
   | Market Pricing (Track B) ###...... 35% Warning   |
   | Relative Value (M1.1)  ##........ 25% Critical   |
   | Covenant Analysis (M1.2) ########. 80%           |
   | Liquidity (M1.3)       ####...... 45% Warning    |
   +--------------------------------------------------+

3. Gap List (Sorted by Impact Priority)
   +-- Each gap: specific missing data -> impact -> alternative

4. Score Confidence Interval
   +-- Corrected score range per dimension based on signal density

5. User Actionable Recommendations
   +-- "For fine relative value analysis, consider subscribing to Bloomberg/Refinitiv terminal"
```

### 5.4 Confidence Impact on Scoring Rules

| Signal Density | Score Output Rule |
|---|---|
| >80% | Direct precise score output |
| 50-80% | Output score with +/-1 range |
| 20-50% | Directional judgment only (positive/negative/neutral), no precise score |
| <20% | "Insufficient data to evaluate," no score for this dimension |

---

## 6. Mode B: External Data Source Adapter (Architecture Placeholder)

> **Mode B Guardrail**: Do NOT invoke Mode B interfaces or generate external data values unless the user explicitly provides CSV upload, API endpoint, or MCP server. When Mode B is inactive, all Mode B fields should be treated as data gaps.

Standardized interface definition allowing users to connect their own data sources to fill mosaic gaps. Contract defined but not implemented.

### 6.1 Adapter Contract

```yaml
DataSourceAdapter:
  # Lifecycle
  init(config):        # Authentication, rate limiting config
  health_check():      # Availability check

  # Core Queries
  query_bond_analytics(bond_code, fields):
    # fields: ["ytm","duration","convexity","z_spread","oas","bid_ask"]
    # returns: {field: value, ...} + data_timestamp

  query_market_data(instrument_code, data_type, date_range):
    # data_type: "price_history" | "volume" | "volatility" | "fund_flow"

  query_industry_benchmark(industry, metric, date):
    # metric: "credit_spread" | "default_rate" | "rating_migration"

  to_signals():  # Convert external data to unified signal object format
```

### 6.2 Supported Connection Methods (Planned)

| Method | Use Case | Priority |
|---|---|---|
| REST API | Bloomberg Terminal / Refinitiv Eikon financial terminal APIs | P1 |
| MCP Server | User-built data services | P2 |
| CSV/Excel upload | One-off analysis, user manually exported data | P1 |
| Database direct connection | User internal data warehouse | P3 |

### 6.3 Mode B Data Flow

```
User provides API Key / MCP Endpoint
         |
    +----+----+
    | Data    |  <- Standard interface: Auth/Rate limit/Cache
    | Adapter |
    | Layer   |
    +----+----+
         |
    +----+----+
    | Signal  |  <- External data -> Signal -> Merge with Mode A signals
    | Enhancement |
    | Layer   |  <- Gaps filled by external data auto-labeled "filled"
    +----+----+
         |
         v  Flow into Mosaic Assembly Layer (same pipeline as Mode A)
```

---

## 7. Example: How the Mosaic Theory Works

### Case: Assessing Tesla's Debt Servicing Capacity

**Five Fragments -- each insufficient alone:**

| Fragment | Signal | Problem Alone |
|---|---|---|
| Tesla 2028 bond yield tightened from 5.2% to 4.8% in Jan-Jun 2025 | Market sees risk decreasing | Could be general monetary easing |
| Tesla 2028 bond yield widened from 4.8% to 5.1% in Jul 2025 | Market starts repricing risk | Small move, could be noise |
| Tesla 2025 operating income fell 22% YoY in H1 2025 | Fundamentals significantly deteriorated | Loss could be one-time (Cybertruck ramp costs) |
| Tesla accounts receivable jumped 35% from Q1 to Q2 2025 | Collection capacity deteriorating | Could be seasonal timing |
| S&P maintains BBB-/Stable rating | Rating agency sees risk as manageable | Rating lag is a known issue |

**Assembled Complete Picture:**

```
Fragment 1 (spread tightening) + Fragment 2 (spread reversal) = Spread inflection signal (weak->moderate)
Fragment 2 (spread reversal) + Fragment 3 (profit decline) = Market starting to reflect fundamentals (upgrade)
Fragment 3 (profit decline) + Fragment 4 (AR jump) = Not just losses, but worsening collection (dual negative)
Fragment 5 (BBB- maintained) + Fragments 1-4 = Rating lag confirmed (rating signal unreliable)

Mosaic Conclusion:
Tesla's debt servicing capacity is deteriorating; market pricing (spread reversal) is beginning to reflect
this trend, but the BBB- rating still lags behind.

Information Completeness Assessment: Moderate
Gap: Tesla parent-level standalone financial data not fully separable from consolidated
-> Cannot precisely assess parent-level true debt servicing capacity
```

### Mosaic Assembly Process Demonstration

| Step | Operation | Result |
|---|---|---|
| 1 | Extract 5 raw signals | Each signal individually at L2-L4 confidence |
| 2 | Same-direction signal stacking | Spread first down then up -> inflection signal (L3->L4 upgrade) |
| 3 | Cross-dimension validation | Loss (L3) + AR jump (L3) = dual negative (L4 upgrade) |
| 4 | Contradiction handling | BBB- rating vs other 4 signals -> rating signal unreliable |
| 5 | Signal density calculation | 4 of 5 dimensions with available signals -> 80% (moderate-high) |
| 6 | Gap identification | Parent financial data missing -> affects L4 score confidence +/-1 |

---

## 8. Implementation Priorities

| Priority | Module | Description |
|---|---|---|
| **P0** | Signal Extraction Layer + Mosaic Assembly Layer | Foundation for all P0/P1/P2 analyses |
| **P0** | Completeness Assessment Layer | **Core differentiator** -- gap annotation engine |
| **P1** | Gap->Risk Mapping Table (industry-customized) | What risk each missing data type implies per industry |
| **P1** | Mode B: CSV Upload Adapter | Lowest-cost "external data" entry point |
| **P2** | Mode B: REST API Adapter | Bloomberg / Refinitiv professional terminals |
| **P3** | Mode B: MCP Adapter | User-built data services |

---

## Related Content

- [Engine Architecture Overview](engine-overview.md) -- Core philosophy, overall architecture, design principles
- [Industry Classification & Analysis Framework](industry-framework.md) -- 10-dimension scoring, industry types, pyramid specifications
- [Dual-Track Analysis Methodology](dual-track-methodology.md) -- Track A + Track B, cross-validation, rating mapping
