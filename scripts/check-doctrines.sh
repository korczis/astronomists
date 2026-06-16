#!/usr/bin/env bash
# Doctrine guard — CI pojistka pro doktríny z .aiad/policies/.
# Zrcadlí .githooks/pre-commit Gate 5, ale skenuje CELÝ tracked strom (ne jen staged diff),
# takže platí i bez lokálního core.hooksPath. Spouštěno v .github/workflows/deploy.yml.
#
# Policy: .aiad/policies/flowbite-stack.policy.md
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

# Build SOURCE (css/html/config/package.json/vlastní JS). .md docs jsou EXEMPT
# (dokumentují pravidla), .min.js a build adresáře taky.
files=$(git ls-files \
  | grep -E '\.(css|html)$|(^|/)(tailwind|postcss)\.config\.js$|(^|/)package\.json$|(^|/)(styles|static/js)/.*\.js$' \
  | grep -vE '\.min\.js$|^(public|public-test|node_modules)/' || true)

fail=0

# --- Flowbite v2 / Tailwind v3: zakázaná v4 / Tailwind-v4 CSS-first syntax ---
if [ -n "$files" ]; then
  hits=$(grep -nE '@custom-variant[[:space:]]+dark|@plugin[[:space:]]+["'\'']flowbite|@import[[:space:]]+["'\'']tailwindcss|@theme[[:space:]]*\{' $files || true)
  if [ -n "$hits" ]; then
    echo "DOCTRINE VIOLATION (flowbite-stack): Tailwind v4 / Flowbite v4 syntax v zdroji."
    echo "Projekt je Flowbite v2 / Tailwind v3 — viz .aiad/policies/flowbite-stack.policy.md"
    echo "$hits"
    fail=1
  fi
fi

# --- advisory: major verze v package.json ---
if grep -qE '"flowbite":[[:space:]]*"[~^]?[34]\.|"tailwindcss":[[:space:]]*"[~^]?4\.' package.json 2>/dev/null; then
  echo "::warning::package.json má flowbite ^3/^4 nebo tailwindcss ^4 (v4 = breaking). Aktualizuj .aiad/policies/flowbite-stack.policy.md."
fi

if [ "$fail" -ne 0 ]; then
  echo "doctrines: FAILED"
  exit 1
fi
echo "doctrines: OK (Flowbite v2 / Tailwind v3)"
