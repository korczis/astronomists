# Campaign posters — generated images

> Astronautisté AI-generované postery zkopírovány z `~/Downloads` (batch `*_36391..._n.jpg`,
> 2026-06-16), přejmenovány podle obsahu (lower-cased-dashed, prefix značky).
> Originály ponechány v Downloads. ~5.5 MB, JPG.

## Astronautisté (17)

| Soubor | Headline / obsah | Brand text v obrázku |
|---|---|---|
| `astronautiste-dnesni-rozhodnuti-jeho-zitrek-story` | „Dnešní rozhodnutí. Jeho zítřek." matka + syn, ISS (9:16) | ✅ ASTRONAUTISTÉ |
| `astronautiste-logo-horizon-wide` | logo nad horizontem Země (wide) | ✅ ASTRONAUTISTÉ |
| `astronautiste-zvedavost-je-jiskra-reading` | „…je jiskra / palivo / cíl" chlapec čte v posteli, Sagan | ⚠️ AUSTRONAUTISTÉ + „ZVÍDAVOST" |
| `astronautiste-zvedavost-je-jiskra-galaxy-jar` | totéž, dívka s galaxií ve sklenici, Roosevelt | ⚠️ AUSTRONAUTISTÉ |
| `astronautiste-zvedavost-otevira-dvere` | „…dveře / vesmír / spolu" dívka staví satelit, Hawking | ⚠️ AUSTRONAUTISTÉ |
| `astronautiste-zvedavost-je-palivo-vzdelani-je-sila` | „…palivo / síla / naše" chlapec staví raketu | ⚠️ AUSTRONAUTISTÉ |
| `astronautiste-deti-dnes-objevitele-zitra` | „Děti dnes. Objevitelé zítra." chlapec ve skafandru | ⚠️ AUSTRONAUTISTÉ + „SKLÍDĚME" |
| `astronautiste-budoucnost-neni-misto-je-to-smer` | „Budoucnost není místo. Je to směr." měsíční kolonie | ⚠️ AUSTRONAUTISTÉ |
| `astronautiste-nektere-lekce-se-nedaji-naucit` | „Některé lekce se nedají naučit. Musíš je vidět." Malcolm X | ⚠️ AUSTRONAUTISTÉ |
| `astronautiste-jedna-planeta-mnoho-generaci-wide` | „Jedna planeta. Mnoho generací." chlapec na útesu (wide) | ⚠️ AUSTRONAUTISTÉ |
| `astronautiste-vzhuru-za-poznanim` | „Vzhůru za poznáním. Za budoucností. Za dětmi." Drucker | ⚠️ AUSTRONAUTISTÉ |
| `astronautiste-hranice-konci-zvedavost-ne` | „Hranice končí. Zvědavost ne." děti hledí na Zemi, Armstrong | ⚠️ AUSTRONAUTISTÉ |
| `astronautiste-objevujeme-dnesek-inspirujeme-zitky` | „Objevujeme dnešek…" chlapec u teleskopu, aurora | ⚠️ AUSTRONAUTISTÉ + „ZÍTKY" |
| `astronautiste-kazde-dite-na-orbitu-nase-nejvetsi-investice-wide` | „Každé dítě na orbitu." dívka u okna, Einstein (wide) | ⚠️ AUSTRONAUTISTÉ |
| `astronautiste-kazde-dite-na-orbitu-square` | typografický square „Každé dítě na orbitu" | ⚠️ austronautiste.cz |
| `astronautiste-kazde-dite-na-orbitu-program-story` | program (kosmické lety…) dívka u okna (9:16) | ❌ AUSTRANISTÉ |
| `astronautiste-rocket-trail-mirime-vysoko` | minimalistická raketa, „Míříme vysoko. Pro všechny." | ⚠️ AUSTRONAUTISTÉ |

## ⚠️ Brand QA — opravit před publikací

Kanonická podoba: **Astronautisté** / **astronautiste.cz** (viz `design-system/`, logo).
Generované obrázky mají vypálené chyby (= nutno **přegenerovat**, ne editovat):

| Chyba v obrázku | Správně | Výskyt |
|---|---|---|
| `AUSTRONAUTISTÉ` (přebývá „U") | ASTRONAUTISTÉ | většina Astronautisté posterů |
| `AUSTRANISTÉ` | ASTRONAUTISTÉ | `…program-story` |
| `austronautiste.cz` | astronautiste.cz | většina |
| `ZVÍDAVOST` | ZVĚDAVOST | `…je-jiskra-reading` |
| `INSPIRUJEME ZÍTKY` | ZÍTŘKY | `…inspirujeme-zitky` |
| `SKLÍDĚME` | SKLÍZÍME | `…objevitele-zitra` |

Bez chyb (použitelné): `…dnesni-rozhodnuti-jeho-zitrek-story`, `…logo-horizon-wide`.

## Astronautisté Series 25 — 2026-06-16

Deterministicky sazená česká campaign series vytvořená skriptem:

```bash
python3 scripts/generate-astronautiste-series-25.py
```

Výstupy:

| Cesta | Počet | Rozměr | DPI | Účel |
|---|---:|---:|---:|---|
| `series-25-20260616/vertical/` | 25 | 2400×3600 | 300 | high-res vertical posters |
| `series-25-20260616/wide-16x9/` | 25 | 3840×2160 | 300 | high-res wide posters |
| `series-25-20260616/clean/vertical/` | 25 | 2400×3600 | 300 | clean vertical backgrounds without text/logo |
| `series-25-20260616/clean/wide-16x9/` | 25 | 3840×2160 | 300 | clean wide backgrounds without text/logo |
| `../static/og/social/series-25-20260616/` | 25 | 1200×630 | 300 | social / OG previews |
| `../static/campaign/series-25-20260616/` | 100 | mixed | 300 | public clean/rendered assets for Flowbite/HTML |

Text je sazen lokálně přes Pillow, aby česká diakritika, logotyp a CTA byly konzistentní.
Podklady jsou primárně beztextové Astronautisté obrazy z `generated-20260616/`.
Clean výstupy neobsahují text ani logotyp; jsou určené pro HTML/CSS/JS overlay.

## Astronautisté Orbital 10 — 2026-06-16

Orbitální doplněk série: pohled ze stanice, EVA, laboratorní pokusy na stanici,
cesta k Měsíci, měsíční výlet, návrat ke stanici a výuka na orbitě.

```bash
python3 scripts/generate-astronautiste-orbital-10.py
```

Výstupy:

| Cesta | Počet | Rozměr | DPI | Účel |
|---|---:|---:|---:|---|
| `orbital-10-20260616/source-clean/` | 10 | source PNG | n/a | původní beztextové AI podklady |
| `orbital-10-20260616/vertical/` | 10 | 2400×3600 | 300 | high-res vertical posters |
| `orbital-10-20260616/wide-16x9/` | 10 | 3840×2160 | 300 | high-res wide posters |
| `orbital-10-20260616/clean/vertical/` | 10 | 2400×3600 | 300 | clean vertical backgrounds without text/logo |
| `orbital-10-20260616/clean/wide-16x9/` | 10 | 3840×2160 | 300 | clean wide backgrounds without text/logo |
| `../static/og/social/orbital-10-20260616/` | 10 | 1200×630 | 300 | social / OG previews |
| `../static/campaign/orbital-10-20260616/` | 40 | mixed | 300 | public clean/rendered assets for Flowbite/HTML |

Clean výstupy neobsahují text ani logotyp; textové varianty jsou pre-rendered
stejným lokálním rendererem jako `series-25-20260616`.
