# Data Architecture

**Source**: Industry Cognitive Analysis Engine Methodology v0.1 · Mosaic Engine System Architecture Design v0.1 · SKILL.md v0.3.0  
**Date**: 2026-07-08  
**Nature**: Structured Archive — extracted and organized from existing specification and methodology documents

---

## 1. Design Principles

### 1.1 Hard Constraints (POC Phase)

| Constraint | Description |
|---|---|
| **Zero Bank Internal Data** | No access to bank core systems, customer transaction records, or internal ratings |
| **Zero Non-Public Data** | No use of any information requiring special permissions |
| **Zero Paid Data Sources** | Validation phase uses only free public data (paid terminals like Wind/Choice are only available as external access options in Mode B) |

### 1.2 Data Philosophy

| Principle | Meaning |
|---|---|
| **Mosaic Theory** | Individual public data fragments are meaningless on their own; pieced together they form a complete picture |
| **Information Completeness Theory** | Data gaps are not flaws — "we don't have this data" is itself a risk signal |
| **Substitution Priority Principle** | When precise data is unavailable, use publicly available proxy indicators, but must annotate accordingly |

---

## 2. Data Source Layering

### 2.1 Six-Layer Data Source Architecture

| Data Layer | Source | Acquisition Method | Reliability | Data Type | Update Frequency |
|---|---|---|---|---|---|
| **L1 Macro Policy** | State Council/NDRC/MIIT/NEA official websites | WebSearch + LLM Parsing | **High** (official releases) | Policy documents, notices, industry guidance catalogues | Irregular (weekly during policy-intensive periods) |
| **L2 Industry Data** | Industry associations (CPIA/SEMI, etc.), broker research abstracts, listed company annual reports | WebSearch + Public databases | **Medium-High** (associations sometimes lag) | Industry statistics, capacity data, price indices | Monthly/Quarterly |
| **L3 Supply Chain Pricing** | PVInfoLink/TrendForce/SMM free data | WebSearch | **Medium** (free version has delays) | Weekly/daily prices, supply-demand data | Weekly |
| **L4 Corporate Public Information** | National Enterprise Credit Information Publicity System, China Judgments Online, Enforcement Information Publicity Network, Cninfo | WebSearch + Designated website queries | **High** (official data) | Financial reports, judicial records, enforcement information, announcements | Continuous updates |
| **L5 Bidding & Tendering** | Local public resource trading centers, central enterprise procurement platforms | WebSearch | **High** (bid-winning announcements are public) | Centralized procurement results, bid quotes | Centralized procurement periods (quarterly) |
| **L6 Regional Economy** | Local statistics bureau yearbooks, industrial park management committee announcements | WebSearch | **Medium-High** | Economic data, park policies, employment data | Annual/Semi-annual |

### 2.2 Detailed Data Sources by Layer

#### L1 Macro Policy

| Subcategory | Specific Source | Acquisition Difficulty | Coverage |
|---|---|---|---|
| Industrial Policy | MIIT (miit.gov.cn), NDRC (ndrc.gov.cn) | Easy | Industry access, technology roadmap guidance, capacity regulation |
| Energy Policy | National Energy Administration (nea.gov.cn) | Easy | Electricity pricing policy, renewable energy, carbon emissions |
| Trade Policy | Ministry of Finance (mof.gov.cn), Ministry of Commerce (mofcom.gov.cn) | Easy | Import/export tariffs, export tax rebates, anti-dumping |
| Monetary Policy | People's Bank of China (pbc.gov.cn) | Easy | LPR/MLF, reserve requirement ratio changes, open market operations |
| Regional Policy | Provincial and municipal government websites | Medium | Local subsidies, industry funds, park policies |

#### L2 Industry Data

| Subcategory | Specific Source | Acquisition Difficulty | Coverage |
|---|---|---|---|
| Industry Statistics | CPIA (solar), SEMI (semiconductor), CAAM (automotive) | Medium | Capacity production, shipment volume, market share |
| Broker Research | Public research abstracts (free platforms) | Medium | Industry trends, company analysis, price forecasts |
| Listed Company Annual Reports | Cninfo (cninfo.com.cn) | Easy | Financial data, business segments, management discussion |
| Industry Price Indices | Various industry price tracking platforms | Medium | Product price trends, cost changes |

#### L3 Supply Chain Pricing

| Subcategory | Specific Source | Data Latency | Coverage |
|---|---|---|---|
| Solar Supply Chain | PVInfoLink (free version) | 1-2 weeks | Polysilicon/wafer/cell/module weekly quotes |
| Semiconductor Materials | TrendForce (free version) | 1-2 weeks | Memory chip/wafer foundry pricing |
| Metals/Raw Materials | SMM (Shanghai Metals Market) free version | 1-2 weeks | Lithium/cobalt/nickel/copper metal prices |
| Module Procurement Pricing | Central enterprise procurement platform bid announcements | Real-time | Actual transaction prices, price decline trends |

#### L4 Corporate Public Information

| Subcategory | Specific Source | Acquisition Difficulty | Coverage |
|---|---|---|---|
| Business Registration | National Enterprise Credit Information Publicity System (gsxt.gov.cn) | Easy | Basic info, shareholders, changes, administrative penalties |
| Judicial Records | China Judgments Online (wenshu.court.gov.cn) | Easy | Litigation, enforcement, bankruptcy cases |
| Enforcement Information | Enforcement Information Publicity Network (zxgk.court.gov.cn) | Easy | Judgment debtors, dishonest persons subject to enforcement, consumption restrictions |
| Listed Company Announcements | Cninfo (cninfo.com.cn) | Easy | Annual/quarterly reports, material events, prospectus |
| Bond Information | ChinaMoney (chinamoney.com.cn), SSE/SZSE | Easy | Issuance announcements, interest rates, rating changes |
| Bankruptcy Restructuring | National Enterprise Bankruptcy Restructuring Case Information Network (pccz.court.gov.cn) | Easy | Bankruptcy applications, administrator appointments, creditors' meetings |

#### L5 Bidding & Tendering

| Subcategory | Specific Source | Acquisition Difficulty | Coverage |
|---|---|---|---|
| Central Enterprise Procurement | Various central enterprise e-procurement platforms (Huaneng/Huadian/SPIC/Sanhe/CNNC/CGN/CHN Energy/ChinaCoal, etc.) | Easy | Solar modules/inverters, wind power equipment, energy storage systems |
| Public Resource Trading | Provincial and municipal public resource trading centers | Medium | Government projects, infrastructure, public service procurement |
| Bid Award Announcements | China Bidding and Tendering Public Service Platform (cebpubservice.com) | Medium | Various bidding results |

#### L6 Regional Economy

| Subcategory | Specific Source | Acquisition Difficulty | Coverage |
|---|---|---|---|
| Local Statistics | Provincial and municipal statistics bureau websites, statistical yearbooks | Medium | Regional GDP, industrial structure, fiscal revenue/expenditure |
| Industrial Parks | Various economic development zones/high-tech zones management committee announcements | Medium-High | Park policies, resident enterprises, output data |

---

## 3. Data Accessibility Verification Process

### 3.1 Four-Category Data Field Verification (Solar Industry, July 2026)

During the POC phase, four key data categories were actually captured and verified:

| Data Type | Test Content | Result | Sample |
|---|---|---|---|
| **Industrial Policy** | Solar policies 2025-2026 | ✅ Retrieved 6+ complete policy documents | Document No. 136 on electricity marketization pricing, Document No. 688 on green electricity direct connection notice, export tax rebate cancellation announcement |
| **Enterprise Risk** | Solar enterprise enforcement/dishonest/ bankruptcy records | ✅ Found 13 enterprises subject to enforcement | Yidao New Energy enforced over 1.5 billion; Aikang Technology enforced over 580 million; Quanwei Technology pre-restructuring |
| **Bidding & Tendering** | Central enterprise module procurement awards | ✅ Retrieved results from 6 central enterprises | Sanhe 2026 centralized procurement 10GW+; Longi shortlisted 50.3GW (85.3%) |
| **Supply Chain Pricing** | Polysilicon/wafer/cell/module weekly quotes | ✅ Retrieved July 2026 Week 1 data | TOPCon cell 0.275 RMB/W, weekly decline 5.17% |

### 3.2 Data Accessibility Verification Process

Before formal analysis of any industry, execute a four-step verification:

```
Step 1: Policy Data Accessibility
  ├── Search for the latest 2 years of national-level policy documents for the industry >= 3
  └── Conclusion: Policy data accessible / Policy data insufficient (marked as data gap)

Step 2: Enterprise Risk Data Accessibility
  ├── Search for enforcement/dishonest/bankruptcy records of major enterprises in the industry
  └── Conclusion: Risk data accessible / Risk data insufficient

Step 3: Industry Supply-Demand Data Accessibility
  ├── Search for price indices/capacity data/demand data for the industry
  └── Conclusion: Supply-demand data accessible / Only partially accessible

Step 4: Bidding & Tendering Data Accessibility
  ├── Search for central enterprise/government bidding results in the industry
  └── Conclusion: Bidding data accessible / Bidding data insufficient
```

### 3.3 Verification Conclusion

> **Zero data procurement cost in the POC phase is entirely feasible.** In July 2026, field verification of four data categories for the solar industry passed all tests. The public data coverage across six data layers is sufficient to support structured credit analysis.

---

## 4. Limitations of Public Data — Data Gap Types

### 4.1 Six Major Categories of Common Data Gaps

| Gap Type | Typical Missing Data | Frequency | Impact Level |
|---|---|---|---|
| **Competitive Data Gap** | Precise cost comparisons across enterprises, yield data, non-silicon costs | High | High — unable to precisely assess cost competitiveness |
| **Financial Data Gap** | Non-listed enterprises without public financial reports, incomplete parent company standalone statements | High | High — completely unable to assess financial health |
| **Market Pricing Gap** | Non-listed enterprises without stock/bond prices, Z-spread/OAS unavailable | Medium-High | Medium-High — Track B completely unavailable |
| **Covenant Data Gap** | Modified duration/convexity (requires Wind terminal), non-transparent key prospectus terms | Medium | Medium — YTM and term structure can be used as substitutes |
| **Liquidity Data Gap** | Bid-ask spread (not disclosed by Chinese exchanges), market maker list, best bid-offer depth | **Very High** (market structure limitation) | Medium — average daily volume + turnover rate can approximate |
| **Governance Data Gap** | Parent-subsidiary fund pooling agreements, related party transaction details, equity pledge specifics | Medium-High | High — governance deficiencies are a common cause of default |

### 4.2 Chinese Market-Specific Data Infrastructure Deficiencies

| Missing Item | Corresponding Mature Market | Impact | Alternative Solution |
|---|---|---|---|
| Bid-ask spread not disclosed | US TRACE system | Unable to assess real transaction costs | Average daily volume + turnover rate |
| CDS/CRMW product scarcity | US CDS market | Unable to hedge credit risk | No effective substitute (holding = bearing naked credit risk) |
| Market maker quotes not transparent | European MiFID II | Unable to judge market depth | Indirect inference from trading activity |
| Individual bond transaction price (not quote) access limited | US FINRA real-time data | Unable to do precise spread decomposition | Issuance rate + trend judgment |

### 4.3 Gap Types and Corresponding Industries

| Gap Type | Most Affected Industries | Specific Impact |
|---|---|---|
| Competitive Data Gap | Solar, semiconductor, new energy vehicles | Unable to precisely judge technology roadmap cost advantages |
| Financial Data Gap | Biomedical (unprofitable biotech), high-end equipment (non-listed) | Unable to use L4 financial verification layer |
| Market Pricing Gap | Non-listed enterprises, private bonds | Track B completely unavailable |
| Covenant Data Gap | All credit bonds | Unable to perform detailed interest rate risk analysis |
| Liquidity Data Gap | All credit bonds (common in Chinese market) | Unable to assess real transaction costs |
| Governance Data Gap | SOEs (multi-layer equity structure), private enterprises (related party transactions) | Unable to identify governance deficiencies like "subsidiary strong, parent weak" |

---

## 5. Gap to Risk Mapping Table

### 5.1 General Mapping Table

| Gap Type | Typical Missing Data | Corresponding Information Risk | Substitute Signal | Substitute Effectiveness |
|---|---|---|---|---|
| **Competitive Data Gap** | Precise cost comparison across enterprises | Overestimate or underestimate cost advantage | Central enterprise centralized procurement bid-winning prices (reflects market-accepted premium) | Medium-High — can be used for relative ranking |
| **Financial Data Gap** | Non-listed enterprises without public financial reports | Completely unable to assess financial health | Enforcement records, judicial disputes, recruitment dynamics, prospectus (if available) | Medium — requires multi-source cross-validation |
| **Market Pricing Gap** | Non-listed enterprises without stock/bond prices, Z-spread | Unable to perform Track B analysis | Public financing events, equity transfer prices, same-rating credit spreads | Medium — precision decreases but direction is correct |
| **Covenant Data Gap** | Modified duration/Z-spread (no Wind) | Unable to do detailed interest rate risk analysis | YTM approximation, same-rating credit spread comparison | Medium — cannot decompose but can rank |
| **Liquidity Data Gap** | Bid-ask spread not disclosed | Unable to assess real transaction costs | Average daily volume, turnover rate, abnormal trading events | Medium — activity can be assessed, costs cannot |
| **Governance Data Gap** | Fund pooling agreements, related party transaction details | Unable to identify hidden debt risks | Other receivables notes analysis, historical dividend records, parent company standalone statements | Medium-High — notes often reveal key information |

### 5.2 Solar Industry Custom Mapping Table

| Gap Type | Typical Missing Data | Substitute Signal | Substitute Effectiveness |
|---|---|---|---|
| Technology Data | Yield data by enterprise (not separately disclosed) | Module mass production efficiency + central enterprise centralized procurement shortlisting rate (indirect inference) | Medium — efficiency gap >1.5pct constitutes a sufficient distinguishing signal |
| Cost Data | Precise non-silicon cost comparison across technology routes | Central enterprise centralized procurement bid-winning price + integrated layout (indirect inference) | Medium — cannot precisely quantify but can qualitatively judge |
| Capacity Data | Capacity utilization by enterprise (industry estimates only) | Operating rate + product price trends (reverse inference) | Medium — estimated value, ±1.5 score range |
| Distributed Data | BC vs TOPCon actual power generation comparison in distributed scenarios | Third-party test data (limited, currently accumulating) | Low — no reliable substitute yet |

### 5.3 Gap Priority Assessment

| Priority | Gap Type | Criteria | Handling Method |
|---|---|---|---|
| **P0 Must Resolve** | Financial Data Gap | Completely unable to perform L4 verification | Use substitute signals, confidence level reduced to "Medium" or below |
| **P1 Significant Impact** | Competition/Governance/Market Pricing Gap | Key dimension score ±1.5 or more | Mark uncertainty interval |
| **P2 Has Substitute Solution** | Covenant/Liquidity Gap | Substitute signal effectiveness medium or above | Use substitute solution, annotate source |
| **P3 Market Limitation** | Bid-ask/CDS and other Chinese market infrastructure deficiencies | Not attributable to this system | Mark "Chinese market infrastructure deficiency" |

---

## 6. Mode B External Data Source Interface Contract

### 6.1 Architecture Design (Placeholder — Not Yet Implemented)

Mode B is the extensible data adaptation layer of the Mosaic Engine, allowing users to connect paid data terminals or internal data sources to fill Mode A gaps.

**Architecture**:
```
User Provides API Key / MCP Endpoint
         │
    ┌────┴────┐
    │ Data Adapter Layer│  ← Standardized interface definition
    │ Auth/Rate Limit/Cache │
    └────┬────┘
         │
    ┌────┴────┐
    │ Signal Enhancement Layer│  ← External data -> Signal -> Fusion with Mode A signals
    │ Gap Filling  │  ← Gaps filled by external data are automatically marked as "filled"
    └────┬────┘
         │
         ↓ Merged into Mosaic Mosaic Layer
```

### 6.2 Standardized Interface Definition

```yaml
DataSourceAdapter:
  # Lifecycle
  init(config):
    # Authentication, rate limiting configuration
    # config.auth_type: "api_key" | "oauth" | "basic"
    # config.rate_limit: requests/minute
    # config.cache_ttl: seconds

  health_check():
    # Returns availability status
    # Return value: { status: "ok" | "degraded" | "down", latency_ms: int }

  # Core Query Interfaces

  query_bond_analytics(bond_code, fields):
    # bond_code: str — Bond code (e.g., "113044.SH")
    # fields: list — ["ytm", "duration", "convexity", "z_spread", "oas", "bid_ask"]
    # Returns: { field: value, data_timestamp: "YYYY-MM-DD" }

  query_market_data(instrument_code, data_type, date_range):
    # instrument_code: str — Instrument code
    # data_type: "price_history" | "volume" | "volatility" | "fund_flow"
    # date_range: { start: "YYYY-MM-DD", end: "YYYY-MM-DD" }
    # Returns: [{ date, value, source }, ...]

  query_industry_benchmark(industry, metric, date):
    # industry: str — Industry name (e.g., "solar")
    # metric: "credit_spread" | "default_rate" | "rating_migration"
    # date: "YYYY-MM-DD"
    # Returns: { value: float, benchmark_source: str, date: "YYYY-MM-DD" }

  # Signal Fusion

  to_signals():
    # Converts external data into unified signal object format
    # Returns: signal object list (format equivalent to Mode A signal objects)
```

### 6.3 Supported Data Types and Fields

| Data Type | Fields | Purpose |
|---|---|---|
| **Bond Analytics** | YTM, Modified Duration, Convexity, Z-spread, OAS | Fill covenant data gap (M1.1 Relative Value) |
| **Market Depth** | Bid-ask spread, market maker quotes, best bid-offer levels | Fill liquidity data gap (M1.3 Liquidity) |
| **Market Data** | Price history, volume, volatility, fund flows | Enhance Track B market pricing signals |
| **Industry Benchmark** | Credit spread curve, industry default rate, rating migration matrix | Enhance M1.1 Relative Value comparison |

### 6.4 Supported Access Methods (Planned)

| Access Method | Applicable Scenario | Priority | Implementation Complexity |
|---|---|---|---|
| CSV/Excel Upload | One-off analysis, user manually exports data | **P1** | Low |
| REST API | Wind/Choice/Flush and other financial terminal APIs | **P1** | Medium |
| MCP Server | User-built data service | **P2** | High |
| Direct Database Connection | User internal data warehouse | **P3** | High |

---

## 7. Data Compliance Boundaries

### 7.1 Three Data Categories: Permitted, Requires Authorization, Prohibited

| Category | Scope | Compliance Requirements | Examples |
|---|---|---|---|
| **✅ Freely Usable** | Government publicly released information, listed company/bond issuer announcements, exchange public data, judicial authority public documents | No authorization required, just annotate source | MIIT policy documents, Cninfo announcements, China Judgments Online rulings |
| **⚠️ Requires Authorization** | Financial terminal API data, paid research reports, industry association internal data | Must sign data usage agreement or purchase subscription | Wind/Choice data terminals, CPIA member data, broker in-depth research reports |
| **❌ Not Permitted** | Bank internal data, corporate non-public financial data, personal privacy information, data obtained through improper means | Absolutely prohibited | Internal ratings, customer transaction records, executive personal credit reports, unauthorized crawler data |

### 7.2 Boundary Use Cases

| Scenario | Compliant | Explanation |
|---|---|---|
| Scraping public policy documents from government websites | ✅ | Government information is in the public domain |
| Crawling judgments from China Judgments Online | ✅ | Judicial openness is a legal principle |
| Obtaining listed company announcements from Cninfo | ✅ | Listed company information disclosure is a legal obligation |
| Obtaining bid award announcements from central enterprise procurement platforms | ✅ | Bidding results must be publicly disclosed by law |
| Using Wind/Choice API (with purchased subscription) | ✅ | Use within authorized scope |
| Obtaining enterprise balance sheets from non-public channels | ❌ | Without enterprise authorization |
| Scraping websites explicitly prohibited by robots.txt | ⚠️ | Must comply with website robots.txt agreement |
| Using internally disclosed corporate information posted by individuals on social media | ⚠️ | Involves personal information protection, requires careful handling |

### 7.3 Data Usage Disclaimer Key Points

1. **Not Investment Advice**: Engine output is structured analysis, not investment advice
2. **Public Data Reliance**: All conclusions are based on information publicly available at the time of analysis
3. **Gaps Do Not Constitute Misrepresentation**: Dimensions marked as data gaps do not represent "absence of risk"
4. **Substitute Signal Precision**: The precision of substitute signals is lower than precise data, users should be aware
5. **Laws and Regulations**: Users must comply with laws and regulations of the jurisdiction where data is obtained

### 7.4 Data Source Annotation Standards

Each analysis output must include:
1. Data source URL for each key signal
2. Publication time of the information (not scrape time)
3. Reliability rating (High/Medium-High/Medium/Medium-Low/Low)
4. Whether it is a substitute signal (if so, annotate the original gap)
5. Timing disclaimer — "This analysis is based solely on information publicly available prior to [YYYY-MM-DD]"
