# Layered Output Framework — Product Design Specification

**Version**: v0.0.7 | **Date**: 2026-07-10
**Status**: Product design document (not code implementation)
**Design Basis**: Practitioner Usability Audit (P0-level output model reform)

---

## 1. Design Background and Problem Statement

### 1.1 Core Criticisms from the Practitioner Audit

The current engine demonstrates solid academic rigor on the methodology level, but from the perspective of a fund manager's daily usage, it is still far from being "embeddable into a workflow." The core contradictions are:

| Engine Current State | Practitioner Need | Nature of Conflict |
|---|---|---|
| Only one output mode: "deep report" | Need 5-second glance, 30-second preliminary judgment, deep dive when needed | Output granularity is not adjustable |
| Output order is L1->L4 (analyst logic) | Thought path is "price/rating -> terms -> industry -> financials" (decision-maker logic) | Information organization does not match cognitive flow |
| Outputs 50-80 information points at once | Users will not read everything; need guidance on "what can be ignored" | No priority filtering |
| Assumes users will proactively query and read thoroughly | 70% of positions require no daily attention; only 10% need deep analysis | Zero workflow embedment |

### 1.2 Design Goals

1. **Time-scalable**: The same analysis engine outputs three granularity levels, from 5 seconds to 5 minutes, adapting to different scenarios
2. **Decision-maker oriented**: Output order starts from "rating + signals" rather than from "macro environment"
3. **Information priority computable**: Not all signals are equally important -- provide implementable ranking rules
4. **Workflow embeddable**: Support four scenarios: "morning push - intraday query - post-market deep dive - weekly scan"

---

## 2. Three-Layer Output System Overview

### 2.1 Three-Layer Definitions

| Layer | Name | Target User | Consumption Time | Core Content | Trigger Method |
|---|---|---|---|---|---|
| **L0 Signal Card** | 5-second Quick View | Fund Manager/Trader | 3-5 seconds | Rating + Outlook + Today's key signals (max 3) + Data completeness indicator light | Morning auto-push/intraday overlay/position alert |
| **L1 Snapshot** | 30-second Diagnosis | Credit Analyst/Investment Manager | 20-40 seconds | Four-dimension radar chart + Key anomaly list + Rating comparison + Industry ranking | Click signal card to expand/on-demand query |
| **L2 Deep** | Full Report | Deep Researcher/Credit Approval | 2-5 minutes | Pyramid layer-by-layer analysis + Mosaic collage + Dual-track collision + Completeness report | Click any dimension in snapshot to expand/on-demand generation |

### 2.2 Navigation Relationships Between Layers

```
User Perspective:

  Morning Push List
       |
   ----+----
   | L0 Signal Card |  <- 5-second judgment: Does this bond need my attention?
   | [Expand]       |
   +----+----
        | Click "Expand" or "View Snapshot"
        v
   +----------+
   | L1 Snapshot |  <- 30-second judgment: Where are the risks? What does the market think?
   | [Expand Dim]|
   +----+-----+
        | Click any dimension (e.g., "Fundamentals" panel)
        v
   +----------+
   | L2 Deep  |  <- 2-5 minutes: Full analysis, supports credit approval decisions
   +----------+
```

**Key Design Constraint**: Each expansion from L0 to L2 must maintain context continuity -- when a user expands a dimension from the snapshot, L2 defaults to navigating to that dimension, not starting from the beginning.

### 2.3 Engine Data Sharing Across Layers

All three layers share the same analysis engine output, differing only in presentation format and information density:

```
Mosaic Engine + Dual-Track Collision
        |
   +----+------------------------------+
   |       Analysis Results Pool       |
   |  +-- Composite Rating + Outlook | |
   |  +-- Dimension Scores (0-10)    | |
   |  +-- Full Signal Priority List  | |
   |  +-- External vs Internal Rating| |
   |  +-- Four-dimension Scores (Spread/Fundamentals/Covenants/Liquidity) |
   |  +-- Industry Rankings          | |
   |  +-- Key Risk Points (veto/near threshold) |
   |  +-- Completeness Report (signal density + gap list) |
   +----+------------------------------+
        |
   +----+----+
   | L0 Renderer |  <- Take TOP3 signals + composite rating + completeness light
   +----+----+
   +----+----+
   | L1 Renderer |  <- Take four-dimension scores + anomaly list + comparison data
   +----+----+
   +----+----+
   | L2 Renderer |  <- Take all analysis results
   +---------+
```

**Implementation Constraint**: L0 must be renderable as soon as the engine finishes outputting the composite rating and signal ranking, without waiting for the L2 full report to be generated.

---

## 3. L0 Signal Card Design Specification

### 3.1 Design Philosophy

The core of L0 is not "providing information" but **answering one question**: "Does this bond need my attention today?"

If not, the signal card should let the user scroll past with zero cognitive load. If yes, the signal card must provide sufficient reason for "why attention is needed," prompting a click to expand.

### 3.2 Layout

All content on the signal card must be visible in one screen without scrolling (height not exceeding one phone screen or a desktop-standard card height).

```
+-------------------------------------------------------+
| LONGi Green Energy (601012)  Internal Rating: BB+  Outlook: Negative |
|                                                          |
| Today's Signals (Priority Sorted)                        |
|  [R] High | LONGi 22 convertible bond premium ratio 74%, put option triggered |
|  [Y] Medium | Northbound capital reduced 24% over 3 months, position ratio down to 2.1% |
|                                                          |
| Data: [##########] 82%  .  Industry Rank: PV convertible bonds 3/5 |
|                                                          |
| [View 30-sec Diagnosis]  [Expand Full Report]  [Mark as Read] |
+-------------------------------------------------------+
```

```
+-------------------------------------------------------+
| An LGFV (XXXXXX)          Internal Rating: AA-  Outlook: Stable |
|                                                          |
| Today's Signals                                           |
|  [i] No new trigger signals -- credit quality stable, routine monitoring sufficient |
|                                                          |
| Data: [######] 62%[W]  .  Industry Rank: LGFV Province/City 1/15 |
|                                                          |
| [View 30-sec Diagnosis]  [Expand Full Report]            |
+-------------------------------------------------------+
```

### 3.3 Element Specifications

| Element | Content | Rules |
|---|---|---|
| **Title Row** | Company abbreviation + Stock code | Bold font, largest font size |
| **Rating Row** | Internal rating + Outlook + External rating (if significant difference) | Rating color-coded (AAA green -> D red), outlook with arrow |
| **Signal Area** | Max 3 signals with priority >30 | Each signal: severity icon + one-line description (<=25 chars) + key figure |
| **Data Completeness** | Signal density percentage + text grade label | Percentage + progress bar, >80% = sufficient / 50-80% = moderate / 20-50% = insufficient / <20% = severely lacking |
| **Industry Ranking** | Industry + rank/total | Only shown when industry comparison data is available |
| **Action Area** | Expand buttons | "View 30-sec Diagnosis" + "Expand Full Report," or "Mark as Read" |

### 3.4 No Signal / Zero Anomaly State

When a bond has no signals with priority >30, the L0 signal card degrades into a "silent card":

- Not pushed (unless the user has actively added the bond to a "mandatory watch list")
- Still visible in the position list, status shows "Normal / No New Signals"
- Rating and outlook displayed as usual
- Signal area replaced with one gray message: "No new trigger signals -- credit quality stable, routine monitoring sufficient"

**Design Principle**: 90% of the time, the engine should tell the user "nothing is happening"; "something happening" is the informative state.

### 3.5 L0 Requirements from the Engine

L0 must be renderable once the following data is ready, without waiting for a complete analysis:

| Data Item | Source | Availability Timing |
|---|---|---|
| Internal rating + Outlook | Dual-track collision composite output | Engine calculation complete |
| TOP3 signals | Signal pool sorted by priority, take top 3 | Signal extraction + priority sorting complete |
| Data completeness percentage | Completeness assessment layer | Signal density calculation complete |
| Industry ranking | Comparable industry analysis | Engine calculation complete |

**Asynchronous Rendering Timing Recommendation**:

```
T+0s: Initiate mosaic engine analysis
T+1s: Rating + outlook ready -> conditions met to render L0 base framework
T+3s: Signal extraction + priority sorting complete -> TOP3 signals ready
T+5s: Completeness assessment + industry ranking ready -> L0 fully renderable
T+30s: L1 snapshot data fully ready (four-dimension scores + anomaly list)
T+120s: L2 full report ready
```

L0 -> L1 -> L2 become ready progressively. Users can decide within 5 seconds after seeing L0 whether to wait for L1.

### 3.6 Systemic Risk Thermometer Card (New in v0.0.1)

When the system intelligence layer's thermometer (SRI) changes color, an **aggregate thermometer card** is inserted at the top of the L0 signal card list, pushing systemic risk level changes to all position-holding users. This card is not specific to any single bond but reflects portfolio-level systemic risk.

#### 3.6.1 Thermometer Card Trigger Rules

The thermometer card is pushed only when the **thermometer level changes**; it is not repeated when the status remains unchanged:

| Temperature Change | Trigger Scenario | Insertion Position | Push Strategy |
|---|---|---|---|
| [G]->[Y] Normal->Watch | Red industry share rises from <20% to 20-30% | Top of L0 list | Push to all users |
| [Y]->[O] Watch->Caution | Red industry share rises from 20-30% to 30-50%, or high-contagion industry triggers alert | Top of L0 list, red border | Push to all users + highlight |
| [O]->[R] Caution->Danger | Red industry share >50%, or multiple high-contagion industries trigger simultaneously | Top of L0 list, deep red flashing border | Force alert for all users |
| [Y]->[G] Watch->Normal | Systemic risk retreats | Top of L0 list (gray) | Push "risk lifted" once only |
| [R]/[O]->[Y]/[G] Danger retreats | Systemic risk resolved | Top of L0 list (green) | Push "alert lifted" once only |

**Frequency Control**: The same temperature level may push at most 1 thermometer card per day to avoid repetitive interference.

#### 3.6.2 [Y] Watch Level Card (Example)

```
+-------------------------------------------------------+
|  [Y] Systemic Risk Watch         SRI: 0.56              |
|                                                          |
|  Red Industries: 2/19 (10.5%)  .  High-contagion industries: 1 at yellow |
|  Triggered Industries: Chemicals (Red)  .  Automobiles (Yellow) |
|                                                          |
|  Contagion Risk: Chemicals -> Energy -> Utilities (transmission intensity 4+) |
|  Recommendation: Check portfolio exposure to above industries, monitor downstream of contagion chain |
|                                                          |
|  [View Systemic Alert >]  [View Contagion Matrix]        |
+-------------------------------------------------------+
```

#### 3.6.3 [O] Caution Level Card (Example)

```
+-------------------------------------------------------+
|  [O] Systemic Risk Caution         SRI: 1.15              |
|  [W] Red industry share exceeds 30%, high-contagion industries showing severe signals |
|-------------------------------------------------------|
|  Red Industries: 5/19 (26.3%)                            |
|  Red List: Energy . Chemicals . Automobiles . Retail . Metals & Mining |
|  High-Contagion Triggered: Chemicals (contagion 5) . Automobiles (contagion 3) |
|                                                          |
|  Expected to affect 2 related industries -> Portfolio impairment stress: Medium |
|  -> Recommendation: Run portfolio stress test, reduce high-risk industry exposure |
|                                                          |
|  [View Systemic Alert]  [View Contagion Matrix]  [Run Stress Test] |
+-------------------------------------------------------+
```

#### 3.6.4 [R] Danger Level Card (Example)

```
+-------------------------------------------------------+
|  [R] Systemic Risk Alert            SRI: 1.83              |
|  [W] Red industry share exceeds 50%, all high-contagion industries triggered |
|-------------------------------------------------------|
|  Red Industries: 7/19 (36.8%)                            |
|  Red List: Energy . Chemicals . Tech Hardware . Automobiles . Retail . Metals & Mining . Consumer Staples |
|  High-Contagion Triggered: Financials (contagion 5) . Tech Hardware (contagion 4) |
|                                                          |
|  4 industries have triggered concentrated contagion -> Expected to affect 3 related industries |
|  -> Portfolio impairment stress: Medium-High             |
|  -> Recommendation: Run portfolio stress test, reduce high-risk industry exposure |
|                                                          |
|  [View Systemic Alert]  [View Contagion Matrix]  [Run Stress Test] |
+-------------------------------------------------------+
```

#### 3.6.5 [G] Risk Lifted Card (Example)

```
+-------------------------------------------------------+
|  [G] Systemic Risk Lifted            SRI: 0.22             |
|                                                          |
|  Red Industries: 0/13 (0%)  .  Thermometer has retreated from [R] to [G] |
|  Duration: 14 days  .  Last [R] level: 2026-06-26       |
|                                                          |
|  Retreat Driver: Real estate industry policy marginal easing, market sentiment repair |
|  -> Recommendation: Maintain routine monitoring frequency, watch for potential rebounds |
+-------------------------------------------------------+
```

#### 3.6.6 Thermometer Card Action Area Mapping

| Action Button | Target View | Description |
|---|---|---|
| [View Systemic Alert] | Type 15 Report | Navigate to the current systemic risk alert full report |
| [View Contagion Matrix] | Contagion Matrix Highlight View | Open the 19x19 contagion matrix, highlighting rows and columns of current red industries |
| [Run Stress Test] | M4 Stress Test Module | Based on current thermometer reading, run portfolio-level stress test (S3 scenario) |

#### 3.6.7 Thermometer Card and Individual Bond L0 Signal Card Linkage

The presence of the thermometer card **upgrades** the signal priority of individual bond L0 signal cards:

- When the thermometer is [O] (Caution) or [R] (Danger), all individual bond L0 signal cards in affected industries automatically receive a +10 priority boost
- Upgraded signal cards in the L0 list appear after the thermometer card and before other individual bond cards
- After the thermometer card disappears (normal state), individual bond signal cards revert to their original priority

**Design Principle**: The system intelligence layer's thermometer is not a substitute for individual bond analysis, but provides **systemic background context** for individual bond decisions -- letting users know "what state the entire market is in" when making individual bond decisions.

---

## 4. L1 Snapshot Design Specification

### 4.1 Design Philosophy

L1's core is to answer four questions:
1. **How is this bond overall?** (Four-dimension radar chart -- see strengths and weaknesses at a glance)
2. **Where are the problems?** (Key anomaly annotations -- red/yellow signal list)
3. **What does the market think?** (External rating vs internal rating comparison)
4. **Where does it rank in the industry?** (Ranking -- expensive or cheap?)

### 4.2 Four-Dimension Radar Chart

#### 4.2.1 Four Dimension Definitions

> **Disambiguation:** The L1 snapshot radar below is an **issuer-level visualization** (Spread / Fundamentals / Covenants / Liquidity). It is distinct from the WP-PM-01 Type-5 dashboard four-dimension (Relative Value / Covenant Protection / Liquidity / Event Calendar), whose single source of truth is `multi-stakeholder.md` §2.2b, and from the PM Portfolio-Construction Assessment (§2.2).

| Dimension | Name | Content | Data Source | Standardization Method |
|---|---|---|---|---|
| **Spread Dimension** | Market pricing attractiveness | YTM, credit spread, spread historical percentile, spread trend (widening/narrowing) | Track B market pricing signals | Map same-industry spread percentile to 0-10: 0=most expensive (lowest spread), 10=cheapest (highest spread) |
| **Fundamentals Dimension** | Credit quality foundation | Track A pyramid composite score, considering L1-L4 comprehensively | Track A fundamentals rating | Track A composite score mapped directly: 0-10 |
| **Covenants Dimension** | Investor protection level | Put protection, cross-default, guarantee, collateral, maturity structure | Bond prospectus (M1.2 covenant analysis) | Covenant checklist scoring: +1.5 per favorable covenant, -1.5 per unfavorable covenant, baseline 5 |
| **Liquidity Dimension** | Trading liquidity | Average daily turnover, turnover rate, bid-ask spread (if available), pledgeability | Track B liquidity signals + M1.3 liquidity assessment | Volume percentile + turnover rate percentile + pledge discount rate composite score: 0-10 |

#### 4.2.2 Radar Chart Presentation Template

```
                    Spread
                     [A]
                    10|
                      |
                      |     .  Fundamentals
         Liquidity [--+-->
                      |
                      |
                      |
                      [V]
                    Covenants

Actual Example (text description, graphical in UI):

                 Spread 8
               /          \
              /            \
             /              \
     Liquidity 3 [-----------> Fundamentals 6
             \              /
              \            /
               \          /
                Covenants 7

Score Labels:
  Spread 8/10    [G] On the cheaper side within the industry, spread percentile 78%
  Fundamentals 6/10  [Y] Upper-medium, composite score 6.2
  Covenants 7/10    [G] Has put protection + cross-default clauses
  Liquidity 3/10  [R] Average daily turnover below 5 million, low turnover rate
```

#### 4.2.3 Radar Chart Interpretation Guide

The four-dimension radar chart presents **scores on four independent dimensions**; it is normal for their directions to not be fully aligned. Common patterns and their meanings:

| Radar Chart Pattern | Typical Characteristics | Meaning | Action Recommendation |
|---|---|---|---|
| **Four-Dimension Balanced** | All four scores between 6-8 | Credit quality stable, market pricing reasonable | Maintain existing positions |
| **High Spread + Low Fundamentals** | Spread 8+, Fundamentals 3-4 | Market has already priced in fundamental deterioration in advance (Divergence B) | Be cautious, do not be tempted by high spread |
| **High Spread + High Fundamentals** | Spread 7+, Fundamentals 7+ | Rare high-value opportunity | Consider increasing position |
| **Low Spread + High Fundamentals** | Spread 2-3, Fundamentals 7+ | High quality but expensive, potentially overvalued | Wait for pullback |
| **Extremely Low Liquidity** | Liquidity 0-2 | High trading cost, difficult to exit | Control position size, reserve liquidity buffer |

### 4.3 Key Anomaly Annotations

The anomaly annotation area lists all current signals with priority >15 (not limited to 3), grouped by severity.

```
--- Key Anomaly Signals ---

[R] Red (High Priority, Needs Attention Within 24 Hours)
  1. LONGi 22 convertible bond premium ratio 74%, has triggered put provision protection price
     -> Recommendation: if underlying stock continues to decline, may trigger put option, affecting liability structure
  2. 2026Q1 revenue -48% YoY, second consecutive quarter decline >30%
     -> Key concern: whether revenue decline triggers cash flow exhaustion threshold

[Y] Yellow (Medium Priority, Needs Continuous Tracking)
  3. Northbound capital reduced 24% over 3 months, position ratio from 2.8% to 2.1%
     -> Sentiment signal, does not directly change fundamental judgment
  4. Short-term commercial paper issuance rate recovered from 2.02% to 2.15%, inflection point signal
     -> Monitor whether next issuance rate continues to rise

[i] Gray (Already in Monitoring, No Action for Now)
  5. Accounts receivable turnover days from 45 days to 62 days
     -> Already marked as continuous observation item, not triggering alert individually
```

**Standard Structure for Each Anomaly Signal**:

```yaml
signal_card:
  severity: "red" | "yellow" | "gray"
  title: "One-line description (<=25 chars)"
  detail: "Key data support (<=40 chars)"
  action: "Meaning or suggested action for the user (<=30 chars)"
```

### 4.4 Rating Comparison

Display a comparison between external ratings and the engine's internal rating, helping users quickly assess "what does the market/rating agency think" vs "what does the engine think."

```
Rating Comparison:

  External (China Chengxin)    Internal (Engine)
   +------+                    +------+
   | AAA  |                    | BB+  |
   +------+                    +------+
   Outlook: Stable             Outlook: Negative
       |                         |
       +----------- +------------+
                   v
             Divergence Level: Severe (deviation 8/10)
             Interpretation: External rating has not yet reflected 2026 projected losses and put risk;
                             Engine judgment is consistent with the rating lag pattern of Yongmei/Ziguang cases
```

Rating comparison divergence grading:

| Divergence | Gap | Meaning | Display Style |
|---|---|---|---|
| 0-2 notches | Internal and external differ by <=2 notches | Basically consistent, mutual verification | Green "=" |
| 3-4 notches | Differ by 3-4 notches | Moderate divergence, needs attention | Yellow "U"/"D" |
| 5+ notches | Differ by >=5 notches | Severe divergence, refer to Yongmei/Ziguang lag pattern | Red "UU"/"DD" |

### 4.5 Same-Industry Ranking

Ranking among comparable targets, satisfying the fund manager's core need for a "comparative perspective."

```
Same-Industry Ranking: PV Industry Convertible Bonds (5 bonds)

  Rank  Target        Internal Rating  Spread(bp)  Trend
  1    Tongwei 22 CB    AAA             258         <- Expensive
  2    LONGi 22 CB      BB+             335         <- Reasonably expensive
  3    Tianhe 23 CB     AA-             312         [S] Recommended
  4    Jingneng CB      A               421         <- High risk premium
  5    Hehe CB          B+              480         <- Bottom characteristics

  LONGi Green Energy ranks 3/5 among PV convertible bonds
  -> Core reason for low ranking: fundamental deterioration (expected loss) + put risk
  -> But BC technology leadership and central enterprise procurement advantages are not fully reflected in spreads
```

Ranking rules:
- Ranking baseline can be "same industry, same product type" or "same rating, same product type"
- Ranking basis defaults to "comprehensive value" (weighted composite of spread + fundamentals + covenants + liquidity)
- User can switch sorting basis (by spread / by rating / by liquidity)
- Targets worth noting are marked with [S] -- rule: spread percentile >60% and fundamentals score >5

---

## 5. L2 Deep Report Design Specification

### 5.1 Design Philosophy

L2 does not reinvent the wheel -- it reuses the current engine's full output (Mosaic report + Dual-track scores + Multi-identity comparison + Completeness report), but does three things:

1. **Re-sort**: Organize output structure from a "decision-maker perspective" rather than an "analyst perspective"
2. **Add gaps**: Annotate in each panel "which data is missing in this area and what that means"
3. **Add navigation**: Users can "drill into" any dimension of the L1 radar chart to the corresponding panel in L2

### 5.2 Output Order: Decision-Maker Perspective Four-Panel Structure

#### Panel 1: Rating + Signals + Ranking (5-second Scan)

```
===== LONGi Green Energy (601012) Full Credit Analysis =====
Analysis Date: 2026-07-08 | Industry: PV (P1 Cyclical) | Duration: ~3 minutes

+-------------------------------------------------------+
| Composite Rating: BB+            Outlook: Negative      |
| External Rating: AAA/Stable      Divergence: Severe (8/10) |
| Veto: Not triggered                                        |
+-------------------------------------------------------+
| Core Conclusion (2 sentences):                              |
| LONGi Green Energy's BC technology leadership remains,      |
| but 2026 projected loss of 9-10 billion combined with       |
| LONGi 22 CB put risk means credit quality is under         |
| short-term pressure. Focus on 2026Q3 financial report.      |
+-------------------------------------------------------+
| Key Signals (TOP5):                                         |
| [R] LONGi 22 CB premium ratio 74%, put protection triggered |
| [Y] Northbound capital reduced 24% over 3 months             |
| [Y] Short-term CP issuance rate inflection (2.02%->2.15%) |
| [Y] AR turnover days from 45 to 62 days                      |
| [G] BC cell production efficiency 24.8%, 2% above industry avg |
+-------------------------------------------------------+
| Industry Rank: PV convertible bonds 3/5 | Data Completeness: 82% Medium-High Confidence |
+-------------------------------------------------------+
```

#### Panel 2: Market Pricing + Covenants + Liquidity (30-second judgment)

```
===== Panel 2: Market Pricing and Trading Conditions =====

[Spread Analysis]
  Current YTM: 2.15% | Spread: 335bp vs same-rating median 312bp
  Spread Historical Percentile: 78% (elevated range)
  Spread Trend (3 months): Widened 42bp
   +-- Spread is widening, but magnitude is less than industry average (66bp), relatively resilient

[Cross-Collision: Spread vs Fundamentals]
  Track A (Fundamentals): 6.2/10 -> Upper-medium
  Track B (Spread): 4/10 -> Anomaly/Attention
  Cross Status: Divergence A (A good + B bad)
  Interpretation: Market has additional concerns (industry-wide losses), spread widening has some fundamental support
  Recommendation: Divergence is on the downside protection; maintain but do not add

[Covenants Analysis]                  +============+
  v Put protection (premium ratio 74%)     | Covenant Score: |
  v Cross-default clause                |   7/10       |
  v Guarantee: None                     +============+
  x No collateral
  x No sinking fund

[Liquidity Analysis]
  Average daily turnover: 12.48M (industry average: 35M)
  Turnover rate: 1.2% (low)
  Pledgeable: Yes (standard bond conversion rate 0.58)
  Bid-Ask: Not disclosed (China credit bond market convention)
  Liquidity Composite Score: 3/10 [W]
```

#### Panel 3: Industry and Fundamentals Deep Dive (2 minutes, long-term allocation decision)

```
===== Panel 3: Industry and Fundamentals Deep Dive =====

[L1 Policy/Macro Score: 8/10]
  - BC technology supported by national policy (2026 NEA document)
  - Central enterprise centralized procurement selected 50.3GW (85% of 2026 total 59GW)
  - Risk: Distributed PV subsidy phase-out pressure
  Data Completeness: 85% [OK]

[L2 Technology/Competition Score: 8/10]
  - BC cell production efficiency 24.8%, leading TOPCon by approx. 1.3%
  - Patents: 510, 2nd in industry
  - [W] Yield rate data not public, cannot precisely quantify cost advantage
  Data Completeness: 72% [W] (Yield rate data missing)

[L3 Supply Chain/Operations Score: 7/10]
  - Diversified customer distribution, top 5 customers 32%
  - Vertical integration (wafer -> cell -> module) reduces supply chain risk
  - Risk: Silicon material price volatility impact on inventory
  Data Completeness: 68% [W]

[L4 Financial/Debt Service Score: 6/10]
  - Cash reserves 52.6B, short-term debt 31.2B, cash/short-term debt ratio 1.69x
  - 2026H1 projected loss 9-10B (silicon material price collapse + inventory impairment)
  - FCF/Interest: 1.2x (2025 annual report, 2026H1 estimated to possibly turn negative)
  - FCF/Revenue: -2.1% (2026H1 estimate, below 0% threshold)
  - [W] FCF/Interest continuously below 2x for >2 years, triggering "Ponzi financing suspicion" observation
  Data Completeness: 89% [OK]
```

#### Panel 4: Data Completeness and Risk Warnings (Confidence Assessment)

```
===== Panel 4: Confidence and Risk Warnings =====

[Data Completeness Overview]
  +---------------------------------------+
  | L1 Policy/Macro      [########] 82%  |
  | L2 Technology/Compet [######] 72% [W] |
  | L3 Supply Chain/Ops  [######] 68% [W] |
  | L4 Financial/Debt    [#########] 89%   |
  | Market Pricing (Tr B) [####] 35% [W]  |
  | Covenant Analysis     [########] 80%  |
  | Liquidity             [####] 45% [W]  |
  +---------------------------------------+

[Core Data Gaps and Impact]
  [X] Yield rate data missing -> Precise cost competitiveness assessment unavailable
     -> Alternative: Central enterprise procurement winning bid pricing as indirect indicator
     -> Impact: L2 score confidence interval +/- 1.5

  [X] Parent company standalone financial data unobtainable
     -> Impact: Cannot precisely assess parent-level short-term debt servicing ability
     -> Alternative: Consolidated statements + listed company announcements for estimation

[Competing Hypotheses]
  Current Judgment: LONGi BB+, short-term credit quality under pressure
  -> If wrong, the most likely reasons are:
     1. 2026Q3 industry cycle reversal, silicon material price recovery driving profit recovery (upside risk)
     2. Put provisions diluted or extended, short-term debt pressure controllable (upside risk)
     3. Losses continue beyond expectations, cash reserve consumption accelerating (downside risk)

[Action Guide]
  [B] What you can do:
     - Maintain positions, do not add
     - Watch 2026Q3 financial report (October 2026)
     - Track LONGi 22 CB premium ratio changes
     - Monitor whether next short-term CP issuance rate continues to rise

  [B] What you do not need to do:
     - No need for panic selling (short-term debt servicing ability still intact)
     - No need for additional credit analysis (data completeness medium-high, gaps do not affect core judgment)
```

### 5.3 Navigation Rules

When a user clicks the "Fundamentals" dimension from L1 snapshot, the L2 deep report should **navigate directly to Panel 3** (Industry and Fundamentals Deep Dive), not start from the beginning.

```
Navigation Mapping Table:

  L1 Dimension Click          ->   L2 Target Position
  Spread Dimension           ->   Panel 2 (Market Pricing and Trading Conditions)
  Fundamentals Dimension     ->   Panel 3 (Industry and Fundamentals Deep Dive)
  Covenants Dimension        ->   Panel 2 - Covenant Analysis
  Liquidity Dimension        ->   Panel 2 - Liquidity Analysis
  Rating Comparison Area     ->   Panel 4 - Confidence and Risk Warnings
  Anomaly Signal List        ->   Panel 1 - Key Signals
```

---

## 6. Information Priority Sorting Rules

### 6.1 Core Formula

```
Signal Priority Score = Urgency Score (1-5) x Importance Score (1-5) x Confidence Score (1-5)

Score Range: 1-125
```

### 6.2 Three-Component Definitions

#### Urgency Score (Needs attention within 24 hours?)

| Score | Criterion | Example |
|---|---|---|
| 5 | Veto condition triggered, or default risk within 30 days | Put triggered, interest overdue, rating cliff downgrade |
| 4 | Core debt service metrics may deteriorate to dangerous threshold within 1-3 months | Short-term CP rate continuously rising, cash reserves suddenly declining |
| 3 | Signal indicates directional change in medium-term (3-6 months) trend | Revenue declining for two consecutive quarters, northbound capital continuously reducing |
| 2 | Marginal change, meaningful at 6-12 month scale but not urgent | Turnover days slowly deteriorating, industry spread overall widening |
| 1 | Long-term trend change, >12 month scale | Technology roadmap iteration, demographic structure change |

#### Importance Score (Impact magnitude on credit quality)

| Score | Criterion | Example |
|---|---|---|
| 5 | Directly affects debt servicing ability or default probability | Cash depletion, FCF persistently negative, put triggered |
| 4 | Material impact on credit quality, but not directly fatal | Revenue decline 50%+, core assets transferred |
| 3 | Moderate impact, changes trend judgment | Spread widening 50bp+, rating outlook downgraded |
| 2 | Minor impact, but needs inclusion in comprehensive judgment | Industry overall spread widening, shareholder reduction |
| 1 | Negligible or indirectly related impact | Management change (non-core), negative media coverage |

#### Confidence Score (Reliability of data behind the signal)

| Score | Criterion | Example |
|---|---|---|
| 5 | Multi-source cross-verification, data direct source | Exchange announcement of put trigger, annual report revenue data |
| 4 | Single-source reliable data, source trustworthy | Wind/Choice terminal data, CSRC disclosure |
| 3 | Derived inference, but logical chain complete | Spread inflection point = market repricing risk (2+ independent spread data points) |
| 2 | Single-source weak signal, or logical chain has gaps | A news report mentioning, analyst estimate |
| 1 | Speculation/rumor, cannot be verified | Market rumor, unsourced social media discussion |

### 6.3 Thresholds and Filtering Rules

```
Priority Score > 30:    Enter L0 Signal Card (max 3 per bond, highest scores selected)
Priority Score > 15:    Enter L1 Snapshot - Key Anomaly List
Priority Score <= 15:   Enter L2 Deep Report - Full Signal List (does not enter L0/L1)
```

### 6.4 Score Calculation Examples

| Signal | Urgency | Importance | Confidence | Total | Entry Layer |
|---|---|---|---|---|---|
| LONGi 22 CB put triggered | 5 | 5 | 5 | 125 | L0 [OK] |
| Short-term CP issuance rate inflection (2.02%->2.15%) | 3 | 4 | 4 | 48 | L0 [OK] |
| Northbound capital reduced 24% over 3 months | 3 | 3 | 4 | 36 | L0 [OK] |
| AR turnover days from 45 to 62 days | 2 | 3 | 3 | 18 | L1 [OK] |
| Industry overall spread widening | 2 | 2 | 4 | 16 | L1 [OK] |
| Management non-core role change | 1 | 1 | 2 | 2 | L2 only |

### 6.5 Special Rules

1. **Veto Signal**: Any signal triggering a veto condition automatically receives priority > 100, directly enters L0 with red marking
2. **False Signal Suppression**: If 3+ signals in the same dimension on the same day point in opposite directions -> all signals in that dimension automatically have confidence reduced by 1 level (contradictory signals reduce reliability)
3. **Time Decay**: Signals older than 30 days automatically have urgency reduced by 1 point (30-60 days) or 2 points (60+ days). But signal priority scores for positions are updated at least once per month.
4. **User Weight Adjustment**: Allow users to set a specific signal type (e.g., "northbound capital flows") to have overall urgency x0.5 (reduce noise), or fix "put triggered" urgency at 5 (cannot be overridden)

---

## 7. Workflow Embedding Design

### 7.1 Four Scenario Definitions

| Scenario | Time Window | User State | Engine Mode | Output Specification |
|---|---|---|---|---|
| **Morning Push** | Before market open (8:00-9:00) | Quick scan mode, 5-10 sec/item | Active push | Aggregate L0 signal cards for all positions (only push bonds with red/yellow signals) |
| **Intraday Query** | Trading hours (9:30-15:00) | Interruption-driven, instant response | Passive query | L1 snapshot (default output) |
| **Post-Market Deep Dive** | After close (15:00-17:00) | Deep mode, 30-60 min/bond | Passive query | L2 full report |
| **Weekly Scan** | Every Monday (full day) | Scan mode, focusing on changes | Active push | L1 snapshot update for watch list (only show changed portions) |

### 7.2 Scenario 1: Morning Push

#### 7.2.1 Trigger Mechanism

- Runs automatically before market open each day (default 8:00, user can adjust between 7:00-9:00 in settings)
- Only analyzes bonds held in the portfolio (bonds not on the watch list are not refreshed daily, saving computing resources)
- Only pushes bonds with red/yellow signals -- bonds without signals are not pushed but remain visible on the "All Positions" page

#### 7.2.2 Output Format

Morning push is presented as an **aggregate view**, not individual reports per bond:

```
===== Morning Credit Snapshot | 2026-07-08 | 8:00 =====

Portfolio Size: 20B | Bonds Held: 52
Today's Signal Status: Red 3 | Yellow 7 | Normal 42

-- Red Alert (Needs Attention Within 24 Hours) --

1. LONGi Green Energy (601012) | Rating: BB+/Negative | LONGi 22 CB put triggered
   -> Position Weight: 2.3% | Recommendation: Assess whether to reduce or communicate with issuer

2. Tongwei (600438) | Rating: B/Negative | Short-term CP issuance rate continuously rising
   -> Position Weight: 1.5% | Recommendation: Watch next short-term CP issuance

-- Yellow Watch (Needs Attention This Week) --

3. An LGFV (XXXXXX) | Rating: AA-/Stable | Regional general budget revenue declined 8%
   -> Position Weight: 4.1% | Recommendation: Monitor regional debt resolution progress

...subsequent yellow entries...

-- Action Summary --
Recommended actions today: 1 item
  LONGi Green Energy -- Assess whether to communicate with issuer regarding put arrangements
Recommended attention this week: 3 items
  Tongwei short-term CP, An LGFV regional finance, Tianhe CB spread change
```

#### 7.2.3 Output Content Organization Principles

- **Aggregation First**: Morning brief for 50 bonds must be displayed in one page view (desktop no scroll needed, mobile scrollable but signal card height compressed)
- **Changes First**: Only show bonds that have changed -- "no change" is good news
- **Position-Aware**: If a high-risk bond has a very low position weight (e.g., <0.5%), reduce its display priority
- **Action-Oriented**: Each signal card must have a "recommended action"; signals without an action recommendation are not pushed

#### 7.2.4 Position-Weighted Adjustment Rules

During morning push, signal display priority considers position weight:

```
Morning Display Priority = Signal Priority Score x (1 + Position Weight Factor)

Position Weight Factor:
  Position > 5%:   +0.5
  Position 2-5%:   +0.2
  Position 0.5-2%: 0
  Position < 0.5%: -0.3 (below threshold, display priority reduced even if signal exists)
```

### 7.3 Scenario 2: Intraday Query

#### 7.3.1 Trigger Timing

- User actively enters a bond code/name during trading hours
- System detects abnormal price/spread fluctuation in a held bond (magnitude >2 standard deviations)
- User clicks a bond on the portfolio dashboard

#### 7.3.2 Output Format

Default output is L1 snapshot. User can select "Changes Only" mode (compared to the last complete analysis):

```
===== LONGi Green Energy (601012) | Intraday Snapshot | 10:32 =====

Rating: BB+/Negative | External: AAA/Stable

[Four-Dimension Radar Chart - same as 7.3.2]

Changes since last analysis (2026-07-07 16:00):
  [Y] Spread from 331bp to 335bp (+4bp) -> Trend continues but magnitude small
  [G] No new fundamental signals -> Unchanged
  [i] No news/announcements -> Unchanged

Key Anomalies:
  [R] LONGi 22 CB premium ratio 74% [v] (continuing, unchanged)
  [Y] Northbound capital continues reducing (-0.3% today) -> Trend continuing
```

Change detection rules:
- Spread change >10bp marked yellow, >30bp marked red
- New external rating event marked red
- New material announcement (financial report, expected loss, asset restructuring) marked red

### 7.4 Scenario 3: Post-Market Deep Dive

#### 7.4.1 Trigger Timing

- User actively requests full analysis
- User clicks any dimension in L1 snapshot to expand
- Credit approval/inclusion decision required

#### 7.4.2 Output Format

L2 full report (see Section 5). Includes timestamp and caching policy:

- L2 analysis results for the same bond cached for 24 hours
- When re-requested within 24 hours, return cached results first with annotation "Analysis time: 2026-07-07 16:00"
- User can force refresh (click "Reanalyze")
- If external rating events/financial reports/material announcements occur within 24 hours, cache automatically invalidated

### 7.5 Scenario 4: Weekly Scan

#### 7.5.1 Trigger Timing

- Runs automatically at 9:00 AM every Monday
- Configurable as "watch list only" or "all positions"

#### 7.5.2 Output Format

Weekly scan displays a **change summary**, not a full analysis:

```
===== Weekly Credit Scan | Week 28 (2026-07-06 ~ 2026-07-10) =====

Coverage: Watch list 30 bonds | Position list 52 bonds

-- New Signals Triggered This Week --
  LONGi Green Energy: 1 new [Y] signal (short-term CP rate inflection)
  An LGFV: 1 new [Y] signal (general budget revenue decline)
  Others: No new triggers

-- Existing Signal Changes --
  Tongwei: [O] Short-term CP rate further rising (2.15%->2.22%) -> Urgency upgraded
  Trina Solar: [G] AR turnover improved (62 days->55 days) -> Marginal improvement

-- Rating Migration --
  Rating changes this week: None
  Rating changes this month: 1 (Tongwei: BB -> B-)

-- Items to Watch Next Week --
  2026-07-10: LONGi Green Energy investor conference
  2026-07-15: LGFV quarterly report disclosure deadline
```

Weekly scan incremental detection rules:
- Compare with last week's snapshot, list "new/upgraded/downgraded/disappeared" signals
- Rating migration records (rating changes within the past month)
- Known event calendar for the next 7-14 days

### 7.6 Workflow Embedding Configuration Items (User-Settable)

| Configuration Item | Default Value | Optional Values | Scope |
|---|---|---|---|
| Morning Push Time | 8:00 | 7:00-9:00 | Scenario 1 |
| Morning Push Scope | All positions | All positions / Watch list only | Scenario 1 |
| Intraday Auto Monitor | On | On / Off | Scenario 2 (price anomaly trigger) |
| Intraday Price Anomaly Threshold | 2 standard deviations | 1-3 standard deviations | Scenario 2 |
| Morning Push Minimum Signal Priority | 30 | 15-50 | Scenario 1 (L0 threshold) |
| Watch List Upper Limit | 30 bonds | 10-100 bonds | Scenario 1/4 |
| Weekly Scan Day | Monday | Monday to Friday | Scenario 4 |

---

## 8. Integration with the Existing Framework

### 8.1 Integration with the Mosaic Engine

L0/L1/L2 all use the Mosaic engine's output as the underlying data source. As shown below:

```
Mosaic Engine Output:
  Signal Pool (list of all signals, with priority scores)
  Dimension Scores (0-10 for each dimension)
  Completeness Report (signal density + gap list)
       |
       +-- L0 Filter: Take signals with priority >30, take top 3
       +-- L1 Aggregator: Take four-dimension scores + signals with priority >15
       +-- L2 Full Output: All content
```

### 8.2 Integration with Dual-Track Analysis

- Market pricing signals appearing in L0 signal cards must be labeled as coming from Track B
- L1 snapshot spread dimension directly corresponds to Track B market pricing score
- L1 snapshot fundamentals dimension directly corresponds to Track A composite score
- L2 deep report dual-track collision results appear only in Panel 3 (information is not omitted, but post-poned)

### 8.3 Integration with Multi-Stakeholder Framework

L2 deep report provides identity switching capability:

```
[Current Perspective: Bond Investor M1] [Switch to: Credit Approval M0] [Switch to: Underwriter M2]

After switching perspectives:
  Rating unchanged
  Signal list unchanged (perspective switching does not affect facts)
  But the "action recommendation" for each signal changes according to the identity
  Example: Put triggered -> M1 recommends "reduce position", M0 recommends "communicate with issuer for additional collateral"
```

L0 and L1 do not provide identity switching (the differences in information volume and action recommendations across identities cannot be fully presented in a 30-second snapshot).

### 8.4 Integration with the Completeness Assessment Layer

Completeness assessment data is presented in different ways across the three layers:

| Layer | Completeness Presentation | Example |
|---|---|---|
| L0 | A color + percentage indicator light | "Data: [########] 82%" |
| L1 | Percentage + text grade label | "Data Completeness: 82% Medium-High Confidence" |
| L2 | Full signal density bar chart + gap list + impact assessment | See Section 5.2 Panel 4 |

**Core Design Principle**: L0/L1 users do not need to see "what signal density 35% means" -- the engine should make this judgment for the user and only expose gap details when needed.

---

## 9. Special State Handling

### 9.1 First Analysis (No Historical Comparison)

When a user queries a bond for the first time, there is no historical data to compare against:

- L0 Signal Card: Display normally, but annotate in the signal area "First analysis, no comparable history available"
- L1 Snapshot: Radar chart displays normally, but the change detection area shows "First analysis, changes will be available on next update"
- L2 Deep Report: Full display, no change annotations

### 9.2 Severely Insufficient Data (Signal Density <20%)

When a bond's overall signal density is below 20%:

- L0 Signal Card: Data completeness indicator light shows red, annotated "Insufficient data, low rating confidence"
- L0 Signal Card: Signal area shows "Insufficient data to generate reliable signals," no signal items displayed
- L1 Snapshot: Only radar chart displayed (with dashed lines indicating low confidence), no anomaly list or rating comparison
- L2 Deep Report: Generated normally, but each panel has a warning bar at the top annotated "Severely insufficient data"

### 9.3 Veto Triggered

When a veto is triggered:

- L0 Signal Card: Rating displayed as CCC (upper limit), red background border, signal area top shows "Veto triggered"
- L1 Snapshot: Fundamentals dimension of the four-dimension radar chart automatically set to 0, first item in anomaly list shows veto reason
- L2 Deep Report: Panel 3 fundamentals deep dive shows the specific dimension and reason for the veto trigger

### 9.4 Non-Listed / No Market Data

For non-listed companies or targets without tradeable bonds:

- L0 Signal Card: Rating displayed normally, but spread dimension marked as "No market data," data completeness automatically reduced
- L1 Snapshot: Spread and liquidity dimensions in the four-dimension radar chart shown in gray (indicating unavailable)
- L1 Snapshot: Ranking area shows "No market data, cannot participate in same-industry ranking"
- L1 Snapshot: Rating comparison shows only external rating (if available)
- L2 Deep Report: Panel 2 (Market Pricing) annotated "No market data," but other panels display normally

---

## 10. Appendices

### 10.1 Terminology Glossary

| Term | Synonyms/Former Names | Definition |
|---|---|---|
| L0 Signal Card | Quick View Card / Morning Card | Minimal credit signal presentation digestible in 5 seconds |
| L1 Snapshot | Quick Diagnosis / 30-second Assessment | Rapid credit assessment including four-dimension radar chart |
| L2 Deep | Full Report / Deep Report | Current engine's complete analysis output |
| Signal Priority | Signal Importance | Composite score of urgency x importance x confidence |
| Data Completeness Light | Signal Density Indicator | Green/yellow/red data adequacy indicator |
| Four-Dimension Radar Chart | Four-Dimension Score | Standardized scores for spread/fundamentals/covenants/liquidity |
| Morning Push | Pre-Market Briefing | Daily auto-push position signal summary |
| Weekly Scan | Weekly Report | Weekly watch list change summary |

### 10.2 Correspondence with Practitioner Audit Recommendations

| Audit Issue | This Framework's Solution | Relevant Sections |
|---|---|---|
| "Only one output mode: deep report" | Three-layer output system: L0/L1/L2 | Sections 2, 3, 4, 5 |
| "Output order is analyst logic, not decision-maker logic" | Decision-maker perspective four-panel structure: rating -> pricing -> fundamentals -> confidence | Section 5.2 |
| "Information overload, 50-80 information points" | Priority sorting formula + three-layer filtering | Section 6 |
| "No morning push" | Workflow scenario 1: Morning push | Section 7.2 |
| "No position aggregate dashboard" | Morning push aggregate view + signal status count | Section 7.2 |
| "No comparison with comparable targets" | L1 snapshot same-industry ranking module | Section 4.5 |
| "Action recommendations not clear" | Each signal comes with an action recommendation | Sections 4, 5, 7 |
| "Signal density percentage is useless" | Replaced with "Reliable/Partially reliable/Large gaps" and action guidance | Sections 3, 4 |
| "No quick diagnosis mode" | L1 snapshot + intraday query scenario | Section 4, Section 7.3 |

### 10.3 Compatibility with Existing Engine Principles

| Existing Principle | Manifestation in This Framework |
|---|---|
| Financial analysis is not the heaviest layer | L2 Panel 3 displays financial depth; Panel 1 only asks "should I care" |
| Industry determines weights | Four-dimension radar chart dimension weights determined by industry type |
| Layer-by-layer progression (L1 must be meaningful before progressing to L2) | L0->L1->L2 progressive expansion is consistent with this |
| Data gap = risk signal | Completeness indicator light visible at every layer |
| When two tracks conflict, prioritize Track A | Rating comparison directly displays divergence and gives interpretation |

### 10.4 Future Expansion Directions

1. **L0 Signal Card Configurability**: Allow users to customize "which types of signals I want to see, which I can ignore"
2. **L1 Snapshot Batch Comparison Mode**: Select 2-5 bonds, batch display their four-dimension radar charts with overlapping comparison (horizontal expansion of the existing multi-identity framework)
3. **L2 Deep Report Export Format**: Support PDF/Word export, directly usable as credit report base material
4. **L2 Report Version Management**: Traceable comparison of multiple analysis results for the same bond
5. **Morning Push Voice Version**: Once the API interface is open, can integrate voice broadcast -- "Good morning, today the portfolio has 3 red alerts, 7 yellow watches..." (this feature depends on TTS/NLP output, not within the current engine design scope)
