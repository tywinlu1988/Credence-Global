#!/usr/bin/env python3
"""Credence version promotion script (Recommendation 4: single source of truth for version declarations).

Accepts a new version number, rewrites all version declaration points per **explicit rule table**
(28 CORE_DOCS headers, 4 SKILL.md files, references headers, README/AGENTS/dev README,
pyproject/package.json, EXPECTED_VERSION, build_dist fallback, .gitignore anti-pattern,
VERSION-MANAGEMENT's "currently" lines). Only matches declaration forms -- version history
tables, "since vX" narratives, "v0.0.1 skill architecture" era descriptions, paradigm version
headers are all outside the rules and naturally immune.

Default dry-run (prints file:line old_line->new_line per-item and remaining unmatched occurrences),
--apply writes to disk. Requires no tracked modifications in the working tree before applying
(?? untracked are allowed).
"""

import argparse
import re
import subprocess
import sys
from collections import namedtuple
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(Path(__file__).resolve().parent))
from consistency_check import CORE_DOCS  # noqa: E402  single source of truth, don't duplicate manifest

SKILL_NAMES = [
    "credit-analysis-router",
    "fixed-income-credit-analysis",
    "credit-report-builder",
    "credit-qa-verifier",
]

VERSION_RE = re.compile(r"^v(\d+\.\d+\.\d+)(?:-[a-z0-9-]+)?$")
EXPECTED_RE = re.compile(r'^EXPECTED_VERSION\s*=\s*"([^"]+)"', re.MULTILINE)

Change = namedtuple("Change", ["rule_id", "path", "line_no", "old_line", "new_line"])


def derive_semver(version: str):
    """v0.0.1 -> 0.0.1; returns None if invalid."""
    m = VERSION_RE.match(version)
    return m.group(1) if m else None


def detect_old_version(root: Path):
    text = (root / "scripts" / "consistency_check.py").read_text(encoding="utf-8")
    m = EXPECTED_RE.search(text)
    return m.group(1) if m else None


def _rules(root: Path, old: str, new: str, semver: str, old_semver: str):
    """Rule table: (rule_id, [relative paths], compiled regex, replacement string). Only matches declaration forms."""
    O = re.escape(old)
    OS = re.escape(old_semver)
    refs = sorted(
        str(p.relative_to(root)).replace("\\", "/")
        for p in root.glob("dev/.claude/skills/*/references/*.md")
    )
    templates = sorted(
        str(p.relative_to(root)).replace("\\", "/")
        for p in root.glob("dev/templates/*.html")
    )
    return [
        ("engine-headers", [f"dev/engine/{d}" for d in CORE_DOCS],
         re.compile(r"(\*\*(?:版本|Version)\*\*[:：]\s*)" + O), r"\g<1>" + new),
        ("engine-crossrefs", [f"dev/engine/{d}" for d in CORE_DOCS],
         re.compile(r"([（(])" + O + r"([）)])"), r"\g<1>" + new + r"\g<2>"),
        ("engine-current", [f"dev/engine/{d}" for d in CORE_DOCS],
         re.compile(r"((?:当前|current) )" + O), r"\g<1>" + new),
        ("overview-table", ["dev/engine/engine-overview.md"],
         re.compile(r"(\|\s*[\w.-]+\.md\s*\|\s*)" + O + r"(?=\s*\|)"), r"\g<1>" + new),
        ("overview-sysver", ["dev/engine/engine-overview.md"],
         re.compile(r"(\*\*(?:引擎版本|Engine Version)\*\*\s*\|[^|\n]*\|\s*)" + O + r"(?=\s*\|)"), r"\g<1>" + new),
        ("skill-version", [f"dev/.claude/skills/{s}/SKILL.md" for s in SKILL_NAMES],
         re.compile(r"(\*\*(?:对应引擎版本|Corresponding Engine Version)\*\*[:：]\s*)" + O), r"\g<1>" + new),
        ("skill-title", ["dev/.claude/skills/fixed-income-credit-analysis/SKILL.md"],
         re.compile(r"(# Fixed Income Credit Analysis Engine\s*)" + O), r"\g<1>" + new),
        ("references-headers", refs,
         re.compile(r"(\*\*(?:版本|Version)\*\*[:：]\s*)" + O), r"\g<1>" + new),
        ("dev-readme-header", ["dev/README.md"],
         re.compile(r"(\*\*(?:版本|Version)\*\*[:：]\s*)" + O), r"\g<1>" + new),
        ("agents-version", ["AGENTS.md"],
         re.compile(r"(\*\*(?:引擎版本|Engine Version)\*\*[:：]\s*)" + O), r"\g<1>" + new),
        ("readme-badge", ["README.md"],
         re.compile(r"`" + O + r"`"), f"`{new}`"),
        ("pyproject", ["pyproject.toml"],
         re.compile(r'^(version\s*=\s*")' + OS + r'"', re.MULTILINE), r"\g<1>" + semver + '"'),
        ("package-json", ["package.json"],
         re.compile(r'("version"\s*:\s*")' + OS + r'"'), r"\g<1>" + semver + '"'),
        ("expected-version", ["scripts/consistency_check.py"],
         re.compile(r'(EXPECTED_VERSION\s*=\s*")' + O + r'"'), r"\g<1>" + new + '"'),
        ("build-dist-fallback", ["scripts/build_dist.py"],
         re.compile(r'(return m\.group\(1\) if m else ")' + O + r'"'), r"\g<1>" + new + '"'),
        ("templates-stamps", templates,
         re.compile(O), new),
        ("adapters-codex", ["docs/adapters/codex.md"],
         re.compile(r"(\*\*(?:引擎版本|Engine Version)\*\*[:：]\s*)" + O), r"\g<1>" + new),
        ("version-mgmt-header", ["docs/VERSION-MANAGEMENT.md"],
         re.compile(r"(\*\*(?:对应引擎版本|Corresponding Engine Version)\*\*[:：]\s*)" + O), r"\g<1>" + new),
        ("version-mgmt-path", ["docs/VERSION-MANAGEMENT.md"],
         re.compile(r"`version/" + O + r"/`"), f"`version/{new}/`"),
        ("version-mgmt-tag", ["docs/VERSION-MANAGEMENT.md"],
         re.compile(r"`" + O + r"`"), f"`{new}`"),
    ]


def apply_rules(root: Path, old: str, new: str, apply: bool) -> list:
    """Rewrite declaration points per rule table; apply=False reports only without writing to disk. Returns list of Changes."""
    semver = derive_semver(new)
    old_semver = derive_semver(old)
    if semver is None or old_semver is None:
        raise ValueError(f"Invalid version format: old={old!r} new={new!r}")
    changes = []
    for rule_id, files, pattern, repl in _rules(root, old, new, semver, old_semver):
        for rel in files:
            path = root / rel
            if not path.is_file():
                continue  # sparse/partial tree: skip missing files (full tree integrity guaranteed by check_versions)
            lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
            touched = False
            for i, line in enumerate(lines):
                new_line = pattern.sub(repl, line)
                if new_line != line:
                    changes.append(
                        Change(rule_id, rel, i + 1, line.rstrip("\n"), new_line.rstrip("\n"))
                    )
                    lines[i] = new_line
                    touched = True
            if touched and apply:
                path.write_text("".join(lines), encoding="utf-8", newline="\n")
    return changes


def _git_grep(root: Path, old: str) -> set:
    out = subprocess.run(
        ["git", "grep", "-n", old, "--", ".", ":!version"],
        cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace",
    ).stdout
    hits = set()
    for line in out.splitlines():
        path, line_no, _content = line.split(":", 2)
        hits.add((path, line_no))
    return hits


def _working_tree_clean(root: Path) -> bool:
    out = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace",
    ).stdout
    return all(line.startswith("??") for line in out.splitlines())


def main() -> int:
    parser = argparse.ArgumentParser(description="Credence version promotion (dry-run by default)")
    parser.add_argument("new_version")
    parser.add_argument("--old", default=None, help="old version (default: auto-detect from consistency_check)")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    if derive_semver(args.new_version) is None:
        print(f"Invalid new version format: {args.new_version!r} (must be vX.Y.Z-<stage>)")
        return 1
    old = args.old or detect_old_version(ROOT)
    if old is None:
        print("Cannot detect old version from consistency_check.py, specify with --old")
        return 1
    if args.apply and not _working_tree_clean(ROOT):
        print("Working tree has tracked changes, --apply refused (commit or stash first)")
        return 1

    changes = apply_rules(ROOT, old, args.new_version, apply=args.apply)
    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"[{mode}] {old} -> {args.new_version}: {len(changes)} declaration rewrite(s)")
    for c in changes:
        print(f"  [{c.rule_id}] {c.path}:{c.line_no}")
        print(f"    - {c.old_line.strip()[:100]}")
        print(f"    + {c.new_line.strip()[:100]}")

    changed_keys = {(c.path, str(c.line_no)) for c in changes}
    leftovers = sorted(_git_grep(ROOT, old) - changed_keys)
    print(f"\nUncovered old version occurrences ({len(leftovers)}, should be all historical references, please verify manually):")
    for path, line_no in leftovers:
        print(f"  {path}:{line_no}")
    if not args.apply:
        print("\n(dry-run, not written to disk; add --apply to confirm)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
