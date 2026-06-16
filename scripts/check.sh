#!/usr/bin/env bash
# check.sh — post-build sanity gate for the Astronautisté promo site.
#
# 🇨🇿 Ověří, že build vyprodukoval očekávané výstupy a neobsahuje nerozrenderované
#     Tera artefakty. Volá se po build.sh; používá se i v CI jako coverage assert.
set -Eeuo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PUB="${1:-$ROOT/public}"

fail=0
need() { [ -f "$PUB/$1" ] && echo "ok   $1" || { echo "FAIL missing: $1"; fail=1; }; }

echo "==> Required outputs"
need index.html
need docs/index.html
need sitemap.xml
need css/main.css
need js/flowbite.min.js
need CNAME
need og/astronautiste-og.png
need robots.txt
need site.webmanifest
need .well-known/security.txt

echo "==> No unrendered Tera artifacts"
if grep -rlE '\{\{|\{%' "$PUB"/index.html "$PUB"/docs/index.html >/dev/null 2>&1; then
  echo "FAIL: unrendered Tera tags found"; fail=1
else
  echo "ok   clean"
fi

echo "==> Key content present"
grep -q "Without guessing" "$PUB/index.html" && echo "ok   hero headline" || { echo "FAIL: hero headline missing"; fail=1; }
grep -q "astronautiste.cz/og/astronautiste-og.png" "$PUB/index.html" && echo "ok   absolute og:image" || { echo "FAIL: og:image not absolute"; fail=1; }

[ "$fail" -eq 0 ] && echo "✅ check passed" || { echo "❌ check failed"; exit 1; }
