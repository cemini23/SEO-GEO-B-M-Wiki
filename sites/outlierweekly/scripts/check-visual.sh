#!/usr/bin/env bash
# Confirm the owned hub keeps the light palette, stylesheet link, and verification tags.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
css="${root}/public/styles.css"
public="${root}/public"

fail() {
  printf 'FAIL: %s\n' "$*" >&2
  exit 1
}

[[ -f "${css}" ]] || fail "missing styles.css"

css_lc="$(tr '[:upper:]' '[:lower:]' < "${css}")"
[[ "${css_lc}" != *0e1116* ]] || fail "styles.css contains 0e1116"

token=""
for token in spectral ff6719 363737; do
  [[ "${css_lc}" == *"${token}"* ]] || fail "styles.css missing ${token}"
done

count=0
while IFS= read -r -d '' file; do
  count=$((count + 1))
  grep -q 'href="/styles.css"' "${file}" || fail "${file} missing /styles.css"
  grep -q 'google-site-verification' "${file}" || fail "${file} missing google-site-verification"
  grep -q 'msvalidate.01' "${file}" || fail "${file} missing msvalidate.01"
  if grep -q 'site-header' "${file}"; then
    grep -q 'class="subscribe"' "${file}" || fail "${file} missing class=subscribe"
  fi
done < <(find "${public}" -type f -name '*.html' -print0)

[[ "${count}" -gt 0 ]] || fail "no html pages"

home="${public}/index.html"
grep -q 'class="letters"' "${home}" || fail "homepage missing class=letters"
grep -q 'youratto.com' "${home}" || fail "homepage missing youratto.com"
grep -q 'guruwatcher.com' "${home}" || fail "homepage missing guruwatcher.com"

printf 'ok %s\n' "${count}"
