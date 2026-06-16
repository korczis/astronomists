# Astronautisté Asset Inventory v1.0

## Asset Catalog & Metadata

Complete inventory of brand assets organized by category, with file references, specifications, and usage guidelines.

---

## 1. Logo Assets

### Primary Logo Set

```
Logo: Spiral Helix Symbol + Wordmark
├── Primary (Dark Background)
│   ├── astronauts_logo_primary_full.svg      [300×100px]
│   ├── astronauts_logo_primary_symbol.svg    [100×100px]
│   └── astronauts_logo_primary_vertical.svg  [100×300px]
├── Inverted (Light Background)
│   ├── astronauts_logo_inverted_full.svg     [300×100px]
│   ├── astronauts_logo_inverted_symbol.svg   [100×100px]
│   └── astronauts_logo_inverted_vertical.svg [100×300px]
└── Monochrome
    ├── astronauts_logo_mono_black.svg        [300×100px]
    └── astronauts_logo_mono_white.svg        [300×100px]
```

### Logo Specifications

**Symbol Design**: Continuous spiral helix (infinity-like curve)
- Color: Cosmic Gold (#D4AF37) on primary, Deep Space Blue (#0F1F3C) on inverted
- Stroke width: 2px
- Viewbox: 0 0 100 100
- Scalable without quality loss (vector SVG only)

**Wordmark**: "ASTRONAUTISTÉ" in Montserrat Bold
- Letter spacing: 0.05em
- Color: Matches symbol
- Minimum size: 40px (height)

**Clearspace**: 20px minimum around entire logo (internal + external)

**Minimum Size**: 100px (symbol only), 150px (symbol + text)

### Logo Usage Rules

| Context | Logo Variant | Background | Padding |
|---------|--------------|-----------|---------|
| Website hero | Primary full | DSB | 40px |
| App header | Primary symbol | DSB | 16px |
| Printed materials | Full-color | White | 20mm |
| Dark backgrounds | Inverted full | #1A1A1A | 30px |
| Favicons | Symbol only | No bg | N/A |
| Merchandise | Monochrome | Natural | 25mm |

---

## 2. Color Assets

### Color Palette Files

```
astronauts_colors.json
├── primary
│   ├── "deep-space-blue": "#0F1F3C"
│   ├── "cosmic-gold": "#D4AF37"
│   └── "stardust-silver": "#E8E8E8"
├── extended
│   ├── "nebula-purple": "#6B4DA1"
│   ├── "aurora-green": "#00C853"
│   ├── "solar-red": "#D32F2F"
│   └── "lunar-gray": "#424242"
└── themes
    ├── "dark": { bg: "#0F1F3C", text: "#E8E8E8" }
    └── "light": { bg: "#FFFFFF", text: "#0F1F3C" }
```

### Color Export Formats

- **JSON**: `astronauts_colors.json` (Web development)
- **CSS**: `astronauts_colors.css` (Stylesheets)
- **SCSS**: `astronauts_colors.scss` (Preprocessor)
- **Figma**: Shared color library (design tool)
- **Pantone**: Print specifications (PDF reference)

---

## 3. Typography Assets

### Font Files

```
fonts/
├── Montserrat/ (sans-serif - primary)
│   ├── Montserrat-Regular.woff2
│   ├── Montserrat-SemiBold.woff2
│   ├── Montserrat-Bold.woff2
│   └── montserrat.css
├── CrimsonText/ (serif - secondary)
│   ├── CrimsonText-Regular.woff2
│   ├── CrimsonText-SemiBold.woff2
│   └── crimson-text.css
└── IBMPlexMono/ (monospace)
    ├── IBMPlexMono-Regular.woff2
    └── ibm-plex-mono.css
```

### Font CSS

```css
@font-face {
  font-family: 'Montserrat';
  src: url('/fonts/Montserrat-Regular.woff2') format('woff2');
  font-weight: 400;
  font-display: swap;
}
```

### Typography Scale Document

- **File**: `typography_scale.json`
- **Contents**: All heading sizes, body text sizes, line heights
- **Format**: CSS custom property format for easy integration

---

## 4. Iconography

### Icon Library

```
icons/
├── Core Icons (24×24px SVG)
│   ├── logo-spiral.svg
│   ├── star.svg
│   ├── planet.svg
│   ├── telescope.svg
│   ├── search.svg
│   ├── menu.svg
│   ├── close.svg
│   ├── chevron-down.svg
│   ├── arrow-right.svg
│   └── settings.svg
├── Status Icons
│   ├── success.svg
│   ├── error.svg
│   ├── warning.svg
│   └── info.svg
├── Social Icons (32×32px)
│   ├── twitter.svg
│   ├── linkedin.svg
│   ├── github.svg
│   └── email.svg
└── Data Viz Icons
    ├── chart-line.svg
    ├── chart-bar.svg
    ├── chart-pie.svg
    └── data-point.svg
```

### Icon Specifications

- **Format**: SVG (scalable)
- **Stroke width**: 2px (24px+), 1.5px (16px)
- **Color**: Typically #E8E8E8 (Silver) or #D4AF37 (Gold)
- **Viewbox**: Consistent 0 0 24 24
- **Accessibility**: Icon + text label required for UI elements

### Icon Usage Example

```html
<svg class="icon icon--star" viewBox="0 0 24 24">
  <use xlink:href="/icons.svg#star"></use>
</svg>
```

---

## 5. Photography & Imagery

### Photography Direction

**Mood**: Scientific, cosmic, contemplative, human-centered

**Subjects**:
- Space imagery (stars, nebulae, planets—authentic NASA/ESA photos preferred)
- People collaborating (diverse, genuine moments)
- Data visualization (charts, graphs, abstract patterns)
- Technology in context (tools being used by humans)

### Image Assets (Metadata Only)

```
photography/
├── Hero Images (1920×1080px min)
│   ├── space_nebula_hero.metadata.json
│   ├── team_collaboration_hero.metadata.json
│   └── data_visualization_hero.metadata.json
├── Pattern Assets (1024×1024px)
│   ├── circuit_pattern.metadata.json
│   └── star_field_pattern.metadata.json
└── Card Images (600×400px)
    ├── researcher_profile.metadata.json
    ├── laboratory_equipment.metadata.json
    └── abstract_data.metadata.json
```

### Metadata Template

```json
{
  "filename": "space_nebula_hero.jpg",
  "size_px": [1920, 1080],
  "format": "jpg",
  "compression": "85% quality",
  "source": "NASA/ESA Public Domain",
  "license": "CC0/Public Domain",
  "usage": "Homepage hero, marketing materials",
  "color_profile": "sRGB",
  "alt_text": "The Orion Nebula with bright stars and dust clouds",
  "accessibility": "decorative | important"
}
```

### Photography Guidelines

- **License**: Only use CC0, CC BY, or proprietary licensed images
- **Attribution**: Always credit source (even CC0)
- **Diversity**: Ensure representation across imagery
- **Authenticity**: Real humans, real data; no generic stock photos
- **Color**: Maintain brand palette harmony

---

## 6. Pattern & Texture Assets

### Decorative Patterns

```
patterns/
├── dot_pattern.svg           [200×200px, repeatable]
├── star_field_pattern.svg    [400×400px, repeatable]
├── circuit_grid_pattern.svg  [300×300px, repeatable]
├── hexagon_mesh.svg          [500×500px, repeatable]
└── gradient_backdrop.svg     [1920×1080px, full-width]
```

### Pattern Usage

| Pattern | Background | Opacity | Use Case |
|---------|-----------|---------|----------|
| Dot pattern | DSB | 15% | Card backgrounds |
| Star field | DSB | 5% | Page backdrop |
| Circuit grid | DSB | 10% | Section dividers |
| Hexagon mesh | CG | 20% | CTA backgrounds |

---

## 7. Presentation Templates

### Document Templates (Metadata Reference)

```
templates/
├── Presentation Deck
│   ├── astronauts_presentation_template.pptx
│   │   └── Layouts: title, content, 2-col, image, blank
│   │   └── Master: brand fonts, colors, logo placement
│   └── astronauts_presentation_guide.pdf
│
├── One-Pager
│   ├── astronauts_one_pager_template.docx
│   └── [1 page, A4, brand margins]
│
├── Whitepaper
│   ├── astronauts_whitepaper_template.docx
│   └── [Multi-page, technical, branded headers/footers]
│
└── Email Newsletter
    ├── astronauts_newsletter_template.html
    └── [Responsive, dark theme default, CTA-friendly]
```

### Template Usage Guidelines

- Use only official templates
- Update brand elements quarterly
- Do not modify fonts or colors without approval
- Maintain 1.5× minimum spacing around logo

---

## 8. Brand Video Assets

### Video Specifications (Metadata)

```
video/
├── Brand Intro (10–15 sec)
│   └── astronauts_brand_intro.metadata.json
│       ├── resolution: 1920×1080 (60fps)
│       ├── format: .mp4 + .webm
│       ├── codec: H.264 (MP4), VP9 (WebM)
│       └── use: Website homepage, social media
│
├── Feature Demo (30–60 sec)
│   └── astronauts_feature_demo.metadata.json
│       └── use: Product pages, email campaigns
│
└── Testimonial Template (15–30 sec)
    └── astronauts_testimonial_template.metadata.json
        └── use: Case studies, homepage rotation
```

### Video Standards

- **Aspect Ratio**: 16:9 (primary), 9:16 (mobile), 1:1 (social)
- **Intro/Outro**: 2–3 seconds (brand logo animation)
- **Color Grading**: Match brand dark theme
- **Captions**: Required (.srt format)
- **Audio**: Royalty-free library (Epidemic Sound, Artlist)

---

## 9. Motion Graphics Assets

### Animation Specifications

```
motion/
├── Logo Animation
│   ├── logo_spiral_entrance.lottie      [JSON animation]
│   ├── duration: 1.5 sec
│   └── use: App startup, page load
│
├── Loading Spinner
│   ├── loading_spinner_cosmic.lottie
│   ├── duration: 2 sec (loop)
│   └── use: Data processing feedback
│
└── Transition Effects
    ├── fade_to_cosmic.lottie
    ├── duration: 0.5 sec
    └── use: Page navigation
```

### Animation Format

- **Format**: Lottie JSON (cross-platform compatibility)
- **Tool**: After Effects + Bodymovin extension
- **File Size**: <50KB per animation (optimized)
- **Loop**: Infinite or explicit endpoint

---

## 10. Social Media Assets

### Social Media Templates

```
social/
├── LinkedIn
│   ├── linkedin_post_1200x628.psd
│   ├── linkedin_banner_1500x500.psd
│   └── brand colors, Montserrat font
│
├── Twitter/X
│   ├── twitter_profile_600x600.svg
│   ├── twitter_banner_1500x500.png
│   └── character limits + image crops
│
├── Instagram
│   ├── instagram_post_1080x1080.psd
│   ├── instagram_stories_1080x1920.psd
│   └── crop-friendly layouts
│
└── Generic Post
    ├── social_post_1200x630.psd
    ├── social_post_square_1080x1080.psd
    └── Use: Multi-platform distribution
```

### Social Media Guidelines

- **Profile Photo**: Logo symbol, 400×400px minimum
- **Banner**: 1500×500px, brand colors, 20px text margin
- **Post Aspect Ratio**: 1.91:1 (desktop feed), 4:5 (mobile feed), 1:1 (square)
- **Text**: Maximum 280 chars (Twitter), 150 chars (recommended legibility)
- **Hashtags**: #Astronautisté #Science #Innovation (brand hashtags)

---

## 11. Development Assets

### Code-Ready Assets

```
dev-assets/
├── CSS
│   ├── brand-colors.css           [Color variables]
│   ├── typography.css              [Font declarations]
│   └── components.css              [Pre-styled components]
│
├── JavaScript
│   ├── brand-config.js             [Constants, settings]
│   └── analytics-events.js         [Event tracking]
│
├── HTML
│   ├── favicon-set.html            [Favicon links]
│   ├── meta-tags.html              [OG tags, SEO]
│   └── structured-data.json        [Schema.org markup]
│
└── SVG
    ├── symbols.svg                 [Sprite sheet]
    └── patterns.svg                [Reusable patterns]
```

### Web Font Implementation

```css
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Crimson+Text:wght@400;600&display=swap');

:root {
  --font-sans: 'Montserrat', sans-serif;
  --font-serif: 'Crimson Text', serif;
}
```

---

## 12. Print & Production Specs

### Print Guidelines

| Item | Format | Size | Colors |
|------|--------|------|--------|
| Business Card | CMYK | 3.5" × 2" | 4-color |
| Letterhead | CMYK | A4/Letter | 2-color |
| Brochure | CMYK | A4 tri-fold | 4-color |
| Poster | CMYK | 24" × 36" | 4-color |
| Banner | CMYK | Custom | 4-color + spot |

### Print Specifications

- **Resolution**: 300 DPI (print), 72 DPI (web)
- **Color Mode**: CMYK (print), RGB (screen)
- **Bleed**: 0.125" on all sides
- **Safe Area**: 0.25" inset from edge
- **File Format**: PDF (print-ready), AI (editable)

---

## 13. Asset Versioning & Updates

### Version Control

| Asset Category | Current Version | Last Updated | Status |
|---|---|---|---|
| Logo | 1.0 | 2026-06-15 | Stable |
| Color Palette | 1.0 | 2026-06-15 | Stable |
| Typography | 1.0 | 2026-06-15 | Stable |
| Icons | 1.2 | 2026-06-10 | Minor updates |
| Patterns | 1.0 | 2026-06-15 | Stable |
| Templates | 1.1 | 2026-06-05 | Minor updates |

### Update Log

- **Metadata file**: `/asset-updates/CHANGELOG.md`
- **Format**: Semantic versioning (MAJOR.MINOR.PATCH)
- **Notice Period**: 30 days before breaking changes

---

## 14. Asset Storage & Access

### Storage Structure

```
/assets (Primary Storage)
├── /logos (all logo variants)
├── /colors (color definitions)
├── /fonts (font files)
├── /icons (icon library)
├── /photography (image metadata)
├── /patterns (texture/pattern SVGs)
├── /templates (presentation files)
├── /videos (video metadata)
└── /social (social media templates)
```

### Access & Permissions

- **Public**: Logos, color definitions, icon library
- **Restricted**: Photography, video content (licensing)
- **Internal Only**: Editable templates, raw source files

### File Naming Convention

```
[category]_[description]_[version].[format]

Examples:
- logo_primary_full_v1.0.svg
- colors_palette_extended_v1.0.json
- icon_star_v1.2.svg
- pattern_dot_v1.0.svg
```

---

## Asset Delivery Checklist

Before distributing brand assets:

- [ ] All files named consistently
- [ ] Metadata complete and current
- [ ] Version numbers accurate
- [ ] License information included
- [ ] Usage guidelines documented
- [ ] Color profiles standardized
- [ ] File formats optimized
- [ ] Accessibility alt-text provided
- [ ] File sizes minimized
- [ ] Directory structure explained

---

**Asset Inventory Version**: 1.0  
**Last Updated**: 2026-06-15  
**Owner**: Brand Operations Team  
**Next Review**: 2026-09-15  
**Status**: Complete, all assets inventoried
