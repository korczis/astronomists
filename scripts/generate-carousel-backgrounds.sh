#!/usr/bin/env bash
# Full-bleed web background varianty kampaňových posterů pro Flowbite carousel.
# Zdroj: assets/campaign-posters/astronautiste-*.jpg → static/backgrounds/carousel/<name>.jpg
# Ořez řeší object-cover v šabloně; tady jen resize (max 1600px) + strip + optimalizace. Idempotentní.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/assets/campaign-posters"
OUT="$ROOT/static/backgrounds/carousel"
MAXW=1600
Q=80

mkdir -p "$OUT"
n=0
for f in "$SRC"/astronautiste-*.jpg; do
  [ -e "$f" ] || continue
  magick "$f" -resize "${MAXW}x${MAXW}>" -strip -quality "$Q" "$OUT/$(basename "$f")"
  n=$((n+1))
done
echo "→ $n background variant → static/backgrounds/carousel/ ($(du -sh "$OUT" | cut -f1))"
