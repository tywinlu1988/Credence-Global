# Layered Output Framework — Product Design Specification — Appendix

> Appendix to `output-layered-framework.md` — version tracks the parent document; reference
> material (worked examples, derivations, historical validation) moved here in
> the 2026-07 restructure. Read on demand.

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
