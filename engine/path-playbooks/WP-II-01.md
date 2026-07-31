# WP-II-01 Execution Contract — Individual Investor Decision Support

**Status**: ✅ active · **Role**: individual-investor · **Object**: single-issuer · **Depth**: special

> This playbook is the execution contract for WP-II-01. Read it fully before starting.
> AGENTS.md Non-Negotiables apply. This path recommends financing channels and timing
> from the issuer's perspective; it requires a completed credit rating and market context.

## 1. Trigger & Scope

Use when: issuer-side financing decisions ("should we issue a bond or take a loan", "when is the best time to finance", "compare bond vs loan cost for this company", "what channel gives us the best terms").
Do not use when: credit rating (→ WP-CS-01 first), underwriter-side origination (→ WP-AD-01), market timing alone without channel comparison (→ WP-TR-01).

## 2. Required Reading Order

**Must read (core rules):**
1. `${CLAUDE_PLUGIN_ROOT}/engine/financing-channel-framework.md` §§1-4 — three-channel framework, six-factor comparison, timing assessment
2. `${CLAUDE_PLUGIN_ROOT}/engine/financing-channel-framework.md` §§5-6 — recommendation structure and quality gates; read when assembling the financing recommendation

**Reference (read on demand):** none beyond the above.

## 3. Procedure

1. **Verify prerequisite** — WP-CS-01 rating must be complete. Channel availability depends on the issuer's credit rating per §2.3 rating-based filter.
2. **Filter available channels** — Per §2.3, determine which channels are available at the issuer's rating. CCC or below: only private credit; D: none (restructuring only).
3. **Compute all-in cost** — Per §3.1, for each available channel, calculate all-in after-tax cost: benchmark/reference rate + spread/margin + annualised issuance costs − tax shield. Use same reference rate tenor and currency. Add cross-currency basis swap cost if currencies differ.
4. **Score six factors** — Per §2.2, score each channel on Cost (30%), Tenor Flexibility (20%), Execution Certainty (20%), Covenant Burden (15%), Disclosure Requirement (10%), Post-Issuance Flexibility (5%). Best channel per factor scores 10, worst scores 1, intermediate linear interpolation.
5. **Apply tie-break** — Per §3.3, if two channels score within 0.5 points, deduct 1.0 from private credit (visibility penalty).
6. **Assess timing** — Per §4, score five factors (window 30%, urgency 25%, rate environment 20%, rating momentum 15%, sector rotation 10%). Determine Accelerate / Maintain Flexibility / Delay.
7. **Produce recommendation** — Primary channel + secondary channel + timing + cost estimate + top 3 risks. Per §5.2, add rate-sensitivity (±50bp) and rating-change (1-notch) to the recommendation.
8. **Output** — financing channel comparison, timing recommendation.

## 4. Dimension Vocabulary

- Channels: Public Bond / Syndicated Loan / Non-Standard Private Credit per §2.1.
- Factors (6): Cost, Tenor Flexibility, Execution Certainty, Covenant Burden, Disclosure Requirement, Post-Issuance Flexibility per §2.2.
- Timing recommendations: Accelerate / Maintain Flexibility / Delay per §4.2.
- Rating-based filter: per §2.3 — use exact thresholds (AAA-A, BBB, BB-B, CCC-C, D).

## 5. Output Shape

Analysis Artifact per `${CLAUDE_PLUGIN_ROOT}/engine/pipeline-contract.md` §2.2.
Path outputs (registry): financing channel comparison, timing recommendation.

## 6. Templates

- `${CLAUDE_PLUGIN_ROOT}/templates/template-type17.html` — Financing Channel Comparison & Timing

Render via `credit-report-builder` using exactly this file; no ad-hoc layouts.

## 7. Quality Gates (all must pass)

- `Channel Comparison (${CLAUDE_PLUGIN_ROOT}/engine/financing-channel-framework.md §3)`
- `Timing Assessment (${CLAUDE_PLUGIN_ROOT}/engine/financing-channel-framework.md §4)`

## 8. Drift Blacklist (forbidden)

- Running channel comparison without a completed credit rating (WP-CS-01).
- Ignoring the rating-based channel filter (§2.3) — e.g., recommending public bond for a B-rated issuer.
- Fabricating all-in cost components (benchmark rates, spreads, margins, arrangement fees) — Mode B: require explicit data.
- Applying channel weights other than six-factor §2.2 (do not invent or drop factors).
- Skipping the visibility penalty on private credit when scores are within 0.5 points (§3.3).
- Recommending a channel for a D-rated issuer — no financing is available; state "restructuring only."
- Inventing timing factors outside the five in §4.1.
- Numeric claims without a `doc §section` citation.
- Designing ad-hoc HTML/dashboards/templates.
- Delivering before `credit-qa-verifier` issues a passing QA Verdict.
