# Astronautiste Page Backgrounds 10 Zero-G — 2026-06-16

Clean responsive page backgrounds and carousel images with a stricter
microgravity pass for orbital station and spacecraft scenes.

## Gravity QA

For orbital station, airlock, transit, and classroom scenes:

- no normal standing or sitting posture
- no feet planted on a floor unless visibly held in foot restraints
- hair is short, tied back, or floating outward rather than hanging down
- bodies float, hold handrails, use foot loops, or are tethered
- loose equipment is mounted, tethered, or visibly contained

Lunar surface scenes may show standing because the Moon has gravity, but the
composition still avoids Earth-like casual posture.

## Outputs

Public manifest:

```text
/page-backgrounds/pages-10-20260616-zero-g/responsive-manifest.json
```

Variant groups:

| Path | Count | Size | DPI | Purpose |
|---|---:|---:|---:|---|
| `../../static/page-backgrounds/pages-10-20260616-zero-g/background/desktop-16x9-3840x2160/` | 10 | 3840×2160 | 300 | desktop HTML5 backgrounds |
| `../../static/page-backgrounds/pages-10-20260616-zero-g/background/tablet-4x3-2048x1536/` | 10 | 2048×1536 | 300 | tablet HTML5 backgrounds |
| `../../static/page-backgrounds/pages-10-20260616-zero-g/background/mobile-9x16-1440x2560/` | 10 | 1440×2560 | 300 | mobile HTML5 backgrounds |
| `../../static/page-backgrounds/pages-10-20260616-zero-g/background/mobile-9x16-2160x3840/` | 10 | 2160×3840 | 300 | high-density mobile backgrounds |
| `../../static/page-backgrounds/pages-10-20260616-zero-g/carousel/wide-16x9-2560x1440/` | 10 | 2560×1440 | 300 | landscape carousel |
| `../../static/page-backgrounds/pages-10-20260616-zero-g/carousel/square-1x1-1600x1600/` | 10 | 1600×1600 | 300 | square carousel |
| `../../static/page-backgrounds/pages-10-20260616-zero-g/carousel/portrait-4x5-1600x2000/` | 10 | 1600×2000 | 300 | portrait carousel |
| `../../static/page-backgrounds/pages-10-20260616-zero-g/carousel/story-9x16-1080x1920/` | 10 | 1080×1920 | 300 | mobile story carousel |

Regenerate:

```bash
PAGE_BG_SET_ID=pages-10-20260616-zero-g python3 scripts/generate-page-background-responsive.py
```
