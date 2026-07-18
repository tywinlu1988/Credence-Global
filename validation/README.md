# Capability Validation Evidence Archive

**Nature**: Engine capability validation artifacts (test outputs and evidence archive)
**Attribution**: **Not a project component** · Never enters `version/` version snapshots

---

## What This Is

This directory contains the **capability validation artifacts** of the fixed income credit analysis engine — i.e., the **test outputs and evidence archives** of the engine across various industries and black swan cases. They serve as the "experimental records" of the engine methodology, used for retrospective review of the engine's analysis and early warning capabilities, **not project deliverables themselves**.

**Project Core** (engine methodology + templates + design/data specifications + product + skills) is located in the root-level `dev/` directory. This directory is completely separate from the core:

- **How to validate** (validation methodology, black swan retrospective, dual time point comparison methods) -> See `dev/engine/validation-methodology.md`, which belongs to the project core
- **What was validated** (72 actual test reports, false positive/false negative test execution records) -> Archived in this directory, **not part of the project core**

## Three Hard Constraints

1. The contents of this directory are **test outputs**, not project components
2. **Never enter `version/` version snapshots** — snapshot = full copy of `dev/`, validation artifacts are naturally excluded
3. The authenticity of engine capabilities is evidenced by this directory, but the existence of evidence does not constitute a functional statement of the project core

---

## Directory Index

### `reports/` — Industry/Case Validation Reports (72 reports, 15 subdirectories; only 2 methodology references public)

> **GitHub Public Scope**: This directory contains test outputs. The main repository only publishes 2 **industry methodology references** — `food-beverage/food-beverage-methodology.html`, `transportation/transportation-methodology.html` (referenced by `dev/engine/` paradigm documents in "Related Content"); the remaining 70 actual test reports are retained on the maintainer's local machine (test outputs, not deliverables), not on GitHub, and not in any version snapshot.

Organized by "13 industries + system intelligence layer + validation special topics":

| Subdirectory | Industry/Category | Report Count |
|---|---|---|
| `solar/` | Solar/Energy Storage | 11 |
| `semiconductor/` | Semiconductor/Integrated Circuits | 7 |
| `lgv/` | LGFV / Local Government Financing Vehicle | 6 |
| `food-beverage/` | Food & Beverage | 4 |
| `media-internet/` | Media/Internet | 4 |
| `nev/` | New Energy Vehicles | 4 |
| `retail/` | Retail | 4 |
| `textile-apparel/` | Textile & Apparel | 4 |
| `transportation/` | Transportation | 4 |
| `biomedicine/` | Biomedicine/Innovative Drugs | 3 |
| `datacenter/` | Data Centers/Computing Infrastructure | 3 |
| `equipment/` | High-End Equipment/Industrial Machine Tools | 3 |
| `medicaldevice/` | Medical Devices | 3 |
| `system-intelligence/` | System Intelligence Layer (Contagion Map · Concentration · Early Warning Thermometer) | 9 |
| `validation/` | Validation Special Topics (Multi-Stakeholder · Industry Validation Summary · Retrospective) | 3 |

### `docs/` — Test Execution Records

- `false-positive-negative-testing.md` — False positive/false negative testing methodology and multi-case actual test execution records

---

## Related

- Project Core: `dev/` (engine architecture overview at `dev/engine/engine-overview.md`)
- Validation Methodology: `dev/engine/validation-methodology.md`
- Version Snapshot Rules: `version/` (this directory is never included)
