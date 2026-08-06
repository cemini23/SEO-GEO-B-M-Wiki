#!/usr/bin/env bash
# K153 Phase-0 - SEO digest (3 OOD; RepairFormer → Atto adopt)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ATTO_ADOPT="${ATTO_ADOPT:-/Users/claudiobarone/Projects/atto/.local/adopts/RepairFormer}"

echo "K153 Phase-0 audits (SEO wiki)"
echo "=============================="
echo ""
echo "1) RepairFormer (2608.05060) — OUT-OF-SCOPE for SEO (≠ schema.org)"
echo "   github.com/pass-uh/RepairFormer MIT ~5MB → GO Adopt on Atto"
if [[ -d "$ATTO_ADOPT/.git" ]]; then
  echo "   ADOPTED: $ATTO_ADOPT ($(du -sh "$ATTO_ADOPT" | awk '{print $1}'))"
else
  echo "   MISSING Atto adopt — clone failed?"
fi
echo "2) Generalized Glauber axion/graviton (2608.05082) — OUT-OF-SCOPE hep-ph"
echo "3) DASyR-LLM kinetic SR (2608.05120) — OUT-OF-SCOPE chemeng"
echo "   Zenodo → Watch / CCC thin brief only"
echo ""
echo "GuruWatcher / TipDrop / poker / prod: SKIP"
echo "Local SEO adopt disk this pass: 0 MB (Atto adopt ~5MB under 500MB)"
echo "Root: $ROOT"
