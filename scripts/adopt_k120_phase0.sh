#!/usr/bin/env bash
# K120 Phase-0 — SEO daily digest full ingest (3 arXiv)
set -euo pipefail
AUDIT="${TMPDIR:-/tmp}/k120-phase0-audit"
mkdir -p "$AUDIT"
cd "$AUDIT"

echo "K120 Phase-0 audits (SEO wiki)"
echo "=============================="

clone_smoke() {
  local repo="$1"
  local dir="${repo##*/}"
  if [[ ! -d "$dir/.git" ]]; then
    git clone --depth 1 "https://github.com/${repo}.git" "$dir" 2>/dev/null || {
      echo "WARN: clone failed: $repo"
      return 0
    }
  fi
  echo "OK clone: $repo"
  gh api "repos/${repo}" --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || true
}

# DeepRubric — Apache-2.0 code release
clone_smoke zminghang/DeepRubric-Code

echo ""
echo "Verdicts (2026-06-16):"
echo "  arxiv-2606.16344 (hotel LLM reputation audit)  REFERENCE — no code; operator GEO playbook + hands-on brief"
echo "  arxiv-2606.11290 (FlowBank)                    REFERENCE — project page only; conductor portfolio steal"
echo "  arxiv-2606.17029 (DeepRubric)                  REFERENCE — Apache-2.0; evidence-tree rubric steal; no RL on laptop"
echo ""
echo "No barbershop operator installs. See wiki/sources/ and briefs/2026-06-16_k120-*.md"
