#!/usr/bin/env python3
"""Publish the built dist/credence/ package to the orphan `plugin-dist` branch.

The main repository does not track dist/ (gitignored) or version/ (only .gitkeep),
so there is no commitable package entity for a marketplace to point at. This script
solves distribution by maintaining an orphan branch `plugin-dist` whose root IS the
installable package (AGENTS.md, engine/, templates/, src/, .claude-plugin/).

Usage:
  python scripts/publish_plugin.py            # build + publish to plugin-dist
  python scripts/publish_plugin.py --check    # verify plugin-dist is in sync with dist/

Requires: clean working tree, git push access to origin (SSH).
"""

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist" / "credence"
BRANCH = "plugin-dist"


def _git(*args, cwd=None, check=True):
    result = subprocess.run(
        ["git", *args], cwd=cwd or ROOT,
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if check and result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result


def _write_marketplace_json(pkg_root: Path, version: str) -> None:
    marketplace = {
        "name": "credence-marketplace",
        "owner": {
            "name": "tywinlu1988",
            "url": "https://github.com/tywinlu1988",
        },
        "plugins": [
            {
                "name": "credence",
                "source": "./",
                "description": "Methodology-first fixed-income credit analysis engine "
                "(four-stage skill chain: router / analysis / report / qa)",
                "version": version,
            }
        ],
    }
    plugin_dir = pkg_root / ".claude-plugin"
    plugin_dir.mkdir(parents=True, exist_ok=True)
    (plugin_dir / "marketplace.json").write_text(
        json.dumps(marketplace, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8", newline="\n",
    )


def publish(push: bool) -> None:
    if not DIST.is_dir():
        raise SystemExit("dist/credence/ not built — run `python scripts/build_dist.py` first")
    if _git("status", "--porcelain").stdout.strip():
        raise SystemExit("working tree not clean — commit or stash first")

    version = json.loads((DIST / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]
    print(f"publishing credence {version} to branch {BRANCH}")

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        if _git("branch", "--list", BRANCH).stdout.strip():
            _git("worktree", "add", str(tmp_path), BRANCH)
        else:
            # portable orphan creation: detached worktree + checkout --orphan
            _git("worktree", "add", "--detach", str(tmp_path), "HEAD")
            _git("checkout", "--orphan", BRANCH, cwd=tmp_path)
            _git("rm", "-rf", "--quiet", ".", cwd=tmp_path)
        try:
            # wipe branch content, then copy the fresh package
            for item in tmp_path.iterdir():
                if item.name == ".git":
                    continue
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()
            shutil.copytree(DIST, tmp_path, dirs_exist_ok=True)
            _write_marketplace_json(tmp_path, version)

            _git("add", "-A", cwd=tmp_path)
            if not _git("diff", "--cached", "--quiet", check=False, cwd=tmp_path).returncode:
                _git("commit", "-m", f"credence {version}: plugin package for marketplace", cwd=tmp_path)
                print("committed package to", BRANCH)
            else:
                print("no changes vs existing", BRANCH)
            if push:
                _git("push", "origin", f"{BRANCH}:{BRANCH}")
                print("pushed", BRANCH, "to origin")
        finally:
            _git("worktree", "remove", "--force", str(tmp_path), check=False)


def check() -> bool:
    local_head = _git("rev-parse", BRANCH, check=False)
    if local_head.returncode:
        print(f"branch {BRANCH} does not exist")
        return False
    print(f"{BRANCH} head: {local_head.stdout.strip()[:12]}")
    remote = _git("ls-remote", "origin", BRANCH)
    print(f"origin/{BRANCH}: {remote.stdout.split()[0][:12] if remote.stdout.strip() else '(absent)'}")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="show branch sync state without publishing")
    ap.add_argument("--no-push", action="store_true", help="commit locally without pushing")
    args = ap.parse_args()
    if args.check:
        return 0 if check() else 1
    publish(push=not args.no_push)
    return 0


if __name__ == "__main__":
    sys.exit(main())
