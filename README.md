# Credence — Fixed-Income Credit Intelligent Analysis Engine (v0.0.8)

> **A methodology-first credit analysis engine for global fixed-income markets** — the
> methodology of a seasoned credit analyst, packaged as **Agent Skills** an AI agent can
> load and execute directly. Not an agent framework, not a standalone app: a
> domain-methodology skill pack for institutional-grade, reproducible credit analysis.

**Version** v0.0.8 · **License** MIT (see `LICENSE`) · **27 methodology documents** ·
**4 executable engines** · pytest regression suite + consistency gates

---

## Why Credence

Traditional analysis assumes credit risk lives in the financial statements. That assumption
fails exactly where it matters most: policy-driven industries (solar, semiconductors),
technology-moat industries (advanced equipment, biopharma), and asset-lease structures
(data centers, infrastructure REITs) — **the heaviest credit factors are never on the
balance sheet**. External ratings lag real deterioration by 17+ months on average
(Enron, Lehman, Wirecard, Greece — all investment grade months before default).

Credence is built on two foundations:

- **Mosaic Theory** — single public data fragments are meaningless in isolation; assembled,
  they form the full picture. The engine aggregates, stacks, and confidence-weights signals.
- **Information Completeness Theory** — data gaps are not defects, they are risk signals.
  Every conclusion ships with a data-completeness score and an explicit gap list.

## Architecture at a Glance

```
System-Intelligence Layer (Layer 4)
  Contagion Map x Concentration Dashboard x Systemic Risk Index (SRI)
                        |
                  Single-Issuer Results
                        |
              +---------+---------+
              |   Mosaic Engine   |   Signal extraction + assembly + completeness
              |    (Layer 1)      |
              +---------+---------+
                        |
           +------------+------------+
           |            |            |
      Track A       Track B      Track C+: Multi-Stakeholder
    Fundamental    Market         6 Buy-Side Roles
     Analysis      Pricing
           |            |
           +------+-----+
                  v
       Cross-Validation Matrix
```

## The Four-Stage Skill Chain

| Stage | Skill | Role |
|---|---|---|
| 1 | `credit-analysis-router` | Intake: classifies the subject, issues the **Path Sheet** (paradigm, work path, engines, templates) |
| 2 | `fixed-income-credit-analysis` | Executes the Path Sheet against the 27 engine documents — no Path Sheet, no analysis |
| 3 | `credit-report-builder` | Renders conclusions into the fixed Type 1-15 report templates |
| 4 | `credit-qa-verifier` | Process + result compliance gate: template, citation, dimension, and chain checks — no verdict, no delivery |

Six international paradigms (P1 Cyclical / P2 Defensive / P3 Growth / P4 Regulated Utility /
P5 Financial / P6 Sovereign-Linked), each with executable work paths and per-path playbooks.

## Install

**Claude Code plugin (recommended):**

```
/plugin marketplace add tywinlu1988/Credence-Global
/plugin install credence@credence-marketplace
```

**Open as a project (Model A — works in Claude Code / Codex / Cursor / Gemini / OpenCode):**
unzip the release package and open the package root as your project folder. Entry point:
`AGENTS.md`. Zero configuration. See **`INSTALL.md`** for all install routes, including
`npx github:tywinlu1988/credence-global`.

## Quick Start

Once installed or opened, just describe the subject:

> "Analyze the credit profile of <issuer>, a European utility with BB- outlook, for a
> 5-year senior unsecured bond."

The router classifies it, issues a Path Sheet, and the chain takes it from there —
every number cited to an engine document, every report rendered from the fixed templates,
every delivery gated by QA.

## Package Contents

- `.claude/skills/` — Four-stage chain skills (router / analysis / report / qa)
- `engine/` — 27 methodology documents: thresholds, weights, rating maps, contagion matrix
  (the single source of truth; coded engines parse rules from these at runtime)
- `engine/path-playbooks/` — Per-work-path execution contracts (procedure, dimension
  vocabulary, output shape, quality gates, drift blacklist)
- `templates/` — Type 1-15 report templates + machine-generated `index.yaml`
- `src/` — Executable orchestrator + 4 coded engines (Concentration, Contagion, SRI, Outlook)
- `adapters/` — Tool-specific deep adapter guidance

## Links

- Repository & full documentation: <https://github.com/tywinlu1988/Credence-Global>
- Issues: <https://github.com/tywinlu1988/Credence-Global/issues>

## Disclaimer

Credence is a methodology demonstration and analysis aid. It is **not investment advice**,
produces no rating-agency opinion, and is provided **AS IS** without warranty of any kind
under the MIT License.
