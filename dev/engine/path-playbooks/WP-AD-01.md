# WP-AD-01 Execution Contract — Advisor Origination Assessment

**Status**: ✅ active · **Role**: advisor · **Object**: single-issuer · **Depth**: special

> This playbook is the execution contract for WP-AD-01. Read it fully before starting.
> AGENTS.md Non-Negotiables apply. This path assesses whether a bond issuance is feasible;
> it requires a completed WP-CS-01 rating as prerequisite.

## 1. Trigger & Scope

Use when: underwriter/advisory perspective on bond issuance feasibility ("can we underwrite this bond", "what price for this new issue", "is now a good window for issuance", "investor matching for this credit").
Do not use when: credit rating (→ WP-CS-01 first), portfolio-level view (→ WP-PM-01), market timing without credit context (→ WP-TR-01), financing channel comparison from issuer side (→ WP-II-01).

## 2. Required Reading Order

**Must read (core rules):**
1. `dev/engine/advisor-origination-framework.md` §§1-4 — issuance window (three-dimension), investor matching (five-segment), comparable pricing (five-factor adjustment)
2. `dev/engine/advisor-origination-framework.md` §§5-6 — decision framework and quality gates; read when assembling the origination conclusion

**Reference (read on demand):** none beyond the above.

## 3. Procedure

1. **Verify prerequisite** — WP-CS-01 rating must be complete. The origination assessment uses the issuer's credit rating as its foundation.
2. **Assess issuance window** — Per `advisor-origination-framework.md` §2, score three dimensions (market conditions 40%, issuer timing 35%, demand signals 25%). Apply sub-indicators: benchmark rate trend, credit spread environment, primary market volume, central bank posture. Check refinancing urgency override.
3. **Match investors** — Per §3, map the proposed bond to five investor segments. Score each segment 0-2 (strong/partial/no match). Apply ESG exclusion overlay deduction if applicable. Compute matching composite.
4. **Price comparables** — Per §4, select 3-5 comparable bonds (industry, rating ±2 notches, tenor ±2 years, same currency/jurisdiction). Apply five-factor pricing adjustment. Output recommended range (asymmetric: [median − 5bp, median + 10bp]).
5. **Conclude** — Per §5, determine Go / Conditional / No-Go. Produce sensitivity table: bull/base/bear pricing.
6. **Output** — underwriting feasibility conclusion, pricing range.

## 4. Dimension Vocabulary

- Window grades: Open / Conditional / Narrow / Closed per §2.2.
- Investor types: IG Institutional, Total Return Funds, Bank Treasury, Retail/Private Banking, ETF/Passive per §3.1.
- Pricing factors: rating differential, tenor differential, size differential, market drift, issuer-specific premium per §4.2.
- Origination outcomes: Go / Conditional / No-Go per §5.1.

## 5. Output Shape

Analysis Artifact per `dev/engine/pipeline-contract.md` §2.2.
Path outputs (registry): underwriting feasibility conclusion, pricing range.

## 6. Templates

- `dev/templates/template-type16.html` — Origination Feasibility Report

Render via `credit-report-builder` using exactly this file; no ad-hoc layouts.

## 7. Quality Gates (all must pass)

- `Issuance Window (dev/engine/advisor-origination-framework.md §2)`
- `Investor Matching (dev/engine/advisor-origination-framework.md §3)`
- `Comparable Pricing (dev/engine/advisor-origination-framework.md §4)`

## 8. Drift Blacklist (forbidden)

- Running origination assessment without a completed WP-CS-01 rating.
- Fabricating comparable bond pricing data (spreads, issuance dates, oversubscription ratios) — Mode B: require explicit data source.
- Inventing investor demand data (fund flows, survey sentiment) without a cited public source.
- Setting pricing range without the five-factor adjustment methodology (§4.2).
- Recommending "Go" when window is Closed or demand is Insufficient (§5.1 conditions).
- Applying the Go/No-Go framework to equity or structured products (bond origination only).
- Numeric claims without a `doc §section` citation.
- Designing ad-hoc HTML/dashboards/templates.
- Delivering before `credit-qa-verifier` issues a passing QA Verdict.
