# Industry Scoring (Track A)

**Version**: v0.0.2

> This document is derived from `fixed-income-credit-analysis` SKILL.md, organizing Track A industry scoring content. The single source of truth is `dev/engine/industry-framework.md` (ten-dimension scoring, six paradigms, pyramids, veto); this file is for navigation and organization only and introduces no new values.

## Track A: Ten-Dimension Scoring (D1-D10)

Each industry is scored on a 1-5 scale across ten structural dimensions. Definitions and scoring guides: `industry-framework.md` §1.

| # | Dimension | # | Dimension |
|---|---|---|---|
| D1 | Industry Lifecycle & Cyclicality | D6 | Customer Concentration & Bargaining Power |
| D2 | Competitive Intensity (Porter's 5 Forces) | D7 | Supply Chain Vulnerability |
| D3 | Regulatory & Policy Risk | D8 | Geographic & Sovereign Exposure |
| D4 | Technology Disruption Risk | D9 | ESG & Climate Transition Risk |
| D5 | Capital Intensity & Financing Dependency | D10 | Barriers to Entry / Moat Durability |

## Six Analytical Paradigms (P1-P6)

Every industry covered by the engine is assigned one of six analytical paradigms (single source of truth: `industry-framework.md` §2-§3; the 19-industry GICS bridge is in its §3.1a). Each paradigm carries its own ten-dimension weight template, four-layer pyramid, and paradigm-specific veto triggers:

| Paradigm | Core Industries (GICS) | Pyramid & Veto Spec |
|---|---|---|
| P1 Cyclical | Energy, Chemicals, Metals & Mining, Construction Materials, Capital Goods, Commercial Services, Automobiles, Consumer Durables, Retail | `industry-framework.md` §2.1 |
| P2 Defensive | Consumer Staples, Healthcare Equipment | `industry-framework.md` §2.2 (+ application note `paradigm-brand-channel.md`) |
| P3 Growth | Technology Hardware (Semis), Software & Services, Biotech & Pharma | `industry-framework.md` §2.3 |
| P4 Regulated Utility | Transportation, Utilities, Telecommunications | `industry-framework.md` §2.4 (+ application note `paradigm-network-traffic.md`) |
| P5 Financial | Financials (Banks/Insurance) | `industry-framework.md` §2.5 (+ dedicated `financial-bond-framework.md`) |
| P6 Sovereign-Linked | Sovereigns & GSEs | `industry-framework.md` §2.6 (+ dedicated `external-support-framework.md`) |

**Paradigm determination**: follow `industry-framework.md` §3 (GICS mapping §3.1, decision tree §3.2, conflict resolution §3.3, special structures §3.4 — e.g., Semiconductors as layered P3 + P1 overlay, Automobiles as P1 + P3 overlay).

## Industry Pyramids

Scoring follows a strict layer-by-layer progression (heaviest layer first; layers cannot be skipped):

- **Four-layer pyramids (L1-L4)**: weights and key indicators per paradigm in `industry-framework.md` §2.1-§2.6 and §4.2-§4.3.
- **Five-layer special structures** (§4.4): Semiconductors (L1 Geopolitical/Trade 25% / L2 Technology & Roadmap 25% / L3 Market Position 20% / L4 Capital & Financing 15% / L5 Financial 15%).

## Veto Mechanism

Each layer/paradigm carries one-vote veto conditions: when triggered, the composite rating ceiling is locked at CCC. Trigger lists and waiver criteria: `industry-framework.md` §5.
