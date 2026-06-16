#!/usr/bin/env python3
"""Generate the 10-topic Astronautiste orbital campaign set."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_SCRIPT = ROOT / "scripts/generate-astronautiste-series-25.py"
SET_ID = "orbital-10-20260616"


def load_base_renderer():
    spec = importlib.util.spec_from_file_location("astronautiste_series_renderer", BASE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load renderer from {BASE_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def configure(module) -> None:
    source_root = ROOT / "assets/campaign-posters" / SET_ID / "source-clean"
    module.BG_SOURCES = [
        source_root / "01-orbital-station-cupola.png",
        source_root / "02-eva-outside-station.png",
        source_root / "03-station-laboratory.png",
        source_root / "04-lunar-transfer.png",
        source_root / "05-orbital-sunrise.png",
        source_root / "06-airlock-eva-training.png",
        source_root / "07-microgravity-physics.png",
        source_root / "08-lunar-surface-excursion.png",
        source_root / "09-moon-return-docking.png",
        source_root / "10-orbital-classroom.png",
    ]

    module.TOPICS = [
        module.Topic("pohled-ze-stanice", "Pohled ze stanice.", "Země se vejde do jednoho okna.", "Kdo vidí celek, chápe odpovědnost.", "ORBITA"),
        module.Topic("vystup-do-volneho-vesmiru", "Výstup do volného vesmíru.", "Odvaha začíná přípravou.", "Každý krok venku stojí na důvěře a vědě.", "EVA"),
        module.Topic("laborator-na-stanici", "Laboratoř na stanici.", "Pokusy, které padají jen na Zemi.", "Mikrogravitace ukazuje svět jinak.", "POKUS"),
        module.Topic("vylet-na-mesic", "Výlet na Měsíc.", "Ne útěk ze Země. Návrat s perspektivou.", "Cesta vzhůru učí pokoru k domovu.", "MĚSÍC"),
        module.Topic("svitani-na-orbite", "Svítání na orbitě.", "Každých devadesát minut nový začátek.", "Rytmus kosmu učí trpělivosti.", "SVÍTÁNÍ"),
        module.Topic("pred-vystupem", "Před výstupem.", "Nejdřív kontrola. Potom odvaha.", "Bezpečnost je součást dobrodružství.", "PŘÍPRAVA"),
        module.Topic("fyzika-bez-tize", "Fyzika bez tíže.", "Kapka vody se stane laboratoří.", "Když změníš podmínky, uvidíš zákony.", "MIKROGRAVITACE"),
        module.Topic("prvni-krok-v-prachu", "První krok v prachu.", "Měsíc je blízko. Odpovědnost ještě blíž.", "Každý otisk má směr domů.", "KROK"),
        module.Topic("navrat-ke-stanici", "Návrat ke stanici.", "Mise končí přesným přiblížením.", "Velké sny potřebují klidné ruce.", "NÁVRAT"),
        module.Topic("trida-na-orbite", "Třída na orbitě.", "Učení začne, když se změní měřítko.", "Vesmír není učebnice. Je to zkušenost.", "TŘÍDA"),
    ]

    module.OUT_ROOT = ROOT / "assets/campaign-posters" / SET_ID
    module.OUT_VERTICAL = module.OUT_ROOT / "vertical"
    module.OUT_WIDE = module.OUT_ROOT / "wide-16x9"
    module.OUT_CLEAN_VERTICAL = module.OUT_ROOT / "clean/vertical"
    module.OUT_CLEAN_WIDE = module.OUT_ROOT / "clean/wide-16x9"
    module.OUT_SOCIAL = ROOT / "static/og/social" / SET_ID
    module.OUT_THUMBS = module.OUT_SOCIAL / "thumbs"
    module.OUT_CLEAN_SOCIAL = module.OUT_SOCIAL / "clean"
    module.OUT_CLEAN_THUMBS = module.OUT_SOCIAL / "thumbs/clean"
    module.OUT_STATIC_CAMPAIGN = ROOT / "static/campaign" / SET_ID
    module.OUT_STATIC_CLEAN_VERTICAL = module.OUT_STATIC_CAMPAIGN / "clean/vertical"
    module.OUT_STATIC_CLEAN_WIDE = module.OUT_STATIC_CAMPAIGN / "clean/wide-16x9"
    module.OUT_STATIC_RENDERED_VERTICAL = module.OUT_STATIC_CAMPAIGN / "rendered/vertical"
    module.OUT_STATIC_RENDERED_WIDE = module.OUT_STATIC_CAMPAIGN / "rendered/wide-16x9"


def write_readmes(module) -> None:
    asset_readme = module.OUT_ROOT / "README.md"
    asset_readme.write_text(
        """# Astronautiste Orbital 10 — generated outputs

Orbitální sada 10 témat: pohled ze stanice, EVA, laboratorní pokusy, cesta k Měsíci,
měsíční výlet, návrat a výuka na orbitě.

Výstupy na téma:

| Formát | Cesta | Rozměr | DPI | Text |
|---|---|---:|---:|---|
| Clean vertical | `clean/vertical/` | 2400×3600 | 300 | ne |
| Clean wide | `clean/wide-16x9/` | 3840×2160 | 300 | ne |
| Clean social | `../../../static/og/social/orbital-10-20260616/clean/` | 1200×630 | 300 | ne |
| Rendered vertical | `vertical/` | 2400×3600 | 300 | ano |
| Rendered wide | `wide-16x9/` | 3840×2160 | 300 | ano |
| Rendered social | `../../../static/og/social/orbital-10-20260616/` | 1200×630 | 300 | ano |

Regenerace:

```bash
python3 scripts/generate-astronautiste-orbital-10.py
```

Manifest je v `manifest.json`; veřejná Flowbite-ready kopie je v
`static/campaign/orbital-10-20260616/`.
""",
        encoding="utf-8",
    )

    static_readme = module.OUT_STATIC_CAMPAIGN / "README.md"
    static_readme.write_text(
        """# Astronautiste Orbital 10 — Flowbite-ready assets

Veřejné assety pro dynamické HTML/CSS overlaye a pre-rendered fallbacky.

## Asset Modes

| Mode | Path | Count | Purpose |
|---|---|---:|---|
| Clean vertical | `clean/vertical/` | 10 | Background-only poster images, no text/logo |
| Clean wide | `clean/wide-16x9/` | 10 | Background-only 16:9 hero images, no text/logo |
| Clean social | `/og/social/orbital-10-20260616/clean/` | 10 | Background-only OG/social images |
| Rendered vertical | `rendered/vertical/` | 10 | Pre-rendered text/logo poster images |
| Rendered wide | `rendered/wide-16x9/` | 10 | Pre-rendered text/logo 16:9 images |
| Rendered social | `/og/social/orbital-10-20260616/` | 10 | Pre-rendered OG/social previews |

Kompletní datová mapa je v `manifest.json`.

## Flowbite / Tailwind Dynamic Overlay

Používej čisté obrázky jako pozadí a text/logo/CTA vkládej přes HTML.

```html
<article class="group relative isolate overflow-hidden rounded-none bg-black text-white shadow-xl">
  <img
    src="/campaign/orbital-10-20260616/clean/wide-16x9/astronautiste-01-pohled-ze-stanice-clean-wide-16x9.jpg"
    alt=""
    class="h-full min-h-[420px] w-full object-cover"
    loading="lazy"
  />
  <div class="absolute inset-0 bg-gradient-to-r from-black/85 via-black/55 to-black/10"></div>
  <div class="absolute inset-0 flex max-w-3xl flex-col justify-between p-6 sm:p-10 lg:p-14">
    <div>
      <p class="mb-3 text-xs font-bold uppercase tracking-[0.22em] text-[#d4a574]">01 · ORBITA</p>
      <h2 class="max-w-xl text-4xl font-black uppercase leading-none tracking-normal text-[#f8f8f8] sm:text-6xl">
        Pohled ze stanice.
      </h2>
      <p class="mt-4 max-w-lg text-xl font-bold text-[#4aa3df] sm:text-2xl">
        Země se vejde do jednoho okna.
      </p>
    </div>
  </div>
</article>
```

## JS-driven Topic Picker

```js
const res = await fetch('/campaign/orbital-10-20260616/manifest.json');
const data = await res.json();
const topic = data.topics[0];

document.querySelector('[data-campaign-img]').src = topic.urls.clean_wide_16x9;
document.querySelector('[data-campaign-headline]').textContent = topic.headline;
document.querySelector('[data-campaign-subhead]').textContent = topic.subhead;
```

Pro kanály bez HTML overlaye použij odpovídající `rendered_*` URL z manifestu.
""",
        encoding="utf-8",
    )


def main() -> None:
    module = load_base_renderer()
    configure(module)
    module.main()
    write_readmes(module)


if __name__ == "__main__":
    main()
