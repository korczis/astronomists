#!/usr/bin/env python3
"""Generate 25 consistent Astronautiste campaign poster sets.

Outputs per topic:
- clean high-res vertical background: 2400x3600, 300 DPI
- clean high-res wide background: 3840x2160, 300 DPI
- clean social/OG background: 1200x630, 300 DPI
- high-res vertical poster: 2400x3600, 300 DPI
- high-res wide poster: 3840x2160, 300 DPI
- social/OG preview: 1200x630, 300 DPI
"""

from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
BG_SOURCES = [
    ROOT / "assets/campaign-posters/generated-20260616/astronautiste-mission-control-classroom-wide.png",
    ROOT / "assets/campaign-posters/generated-20260616/astronautiste-hill-rocket-trail-wide.png",
    ROOT / "assets/campaign-posters/generated-20260616/astronautiste-generational-stewardship-vertical.png",
    ROOT / "assets/campaign-posters/generated-20260616/astronautiste-observatory-curiosity-vertical.png",
]

OUT_ROOT = ROOT / "assets/campaign-posters/series-25-20260616"
OUT_VERTICAL = OUT_ROOT / "vertical"
OUT_WIDE = OUT_ROOT / "wide-16x9"
OUT_CLEAN_VERTICAL = OUT_ROOT / "clean/vertical"
OUT_CLEAN_WIDE = OUT_ROOT / "clean/wide-16x9"
OUT_SOCIAL = ROOT / "static/og/social/series-25-20260616"
OUT_THUMBS = OUT_SOCIAL / "thumbs"
OUT_CLEAN_SOCIAL = OUT_SOCIAL / "clean"
OUT_CLEAN_THUMBS = OUT_SOCIAL / "thumbs/clean"
OUT_STATIC_CAMPAIGN = ROOT / "static/campaign/series-25-20260616"
OUT_STATIC_CLEAN_VERTICAL = OUT_STATIC_CAMPAIGN / "clean/vertical"
OUT_STATIC_CLEAN_WIDE = OUT_STATIC_CAMPAIGN / "clean/wide-16x9"
OUT_STATIC_RENDERED_VERTICAL = OUT_STATIC_CAMPAIGN / "rendered/vertical"
OUT_STATIC_RENDERED_WIDE = OUT_STATIC_CAMPAIGN / "rendered/wide-16x9"

VOID = "#0a0a0a"
WHITE = "#f8f8f8"
BLUE = "#4aa3df"
SPACE = "#1d3557"
GOLD = "#d4a574"
RED = "#e63946"
GRAY = "#b8c2cf"
MUTED = "#7e8da3"

FONT_HEAD = "/System/Library/Fonts/Supplemental/Arial Narrow Bold.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"


@dataclass(frozen=True)
class Topic:
    slug: str
    headline: str
    subhead: str
    proof: str
    accent: str


TOPICS = [
    Topic("zvedavost-je-start", "Zvědavost je start.", "Každá velká cesta začíná otázkou.", "Podporujeme děti, které se ptají proč.", "ZVĚDAVOST"),
    Topic("kazde-dite-na-orbitu", "Každé dítě na orbitu.", "Jeden pohled na Zemi může změnit celý život.", "Perspektiva není luxus. Je to základ.", "PERSPEKTIVA"),
    Topic("myslet-hvezd", "Myslíme na hvězdy.", "Dívat se dál než za nejbližší horizont.", "Učíme odvaze, která stojí na poznání.", "HORIZONT"),
    Topic("jednat-vedecky", "Jednáme vědecky.", "Nadšení nestačí. Důkaz rozhoduje.", "Pozorovat, ověřit, teprve potom tvrdit.", "DŮKAZ"),
    Topic("jedna-planeta", "Jedna planeta.", "Všichni sdílíme stejný domov i odpovědnost.", "Kosmický pohled vrací věcem měřítko.", "DOMOV"),
    Topic("hranice-konci", "Hranice končí.", "Zvědavost nezná ploty ani mapové čáry.", "Věda spojuje tam, kde svět rozděluje.", "BEZ HRANIC"),
    Topic("budoucnost-je-smer", "Budoucnost je směr.", "Není to místo, kam dorazíme náhodou.", "Volíme ji dnešními rozhodnutími.", "SMĚR"),
    Topic("lekce-ktere-musis-videt", "Některé lekce musíš vidět.", "Zážitek učí rychleji než tisíc slov.", "Pohled z výšky mění vztah k Zemi.", "ZÁŽITEK"),
    Topic("odvaha-ptat-se", "Odvaha ptát se.", "Nejlepší otázky často zní jednoduše.", "Děti potřebují prostor hledat vlastní odpovědi.", "OTÁZKY"),
    Topic("veda-je-dobrodruzstvi", "Věda je dobrodružství.", "Ne útěk od světa, ale cesta k jeho pochopení.", "Objevování začíná tam, kde končí jistota.", "OBJEV"),
    Topic("budujeme-pro-ty-po-nas", "Budujeme pro ty po nás.", "Každé rozhodnutí má svůj zítřek.", "Děti zdědí výsledky naší odvahy i opatrnosti.", "ZÍTŘEK"),
    Topic("velke-sny-potrebuji-oporu", "Velké sny potřebují oporu.", "Talent nestačí, když chybí příležitost.", "Otevíráme cestu dětem bez ohledu na start.", "PŘÍLEŽITOST"),
    Topic("vesmir-neni-luxus", "Vesmír není luxus.", "Je to perspektiva, kterou si zaslouží každý.", "Nejde o útěk vzhůru. Jde o návrat k Zemi.", "PERSPEKTIVA"),
    Topic("zeme-z-vysky", "Země z výšky.", "Malý pohled, velká odpovědnost.", "Kdo vidí celek, rozhoduje méně krátkozrace.", "ODPOVĚDNOST"),
    Topic("ucime-se-divat", "Učíme se dívat.", "Ne rychle soudit, ale přesně pozorovat.", "Pozornost je první nástroj vědy.", "POZOROVÁNÍ"),
    Topic("kazda-otazka-ma-orbitu", "Každá otázka má orbitu.", "Když ji sleduješ dost dlouho, ukáže souvislosti.", "Zvědavost drží myšlení v pohybu.", "SOUVISLOSTI"),
    Topic("mirit-vysoko", "Mířit vysoko.", "Pro všechny. Ne jen pro vyvolené.", "Budoucnost má být otevřená, ne exkluzivní.", "PRO VŠECHNY"),
    Topic("skola-jako-ridici-stredisko", "Škola jako řídicí středisko.", "Třída může být první mise.", "Stačí dát dětem nástroje a důvěru.", "MISE"),
    Topic("dnesni-rozhodnuti", "Dnešní rozhodnutí.", "Jejich zítřek.", "To, co podpoříme dnes, ponese svět zítra.", "ZÍTŘEK"),
    Topic("svetlo-pro-zvedave", "Světlo pro zvídavé.", "Někdy stačí jedna jiskra.", "Dobrá otázka dokáže rozzářit celý směr.", "JISKRA"),
    Topic("poznej-aby-chranil", "Poznej, abys chránil.", "Planetu chráníme líp, když jí rozumíme.", "Vztah k Zemi začíná zkušeností.", "PLANETA"),
    Topic("technologie-s-lidskym-meritkem", "Technologie s lidským měřítkem.", "Stroje jsou nástroje. Směr určují lidé.", "Věda má sloužit dětem, ne naopak.", "MĚŘÍTKO"),
    Topic("spolecny-horizont", "Společný horizont.", "Budoucnost není soutěž jednotlivců.", "Nejlepší mise se staví společně.", "SPOLU"),
    Topic("duvera-v-dukazy", "Důvěra v důkazy.", "Ne v dojmy. Ne v hluk.", "Když děti učíme ověřovat, učíme je svobodě.", "DŮVĚRA"),
    Topic("zacni-otazkou", "Začni otázkou.", "Pak sleduj, kam tě dovede.", "Tak vzniká věda. Tak roste odvaha.", "ZAČÁTEK"),
]


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def slugify(text: str) -> str:
    text = text.lower()
    repl = str.maketrans("áčďéěíňóřšťúůýž", "acdeeinorstuuyz")
    text = text.translate(repl)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def cover(path: Path, size: tuple[int, int], bias_x: float = 0.5, bias_y: float = 0.5) -> Image.Image:
    img = Image.open(path).convert("RGB")
    w, h = img.size
    tw, th = size
    scale = max(tw / w, th / h)
    nw, nh = int(w * scale), int(h * scale)
    img = img.resize((nw, nh), Image.Resampling.LANCZOS)
    left = int((nw - tw) * bias_x)
    top = int((nh - th) * bias_y)
    return img.crop((left, top, left + tw, top + th))


def overlay_gradients(img: Image.Image, layout: str) -> Image.Image:
    w, h = img.size
    base = ImageEnhance.Color(img).enhance(0.82)
    base = ImageEnhance.Contrast(base).enhance(1.08)
    sw = 320
    sh = max(1, round(h * (sw / w)))
    overlay_small = Image.new("RGBA", (sw, sh), (0, 0, 0, 0))
    overlay = Image.new("RGBA", (sw, sh), (0, 0, 0, 0))
    px = overlay.load()
    for y in range(sh):
        for x in range(sw):
            if layout == "vertical":
                left = max(0, 1 - x / (sw * 0.72))
                top = max(0, 1 - y / (sh * 0.58))
                bottom = max(0, (y - sh * 0.70) / (sh * 0.30))
                a = int(min(225, 35 + 170 * max(left, top * 0.75, bottom * 0.8)))
            else:
                left = max(0, 1 - x / (sw * 0.62))
                bottom = max(0, (y - sh * 0.55) / (sh * 0.45))
                a = int(min(220, 25 + 185 * max(left, bottom * 0.55)))
            px[x, y] = (10, 10, 10, a)
    overlay = Image.alpha_composite(overlay_small, overlay).resize((w, h), Image.Resampling.BICUBIC)
    return Image.alpha_composite(base.convert("RGBA"), overlay)


def clean_canvas(bg: Path, size: tuple[int, int], layout: str, bias_x: float, bias_y: float) -> Image.Image:
    return overlay_gradients(cover(bg, size, bias_x, bias_y), layout)


def text_bbox(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int, int, int]:
    return draw.textbbox(xy, text, font=fnt)


def fit_text(draw: ImageDraw.ImageDraw, text: str, max_width: int, font_path: str, start_size: int, min_size: int) -> ImageFont.FreeTypeFont:
    size = start_size
    while size >= min_size:
        fnt = font(font_path, size)
        if text_bbox(draw, (0, 0), text, fnt)[2] <= max_width:
            return fnt
        size -= 4
    return font(font_path, min_size)


def wrap_words(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if text_bbox(draw, (0, 0), candidate, fnt)[2] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_mark(draw: ImageDraw.ImageDraw, x: int, y: int, s: int) -> None:
    draw.polygon([(x + s * 0.50, y), (x + s * 0.88, y + s), (x + s * 0.72, y + s), (x + s * 0.50, y + s * 0.36), (x + s * 0.28, y + s), (x + s * 0.12, y + s)], fill=WHITE)
    draw.line([(x + s * 0.16, y + s * 0.72), (x + s * 0.88, y + s * 0.22)], fill=BLUE, width=max(4, s // 12))
    draw.ellipse((x + s * 0.83, y + s * 0.15, x + s * 0.93, y + s * 0.25), fill=WHITE)


def draw_icon_row(draw: ImageDraw.ImageDraw, x: int, y: int, w: int, scale: int, labels: list[str]) -> None:
    fnt = font(FONT_BOLD, scale)
    small = font(FONT_REG, int(scale * 0.70))
    count = len(labels)
    col_w = w // count
    for i, label in enumerate(labels):
        cx = x + i * col_w + col_w // 2
        cy = y
        if i > 0:
            draw.line((x + i * col_w, y - scale, x + i * col_w, y + scale * 2), fill=(248, 248, 248, 85), width=max(2, scale // 8))
        r = scale // 2
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), outline=BLUE, width=max(2, scale // 8))
        draw.line((cx - r // 2, cy, cx + r // 2, cy), fill=GOLD, width=max(2, scale // 10))
        tw = text_bbox(draw, (0, 0), label, fnt)[2]
        draw.text((cx - tw // 2, y + scale), label, font=fnt, fill=WHITE)
        sub = ["VĚDA", "ODVAHA", "PLANETA", "BUDOUCNOST"][i % 4]
        sw = text_bbox(draw, (0, 0), sub, small)[2]
        draw.text((cx - sw // 2, y + int(scale * 1.85)), sub, font=small, fill=BLUE)


def draw_brand(draw: ImageDraw.ImageDraw, x: int, y: int, scale: int, compact: bool = False) -> None:
    draw_mark(draw, x, y, scale)
    word = font(FONT_BOLD, int(scale * (0.31 if compact else 0.34)))
    tag = font(FONT_REG, int(scale * 0.13))
    tx = x + int(scale * 1.18)
    draw.text((tx, y + int(scale * 0.14)), "ASTRONAUTISTÉ", font=word, fill=WHITE)
    draw.text((tx, y + int(scale * 0.58)), "KAŽDÉ DÍTĚ NA ORBITU.", font=tag, fill=(160, 182, 210))


def draw_vertical(topic: Topic, bg: Path, out: Path, idx: int) -> None:
    size = (2400, 3600)
    img = clean_canvas(bg, size, "vertical", 0.54, 0.48)
    draw = ImageDraw.Draw(img)
    margin = 150
    max_w = 1120

    draw.text((margin, 120), "ASTRONAUTISTÉ", font=font(FONT_BOLD, 58), fill=WHITE)
    draw.line((margin, 205, margin + 520, 205), fill=(74, 163, 223, 190), width=5)
    draw.text((margin, 245), f"{idx:02d} · {topic.accent}", font=font(FONT_BOLD, 42), fill=GOLD)

    head = fit_text(draw, topic.headline.upper(), max_w, FONT_HEAD, 218, 120)
    lines = wrap_words(draw, topic.headline.upper(), head, max_w)
    y = 390
    for line in lines:
        draw.text((margin, y), line, font=head, fill=WHITE)
        y += int(head.size * 0.86)

    sub = font(FONT_BOLD, 70)
    sub_lines = wrap_words(draw, topic.subhead, sub, max_w)
    y += 48
    for line in sub_lines[:3]:
        draw.text((margin, y), line, font=sub, fill=BLUE)
        y += 86

    draw.rounded_rectangle((margin, y + 40, margin + 880, y + 165), radius=0, outline=(248, 248, 248, 170), width=4)
    draw.text((margin + 34, y + 66), "KAŽDÉ DÍTĚ", font=font(FONT_BOLD, 58), fill=WHITE)
    draw.text((margin + 390, y + 66), "NA ORBITU.", font=font(FONT_BOLD, 58), fill=BLUE)

    proof = font(FONT_REG, 48)
    proof_lines = wrap_words(draw, topic.proof, proof, 1120)
    py = y + 235
    draw.line((margin, py - 30, margin + 160, py - 30), fill=RED, width=10)
    for line in proof_lines[:3]:
        draw.text((margin, py), line, font=proof, fill=(230, 236, 244))
        py += 62

    draw_icon_row(draw, margin, 2750, 1400, 44, ["SNY", "VĚDA", "ZEMĚ", "SPOLU"])
    draw_brand(draw, margin, 3230, 180)
    draw.text((margin + 1180, 3360), "astronautiste.cz", font=font(FONT_REG, 44), fill=(190, 205, 222))
    draw.text((margin, 3525), "JEDNA PLANETA.  JEDEN DOMOV.  JEDNA BUDOUCNOST.", font=font(FONT_REG, 34), fill=(132, 151, 176))
    img.convert("RGB").save(out, quality=94, dpi=(300, 300), optimize=True)


def draw_wide(topic: Topic, bg: Path, out: Path, idx: int) -> None:
    size = (3840, 2160)
    img = clean_canvas(bg, size, "wide", 0.62, 0.48)
    draw = ImageDraw.Draw(img)
    margin = 170
    max_w = 1500

    draw.text((margin, 125), "ASTRONAUTISTÉ", font=font(FONT_BOLD, 58), fill=WHITE)
    draw.text((margin, 205), f"{idx:02d} · {topic.accent}", font=font(FONT_BOLD, 40), fill=GOLD)

    head = fit_text(draw, topic.headline.upper(), max_w, FONT_HEAD, 190, 108)
    y = 360
    for line in wrap_words(draw, topic.headline.upper(), head, max_w)[:3]:
        draw.text((margin, y), line, font=head, fill=WHITE)
        y += int(head.size * 0.88)

    sub = font(FONT_BOLD, 68)
    y += 42
    for line in wrap_words(draw, topic.subhead, sub, max_w)[:3]:
        draw.text((margin, y), line, font=sub, fill=BLUE)
        y += 82

    proof = font(FONT_REG, 44)
    y += 40
    draw.line((margin, y - 25, margin + 140, y - 25), fill=RED, width=9)
    for line in wrap_words(draw, topic.proof, proof, 1220)[:3]:
        draw.text((margin, y), line, font=proof, fill=(228, 235, 244))
        y += 58

    draw_brand(draw, margin, 1810, 150, compact=True)
    draw.rounded_rectangle((margin + 1220, 1830, margin + 1950, 1935), radius=0, outline=(248, 248, 248, 150), width=4)
    draw.text((margin + 1260, 1852), "KAŽDÉ DÍTĚ NA ORBITU.", font=font(FONT_BOLD, 44), fill=WHITE)
    draw.text((margin + 2200, 1870), "astronautiste.cz", font=font(FONT_REG, 40), fill=(190, 205, 222))
    img.convert("RGB").save(out, quality=94, dpi=(300, 300), optimize=True)


def draw_social(topic: Topic, bg: Path, out: Path, idx: int) -> None:
    size = (1200, 630)
    img = clean_canvas(bg, size, "wide", 0.62, 0.48)
    draw = ImageDraw.Draw(img)
    margin = 54
    max_w = 540

    draw.text((margin, 42), "ASTRONAUTISTÉ", font=font(FONT_BOLD, 23), fill=WHITE)
    draw.text((margin, 76), f"{idx:02d} · {topic.accent}", font=font(FONT_BOLD, 17), fill=GOLD)

    head = fit_text(draw, topic.headline.upper(), max_w, FONT_HEAD, 66, 42)
    y = 128
    for line in wrap_words(draw, topic.headline.upper(), head, max_w)[:3]:
        draw.text((margin, y), line, font=head, fill=WHITE)
        y += int(head.size * 0.88)

    sub = font(FONT_BOLD, 25)
    y += 16
    for line in wrap_words(draw, topic.subhead, sub, max_w)[:2]:
        draw.text((margin, y), line, font=sub, fill=BLUE)
        y += 32

    draw.line((margin, 486, margin + 72, 486), fill=RED, width=5)
    draw.text((margin, 508), "KAŽDÉ DÍTĚ NA ORBITU.", font=font(FONT_BOLD, 27), fill=WHITE)
    draw.text((margin, 550), "astronautiste.cz", font=font(FONT_REG, 20), fill=(196, 210, 228))
    draw_mark(draw, 975, 485, 90)
    img.convert("RGB").save(out, quality=90, dpi=(300, 300), optimize=True)


def make_contact_sheet(paths: list[Path], out: Path, cell: int = 260, cols: int = 5) -> None:
    rows = math.ceil(len(paths) / cols)
    gap = 8
    sheet = Image.new("RGB", (cols * cell + (cols + 1) * gap, rows * cell + (rows + 1) * gap), VOID)
    for i, path in enumerate(paths):
        img = Image.open(path).convert("RGB")
        img.thumbnail((cell, cell), Image.Resampling.LANCZOS)
        row, col = divmod(i, cols)
        x = gap + col * (cell + gap) + (cell - img.width) // 2
        y = gap + row * (cell + gap) + (cell - img.height) // 2
        sheet.paste(img, (x, y))
    sheet.save(out, quality=88, optimize=True)


def main() -> None:
    for path in [
        OUT_VERTICAL, OUT_WIDE, OUT_CLEAN_VERTICAL, OUT_CLEAN_WIDE,
        OUT_SOCIAL, OUT_THUMBS, OUT_CLEAN_SOCIAL, OUT_CLEAN_THUMBS,
        OUT_STATIC_CLEAN_VERTICAL, OUT_STATIC_CLEAN_WIDE,
        OUT_STATIC_RENDERED_VERTICAL, OUT_STATIC_RENDERED_WIDE,
    ]:
        path.mkdir(parents=True, exist_ok=True)

    rows = ["# Astronautiste Series 25 — generated outputs", ""]
    rows.append("| # | Topic | Clean vertical | Clean wide | Clean social | Rendered vertical | Rendered wide | Rendered social |")
    rows.append("|---:|---|---|---|---|---|---|---|")

    social_paths: list[Path] = []
    clean_social_paths: list[Path] = []
    manifest = {
        "version": "20260616",
        "brand": "Astronautiste",
        "formats": {
            "clean_vertical": {"size": [2400, 3600], "dpi": 300},
            "clean_wide_16x9": {"size": [3840, 2160], "dpi": 300},
            "clean_social": {"size": [1200, 630], "dpi": 300},
            "rendered_vertical": {"size": [2400, 3600], "dpi": 300},
            "rendered_wide_16x9": {"size": [3840, 2160], "dpi": 300},
            "rendered_social": {"size": [1200, 630], "dpi": 300},
        },
        "css_tokens": {
            "void": VOID,
            "presence": WHITE,
            "space": SPACE,
            "gold": GOLD,
            "signal": RED,
            "blue": BLUE,
            "font_family": "Inter, Arial, Helvetica, sans-serif",
        },
        "topics": [],
    }
    for idx, topic in enumerate(TOPICS, start=1):
        bg = BG_SOURCES[(idx - 1) % len(BG_SOURCES)]
        slug = f"{idx:02d}-{topic.slug or slugify(topic.headline)}"
        clean_vertical = OUT_CLEAN_VERTICAL / f"astronautiste-{slug}-clean-vertical.jpg"
        clean_wide = OUT_CLEAN_WIDE / f"astronautiste-{slug}-clean-wide-16x9.jpg"
        clean_social = OUT_CLEAN_SOCIAL / f"astronautiste-{slug}-clean-social.jpg"
        clean_thumb = OUT_CLEAN_THUMBS / f"astronautiste-{slug}-clean-thumb.jpg"
        vertical = OUT_VERTICAL / f"astronautiste-{slug}-vertical.jpg"
        wide = OUT_WIDE / f"astronautiste-{slug}-wide-16x9.jpg"
        social = OUT_SOCIAL / f"astronautiste-{slug}-social.jpg"
        thumb = OUT_THUMBS / f"astronautiste-{slug}-thumb.jpg"
        static_clean_vertical = OUT_STATIC_CLEAN_VERTICAL / clean_vertical.name
        static_clean_wide = OUT_STATIC_CLEAN_WIDE / clean_wide.name
        static_rendered_vertical = OUT_STATIC_RENDERED_VERTICAL / vertical.name
        static_rendered_wide = OUT_STATIC_RENDERED_WIDE / wide.name

        clean_v = clean_canvas(bg, (2400, 3600), "vertical", 0.54, 0.48).convert("RGB")
        clean_w = clean_canvas(bg, (3840, 2160), "wide", 0.62, 0.48).convert("RGB")
        clean_v.save(clean_vertical, quality=94, dpi=(300, 300), optimize=True)
        clean_w.save(clean_wide, quality=94, dpi=(300, 300), optimize=True)
        clean_v.save(static_clean_vertical, quality=88, dpi=(300, 300), optimize=True)
        clean_w.save(static_clean_wide, quality=88, dpi=(300, 300), optimize=True)
        clean_canvas(bg, (1200, 630), "wide", 0.62, 0.48).convert("RGB").save(clean_social, quality=90, dpi=(300, 300), optimize=True)
        draw_vertical(topic, bg, vertical, idx)
        draw_wide(topic, bg, wide, idx)
        draw_social(topic, bg, social, idx)
        Image.open(vertical).convert("RGB").save(static_rendered_vertical, quality=88, dpi=(300, 300), optimize=True)
        Image.open(wide).convert("RGB").save(static_rendered_wide, quality=88, dpi=(300, 300), optimize=True)

        t = Image.open(social).convert("RGB")
        t.thumbnail((600, 315), Image.Resampling.LANCZOS)
        t.save(thumb, quality=88, dpi=(144, 144), optimize=True)
        ct = Image.open(clean_social).convert("RGB")
        ct.thumbnail((600, 315), Image.Resampling.LANCZOS)
        ct.save(clean_thumb, quality=88, dpi=(144, 144), optimize=True)
        social_paths.append(social)
        clean_social_paths.append(clean_social)
        rows.append(
            f"| {idx} | {topic.headline} | `{clean_vertical.relative_to(OUT_ROOT)}` | "
            f"`{clean_wide.relative_to(OUT_ROOT)}` | `{clean_social.relative_to(OUT_SOCIAL)}` | "
            f"`{vertical.name}` | `{wide.name}` | `{social.name}` |"
        )
        manifest["topics"].append({
            "index": idx,
            "slug": topic.slug,
            "headline": topic.headline,
            "subhead": topic.subhead,
            "proof": topic.proof,
            "accent": topic.accent,
            "background_source": str(bg.relative_to(ROOT)),
            "assets": {
                "clean_vertical": str(clean_vertical.relative_to(ROOT)),
                "clean_wide_16x9": str(clean_wide.relative_to(ROOT)),
                "clean_social": str(clean_social.relative_to(ROOT)),
                "rendered_vertical": str(vertical.relative_to(ROOT)),
                "rendered_wide_16x9": str(wide.relative_to(ROOT)),
                "rendered_social": str(social.relative_to(ROOT)),
                "rendered_thumb": str(thumb.relative_to(ROOT)),
                "clean_thumb": str(clean_thumb.relative_to(ROOT)),
            },
            "urls": {
                "clean_vertical": "/" + str(static_clean_vertical.relative_to(ROOT / "static")),
                "clean_wide_16x9": "/" + str(static_clean_wide.relative_to(ROOT / "static")),
                "clean_social": "/" + str(clean_social.relative_to(ROOT / "static")),
                "rendered_vertical": "/" + str(static_rendered_vertical.relative_to(ROOT / "static")),
                "rendered_wide_16x9": "/" + str(static_rendered_wide.relative_to(ROOT / "static")),
                "rendered_social": "/" + str(social.relative_to(ROOT / "static")),
                "rendered_thumb": "/" + str(thumb.relative_to(ROOT / "static")),
                "clean_thumb": "/" + str(clean_thumb.relative_to(ROOT / "static")),
            },
        })

    make_contact_sheet(social_paths, OUT_SOCIAL / "_contact-sheet.jpg")
    make_contact_sheet(clean_social_paths, OUT_SOCIAL / "_contact-sheet-clean.jpg")
    (OUT_ROOT / "README.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    (OUT_ROOT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT_SOCIAL / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT_STATIC_CAMPAIGN / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Generated {len(TOPICS)} topics")
    print(f"Clean vertical: {OUT_CLEAN_VERTICAL}")
    print(f"Clean wide: {OUT_CLEAN_WIDE}")
    print(f"Clean social: {OUT_CLEAN_SOCIAL}")
    print(f"Rendered vertical: {OUT_VERTICAL}")
    print(f"Rendered wide: {OUT_WIDE}")
    print(f"Rendered social: {OUT_SOCIAL}")
    print(f"Static campaign: {OUT_STATIC_CAMPAIGN}")


if __name__ == "__main__":
    main()
