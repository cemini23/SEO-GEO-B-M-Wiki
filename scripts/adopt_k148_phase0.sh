#!/usr/bin/env bash
# K148 Phase-0 - SEO digest (DenseOn/LateOn + 2 OOD)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TOOLS="$ROOT/raw-sources/tools"

echo "K148 Phase-0 audits (SEO wiki)"
echo "=============================="
echo ""
echo "1) DenseOn / LateOn (arXiv 2607.27178) — IN-SCOPE GEO/AEO retrieval"
echo "   HF lightonai/DenseOn ~600MB  → Watch (over 500MB adopt cap)"
echo "   HF lightonai/LateOn  ~600MB+ → Watch"
echo "   Datasets embeddings-* multi-GB → Watch / no pull"
echo "   github.com/lightonai/pylate MIT → GO Adopt (~2.6MB)"
echo "   github.com/lightonai/fast-plaid MIT → GO Adopt (~4.4MB)"
echo ""
if [[ -d "$TOOLS/pylate/.git" ]]; then
  echo "   ADOPTED: $TOOLS/pylate ($(du -sh "$TOOLS/pylate" | awk '{print $1}'))"
else
  echo "   MISSING pylate — clone failed?"
fi
if [[ -d "$TOOLS/fast-plaid/.git" ]]; then
  echo "   ADOPTED: $TOOLS/fast-plaid ($(du -sh "$TOOLS/fast-plaid" | awk '{print $1}'))"
else
  echo "   MISSING fast-plaid — clone failed?"
fi
echo ""
echo "2) arXiv 2607.27188 RND options inverse learning — OUT-OF-SCOPE → OSINT+Gambling"
echo "3) arXiv 2607.27190 quadratic axion string theory — OUT-OF-SCOPE overflow only"
echo ""
echo "Atto: thin multilingual retrieval brief (DenseOn/LateOn)"
echo "TipDrop / poker / prod: SKIP (no image/arena/harness install)"
echo "Local adopt disk this pass: ~7MB (under 500MB)"
