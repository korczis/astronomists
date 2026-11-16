# Astronautiste Orbital 10 — Flowbite-ready assets

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
