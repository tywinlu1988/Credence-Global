# System-Intelligence Layer

**Version**: v0.0.5

> This document is derived from `fixed-income-credit-analysis` SKILL.md, organizing the system-intelligence layer (cross-industry contagion / five-dimensional concentration / systemic risk index) content. The single sources of truth for algorithms and thresholds are `dev/engine/systemic-warning-framework.md`, `dev/engine/contagion-matrix.md`, and `dev/engine/concentration-framework.md`; this file is for navigation and organization only and introduces no new values.

The system-intelligence layer aggregates individual issuer assessments into portfolio- and market-level signals.

## Cross-Industry Contagion

- **Contagion theory**: four contagion types (credit-chain, regional resonance, liquidity squeeze, confidence collapse) and seven standard transmission paths.
- **Contagion matrix**: 19×19 industry intensity matrix with direction, confidence, and upgrade-factor linkage. See `dev/engine/contagion-matrix.md`.
- **Industry clustering**: based on six analytical paradigms. Industries in the same paradigm have higher innate contagion coupling.

## Five-Dimensional Concentration Framework

Concentration risk is scored across:

1. **Industry concentration** (HHI, CR3, CR5, MAX1)
2. **Regional concentration** (single-province share, weak-region share, fiscal-health-weighted share)
3. **Rating concentration** (external AAA share, pseudo-high-rating share, internal-external rating dispersion)
4. **Tenor concentration** (12/24/36-month maturities, single-month peak)
5. **Funding-channel concentration** (bank, bond, non-standard, leasing, equity)

Suggested default weights (adjustable per `concentration-framework.md` §8.4): industry 25%, region 20%, rating 20%, tenor 20%, funding channel 15%.

## Systemic Risk Index (SRI)

```
SRI = Σ(industry_risk_score × industry_weight_pct)
```

- Scale: 0–3+
- Levels: 🟢 normal (<0.5), 🟡 watch (0.5–1.0), 🟠 alert (1.0–1.8), 🔴 danger (≥1.8)
- Inputs: Track-A industry score, Track-B market signal, outlook direction, and one-shot-veto triggers.

For full specification see `dev/engine/systemic-warning-framework.md`.
