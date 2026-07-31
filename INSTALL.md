# INSTALL — Install Credence (v0.2.0)

Credence is a self-contained agent package. **Key premise**: skills are not self-contained --
they read `engine/` methodology documents and `templates/` report templates from the
**project root** at runtime (single source of truth, never duplicated).
Therefore the install unit is the **entire package root**, not individual skill folders.

## Model A -- Open as Project (Recommended, Zero Config)

Open the package root directory `credence/` as your project/workspace and ask questions
directly in natural language; `credit-analysis-router` handles the four-question routing.
All references (`engine/`, `templates/`, `.claude/skills/`) resolve automatically.

```
unzip credence-v0.2.0.zip        # or git clone <repo> credence
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
`${CLAUDE_PLUGIN_ROOT}` prefix baked into every skill (see Path Resolution above).
