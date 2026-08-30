#!/usr/bin/env bash
# Deploy the Outlier Weekly owned hub. The parent (human) runs this after review.
# Worker name is LOCKED to outlierweekly-redirect — routes already point at it.
# A failed IndexNow ping must warn, never fail the deploy.
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

echo "Deploying worker 'outlierweekly-redirect' from $(pwd) ..."
# wrangler is not always on PATH; pin v4 so workers_dev / preview_urls apply.
npx --yes wrangler@4 deploy
echo "Deploy OK."

echo "Pinging IndexNow with owned URLs from public/sitemap.xml ..."
# Run in a child shell so IndexNow exit 1 cannot abort the deploy.
if bash scripts/indexnow-ping.sh; then
  echo "IndexNow OK."
else
  echo "WARN: IndexNow ping failed. Deploy stays live; retry with: bash scripts/indexnow-ping.sh" >&2
fi
