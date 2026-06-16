#!/usr/bin/env bash
# build.sh — canonical build pipeline for the Astronautisté promo site.
#
# 🇨🇿 Sekvence: Tailwind/Flowbite CSS → vendore Flowbite JS → zola build → zola check.
#     Inspirováno toolingem prismatic-platform/sites/promo (right-sized pro malý web).
#
# Env:
#   BASE_URL   override base_url (např. http://localhost:8765 pro lokální náhled)
#   OUTPUT_DIR výstupní adresář (default: public)
set -Eeuo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

OUTPUT_DIR="${OUTPUT_DIR:-public}"

echo "==> [1/4] Tailwind + Flowbite CSS"
npx tailwindcss -i ./styles/input.css -o ./static/css/main.css --minify

echo "==> [2/4] Vendor JS (Flowbite + p5 + Alpine)"
mkdir -p static/js
cp node_modules/flowbite/dist/flowbite.min.js static/js/flowbite.min.js
cp node_modules/p5/lib/p5.min.js static/js/p5.min.js
cp node_modules/alpinejs/dist/cdn.min.js static/js/alpine.min.js
cp node_modules/@alpinejs/intersect/dist/cdn.min.js static/js/alpine-intersect.min.js

echo "==> [3/4] Zola build (output: ${OUTPUT_DIR})"
if [ -n "${BASE_URL:-}" ]; then
  zola build --base-url "$BASE_URL" --output-dir "$OUTPUT_DIR" --force
else
  zola build --output-dir "$OUTPUT_DIR" --force
fi

echo "==> [4/4] Zola check (internal links + structure)"
zola check --skip-external-links || echo "WARN: zola check reported issues (non-blocking locally)"

echo "✅ build complete → ${OUTPUT_DIR} ($(find "$OUTPUT_DIR" -type f | wc -l | tr -d ' ') files)"
