# Agent Protocol — Shared Infrastructure for All Skills

**Version**: v0.0.9 | **Date**: 2026-07-29

> This document is referenced by every SKILL.md. It defines two pieces of shared
> infrastructure that every skill needs: path resolution and non-negotiable constraints.
> Skills reference this document by section number rather than duplicating the content.

---

## 1. Path Resolution

All paths written as `engine/...` or `templates/...` resolve to the **package root** —
the directory containing `.claude-plugin/`, `engine/`, `templates/`, and `src/`.

- **Plugin install** (Claude Code marketplace): the package root is inside the plugins
  directory. The harness expands `${CLAUDE_PLUGIN_ROOT}` to this path automatically.
- **Opened as a project** (downloaded zip / Model A): the package root is the folder
  you opened. No prefix needed — `engine/` and `templates/` resolve directly.

**Rule**: always resolve `engine/` and `templates/` relative to the package root.
Never assume a hardcoded absolute path. If the harness provides `${CLAUDE_PLUGIN_ROOT}`,
use it; otherwise treat the working directory's `engine/` and `templates/` folders as
the resolution target.

---

## 2. Non-Negotiables (from AGENTS.md)

These six rules bind every agent, every CLI, every request:

1. **No analysis without a Path Sheet.** Any credit conclusion, rating, or score requires
   a Path Sheet from `credit-analysis-router` (or an explicit `path_id`). Knowledge
   questions exempt.
2. **No numbers without a citation.** Every threshold, weight, score, tier, or rating
   MUST cite `dev/engine/<doc>.md §section`. If undefined, output `engine_undefined`.
3. **No report without a template.** Deliverable reports MUST be assembled by
   `credit-report-builder` from `dev/templates/`. Never design ad-hoc HTML or layouts.
4. **No delivery without QA.** Analysis ships only after `credit-qa-verifier` produces
   a passing QA Verdict. Knowledge questions exempt.
5. **No invented dimensions or vocabulary.** Use only engine-defined dimensions,
   industries, paradigms, and metrics. Never create new ones.
6. **Follow the path's Playbook.** For active paths, `dev/engine/path-playbooks/<path_id>.md`
   is the execution contract — read it first, do not deviate.

The authoritative text is in `AGENTS.md`. This section is a reference copy for skills
that need the full list inline; most skills only need a subset.

---

## 3. Skill Reference Convention

Each SKILL.md declares which subset of Non-Negotiables apply to it:

| Skill | Applicable Rules |
|---|---|
| `credit-analysis-router` | #1, #2, #3, #4, #5 |
| `fixed-income-credit-analysis` | #1, #2, #3, #4, #5, #6 |
| `credit-report-builder` | #2, #3, #4 |
| `credit-qa-verifier` | #2, #3, #4 |

The Path Resolution (§1) applies to all skills equally.

---

## Related

- `AGENTS.md` — authoritative Non-Negotiables and cross-CLI entry point
- `dev/engine/pipeline-contract.md` — four-stage I/O contract
- `dev/engine/work-path-registry.md` — 16 work paths, routing table
