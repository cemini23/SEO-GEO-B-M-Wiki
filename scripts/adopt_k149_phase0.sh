#!/usr/bin/env bash
# K149 Phase-0 - SEO digest (4/4 OOD arXiv API false positives)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "K149 Phase-0 audits (SEO wiki)"
echo "=============================="
echo ""
echo "1) IndelFreeAligner (2607.27291) — genomics/BBTools — OUT-OF-SCOPE (no SEO adopt)"
echo "2) ORCA-bench (2607.28545) — agent oncall RCA — OUT-OF-SCOPE; ~50GB Harbor dataset Watch"
echo "   → CCC + Cyber briefs (no prod scp)"
echo "3) Böotes III / Styx (2607.28594) — astro-ph — OUT-OF-SCOPE overflow only"
echo "4) Seiberg dualities ML (2607.28628) — hep-th — OUT-OF-SCOPE; thin CCC pathfinder brief"
echo ""
echo "Atto / TipDrop / poker / prod: SKIP"
echo "Local SEO adopt disk this pass: 0 MB"
echo "Root: $ROOT"
