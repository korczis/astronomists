#!/usr/bin/env python3
"""generate-og.py — unique 1200x630 OG/social preview per page.

🇨🇿 Vygeneruje brandovaný OG obrázek pro každou stránku webu: tmavé cosmic pozadí
    (volitelně namapovaný poster z static/og/social), gold dot + wordmark, eyebrow,
    title (zalomený) a tagline. Idempotentní → output do static/og/pages/<slug>.png.

Render: SVG → PNG přes rsvg-convert (Helvetica/Arial, plná česká diakritika).
"""
import html
import os
import random
import subprocess
import sys
import textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC = os.path.join(ROOT, "static")
OUT = os.path.join(STATIC, "og", "pages")
OUT_CARDS = os.path.join(STATIC, "og", "cards")
SOCIAL = "/og/social"  # web path under static

W, H = 1200, 630          # OG / social preview (with text)
CW, CH = 1280, 800        # on-site card art (16:10, TEXT-FREE — HTML overlays the title)
SANS = "Helvetica Neue, Helvetica, Arial, sans-serif"
SERIF = "Georgia, Times New Roman, serif"

# Per-slug accent (meta-narrative / section): blue=WITNESS, red=SIGNAL, gold=CONTINUITY/default.
BLUE, GOLD, RED = "#1d3557", "#d4a574", "#e63946"
ACCENT = {
    "motivy-pale-blue-dot": BLUE, "motivy-prvni-pohled": BLUE, "motivy-sagan": BLUE,
    "motivy-hranice": RED, "motivy-nejnebezpecnejsi-poster": RED,
    "proc-perspektiva": BLUE, "proc-zvidavost": GOLD, "proc-budoucnost": RED,
    "proc": BLUE, "motivy": BLUE,
    "pridej-se": RED, "pridej-se-skolni-vylet-orbit": RED, "pridej-se-vesmir-detske-pravo": RED,
    "pridej-se-kazde-dite-vidi-zemi": RED, "pridej-se-vetsi-budoucnost": RED,
}

# Full-bleed, genuinely text-free source photos (asset originals, NOT the letterboxed
# social JPGs) usable as card backgrounds. Cover-cropped to 16:10.
_GEN = os.path.join(ROOT, "assets", "campaign-posters", "generated-20260616")
CARD_PHOTO = {
    "motivy-prvni-pohled": os.path.join(_GEN, "astronautiste-observatory-curiosity-vertical.png"),
    "motivy-matka": os.path.join(_GEN, "astronautiste-generational-stewardship-vertical.png"),
    "motivy-evoluce": os.path.join(_GEN, "astronautiste-hill-rocket-trail-wide.png"),
    "motivy-skolni-vylet": os.path.join(_GEN, "astronautiste-mission-control-classroom-wide.png"),
    "pro-koho-ucitele": os.path.join(_GEN, "astronautiste-mission-control-classroom-wide.png"),
    "pridej-se-skolni-vylet-orbit": os.path.join(_GEN, "astronautiste-mission-control-classroom-wide.png"),
    "pridej-se-kazde-dite-vidi-zemi": os.path.join(_GEN, "astronautiste-hill-rocket-trail-wide.png"),
    "pro-koho-rodice": os.path.join(_GEN, "astronautiste-generational-stewardship-vertical.png"),
}

# slug → (eyebrow, title, background image web-path under static or "")
PAGES = [
    # ---- hubs ----
    ("proc", "Tři pilíře perspektivy", "Proč Astronautisté", f"{SOCIAL}/astronautiste-jedna-planeta-mnoho-generaci-wide.jpg"),
    ("manifest", "Manifest v jedné větě", "Manifest", f"{SOCIAL}/astronautiste-budoucnost-neni-misto-je-to-smer.jpg"),
    ("pro-koho", "Pro koho", "Pro koho", f"{SOCIAL}/astronautiste-deti-dnes-objevitele-zitra.jpg"),
    ("motivy", "Vizuální mytologie", "Motivy", f"{SOCIAL}/astronautiste-logo-horizon-wide.jpg"),
    ("pridej-se", "Program hnutí", "Přidej se", f"{SOCIAL}/astronautiste-kazde-dite-na-orbitu-nase-nejvetsi-investice-wide.jpg"),
    ("brand", "Brand & Design System", "Brand & Design System", f"{SOCIAL}/astronautiste-vzhuru-za-poznanim.jpg"),
    ("docs", "Brand package", "Dokumentace", f"{SOCIAL}/astronautiste-logo-horizon-wide.jpg"),
    ("home", "Hnutí za větší horizont", "Dětem patří hvězdy. Každé dítě na orbitu.", f"{SOCIAL}/astronautiste-kazde-dite-na-orbitu-nase-nejvetsi-investice-wide.jpg"),
    # ---- motifs ----
    ("motivy-pale-blue-dot", "Motiv 01 · Witness", "Pale Blue Dot", f"{SOCIAL}/astronautiste-jedna-planeta-mnoho-generaci-wide.jpg"),
    ("motivy-prvni-pohled", "Motiv 02 · Witness", "První pohled", f"{SOCIAL}/generated-20260616/astronautiste-observatory-curiosity-vertical.jpg"),
    ("motivy-hranice", "Motiv 03 · Signal", "Hranice", f"{SOCIAL}/astronautiste-hranice-konci-zvedavost-ne.jpg"),
    ("motivy-evoluce", "Motiv 04 · Continuity", "Evoluce", f"{SOCIAL}/astronautiste-rocket-trail-mirime-vysoko.jpg"),
    ("motivy-generace-2100", "Motiv 05 · Continuity", "Generace 2100", f"{SOCIAL}/astronautiste-deti-dnes-objevitele-zitra.jpg"),
    ("motivy-skolni-vylet", "Motiv 06 · Continuity", "Školní výlet", f"{SOCIAL}/generated-20260616/astronautiste-mission-control-classroom-wide.jpg"),
    ("motivy-sagan", "Motiv 07 · Witness", "Carl Sagan vibe", f"{SOCIAL}/astronautiste-zvedavost-je-jiskra-galaxy-jar.jpg"),
    ("motivy-matka", "Motiv 08 · Continuity", "Matka", f"{SOCIAL}/generated-20260616/astronautiste-generational-stewardship-vertical.jpg"),
    ("motivy-ceska-republika-2075", "Motiv 09 · Continuity", "Česká republika 2075", f"{SOCIAL}/astronautiste-vzhuru-za-poznanim.jpg"),
    ("motivy-nejnebezpecnejsi-poster", "Motiv 10 · Signal", "Nejnebezpečnější poster", f"{SOCIAL}/astronautiste-nektere-lekce-se-nedaji-naucit.jpg"),
    # ---- pillars (proc) ----
    ("proc-perspektiva", "Pilíř 01", "Perspektiva", f"{SOCIAL}/astronautiste-jedna-planeta-mnoho-generaci-wide.jpg"),
    ("proc-zvidavost", "Pilíř 02", "Zvídavost", f"{SOCIAL}/astronautiste-zvedavost-je-palivo-vzdelani-je-sila.jpg"),
    ("proc-budoucnost", "Pilíř 03", "Budoucnost", f"{SOCIAL}/astronautiste-budoucnost-neni-misto-je-to-smer.jpg"),
    # ---- audiences (pro-koho) ----
    ("pro-koho-rodice", "Pro koho", "Rodiče & mámy", f"{SOCIAL}/astronautiste-deti-dnes-objevitele-zitra.jpg"),
    ("pro-koho-ucitele", "Pro koho", "Učitelé", f"{SOCIAL}/generated-20260616/astronautiste-mission-control-classroom-wide.jpg"),
    ("pro-koho-studenti", "Pro koho", "Studenti", f"{SOCIAL}/astronautiste-zvedavost-otevira-dvere.jpg"),
    ("pro-koho-vedci", "Pro koho", "Vědci & technici", f"{SOCIAL}/astronautiste-objevujeme-dnesek-inspirujeme-zitky.jpg"),
    # ---- manifest slogans ----
    ("manifest-detem-patri-hvezdy", "Manifest", "Dětem patří hvězdy", f"{SOCIAL}/astronautiste-jedna-planeta-mnoho-generaci-wide.jpg"),
    ("manifest-vesmir-neni-luxus", "Manifest", "Vesmír není luxus. Vesmír je perspektiva.", f"{SOCIAL}/astronautiste-logo-horizon-wide.jpg"),
    ("manifest-kazde-dite-na-orbitu", "Manifest", "Každé dítě na orbitu", f"{SOCIAL}/astronautiste-kazde-dite-na-orbitu-square.jpg"),
    ("manifest-budoucnost-nezacina-u-urny", "Manifest", "Budoucnost nezačíná u volební urny.", f"{SOCIAL}/astronautiste-budoucnost-neni-misto-je-to-smer.jpg"),
    ("manifest-deti-potrebuji-horizont", "Manifest", "Děti potřebují větší horizont.", f"{SOCIAL}/astronautiste-deti-dnes-objevitele-zitra.jpg"),
    ("manifest-exkurze-za-atmosferu", "Manifest", "Exkurze za atmosféru.", f"{SOCIAL}/astronautiste-rocket-trail-mirime-vysoko.jpg"),
    ("manifest-sokoli-astronauti", "Manifest", "Měli jsme sokoly. Budeme mít astronauty.", f"{SOCIAL}/astronautiste-vzhuru-za-poznanim.jpg"),
    ("manifest-ne-vetsi-stat", "Manifest", "Ne větší stát. Větší budoucnost.", f"{SOCIAL}/astronautiste-kazde-dite-na-orbitu-nase-nejvetsi-investice-wide.jpg"),
    # ---- program (pridej-se) ----
    ("pridej-se-skolni-vylet-orbit", "Program · 01", "Školní výlet na orbitální stanici", f"{SOCIAL}/generated-20260616/astronautiste-mission-control-classroom-wide.jpg"),
    ("pridej-se-vesmir-detske-pravo", "Program · 02", "Vesmír jako základní dětské právo", f"{SOCIAL}/astronautiste-kazde-dite-na-orbitu-nase-nejvetsi-investice-wide.jpg"),
    ("pridej-se-kazde-dite-vidi-zemi", "Program · 03", "Každé dítě aspoň jednou vidí Zemi z výšky", f"{SOCIAL}/astronautiste-jedna-planeta-mnoho-generaci-wide.jpg"),
    ("pridej-se-vetsi-budoucnost", "Program · 04", "Ne větší stát. Větší budoucnost.", f"{SOCIAL}/astronautiste-budoucnost-neni-misto-je-to-smer.jpg"),
]


def esc(s):
    return html.escape(s, quote=True)


def wrap_title(title):
    # Choose width + font-size by length so it always fits the 1040px text column.
    n = len(title)
    if n <= 16:
        size, width, lh = 84, 16, 92
    elif n <= 28:
        size, width, lh = 68, 18, 78
    elif n <= 44:
        size, width, lh = 54, 24, 64
    else:
        size, width, lh = 44, 30, 54
    lines = textwrap.wrap(title, width=width) or [title]
    lines = lines[:3]
    return lines, size, lh


def build_svg(eyebrow, title, bg):
    lines, size, lh = wrap_title(title)
    # Title block bottom-anchored above the tagline.
    block_h = len(lines) * lh
    title_top = 470 - block_h
    tspans = ""
    for i, ln in enumerate(lines):
        y = title_top + (i + 1) * lh - 12
        tspans += f'<text x="80" y="{y}" font-family="{SANS}" font-size="{size}" font-weight="800" fill="#f8f8f8" letter-spacing="-1">{esc(ln)}</text>'

    # Background poster (composited in main() via ImageMagick, when present).
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <radialGradient id="cosmic" cx="78%" cy="-8%" r="90%">
      <stop offset="0%" stop-color="#1d3557" stop-opacity="0.55"/>
      <stop offset="60%" stop-color="#0a0a0a" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="legib" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#0a0a0a" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#0a0a0a" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="#0a0a0a" opacity="{0 if bg else 1}"/>
  <rect width="{W}" height="{H}" fill="#0a0a0a" opacity="{0.5 if bg else 0}"/>
  <rect width="880" height="{H}" fill="url(#legib)"/>
  <rect width="{W}" height="{H}" fill="url(#cosmic)"/>
  <!-- wordmark -->
  <circle cx="88" cy="86" r="9" fill="#d4a574"/>
  <circle cx="88" cy="86" r="18" fill="#d4a574" opacity="0.18"/>
  <text x="112" y="94" font-family="{SANS}" font-size="26" font-weight="700" fill="#f8f8f8" letter-spacing="2">ASTRONAUTISTÉ</text>
  <!-- eyebrow -->
  <text x="80" y="{470 - len(wrap_title(title)[0]) * wrap_title(title)[2] - 26}" font-family="{SANS}" font-size="26" font-weight="700" fill="#d4a574" letter-spacing="3">{esc(eyebrow.upper())}</text>
  <!-- title -->
  {tspans}
  <!-- signal rule -->
  <rect x="80" y="498" width="64" height="5" rx="2.5" fill="#e63946"/>
  <!-- tagline -->
  <text x="80" y="560" font-family="{SERIF}" font-size="30" font-style="italic" fill="#d4a574">Každé dítě na orbitu.</text>
  <text x="{W - 80}" y="560" text-anchor="end" font-family="{SANS}" font-size="22" font-weight="600" fill="#e8e8e8" opacity="0.8">astronautiste.cz</text>
</svg>'''


def build_card_svg(slug, bg):
    """Text-free 16:10 card art: cosmic gradient + sparse star field + accent glow.
    Title/eyebrow are overlaid in HTML/CSS on the page — never baked in here."""
    accent = ACCENT.get(slug, GOLD)
    rnd = random.Random(slug)  # deterministic per slug → stable output, varied per page
    stars = ""
    for _ in range(90):
        x, y = rnd.uniform(0, CW), rnd.uniform(0, CH)
        r = rnd.uniform(0.5, 2.0)
        op = rnd.uniform(0.15, 0.85)
        col = GOLD if rnd.random() < 0.12 else "#f8f8f8"
        stars += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{col}" opacity="{op:.2f}"/>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{CW}" height="{CH}" viewBox="0 0 {CW} {CH}">
  <defs>
    <radialGradient id="g" cx="75%" cy="-10%" r="110%">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0.55"/>
      <stop offset="55%" stop-color="#0a0a0a" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="g2" cx="10%" cy="115%" r="80%">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0.22"/>
      <stop offset="60%" stop-color="#0a0a0a" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="{CW}" height="{CH}" fill="#0a0a0a" opacity="{0 if bg else 1}"/>
  <rect width="{CW}" height="{CH}" fill="#0a0a0a" opacity="{0.42 if bg else 0}"/>
  {"" if bg else stars}
  <rect width="{CW}" height="{CH}" fill="url(#g)"/>
  <rect width="{CW}" height="{CH}" fill="url(#g2)"/>
</svg>'''


def render(svg, png_path, w, h, bg):
    """Render SVG overlay; composite over cover-cropped poster if bg present."""
    svg_path = png_path + ".svg"
    overlay = png_path + ".overlay.png"
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    subprocess.run(["rsvg-convert", "-w", str(w), "-h", str(h), svg_path, "-o", overlay], check=True)
    if bg:
        bg_abs = bg if os.path.isabs(bg) else os.path.join(STATIC, bg.lstrip("/"))
    else:
        bg_abs = ""
    if bg_abs and os.path.exists(bg_abs):
        subprocess.run([
            "magick", bg_abs, "-resize", f"{w}x{h}^", "-gravity", "center", "-extent", f"{w}x{h}",
            overlay, "-composite", png_path,
        ], check=True)
        os.remove(overlay)
    else:
        if bg:
            print(f"  WARN missing bg: {bg_abs}", file=sys.stderr)
        os.replace(overlay, png_path)
    os.remove(svg_path)


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(OUT_CARDS, exist_ok=True)
    only = set(a for a in sys.argv[1:] if not a.startswith("-"))
    cards_only = "--cards" in sys.argv
    og_only = "--og" in sys.argv
    count = 0
    for slug, eyebrow, title, bg in PAGES:
        if only and slug not in only:
            continue
        if not cards_only:  # OG social previews (with text) → /og/pages
            render(build_svg(eyebrow, title, bg), os.path.join(OUT, slug + ".png"), W, H, bg)
        if not og_only:     # text-free on-site card art (16:10) → /og/cards
            # Card backgrounds use ONLY full-bleed text-free asset photos; every other
            # page gets pure cosmic art (the social posters have baked-in text).
            card_bg = CARD_PHOTO.get(slug, "")
            render(build_card_svg(slug, card_bg), os.path.join(OUT_CARDS, slug + ".png"), CW, CH, card_bg)
        count += 1
        print(f"  ok  {slug}")
    print(f"✅ generated {count} pages → og/pages + og/cards")


if __name__ == "__main__":
    main()
