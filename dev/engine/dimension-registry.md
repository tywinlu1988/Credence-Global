# Dimension Registry

**Version**: v0.0.3 | **Date**: 2026-07-18

This registry objectifies the engine's **analysis dimensions** into addressable, machine-readable entries: **6 analysis paradigms (P1-P6)**, and **6 stakeholder role types**. It serves as the unified index layer for "route-by-dimension / search-by-dimension" in the v0.0.1 skill architecture.

**Single Source of Truth Principle**: This registry is a **pointer layer** -- it only registers each dimension as an addressable entry (id + pointer to the defining document + applicable industries + which work paths consume it). It does **not copy** any definition text, thresholds, or weights. The judging criteria, pyramid weights, veto rules, etc., for each dimension are always ultimately governed by the corresponding section of the engine document referenced by `definition`. If any inconsistency arises between this registry and those engine documents, the engine documents prevail.

## Table of Contents

1. [Analysis Paradigm Dimensions](#1-analysis-paradigm-dimensions)
2. [Stakeholder Role Dimensions](#2-stakeholder-role-dimensions)
3. [Schema and Traceability Conventions](#3-schema-and-traceability-conventions)

## 1. Analysis Paradigm Dimensions

Each entry corresponds to an analysis paradigm (P1-P6). The `industries` field reflects the **primary paradigm** assignment in the contagion matrix (single source of truth: [contagion-matrix.md](contagion-matrix.md) §1.2 Paradigm Mapping Table). Secondary paradigm attributes (e.g., semiconductor also has P1 attributes) are not expanded here and are governed by that mapping table's "Secondary Paradigm" column.

```yaml
dimensions:
  - id: paradigm-P1
    name: Cyclical
    letter: P1
    definition: Cyclical (dev/engine/industry-framework.md §3)
    standalone_doc: embedded in dev/engine/industry-framework.md §3 (determination) and §4 (pyramid weights)
    industries: [Energy (Oil & Gas), Chemicals, Metals & Mining, Construction Materials, Capital Goods, Commercial Services, Automobiles, Consumer Durables, Retail]
    used_by_paths: [WP-CS-01, WP-PM-02, WP-X-02, WP-X-03]

  - id: paradigm-P2
    name: Defensive
    letter: P2
    definition: Defensive (dev/engine/industry-framework.md §3)
    standalone_doc: embedded in dev/engine/industry-framework.md §3 (determination) and §4 (pyramid weights) + application note dev/engine/paradigm-brand-channel.md
    industries: [Consumer Staples, Healthcare Equipment]
    used_by_paths: [WP-CS-01, WP-PM-02, WP-X-02, WP-X-03]

  - id: paradigm-P3
    name: Growth
    letter: P3
    definition: Growth (dev/engine/industry-framework.md §3)
    standalone_doc: embedded in dev/engine/industry-framework.md §3 (determination) and §4 (pyramid weights)
    industries: [Technology Hardware (Semis), Software & Services, Biotech & Pharma]
    used_by_paths: [WP-CS-01, WP-PM-02, WP-X-02, WP-X-03]

  - id: paradigm-P4
    name: Regulated Utility
    letter: P4
    definition: Regulated Utility (dev/engine/industry-framework.md §3)
    standalone_doc: embedded in dev/engine/industry-framework.md §3 (determination) and §4 (pyramid weights) + application note dev/engine/paradigm-network-traffic.md (network/throughput lens)
    industries: [Transportation (Air/Rail/Shipping), Utilities (Regulated), Telecommunications]
    used_by_paths: [WP-CS-01, WP-PM-02, WP-X-02, WP-X-03]

  - id: paradigm-P5
    name: Financial
    letter: P5
    definition: Financial (dev/engine/industry-framework.md §3)
    standalone_doc: embedded in dev/engine/industry-framework.md §3 (determination) and §4 (pyramid weights) + dedicated framework dev/engine/financial-bond-framework.md
    industries: [Financials (Banks/Insurance)]
    used_by_paths: [WP-CS-01, WP-PM-02, WP-X-02, WP-X-03]

  - id: paradigm-P6
    name: Sovereign-Linked
    letter: P6
    definition: Sovereign-Linked (dev/engine/industry-framework.md §3)
    standalone_doc: embedded in dev/engine/industry-framework.md §3 (determination) and §4 (pyramid weights) + dedicated framework dev/engine/external-support-framework.md
    industries: [Sovereigns & GSEs]
    used_by_paths: [WP-CS-01, WP-PM-02, WP-X-02, WP-X-03]

```

## 2. Stakeholder Role Dimensions

Each entry corresponds to a stakeholder role type. The core decision question, decision time horizon, key data requirements, etc., for each role are defined in [multi-stakeholder.md](multi-stakeholder.md) §1 (Six Stakeholder Types Overview). The `used_by_paths` field aggregates by the `role` field of each path in the work path registry.

```yaml
roles:
  - id: role-credit-selector
    name: Credit Selector
    definition: Credit Selector (dev/engine/multi-stakeholder.md §1)
    used_by_paths: [WP-CS-01, WP-CS-02]

  - id: role-portfolio-manager
    name: Portfolio Manager
    definition: Portfolio Manager (dev/engine/multi-stakeholder.md §1)
    used_by_paths: [WP-PM-01, WP-PM-02]

  - id: role-advisor
    name: Advisor
    definition: Advisor (dev/engine/multi-stakeholder.md §1)
    used_by_paths: [WP-AD-01]

  - id: role-trader
    name: Trader
    definition: Trader (dev/engine/multi-stakeholder.md §1)
    used_by_paths: [WP-TR-01]

  - id: role-risk-officer
    name: Risk Officer
    definition: Risk Officer (dev/engine/multi-stakeholder.md §1)
    used_by_paths: [WP-RO-01, WP-RO-02, WP-RO-03, WP-RO-04]

  - id: role-individual-investor
    name: Individual Investor
    definition: Individual Investor (dev/engine/multi-stakeholder.md §1)
    used_by_paths: [WP-II-01]
```

## 3. Schema and Traceability Conventions

### Dimension Entry Fields (dimensions)

| Field | Type | Description |
|---|---|---|
| `id` | string | Dimension unique identifier: `paradigm-{P1..P6}` |
| `name` | string | Dimension name (Cyclical / Defensive / Growth / Regulated Utility / Financial / Sovereign-Linked) |
| `letter` | string | Paradigm identifier `P1`-`P6` |
| `definition` | string | Definition pointer, format `keyword (doc-path §section)` (see traceability convention below) |
| `standalone_doc` | string | Where the full specification resides: repository root relative path to standalone paradigm document, or `embedded in ...` (indicating the specification is embedded within industry-framework.md) |
| `industries` | string[] | Industries covered by this paradigm as primary paradigm (consistent with the primary paradigm column in contagion-matrix.md §1.2) |
| `used_by_paths` | string[] | Work path IDs that consume this dimension (from work-path-registry.md) |

### Role Entry Fields (roles)

| Field | Type | Description |
|---|---|---|
| `id` | string | Role unique identifier: `role-{credit-selector|portfolio-manager|advisor|trader|risk-officer|individual-investor}` |
| `name` | string | Role name (Credit Selector / Portfolio Manager / Advisor / Trader / Risk Officer / Individual Investor) |
| `definition` | string | Definition pointer, format `keyword (doc-path §section)` (see traceability convention below) |
| `used_by_paths` | string[] | Work path IDs for which this role serves as the `role` field (from work-path-registry.md) |

### `definition` Traceability Convention

The `definition` field follows the same traceability convention as the work path registry's `quality_gates`: the **keyword** before `(` must be a term that actually exists in and can be traced by grep within the referenced document (enforced by consistency testing). The parentheses contain `repository-root-relative doc-path + §section`. The `§section` is for human-reading navigation and is not machine-validated.

### `used_by_paths` Aggregation Scope

- **Paradigm dimensions**: The work path registry's `paradigm_selection` field references the paradigm set as a whole via "six paradigms (per industry mapping table)" (collective granularity, rather than naming individual paradigms). Therefore, all paths that select this mapping table -- WP-CS-01, WP-PM-02, WP-X-02, WP-X-03 -- are counted against every paradigm dimension. Paths with `paradigm_selection` set to `n/a` or `TBD` do not consume paradigm dimensions.
- **Role dimensions**: Directly aggregated by the `role` field of each path in the work path registry. Cross-role paths with `role: meta` (WP-X-*) are not attributed to any single role dimension.

> **Deferred Item (back-reference)**: The originally planned optional change "work-path-registry `paradigm_selection` may reference dimension IDs" (path-to-dimension reverse pointer) **is not implemented in this version**. Because the registry's `paradigm_selection` references the paradigm set as a whole (collective granularity, rather than naming individual paradigms), reverse pointers cannot provide finer granularity than the existing `used_by_paths`. Therefore, the status quo is maintained. The forward aggregation from dimensions to paths (this section's scope + consistency testing enforced reconciliation) already meets routing and addressing needs. If future `paradigm_selection` is changed to reference paradigms individually, reverse pointers will be added at that time.

## Related Content

- [Industry Classification and Analysis Framework](industry-framework.md) -- Six paradigm determination (§3) / Industry pyramid specifications (§4)
- [Financial Paradigm (P5)](industry-framework.md) — Paradigm P5 full specification (Financials: Banks/Insurance)
- [Sovereign-Linked Paradigm (P6)](industry-framework.md) — Paradigm P6 full specification (Sovereigns, sub-sovereigns, GSEs, DFIs)
- [19-Industry Contagion Matrix](contagion-matrix.md) -- §1.2 Paradigm Mapping Table (industry to primary/secondary paradigm)
- [Multi-Stakeholder Perspective Framework](multi-stakeholder.md) -- Role definitions (§1)
- [Work Path Registry](work-path-registry.md) -- Each path's role and paradigm_selection
