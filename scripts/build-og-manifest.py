#!/usr/bin/env python3
"""Sestaví data/og-previews.toml z reálných souborů ve static/og/social/.

Stránka /docs/social-kit/ čte tento manifest přes Zola `load_data`, takže
dokumentace se nikdy nerozejde s realitou na disku. Idempotentní.

Spusť po `scripts/generate-og-previews.sh`:
    python3 scripts/build-og-manifest.py
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOCIAL = ROOT / "static" / "og" / "social"
GEN_SUB = "generated-20260616"
OUT = ROOT / "data" / "og-previews.toml"

# slug -> (CZ titulek, brand status [ok|warn|error], aspect, poznámka)
META = {
    # bez chyb
    "astronautiste-dnesni-rozhodnuti-jeho-zitrek-story": ("Dnešní rozhodnutí. Jeho zítřek.", "ok", "story", "Matka a syn, ISS za oknem."),
    "astronautiste-logo-horizon-wide": ("Logo nad horizontem Země", "ok", "wide", "Čistý logotyp — vhodné jako default OG."),
    # vypálený překlep v názvu/copy
    "astronautiste-zvedavost-je-jiskra-reading": ("Zvědavost je jiskra (čtení)", "warn", "portrait", "V obrázku AUSTRONAUTISTÉ + ZVÍDAVOST."),
    "astronautiste-zvedavost-je-jiskra-galaxy-jar": ("Zvědavost je jiskra (galaxie ve sklenici)", "warn", "portrait", "V obrázku AUSTRONAUTISTÉ."),
    "astronautiste-zvedavost-otevira-dvere": ("Zvědavost otevírá dveře", "warn", "portrait", "V obrázku AUSTRONAUTISTÉ."),
    "astronautiste-zvedavost-je-palivo-vzdelani-je-sila": ("Zvědavost je palivo. Vzdělání je síla.", "warn", "portrait", "V obrázku AUSTRONAUTISTÉ."),
    "astronautiste-deti-dnes-objevitele-zitra": ("Děti dnes. Objevitelé zítra.", "warn", "portrait", "V obrázku AUSTRONAUTISTÉ + SKLÍDĚME."),
    "astronautiste-budoucnost-neni-misto-je-to-smer": ("Budoucnost není místo. Je to směr.", "warn", "portrait", "V obrázku AUSTRONAUTISTÉ."),
    "astronautiste-nektere-lekce-se-nedaji-naucit": ("Některé lekce se nedají naučit. Musíš je vidět.", "warn", "portrait", "V obrázku AUSTRONAUTISTÉ."),
    "astronautiste-jedna-planeta-mnoho-generaci-wide": ("Jedna planeta. Mnoho generací.", "warn", "wide", "V obrázku AUSTRONAUTISTÉ."),
    "astronautiste-vzhuru-za-poznanim": ("Vzhůru za poznáním. Za budoucností. Za dětmi.", "warn", "portrait", "V obrázku AUSTRONAUTISTÉ."),
    "astronautiste-hranice-konci-zvedavost-ne": ("Hranice končí. Zvědavost ne.", "warn", "portrait", "V obrázku AUSTRONAUTISTÉ."),
    "astronautiste-objevujeme-dnesek-inspirujeme-zitky": ("Objevujeme dnešek. Inspirujeme zítřky.", "warn", "portrait", "V obrázku AUSTRONAUTISTÉ + ZÍTKY."),
    "astronautiste-kazde-dite-na-orbitu-nase-nejvetsi-investice-wide": ("Každé dítě na orbitu (Einstein)", "warn", "wide", "V obrázku AUSTRONAUTISTÉ."),
    "astronautiste-kazde-dite-na-orbitu-square": ("Každé dítě na orbitu (typografický)", "warn", "square", "V obrázku austronautiste.cz."),
    # hrubý překlep
    "astronautiste-kazde-dite-na-orbitu-program-story": ("Každé dítě na orbitu — program", "error", "story", "V obrázku AUSTRANISTÉ."),
    "astronautiste-rocket-trail-mirime-vysoko": ("Míříme vysoko. Pro všechny.", "warn", "portrait", "V obrázku AUSTRONAUTISTÉ."),
    # beztextové generated assety (brand-safe)
    "astronautiste-mission-control-classroom-wide": ("Mission control / třída", "ok", "wide", "Beztextové; left safe area pro overlay."),
    "astronautiste-hill-rocket-trail-wide": ("Raketová stopa nad kopcem", "ok", "wide", "Beztextové; sky safe area."),
    "astronautiste-observatory-curiosity-vertical": ("Observatoř — zvědavost", "ok", "vertical", "Beztextové; vertikální pozadí."),
    "astronautiste-generational-stewardship-vertical": ("Generační odpovědnost", "ok", "vertical", "Beztextové; rodina/stewardship."),
}


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def title_from_slug(slug: str) -> str:
    return slug.replace("astronautiste-", "").replace("-", " ").capitalize()


def collect(directory: Path, thumb_dir: Path, og_prefix: str, thumb_prefix: str) -> list[dict]:
    items = []
    for f in sorted(directory.glob("astronautiste-*.jpg")):
        slug = f.stem
        meta = META.get(slug)
        title, brand, aspect, note = meta if meta else (title_from_slug(slug), "warn", "portrait", "")
        has_thumb = (thumb_dir / f.name).exists()
        items.append({
            "slug": slug,
            "title": title,
            "brand": brand,
            "aspect": aspect,
            "note": note,
            "og": f"{og_prefix}/{f.name}",
            "thumb": f"{thumb_prefix}/{f.name}" if has_thumb else f"{og_prefix}/{f.name}",
        })
    return items


def write_group(lines: list[str], gid: str, title: str, note: str, items: list[dict]) -> None:
    lines.append("[[groups]]")
    lines.append(f'id = "{esc(gid)}"')
    lines.append(f'title = "{esc(title)}"')
    lines.append(f'note = "{esc(note)}"')
    lines.append(f"count = {len(items)}")
    for it in items:
        lines.append("")
        lines.append("  [[groups.items]]")
        for key in ("slug", "title", "brand", "aspect", "note", "og", "thumb"):
            lines.append(f'  {key} = "{esc(it[key])}"')
    lines.append("")


def main() -> None:
    campaign = collect(SOCIAL, SOCIAL / "thumbs", "/og/social", "/og/social/thumbs")
    # generated jsou v podsložce (glob kořene je nezahrne) → načti zvlášť
    gen_dir = SOCIAL / GEN_SUB
    generated = collect(
        gen_dir, SOCIAL / "thumbs" / GEN_SUB,
        f"/og/social/{GEN_SUB}", f"/og/social/thumbs/{GEN_SUB}",
    ) if gen_dir.exists() else []

    ok = sum(1 for it in campaign + generated if it["brand"] == "ok")
    warn = sum(1 for it in campaign + generated if it["brand"] == "warn")
    err = sum(1 for it in campaign + generated if it["brand"] == "error")

    lines: list[str] = []
    lines.append("# AUTO-GENEROVÁNO scripts/build-og-manifest.py — needituj ručně.")
    lines.append(f"total = {len(campaign) + len(generated)}")
    lines.append(f"ok = {ok}")
    lines.append(f"warn = {warn}")
    lines.append(f"error = {err}")
    lines.append('hero = "/og/astronautiste-og-hero.jpg"')
    lines.append('contact_sheet = "/og/social/_contact-sheet.jpg"')
    lines.append("")
    write_group(lines, "generated", "Beztextové generated assety (2026-06-16)",
                "Bez vypáleného textu — bezpečné pro veřejné OG s HTML/CSS overlayem.", generated)
    write_group(lines, "campaign", "Kampaňové postery",
                "Náhledy 1200×630 (contain na Void Black). Pozor na vypálené překlepy.", campaign)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"→ {OUT.relative_to(ROOT)}  ({len(campaign)} campaign + {len(generated)} generated; ok={ok} warn={warn} error={err})")


if __name__ == "__main__":
    main()
