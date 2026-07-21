#!/usr/bin/env bash
# End-to-end smoke test for bin/install.js: build the real release zip, serve it
# locally exactly as GitHub Releases would, run the installer against it, verify
# the extracted layout and the checksum-tamper rejection. Requires python + node.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

TAG=$(python -c "
import re
text = open('scripts/consistency_check.py', encoding='utf-8').read()
print(re.search(r'EXPECTED_VERSION\s*=\s*\"(.+?)\"', text).group(1))")
echo ">> release tag: $TAG"

python scripts/build_dist.py --zip >/dev/null
SERVE="$(mktemp -d)"
mkdir -p "$SERVE/$TAG"
cp "version/$TAG-release.zip" "version/$TAG-release.zip.sha256" "$SERVE/$TAG/"

PORT=$(python -c "
import socket
s = socket.socket(); s.bind(('127.0.0.1', 0)); print(s.getsockname()[1]); s.close()")
python -m http.server "$PORT" --bind 127.0.0.1 --directory "$SERVE" >/dev/null 2>&1 &
SERVER_PID=$!
trap 'kill $SERVER_PID 2>/dev/null || true; rm -rf "$SERVE" "$WORK"' EXIT

WORK="$(mktemp -d)"
sleep 1
# fail fast if the server did not bind (e.g., stale process on the port)
curl -fsS -o /dev/null "http://127.0.0.1:$PORT/$TAG/$TAG-release.zip.sha256" || {
  echo "!! local release server did not come up on port $PORT" >&2
  exit 1
}

echo ">> positive path: download + checksum + extract"
cd "$WORK"
CREDENCE_TAG="$TAG" CREDENCE_RELEASES_BASE="http://127.0.0.1:$PORT" node "$ROOT/bin/install.js" credence

test -f credence/AGENTS.md
test -f credence/engine/pipeline-contract.md
test -f credence/templates/template-base.css
test -f credence/src/pipeline.py
test -d credence/.claude/skills/credit-analysis-router
echo ">> layout OK"

echo ">> tamper path: corrupted sidecar must abort with exit 1"
printf 'deadbeef0000000000000000000000000000000000000000000000000000000000  %s-release.zip\n' "$TAG" \
  > "$SERVE/$TAG/$TAG-release.zip.sha256"
if CREDENCE_TAG="$TAG" CREDENCE_RELEASES_BASE="http://127.0.0.1:$PORT" node "$ROOT/bin/install.js" credence2 2>/dev/null; then
  echo "!! tampered zip was accepted" >&2
  exit 1
fi
echo ">> tamper rejected OK"

echo ">> existing-dest guard"
if CREDENCE_TAG="$TAG" CREDENCE_RELEASES_BASE="http://127.0.0.1:$PORT" node "$ROOT/bin/install.js" credence 2>/dev/null; then
  echo "!! existing destination was not rejected" >&2
  exit 1
fi
echo ">> dest-exists rejected OK"

echo "SMOKE OK ($TAG)"
