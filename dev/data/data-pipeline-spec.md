# Data Pipeline Interface Specification · Fixed Income Credit Analysis Engine Mode A Mosaic Engine

**Version**: v0.1 | **Date**: 2026-07-09
**Nature**: Interface Contract Document — Defines standardized interfaces for the data collection layer, signal extraction layer, and report generation layer
**Status**: Draft — Sections supported by existing methodology documents are annotated

---

## Table of Contents

1. [Overall Architecture](#1-overall-architecture)
2. [Data Collection Layer (Input Adapter)](#2-data-collection-layer-input-adapter)
3. [Signal Extraction Layer (Signal Extractor)](#3-signal-extraction-layer-signal-extractor)
4. [Report Generation Layer (Report Generator)](#4-report-generation-layer-report-generator)
5. [Data Flow Timing](#5-data-flow-timing)
6. [Public Data Source List](#6-public-data-source-list)
7. [Priorities and Dependencies](#7-priorities-and-dependencies)
8. [Error Handling and Edge Cases](#8-error-handling-and-edge-cases)
9. [Appendix: Mapping with Existing Design Documents](#9-appendix-mapping-with-existing-design-documents)

---

## 1. Overall Architecture

### 1.1 Five-Layer Pipeline

```
                +------------+
                │  User Input │
                │ Industry+Company │
                +------+-----+
                       │
                       ▼
          ┌──────────────────────┐
          │  1. Data Collection Layer│  ← New Engineering
          │  Input Adapter       │
          │  Mode A: WebSearch   │
          │  Mode B: External Data Source│  (Interface defined, future implementation)
          └──────────┬───────────┘
                     │ RawData[]
                     ▼
          ┌──────────────────────┐
          │  2. Signal Extraction Layer│  ← New Engineering
          │  Signal Extractor    │
          │  Unstructured -> Structured│
          └──────────┬───────────┘
                     │ Signal[]
                     ▼
          ┌──────────────────────┐
          │  3. Mosaic Assembly Layer  │  ← Existing Design
          │  Mosaic Engine       │  (mosaic-engine.md Section 4)
          │  Signal Overlay/Cross-Validation│
          │  Completeness Assessment│
          └──────────┬───────────┘
                     │ MosaicResult
                     ▼
          ┌──────────────────────┐
          │  4. Analysis Engine Layer │  ← Existing Design
          │  Analysis Engine     │  (analysis-engine-methodology.md)
          │  Pyramid Scoring/Rating Mapping│
          └──────────┬───────────┘
                     │ AnalysisResult
                     ▼
          ┌──────────────────────┐
          │  5. Report Generation Layer│  ← New Engineering
          │  Report Generator    │
          │  Result -> HTML Report│
          └──────────────────────┘
```

### 1.2 Layer Responsibilities

| Layer | Responsibility | Input | Output | Current Status |
|---|---|---|---|---|
| 1. Data Collection Layer | Obtain raw data from multiple sources | `(industry, company)` | `RawData[]` | **Completely Blank** — Currently relies on manual WebSearch |
| 2. Signal Extraction Layer | Unstructured -> Structured signal conversion | `RawData[]` | `Signal[]` | **Completely Blank** — Currently relies on LLM ad-hoc prompts |
| 3. Mosaic Assembly Layer | Signal aggregation/cross-validation/completeness | `Signal[]` | `MosaicResult` | **Full Design Existing** — mosaic-engine.md Sections 3-5 |
| 4. Analysis Engine Layer | Pyramid scoring/rating mapping | `MosaicResult` | `AnalysisResult` | **Full Design Existing** — analysis-engine-methodology.md Sections 4-6 |
| 5. Report Generation Layer | Result -> HTML rendering | `AnalysisResult` | `HTML file` | **Partially Blank** — Templates designed, rendering logic not engineered |

### 1.3 Key Design Principles

1. **Data Layer No Judgment**: The data collection layer only performs retrieval and structuring, no credit judgment
2. **Interface Contract First**: Each layer defines strict input/output interfaces, supporting independent development
3. **Parallel Fetching**: The data collection layer initiates requests to multiple data sources simultaneously, aggregates and delivers uniformly
4. **Honest Marking**: Data must never be tampered with or fabricated; missing information must be explicitly marked
5. **Backward Compatibility**: New data source types must not break existing pipelines

---

## 2. Data Collection Layer (Input Adapter)

### 2.1 Overview

**Current Status**: **Completely Blank**. All data collection is currently done through manual WebSearch, with no standardized interface.

**Responsibilities**:
- Receive `(industry, company)` input
- Automatically determine the data layers to collect based on input (policy/enterprise/industry/market)
- Initiate multiple data collection tasks per layer in parallel
- Aggregate raw data and pass to the signal extraction layer

**Core Interface**:

```yaml
InputAdapter:
  # ── Entry Point ──
  collect(industry: string, company: string, options?: CollectOptions):
    # Main entry: collect from all data sources in parallel
    # Returns: CollectResult

  # ── Internal Interfaces (can be called independently) ──
  collect_policy(industry: string): PolicyDoc[]
    # Collect industrial policy data

  collect_enterprise(company: string): EnterpriseProfile
    # Collect enterprise public data

  collect_industry_data(industry: string): IndustryData[]
    # Collect industry/market data

  collect_market_pricing(company: string): MarketData[]
    # Collect market pricing data

  # ── Lifecycle ──
  validate_source(name: string): SourceStatus
    # Check whether a data source is reachable

  # ── Events ──
  on_source_complete(source_name: string): void
    # Triggered when a single data source collection completes
  on_all_complete(): void
    # Triggered when all data sources have completed collection
  on_source_error(source_name: string, error: Error): void
    # Triggered when a single data source collection fails
```

**Error Handling**:

```yaml
CollectError:
  type: "source_unreachable" | "parse_failed" | "rate_limited" | "timeout" | "empty_result"
  source: string          # Name of the problematic data source
  detail: string          # Error details
  recoverable: boolean    # Whether retryable
  retry_after?: int       # Recommended retry wait time (seconds)

  # Error Handling Strategy:
  # - Non-critical source (e.g., a particular industry data source) failure -> Log error, continue with other sources
  # - Critical source (e.g., enterprise registration info) failure -> Entire collection fails, return error upstream
  # - All sources return empty -> Return "no_data" error
```

### 2.2 Mode A: Public Data Source Adapter (Current Implementation)

```yaml
PublicDataSource:
  # ═══════════════════════════════════════════
  # A1 — Policy Data Source Adapter
  # ═══════════════════════════════════════════
  - name: "web_search_policy"
    description: "Keyword search -> Search strategy template -> Result list"
    method: >
      1. Load search keyword template based on industry
      2. Initiate queries to multiple search strategies in parallel
      3. Filter for .gov/.org and other high-reliability sources
      4. Sort by relevance and time
    input:
      industry: string        # e.g., "solar"
      keywords: string[]       # Auto-generated keyword list
      time_range: string       # "1y" | "2y" | "all"
    output: SearchResult[]
    output_structure:
      SearchResult:
        url: string
        title: string
        snippet: string
        source: string         # Domain
        publish_date: datetime
        relevance_score: 0-1
        content_type: "policy_document" | "regulation" | "notice" | "industry_plan"
    error:
      - "no_results": Search returned no results -> Mark as data gap
      - "rate_limited": Search rate limited -> Wait and retry (max 3 times)
    # Supported by existing methodology documents: data-architecture.md L1 layer, mosaic-engine.md Section 7

  # ═══════════════════════════════════════════
  # A2 — Enterprise Data Source Adapter
  # ═══════════════════════════════════════════
  - name: "web_search_enterprise"
    description: "Company name -> Multi-source aggregation of registration/judicial/enforcement/bidding"
    method: >
      1. Initiate search by full company name + aliases
      2. Identify and classify result types (registration/judicial/bidding/news)
      3. Extract structured info from GSXT/wenshu/zxgk and other target sites
      4. Multi-source deduplication and merging
    input:
      company: string          # Full company name
      aliases?: string[]       # Former names/abbreviations
    output: EnterpriseProfile
    output_structure:
      EnterpriseProfile:
        basic:
          name: string
          unified_social_credit_code: string
          registered_capital: string
          legal_representative: string
          establishment_date: datetime
          status: "active" | "revoked" | "cancelled" | "bankruptcy"
        risk_records:
          enforcement_records: EnforcementRecord[]
          dishonest_persons: DishonestPerson[]
          litigation_records: LitigationRecord[]
          admin_penalties: AdminPenalty[]
          bankruptcy_info?: BankruptcyInfo
        bidding_records:
          won_bids: BidRecord[]
          win_rate: float
          major_customers: string[]
        news_and_events:
          news: NewsItem[]
          financing_events: FinancingEvent[]
          major_announcements: Announcement[]
    error:
      - "company_not_found": Company name cannot be matched -> Return search suggestions
      - "partial_data": Some data sources unavailable -> Return available data + gap annotations
    # Supported by existing methodology documents: data-architecture.md L4-L5 layers

  # ═══════════════════════════════════════════
  # A3 — Industry Data Source Adapter
  # ═══════════════════════════════════════════
  - name: "web_search_industry"
    description: "Industry name -> Multi-source aggregation of industry statistics/prices/reports"
    method: >
      1. Load data template based on industry (price indices, production, installed capacity, etc.)
      2. Search from CPIA/SEMI/broker reports and other sources
      3. Identify timestamps and units of data points
      4. Align multi-source data for the same indicator
    input:
      industry: string         # e.g., "solar"
      data_categories: string[]  # ["price", "capacity", "demand", "policy_impact"]
      time_range: string       # "6m" | "1y" | "3y"
    output: IndustryData[]
    output_structure:
      IndustryData:
        category: string       # "price_index" | "capacity" | "shipment" | "utilization_rate"
        series_name: string    # "TOPCon cell price" | "polysilicon production"
        data_points: DataPoint[]
          - date: datetime
            value: float
            unit: string
            source: string
            data_quality: "official" | "estimated" | "inferred"
    error:
      - "insufficient_data": Insufficient public data for this industry -> Return all available data + gap marker
    # Supported by existing methodology documents: data-architecture.md L2-L3 layers, four-category data verification

  # ═══════════════════════════════════════════
  # A4 — Market Pricing Data Source Adapter
  # ═══════════════════════════════════════════
  - name: "web_search_market"
    description: "Company/industry -> Public market pricing signals"
    method: >
      1. Search for publicly traded corporate bond/stock information
      2. Obtain interest rates and credit spread data from ChinaMoney/exchanges/ChinaBond Valuation
      3. Aggregate search results into structured signals
    input:
      company: string
      bond_codes?: string[]    # Known bond codes
      market_type: "bond" | "stock" | "both"
    output: MarketData[]
    output_structure:
      MarketData:
        instrument_type: "bond" | "stock"
        code?: string
        name: string
        data_type: "ytm" | "spread" | "volume" | "rating"
        data_points: DataPoint[]
          - date: datetime
            value: float
            source: string
        # Note: Chinese market bid-ask spread is not disclosed -> Mark as "structural deficiency"
    error:
      - "no_public_pricing": Non-listed company or bonds without public quotes -> Normal gap
    # Supported by existing methodology documents: data-architecture.md Section 4, mosaic-engine.md Section 5.2
```

### 2.3 Mode B: External Data Source Adapter (Future Implementation)

```yaml
ExternalDataSource:
  description: >
    Mode B is the extensible data adaptation layer of the Mosaic Engine, allowing users to
    connect paid data terminals or internal data sources to fill Mode A gaps.
    Interface definition is complete (see mosaic-engine.md Section 6 and data-architecture.md Section 6),
    this is only a summary reference.

  # ── Adapter Contract (full version see mosaic-engine.md Section 6.1) ──
  DataSourceAdapter:
    # Lifecycle
    init(config):
      # config.auth_type: "api_key" | "oauth" | "basic"
      # config.rate_limit: requests/minute
      # config.cache_ttl: seconds

    health_check():
      # Returns: { status: "ok" | "degraded" | "down", latency_ms: int }

    # Core Queries
    query_bond_analytics(bond_code, fields):
      # fields: ["ytm","duration","convexity","z_spread","oas","bid_ask"]
      # Returns: { field: value, data_timestamp: string }

    query_market_data(instrument_code, data_type, date_range):
      # data_type: "price_history" | "volume" | "volatility" | "fund_flow"

    query_industry_benchmark(industry, metric, date):
      # metric: "credit_spread" | "default_rate" | "rating_migration"

    to_signals():
      # Converts external data to unified signal object format

  # ── Supported Access Methods (Planned) ──
  connection_methods:
    - type: "csv_upload"
      priority: P1
      scenario: "One-off analysis, user manually exports data"

    - type: "rest_api"
      priority: P1
      scenario: "Wind/Choice/Flush and other financial terminal APIs"
      examples:
        - "Wind API"
        - "Choice API"
        - "ChinaBond Valuation API"

    - type: "mcp_server"
      priority: P2
      scenario: "User-built data service"
      protocol: "MCP (Model Context Protocol)"

    - type: "database"
      priority: P3
      scenario: "User internal data warehouse"

  # Current Status: Interface defined (contract complete), but no implementation
```

### 2.4 Data Collection Strategy

```yaml
CollectStrategy:
  # ── Search Keyword Templates (loaded by industry) ──
  keyword_templates:
    policy:
      industry: "industry"     # Replaced with actual industry name
      templates:
        - "{industry} policy {year}"
        - "{industry} NDRC latest regulations"
        - "{industry} industry guidance catalogue"
        - "{industry} subsidy phase-out"
    enterprise:
      company: "company"       # Replaced with actual company name
      templates:
        - "{company} business registration"
        - "{company} judgment debtor"
        - "{company} court documents"
        - "{company} bidding"
        - "{company} announcements"
    industry:
      - "{industry} production {year}"
      - "{industry} price latest"
      - "{industry} market size"
      - "{industry} installed capacity"

  # ── Parallel Strategy ──
  concurrency:
    max_parallel_sources: 4       # Query up to 4 data sources simultaneously
    source_timeout: 30000          # Single source timeout 30s
    total_timeout: 120000          # Total timeout 120s
    retry_count: 3                 # Failure retry count
    retry_backoff: "exponential"   # Exponential backoff

  # ── Cache Strategy ──
  cache:
    policy_data: 86400             # Policy data cache 24 hours
    enterprise_data: 3600          # Enterprise data cache 1 hour
    market_data: 300               # Market data cache 5 minutes
    industry_data: 86400           # Industry data cache 24 hours

  # ── Data Quality Annotation ──
  DataQuality:
    - level: "official"
      description: "Officially released, precise data"
      examples: ["government announcements", "exchange data", "court judgments"]
      confidence_modifier: 0       # No impact on signal confidence

    - level: "reported"
      description: "Reliable media reports or summaries"
      examples: ["broker research abstracts", "industry media reports"]
      confidence_modifier: -1      # Signal confidence reduced by one level

    - level: "estimated"
      description: "Estimated or inferred data"
      examples: ["industry estimates", "multi-source inference"]
      confidence_modifier: -2      # Signal confidence reduced by two levels

    - level: "inferred"
      description: "Derived from fragmented data"
      examples: ["inferring production from bidding results", "inferring supply-demand from price trends"]
      confidence_modifier: -3      # Signal confidence reduced by three levels
```

---

## 3. Signal Extraction Layer (Signal Extractor)

### 3.1 Overview

**Current Status**: **Completely Blank**. Current signal extraction is done through ad-hoc LLM prompts, with no standardized interface, no cache, and no quality monitoring.

**Responsibilities**:
- Convert unstructured/semi-structured data returned by the data collection layer into unified signal objects
- Each signal annotated with source URL, timestamp, dimension, direction, strength, confidence
- No judgment, only structuring (see mosaic-engine.md Section 3.3)
- Maximum 3 signals extracted per raw data item (to prevent LLM over-generation)

**Core Interface**:

```yaml
SignalExtractor:
  # ── Main Entry ──
  extract(raw_data: RawData[], industry: string, company: string):
    # Converts a batch of raw data into structured signals
    # Returns: ExtractResult

  # ── Type-Specific Extractors ──
  extract_from_search_results(results: SearchResult[]): Signal[]
    # Extract signals from search results (title + snippet + URL)

  extract_from_policy_doc(doc: PolicyDoc): Signal[]
    # Extract signals from full policy text (requires LLM full-text understanding)

  extract_from_enterprise_profile(profile: EnterpriseProfile): Signal[]
    # Extract signals from enterprise profile (business/judicial/bidding structured data -> signals)

  extract_from_industry_data(data: IndustryData[]): Signal[]
    # Extract trend signals from industry data series

  extract_from_market_data(data: MarketData[]): Signal[]
    # Extract signals from market pricing data

  # ── Metadata ──
  get_extraction_stats(session_id: string): ExtractionStats
    # Get extraction statistics (signal count/source count/average confidence/duration)

  # ── Events ──
  on_signal_extracted(signal: Signal): void
  on_extraction_complete(result: ExtractResult): void
  on_extraction_error(source_id: string, error: Error): void
```

### 3.2 Signal Object Data Structure

```yaml
Signal:
  # ── Identification Fields ──
  id: string                     # Format: "sig_{timestamp}_{uuid_short}"
  session_id: string             # Collection session ID
  source_url: string             # Specific data source URL
  source_type: string            # "policy_document" | "court_record" | "bidding_result"
                                 # | "industry_report" | "news" | "enterprise_db"
                                 # | "financial_statement" | "market_data" | "rating_event"
  source_data_quality: string    # "official" | "reported" | "estimated" | "inferred"

  # ── Time Fields ──
  published_at: datetime         # Information source publication time (not collection time)
  extracted_at: datetime         # Signal extraction time
  effective_at: datetime         # Signal effective time (time corresponding to data point)

  # ── Content Fields ──
  dimension: string              # "L1_policy" | "L2_technology" | "L3_supply_chain"
                                 # | "L4_financial" | "track_b"
  sub_dimension: string          # Subcategory within dimension (corresponding to industry pyramid structure)
  content: string                # Signal text (concise, factual)
  summary: string                # One-sentence summary (for report display)

  # ── Signal Strength ──
  direction: string              # "positive" | "negative" | "neutral"
  strength: int                  # 1-5
  # 1 = Directional weak signal (direction only, no magnitude)
  # 2 = Directional medium signal (direction + qualitative description)
  # 3 = Directional strong signal (direction + rough magnitude)
  # 4 = Quantitative signal (precise numerical comparison)
  # 5 = Definitive signal (precise value + authoritative source)

  # ── Confidence (initial value, may be upgraded after entering mosaic layer) ──
  confidence: string             # "L5_cross_validated" | "L4_direct"
                                 # | "L3_inferred" | "L2_weak" | "L1_gap"
  # L5 = Multi-source cross-validated (>=2 independent sources confirming the same fact)
  # L4 = Single source direct signal (one reliable source clearly stated)
  # L3 = Derived inference (inferred from multiple fragments combined)
  # L2 = Directional weak signal (direction only, no magnitude)
  # L1 = Missing signal (gap)

  # ── Association Fields ──
  related_signals: string[]      # Related signal ID list (for mosaic association)
  tags: string[]                 # Free tags (for filtering and aggregation)

  # ── Verification Fields ──
  extraction_method: string      # "llm_extract" | "rule_parse" | "direct_transform"
  human_verified: boolean        # Whether manually verified (default false)

  # ── Conflict Management ──
  conflicts_with: string[]       # If conflicting with other signals, record conflicting signal IDs
  is_contradicted: boolean       # Whether contradicted by other signals
```

### 3.3 Extraction Rules

```yaml
ExtractionRules:
  # ── Quantity Limits ──
  max_signals_per_source: 3     # Maximum 3 signals per source data item
  max_signals_per_session: 200  # Maximum 200 signals per analysis round
  min_content_length: 10        # Minimum signal text length
  max_content_length: 200       # Maximum signal text length

  # ── Quality Rules ──
  rules:
    - name: "fact_only"
      description: "Extract only factual content, no judgments"
      example:
        - NOT_OK: "LONGi Green Energy has leading technology"  # This is a judgment, not fact
        - OK: "LONGi BC cell mass production efficiency reached 24.8%"  # This is fact

    - name: "source_required"
      description: "Must link to a specific data source URL"
      example:
        - NOT_OK: "Industry competition intensifying"  # No source
        - OK: "Module prices dropped from 0.38 RMB/W to 0.24 RMB/W (Source: PVInfoLink July 2026 Week 1 Weekly Report)"

    - name: "time_required"
      description: "Must annotate data time point"
      example:
        - NOT_OK: "Enterprise enforcement record"  # No time
        - OK: "New enforcement record in June 2026, subject amount 120 million"

    - name: "no_duplicate"
      description: "Same fact from same source extracted only once"
      dedup_window: 3600  # Deduplicate same source same content within 1 hour

  # ── Dimension Mapping Rules ──
  dimension_mapping:
    # Default mapping from source_type to dimension (can be overridden by industry template)
    policy_document: "L1_policy"
    court_record: "L4_financial"  # Judicial records mapped to financial risk
    bidding_result: "L2_technology"  # Bidding mapped to competitive position
    industry_report: "L2_technology"
    news: "L1_policy" | "L3_supply_chain"  # Depending on content
    financial_statement: "L4_financial"
    market_data: "track_b"
    rating_event: "track_b"

  # ── Strength Mapping Rules ──
  strength_mapping:
    - condition: "Contains precise value + comparative relationship"
      examples: ["efficiency gap 1.5pct", "debt ratio 86.89%", "increase 13%"]
      strength: 5

    - condition: "Contains precise value"
      examples: ["cell efficiency 24.8%", "bid 52GW", "loss 9.5 billion"]
      strength: 4

    - condition: "Contains qualitative description + comparison"
      examples: ["significantly ahead of peers", "marked deterioration", "above industry average"]
      strength: 3

    - condition: "Contains qualitative description"
      examples: ["insufficient capacity", "divergent technology roadmaps", "declining market share"]
      strength: 2

    - condition: "Direction only"
      examples: ["policy support", "intense competition", "increasing risk"]
      strength: 1
```

### 3.4 LLM Extraction Prompt Framework

```yaml
LLMPromptFramework:
  description: >
    The signal extraction layer relies on LLM for structured conversion of unstructured text.
    The following defines standardized prompt templates to ensure consistent output format across extraction nodes.

  system_prompt_template: |
    You are a signal extractor for a credit analysis engine. Your task is to extract structured credit signals from given text.

    Rules:
    1. Extract only facts — no judgments, no speculation
    2. Each signal must have a clear data source
    3. Each signal must have time information (if no specific date, use the document date)
    4. Each signal annotates its dimension (L1 policy/L2 technology/L3 supply chain/L4 financial/track_b market)
    5. Quantity limit: maximum 3 signals per source data item
    6. If the text contains no usable credit signals, return an empty list
    7. Do not fabricate — only extract when the text explicitly contains the information
    8. Normalize numerical values, times, and entities in unstructured text

    Output format:
    [
      {
        "content": "Signal text (concise, within 200 characters)",
        "summary": "One-sentence summary (within 30 characters)",
        "dimension": "L1_policy",
        "sub_dimension": "Electricity pricing policy",
        "direction": "positive" | "negative" | "neutral",
        "strength": 1-5,
        "published_at": "YYYY-MM-DD",
        "source_url": "URL",
        "source_type": "policy_document" | "court_record" | "bidding_result" | "industry_report" | "news"
      }
    ]

  context_template: |
    Industry: {industry}
    Company: {company}
    Analysis Date: {analysis_date}
    Context: {additional_context}

    Raw Text:
    {raw_text}

    Please extract structured signals.
```

### 3.5 Error Handling

```yaml
SignalExtractorError:
  type: "llm_failure" | "parse_failure" | "empty_result" | "quality_check_failed"
  source_id: string          # Problematic source data ID
  detail: string
  recoverable: boolean

  # Error Handling Strategy:
  # - llm_failure (LLM call failed) -> Retry 2 times, exponential backoff
  # - parse_failure (LLM returned unparseable format) -> Retry 1 time, add format constraints
  # - empty_result (LLM returned empty signal list) -> Normal, record "no signal extracted from this source"
  # - quality_check_failed (extraction result fails quality rules) -> Discard, record reason
  # - Single source extraction failure -> Does not affect other sources
```

### 3.6 Extraction Result Aggregation

```yaml
ExtractResult:
  session_id: string
  signals: Signal[]
  stats: ExtractionStats
  errors: SignalExtractorError[]

ExtractionStats:
  total_raw_sources: int         # Number of input raw data sources
  total_signals: int             # Total number of extracted signals
  avg_confidence: string         # Average confidence
  distribution:
    L1_gap: int                  # Signal count per confidence level
    L2_weak: int
    L3_inferred: int
    L4_direct: int
    L5_cross_validated: int
  by_dimension:
    L1_policy: int
    L2_technology: int
    L3_supply_chain: int
    L4_financial: int
    track_b: int
  extraction_duration_ms: int    # Extraction duration
  failed_sources: int            # Number of failed sources

  # Statistical output example:
  # total_signals: 37
  # avg_confidence: "L3_inferred"
  # distribution: { L1: 2, L2: 8, L3: 15, L4: 10, L5: 2 }
  # by_dimension: { L1: 12, L2: 8, L3: 5, L4: 7, track_b: 5 }
```

---

## 4. Report Generation Layer (Report Generator)

### 4.1 Overview

**Current Status**: **Partially Blank**. HTML/CSS design for 12 report templates is complete (`report-style-system.md`), but systematic rendering logic from analysis results to HTML is not implemented. Current reports are generated by manually writing HTML.

**Responsibilities**:
- Receive structured results output by the analysis engine
- Select the corresponding template based on the specified report type
- Inject data into the template and render as a complete HTML file
- Handle fixed structures such as report header/footer/metadata
- Handle multi-language (primarily Chinese) and number formatting

**Core Interface**:

```yaml
ReportGenerator:
  # ── Main Entry ──
  render(result: AnalysisResult, options: RenderOptions):
    # Renders analysis result to HTML
    # Returns: RenderResult (includes rendered HTML content and metadata)

  # ── Independent Rendering Methods ──
  render_hero(result: AnalysisResult): string
    # Render HERO area (title + metadata)

  render_strip(result: AnalysisResult): string
    # Render top bar number strip

  render_section(layer_score: LayerScore, signals: Signal[]): string
    # Render analysis section for a single layer

  render_signal_table(signals: Signal[]): string
    # Render signal list table

  render_completeness(mosaic_result: MosaicResult): string
    # Render completeness report

  render_risk_signals(risk_signals: RiskSignal[]): string
    # Render risk signal list

  # ── Helper Methods ──
  format_value(value: float, format_spec: string): string
    # Format numerical values (thousands separator, decimal places, percentage, etc.)
  format_date(date: datetime, format_spec: string): string
    # Format date
  resolve_template_path(template_type: string): string
    # Resolve template file path

  # ── Events ──
  on_before_render(result: AnalysisResult, options: RenderOptions): void
  on_after_render(html: string, file_path: string): void
  on_render_error(error: RenderError): void
```

### 4.2 Render Options

```yaml
RenderOptions:
  # ── Report Type (select from 12 types) ──
  template_type: string
  # "type1" — Single entity deep analysis (P0)
  # "type2" — Dual entity forward-looking comparison (P1+)
  # "type3" — Black swan retrospective verification (P1+)
  # "type4" — Multi-identity parallel assessment (P1+)
  # "type5" — Bond investment dashboard (P0)
  # "type6" — Mosaic completeness report (P0)
  # "type7" — Industry methodology page (P1+)
  # "type8" — Bond LGD assessment (P1+)
  # "type9" — External support special assessment (P1+)
  # "type10" — ESG+governance risk scan (P1+)
  # "type11" — Stress test report (P1+)
  # "type12" — Engine validation statistics (P2+)

  # ── Report Information ──
  report_title: string          # Report title (e.g., "LONGi Green Energy Credit Analysis Report")
  report_subtitle?: string      # Subtitle
  analyst?: string              # Analyst (optional)
  analysis_date: datetime       # Analysis date

  # ── Display Options ──
  language: string              # "zh" | "en" (default is zh)
  show_completeness: boolean    # Whether to show completeness report (default true)
  show_signals: boolean         # Whether to show complete signal list (default false)
  show_gaps: boolean            # Whether to show data gaps (default true)
  compact_mode: boolean         # Compact mode (suitable for printing, default false)

  # ── Output ──
  output_path?: string          # Output file path (returns HTML string if not specified)
  include_css: boolean          # Whether to inline CSS (default true, false for standalone file)
  minify: boolean               # Whether to minify HTML (default false)

  # ── Advanced Options ──
  custom_css_path?: string      # Custom CSS override
  custom_header?: string        # Custom header HTML
  custom_footer?: string        # Custom footer HTML
  watermark_text?: string       # Watermark text (e.g., "draft")
```

### 4.3 Analysis Result Data Structure

```yaml
AnalysisResult:
  description: >
    Final output of the analysis engine. Contains scores, signals, completeness, cross-comparison, etc.
    This is the input for the report generation layer.

  # ── Identification ──
  industry: string              # Industry name
  company: string               # Company name
  analysis_date: datetime       # Analysis date
  engine_version: string        # Engine version number

  # ── Composite Scores ──
  scores:                       # Scores per layer
    L1_policy: float            # Policy environment (0-10)
    L2_technology: float        # Technology/competition (0-10)
    L3_supply_chain: float      # Supply chain (0-10)
    L4_financial: float         # Financial/debt service (0-10)
    track_b: float              # Market pricing (0-10, optional)

  composite_score: float        # Composite score (0-10)
  rating: string                # Rating (AAA/AA/A/BBB/BB/B/CCC/D)
  outlook: string               # "positive" | "stable" | "negative" | "developing"
  veto_triggered: boolean       # Whether veto conditions were triggered
  veto_detail?: string          # Veto details

  # ── Signals ──
  signals: Signal[]             # All signals
  key_signals: Signal[]         # Key signals (for curated display, <=10 items)

  # ── Completeness ──
  completeness:
    density:
      L1_policy: number         # Signal density 0-100%
      L2_technology: number
      L3_supply_chain: number
      L4_financial: number
      track_b: number
    overall_density: number     # Total signal density
    confidence_level: string    # "high" | "medium" | "low"

  # ── Gaps ──
  gaps: Gap[]
    Gap:
      dimension: string         # Dimension where the gap exists
      missing_data: string      # Specific missing data
      impact: string            # Impact on analysis conclusions
      substitute?: string       # Substitute signal (if available)
      substitute_effectiveness: string  # "high" | "medium" | "low"

  # ── Cross Comparison ──
  cross_comparison:
    track_a_b_consensus: boolean
    track_a_score: float
    track_b_score: float
    quadrant: string            # "consensus_good" | "consensus_poor"
                                # | "divergence_market_panic"
                                # | "divergence_market_ignoring"
    divergence_analysis?: string

  # ── Stakeholder Views ──
  stakeholder_views:
    credit_approval: string     # Credit approval perspective
    bond_investment?: string    # Bond investment perspective (M1)
    bond_underwriting?: string  # Bond underwriting perspective (M2)
    market_trading?: string     # Market trading perspective (M3)
    portfolio_risk?: string     # Portfolio risk perspective (M4)
    corporate_finance?: string  # Corporate finance perspective (M5)

  # ── Vetos ──
  vetos:
    triggered: boolean
    items: VetoItem[]
      VetoItem:
        layer: string
        condition: string
        consequence: string
        evidence: string

  # ── Risk Signal List ──
  risk_signals: RiskSignal[]
    RiskSignal:
      priority: "critical" | "high" | "medium" | "low"
      signal: Signal
      description: string
      recommended_action: string

  # ── Credit Suggestion (Type1 only) ──
  credit_suggestion?:
    facility_amount: string
    term: string
    collateral: string
    conditions: string[]
    monitoring_focus: string[]
```

### 4.4 Template System

```yaml
TemplateSystem:
  description: >
    Report templates are based on the 12 report types defined in report-style-system.md Section 5.
    Each type corresponds to an HTML template file and a Hero gradient configuration.

  # ── Template Directory Structure (Existing Design) ──
  directory: "dev/templates/"
  files:
    base: "template-base.css"         # 14KB, base styles shared by all types
    components: "components/components.css"  # Component styles (not created yet)
    types:
      - "template-type1.html"         # Single entity deep analysis (currently missing)
      - "template-type2.html"         # Dual entity forward-looking comparison
      - "template-type3.html"         # Black swan retrospective verification
      - "template-type4.html"         # Multi-identity parallel assessment
      - "template-type5.html"         # Bond investment dashboard
      - "template-type6.html"         # Mosaic completeness report
      - "template-type7.html"         # Industry methodology page
      - "template-type8.html"         # Bond LGD assessment
      - "template-type9.html"         # External support special assessment
      - "template-type10.html"        # ESG+governance risk scan
      - "template-type11.html"        # Stress test report
      - "template-type12.html"        # Engine validation statistics

  # ── Current Template Status ──
  template_status:
    template-base.css: "Created"       # v1.0, 2026-07-08
    components.css: "Not Created"      # Styles defined in report-style-system.md Section 4
    template-type1.html: "Not Created" # Current report HTML is manually written
    template-type2.html: "Created"
    template-type3.html: "Created"
    template-type4.html: "Created"
    template-type5.html: "Created"
    template-type6.html: "Created"
    template-type7.html: "Created"
    template-type8.html: "Created"
    template-type9.html: "Created"
    template-type10.html: "Created"
    template-type11.html: "Created"
    template-type12.html: "Created"

  # ── Rendering Strategy ──
  rendering_strategy:
    method: "jinja2" | "mustache" | "ejs" | "string_replace"
    # Recommended to use a template engine (e.g., Jinja2 for Python or template string replacement),
    # to inject AnalysisResult data into predefined HTML templates.

    injection_points:
      # Marker points in the template that need data injection (using Mustache syntax as example):
      hero: >
        {{report_title}}
        {{industry}} · {{company}}
        {{analysis_date}}
        {{rating}} | {{composite_score}}
        {{outlook}}

      strip_items: >
        {{#strip_items}}
        {{label}}: {{value}}
        {{/strip_items}}

      pyramid_layers: >
        {{#layers}}
        {{name}}: {{score}}/10
        {{#signals}}
        - {{content}}
        {{/signals}}
        {{/layers}}

      completeness: >
        {{#completeness}}
        {{dimension}}: {{density}}%
        {{/completeness}}
```

### 4.5 Render Result

```yaml
RenderResult:
  html: string                  # Rendered HTML string
  file_path?: string            # Output file path (if specified)
  file_size: int                # File size (bytes)
  render_duration_ms: int       # Rendering duration
  template_used: string         # Template ID used
  included_sections: string[]   # List of included sections
  warnings: string[]            # Render warnings (e.g., placeholders due to missing data)

  # Example
  # file_size: 48500
  # render_duration_ms: 320
  # template_used: "type1"
  # included_sections: ["hero", "strip", "pyramid", "risk_signals", "credit_suggestion"]
  # warnings: ["market pricing data missing -> track_b section left blank"]
```

### 4.6 Error Handling

```yaml
RenderError:
  type: "template_not_found" | "data_mismatch" | "css_load_failed"
        | "output_write_failed" | "data_incomplete"
  detail: string
  recoverable: boolean

  # Error Handling Strategy:
  # - template_not_found: Template does not exist -> Fall back to type1 template
  # - data_mismatch: Data fields do not match template -> Skip mismatched fields, record warning
  # - css_load_failed: CSS file failed to load -> Use inline styles as fallback
  # - output_write_failed: File write failed -> Return HTML string
  # - data_incomplete: Data incomplete -> Render partial blocks, annotate "insufficient data"
```

---

## 5. Data Flow Timing

### 5.1 Complete Timing (Synchronous View)

```
User Input (Industry, Company Name, Analysis Date)
  │
  ├── [Step 1] Industry Identification (Existing)
  │     Load industry ten-dimension scoring -> Determine industry type -> Load weight template
  │     Input: (industry name)
  │     Output: (industry type, weight template, analysis framework configuration)
  │     Supported by existing methodology documents: analysis-engine-methodology.md Section 2
  │
  ├── [Step 2] Data Collection (New)
  │  ┌─ Parallel ───────────────────────────────────────────────────┐
  │  │ A1. web_search_policy(industry)                               │
  │  │     -> Search strategy keywords -> LLM parsing -> PolicyDoc[] │
  │  │ A2. web_search_enterprise(company)                             │
  │  │     -> Multi-source aggregation -> EnterpriseProfile          │
  │  │ A3. web_search_industry(industry)                               │
  │  │     -> Data template -> IndustryData[]                         │
  │  │ A4. web_search_market(company)                                  │
  │  │     -> Search -> MarketData[]                                  │
  │  └───────────────────────────────────────────────────────────────┘
  │     Input: (industry, company)
  │     Output: RawData[] (aggregated multi-source raw data)
  │     Current Status: Completely Blank
  │
  ├── [Step 3] Signal Extraction (New)
  │     extract_from_* -> Signal[]
  │     Input: RawData[]
  │     Output: Signal[] (structured signals)
  │     Each signal: {source, time, dimension, direction, strength, confidence, content}
  │     Current Status: Completely Blank
  │
  ├── [Step 4] Mosaic Assembly (Existing Design)
  │     Signal overlay -> Cross-validation -> Signal density calculation -> Completeness assessment
  │     Input: Signal[]
  │     Output: MosaicResult { aggregated signals, signal density, gap list, confidence }
  │     Supported by existing methodology documents: mosaic-engine.md Sections 4-5
  │
  ├── [Step 5] Analysis Scoring (Existing Design)
  │     Layer-by-layer scoring -> Composite weighting -> Rating mapping -> Veto check
  │     Input: MosaicResult + industry weight template
  │     Output: AnalysisResult { scores, rating, outlook, risk signals, credit suggestion }
  │     Supported by existing methodology documents: analysis-engine-methodology.md Sections 4-6
  │
  └── [Step 6] Report Generation (New)
        render(result, type1) -> HTML file
        Input: AnalysisResult + template ID
        Output: HTML file (complete report)
        Template exists: report-style-system.md
        Rendering logic: Completely Blank
```

### 5.2 Asynchronous Parallel View

```
Timeline ->
─────────────────────────────────────────────────────

Step 2 (Data Collection)        ████████████████████░░░░  ~120s
  A1 web_search_policy          ████████░░░░░░░░░░░░░░░   ~30s
  A2 web_search_enterprise      ██████████████░░░░░░░░░░   ~60s
  A3 web_search_industry        ████████░░░░░░░░░░░░░░░   ~30s
  A4 web_search_market          ████████░░░░░░░░░░░░░░░   ~30s

Step 3 (Signal Extraction)      ░░░░████████████░░░░░░░░  ~60s
  LLM extraction x 4 source types  ░░░░████████████░░░░░░░░

Step 4 (Mosaic Assembly)        ░░░░░░░░████░░░░░░░░░░░░  ~15s
  Signal overlay + cross-validation  ░░░░░░░░████░░░░░░░░░░

Step 5 (Analysis Scoring)       ░░░░░░░░░░████░░░░░░░░░░  ~15s
  Scoring + rating + veto       ░░░░░░░░░░████░░░░░░░░░░

Step 6 (Report Generation)      ░░░░░░░░░░░░████████░░░░  ~30s
  HTML rendering + file write   ░░░░░░░░░░░░████████░░░░

Total: ~240s (4 minutes)
```

### 5.3 Cache Strategy

```yaml
CacheStrategy:
  # ── Data Collection Cache (Input Adapter Internal) ──
  data_cache:
    - key: "policy_{industry}_{date}"
      ttl: 86400       # Policy data 24 hours
    - key: "industry_{industry}_{date}"
      ttl: 86400       # Industry data 24 hours
    - key: "enterprise_{company}"
      ttl: 3600        # Enterprise data 1 hour
    - key: "market_{company}"
      ttl: 300         # Market data 5 minutes

  # ── Signal Extraction Cache (Signal Extractor Internal) ──
  signal_cache:
    - key: "signals_{source_hash}"
      ttl: 3600        # Signal extraction results for the same source data cached 1 hour

  # ── Report Cache (Report Generator Internal) ──
  report_cache:
    - key: "report_{company}_{analysis_date}_{template_type}"
      ttl: 3600        # Report for same company on same day cached 1 hour

  # ── Cache Invalidation Conditions ──
  invalidation:
    - User manually refreshes
    - Data source returns "new data available"
    - Analysis start date changes
```

---

## 6. Public Data Source List

### 6.1 Verified Public Data Sources

The following data sources have been field-tested in the POC phase, covering the six-layer data architecture:

```yaml
VerifiedPublicSources:
  # ═══════════════════════════════════════
  # L1 Macro Policy
  # ═══════════════════════════════════════
  policy_sources:
    - name: "State Council"
      url: "https://www.gov.cn"
      type: "policy_document"
      coverage: "State Council decrees, State Council documents, policy interpretations"
      verified: true
      verified_case: "Solar export tax rebate cancellation announcement"

    - name: "National Development and Reform Commission"
      url: "https://www.ndrc.gov.cn"
      type: "policy_document"
      coverage: "Industrial policy, pricing policy, investment approval"
      verified: true
      verified_case: "Document No. 136 on electricity marketization pricing"

    - name: "Ministry of Industry and Information Technology"
      url: "https://www.miit.gov.cn"
      type: "policy_document"
      coverage: "Industry management, technical standards, capacity regulation"
      verified: true
      verified_case: "Solar industry standard conditions"

    - name: "National Energy Administration"
      url: "https://www.nea.gov.cn"
      type: "policy_document"
      coverage: "Green electricity, electricity pricing, grid connection policies"
      verified: true
      verified_case: "Document No. 688 on green electricity direct connection"

    - name: "Ministry of Finance"
      url: "https://www.mof.gov.cn"
      type: "policy_document"
      coverage: "Fiscal policy, export tax rebates"
      verified: true
      verified_case: "Solar export tax rebate cancellation announcement"

    - name: "Ministry of Commerce"
      url: "https://www.mofcom.gov.cn"
      type: "policy_document"
      coverage: "Trade policy, anti-dumping"
      verified: true
      verified_case: "Solar trade friction data"

    - name: "People's Bank of China"
      url: "https://www.pbc.gov.cn"
      type: "policy_document"
      coverage: "Monetary policy, LPR/MLF"
      verified: true
      verified_case: "Open market operation data"

  # ═══════════════════════════════════════
  # L2 Industry Data
  # ═══════════════════════════════════════
  industry_sources:
    - name: "CPIA (China Photovoltaic Industry Association)"
      url: "https://www.chinapv.org.cn"
      type: "industry_statistics"
      coverage: "Solar capacity production, export data, market share"
      verified: true
      verified_case: "Solar industry 2025 installed capacity data"

    - name: "SEMI (Semiconductor Equipment and Materials International)"
      url: "https://www.semi.org"
      type: "industry_statistics"
      coverage: "Semiconductor equipment shipments, materials market"
      verified: false
      note: "Relies on public report searches"

    - name: "CAAM (China Association of Automobile Manufacturers)"
      url: "https://www.caam.org.cn"
      type: "industry_statistics"
      coverage: "Automotive production and sales, new energy vehicle data"
      verified: false

    - name: "Cninfo"
      url: "https://www.cninfo.com.cn"
      type: "public_company_filing"
      coverage: "Listed company annual/quarterly reports, prospectus, announcements"
      verified: true
      verified_case: "LONGi Green Energy 2025 annual report data extraction"

  # ═══════════════════════════════════════
  # L3 Supply Chain Pricing
  # ═══════════════════════════════════════
  pricing_sources:
    - name: "PVInfoLink"
      url: "https://www.pvinfolink.com"
      type: "price_index"
      coverage: "Solar supply chain weekly quotes (free version delayed 1-2 weeks)"
      verified: true
      verified_case: "TOPCon cell 0.275 RMB/W, weekly decline 5.17%"

    - name: "TrendForce"
      url: "https://www.trendforce.com"
      type: "price_index"
      coverage: "Memory chip/panel prices"
      verified: false
      note: "Free version has limited data"

    - name: "SMM (Shanghai Metals Market)"
      url: "https://www.smm.cn"
      type: "price_index"
      coverage: "Metal/lithium/cobalt/nickel prices"
      verified: true
      verified_case: "Polysilicon price data"

  # ═══════════════════════════════════════
  # L4 Enterprise Public Information
  # ═══════════════════════════════════════
  enterprise_sources:
    - name: "National Enterprise Credit Information Publicity System"
      url: "https://www.gsxt.gov.cn"
      type: "enterprise_basic"
      coverage: "Business registration, shareholders, changes, administrative penalties"
      verified: true
      verified_case: "Yidao New Energy business registration query"

    - name: "China Judgments Online"
      url: "https://wenshu.court.gov.cn"
      type: "judicial_record"
      coverage: "Litigation, judgments, ruling documents"
      verified: true
      verified_case: "Solar enterprise litigation records"

    - name: "China Enforcement Information Publicity Network"
      url: "https://zxgk.court.gov.cn"
      type: "enforcement_record"
      coverage: "Judgment debtors, dishonest persons subject to enforcement, consumption restrictions"
      verified: true
      verified_case: "Aikang Technology enforced >580 million"

    - name: "National Enterprise Bankruptcy Restructuring Case Information Network"
      url: "https://pccz.court.gov.cn"
      type: "bankruptcy_record"
      coverage: "Bankruptcy applications, administrator appointments, creditors' meetings"
      verified: true
      verified_case: "Quanwei Technology pre-restructuring information"

    - name: "Cninfo"
      url: "https://www.cninfo.com.cn"
      type: "public_company_filing"
      coverage: "Annual/quarterly reports, material events, prospectus"
      verified: true

  # ═══════════════════════════════════════
  # L5 Bidding & Tendering
  # ═══════════════════════════════════════
  bidding_sources:
    - name: "Central Enterprise E-Procurement Platform"
      url: "Various central enterprise platforms"
      type: "bidding_result"
      coverage: "Huaneng/Huadian/SPIC/Sanhe/CNNC/CGN/CHN Energy/ChinaCoal, etc."
      verified: true
      verified_case: "Sanhe 2026 centralized procurement 10GW+, Longi shortlisted 50.3GW"

    - name: "China Bidding and Tendering Public Service Platform"
      url: "https://www.cebpubservice.com"
      type: "bidding_result"
      coverage: "Various bidding results"
      verified: false

  # ═══════════════════════════════════════
  # L6 Regional Economy
  # ═══════════════════════════════════════
  regional_sources:
    - name: "Provincial and Municipal Statistics Bureaus"
      url: "Various provincial and municipal websites"
      type: "regional_economy"
      coverage: "Regional GDP, industrial structure, fiscal revenue/expenditure"
      verified: false

  # ═══════════════════════════════════════
  # Market Data
  # ═══════════════════════════════════════
  market_sources:
    - name: "ChinaMoney"
      url: "https://www.chinamoney.com.cn"
      type: "bond_market_data"
      coverage: "Bond issuance rates, yield curves, credit spreads"
      verified: true
      verified_case: "ChinaBond valuation yield curve"

    - name: "Shanghai Stock Exchange"
      url: "https://www.sse.com.cn"
      type: "exchange_data"
      coverage: "Bond quotes, trading volume, announcements"
      verified: true

    - name: "Shenzhen Stock Exchange"
      url: "https://www.szse.cn"
      type: "exchange_data"
      coverage: "Bond quotes, trading volume, announcements"
      verified: true
```

### 6.2 Data Source Accessibility Quick Reference

| Industry | Policy Data | Enterprise Risk | Industry Data | Bidding | Market Data | Data Availability |
|---|---|---|---|---|---|---|
| Solar | ✅ High | ✅ High | ✅ High | ✅ High | ✅ Medium | ★★★★★ |
| Semiconductor | ✅ High | ✅ Medium | ✅ Medium | ⚠️ Low | ✅ Medium | ★★★★ |
| New Energy Vehicles | ✅ High | ✅ High | ✅ High | ⚠️ Low | ✅ High | ★★★★ |
| Biomedicine | ✅ Medium | ✅ Medium | ✅ Medium | ⚠️ Low | ✅ Medium | ★★★ |
| High-End Equipment | ✅ Medium | ✅ Medium | ⚠️ Low | ✅ Medium | ⚠️ Low | ★★★ |
| Data Centers | ✅ Medium | ⚠️ Low | ⚠️ Low | ⚠️ Low | ✅ High | ★★ |
| Medical Devices | ✅ Medium | ✅ Medium | ✅ Medium | ✅ Medium | ✅ Medium | ★★★★ |

> Note: The above quick reference is based on existing POC experience; some industries have not been practically verified. "⚠️ Low" does not mean data does not exist, only that acquisition via WebSearch is more difficult or data density is lower.

---

## 7. Priorities and Dependencies

### 7.1 Component Priority Matrix

```yaml
PriorityMatrix:
  # ── P0: Core Pipeline Must Operate ──
  P0:
    - component: "Input Adapter (Mode A)"
      description: "Public data collection — at minimum implement A1 (policy) + A2 (enterprise) dual-source parallel"
      depends_on: ["LLM search capability", "Search keyword templates"]
      estimated_effort: "5-7 days (including keyword template engineering)"
      validation: "Run pipeline on existing POC cases (Longi/Yidao New Energy), compare output with original manual search results"
      current_status: "Completely Blank"

    - component: "Signal Extractor"
      description: "Extract structured signals from collected data"
      depends_on: ["Input Adapter (Mode A)"]
      estimated_effort: "3-5 days (including LLM prompt system)"
      validation: "Compare manual extraction vs pipeline extraction signals on the same set of raw data"
      current_status: "Completely Blank"

  # ── P1: Report Output ──
  P1:
    - component: "Report Generator (Type 1)"
      description: "Single entity deep analysis — most commonly used report type"
      depends_on: ["Analysis Engine (Existing)", "template-type1.html (Not Created)"]
      estimated_effort: "3-4 days (including template creation + rendering logic)"
      validation: "Input existing analysis results, output HTML conforming to report-style-system.md Type 1 specification"
      current_status: "Template not created, rendering logic blank"

    - component: "Report Generator (Type 5 + Type 6)"
      description: "Bond investment dashboard + Mosaic completeness report"
      depends_on: ["Analysis Engine (Existing)"]
      estimated_effort: "2-3 days"
      current_status: "Templates created, rendering logic blank"

  # ── P2: Complete Report System ──
  P2:
    - component: "Report Generator (Types 2-4, 7-12)"
      description: "Remaining 9 report types"
      depends_on: ["Report Generator (Type 1)"]
      estimated_effort: "5-7 days (reusing Type 1 rendering framework)"
      current_status: "Templates created (except Type1), rendering logic blank"

    - component: "Input Adapter (Mode A3 + A4)"
      description: "Add industry data + market pricing data sources"
      depends_on: ["Input Adapter (Mode A1+A2)"]
      estimated_effort: "2-3 days"
      current_status: "Completely Blank"

  # ── P3: External Data Sources ──
  P3:
    - component: "Input Adapter (Mode B - CSV Upload)"
      description: "CSV/Excel upload adapter"
      depends_on: ["Signal Extractor (new -> existing)", "Mosaic Engine (existing)"]
      estimated_effort: "3-5 days"
      current_status: "Interface defined, no implementation"

    - component: "Input Adapter (Mode B - REST API)"
      description: "Wind/Choice and other financial terminal APIs"
      depends_on: ["External data source access license"]
      estimated_effort: "5-8 days"
      current_status: "Interface defined, no implementation"

    - component: "Input Adapter (Mode B - MCP)"
      description: "MCP data service adapter"
      depends_on: ["MCP protocol stack"]
      estimated_effort: "8-10 days"
      current_status: "Interface defined, no implementation"
```

### 7.2 Dependency Graph (DAG)

```
P0 ─────────────────────────────────────────────────
  InputAdapter(Mode A1+A2)
       │
       ▼
  SignalExtractor
       │
       ▼
  MosaicEngine (Existing) ──┬── AnalysisEngine (Existing)
       │
       ▼
  [Existing Pipeline Complete]

P1 ─────────────────────────────────────────────────
  AnalysisEngine (Existing)
       │
       ▼
  ReportGenerator(Type1)


P2 ─────────────────────────────────────────────────
  InputAdapter(Mode A3+A4)         ReportGenerator(Type1)
       │                                  │
       ▼                                  ▼
  SignalExtractor(Enhanced)       ReportGenerator(Type2-12)

P3 ─────────────────────────────────────────────────
  InputAdapter(Mode B)
       │
       ▼
  SignalExtractor(Enhanced)
```

### 7.3 Implementation Path Recommendations

```yaml
ImplementationPath:
  Phase1: "P0 Core Pipeline (2 weeks)"
    steps:
      - "Complete InputAdapter Mode A1 (policy) + A2 (enterprise)"
      - "Complete SignalExtractor core logic"
      - "Connect existing MosaicEngine and AnalysisEngine"
      - "Use Longi/Yidao New Energy as verification cases"

  Phase2: "P0 Report Output (1 week)"
    steps:
      - "Create template-type1.html"
      - "Complete ReportGenerator Type1 rendering logic"
      - "Validation: existing analysis results -> automatically generate compliant HTML report"

  Phase3: "P1-P2 Expansion (2 weeks)"
    steps:
      - "InputAdapter extend A3 (industry) + A4 (market)"
      - "ReportGenerator extend Type5+Type6"
      - "ReportGenerator extend remaining Types"

  Phase4: "P3 External Data Sources (contingent)"
    steps:
      - "Implement CSV Upload adapter"
      - "Implement REST API adapter (requires Wind/Choice license)"
```

---

## 8. Error Handling and Edge Cases

### 8.1 Global Error Classification

```yaml
ErrorClassification:
  # ── Input Layer Errors ──
  input_errors:
    - error: "empty_company_name"
      handling: "Return validation error: company name cannot be empty"
    - error: "invalid_industry"
      handling: "Return validation error: unsupported industry"
    - error: "ambiguous_company_name"
      handling: "Return company name candidate list, request user confirmation"

  # ── Data Collection Layer Errors ──
  collection_errors:
    - error: "source_unreachable"
      handling: "Mark this source as unavailable, continue with other sources"
    - error: "all_sources_failed"
      handling: "Return data collection failure error, suggest user check network or retry later"
    - error: "rate_limited"
      handling: "Exponential backoff retry (max 3 times), skip source if still fails"
    - error: "timeout"
      handling: "Single source timeout 30s -> skip source; overall timeout 120s -> use collected data"

  # ── Signal Extraction Layer Errors ──
  extraction_errors:
    - error: "llm_failure"
      handling: "Retry 2 times, skip source if still fails"
    - error: "parse_failure"
      handling: "Retry 1 time (add format constraints), skip source if still fails"
    - error: "empty_extraction"
      handling: "Normal processing — record 'no signal extracted from this source'"
    - error: "quality_check_failed"
      handling: "Discard the signal, record reason"

  # ── Analysis Engine Layer Errors (Existing) ──
  engine_errors:
    - error: "veto_triggered"
      handling: "Terminate analysis, directly output upper limit rating"
    - error: "insufficient_data"
      handling: "Mark as 'insufficient data to score', output directional judgment"
    - error: "score_out_of_range"
      handling: "Truncate to 0-10 range"

  # ── Report Generation Layer Errors ──
  render_errors:
    - error: "template_not_found"
      handling: "Fall back to type1 template"
    - error: "data_mismatch"
      handling: "Skip mismatched fields, record warning"
    - error: "output_write_failed"
      handling: "Return HTML string as fallback"
```

### 8.2 Edge Cases

```yaml
EdgeCases:
  # ── Enterprise Dimension ──
  - scenario: "Multiple companies with the same name"
    handling: "Use unified social credit code + registration location + registration date for disambiguation"
    fallback: "Return candidate list, request user selection"

  - scenario: "Company name change"
    handling: "Search using both new name and former name"
    fallback: "Use only current registered name"

  - scenario: "Group/parent company vs bond issuing entity"
    handling: "Clearly distinguish analysis entity (e.g., 'Brilliance Auto Group' vs 'Brilliance China')"
    fallback: "Annotate scope of analysis entity"

  # ── Data Dimension ──
  - scenario: "Data time inconsistency"
    handling: "Annotate publication time for each signal, analysis engine uses weighted timeline"
    fallback: "For data without time, mark as 'time unknown'"

  - scenario: "Completely empty data"
    handling: "Signal extraction layer returns empty signal list -> Mosaic engine marks as 'severely insufficient data'"
    fallback: "Composite score based on available signals"

  - scenario: "Search results are zero"
    handling: "All search strategies return empty -> Mark as 'insufficient public data coverage'"
    fallback: "Prompt user: this company may have no public credit data"

  - scenario: "Single data source returns large number of results"
    handling: "Take at most top 50 results for signal extraction"
    fallback: "Sample based on snippet signal density"

  # ── Report Dimension ──
  - scenario: "Score equals boundary value"
    handling: "Assign to higher range preferentially (e.g., 7.50 classified as AA rather than BBB)"
    fallback: "Annotate proximity to boundary"

  - scenario: "Signals from different dimensions contradict"
    handling: "Handled by Mosaic assembly layer (mosaic-engine.md Section 4.1)"
    fallback: "Mark as divergent signals, reduce related dimension confidence"

  - scenario: "Cross-industry enterprise (conglomerate)"
    handling: "Classify by main business industry, annotate ancillary businesses in analysis"
    fallback: "Use analysis framework corresponding to main business"
```

### 8.3 Data Completeness Graded Response

```yaml
DataCompletenessResponse:
  # Based on mosaic-engine.md Section 5.4 signal density response rules:
  
  density_gt_80:
    response: "High confidence"
    scoring: "Directly output precise score"
    report_note: "None"

  density_50_to_80:
    response: "Medium confidence"
    scoring: "Output score +/- 1 range"
    report_note: "Annotate 'data foundation moderate, score has +/-1 error range'"

  density_20_to_50:
    response: "Low confidence"
    scoring: "Output only directional judgment (positive/negative/neutral), no precise score"
    report_note: "Annotate 'insufficient information, directional judgment only', suggest supplementing data"

  density_lt_20:
    response: "Unable to assess"
    scoring: "Do not provide score for this dimension"
    report_note: "Annotate 'insufficient information to assess', prompt user to supplement data sources"
```

---

## 9. Appendix: Mapping with Existing Design Documents

### 9.1 Correspondence between this Specification and Existing Documents

| This Specification Section | Corresponding Existing Document | Relationship |
|---|---|---|
| Section 1 Overall Architecture | `mosaic-engine.md` Section 2, `analysis-engine-methodology.md` Section 1 | Extends existing architecture, adds data collection and report generation layers |
| Section 2 Data Collection Layer | `data-architecture.md` Section 2, `mosaic-engine.md` Section 6 | Engineering "manually verified" data sources into standardized interfaces |
| Section 3 Signal Extraction Layer | `mosaic-engine.md` Section 3 | Extends "signal data structure definition" into complete extraction interface |
| Section 4 Report Generation Layer | `report-style-system.md` Sections 1-6 | Converts template specifications in "design specs" into rendering interface |
| Section 5 Data Flow Timing | `analysis-engine-methodology.md` Section 5.1 | Extends single step into complete pipeline timing |
| Section 6 Public Data Source List | `data-architecture.md` Section 2, `analysis-engine-methodology.md` Section 3 | Compiled based on existing POC verification data |
| Section 7 Priorities and Dependencies | `mosaic-engine.md` Section 8, `2026-07-08-full-chain-design-plan.md` Sections 2-4 | Aligns with existing priority system |

### 9.2 Current Implementation Status Overview

```
Legend:
  ▓ Full design exists (methodology documents)
  ▒ Partially complete (interface defined / template created)
  ░ Completely blank (needs development from scratch)

Component                        Status    Context
──────────────────────────────────────────────────
Industry Classification (10-dim)  ▓▓▓▓▓  analysis-engine-methodology.md Section 2
Industry Pyramid Weight Templates ▓▓▓▓▓  industry-pyramids.md
Track A: Fundamental Analysis     ▓▓▓▓▓  analysis-engine-methodology.md Section 4
Track B: Market Pricing           ▓▓▓▓▓  mosaic-engine.md, dual-track-methodology.md
Cross Collision (Four Quadrants)  ▓▓▓▓▓  dual-track-methodology.md
Veto Condition Database           ▓▓▓▓▓  analysis-engine-methodology.md Section 6
Mosaic Assembly Layer (Signal Overlay/Cross)  ▓▓▓▓▓  mosaic-engine.md Section 4
Mosaic Completeness Assessment Layer          ▓▓▓▓▓  mosaic-engine.md Section 5
Data Gap -> Risk Mapping                      ▓▓▓▓▓  mosaic-engine.md Section 5.2
Mode B Interface Contract                     ▓▓▓▓▓  mosaic-engine.md Section 6, data-architecture.md Section 6
Template Base CSS                ▓▓▓▓  report-style-system.md, template-base.css
Report Templates (Types 2-12)    ▓▓▓▓  report-style-system.md, template-type*.html
Report Template (Type 1)         ░░░░░  Not Created
──────────────────────────────────────────────────
Input Adapter (Data Collection)  ░░░░░  This specification Section 2
Signal Extractor (Signal Extraction)  ░░░░░  This specification Section 3
Report Generator (Report Rendering)   ░░░░░  This specification Section 4
LLM Prompt System                ░░░░░  This specification Section 3.4 (framework level definition)
Search Keyword Templates         ░░░░░  This specification Section 2.4 (framework level definition)
```

### 9.3 Version History

| Version | Date | Changes |
|---|---|---|
| v0.1 | 2026-07-09 | Initial draft: Define standardized interfaces for Input Adapter/Signal Extractor/Report Generator three layers, compile data source list, annotate priorities and dependencies |

---

*This document defines the data pipeline interface specification for the Fixed Income Credit Analysis Engine Mode A Mosaic Engine. Detailed implementation of each layer's interface requires corresponding development of separate technical design documents.*
