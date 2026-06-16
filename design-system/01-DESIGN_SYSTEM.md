# Astronautisté Design System v1.0

## System Overview

Complete design specification for Astronautisté visual language. This document covers color systems, typography, components, spacing, iconography, and implementation guidelines.

---

## 1. Color System

### Primary Palette

```
Deep Space Blue (DSB)
  Hex: #0F1F3C
  RGB: 15, 31, 60
  CMYK: 75, 48, 0, 76
  Usage: Primary background, brand anchor, headers
  Accessibility: WCAG AAA compliant

Cosmic Gold (CG)
  Hex: #D4AF37
  RGB: 212, 175, 55
  CMYK: 0, 17, 74, 17
  Usage: Accent, CTA buttons, highlights
  Accessibility: High contrast on DSB

Stardust Silver (SS)
  Hex: #E8E8E8
  RGB: 232, 232, 232
  CMYK: 0, 0, 0, 9
  Usage: Text, dividers, subtle backgrounds
  Accessibility: Primary text color on DSB
```

### Extended Palette

| Color Name | Hex | Usage | WCAG |
|------------|-----|-------|------|
| Nebula Purple | #6B4DA1 | Secondary accent, data viz | AAA |
| Stellar White | #FFFFFF | Maximum contrast | AAA |
| Void Black | #000000 | Text emphasis | AAA |
| Aurora Green | #00C853 | Success states | AAA |
| Solar Red | #D32F2F | Error/warning states | AAA |
| Lunar Gray | #424242 | Disabled states, subtle text | AA |

### Accessibility Requirements

- Minimum contrast ratio: 4.5:1 (normal text), 3:1 (large text)
- Color not sole means of conveying information
- All data visualizations must have pattern/texture backup
- High-contrast mode support mandatory

---

## 2. Typography System

### Font Family

**Primary: Montserrat** (sans-serif)
- Usage: Headings, UI labels, navigation
- Weights: 400 (regular), 600 (semibold), 700 (bold)
- Letter spacing: -0.5% (headlines), 0% (body)

**Secondary: Crimson Text** (serif)
- Usage: Long-form content, quotes, emphasis
- Weights: 400 (regular), 600 (semibold)
- Line height: 1.6 (body), 1.3 (headers)

**Monospace: IBM Plex Mono** (monospace)
- Usage: Code blocks, technical references
- Weight: 400 (regular)
- Size: 0.9em relative to parent

### Scale & Sizing

```
H1: 3.2rem (51.2px)  | Montserrat 700 | Line-height 1.2
H2: 2.4rem (38.4px)  | Montserrat 700 | Line-height 1.3
H3: 1.8rem (28.8px)  | Montserrat 600 | Line-height 1.4
H4: 1.4rem (22.4px)  | Montserrat 600 | Line-height 1.4
Body: 1rem (16px)    | Crimson Text 400 | Line-height 1.6
Small: 0.875rem      | Montserrat 400 | Line-height 1.5
Caption: 0.75rem     | Montserrat 400 | Line-height 1.4
```

### Line Height & Spacing

- Headings: 1.2–1.4
- Body text: 1.6–1.8
- Paragraph margin-bottom: 1.5rem
- Letter spacing (headings): -0.02em

---

## 3. Spacing & Layout

### Spacing Scale

```
0px    base
4px    xs
8px    sm
16px   md
24px   lg
32px   xl
48px   2xl
64px   3xl
96px   4xl
```

### Grid System

- 12-column responsive grid
- Gutter: 24px (desktop), 16px (tablet), 8px (mobile)
- Max container width: 1280px
- Breakpoints: 320px, 768px, 1024px, 1280px, 1600px

### Common Spacing Patterns

| Pattern | Spacing | Context |
|---------|---------|---------|
| Component padding | 16px–24px | Cards, buttons |
| Section margin | 48px–64px | Major content blocks |
| Nested padding | 8px–12px | Input fields, chips |
| Whitespace ratio | 30–40% | Page layouts |

---

## 4. Component Library

### Button Component

**States**: Default, Hover, Active, Disabled, Loading

**Variants**:
- **Primary** (Cosmic Gold bg, DSB text)
- **Secondary** (DSB border, DSB text, transparent bg)
- **Tertiary** (Text-only, DSB text)
- **Danger** (Solar Red bg, white text)

**Sizing**: Small (12px padding), Medium (16px padding), Large (20px padding)

**Examples**:
```
[Primary Button] [Secondary Button] [Tertiary Link]
```

### Card Component

- Border radius: 8px
- Background: DSB (#0F1F3C)
- Shadow: 0 2px 8px rgba(0,0,0,0.15)
- Padding: 24px
- Border: 1px solid rgba(232,232,232,0.1)

### Input Fields

- Border radius: 4px
- Border: 1px solid #424242
- Padding: 12px 16px
- Font: Montserrat 400, 1rem
- Focus: Cosmic Gold outline (2px)

### Badge/Chip

- Border radius: 16px
- Padding: 4px 12px
- Font: Montserrat 600, 0.75rem
- Default: DSB bg, Silver text

---

## 5. Iconography

### Icon Library

- **Source**: Custom SVG + Material Design icons (subset)
- **Format**: SVG (preferred), PNG fallback
- **Sizes**: 16px, 24px, 32px, 48px (multiples of 8)
- **Stroke width**: 2px (24px+), 1.5px (16px)
- **Color**: Silver or Gold (context-dependent)

### Icon Usage Rules

- Pair icons with text labels for clarity
- Maintain 8px minimum spacing from adjacent elements
- Use consistent line weight across icon system
- Provide alt text for semantic images

### Custom Icon Set

- Spiral/helix (brand symbol)
- Space-related: planet, stars, telescope
- Navigation: menu, search, settings
- Action: play, pause, download, share
- Status: success, error, warning, info

---

## 6. Dark Mode & Themes

### Dark Theme (Default)

- Background: #0F1F3C (DSB)
- Surface: #1A2F4D
- Text primary: #E8E8E8 (Silver)
- Text secondary: #9E9E9E
- Accent: #D4AF37 (Gold)

### Light Theme (Optional)

- Background: #FFFFFF
- Surface: #F5F5F5
- Text primary: #0F1F3C (DSB)
- Text secondary: #424242
- Accent: #D4AF37 (Gold, unchanged)

### System Theme Selection

```javascript
// Detect system preference
const darkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
// Allow user override via settings
```

---

## 7. Data Visualization

### Chart Color Sequence

```
Primary: #D4AF37 (Cosmic Gold)
Secondary: #6B4DA1 (Nebula Purple)
Tertiary: #00C853 (Aurora Green)
Quaternary: #FFEB3B (Solar Yellow)
Accent: #00B0FF (Stellar Blue)
```

### Accessibility in Visualizations

- Pattern fills for color-blind users
- Distinct line styles (solid, dashed, dotted)
- High contrast ratios maintained
- Legend always visible

---

## 8. Responsive Design

### Breakpoint Strategy

| Breakpoint | Device | Grid | Gutter | Font |
|------------|--------|------|--------|------|
| 320px | Mobile | 4 cols | 8px | 0.875rem |
| 768px | Tablet | 8 cols | 16px | 1rem |
| 1024px | Desktop | 12 cols | 24px | 1.125rem |
| 1280px | Large | 12 cols | 24px | 1.25rem |

### Mobile-First Approach

- Base styles target 320px
- Progressive enhancement for larger screens
- Touch targets: minimum 44px × 44px
- Viewport: `width=device-width, initial-scale=1.0`

---

## 9. Animation & Motion

### Transition Standards

```
Fast: 150ms (UI elements, tooltips)
Normal: 300ms (page transitions, modals)
Slow: 500ms (complex animations, parallax)
Easing: cubic-bezier(0.4, 0, 0.2, 1) [Material Design standard]
```

### Animation Guidelines

- Respect `prefers-reduced-motion` for accessibility
- Avoid flashing (no >3Hz flicker)
- Micro-interactions (hover, focus) under 300ms
- Page transitions smooth but not distracting

---

## 10. Accessibility Standards

### WCAG 2.1 Level AA (Minimum)

- Contrast: 4.5:1 normal text, 3:1 large text
- Focus indicators: Clear, visible, high contrast
- Alt text: Descriptive, concise
- Keyboard navigation: Full support (Tab, Enter, Esc)
- Color: Never sole means of communication
- Motion: Respects `prefers-reduced-motion`

### Testing Checklist

- [ ] Automated accessibility audit (axe, Lighthouse)
- [ ] Manual keyboard navigation
- [ ] Screen reader testing (NVDA, JAWS, VoiceOver)
- [ ] Color contrast verification
- [ ] Form field labeling audit

---

## 11. Implementation Guidelines

### CSS Custom Properties (Variables)

```css
:root {
  --color-primary: #0F1F3C;
  --color-accent: #D4AF37;
  --color-text: #E8E8E8;
  --color-surface: #1A2F4D;
  
  --font-sans: 'Montserrat', sans-serif;
  --font-serif: 'Crimson Text', serif;
  --font-mono: 'IBM Plex Mono', monospace;
  
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
}
```

### BEM Naming Convention

```css
.button { } /* Block */
.button--primary { } /* Modifier */
.button__icon { } /* Element */
.button__icon--loading { } /* Element Modifier */
```

---

## 12. Version Control & Updates

### Current Version
- **v1.0** (2026-06-15): Initial design system launch
- Font: Montserrat + Crimson Text
- Colors: 6-color primary + extended palette
- Components: 8 core components defined
- Accessibility: WCAG 2.1 AA compliance

### Update Log
- See `/design-updates/` for version history
- Breaking changes noted with migration guide
- Deprecation notices 90 days before removal

---

**Design System Version**: 1.0  
**Last Updated**: 2026-06-15  
**Owner**: Design Team  
**Next Review**: 2026-12-15  
**Status**: Stable, production-ready
