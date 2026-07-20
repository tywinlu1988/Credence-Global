# Industry Scoring (Track A)

**Version**: v0.0.2

> This document is derived from `fixed-income-credit-analysis` SKILL.md, organizing Track A industry scoring content (industry pyramids / six paradigms / ten-dimension scoring / industry selection). The single source of truth for thresholds, weights, and one-shot veto conditions is `dev/engine/industry-framework.md`; this file is for navigation and organization only and introduces no new values.

## Track A: Industry Analysis Pyramids

Each industry type has a different heaviest factor. Weights determined by 10-dimension scoring.

| Industry Type | Conditions | L1 (Heaviest) | L2 | L3 | L4 (Lightest) |
|---|---|---|---|---|---|
| Policy-Driven | D3>=4, D4>=3 | 35% Policy/Macro | 30% Technology | 20% Supply Chain | 15% Financial |
| Tech-Barrier | D7>=3, D9>=3 | 20% Policy | 35% Tech/IP/Registration | 25% Operations | 20% Financial |
| Consolidation | D2<=3, D10>=3 | 25% Survival | 20% Technology | 30% Profit Fortress | 25% Financial |
| Asset-Lease | D5>=4, D8>=3 | 15% Policy | 20% Technology | 35% Client/Lease | 30% Financial |

**Semiconductor uses a 5-layer pyramid** (L1 Geopolitics 30-35% / L2 Technology 25-30% / L3 Market 15-20% / L4 Policy 10-15% / L5 Financial 5-10%).

**NEV uses dual-track** (OEM survival model vs supply chain profit fortress model — completely separate frameworks).

Each layer scores 0-10. Each layer has one-shot veto conditions (see `dev/engine/industry-framework.md`).

## Six Analytical Paradigms + LGFV Special Category

This section introduces **6 analytical paradigms + 1 special category (LGFV)**: the six general paradigms describe the credit contagion structure of ordinary industries. LGFV is listed separately due to its unique government credit binding mechanism, and is not forced into the six paradigms, but still participates in industry clustering analysis within the contagion matrix.

> **Note**: The 6 analytical paradigms are conceptual tools for contagion clustering and industry grouping; they differ from the 4 industry types defined in `industry-framework.md` (used for setting pyramid weights). An industry may simultaneously satisfy characteristics of multiple paradigms. In such cases, the industry type from `industry-framework.md` serves as the basis for pyramid weights, while the paradigms serve as the basis for contagion analysis. When conflicts arise, use the priority rules from `industry-framework.md` §3.1.

| Paradigm | Primary Industries | Secondary Attributes | Heaviest Factor | Key Contagion Path |
|---|---|---|---|---|
| Policy-Driven | Solar/PV; Semiconductor (primary) | Semiconductor also Tech-Barrier | Policy/geopolitics cycle | Same-region SOE, same-industry |
| Tech-Barrier | High-end equipment; Biomedicine (primary); Medical devices; NEV-Supply Chain | Biomedicine also Policy-Driven; NEV-Supply Chain also Profit Fortress | Technology/IP/registration | Supplier-customer chain, same funding channel |
| Consolidation | NEV-OEM | — | Survival / profit fortress | Same-industry, credit-chain |
| Asset-Lease | Data centers (IDC/colocation primary) | Cloud/telecom hybrid as Network+Traffic | Client/lease quality | Supplier-customer chain, same funding channel |
| Brand+Channel | Food & beverage; Textile & apparel | — | Brand equity | Confidence collapse, same-industry |
| Network+Traffic | Transportation; Retail; Media/Internet; Data centers (cloud/telecom hybrid) | — | Network traffic | Supplier-customer chain, same funding channel |
| Special / Government Credit | LGFV | — | Regional fiscal health | Regional resonance, same funding channel |

See `dev/engine/industry-framework.md`, `dev/engine/paradigm-brand-channel.md`, and `dev/engine/paradigm-network-traffic.md` for detailed specs.

The **addressable dimension index** of the six paradigms + LGFV special category for M0–M5 roles is found in `dev/engine/dimension-registry.md` (each dimension's id, definition pointer, applicable industries, and consumption paths); this file does not duplicate its definitions or thresholds.

## Ten-Dimension Industry Scoring (D1-D10)

| # | Dimension | Definition |
|---|---|---|
| D1 | Market Size | Current domestic market size (not projected) |
| D2 | Growth Trajectory | Growth certainty over next 3-5 years |
| D3 | Policy Support | Clarity and continuity of national-level policy support |
| D4 | Policy Volatility | Frequency of policy change, risk of abrupt pivots |
| D5 | Capital Sustainability | Diversity and longevity of capital sources |
| D6 | Livelihood Linkage | Direct relationship to social stability and basic welfare |
| D7 | External Dependency | Dependence on foreign technology, equipment, materials, markets |
| D8 | Supply Chain Power Concentration | Bargaining power distribution in the value chain |
| D9 | Industry Lifecycle | Stage of industry development |
| D10 | Cyclicality | Sensitivity to macro/inventory/price cycles |

## Industry Selection Filters (C1-C4)

| Condition | Meaning | Hard Gate? |
|---|---|---|
| C1 Transaction Volume | Sufficient lending + bond/equity issuance | Yes |
| C2 Analytical Barrier | "Can't understand it just from financials" | Yes |
| C3 Practitioner Pain | Professionals actively seeking capability | No |
| C4 Data Credibility | Public data is fundamentally reliable | **Yes — hard gate** |
