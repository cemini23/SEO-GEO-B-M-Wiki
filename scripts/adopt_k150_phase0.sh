#!/usr/bin/env bash
# K150 Phase-0 - SEO digest (3/3 OOD arXiv API false positives)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "K150 Phase-0 audits (SEO wiki)"
echo "=============================="
echo ""
echo "1) Multi-policy PEFT task sequencing (2607.29601) — OUT-OF-SCOPE (cs.LG)"
echo "   No public code → REFERENCE via CCC brief only"
echo "2) QASP query-adaptive vector search (2607.29606) — OUT-OF-SCOPE (ANN infra)"
echo "   No public QASP code; related Quake (marius-team/quake ~22MB MIT) = different paper → Watch / no SEO adopt"
echo "3) ExtractBench schema-guided IE (2607.29677) — OUT-OF-SCOPE (JSON Schema ≠ schema.org)"
echo "   Claimed GitHub run-llama/ExtractBench → 404 at ingest; HF Watch / no pull"
echo "   → Atto + CCC briefs (genealogy/agent extraction steal)"
echo ""
echo "Atto: ExtractBench schema+grounding brief"
echo "TipDrop / poker / prod: SKIP"
echo "Local SEO adopt disk this pass: 0 MB"
echo "Root: $ROOT"
