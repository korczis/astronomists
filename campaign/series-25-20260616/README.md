# Astronautiste Series 25 — Flowbite-ready assets

This directory contains public website assets for dynamic HTML/CSS overlays.

## Asset Modes

| Mode | Path | Count | Purpose |
|---|---|---:|---|
| Clean vertical | `clean/vertical/` | 25 | Background-only poster images, no text/logo |
| Clean wide | `clean/wide-16x9/` | 25 | Background-only 16:9 hero images, no text/logo |
| Clean social | `/og/social/series-25-20260616/clean/` | 25 | Background-only OG/social images |
| Rendered vertical | `rendered/vertical/` | 25 | Pre-rendered text/logo poster images |
| Rendered wide | `rendered/wide-16x9/` | 25 | Pre-rendered text/logo 16:9 images |
| Rendered social | `/og/social/series-25-20260616/` | 25 | Pre-rendered OG/social previews |

The complete data map is in `manifest.json`.

## Flowbite / Tailwind Dynamic Overlay

Use clean images as backgrounds and place all copy in HTML. This keeps Czech text,
CTA, logo, and layout editable.

```html
<article class="group relative isolate overflow-hidden rounded-none bg-black text-white shadow-xl">
  <img
    src="/campaign/series-25-20260616/clean/wide-16x9/astronautiste-01-zvedavost-je-start-clean-wide-16x9.jpg"
    alt=""
    class="h-full min-h-[420px] w-full object-cover"
    loading="lazy"
  />

  <div class="absolute inset-0 bg-gradient-to-r from-black/85 via-black/55 to-black/10"></div>

  <div class="absolute inset-0 flex max-w-3xl flex-col justify-between p-6 sm:p-10 lg:p-14">
    <div>
      <p class="mb-3 text-xs font-bold uppercase tracking-[0.22em] text-[#d4a574]">
        01 · ZVĚDAVOST
      </p>
      <h2 class="max-w-xl text-4xl font-black uppercase leading-none tracking-normal text-[#f8f8f8] sm:text-6xl">
        Zvědavost je start.
      </h2>
      <p class="mt-4 max-w-lg text-xl font-bold text-[#4aa3df] sm:text-2xl">
        Každá velká cesta začíná otázkou.
      </p>
    </div>

    <div class="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
      <div>
        <div class="mb-4 h-1.5 w-20 bg-[#e63946]"></div>
        <p class="text-lg font-black uppercase text-[#f8f8f8]">Každé dítě na orbitu.</p>
        <p class="text-sm text-slate-300">astronautiste.cz</p>
      </div>
      <a href="#zapoj-se" class="inline-flex items-center rounded-none bg-[#f8f8f8] px-5 py-3 text-sm font-bold uppercase text-[#0a0a0a] hover:bg-[#d4a574]">
        Zapoj se
      </a>
    </div>
  </div>
</article>
```

## JS-driven Topic Picker

```js
const res = await fetch('/campaign/series-25-20260616/manifest.json');
const data = await res.json();
const topic = data.topics[0];

document.querySelector('[data-campaign-img]').src = topic.urls.clean_wide_16x9;
document.querySelector('[data-campaign-kicker]').textContent =
  `${String(topic.index).padStart(2, '0')} · ${topic.accent}`;
document.querySelector('[data-campaign-headline]').textContent = topic.headline;
document.querySelector('[data-campaign-subhead]').textContent = topic.subhead;
```

## Prerendered Fallback

For channels that cannot render HTML overlays reliably, use the corresponding
`rendered_*` URL from the manifest.

