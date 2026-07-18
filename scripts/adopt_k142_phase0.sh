#!/usr/bin/env bash
# Phase-0 + local adopt for K142 and prior CONDITIONAL-GO tools.
# Budget: 750 MB (raised 2026-07-18 so full E-GEO HF data/ can land).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
BUDGET_MB=750

echo "=== Local adopt (budget ${BUDGET_MB} MB) ==="

echo "1) E-GEO code"
if [[ ! -d raw-sources/tools/E-GEO/.git ]]; then
  git clone --depth 1 https://github.com/psbagga17/E-GEO.git raw-sources/tools/E-GEO
fi
du -sh raw-sources/tools/E-GEO
test ! -f raw-sources/tools/E-GEO/LICENSE && echo "WARN: no LICENSE — CONDITIONAL-GO"
test -f raw-sources/tools/E-GEO/src/optimized_prompts.json && echo "OK: optimized_prompts.json"

echo "2) E-GEO HF full data/ (+ best_prompts)"
DEST=raw-sources/datasets/E-GEO
mkdir -p "$DEST"
if [[ ! -f "$DEST/data/queries_products.json" ]]; then
  hf download psbagga17/E-GEO --repo-type dataset --local-dir "$DEST" \
    --include "data/**" \
    --include "results/META_OPT_RESULTS/best_prompts.json" \
    --include "README.md"
fi
du -sh "$DEST"

echo "3) geo-optimizer-skill (K134 CONDITIONAL-GO)"
if [[ ! -d raw-sources/tools/geo-optimizer-skill/.git ]]; then
  git clone --depth 1 https://github.com/Auriti-Labs/geo-optimizer-skill.git raw-sources/tools/geo-optimizer-skill
fi
du -sh raw-sources/tools/geo-optimizer-skill

echo "4) wondelai/skills (K113 CONDITIONAL-GO)"
if [[ ! -d raw-sources/tools/wondelai-skills/.git ]]; then
  git clone --depth 1 https://github.com/wondelai/skills.git raw-sources/tools/wondelai-skills
fi
du -sh raw-sources/tools/wondelai-skills

echo "5) Agent-ready paper — REFERENCE only (no author code)"

echo "=== Disk summary vs ${BUDGET_MB} MB ==="
python3 - <<'PY'
import subprocess
paths = [
  "raw-sources/tools/E-GEO",
  "raw-sources/tools/geo-optimizer-skill",
  "raw-sources/tools/wondelai-skills",
  "raw-sources/datasets/E-GEO",
]
budget = 750
t = 0
for p in paths:
    try:
        kb = int(subprocess.check_output(["du", "-sk", p], text=True).split()[0])
    except Exception:
        continue
    t += kb
    print(f"{p}: {kb/1024:.1f} MB")
print(f"TOTAL: {t/1024:.1f} MB  {'OK' if t/1024 <= budget else 'OVER BUDGET'}")
PY

echo "=== Usage hooks ==="
echo "  E-GEO rewrite:  python3 scripts/e_geo_rewrite_service_page.py --help"
echo "  GEO audit:      bash scripts/run_geo_audit.sh https://YOUR-SHOP"
echo "  Wondelai CRO:   read raw-sources/tools/wondelai-skills/cro-methodology/SKILL.md"
echo "=== Done ==="
