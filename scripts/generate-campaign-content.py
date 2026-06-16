#!/usr/bin/env python3
"""Generuje Zola content pro kampaňovou sekci /kampan/ z 25dílné série.

Zdroj pravdy je `TOPICS` (sdílené se scripts/generate-astronautiste-series-25.py).
Výstup:
- content/kampan/_index.md            → hub (template hub.html)
- content/kampan/NN-<slug>.md         → 25 detail stránek (template detail.html)

OG náhledy bere z static/og/social/series-25-20260616/ (idempotentní, přepisuje).
Spusť: python3 scripts/generate-campaign-content.py
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "content" / "kampan"
SOCIAL_BASE = "/og/social/series-25-20260616"
SOCIAL_DISK = ROOT / "static" / "og" / "social" / "series-25-20260616"


@dataclass(frozen=True)
class Topic:
    slug: str
    headline: str
    subhead: str
    proof: str
    accent: str


# Pořadí je závazné — určuje weight i číslo v názvu OG souboru (NN).
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

TAGLINE = "Myslíme na hvězdy, jednáme vědecky."


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def og_path(idx: int, slug: str) -> str:
    return f"{SOCIAL_BASE}/astronautiste-{idx:02d}-{slug}-social.jpg"


def detail_md(idx: int, t: Topic) -> str:
    og = og_path(idx, t.slug)
    alt = f"Astronautisté — {t.headline}"
    body = (
        f"{t.proof}\n\n"
        "Každý plakát téhle série je jedna věta a jeden obraz — protože nejsilnější "
        f"myšlenky se vejdou na jeden dech. {t.subhead}\n\n"
        f"**{TAGLINE}**\n"
    )
    return (
        "+++\n"
        f'title = "{esc(t.headline)}"\n'
        f'description = "{esc(t.subhead)}"\n'
        f"weight = {idx}\n"
        'template = "detail.html"\n'
        "\n"
        "[extra]\n"
        f'eyebrow = "{esc(t.accent)}"\n'
        f'lead = "{esc(t.subhead)}"\n'
        f'anchor = "{esc(t.proof)}"\n'
        f'image = "{og}"\n'
        f'og_image = "{og}"\n'
        f'og_image_alt = "{esc(alt)}"\n'
        "+++\n\n"
        f"{body}"
    )


def hub_md() -> str:
    hero = og_path(1, TOPICS[0].slug)
    return (
        "+++\n"
        'title = "Kampaň — 25 plakátů"\n'
        'description = "Dvacet pět plakátů, jeden horizont. Jedna věta, jeden obraz, jeden dech."\n'
        'sort_by = "weight"\n'
        'template = "hub.html"\n'
        "\n"
        "[extra]\n"
        'eyebrow = "Kampaň 2026"\n'
        'lead = "Dvacet pět plakátů, jeden horizont. Každý nese jednu myšlenku hnutí — od dětské otázky k větší budoucnosti."\n'
        f'image = "{hero}"\n'
        f'og_image = "{hero}"\n'
        'og_image_alt = "Astronautisté — kampaň 2026, 25 plakátů."\n'
        "+++\n\n"
        "Kampaňová série Astronautistů. Klikni na kterýkoli plakát pro jeho myšlenku, "
        "kontext a sdílecí náhled.\n"
    )


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "_index.md").write_text(hub_md(), encoding="utf-8")
    missing = []
    for i, t in enumerate(TOPICS, start=1):
        if not (SOCIAL_DISK / f"astronautiste-{i:02d}-{t.slug}-social.jpg").exists():
            missing.append(f"{i:02d}-{t.slug}")
        (OUT_DIR / f"{i:02d}-{t.slug}.md").write_text(detail_md(i, t), encoding="utf-8")
    print(f"→ content/kampan/  (1 hub + {len(TOPICS)} detail stránek)")
    if missing:
        print(f"  ⚠ chybí OG náhled pro: {', '.join(missing)}")


if __name__ == "__main__":
    main()
