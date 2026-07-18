#!/usr/bin/env bash
# Phase-0 for K142: E-GEO code (adopt) + agent-ready paper (REFERENCE only).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "=== K142 Phase-0 ==="
echo "1) E-GEO GitHub clone (already at raw-sources/tools/E-GEO)"
if [[ -d raw-sources/tools/E-GEO ]]; then
  du -sh raw-sources/tools/E-GEO
  test ! -f raw-sources/tools/E-GEO/LICENSE && echo "WARN: no LICENSE — CONDITIONAL-GO"
  test -f raw-sources/tools/E-GEO/src/optimized_prompts.json && echo "OK: optimized_prompts.json present"
else
  echo "MISSING clone — run: git clone --depth 1 https://github.com/psbagga17/E-GEO.git raw-sources/tools/E-GEO"
  exit 1
fi

echo "2) HF dataset — SKIP (Watch; do not pull without size check)"
echo "3) Agent-ready paper — REFERENCE only (no author code)"
echo "=== Phase-0 complete: E-GEO CONDITIONAL-GO; agent-ready REFERENCE ==="
