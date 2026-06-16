#!/usr/bin/env bash
# Generuje social/OG preview obrázky z kampaňových posterů.
# Astronautisté → static/og/social/ (publikuje se).
# Contain-fit na Void Black (#0a0a0a) → celý poster viditelný, branded pozadí. Idempotentní.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC_AST="$ROOT/assets/campaign-posters"
SRC_AST_GEN="$SRC_AST/generated-20260616"

OUT_AST="$ROOT/static/og/social"
OUT_AST_THUMB="$OUT_AST/thumbs"
OUT_AST_GEN="$OUT_AST/generated-20260616"
OUT_AST_GEN_THUMB="$OUT_AST_THUMB/generated-20260616"

BG="#0a0a0a"        # Void Black (design token)
OG_W=1200; OG_H=630 # Open Graph / Twitter summary_large_image
THUMB_W=600         # gallery náhled
Q=88

mkdir -p "$OUT_AST" "$OUT_AST_THUMB" "$OUT_AST_GEN" "$OUT_AST_GEN_THUMB"

og() {  # <src> <dst>
  magick "$1" -resize "${OG_W}x${OG_H}" -background "$BG" -gravity center \
    -extent "${OG_W}x${OG_H}" -quality "$Q" -strip "$2"
}
thumb() {  # <src> <dst>
  magick "$1" -resize "${THUMB_W}x" -quality "$Q" -strip "$2"
}

echo "→ Astronautisté OG (${OG_W}x${OG_H}) + thumbs → static/og/social/"
n=0
for f in "$SRC_AST"/astronautiste-*.jpg; do
  [ -e "$f" ] || continue
  base="$(basename "$f" .jpg)"
  og    "$f" "$OUT_AST/$base.jpg"
  thumb "$f" "$OUT_AST_THUMB/$base.jpg"
  n=$((n+1))
done
echo "  $n posterů"

echo "→ Astronautisté generated OG (${OG_W}x${OG_H}) + thumbs → static/og/social/generated-20260616/"
g=0
for f in "$SRC_AST_GEN"/astronautiste-*.png; do
  [ -e "$f" ] || continue
  base="$(basename "$f" .png)"
  og    "$f" "$OUT_AST_GEN/$base.jpg"
  thumb "$f" "$OUT_AST_GEN_THUMB/$base.jpg"
  g=$((g+1))
done
echo "  $g generated obrázků"

echo "→ Default site OG z čistého logo-horizon → static/og/astronautiste-og-hero.jpg"
og "$SRC_AST/astronautiste-logo-horizon-wide.jpg" "$ROOT/static/og/astronautiste-og-hero.jpg"

echo "→ Kontaktní montáž (vizuální index) → static/og/social/_contact-sheet.jpg"
python3 - "$OUT_AST/_contact-sheet.jpg" "$BG" "$OUT_AST_THUMB"/astronautiste-*.jpg "$OUT_AST_GEN_THUMB"/astronautiste-*.jpg <<'PY'
from __future__ import annotations

import math
import sys
from pathlib import Path
from PIL import Image

out = Path(sys.argv[1])
bg = sys.argv[2]
paths = [Path(p) for p in sys.argv[3:] if Path(p).exists()]

cols = 4
cell_w = 300
gap = 6
rows = math.ceil(len(paths) / cols) if paths else 1
sheet_w = cols * cell_w + (cols + 1) * gap
sheet_h = rows * cell_w + (rows + 1) * gap
sheet = Image.new("RGB", (sheet_w, sheet_h), bg)

for idx, path in enumerate(paths):
    img = Image.open(path).convert("RGB")
    img.thumbnail((cell_w, cell_w), Image.Resampling.LANCZOS)
    row, col = divmod(idx, cols)
    x = gap + col * (cell_w + gap) + (cell_w - img.width) // 2
    y = gap + row * (cell_w + gap) + (cell_w - img.height) // 2
    sheet.paste(img, (x, y))

sheet.save(out, quality=88, optimize=True)
print(f"  {len(paths)} nahledu")
PY

echo "Hotovo."
