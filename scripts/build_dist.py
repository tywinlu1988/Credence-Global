"""Deterministic assembler for the Credence installable agent package (version derived from
engine-overview.md header -- see _version()).

Transforms the `dev/` workspace (source) into `dist/credence/` (artifact) -- a self-contained,
portable, industry-standard agent package installable in Claude Code / Codex / Cursor / Gemini /
OpenCode. The `dev/` layout remains unchanged (checker and tests continue to verify it); this
script only **copies+rewrites+cleanses** to produce what goes into `version/<v>-release/` and the
zip archive. This is the standard source-vs-artifact model.

## Layout Contract (sole reference shared by dist test test_dist_package.py and this script)

dist/credence/
|-- AGENTS.md / CLAUDE.md / GEMINI.md / INSTALL.md / README.md   (generated)
|-- .claude-plugin/plugin.json                                   (generated)
|-- .claude/skills/<4 skills>/{SKILL.md,references/}            (copied+rewritten from dev/.claude/skills)
|-- engine/          (dev/engine excluding audits/ + appendix/ + reference/, rewritten+pointer-cleansed)
|-- templates/       (dev/templates full copy)
|-- src/             (excluding __pycache__/*.pyc, comments rewritten)
`-- adapters/codex.md (moved from docs/adapters + rewritten)

## Reference Rewrite Rules (ordered, longest prefix first; applied to every copied text file)
1. `dev/.claude/skills/` -> `.claude/skills/`
2. `dev/engine/`         -> `${CLAUDE_PLUGIN_ROOT}/engine/`
3. `dev/templates/`      -> `${CLAUDE_PLUGIN_ROOT}/templates/`
4. `../../src/`          -> `../src/`        (deep link fix for engine-overview.md)
Note: `multi-stakeholder.md`'s `../engine/`, `../templates/` resolve in both layouts; left unchanged.

## Pointer Cleansing (pattern-based, not line-number-based; each occurrence is logged)
- Inline fragment removal: `(audits/)` parenthetical snippets (retain sentence remainder).
- Full-line deletion: lines still containing `audits/` after parenthetical stripping (table rows,
  source notes, bullet points).
- Full-line deletion: lines containing `validation/` path tokens (validation/ excluded from package).
- Full-line deletion: lines containing `appendix/` or `reference/` tokens (on-demand material
  excluded from package; pointer lines are single-row by design).

## Exclusions (never allowed into dist)
`settings.local.json`, `__pycache__`, `*.pyc`, `engine/audits/`, `engine/appendix/`,
`engine/reference/`, `design/`,
`product/`, `data/`, `validation/`, `.git/`, `version/`, `tests/`, `scripts/`,
`docs/` (except adapters/codex.md), `dev/README.md` (replaced by generated README).

## Validation (--check or auto-run after build; any failure exits loudly)
(i) Zero `[A-Za-z]:[\\/]` absolute paths; (ii) zero residual `dev/` path tokens; (iii) every
relative link resolves within dist; (iv) 4 SKILL.md with frontmatter exactly name+description;
(v) 27 shipped CORE_DOCS all present under engine/; (vi) src can locate engine/templates in dist layout;
(vii) zero excluded artifacts present.
(viii) No CRLF in text files (LF enforced per root .gitattributes).
"""

import argparse
import hashlib
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEV = ROOT / "dev"
DIST = ROOT / "dist" / "credence"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from consistency_check import CORE_DOCS, DIST_CORE_DOCS  # noqa: E402  single source of truth, don't duplicate manifest

# Ordered rewrite rules (longest prefix first). The skills rule has no trailing slash
# to cover both `dev/.claude/skills` and `dev/.claude/skills/...` forms.
REWRITE_RULES = [
    ("dev/.claude/skills", ".claude/skills"),
    ("dev/engine/", "${CLAUDE_PLUGIN_ROOT}/engine/"),
    ("dev/templates/", "${CLAUDE_PLUGIN_ROOT}/templates/"),
    ("../../src/", "../src/"),
]

# Prefix injected by the rules above for plugin installs; the link checker strips it
# before resolving paths inside the package.
_PLUGIN_PREFIX = "${CLAUDE_PLUGIN_ROOT}/"

# Path Resolution note injected into generated entry docs and every SKILL.md. It tells
# the agent how to resolve the ${CLAUDE_PLUGIN_ROOT} prefix in both install modes.
_PATH_NOTE = """## Path Resolution

Paths written as `${CLAUDE_PLUGIN_ROOT}/engine/...` and `${CLAUDE_PLUGIN_ROOT}/templates/...` resolve to the package root:

- **Plugin install** (Claude Code plugin/marketplace): `${CLAUDE_PLUGIN_ROOT}` is the package root inside the plugins directory — all references resolve automatically.
- **Opened as a project** (downloaded zip / Model A): treat `${CLAUDE_PLUGIN_ROOT}` as the package root you opened (the directory holding the engine and templates folders).
"""

TEXT_EXTS = {".md", ".py", ".html", ".css", ".yaml", ".yml", ".txt", ".json"}

SKILL_NAMES = [
    "credit-analysis-router",
    "fixed-income-credit-analysis",
    "credit-report-builder",
    "credit-qa-verifier",
]

ABS_PATH_RE = re.compile(r"(?<![A-Za-z])[A-Za-z]:[\\/]")  # drive letter not preceded by a letter (excludes https:// etc.)
DEV_TOKEN_RE = re.compile(r"(?<![\w/.-])dev[/\\]")
# Inline audits parentheses fragments (full-width/half-width brackets), stripped while retaining sentence.
AUDIT_FRAGMENT_RE = re.compile(r"（[^（）]*audits/[^（）]*）|\([^()]*audits/[^()]*\)")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


# ---------------------------------------------------------------------------
# Copy + Rewrite + Cleanse
# ---------------------------------------------------------------------------

def _apply_rewrites(text: str) -> str:
    for old, new in REWRITE_RULES:
        text = text.replace(old, new)
    return text


def _scrub(text: str, rel: str, log: list) -> str:
    """Pointer cleansing: strip inline audits fragments, then drop residual audits/validation/ pointer lines."""
    text, n_frag = AUDIT_FRAGMENT_RE.subn("", text)
    for _ in range(n_frag):
        log.append(f"fragment-strip (audits paren) in {rel}")
    kept = []
    for line in text.split("\n"):
        if ("audits/" in line or "validation/" in line
                or "appendix/" in line or "reference/" in line):
            log.append(f"drop pointer line in {rel}: {line.strip()[:70]}")
            continue
        kept.append(line)
    return "\n".join(kept)


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _inline_css(html_text: str, templates_dir: Path) -> str:
    """Replace <link rel="stylesheet" href="template-base.css"> with inline <style>.

    Dev templates use an external CSS link (single source of truth, zero duplication).
    At build time we inline the CSS so the dist HTML files are self-contained — copy
    a report anywhere and it renders correctly, no missing CSS dependency.
    """
    css_path = templates_dir / "template-base.css"
    css_content = css_path.read_text(encoding="utf-8")
    # Wrap in <style> with a marker so it's clear this was build-time inlined
    inline_block = f"<style>/* inlined from template-base.css at build time */\n{css_content}\n</style>"
    return html_text.replace(
        '<link rel="stylesheet" href="template-base.css">',
        inline_block,
    )


def _copy_and_transform(src: Path, dst: Path, log: list, scrub: bool) -> None:
    for f in sorted(src.rglob("*")):
        if f.is_dir():
            continue
        if "__pycache__" in f.parts or f.suffix == ".pyc" or f.name == "settings.local.json":
            log.append(f"excluded: {f.relative_to(src)}")
            continue
        rel = f.relative_to(src)
        out = dst / rel
        if f.suffix in TEXT_EXTS:
            text = f.read_text(encoding="utf-8")
            text = _apply_rewrites(text)
            if scrub:
                text = _scrub(text, str(rel), log)
            if f.suffix == ".html":
                text = _inline_css(text, src)
            _write_text(out, text)
        else:
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(f, out)


# ---------------------------------------------------------------------------
# Generated entry / installation files (version stamped from engine-overview.md header, not hardcoded)
# ---------------------------------------------------------------------------

def _version() -> str:
    text = (DEV / "engine" / "engine-overview.md").read_text(encoding="utf-8")
    m = re.search(r"\*\*Version\*\*\s*[:：]\s*(\S+)", text)
    return m.group(1) if m else "v0.3.1"


def _gen_agents_md(v: str) -> str:
    return f"""# AGENTS.md — Credence Cross-CLI Universal Entry

**Project**: Credence (Fixed-Income Credit Intelligent Analysis Engine)
**Engine Version**: {v}
**Tagline**: Methodology-first credit analysis engine; portable unit is `SKILL.md`.

> Any agent CLI starts here: read your instructions file first, then the `SKILL.md` for the current task.
> For installation and tool-specific setup, see `INSTALL.md`.

## What This Package Is

A credit analysis engine for international fixed-income markets, organized into four layers:

1. **Mosaic Engine** — Assembles fragmented public data into coherent signals; data gaps are themselves risk signals.
2. **Dual-Track Engine** — Industry multi-layer pyramids (fundamentals) and market pricing signals run in parallel, then cross-validated.
3. **Multi-Stakeholder** — Credit Selector / Portfolio Manager / Trader / Risk Officer / Advisor / Individual Investor viewpoints.
4. **System-Intelligence Layer (SRI)** — Cross-industry contagion, five-dimension concentration, Systemic Risk Index (SRI).

**Thresholds, weights, and rating maps live only in `engine/*.md`.** This file and every skill never duplicate these values; any numerical judgment must reference the engine document and section.

""" + _PATH_NOTE + """

## How to Use in Your Agent CLI

This package is a self-contained installable agent package, with skills under `.claude/skills/`. **Simplest approach (Model A)**: Open the package root as your project and all references resolve automatically.

| Agent CLI | How to Access |
|---|---|
| **Claude Code** | Auto-discovers `.claude/skills/` (open the package root as project); `CLAUDE.md` points here. Distribution channel: plugin/marketplace (see `.claude-plugin/plugin.json`). |
| **Codex** | Natively reads `AGENTS.md`; then manually read the current task's `SKILL.md`. Deep adapter guidance in `adapters/codex.md`. |
| **Cursor** | Reads `AGENTS.md` and compatibly reads `.claude/skills/`. |
| **Gemini** | Reads `GEMINI.md` and compatibly reads `.claude/skills/`. |
| **OpenCode** | Reads `AGENTS.md` and compatibly reads `.claude/skills/`. |

Uniform approach: **Read your instructions file first, then the `SKILL.md` for the current task.** For integrating into an existing project (Model B) or global installation paths, see `INSTALL.md`.

## Skill Index

| Skill | Use When... | Path |
|---|---|---|
| `credit-analysis-router` | Requirements are vague or composite: route to a work path via four-question protocol | `.claude/skills/credit-analysis-router/SKILL.md` |
| `fixed-income-credit-analysis` | Concrete methodology task or engine path: execute analysis per path sheet or core doc set | `.claude/skills/fixed-income-credit-analysis/SKILL.md` |
| `credit-report-builder` | Assemble completed credit analysis into deliverables (select template Type 1-15, map L0/L1/L2 layers, dashboard); needs upstream analysis output | `.claude/skills/credit-report-builder/SKILL.md` |
| `credit-qa-verifier` | Pre-delivery review of report/analysis (quality gates, density rules, veto ceiling, Mode B guardrails, single-source compliance); terminal QA for four-stage chain | `.claude/skills/credit-qa-verifier/SKILL.md` |

## Four-Stage Pipeline

The engine decomposes each credit analysis into a four-stage chained contract, with `path_id` as the join key across stages:

| Stage | Responsibility | Carrying Skill |
|---|---|---|
| 1 intake | Four-question routing, produces Path Sheet | `credit-analysis-router` |
| 2 analysis | Execute analysis per `engine_reading_order` | `fixed-income-credit-analysis` |
| 3 report | Assemble analysis into deliverable report | `credit-report-builder` |
| 4 qa | Pre-delivery quality gate review | `credit-qa-verifier` |

Four-stage artifacts (Path Sheet / Analysis Artifact / Delivery Note / QA Verdict) field shapes and chaining edges are single-sourced in `engine/pipeline-contract.md`.

**Executable Orchestrator**: `src/pipeline.py` drives the four-stage chain as code, reading stage definitions from `pipeline-contract.md`. It calls coded engines only for wired paths -- **WP-RO-01 -> Concentration (`src/concentration_scorer.py`), WP-RO-02 -> Contagion (`src/contagion_engine.py`), WP-RO-03 -> SRI (`src/sri_calculator.py`), WP-X-05 -> Outlook (`src/outlook_engine.py`)**; remaining paths are LLM-orchestrated via engine documents.

## Single Source of Truth Rule

**Never duplicate thresholds, weights, SRI tiers, rating maps, or layer time budgets.** Any numerical judgment must reference `engine/<doc>.md SS<section>`; if the engine document does not define it, output `engine_undefined` -- do not fabricate values.

## Routing Baseline (Work Path Registry)

`engine/work-path-registry.md` is the single source of truth for routing: **16 work paths (all active in v0.1.0)**. The router maps ambiguous requirements to concrete work paths; when recommending a planned path, honestly state "not yet implemented" and suggest an active alternative.

## Platform Neutrality Note

This file and each skill uniformly refer to "your instructions file" -- every agent CLI has a different project-level instruction filename, and this package does not assume any specific product filename. Literal path references to `.claude/skills` are allowed: that is a path, not a behavioral instruction.

## Developer Regression Gate (Full Source Repository Required)

This installable package is a **runtime artifact** and does not include tests or consistency-check scripts. To run the regression gate (`pytest` + `consistency_check.py`) or modify the methodology itself, clone the full source repository.
"""


def _gen_cli_entry(name: str, note: str = "") -> str:
    """Generate a minimal CLI entry-point file (CLAUDE.md / GEMINI.md).

    Both files share the same structure: pointer to AGENTS.md, skills location,
    SSOT rule, and Path Resolution block. The only difference is the filename
    header and an optional CLI-specific note.
    """
    return f"""# {name}.md — Credence

Read `AGENTS.md` first. Skills are in `.claude/skills/`{(' (' + note + ')') if note else ''}.

Thresholds, weights, and rating maps live only in `engine/*.md`; never fabricate values -- reference `engine/<doc>.md SS<section>`, output `engine_undefined` if not defined.

""" + _PATH_NOTE + """
"""


def _gen_install_md(v: str) -> str:
    return f"""# INSTALL — Install Credence ({v})

Credence is a self-contained agent package. **Key premise**: skills are not self-contained --
they read `engine/` methodology documents and `templates/` report templates from the
**project root** at runtime (single source of truth, never duplicated).
Therefore the install unit is the **entire package root**, not individual skill folders.

## Model A -- Open as Project (Recommended, Zero Config)

Open the package root directory `credence/` as your project/workspace and ask questions
directly in natural language; `credit-analysis-router` handles the four-question routing.
All references (`engine/`, `templates/`, `.claude/skills/`) resolve automatically.

```
unzip credence-{v}.zip        # or git clone <repo> credence
cd credence                   # use package root as project root
# Claude Code: claude   .   Codex: codex   .   Others: open the folder
```

**Python dependency**: the executable orchestrator (`src/pipeline.py`) and its wired coded
engines require Python 3.11+ with PyYAML (`pip install pyyaml`). The LLM-orchestrated
skills need no Python setup at all.

## Model B -- Integrate Into Your Existing Project

Copy the **entire runtime core** to your project root (not just the skills folder):

```
.claude/skills/   ->  <your-project>/.claude/skills/
engine/           ->  <your-project>/engine/
templates/        ->  <your-project>/templates/
src/              ->  <your-project>/src/        (optional, only if using executable orchestrator)
AGENTS.md / CLAUDE.md / GEMINI.md  ->  merge into your project's instructions file
```

## Tool-Specific Global Installation Targets (Optional)

Place the 4 skill directories under `.claude/skills/` (along with `engine/`, `templates/`)
into the corresponding tool's global skills location for use across any project:

| Tool | Global Skills Target | Entry File |
|---|---|---|
| Claude Code | `~/.claude/skills/` | `CLAUDE.md` |
| Codex | `~/.codex/skills/` (skills are experimental; primary: `AGENTS.md`) | `AGENTS.md` |
| Cursor | `~/.cursor/skills/` | `AGENTS.md` |
| Gemini CLI | `~/.gemini/skills/` | `GEMINI.md` |
| OpenCode | `~/.config/opencode/skills/` | `AGENTS.md` |

> For global install, `engine/` and `templates/` must also be reachable by skills (see premise above).
> The simplest and most reliable approach remains Model A -- open the package root as your project.

## Claude Code Plugin / Marketplace

`.claude-plugin/plugin.json` is a minimal marketplace manifest enabling this package to be
listed/installed as a plugin. When installed as a plugin, the 4 skills under `.claude/skills/`
are loaded by Claude Code, and `engine/` and `templates/` remain reachable via the
`${{CLAUDE_PLUGIN_ROOT}}` prefix baked into every skill (see Path Resolution above).
"""


def _gen_readme_md(v: str) -> str:
    return f"""# Credence — Fixed-Income Credit Intelligent Analysis Engine ({v})

> **A methodology-first credit analysis engine for global fixed-income markets** — the
> methodology of a seasoned credit analyst, packaged as **Agent Skills** an AI agent can
> load and execute directly. Not an agent framework, not a standalone app: a
> domain-methodology skill pack for institutional-grade, reproducible credit analysis.

**Version** {v} · **License** MIT (see `LICENSE`) · **27 core methodology documents** ·
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
- `engine/` — 27 core methodology documents: thresholds, weights, rating maps, contagion matrix
  (legacy reference docs and per-document appendices live in the source repository)
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
"""


def _gen_plugin_json(v: str) -> str:
    import json
    manifest = {
        "name": "credence",
        "version": v.lstrip("v"),
        "description": "Credence Fixed-Income Credit Analysis Engine: industry multi-layer "
        "pyramids + dual-track cross-validation + mosaic engine + system-intelligence layer. "
        "Four-stage skills: intake router / analysis / report / qa.",
        "author": {
            "name": "tywinlu1988",
            "url": "https://github.com/tywinlu1988",
        },
        "homepage": "https://github.com/tywinlu1988/Credence-Global",
        "repository": "https://github.com/tywinlu1988/Credence-Global",
        "license": "MIT",
        "keywords": ["credit-analysis", "fixed-income", "bond", "risk", "finance"],
        "skills": "./.claude/skills/",
    }
    return json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"


def _gen_adapter_codex(log: list) -> str:
    src = ROOT / "docs" / "adapters" / "codex.md"
    text = src.read_text(encoding="utf-8")
    text = _apply_rewrites(text)
    # dist has no tests/scripts: replace "run two validators" with Model-A usage.
    text = re.sub(
        r"## 4\. .*",
        "## 4. Notes\n\nThis adapter targets **install package** users. The installable package "
        "is a runtime artifact and does not include tests or consistency-check scripts. "
        "To run the regression gate (`pytest` + `consistency_check.py`) or modify the "
        "methodology, clone the full source repository.\n",
        text,
        flags=re.DOTALL,
    )
    return text


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def _check_links(errors: list, base: Path) -> None:
    for f in sorted(base.rglob("*.md")):
        text = f.read_text(encoding="utf-8")
        for m in LINK_RE.finditer(text):
            target = m.group(1).split("#")[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith(_PLUGIN_PREFIX):
                target = target[len(_PLUGIN_PREFIX):]
            if (
                (f.parent / target).exists()
                or (base / target).exists()
                or (base / "engine" / target).exists()
            ):
                continue
            errors.append(f"BROKEN_LINK: {f.relative_to(base)} -> {target}")


def validate(out_dir=None) -> list:
    base = Path(out_dir) if out_dir is not None else DIST
    errors = []
    if not base.is_dir():
        return [f"dist missing: {base}"]

    for f in sorted(base.rglob("*")):
        if f.is_dir():
            continue
        rel = f.relative_to(base)
        # (vii) excluded artifacts must not appear
        if "__pycache__" in f.parts or f.suffix == ".pyc" or f.name == "settings.local.json":
            errors.append(f"EXCLUDED_PRESENT: {rel}")
        if ("audits" in f.parts or f.parts[0] in ("design", "product", "data", "validation")
                or (f.parts[0] == "engine" and len(f.parts) > 1
                    and f.parts[1] in ("appendix", "reference"))):
            errors.append(f"EXCLUDED_DIR_PRESENT: {rel}")
        data = f.read_bytes()
        if b"\0" not in data and b"\r\n" in data:
            errors.append(f"CRLF: {rel}")
        if f.suffix in TEXT_EXTS:
            text = f.read_text(encoding="utf-8")
            for m in ABS_PATH_RE.finditer(text):
                errors.append(f"ABS_PATH: {rel}: ...{text[max(0,m.start()-15):m.start()+25]!r}...")
            if DEV_TOKEN_RE.search(text):
                errors.append(f"DEV_TOKEN: {rel}")
            if "appendix/" in text or "reference/" in text:
                errors.append(f"ON_DEMAND_TOKEN: {rel} mentions appendix/ or reference/ (scrub missed a line)")

    # (iv) 4 skills + strict frontmatter
    for name in SKILL_NAMES:
        sf = base / ".claude" / "skills" / name / "SKILL.md"
        if not sf.exists():
            errors.append(f"MISSING_SKILL: {name}")
            continue
        fm = sf.read_text(encoding="utf-8").split("---")[1]
        keys = re.findall(r"^([a-z-]+):", fm, re.MULTILINE)
        if keys != ["name", "description"]:
            errors.append(f"FRONTMATTER: {name} keys={keys}, want ['name','description']")

    # (v) shipped CORE_DOCS under engine/ (appendix/ + reference/ are repo-only)
    for doc in DIST_CORE_DOCS:
        if not (base / "engine" / doc).exists():
            errors.append(f"MISSING_CORE_DOC: engine/{doc}")

    # (vi) src can locate engine/templates (flat dist layout)
    if not (base / "engine").is_dir() or not (base / "templates").is_dir():
        errors.append("LAYOUT: engine/ or templates/ missing at package root")

    # (viii) LICENSE must ship with the package
    if not (base / "LICENSE").is_file():
        errors.append("MISSING_LICENSE: LICENSE file not present in dist package")

    # (ix) skills must not carry bare engine/templates references (plugin installs
    # resolve them from the user's project root, where they do not exist)
    for f in sorted(base.rglob(".claude/skills/**/*.md")):
        text = f.read_text(encoding="utf-8")
        for m in re.finditer(r"`(engine|templates)/", text):
            errors.append(f"BARE_REF: {f.relative_to(base)}: bare `{m.group(0)}` reference at offset {m.start()}")

    # (iii) links
    _check_links(errors, base)
    return errors


# ---------------------------------------------------------------------------
# Release zip (single distribution artifact; ships via GitHub Releases, never committed)
# ---------------------------------------------------------------------------

def build_release_zip(out_dir=None, version_dir=None):
    """Zip the built dist tree into ``<version_dir>/<v>-release.zip`` + ``.sha256`` sidecar.

    Layout: single top-level ``credence/`` root (what bin/install.js extracts and what
    Quick Start promises users). Deterministic: sorted entries, fixed timestamps and
    permissions, so identical inputs produce byte-identical zips.
    Returns ``(zip_path, sha256_path)``.
    """
    base = Path(out_dir) if out_dir is not None else DIST
    vdir = Path(version_dir) if version_dir is not None else ROOT / "version"
    if not base.is_dir():
        raise FileNotFoundError(f"dist tree missing: {base} (run build first)")
    vdir.mkdir(parents=True, exist_ok=True)

    v = _version()
    zip_path = vdir / f"{v}-release.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(base.rglob("*")):
            if not f.is_file():
                continue
            arc = str(Path("credence") / f.relative_to(base)).replace("\\", "/")
            info = zipfile.ZipInfo(arc, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, f.read_bytes())

    digest = hashlib.sha256(zip_path.read_bytes()).hexdigest()
    sha_path = vdir / f"{v}-release.zip.sha256"
    sha_path.write_text(f"{digest}  {zip_path.name}\n", encoding="utf-8", newline="\n")
    return zip_path, sha_path


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def build(out_dir=None) -> list:
    out = Path(out_dir) if out_dir is not None else DIST
    log = []
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    _copy_and_transform(DEV / ".claude" / "skills", out / ".claude" / "skills", log, scrub=True)
    # engine: exclude audits/ (review records) + appendix/ and reference/
    # (on-demand material stays repo-only; pointer lines to them are scrubbed above)
    engine_src = DEV / "engine"
    for f in sorted(engine_src.rglob("*")):
        if f.is_dir() or f.relative_to(engine_src).parts[0] in ("audits", "appendix", "reference"):
            continue
        rel = f.relative_to(engine_src)
        if f.suffix in TEXT_EXTS:
            text = _scrub(_apply_rewrites(f.read_text(encoding="utf-8")), str(rel), log)
            _write_text(out / "engine" / rel, text)
        else:
            dst = out / "engine" / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(f, dst)
    _copy_and_transform(DEV / "templates", out / "templates", log, scrub=True)
    _copy_and_transform(ROOT / "src", out / "src", log, scrub=False)

    v = _version()
    shutil.copyfile(ROOT / "LICENSE", out / "LICENSE")
    _write_text(out / "AGENTS.md", _gen_agents_md(v))
    _write_text(out / "CLAUDE.md", _gen_cli_entry("CLAUDE"))
    _write_text(out / "GEMINI.md", _gen_cli_entry("GEMINI", "Gemini CLI compatibly reads this directory"))
    _write_text(out / "INSTALL.md", _gen_install_md(v))
    _write_text(out / "README.md", _gen_readme_md(v))
    _write_text(out / ".claude-plugin" / "plugin.json", _gen_plugin_json(v))
    _write_text(out / "adapters" / "codex.md", _gen_adapter_codex(log))

    return log


def main() -> int:
    ap = argparse.ArgumentParser(description="Assemble the Credence installable agent package.")
    ap.add_argument("--check", action="store_true", help="validate an existing dist/ only")
    ap.add_argument("--zip", action="store_true",
                    help="after a passing build, also write version/<v>-release.zip + .sha256")
    ap.add_argument("--verbose", action="store_true", help="print the transform log")
    args = ap.parse_args()

    if not args.check:
        log = build()
        print(f"built {DIST} ({sum(1 for _ in DIST.rglob('*') if _.is_file())} files)")
        if args.verbose:
            for line in log:
                print("  ", line)

    errors = validate()
    if errors:
        print(f"dist validation FAILED ({len(errors)}):")
        for e in errors[:60]:
            print("  ", e)
        return 1
    print("dist validation PASSED")

    if args.zip:
        zip_path, sha_path = build_release_zip()
        print(f"release zip: {zip_path}")
        print(f"sha256 sidecar: {sha_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
