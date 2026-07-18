#!/usr/bin/env bash
# Phase-0 + local adopt for K142 and prior CONDITIONAL-GO tools still missing on disk.
# Budget: keep total raw-sources adopt under 500 MB.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "=== Local adopt (K142 + pending CONDITIONAL-GO) ==="

echo "1) E-GEO code"
if [[ -d raw-sources/tools/E-GEO ]]; then
  du -sh raw-sources/tools/E-GEO
  test ! -f raw-sources/tools/E-GEO/LICENSE && echo "WARN: no LICENSE — CONDITIONAL-GO"
  test -f raw-sources/tools/E-GEO/src/optimized_prompts.json && echo "OK: optimized_prompts.json"
else
  git clone --depth 1 https://github.com/psbagga17/E-GEO.git raw-sources/tools/E-GEO
fi

echo "2) E-GEO HF slim dataset (exclude queries_products + train_val_full ≈ 558 MB)"
DEST=raw-sources/datasets/E-GEO
if [[ ! -f "$DEST/data/test_data.json" ]]; then
  mkdir -p "$DEST"
  hf download psbagga17/E-GEO --repo-type dataset --local-dir "$DEST" \
    --include "data/test_data.json" \
    --include "data/train1000_val500.json" \
    --include "data/test_selected_products.json" \
    --include "data/train_selected_products.json" \
    --include "data/initial_ranking/**" \
    --include "README.md" \
    --include "results/META_OPT_RESULTS/best_prompts.json"
fi
du -sh "$DEST"
echo "SKIP full data/queries_products.json + data/train_val_full.json (over budget)"

echo "3) geo-optimizer-skill (K134 CONDITIONAL-GO)"
if [[ ! -d raw-sources/tools/geo-optimizer-skill/.git ]]; then
  git clone --depth 1 https://github.com/Auriti-Labs/geo-optimizer-skill.git raw-sources/tools/geo-optimizer-skill
fi
du -sh raw-sources/tools/geo-optimizer-skill
test -f raw-sources/tools/geo-optimizer-skill/LICENSE && echo "OK: MIT LICENSE"

echo "4) wondelai/skills (K113 CONDITIONAL-GO)"
if [[ ! -d raw-sources/tools/wondelai-skills/.git ]]; then
  git clone --depth 1 https://github.com/wondelai/skills.git raw-sources/tools/wondelai-skills
fi
du -sh raw-sources/tools/wondelai-skills

echo "5) Agent-ready paper — REFERENCE only (no author code)"

echo "=== Disk summary ==="
du -sh raw-sources/tools/E-GEO raw-sources/tools/geo-optimizer-skill raw-sources/tools/wondelai-skills raw-sources/datasets/E-GEO 2>/dev/null
echo "=== Done ==="
