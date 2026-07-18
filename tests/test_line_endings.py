"""P0 line-ending gate: tracked text files must be LF in the working tree.

`.gitattributes` (`* text=auto eol=lf`) is the enforcement mechanism; this test is
a tripwire -- any CRLF introduced by checkout/commit due to non-standard machine
config will be caught here, instead of silently entering the release zip.
"""

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _tracked_files() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout
    return [line for line in out.splitlines() if line]


def test_gitattributes_enforces_lf():
    content = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    assert "text=auto" in content and "eol=lf" in content


def test_tracked_files_have_no_crlf():
    offenders = []
    for rel in _tracked_files():
        data = (ROOT / rel).read_bytes()
        if b"\0" in data:  # binary heuristic (same as git): skip; binary marked via .gitattributes
            continue
        if b"\r\n" in data:
            offenders.append(rel)
    assert offenders == [], f"CRLF in tracked files: {offenders[:10]}"
