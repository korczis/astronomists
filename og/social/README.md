# Social / OG preview platforma

Generováno z `assets/campaign-posters/` skriptem `scripts/generate-og-previews.sh`.
Idempotentní — re-generuj kdykoli po změně zdrojů.

## Obsah

| Cesta | Rozměr | Účel |
|---|---|---|
| `static/og/social/astronautiste-*.jpg` | 1200×630 | OG / Twitter `summary_large_image` preview (1 na poster) |
| `static/og/social/thumbs/astronautiste-*.jpg` | 600 px šířka | náhledy do galerie / gridu |
| `static/og/social/generated-20260616/astronautiste-*.jpg` | 1200×630 | OG preview z nových beztextových generated assetů |
| `static/og/social/thumbs/generated-20260616/astronautiste-*.jpg` | 600 px šířka | náhledy nových beztextových generated assetů |
| `static/og/social/series-25-20260616/astronautiste-*.jpg` | 1200×630 | OG preview pro 25-topic českou campaign series |
| `static/og/social/series-25-20260616/clean/astronautiste-*.jpg` | 1200×630 | čisté OG backgroundy bez textu/loga |
| `static/og/social/series-25-20260616/thumbs/astronautiste-*.jpg` | 600×315 | náhledy 25-topic series |
| `static/campaign/series-25-20260616/` | mixed | veřejné clean/rendered assety pro Flowbite/HTML |
| `static/og/social/orbital-10-20260616/astronautiste-*.jpg` | 1200×630 | OG preview pro 10-topic orbitální campaign set |
| `static/og/social/orbital-10-20260616/clean/astronautiste-*.jpg` | 1200×630 | čisté orbitální OG backgroundy bez textu/loga |
| `static/og/social/orbital-10-20260616/thumbs/astronautiste-*.jpg` | 600×315 | náhledy orbitální sady |
| `static/campaign/orbital-10-20260616/` | mixed | veřejné orbitální clean/rendered assety pro Flowbite/HTML |
| `static/og/social/_contact-sheet.jpg` | 4 sloupce | vizuální index všech náhledů |
| `static/og/astronautiste-og-hero.jpg` | 1200×630 | čistý default OG kandidát (logo-horizon) |

Fit = **contain** na Void Black `#0a0a0a` → celý poster viditelný, bez ořezu, branded pozadí.

## Použití na stránce (per-page OG override)

`base.html` + `head.html` nově podporují override. V `.md` front matteru sekce/stránky:

```toml
[extra]
og_image = "/og/social/astronautiste-budoucnost-neni-misto-je-to-smer.jpg"
og_image_alt = "Budoucnost není místo. Je to směr."
```

Bez override se použije globální default z `config.toml` (`extra.og_image`).

Pro nové beztextové generated assety používej např.:

```toml
[extra]
og_image = "/og/social/generated-20260616/astronautiste-mission-control-classroom-wide.jpg"
og_image_alt = "Astronautisté — děti objevují svět jako ověřitelnou síť."
```

Pro 25-topic series používej např.:

```toml
[extra]
og_image = "/og/social/series-25-20260616/astronautiste-01-zvedavost-je-start-social.jpg"
og_image_alt = "Astronautisté — Zvědavost je start."
```

Pro dynamické HTML/CSS overlaye používej čisté assety a manifest:

```text
/campaign/series-25-20260616/manifest.json
/campaign/series-25-20260616/clean/wide-16x9/
/campaign/series-25-20260616/clean/vertical/
```

Pro orbitální 10-topic sadu:

```text
/campaign/orbital-10-20260616/manifest.json
/campaign/orbital-10-20260616/clean/wide-16x9/
/campaign/orbital-10-20260616/clean/vertical/
```

## Default OG webu

Aktuální default: `config.toml → extra.og_image = "/og/astronautiste-og.png"`.
Čistý kandidát (správné `ASTRONAUTISTÉ`): `/og/astronautiste-og-hero.jpg`.

## Regenerace

```bash
bash scripts/generate-og-previews.sh
python3 scripts/generate-astronautiste-series-25.py
python3 scripts/generate-astronautiste-orbital-10.py
```

## ⚠️ Pozn. k brand chybám
Většina zdrojových posterů má vypálené `AUSTRONAUTISTÉ` / `austronautiste.cz`
(viz `assets/campaign-posters/README.md`). Pro veřejné OG preferuj bez-chybové:
`astronautiste-logo-horizon-wide`, `astronautiste-dnesni-rozhodnuti-jeho-zitrek-story`.
Nové assety v `generated-20260616/` jsou bez vypáleného textu a jsou bezpečnější
pro veřejné použití s HTML/CSS overlayem.
`og:image:type` v head.html se nastavuje podle přípony (`png`/`jpg`/`webp`).
