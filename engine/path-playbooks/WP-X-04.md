# WP-X-04 Execution Contract — ESG / Governance Risk Scan

**Status**: ✅ active · **Role**: meta · **Object**: single-issuer · **Depth**: special

> This playbook is the execution contract for WP-X-04. Read it fully before starting.
> AGENTS.md Non-Negotiables apply. This path scans for ESG and governance red flags;
> it can run standalone or as a supplement to a WP-CS-01 main rating.

## 1. Trigger & Scope

Use when: the user needs an ESG risk scan ("any ESG red flags on this issuer", "governance risk check", "fraud indicators for this company"), or a governance/fraud supplement to a credit rating.
Do not use when: full credit rating (→ WP-CS-01), industry framework building (→ WP-X-03), black-swan validation (→ WP-X-01).

## 2. Required Reading Order

**Must read (core rules):**
1. `${CLAUDE_PLUGIN_ROOT}/engine/esg-framework.md` §§2-5 — ESG scoring dimensions, risk assessment, mapping rules, red-flag triggers
2. `${CLAUDE_PLUGIN_ROOT}/engine/governance-fraud-risk.md` §§1-2 — financial fraud red flags; §4 — earnings management and manipulation signals

**Reference (read on demand):**
- `${CLAUDE_PLUGIN_ROOT}/engine/esg-framework.md` §1 — conceptual background (read on first encounter)
- `${CLAUDE_PLUGIN_ROOT}/engine/governance-fraud-risk.md` §3, §§5-7 — case studies and extended discussion

## 3. Procedure

1. **ESG baseline** — Per `esg-framework.md` §1, assess the issuer across the three ESG pillars (Environmental, Social, Governance). Each pillar is scored independently; red-flag triggers are defined per pillar. A red flag in any pillar elevates the overall ESG risk profile.
2. **Environmental scan** — Check for sector-specific environmental risk factors (carbon-intensive industries, regulatory exposure, environmental liabilities). Flag if the issuer operates in a high-risk sector without disclosed mitigation.
3. **Social scan** — Check for labor relations, community impact, supply-chain ethics, and regulatory/social license risks. Flag if social controversies are documented or regulatory actions are pending.
4. **Governance scan** — Check board structure, ownership concentration, related-party transactions, audit quality, and shareholder rights. Flag if governance weaknesses are present per `esg-framework.md` governance factors.
5. **Financial fraud detection** — Per `governance-fraud-risk.md` §1, run the 20+ fraud signal checklist: accounting anomalies (aggressive revenue recognition, capitalisation of expenses, off-balance-sheet exposures), governance red flags (auditor changes, executive turnover, related-party opacity), and market-based signals (CDS spread divergence, short-interest spikes).
6. **Earnings management scan** — Per `governance-fraud-risk.md` §4, check for earnings management and manipulation signals: aggressive revenue recognition, expense capitalisation, off-balance-sheet exposures, channel stuffing, reserve manipulation. Flag any matching patterns.
7. **Synthesize red-flag list** — Aggregate findings into a structured ESG risk scan + governance red-flag list. Each flag must cite the specific detection signal from the engine documents.
8. **Output** — ESG risk scan (three-pillar assessment), governance red-flag list.

## 4. Dimension Vocabulary

- ESG pillars: Environmental, Social, Governance per `esg-framework.md` §1 only.
- Fraud signals: the 20+ signals in `governance-fraud-risk.md` §1 — do not invent new fraud indicators.
- Earnings management patterns: the documented patterns in `governance-fraud-risk.md` §4.
- Rating scale: ESG risk profile uses High / Elevated / Moderate / Low per the engine documents — no invented grades.

## 5. Output Shape

Analysis Artifact per `${CLAUDE_PLUGIN_ROOT}/engine/pipeline-contract.md` §2.2.
Path outputs (registry): ESG risk scan, governance red-flag list.

## 6. Templates

- `${CLAUDE_PLUGIN_ROOT}/templates/template-type10.html` — ESG / Governance Scan

Render via `credit-report-builder` using exactly this file; no ad-hoc ESG dashboards.

## 7. Quality Gates (all must pass)

- `ESG (${CLAUDE_PLUGIN_ROOT}/engine/esg-framework.md §1)`
- `Financial Fraud Red Flag Checklist (${CLAUDE_PLUGIN_ROOT}/engine/governance-fraud-risk.md §1)`
- `Earnings Management and Manipulation Signals (${CLAUDE_PLUGIN_ROOT}/engine/governance-fraud-risk.md §4)`

## 8. Drift Blacklist (forbidden)

- Inventing ESG scoring dimensions, weights, or red-flag triggers beyond those defined in `esg-framework.md`.
- Fabricating fraud signals outside the 20+ defined in `governance-fraud-risk.md` §1.
- Attributing fraud without a specific signal match from the engine documents (every flag must cite a detection signal).
- Inventing earnings management signals not in `governance-fraud-risk.md` §4.
- Substituting ESG opinion for credit rating — the ESG scan is a supplement, not a standalone rating.
- Numeric claims without a `doc §section` citation.
- Designing ad-hoc HTML/dashboards/templates.
- Invoking Mode B without an explicit user-provided data source.
- Delivering before `credit-qa-verifier` issues a passing QA Verdict.
