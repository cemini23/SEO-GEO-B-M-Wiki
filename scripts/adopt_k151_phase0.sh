#!/usr/bin/env bash
# K151 Phase-0 - SEO digest (3/3 OOD arXiv API false positives; 1 thin GEO steal)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "K151 Phase-0 audits (SEO wiki)"
echo "=============================="
echo ""
echo "1) Pinterest VLM relevance (2608.02446) — OUT-OF-SCOPE Adopt (no public code)"
echo "   Thin GEO steal → geo-visibility-measurement (engagement ≠ semantic relevance guardrail)"
echo "   → CCC brief"
echo "2) AtumAI datacenter control-plane (2608.02569) — OUT-OF-SCOPE systems/cloud"
echo "   No public framework code → CCC agentic-policy brief only"
echo "3) Smooth simplicial reparameterizations (2608.02576) — OUT-OF-SCOPE math"
echo "   github.com/Arafat245/smooth_reparameterizations ~17KB null-SPDX → NO SEO adopt"
echo ""
echo "Atto / GuruWatcher / TipDrop / poker / prod: SKIP"
echo "Local SEO adopt disk this pass: 0 MB"
echo "Root: $ROOT"
