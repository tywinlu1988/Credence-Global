---
name: credit-analysis-router
description: Intake router for vague or compound fixed-income credit-analysis requests such as 'evaluate this company', 'check this portfolio for issues', 'what analysis should I run', 'where to start'. Use when the need is ambiguous, spans multiple roles (Credit Selector/Portfolio Manager/Advisor/Trader/Risk Officer/Individual Investor), or the user asks which analysis to run or where to start. If the user already names a concrete methodology task or engine path, use the fixed-income-credit-analysis skill instead.
---

## Purpose

**Engine version**: v0.0.7

**Non-Negotiables (see AGENTS.md)**: no analysis without a Path Sheet · no numbers without a `doc §section` citation · no report outside `dev/templates/` · no delivery without a QA Verdict · no invented dimensions or vocabulary.

Routing layer — does no analysis. Responsibility is three steps: interpret vague/compound needs → match a work path in `work-path-registry` → output a structured Path Sheet. This skill does not replicate any engine thresholds/weights/rating mappings; rule content uses engine documents as the single source of truth. After routing, hand off to the `fixed-income-credit-analysis` skill, which executes according to the Path Sheet's `engine_reading_order`.

## Intake Protocol (Four Questions, Progressive)

Clarify question by question. Allow skipping, multiple answers, or providing all information at once. If the user has already given sufficient information, skip the corresponding question; do not mechanically follow up.

- **Q1 Role**: What role are you deciding as? Credit Selector / Portfolio Manager / Advisor / Trader / Risk Officer / Individual Investor / Not sure (infer from the question characteristics and confirm with the user).
- **Q2 Object**: What is the analysis object? Single Issuer / Bond Portfolio / Industry / Full Market / Methodology Construction or Engine Validation.
- **Q3 Depth**: How deep an output do you need? L0 Quick Signal / L1 Decision Snapshot / L2 Deep Report / Special Report.
- **Q4 Data**: What data to use? Public data only (Mode A) / User explicitly provides external data sources (CSV/API/MCP → Mode B).

**Uncertainty default strategy**:
- Insufficient information → start from L0/L1, do not jump to L2 directly.
- Object unclear → default to Single Issuer.
- Role unclear → present 2 candidate paths for the user to choose; do not decide the path unilaterally.

## Routing Table

Match recommended paths by user input. `Status` column: ✅ active / 🟡 partial / 🔴 planned (under development — must be disclosed). For vague needs, do not give a path directly; go through the Four Questions protocol first.

| Scenario | Example User Statements | Recommended Path | Status | Alternative |
|---|---|---|---|---|
| Credit Selector single target | "Can our lending officer approve credit for X?" | WP-CS-01 | ✅ | WP-X-02 |
| Credit Selector special topic | "What about LGD, recovery rate, external support for this bond?" | WP-CS-02 | 🟡 | WP-CS-01 |
| Bond valuation | "Is this bond cheap/expensive, worth buying?" | WP-PM-01 | ✅ | WP-PM-02 |
| Dual-target comparison | "Which one to buy, LONGi or Yidao?" | WP-PM-02 | 🟡 | WP-X-02 |
| Underwriting advisory | "Can this bond be underwritten? What is the window?" | WP-AD-01 | 🔴 | WP-PM-01 |
| Market monitoring signal | "Give me today's market monitoring signal card." | WP-TR-01 | 🟡 | WP-RO-03 |
| Portfolio concentration | "Portfolio has too much solar exposure, how concentrated is it?" | WP-RO-01 | ✅ | WP-RO-04 |
| Contagion screening | "If sector X defaults, which holdings would be affected?" | WP-RO-02 | ✅ | WP-RO-01 |
| SRI reading | "What level is systemic risk at now?" | WP-RO-03 | ✅ | WP-TR-01 |
| Stress testing | "How much would the portfolio lose under extreme scenarios?" | WP-RO-04 | 🟡 | WP-RO-01 |
| Financing advisory | "Should this company issue bonds or take a loan? When to raise?" | WP-II-01 | 🔴 | WP-CS-01 |
| Backtest validation | "How accurate was this framework historically?" | WP-X-01 | ✅ | WP-X-02 |
| Multi-role parallel | "Evaluate X from Credit Selector/PM/Risk Officer perspectives simultaneously." | WP-X-02 | ✅ | WP-CS-01 |
| Industry framework building | "Help me build an analytical framework for a new industry." | WP-X-03 | ✅ | WP-CS-01 |
| ESG scan | "Check this company's governance and ESG risks." | WP-X-04 | 🟡 | WP-CS-01 |
| Outlook monitoring | "Give X a rating outlook and keep monitoring." | WP-X-05 | 🟡 | WP-CS-01 |
| Vague need | "Evaluate this company" / "What analysis should I do?" | Four Questions protocol | — | — |

## Path Sheet Output

After the four questions converge, output the following YAML. Fields align with the registry schema; `path_id` must exist in the registry; `engine_reading_order` is the sequence of engine documents registered for that path.

Template:

```yaml
role: ""                    # Credit Selector|Portfolio Manager|Advisor|Trader|Risk Officer|Individual Investor
object: ""                  # single-issuer|portfolio|industry|market|meta
depth: ""                   # L0|L1|L2|special
mode: ""                    # A=public data only / B=user explicitly provides external data sources
path_id: ""                 # work path ID that exists in the registry
engine_reading_order: []    # engine document sequence registered for this path (single source of truth)
templates: []               # copied from the registry entry's templates field (no ad-hoc substitutes)
quality_gates: []           # "rule name (dev/engine/<doc>.md §section)"
notes: ""
```

The `templates` field is **copied from the registry entry** — downstream stages render exactly these templates from `dev/templates/`; designing ad-hoc report layouts is a protocol violation (AGENTS.md Non-Negotiables #3).

Example (Credit Selector single target, public data only, L2 Deep Report):

```yaml
role: credit-selector
object: single-issuer
depth: L2
mode: A
path_id: WP-CS-01
engine_reading_order:
  - dev/engine/industry-framework.md
  - dev/engine/mosaic-engine.md
  - dev/engine/dual-track-methodology.md
quality_gates:
  - "Signal Density (dev/engine/mosaic-engine.md §4.3)"
  - "Veto (dev/engine/industry-framework.md §5)"
  - "Cross-Validation (dev/engine/dual-track-methodology.md §4)"
notes: "If information is insufficient, downgrade to L1 Decision Snapshot with a data gap inventory."
```

## Guardrails

- **Do not replicate engine content**: This skill only references path IDs and document names/sections; it does not replicate any thresholds, weights, or rating mappings. Rule content is always determined by the engine documents pointed to by `engine_reading_order`.
- **Mode B guardrail**: When the user has not explicitly provided data sources (CSV/API/MCP), `mode` must not be set to B; all Mode B fields are treated as data gaps; do not fabricate external data values.
- **Planned paths must be disclosed**: When recommending a 🔴 planned path (e.g., WP-AD-01, WP-II-01), must explicitly state "this path is under development" and provide an alternative active path; do not misrepresent capability.
- **Route then hand off**: Once the Path Sheet is produced, switch to the `fixed-income-credit-analysis` skill, read engine documents in `engine_reading_order` and execute; validate quality gates per `quality_gates`. (Since v0.0.1 the execution skill is driven by the Path Sheet for reading order; without a Path Sheet, fall back to the core set `engine-overview.md` + `dual-track-methodology.md` + topic-specific documents requested.)

## Chaining

- **Downstream (REQUIRED NEXT SUB-SKILL)**: `fixed-income-credit-analysis` — after producing the Path Sheet, hand off to this skill for analysis execution; the four-stage chain artifact contract is at `dev/engine/pipeline-contract.md`.

## References

- `references/work-paths.md` — Work path routing view (summary table, with status and one-line trigger characteristics)
- `dev/engine/work-path-registry.md` — Work path registry (single source of truth)
