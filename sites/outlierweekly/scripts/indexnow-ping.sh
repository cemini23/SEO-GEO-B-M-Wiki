#!/usr/bin/env bash
# Ping IndexNow with every owned URL from public/sitemap.xml.
# The IndexNow key lives on outlierweekly.com only — never ping *.substack.com URLs.
# Exit 0 on HTTP 200 or 202; exit 1 otherwise.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
SITEMAP="$PROJECT_DIR/public/sitemap.xml"

HOST="outlierweekly.com"
KEY="de772b30118b4e6b8ac9b5dd3b52263d"
KEY_LOCATION="https://outlierweekly.com/de772b30118b4e6b8ac9b5dd3b52263d.txt"

if [ ! -f "$SITEMAP" ]; then
  echo "ERROR: sitemap not found at $SITEMAP" >&2
  exit 1
fi

# urlList = every <loc> in the owned sitemap.
URL_LIST="$(sed -n 's:.*<loc>\(.*\)</loc>.*:\1:p' "$SITEMAP")"
if [ -z "$URL_LIST" ]; then
  echo "ERROR: no <loc> entries found in $SITEMAP" >&2
  exit 1
fi

# Build a JSON array from the URL list.
URLS_JSON="["
FIRST=1
while IFS= read -r u; do
  [ -z "$u" ] && continue
  if [ "$FIRST" = "1" ]; then
    URLS_JSON="${URLS_JSON}\"$u\""
    FIRST=0
  else
    URLS_JSON="${URLS_JSON},\"$u\""
  fi
done <<< "$URL_LIST"
URLS_JSON="${URLS_JSON}]"

PAYLOAD="{\"host\":\"$HOST\",\"key\":\"$KEY\",\"keyLocation\":\"$KEY_LOCATION\",\"urlList\":$URLS_JSON}"

HTTP_CODE="$(curl -sS --max-time 30 -o /tmp/indexnow-response-$$.txt -w '%{http_code}' \
  -X POST "https://api.indexnow.org/indexnow" \
  -H 'Content-Type: application/json; charset=utf-8' \
  --data "$PAYLOAD")" || HTTP_CODE="000"
rm -f /tmp/indexnow-response-$$.txt

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "202" ]; then
  echo "IndexNow ping OK (HTTP $HTTP_CODE) for $URLS_JSON"
  exit 0
fi

echo "ERROR: IndexNow ping returned HTTP $HTTP_CODE for $URLS_JSON" >&2
exit 1
