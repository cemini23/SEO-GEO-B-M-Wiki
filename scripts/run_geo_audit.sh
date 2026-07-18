#!/usr/bin/env bash
# Run adopted geo-optimizer-skill CLI against a site URL (K134 CONDITIONAL-GO).
# Usage: bash scripts/run_geo_audit.sh https://your-shop.example
# Citation scores are directional — pair with @concepts/geo-visibility-measurement.md CIs.
set -euo pipefail
URL="${1:-}"
if [[ -z "$URL" ]]; then
  echo "Usage: $0 <https://your-site>" >&2
  echo "Operator: fill shop website on wiki/entities/companies/shop-1.md first." >&2
  exit 1
fi
OUT_DIR="${2:-briefs}"
mkdir -p "$OUT_DIR"
STAMP="$(date +%Y-%m-%d)"
OUT="$OUT_DIR/${STAMP}_geo-optimizer-audit.txt"
echo "Auditing $URL → $OUT"
# Prefer local clone editable install if present; else uvx from PyPI
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
if [[ -d "$ROOT/raw-sources/tools/geo-optimizer-skill" ]]; then
  uvx --from "$ROOT/raw-sources/tools/geo-optimizer-skill" geo audit --url "$URL" 2>&1 | tee "$OUT"
else
  uvx --from geo-optimizer-skill geo audit --url "$URL" 2>&1 | tee "$OUT"
fi
echo "Done. Ignore llms.txt recommendations for Google Search (first-party mythbust)."
