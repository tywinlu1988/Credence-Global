# Financing Channel Comparison & Timing Framework

**Version**: v0.3.0 | **Date**: 2026-07-29 | **Status**: Published

**Module**: Fixed Income Credit Analysis Engine · Multi-Stakeholder Layer

---

> This document is the single source of truth for WP-II-01 (Individual Investor Decision
> Support). It defines the methodology for comparing financing channels — bond issuance,
> syndicated loan, and non-standard/private credit — and determining optimal financing
> timing and cost. All thresholds, weights, and decision rules are canonical.

---

> **Reading guide**: §§1-4 contain the executable methodology — thresholds,
> weights, scoring rules, and decision frameworks. These sections are required
> reading before executing any work path that references this document.
> §§5-6 contain the decision framework and quality gates — read when
> assembling the financing recommendation — read only when the analysis needs detailed justification
> or the user asks for methodological background.


## Table of Contents

- [1. Positioning in the Engine](#1-positioning-in-the-engine)
- [2. Financing Channel Framework](#2-financing-channel-framework)
- [3. Channel Comparison Methodology](#3-channel-comparison-methodology)
- [4. Timing Assessment](#4-timing-assessment)
- [5. Financing Recommendation](#5-financing-recommendation)
- [6. Quality Gates](#6-quality-gates)

---

## 1. Positioning in the Engine

### 1.1 Role

The individual investor (issuer-side) perspective asks: *"Should this company issue a bond,
take a bank loan, or use non-standard financing? And when?"* It applies the engine's credit
analysis in reverse — starting from the issuer's credit profile and market conditions,
recommending the optimal financing channel and timing.

### 1.2 Relationship to Other Paths

| Path | Relationship |
|---|---|
| WP-CS-01 (Single-Issuer Rating) | **Prerequisite** — channel comparison requires a credit rating |
| WP-AD-01 (Origination Assessment) | Complements — AD-01 asks "can we underwrite," II-01 asks "should the issuer choose this channel" |
| WP-RO-03 (SRI Reading) | Macro conditions affect relative channel attractiveness |
| WP-X-05 (Outlook Monitoring) | Rating outlook affects refinancing timing |

---

## 2. Financing Channel Framework

### 2.1 Three Channels

| Channel | Typical Tenor | Cost Metric | Key Advantages | Key Disadvantages |
|---|---|---|---|---|
| **Public Bond** | 3-30 years | Spread over benchmark (OAS / G-spread) | Deepest investor base, longest tenor, fixed-rate, covenant-light, public market discipline | High fixed costs (rating, legal, roadshow), disclosure burden, execution risk (market window) |
| **Syndicated Loan** | 1-7 years | Margin over reference rate (EURIBOR/SOFR + margin) | Relationship-based, flexible drawdown, shorter execution time, confidentiality, amend-and-extend flexibility | Shorter tenor, floating-rate exposure, bank credit risk concentration, covenant-heavy |
| **Non-Standard / Private Credit** | 1-10 years | All-in yield (variable, typically 300-800bp over benchmark) | Bespoke structure, rapid execution, accommodates complex situations, limited disclosure | Highest cost, opaque pricing, limited secondary liquidity, investor concentration |

### 2.2 Channel Selection Factors

| Factor | Weight | Bond | Loan | Private Credit |
|---|---|---|---|---|
| **Cost (all-in)** | 30% | 1-10 (lower = better) | 1-10 | 1-10 |
| **Tenor Flexibility** | 20% | 1-10 (longer = better) | 1-10 | 1-10 |
| **Execution Certainty** | 20% | 1-10 (lower risk = better) | 1-10 | 1-10 |
| **Covenant Burden** | 15% | 1-10 (lighter = better) | 1-10 | 1-10 |
| **Disclosure Requirement** | 10% | 1-10 (less = better) | 1-10 | 1-10 |
| **Post-Issuance Flexibility** | 5% | 1-10 (more = better) | 1-10 | 1-10 |

### 2.3 Rating-Based Channel Filter

| Internal Rating | Available Channels | Notes |
|---|---|---|
| AAA — A | **All three** | Deepest bond market access; loan pricing competitive |
| BBB | **Bond + Loan** | IG bond market accessible; private credit unattractive on cost |
| BB — B | **Loan + Private Credit** | Bond market largely closed (HY window-dependent); loan primary, private credit fallback |
| CCC — C | **Private Credit only** | Bond and loan markets closed; distress pricing applies |
| D | **None** | Default — no new financing; restructuring only |

---

## 3. Channel Comparison Methodology

### 3.1 Cost Calculation

For each available channel, compute the **all-in after-tax cost**:

**Bond**: Benchmark rate + spread + issuance costs (annualised over tenor) — tax shield
**Loan**: Reference rate + margin + commitment fee (undrawn portion) — tax shield
**Private Credit**: All-in yield + arrangement fee (annualised) + equity kicker value (if any) — tax shield

The comparison must use the same reference rate tenor and currency for all channels.
If the channels are in different currencies, include cross-currency basis swap cost.

### 3.2 Score Normalisation

For each factor, the best-performing channel scores 10; the worst scores 1. Intermediate
values are linearly interpolated. The channel with the highest weighted composite score
is the primary recommendation.

### 3.3 Tie-Breaking Rule

When two channels score within 0.5 points of each other, apply a **visibility penalty**
to the non-standard channel: deduct 1.0 point from the private credit score. This reflects
the structural opacity premium — private credit pricing is not publicly observable,
creating a hidden cost risk that the comparison framework must acknowledge.

---

## 4. Timing Assessment

### 4.1 Timing Factors

| Factor | Weight | Scoring |
|---|---|---|
| **Issuance Window** (per advisor-origination-framework §2) | 30% | Derived from WP-AD-01 window grade for the lead channel |
| **Refinancing Urgency** | 25% | 6+ months to maturity → 8-10; 3-6 months → 5-7; <3 months → 1-4 (urgency = lower score but mandatory action) |
| **Rate Environment** | 20% | Falling rate path → 1-3 (delay); Flat → 4-7; Rising → 8-10 (accelerate) |
| **Rating Momentum** | 15% | Upgrade expected within 6 months → 1-3 (delay to capture upgrade); Stable → 4-7; Downgrade expected → 8-10 (accelerate before downgrade) |
| **Sector Rotation** | 10% | Sector in favour (fund inflows, tightening spreads) → 8-10; Neutral → 4-7; Out of favour → 1-4 |

### 4.2 Timing Recommendation

| Composite Timing Score | Recommendation |
|---|---|
| 7.0-10.0 | **Accelerate** — launch within 4 weeks; window is open and issuer has tailwinds |
| 4.0-6.9 | **Maintain Flexibility** — prepare documentation (prospectus/facility agreement), launch within 3 months when conditions are favourable |
| 0.0-3.9 | **Delay** — do not launch now; review quarterly; consider bridge financing if refinancing is urgent |

---

## 5. Financing Recommendation

### 5.1 Output Structure

The recommendation combines channel comparison and timing assessment into a single
actionable output:

1. **Primary Channel**: Highest-scoring channel with weighted composite score
2. **Secondary Channel**: Runner-up (for negotiation leverage / fallback)
3. **Timing**: Accelerate / Maintain Flexibility / Delay with target launch window
4. **Cost Estimate**: All-in after-tax cost range for primary channel
5. **Key Risks**: Top 3 risks to the recommendation (e.g., "bond window closes before launch," "loan syndication fails due to bank credit constraints," "rate hike increases floating-rate cost")

### 5.2 Sensitivity

For the primary channel recommendation, produce a rate-sensitivity table:
- **±50bp rate shock**: Recalculate all-in cost and re-score channel comparison
- **1-notch rating change**: Recalculate rating-based channel filter and re-score if filter changes

---

## 6. Quality Gates

The following quality gates are defined for WP-II-01:

- **Channel Comparison (dev/engine/financing-channel-framework.md §3)** — six-factor weighted comparison with all-in after-tax cost calculation, tie-breaking rule, and visibility penalty
- **Timing Assessment (dev/engine/financing-channel-framework.md §4)** — five-factor timing composite with refinancing urgency and issuance-window linkage

---

## Related Content

- [Engine Architecture Overview](engine-overview.md)
- [Work Path Registry](work-path-registry.md) — WP-II-01 path definition
- [Advisor Origination Framework](advisor-origination-framework.md) — issuance window assessment (feeds timing)
- [Quantitative Analysis](reference/quantitative-analysis.md) — §7.4 issuance rate changes
- [Financial Deep Dive](financial-deep-dive.md) — capital structure analysis (feeds cost calculation)
