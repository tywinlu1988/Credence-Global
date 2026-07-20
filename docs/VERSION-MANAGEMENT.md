# Version Management Strategy

**Corresponding Engine Version**: v0.0.1
**Last Updated**: 2026-07-20

## Directory Structure Convention

- `dev/` — Current active development workspace. All in-progress methodology documents, reports, templates, and skills are placed here.
- `version/` — **Local build output only.** Holds the release zip produced by `scripts/build_dist.py --zip` (`version/<v>-release.zip` + `version/<v>-release.zip.sha256`). Git tracks only `version/.gitkeep`; every zip/sidecar is gitignored and **distributed externally as a GitHub Releases attachment**, never committed.
- `validation/` — Engine capability verification artifacts (test outputs and evidence archives), **not part of the project core**.

**Release artifact**: a single zip per version, produced by `python scripts/build_dist.py --zip`:

- Name: `version/<v>-release.zip` (e.g. `version/v0.0.1-release.zip`), plus a `<v>-release.zip.sha256` sidecar (`<hex>  <filename>`).
- Internal layout: one top-level `credence/` directory containing the installable agent package (contents of `dist/credence/`): skills at `.claude/skills/`, flattened `engine/`, `templates/`, `src/`, `adapters/`, plus generated `AGENTS.md`/`CLAUDE.md`/`GEMINI.md`/`INSTALL.md`/`README.md`/`.claude-plugin/plugin.json`. The package has dead links and root-directory assumptions removed (no `settings.local.json` absolute paths, no `audits/`, `design/`, `product/`, `data/`, `validation/`).
- Deterministic: sorted entries, fixed timestamps and permissions — identical inputs produce byte-identical zips (verified by tests).

**Install path**: `bin/install.js` (invoked via `npx github:tywinlu1988/credence-global`) resolves the release tag (latest GitHub Release, or `--tag vX.Y.Z` / `CREDENCE_TAG`), downloads `<tag>-release.zip` + `.sha256` from the GitHub Releases page, verifies the checksum (mismatch aborts), and unpacks into `./credence/` (or a user-supplied directory). The git tree is **not** the distribution channel — no release directories are tracked in git.

## Version Numbering System

### Engine Version

- Format: `v<major>.<minor>.<patch>-<stage>`
- Scope: All core methodology documents under `dev/engine/`, skill packages, templates, and reports.
- Current: `v0.0.1`
- Upgrade Trigger Conditions:
  - New feature modules or industry coverage -> Increment minor version
  - Major methodology restructuring or rating system changes -> Increment major version
  - Consistency fixes, terminology unification, threshold alignment -> Increment patch version

### Review Report Version

- Format: `v<major>.<minor>` (e.g., v1.0, v1.1)
- Scope: historical `dev/engine/*-audit.md`, `dev/engine/*-review-*.md`, `dev/engine/self-assessment-*.md` — the audits/ archive was removed in the v0.0.1 cleanup; this scheme applies again only if review reports are reintroduced.
- Must annotate in file header: `**Corresponding Engine Version**: vX.Y.Z-<stage>`

## Release Checklist

Before cutting a new release, the following checks must be completed:

- [ ] `python scripts/promote.py vX.Y.Z-<stage>` (dry-run preview) -> `--apply` to commit, and verify that all printed "rules not covered remaining" are historical references after manual review; both version history tables (engine-overview Section 6, dev/README.md) have been manually updated with new rows.
- [ ] All core methodology documents' `**Version**:` headers are unified to the current engine version.
- [ ] Claude Skill package (`dev/.claude/skills/fixed-income-credit-analysis/`) has been synced and upgraded to the current engine version.
- [ ] `scripts/consistency_check.py` runs successfully (no broken links, consistent version numbers, SRI examples within valid range).
- [ ] `python scripts/build_dist.py --zip` build + built-in validation passes (zero absolute paths, zero dev/ tokens, all links resolvable, 4 skills with strict frontmatter, 27 CORE_DOCS complete) and produces `version/<v>-release.zip` + `.sha256`.
- [ ] All templates and reports have version numbers aligned with the engine version.
- [ ] `dev/README.md` version history and directory structure description have been updated.

## Release Process

1. Complete all changes in `dev/` and pass regression gates (`scripts/consistency_check.py` and `pytest` all green).
2. Run `python scripts/build_dist.py --zip`: deterministically assemble `dev/` sources into `dist/credence/`, validate, then emit `version/<v>-release.zip` + `version/<v>-release.zip.sha256`.
3. Create the git tag `vX.Y.Z` and push it. Tags and Releases **are retained and no longer cleaned up** — historical versions can be checked out/downloaded directly by tag, and `npx github:tywinlu1988/credence-global#<tag>` supports pinned-version installation.
4. Create the GitHub Release for that tag and attach **both** `version/<v>-release.zip` and `version/<v>-release.zip.sha256` (the sidecar is what `bin/install.js` verifies against).
5. Update version history in `dev/README.md` and `dev/engine/engine-overview.md`.

> Historical note: pre-v0.0.1 snapshots experimented with committing a `version/<v>/` directory (flat copy, mirrored three-root, installable package) to git. That convention is retired: the git tree is no longer the distribution channel, and `bin/install.js` no longer reads `version/` from the npm tarball.
