# Astronautisté Visual System — One-Sheet Reference
*A complete visual design language for intelligence network exploration. Print this and post it in your design space.*

---

## THE IDEA IN ONE SENTENCE
**Explore intelligence networks with the minimalist clarity of Carl Sagan's Pale Blue Dot, rendered through network topology geometry and playful rocket metaphors.**

---

## PRIMARY PALETTE (MEMORIZE THESE)

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  PRIMARY (Core Identity)                                │
│  ════════════════════════════════════════════════════   │
│                                                         │
│  🟦 Pale Blue      #5B9FD4    ← Trust, exploration      │
│  🟦 Deep Navy      #1F3A52    ← Authority, depth        │
│  🟨 Prism Gold     #E8B85C    ← Refraction, precision   │
│  🟦 Orbit Gray     #4A5568    ← Balance, neutrality     │
│  ⬜ Space White    #F8F9FA    ← Clean, accessible       │
│                                                         │
│  SEMANTIC (Add as needed)                               │
│  ═════════════════════════════════════════════════════   │
│  🟢 Success Green  #5DB85D    ← Verified, positive     │
│  🔴 Alert Red      #C94A4A    ← Threat, error         │
│  🟠 Warning Amber  #D9A84D    ← Caution, deviation    │
│  🔵 Info Cyan      #4DA8D9    ← Information, data     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## TYPE SCALE (USE THESE SIZES)

```
TITAN       3.5rem  Caloto 700   | Hero headlines, max impact
HERO        2.8rem  Caloto 700   | Section titles, CTAs
DISPLAY     2.0rem  Caloto 600   | Subsections
TITLE       1.5rem  Inter 500    | Card titles
BODY        1.0rem  Inter 400    | Paragraph text, UI
SMALL       0.875rem Inter 500   | Captions, metadata
TINY        0.75rem Inter 400    | Timestamps, badges
MONO        0.875rem JetBrains Mono | Code, data output
```

**Key rules**:
- Caloto for headlines (geometric precision + warmth)
- Inter for body (legible, friendly, scales perfectly)
- JetBrains Mono for code/data (intelligence output)

---

## ICON LANGUAGE (CORE 10)

```
⬢  Node         Unit of intelligence, entity, verified fact
→  Edge         Connection, trust flow, trajectory
◉  Orbit        Cycle, monitoring, continuous operation
▲  Trajectory   Positive movement, discovery, growth
⚡ Pulse        Alert, anomaly, sudden change
◆  Prism        Refraction, perspective shift, analysis
⊡  Gate         Verification, passage, threshold
≈  Wave         Data flow, communication, signal
⭐ Star         Excellence, landmark, high-confidence
🚀 Rocket       Launch, aspiration, exploration

How to use:
• Icons in 24px base grid (scales to 16/32/48/64px)
• 1.5px stroke for primary icons
• Color with semantic colors (green for verified, red for threat)
• Hexagon container for network contexts
```

---

## SPACING RHYTHM (THE 8PX RULE)

```
xs:  4px   ← Minimal (tight elements)
sm:  8px   ← Element padding, small gaps
md: 16px   ← Component spacing, card margins
lg: 24px   ← Section spacing, visual breathing
xl: 32px   ← Page margins, major separations
xxl:48px   ← Hero sections, widest gaps

Example card:
┌─────────────────────────────┐
│  padding: 24px (lg)         │
│                             │
│  Title                      │
│  margin-bottom: 16px (md)   │
│                             │
│  Body text...               │
│                             │
│  [Button] [Button]          │
│  gap: 8px (sm)              │
└─────────────────────────────┘
margin: 16px 0 (md)
```

---

## LAYOUTS (RULE OF THIRDS)

```
HERO SECTION (16:9 Desktop)
┌──────────────────────────────────────────┐
│                                          │
│  ┌────────────┐  ┌─────────────────┐    │
│  │  Title     │  │                 │    │
│  │  (at 1/3)  │  │  Network Image  │    │
│  │  Subtitle  │  │  (at 2/3)       │    │
│  │            │  │                 │    │
│  │  [CTA]     │  └─────────────────┘    │
│  │  (at 2/3)  │                         │
│  └────────────┘                         │
│                                          │
└──────────────────────────────────────────┘

DASHBOARD (3-Column Grid)
┌──────────────┬──────────────┬──────────────┐
│              │              │              │
│   Card 1     │   Card 2     │   Card 3     │
│  (1/3 wide)  │  (1/3 wide)  │  (1/3 wide)  │
│              │              │              │
└──────────────┴──────────────┴──────────────┘

MOBILE (Single Column)
┌────────────────────┐
│                    │
│   Card 1           │
│                    │
├────────────────────┤
│                    │
│   Card 2           │
│                    │
├────────────────────┤
│                    │
│   Card 3           │
│                    │
└────────────────────┘
```

---

## DO'S & DON'TS AT A GLANCE

```
✅ DO                              ❌ DON'T

✓ Use Pale Blue + Navy duet       ✗ Mix Pale Blue + Gold in body copy
✓ Nest icons in hexagons          ✗ Use naked icons in dense layouts
✓ Rule-of-thirds for heroes       ✗ Stretch content to full width
✓ 8px whitespace rhythm           ✗ Use <8px spacing (looks cramped)
✓ Max 3 color accents per page    ✗ Use all 10 colors in one mockup
✓ Hexagon grid on landing pages   ✗ Hexagon grid on mobile dashboards
✓ Blue + Navy for trust-building  ✗ Red + Gold for primary CTAs
✓ 16px minimum icon size          ✗ Icons smaller than 16px (blurry)
✓ Semantic colors for status      ✗ Use gold for errors or warnings
✓ 2px outline on focus states     ✗ Browser default blue focus ring
```

---

## COLOR COMBOS (READY TO USE)

```
TRUST & AUTHORITY
├─ Body: Deep Navy #1F3A52 on Space White #F8F9FA
├─ Primary Button: Pale Blue #5B9FD4 on white
├─ Hover Button: +shadow, scale 1.02
└─ Focus Ring: 2px solid Pale Blue (offset 2px)

INTELLIGENCE DASHBOARD
├─ Background: Space White with subtle grid pattern
├─ Cards: White with 1px Orbit Gray border
├─ Primary data: Pale Blue #5B9FD4
├─ Secondary data: Info Cyan #4DA8D9
├─ Status: Green/Red/Amber (semantic)
└─ Labels: Orbit Gray #4A5568

NETWORK VISUALIZATION
├─ Active node: Pale Blue (pulsing)
├─ Verified node: Success Green (checkmark overlay)
├─ Unknown node: Orbit Gray (no fill)
├─ Threat node: Alert Red (exclamation overlay)
└─ Edge/connection: Orbit Gray at 60% opacity

MOBILE DARK MODE
├─ Background: #1A1E25 (very dark, not pure black)
├─ Text: Space White #F8F9FA
├─ Primary: Pale Blue #5B9FD4
├─ Accent: Use gold sparingly (high contrast)
└─ Cards: Semi-transparent white (rgba(248, 249, 250, 0.05))
```

---

## COMPONENT CHECKLIST (BUILD THESE FIRST)

### MVP (3–4 Weeks)
```
☐ PrimaryButton    (size: sm/md/lg, state: default/hover/disabled)
☐ SecondaryButton  (outline style, same size/state variants)
☐ EntityCard       (profile, status badge, confidence bar)
☐ NodeIcon         (16 core set, color-map for states)
☐ Navbar           (logo, nav links, user menu)
☐ Breadcrumbs      (navigation trail with separators)
```

### Phase 2 (4–6 Weeks)
```
☐ InvestigationCard     (network viz + CTA buttons)
☐ TextInput             (with focus/error states)
☐ SelectDropdown        (native-like styling)
☐ ConfidenceIndicator   (sources + percentage)
☐ Table                 (with sort headers)
☐ Modal                 (alert, form, confirmation)
```

### Phase 3 (6+ Weeks)
```
☐ NetworkDiagram        (SVG-based topology)
☐ BarChart / LineChart  (with Pale Blue primary)
☐ Heatmap              (geographic/matrix view)
☐ FilterPanel          (multi-select, search)
☐ Toast Notification   (success, error, info)
☐ Skeleton Loader      (loading states)
```

---

## FONTS TO INSTALL

```
Google Fonts (Recommended):
├─ Caloto      (https://fonts.google.com/specimen/Caloto)
├─ Inter       (https://fonts.google.com/specimen/Inter)
└─ JetBrains Mono (https://fonts.google.com/specimen/JetBrains+Mono)

System Fallback Chain:
font-family: 'Caloto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

Self-Host (Performance):
npm install @fontsource/caloto @fontsource/inter @fontsource/jetbrains-mono
```

---

## STORYBOOK STRUCTURE (FOR TEAMS)

```
Storybook Sidebar:
├─ 🎨 Design Tokens
│  ├─ Colors
│  ├─ Typography
│  └─ Spacing
├─ 🔘 Components
│  ├─ Buttons
│  ├─ Cards
│  ├─ Forms
│  ├─ Navigation
│  └─ Icons
├─ 📱 Pages
│  ├─ Landing Hero
│  ├─ Dashboard
│  └─ Investigation
└─ 🧪 Patterns
   ├─ Network Diagram
   ├─ Data Viz
   └─ Animations
```

Each component story includes:
- Visual (default state)
- Variants (size/state combos)
- Code snippet (copy-paste ready)
- Accessibility notes (WCAG ratios)
- Usage guidelines (when to use)

---

## DARK MODE QUICK SETUP

```css
/* Copy-paste into your CSS */
:root {
  --color-bg: #F8F9FA;
  --color-text: #1F3A52;
  --color-primary: #5B9FD4;
  --color-border: #4A5568;
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #1A1E25;
    --color-text: #F8F9FA;
    --color-primary: #7FB3E8;    /* Lighter pale blue */
    --color-border: #2E3440;     /* Lighter gray */
  }
}

body {
  background: var(--color-bg);
  color: var(--color-text);
}

button {
  background: var(--color-primary);
}
```

---

## ACCESSIBILITY CHECKLIST

```
☐ Color contrast ratios
  ├─ Body text: 4.5:1 minimum (AAA)
  ├─ Large text: 3:1 minimum (AA)
  └─ Test: WebAIM Contrast Checker

☐ Focus states
  ├─ All interactive elements: visible outline
  ├─ Style: 2px solid Pale Blue, 2px offset
  └─ Never remove focus ring without replacement

☐ Typography
  ├─ Minimum 16px on mobile
  ├─ Line-height: 1.5 for body text
  └─ Readable on 200% zoom

☐ Icons
  ├─ All images: descriptive alt text
  ├─ Icons as links: aria-label
  └─ Status icons: color + pattern (not color alone)

☐ Motion
  ├─ Respect prefers-reduced-motion
  ├─ Remove animations if set
  └─ Test: DevTools > Rendering > Emulate CSS media

☐ Keyboard navigation
  ├─ Tab order: logical (top→down, left→right)
  ├─ Visible skip links
  └─ No keyboard traps (arrow in modal, exit with Esc)
```

---

## PERFORMANCE TARGETS

```
Page Load:       <3 seconds (3G)
First Paint:     <1 second
Largest Paint:   <2.5 seconds
Interaction:     <100ms (button click to response)
Network:         <100KB JS, <200KB CSS+fonts
Icon SVG:        <5KB per icon (optimized)
```

**Optimization**:
```bash
svgo src/icons/*.svg          # Optimize SVGs
purgecss --content src/**/*.tsx # Remove unused CSS
npm run build:production      # Minify all assets
lighthouse https://your-site  # Audit performance
```

---

## FILE STRUCTURE (FOR NEW PROJECTS)

```
src/
├─ components/
│  ├─ Button/
│  │  ├─ Button.tsx
│  │  ├─ Button.module.css
│  │  ├─ Button.stories.tsx
│  │  └─ __tests__/Button.test.tsx
│  ├─ Card/
│  ├─ Icons/
│  └─ index.ts
│
├─ styles/
│  ├─ astronautiste.css      ← Main tokens
│  ├─ reset.css              ← Browser reset
│  ├─ index.css              ← Global imports
│  └─ utilities.css          ← Helper classes
│
├─ assets/
│  ├─ icons/                 ← SVG components
│  ├─ patterns/              ← Network grids, etc.
│  └─ fonts/                 ← @font-face declarations
│
└─ App.tsx                   ← Wrap with theme provider
```

---

## QUICK COMMAND REFERENCE

```bash
# Development
npm run dev              # Start dev server with hot reload
npm run storybook       # Open component library (port 6006)

# Build & Test
npm run build           # Production build
npm run test            # Run all tests
npm run test:a11y       # Accessibility testing
npm run lint            # Style & type checking

# Design Tokens
npm run export:tokens   # Figma → JSON
npm run build:css       # JSON → CSS variables
npm run sync:figma      # Pull latest from Figma

# Optimization
npm run optimize:icons  # Compress all SVG icons
npm run purge:css       # Remove unused styles
npm run audit:color     # WCAG contrast check

# Deployment
npm run build:prod      # Optimized production build
npm run lighthouse      # Performance audit
```

---

## FIGMA PLUGIN RECOMMENDATIONS

```
⭐ Essential (Install First)
├─ Figma Tokens            (sync tokens to code)
├─ Wireframer              (rapid prototyping)
├─ Color Blind             (a11y testing)
└─ Accessibility Checker   (WCAG validation)

⭐ Nice to Have
├─ Component Organizer     (keep library clean)
├─ Rename It               (bulk renaming)
├─ Storybook Connect       (Figma ↔ Storybook)
└─ Iconify                 (icon management)
```

---

## KEY METRICS TO TRACK

```
Design System Health:
├─ Component adoption (% of app using library)
├─ Design debt (# of custom one-offs)
├─ Figma library version adoption
├─ CSS variable usage (% coverage)
└─ Accessibility compliance (WCAG AAA %)

Product Metrics:
├─ Time to prototyping (reduced with component lib?)
├─ Bug rate (improved with constraints?)
├─ User satisfaction (A/B test new designs)
└─ Performance (Core Web Vitals)
```

---

## CONTACTS & RESOURCES

```
Design System Lead:   design@astronautiste.io
Component Issues:     GitHub #design
Design Feedback:      Figma comments
Storybook:           localhost:6006 (dev)
WCAG Checker:        https://www.tpgi.com/color-contrast-checker/
Google Fonts:        https://fonts.google.com
Figma Plugins:       https://www.figma.com/community/plugins
```

---

## PRINT THIS & POST IT

**Save as**: `astronautiste-design-onesheet.pdf`  
**Print size**: 11" × 17" (tabloid) or 8.5" × 11" (letter)  
**Location**: Design team desk, conference room, Slack pinned message

---

**Astronautisté Visual System — One-Sheet**  
*v1.0 | 2026-06-15 | Print & Share*
