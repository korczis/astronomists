#!/usr/bin/env bash
# serve.sh — local live-preview dev server for the Astronautisté promo site.
#
# 🇨🇿 Spustí Tailwind/Flowbite CSS ve watch módu + `zola serve` s live-reloadem.
#     Otevři http://127.0.0.1:1111 — změny v templates/content/CSS se projeví živě.
#
# Env:
#   PORT       dev server port (default: 1111)
#   IFACE      bind interface (default: 127.0.0.1)
set -Eeuo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PORT="${PORT:-1111}"
IFACE="${IFACE:-127.0.0.1}"

# Vendor Flowbite JS once (served from static/js/).
mkdir -p static/js
cp node_modules/flowbite/dist/flowbite.min.js static/js/flowbite.min.js

# Tailwind/Flowbite CSS in watch mode (rebuilds main.css on template/content edits).
npx tailwindcss -i ./styles/input.css -o ./static/css/main.css --watch >/tmp/astro-tailwind-watch.log 2>&1 &
TW_PID=$!
cleanup() { kill "$TW_PID" 2>/dev/null || true; }
trap cleanup EXIT INT TERM

# Give Tailwind a moment to emit the first CSS so the first page load is styled.
for _ in $(seq 1 30); do [ -s static/css/main.css ] && break; sleep 0.2; done

echo "──────────────────────────────────────────────"
echo "  Astronautisté dev server"
echo "  → open in browser:  http://${IFACE}:${PORT}"
echo "  live reload: templates / content / static / CSS"
echo "  stop: Ctrl-C"
echo "──────────────────────────────────────────────"

# zola serve watches content/templates/static/sass and live-reloads the browser.
exec zola serve --interface "$IFACE" --port "$PORT"
