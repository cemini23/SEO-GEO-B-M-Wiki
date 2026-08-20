#!/usr/bin/env bash
# K161 Phase-0 - SEO digest (4 OOD; Madin GBP → CCC thin; Datrier CELS → CCC/OSINT thin + MIT REFERENCE; Gressier helium overflow only; Zhang PGFS++ magnet-output → CCC thin)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "K161 Phase-0 audits (SEO wiki)"
echo "=============================="
echo ""
echo "1) Madin et al. GBP collective ranking in patrol swarm (2608.17690) — OUT-OF-SCOPE cs.RO"
echo "   Steal: CCC thin (dual-purpose graph; GBP degrades gracefully under noise)."
echo "   No code URL → no clone"
echo "2) Datrier et al. Cosmic Explorer CELS site-cost GIS (2608.19114) — OUT-OF-SCOPE astro-ph"
echo "   Steal: CCC thin + OSINT thin (GIS multi-factor site cost)."
echo "   gitlab.com/cosmic-explorer/cels — MIT ~2MB → .local/adopts/cels REFERENCE;"
echo "   runtime wont_wire (astro OOD)"
echo "3) Gressier et al. LHS 1140 b helium JWST (2608.19120) — OUT-OF-SCOPE astro-ph.EP"
echo "   Steal: none (overflow only); no code → no clone"
echo "4) Zhang et al. PGFS++ magnet-output molecular RL (2608.19121) — OUT-OF-SCOPE cs.LG"
echo "   Steal: CCC thin (magnet-output / reward-hack diversity collapse)."
echo "   Do NOT clone Graphcore ogb-lsc-pcqm4mv2 (GPS++ ≠ PGFS++). Watch / 0 MB"
echo ""
echo "GuruWatcher / TipDrop / poker / prod: SKIP"
echo "Local SEO adopt disk this pass: ~2 MB CELS REFERENCE only (not wired)"
echo "Phase-1 SEO: no new wire (0 ADOPT/GO)"
echo "Root: $ROOT"
if [[ -d "$ROOT/.local/adopts/cels" ]]; then
  echo "CELS present: $(du -sm "$ROOT/.local/adopts/cels" | awk '{print $1}') MB"
fi
