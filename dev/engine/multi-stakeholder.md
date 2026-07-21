# Multi-Stakeholder Perspective Framework

**Version**: v0.0.3 | **Date**: 2026-07-17
**Source**: Fixed Income Credit Intelligence Engine v0.0.1 · Mosaic Engine Architecture
**Nature**: Structured archive — compiled from existing skill packages and specification documents

---

## 1. Six International Buy-Side Roles Overview

The framework covers six buy-side roles in the fixed income investment process. Each role operates with a distinct core decision, decision horizon, and data requirements. The roles are listed in order of analytical depth — from single-issuer credit analysis to personal investment decisions.

| # | Role | Core Decision | Horizon | Key Data Needs |
|---|------|--------------|---------|----------------|
| 1 | **Credit Selector** | "Does this credit belong in the book?" — single-issuer rating, default probability | 12-36 months | Industry pyramid, financial deep-dive, LGD/recovery, external support |
| 2 | **Portfolio Manager** | "Is this the best risk/reward?" — relative value, sector allocation | 6-24 months | Relative value metrics, comparative analysis, curve positioning |
| 3 | **Risk Officer** | "Where are concentration/contagion hotspots?" — portfolio risk monitoring | Continuous (monthly SRI + event-driven) | Concentration dashboard, contagion matrix, SRI, stress tests |
| 4 | **Trader** | "Is today the day to act?" — execution, market timing | Intraday to 2 weeks | L0 signal card, real-time spreads, liquidity conditions |
| 5 | **Advisor** | "What should my client do?" — allocation advice, suitability | 3-12 months | Client risk profile overlay, L1 snapshot, thematic views |
| 6 | **Individual Investor** | "Should I own this bond?" — personal investment decision | 6-36 months | Simplified L0/L1, buy/hold/sell signal, plain-language risk summary |

### 1.1 Role Core Constraints

Each role operates under a distinct set of constraints that shape its analytical priorities and decision thresholds.

| Role | Core Constraints |
|------|-----------------|
| **Credit Selector** | Rating accuracy, default prediction horizon, recovery rate estimation, regulatory capital treatment |
| **Portfolio Manager** | Benchmark tracking error, maximum drawdown, liquidity budget, sector concentration limits |
| **Risk Officer** | Concentration limits, stress test pass rates, tail risk management, systemic risk exposure |
| **Trader** | VaR limits, carry/roll-down economics, hedging instrument availability, settlement constraints |
| **Advisor** | Fiduciary duty, client suitability rules, diversification requirements, fee transparency |
| **Individual Investor** | Personal risk tolerance, income needs, investment horizon, tax implications |

### 1.2 Role-Level Data Requirements

| Role | Primary Data | Secondary Data | Data Gap Impact |
|------|--------------|----------------|-----------------|
| **Credit Selector** | Financial statements (parent-level, not consolidated), capital structure, operating cash flow | Industry benchmarks, peer comparisons, management quality indicators | Consolidated statements mask parent-level cash flow stress |
| **Portfolio Manager** | Yield/spread vs peer group, modified duration, convexity, Z-spread | Rating migration trends, sector sentiment indicators, macro forecasts | Without curve data, relative value assessment is unreliable |
| **Risk Officer** | Portfolio concentration heatmap, correlation matrix, drawdown history | Contagion matrix output, SRI temperature, scenario loss tables | Precise RWA calculation requires firm-internal data |
| **Trader** | Money market rates, yield curve, cross-market linkages | Market microstructure data, dealer quotes, order book depth | Bid-ask spread not disclosed in most markets — transaction cost unknowable |
| **Advisor** | Client portfolio holdings, risk tolerance score, income requirements | Market outlook reports, sector rotation signals, rating agency watches | Client position data often incomplete or delayed |
| **Individual Investor** | Bond price, coupon rate, maturity date, credit rating | News headlines, analyst summaries, fund flow data | Full prospectus too long — needs concise risk summary |

---

## 2. Role Deep-Dive Frameworks

### 2.1 Credit Selector — Single-Issuer Credit Assessment

The Credit Selector evaluates whether a specific credit belongs in the investment book. This is the foundational analytical role — every other role depends on accurate credit assessment.

**Decision Logic**: Evaluate the issuer's ability and willingness to service debt through one full credit cycle, using the industry-pyramid framework as the structural starting point.

**Assessment Framework**:

| Dimension | Weight | Key Question |
|-----------|--------|--------------|
| Industry Position (Pyramid Layer) | 25% | Where does the issuer sit in its industry structure? Is its position sustainable? |
| Financial Strength | 30% | Does the issuer generate sufficient cash flow to cover fixed charges through a downturn? |
| LGD / Recovery | 20% | If default occurs, what is the expected recovery given the capital structure and collateral? |
| External Support | 15% | Is there a parent, government, or strategic partner that would provide support in distress? |
| Governance & Management | 10% | Is management aligned with creditor interests? Are there governance red flags? |

**Scoring Logic**:

```
Credit Quality Score = f(
  Industry pyramid position (L1-L4),    // Structural moat assessment
  Debt/EBITDA + FCF/Total Debt,         // Leverage and coverage
  Collateral coverage ratio,             // Asset-based protection
  Parent/sovereign support capacity,     // External backstop
  Governance red flag count              // Qualitative overlay
)
```

**Decision Thresholds**:

| Score Range | Rating Equivalent | Action |
|-------------|-------------------|--------|
| 8.0~10.0 | AA- and above | Book with confidence |
| 6.0~7.9 | A- to A+ | Book with monitoring triggers |
| 4.0~5.9 | BBB- to BBB+ | Hold at reduced size |
| 2.0~3.9 | B to BB | Restrict — require covenant protection |
| 0~1.9 | CCC and below | Exclude from book |

### 2.2 Portfolio Manager — Relative Value & Sector Allocation

The Portfolio Manager determines whether a credit offers the best risk-adjusted return relative to alternatives. This role operates at the intersection of single-issuer analysis and portfolio construction. The PM Four-Dimension framework evaluates Relative Value, Sector Allocation Fit, Curve Positioning, and Event & Calendar factors.

**Decision Logic**: Compare each credit against its peer group on yield, spread, and risk metrics, then allocate capital to the best risk/reward opportunities within sector and duration constraints.

**Assessment Framework**:

| Dimension | Weight | Key Question |
|-----------|--------|--------------|
| Relative Value | 30% | Where does this bond rank within its peer group on yield, Z-spread, and OAS? |
| Sector Allocation Fit | 25% | Does adding this position improve the portfolio's sector diversification? |
| Curve Positioning | 20% | Is this point on the curve offering attractive roll-down vs comparable maturities? |
| Event & Calendar | 25% | What upcoming events (earnings, rating review, call/put dates) could move this bond? |

**Relative Value Scoring**:

```
Relative Value Score = f(
  Yield vs peer median,                  // Higher yield = cheaper
  Z-spread vs sector average,            // Excess spread = value opportunity
  Duration-adjusted carry,                // Carry net of hedging cost
  Roll-down vs curve steepness,          // Curve positioning benefit
  Peer rank percentile                   // Where this bond sits in the distribution
)
```

**Key Thresholds**:

- Z-spread > 50bp over peer median — potential value trap, not just cheapness
- Negative carry but high roll-down — curve trade, requires duration conviction
- Sector allocation delta > 5% from benchmark — active bet size needs justification
- Top-quartile relative value + bottom-quartile liquidity — tension signal, escalate

### 2.3 Risk Officer — Portfolio Risk Monitoring

The Risk Officer monitors concentration and contagion risks across the portfolio. This role is continuous rather than episodic, triggered by both scheduled reviews (monthly SRI cycles) and ad-hoc events (rating actions, market dislocations).

**Decision Logic**: Identify where the portfolio is most exposed to a single-factor shock, then quantify the loss under stress scenarios.

**Assessment Framework**:

| Dimension | Frequency | Key Question |
|-----------|-----------|--------------|
| Concentration Dashboard | Monthly | Is any single issuer, sector, region, or rating bucket over the predefined limit? |
| Contagion Matrix | Monthly + Event | If a key sector/issuer defaults, which other positions are at risk through interconnectedness? |
| SRI (Systematic Risk Indicator) | Monthly + Event | What is the current systemic risk temperature across all covered sectors? |
| Stress Tests | Quarterly + Event | Under a predefined adverse scenario, what is the expected loss? Does it exceed risk appetite? |

**Key Metrics**:

| Metric | Threshold | Action |
|--------|-----------|--------|
| Single-issuer concentration | > 5% of NAV | Flag for review; escalate if > 10% |
| Top-3 sector concentration | > 50% of NAV | Initiate diversification plan |
| Pseudo-AAA ratio (external AAA but internal < 7.5) | > 15% of NAV | Full review of AAA holdings |
| Contagion overlap score | > 3 sectors sharing a common risk factor | Scenario analysis required |
| SRI temperature | Red (critical) | Portfolio-wide risk reduction |

### 2.4 Trader — Execution & Market Timing

The Trader decides whether today is the right day to execute a trade. This role operates at the shortest horizon, converting analytical signals into market actions.

**Decision Logic**: Given a signal from the Credit Selector, Portfolio Manager, or Risk Officer, is now the right time to buy, sell, or hedge? What is the optimal execution strategy?

**Assessment Framework**:

| Dimension | Weight | Key Question |
|-----------|--------|--------------|
| L0 Signal Card | 35% | What is the real-time signal from the engine? Buy/sell/hold with conviction level? |
| Real-Time Spreads | 25% | Are current spreads favorable relative to recent history and fair-value estimates? |
| Liquidity Conditions | 25% | Can the trade be executed without moving the market? What is the estimated slippage? |
| Market Context | 15% | Are there macro events, news flow, or technical factors that create favorable windows? |

**Execution Decision Matrix**:

| Signal | Spread vs FV | Liquidity | Action |
|--------|--------------|-----------|--------|
| Buy | Cheap (spread > FV + 10bp) | Good | Execute at market |
| Buy | Cheap | Poor | Use limit orders, split over sessions |
| Buy | Fair | Any | Wait for better entry |
| Sell | Rich (spread < FV - 10bp) | Good | Execute at market |
| Sell | Rich | Poor | Start selling early |
| Hold | Any | Any | Do nothing, await signal change |

### 2.5 Advisor — Allocation Advice & Suitability

The Advisor translates institutional-grade credit analysis into actionable advice for clients. This role is the bridge between the analytical engine and the end investor.

**Decision Logic**: Given a client's risk profile, income needs, and existing holdings, should this bond be recommended? If so, at what allocation size?

**Assessment Framework**:

| Dimension | Weight | Key Question |
|-----------|--------|--------------|
| Client Suitability | 35% | Does this bond match the client's risk tolerance, income needs, and investment horizon? |
| L1 Snapshot | 25% | What is the one-page summary of the Credit Selector's full analysis — key risks and mitigants? |
| Portfolio Compatibility | 20% | Does this bond improve the client portfolio's diversification and risk/return profile? |
| Thematic Outlook | 20% | Does this bond align with the current market themes and sector views established by the PM? |

**Suitability Scoring**:

| Client Type | Suitable Bonds | Allocation Cap |
|-------------|----------------|----------------|
| Conservative (retiree, income-focused) | IG only, short-to-medium duration | 5% single name |
| Moderate (balanced portfolio) | IG core + up to 20% HY | 3% single HY name |
| Aggressive (growth-oriented) | IG + HY + distressed | 10% single name |
| Institutional (pension, endowment) | Broad mandate, IG focus | Based on IPS limits |

### 2.6 Individual Investor — Personal Investment Decision

The Individual Investor represents the end user of the analytical framework — a non-professional making personal investment decisions. This role requires simplified signals and plain-language explanations.

**Decision Logic**: Should I buy, hold, or sell this bond? What is the most important thing I need to know about this credit?

**Assessment Framework**:

| Dimension | Weight | Key Question |
|-----------|--------|--------------|
| Simplified L0/L1 Signal | 40% | Is the engine's signal clearly buy, hold, or sell? What is the conviction level? |
| Plain-Language Risk Summary | 30% | Can I understand the key risk in one paragraph? What could go wrong? |
| Buy/Hold/Sell Signal | 20% | What should I do today with my existing position or new cash? |
| Income & Duration Match | 10% | Does this bond's coupon and maturity match my income needs and timeline? |

**Signal Presentation**:

| Signal | Color | Meaning | Action |
|--------|-------|---------|--------|
| Strong Buy | Dark Green | Credit is strong and cheap | Add to position |
| Buy | Light Green | Good risk/reward | Consider adding |
| Hold | Yellow | Fairly priced, no catalyst | Maintain position |
| Sell | Orange | Deteriorating or better alternatives | Reduce position |
| Strong Sell | Red | Credit risk is rising significantly | Exit position |

---

## 3. Cross-Role Matrix — Tensions Between Roles Viewing the Same Issuer

When multiple roles assess the same issuer simultaneously, tensions arise from differing horizons, constraints, and analytical priorities. Understanding these tensions is essential for building a robust decision-making process.

### 3.1 Pairwise Tension Matrix

| Role A | Role B | Typical Tension | Resolution |
|--------|--------|-----------------|------------|
| **Credit Selector** | **Portfolio Manager** | CS sees a deteriorating single name and wants to remove; PM sees cheap spreads relative to sector and wants to hold for carry | Set a max hold period; if CS score drops below threshold, PM must present a compensating thesis |
| **Credit Selector** | **Risk Officer** | CS assigns a borderline credit score (e.g., 4.5); RO flags the position as a top-5 concentration risk | Escalate to investment committee; require enhanced monitoring and tighter stop-loss |
| **Credit Selector** | **Trader** | CS recommends buying; Trader sees poor liquidity and wide spreads — execution may erode the value proposition | Trader provides estimated slippage; CS re-evaluates at net entry spread |
| **Portfolio Manager** | **Risk Officer** | PM wants to increase sector exposure for relative value; RO warns the sector is already in the top concentration tier | Risk-adjusted sizing: allow the trade at a reduced allocation within the RO's limit |
| **Portfolio Manager** | **Trader** | PM wants to build a position over days/weeks; Trader sees intraday liquidity surge and wants to execute immediately | Agree on execution schedule; PM sets total allocation, Trader chooses best execution window |
| **Portfolio Manager** | **Advisor** | PM sees value in a complex structured product; Advisor cannot explain it clearly to clients | Restrict to qualified investor mandates only; Advisor provides plain-language addendum |
| **Risk Officer** | **Trader** | RO flags rising tail risk and wants reduced exposure; Trader sees dislocated pricing as a buying opportunity for the desk | Separate risk limits for "risk reduction" vs "opportunistic" trades; Trader must fund the trade from a dedicated tactical bucket |
| **Advisor** | **Individual Investor** | Advisor recommends a diversified portfolio; Individual wants to concentrate in a name they know | Fiduciary override: Advisor documents suitability objection; client signs acknowledgement of concentration risk |

### 3.2 Consensus and Divergence Handling

**Consensus Scenarios** (all applicable roles agree):

| Scenario | Protocol |
|----------|----------|
| All negative (avoid/reduce/risk-down) | Credit risk confirmed, no further validation needed. Escalate to PM/RO for action. |
| All positive (buy/allocate/risk-neutral) | Proceed with standard controls. Flag for collective blind-spot review quarterly. |

**Divergence Scenarios** (roles disagree):

| Divergence Pattern | Meaning | Resolution Principle |
|--------------------|---------|---------------------|
| CS negative, PM neutral | Credit Selector's stricter standards may be overridden for liquid, short-dated positions | PM must document compensating factors; position size reduced by 50% |
| PM negative, Advisor positive | PM sees poor relative value; Advisor client may have non-economic reasons (ESG, relationship) | Document non-economic rationale; flag for fair-value reporting |
| RO negative, everyone else positive | Risk officer sees concentration/exposure that others are ignoring | RO has veto power: max position size = 50% of RO's limit |
| Trader negative, CS/PM positive | Market conditions unfavorable for execution | Delay 5 trading days; if conditions persist, escalate to desk head |
| CS negative, Individual positive | Retail investor attracted by high coupon on a deteriorating credit | Advisor must intervene: suitability override required |

---

## 4. Multi-Role Parallel Assessment Methodology (WP-X-02)

Work Path X-02 defines the standard process for evaluating a single issuer or credit from multiple buy-side role perspectives simultaneously. The methodology ensures each role's analysis is independent, comparable, and collectively complete.

### 4.1 Five-Step Parallel Process

```
Step 1: Shared Data Preparation (all roles)
  |-- Establish analysis base date T0
  |-- Declare all publicly available data as of T0
  |   (instrument-level, issuer-level, market-level)
  |-- Tag each data item with source and timestamp
  |-- Output: Shared Data Inventory (SDI)
  |-- Constraint: no forward-looking information or hindsight

Step 2: Independent Role Assessments (parallel, isolated)
  |-- Credit Selector: pyramid + financial deep-dive + LGD + external support
  |-- Portfolio Manager: relative value + sector allocation + curve positioning
  |-- Risk Officer: concentration check + contagion scan + stress scenario
  |-- Trader: L0 signal + liquidity check + execution feasibility
  |-- Advisor: suitability overlay + client mapping + plain-language summary
  |-- Individual Investor: simplified signal + risk summary
  |-- Constraint: roles do NOT exchange interim conclusions (avoid contamination)

Step 3: Cross-Role Comparison
  |-- Build 6-role comparison matrix (or N-role, depending on mandate)
  |-- Mark consensus points (all roles align)
  |-- Mark divergence points (roles disagree on direction or magnitude)
  |-- For each divergence: identify which role's blind spot is exposed
  |-- Output: Cross-Role Comparison Matrix (CRCM)

Step 4: Mosaic Completeness Report
  |-- Signal density per role (%) — how much of the analytical framework was populated
  |-- Confidence level per role (Low / Medium / Medium-High / High)
  |-- Key data gaps per role
  |-- Gap-to-substitute mapping — for each gap, what proxy or alternative was used

Step 5: Consolidated Output
  |-- Consensus judgment (if all roles agree)
  |-- Divergence judgment with blind-spot analysis (if disagreement)
  |-- Warning window estimate — from T0 to earliest possible credit event
  |-- Role-specific action recommendations
```

### 4.2 Process Constraints

1. **Data must be strictly limited to what was publicly available at T0** — no hindsight, no post-event data, no "as we now know."
2. **Each role analyzes independently** — no role's conclusions may influence another role's assessment.
3. **Mosaic completeness report is mandatory** — every role must report signal density and confidence level.
4. **Blind spots must be explicitly documented** — each role has inherent blind spots; identify which other role's analysis compensates for each.
5. **Divergence is not a bug** — healthy tension between roles surfaces risks that any single role would miss.

### 4.3 Integration with Engine Work Paths

| Work Path | Relationship to Multi-Role Assessment |
|-----------|--------------------------------------|
| WP-X-02 (this) | Standard process for multi-role parallel evaluation |
| Type 4 Report Template | Standard output format for cross-role comparison matrix |
| WP-CS-01, WP-PM-01, WP-TR-01, WP-RO-01, WP-AD-01, WP-II-01 | Individual role work paths feed into Step 2 |
| WP-X-03 (Industry Analysis) | Pyramid structure feeds Credit Selector framework |
| WP-X-05 (Outlook Monitoring) | Updates each role's starting assumptions in periodic reviews |
| WP-RO-02 (Contagion Matrix) | Risk Officer uses this in Step 2 |

### 4.4 Workflow Diagram

```
                    +-------------------+
                    | Shared Data       |
                    | Inventory (SDI)   |
                    +--------+----------+
                             |
              +--------------+--------------+
              |              |              |
     +--------v------+ +----v--------+ +---v-----------+
     | Credit        | | Portfolio   | | Risk Officer  |
     | Selector      | | Manager     | |               |
     | (Step 2a)     | | (Step 2b)   | | (Step 2c)     |
     +-------+-------+ +------+------+ +-------+-------+
             |                |                |
     +-------v-------+ +------v------+ +------v--------+
     | Trader        | | Advisor     | | Individual    |
     | (Step 2d)     | | (Step 2e)   | | Investor      |
     |               | |             | | (Step 2f)     |
     +-------+-------+ +------+------+ +-------+-------+
             |                |                |
             +-------+--------+----------------+
                     |
          +----------v-----------+
          | Cross-Role Comparison |
          | Matrix (Step 3)      |
          +----------+-----------+
                     |
          +----------v-----------+
          | Mosaic Completeness  |
          | Report (Step 4)      |
          +----------+-----------+
                     |
          +----------v-----------+
          | Consolidated Output  |
          | (Step 5)             |
          +----------------------+
```

---

## 5. Role-Specific Dashboard Specifications

Each role requires a dedicated dashboard that surfaces the most relevant information at the appropriate frequency and granularity.

### 5.1 Credit Selector Dashboard

**Purpose**: Single-issuer credit quality monitoring and new-issue evaluation.

**Update Frequency**: Daily (score refresh on new data); Full review every quarter.

| Panel | Content | Display Type | Priority |
|-------|---------|--------------|----------|
| Industry Pyramid | Issuer placement in L1-L4 pyramid layer with peer cluster | Visual pyramid | P0 |
| Financial Deep-Dive | Key ratios: Debt/EBITDA, FCF/Debt, Interest Coverage, D/E | Time-series chart + table | P0 |
| LGD / Recovery | Capital structure waterfall, collateral coverage, seniority | Stacked bar chart | P0 |
| External Support | Parent rating, sovereign rating, support capacity score | Score card | P1 |
| Governance Red Flags | Related-party transactions, audit issues, management turnover | Alert list | P0 |
| Score Timeline | Credit Quality Score over trailing 12 months | Sparkline | P1 |
| Peer Comparison | Key ratios vs 5 closest peers in pyramid layer | Radar chart | P1 |

**Alert Thresholds**:
- Score drops below 4.0 -> Amber alert
- Score drops below 2.0 -> Red alert (consider removal from book)
- Debt/EBITDA crosses 6x -> Review initiated
- FCF/Debt turns negative for 2 consecutive quarters -> Watch list

### 5.2 Portfolio Manager Dashboard

**Purpose**: Relative value identification, sector allocation, and portfolio construction.

**Update Frequency**: Daily (market data refresh); Full rebalance review monthly.

| Panel | Content | Display Type | Priority |
|-------|---------|--------------|----------|
| Relative Value Heatmap | Z-spread decile ranking by peer group | Heatmap grid | P0 |
| Sector Allocation | Current vs benchmark sector weights | Waterfall bar | P0 |
| Curve Positioning | Portfolio duration buckets vs benchmark | Histogram overlay | P0 |
| Best/Worst Performers | Top/bottom 5 bonds by YTW change | Table with delta | P1 |
| Trade Ideas | Pre-screened relative value opportunities | Card list | P1 |
| Peer Rank Tracker | Where the portfolio ranks vs peer funds | Gauge meter | P1 |

**Alert Thresholds**:
- Sector allocation > 5% from benchmark -> Flag
- Single-name YTW moves > 2 standard deviations from 30-day average -> Review
- Relative value score shifts by > 2 deciles -> Re-evaluate thesis
- Any bond with BS (Strong Sell) from Credit Selector but still in portfolio -> Mandatory review

### 5.3 Risk Officer Dashboard

**Purpose**: Portfolio-level risk surveillance, concentration monitoring, stress testing.

**Update Frequency**: Continuous (intraday for market risk); Full review monthly.

| Panel | Content | Display Type | Priority |
|-------|---------|--------------|----------|
| SRI Temperature | Systematic Risk Indicator across all sectors | Thermometer (Green/Yellow/Red) | P0 |
| Concentration Heatmap | Sector x Region x Rating exposure matrix | Heatmap | P0 |
| Contagion Matrix | Inter-sector transmission paths with current exposure | Network graph | P0 |
| Top-10 Exposures | Largest single-name exposures with CS scores | Ranked table | P0 |
| Stress Test Results | Loss under adverse scenario by sector | Waterfall | P0 |
| Pseudo-AAA Tracker | External AAA bonds with internal score < 7.5 | Alert list | P1 |
| Limit Breach Log | Historical breaches of concentration limits | Timeline | P1 |

**Alert Thresholds**:
- SRI enters Yellow -> Weekly monitoring committee
- SRI enters Red -> Portfolio risk reduction mandated
- Any single-name > 10% NAV -> Immediate escalation
- Pseudo-AAA ratio > 15% -> Full review of AAA holdings
- Top-3 sectors > 60% NAV -> Diversification plan required

### 5.4 Trader Dashboard

**Purpose**: Execution decision support, real-time market conditions, signal prioritization.

**Update Frequency**: Real-time (intraday streaming).

| Panel | Content | Display Type | Priority |
|-------|---------|--------------|----------|
| L0 Signal Card | Real-time buy/hold/sell signal per ticker with conviction | Card per issuer (color-coded) | P0 |
| Spread vs FV | Current spread vs fair-value estimate with z-score | Gauge + sparkline | P0 |
| Liquidity Score | Composite liquidity score (volume, turnover, depth) | Bar with percentile rank | P0 |
| Watch List | Pre-approved trade ideas from PM/CS ready to execute | Actionable card list | P0 |
| Market Context | Key macro events, central bank calendar, earnings releases | Timeline | P1 |

**Alert Thresholds**:
- Spread moves > 2 z-scores from fair value -> Highlight as opportunity
- Liquidity score drops below 20th percentile -> Use limit orders only
- Signal switches from Hold to Buy/Sell -> Push notification
- Bid-ask spread widens > 3x normal -> Reduce order size

### 5.5 Advisor Dashboard

**Purpose**: Client portfolio suitability checking, investment memo generation, client communication.

**Update Frequency**: Daily (new analysis available); Client review prep weekly.

| Panel | Content | Display Type | Priority |
|-------|---------|--------------|----------|
| Client Risk Profile | Current risk tolerance score, income needs, horizon | Profile card | P0 |
| L1 Snapshot | One-page bond summary: key risks, rating, signal | Summary card | P0 |
| Portfolio Fit | Effect of recommended bond on client portfolio diversification | Before/after donut | P1 |
| Suitability Check | Pass/fail for recommended bonds against client criteria | Pass/Fail badges | P0 |
| Thematic Views | Current sector/thematic outlook from PM team | Bullet list | P1 |

**Alert Thresholds**:
- Any bond with CS score < 4.0 flagged for a conservative client -> Mandatory suitability override
- Recommended bond would push single-name concentration > client limit -> Block trade
- Advisor recommends Hold/Sell across > 30% of positions -> Rebalance discussion triggered

### 5.6 Individual Investor Dashboard

**Purpose**: Personal bond investment decisions with simplified signals and plain language.

**Update Frequency**: Updated when new analysis is published; User can refresh on demand.

| Panel | Content | Display Type | Priority |
|-------|---------|--------------|----------|
| My Portfolio | Holdings with buy/hold/sell signal per bond | Portfolio list with color badges | P0 |
| Signal Summary | Overall portfolio signal distribution | Donut chart | P0 |
| Bond Detail | L1 snapshot, risk summary, signal, price chart | Detail card | P0 |
| Risk Summary | Plain-language: "What could go wrong with this bond?" | Expandable section | P0 |
| Action Items | Recommended trades (buy this, sell that) with rationale | Action card list | P1 |

**Alert Thresholds**:
- Any bond signal changes to Strong Sell -> Email/push notification
- Portfolio > 50% concentrated in one sector -> Diversification prompt
- Bond coupon exceeds 2x comparable CD rate -> Risk warning (yield trap signal)
- Any bond in portfolio crosses its expected maturity -> Roll-over consideration prompt

---

## Appendix A: Role-to-Metric Mapping

| Metric | Credit Selector | Portfolio Manager | Risk Officer | Trader | Advisor | Individual Investor |
|--------|:---:|:---:|:---:|:---:|:---:|:---:|
| Industry Pyramid Score | Primary | Reference | — | — | Reference | — |
| Debt/EBITDA | Primary | — | — | — | — | — |
| Z-Spread vs Peer Median | — | Primary | — | Primary | — | — |
| LGD / Recovery | Primary | — | — | — | — | — |
| SRI Temperature | — | Reference | Primary | Reference | — | — |
| Concentration Ratio | — | — | Primary | — | — | — |
| Liquidity Score | — | — | — | Primary | — | — |
| Signal (Buy/Hold/Sell) | Output | Output | Output | Output | Filtered | Primary |
| Client Suitability | — | — | — | — | Primary | — |
| Plain-Language Summary | — | — | — | — | Primary | Primary |

## Appendix B: Horizon Alignment Across Roles

When roles with different horizons assess the same issuer, time-horizon conflicts must be explicitly managed.

| Base Horizon | Role(s) | Conflict with Shorter Horizon | Conflict with Longer Horizon |
|--------------|---------|-------------------------------|------------------------------|
| 12-36 months | Credit Selector | Short-term price volatility ignored | — |
| 6-24 months | Portfolio Manager | Tactical trades may conflict with sector allocation | Medium-term thesis may persist through short-term noise |
| Continuous | Risk Officer | — | Long positions may exceed risk limits temporarily |
| Intraday-2 weeks | Trader | Execution focus may miss medium-term deterioration | Market timing irrelevant for strategic holding |
| 3-12 months | Advisor | Advice may be too slow for fast-moving markets | May miss long-term credit improvement |
| 6-36 months | Individual Investor | Overreacts to short-term news | Patience may miss warning signals |

**Horizon Conflict Resolution**:
- Short-term signals do not override long-term credit scores, but they do trigger a review.
- Long-term assesses are not used to justify holding through known credit deterioration.
- Risk Officer's continuous monitoring overrides all fixed-horizon assessments during stress events.

---

*This framework supersedes the legacy M0-M5 Chinese-market stakeholder framework. All roles are now aligned to international buy-side functions and the WP-X-02 parallel assessment methodology.*
