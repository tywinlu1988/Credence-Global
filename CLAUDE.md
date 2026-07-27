# CLAUDE.md — Credence

Read `AGENTS.md` first. Skills are in `.claude/skills/`.

Thresholds, weights, and rating maps live only in `engine/*.md`; never fabricate values -- reference `engine/<doc>.md SS<section>`, output `engine_undefined` if not defined.

## Path Resolution

Paths written as `${CLAUDE_PLUGIN_ROOT}/engine/...` and `${CLAUDE_PLUGIN_ROOT}/templates/...` resolve to the package root:

- **Plugin install** (Claude Code plugin/marketplace): `${CLAUDE_PLUGIN_ROOT}` is the package root inside the plugins directory — all references resolve automatically.
- **Opened as a project** (downloaded zip / Model A): treat `${CLAUDE_PLUGIN_ROOT}` as the package root you opened (the directory holding the engine and templates folders).

