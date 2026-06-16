# Astronautiste Page Backgrounds 10 — 2026-06-16

Clean 16:9 background images for website pages. No text, no logos, no labels,
no watermarks. Intended for HTML/CSS overlays with Flowbite/Tailwind.

## Outputs

| Path | Count | Format | Size | DPI | Purpose |
|---|---:|---|---:|---:|---|
| `source-clean/` | 10 | PNG | generator-native | n/a | archived clean generated sources |
| `../../static/page-backgrounds/pages-10-20260616/clean-16x9-8k/` | 10 | JPG | 7680×4320 | 300 | public super high-res page backgrounds |
| `../../static/page-backgrounds/pages-10-20260616/thumbs/` | 10 | JPG | 960×540 | 144 | lightweight previews |
| `../../static/page-backgrounds/pages-10-20260616/background/desktop-16x9-3840x2160/` | 10 | JPG | 3840×2160 | 300 | desktop HTML5 backgrounds |
| `../../static/page-backgrounds/pages-10-20260616/background/tablet-4x3-2048x1536/` | 10 | JPG | 2048×1536 | 300 | tablet HTML5 backgrounds |
| `../../static/page-backgrounds/pages-10-20260616/background/mobile-9x16-1440x2560/` | 10 | JPG | 1440×2560 | 300 | mobile HTML5 backgrounds |
| `../../static/page-backgrounds/pages-10-20260616/background/mobile-9x16-2160x3840/` | 10 | JPG | 2160×3840 | 300 | high-density mobile backgrounds |
| `../../static/page-backgrounds/pages-10-20260616/carousel/wide-16x9-2560x1440/` | 10 | JPG | 2560×1440 | 300 | landscape carousel slides |
| `../../static/page-backgrounds/pages-10-20260616/carousel/square-1x1-1600x1600/` | 10 | JPG | 1600×1600 | 300 | square carousel slides |
| `../../static/page-backgrounds/pages-10-20260616/carousel/portrait-4x5-1600x2000/` | 10 | JPG | 1600×2000 | 300 | portrait carousel slides |
| `../../static/page-backgrounds/pages-10-20260616/carousel/story-9x16-1080x1920/` | 10 | JPG | 1080×1920 | 300 | mobile story carousel slides |

Public manifest:

```text
/page-backgrounds/pages-10-20260616/manifest.json
/page-backgrounds/pages-10-20260616/responsive-manifest.json
```

## HTML5 Page Background

Use `picture` for device-specific crops. The mobile crop is portrait, so the page
does not depend on browser-side `object-fit` cropping.

```html
<section class="relative isolate min-h-[72svh] overflow-hidden bg-black text-white">
  <picture class="absolute inset-0">
    <source
      media="(max-width: 640px)"
      srcset="/page-backgrounds/pages-10-20260616/background/mobile-9x16-1440x2560/astronautiste-page-bg-01-orbital-station-observation-bg-mobile-9x16-1440x2560.jpg 1440w,
              /page-backgrounds/pages-10-20260616/background/mobile-9x16-2160x3840/astronautiste-page-bg-01-orbital-station-observation-bg-mobile-9x16-2160x3840.jpg 2160w"
    />
    <source
      media="(max-width: 1024px)"
      srcset="/page-backgrounds/pages-10-20260616/background/tablet-4x3-2048x1536/astronautiste-page-bg-01-orbital-station-observation-bg-tablet-4x3-2048x1536.jpg"
    />
    <img
      src="/page-backgrounds/pages-10-20260616/background/desktop-16x9-3840x2160/astronautiste-page-bg-01-orbital-station-observation-bg-desktop-16x9-3840x2160.jpg"
      alt=""
      class="h-full w-full object-cover"
      loading="eager"
      decoding="async"
    />
  </picture>
  <div class="absolute inset-0 bg-gradient-to-r from-black/85 via-black/50 to-black/10"></div>
  <div class="relative z-10 mx-auto flex min-h-[72svh] max-w-7xl items-center px-6 py-20">
    <!-- Dynamic page content goes here. -->
  </div>
</section>
```

## Carousel

Use the carousel aspect that matches the current layout: `wide-16x9` for desktop,
`portrait-4x5` for compact cards, `square-1x1` for grids, and `story-9x16` for
mobile full-height slides.

```html
<img
  src="/page-backgrounds/pages-10-20260616/carousel/portrait-4x5-1600x2000/astronautiste-page-bg-01-orbital-station-observation-carousel-portrait-4x5-1600x2000.jpg"
  alt=""
  class="h-full w-full object-cover"
  loading="lazy"
  decoding="async"
/>
```

Regenerate:

```bash
python3 scripts/generate-page-background-responsive.py
```
