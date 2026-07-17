# Credence · Fixed-Income Credit Analysis Engine

> **A methodology-first credit analysis engine for global fixed-income markets** — delivered as **Agent Skills** (`SKILL.md`), installable into Claude Code / Codex / Cursor / Gemini / OpenCode.
>
> 🌐 **Read this in:** [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Français](README.fr.md)

**Version** `v0.0.1` · **License** Source-available · Non-commercial (see [LICENSE](LICENSE))

---

## What Is This

Credence packages the methodology of a seasoned fixed-income credit analyst into a form an AI agent can load and execute directly. It is **not an agent framework and not a standalone app** — it is a domain-methodology skill pack:

| Layer | Contents | Location |
|-------|----------|----------|
| **Core Asset = Domain Methodology** | Ten-dimension scoring · dual-track cross-validation · international rating map · LGD · external support · system-intelligence layer | `dev/engine/` |
| **Delivery = Agent Skills Pack** | Four-stage skill chain: route → analyze → report → QA | `dev/.claude/skills/` |
| **Runtime = Inside Existing Agent CLIs** | Model and loop from the host; Credence supplies domain expertise | — |
| **Extras** | Report templates (Type 1–18) + executable orchestrator (4 coded engines: SRI, 5-dim concentration, contagion matrix, outlook monitoring) | `dev/templates/` · `src/` |

**Core principle**: traditional financial analysis fails systematically in policy-driven, tech-barrier, and asset-lease industries; the heaviest credit factors rarely appear on the balance sheet; external ratings lag real credit deterioration by 17+ months on average.

## Quick Start

**Key premise**: the skills are NOT self-contained — at runtime they read `engine/` and `templates/` from the **package root** (single source of truth, never copied). So the install unit is the whole package root; **open the package root as your project** (Model A) and everything resolves with zero copying.

**A · npx (recommended)**

```bash
npx github:tywinlu1988/credence-global
```

Lays the current release package into `./credence/`; open that folder with your agent CLI.

**B · GitHub Release**

Download the latest `vX.Y.Z-release.zip` from [Releases](https://github.com/tywinlu1988/Credence-Global/releases), unzip, and open the package root as a project.

**C · Clone the Source**

```bash
git clone git@github.com:tywinlu1988/Credence-Global.git
```

## Repository Map

```
dev/          methodology & skill source (engine/ 27 docs · .claude/skills/ 4-stage chain · templates/ 18)
src/          executable orchestrator + 4 coded engines (pipeline.py · sri_calculator.py · concentration_scorer.py · contagion_engine.py · outlook_engine.py)
scripts/      build_dist.py (dev/ → release-package assembler) · consistency_check.py · promote.py
tests/        regression tests
version/      installable release packages (history via git tags)
validation/   capability evidence
docs/         versioning strategy · Codex deep-dive adapter
AGENTS.md     cross-CLI universal entry (start here from any agent CLI)
```

## Documentation

- **Project overview & full map** → [`dev/README.md`](dev/README.md)
- **Engine architecture** → [`dev/engine/engine-overview.md`](dev/engine/engine-overview.md)
- **Cross-CLI setup (incl. Codex deep-dive)** → [`AGENTS.md`](AGENTS.md) · [`docs/adapters/codex.md`](docs/adapters/codex.md)

## License & Disclaimer

This repository is **source-available**: you may view, learn from, and use it for non-commercial / internal evaluation; **any commercial use requires prior written permission** — see [LICENSE](LICENSE). The engine's output is a methodology demonstration / research artifact and is **not investment advice**.
