# Astronautisté Visual System
## A Cohesive Design Language: From Playful Rockets to Prismatic Networks

**Version**: 1.0.0  
**Created**: 2026-06-15  
**Status**: Ready for Implementation  
**Audience**: Designers, developers, brand stakeholders

---

## Executive Summary

Astronautisté's visual system unites three eras of platform identity:
- **Childhood** (playful rocket ships, wonder, discovery)
- **Maturity** (Prismatic network topology, intelligence infrastructure)
- **Philosophy** (Pale Blue Dot minimalism: "we are all explorers")

The result is a **minimalist, topologically honest system** that feels simultaneously inviting to newcomers and credible to security/intelligence professionals. Every visual element descends from either **network geometry** (nodes, edges, perspective shifts) or **rocket/astronaut metaphors** (trajectories, orbits, celestial bodies).

---

## I. COLOR PALETTE

### 1. Primary Palette (Pale Blue Dot Foundation)

| Role | Name | Hex | RGB | Usage | Rationale |
|------|------|-----|-----|-------|-----------|
| **Primary** | Pale Blue | `#5B9FD4` | 91, 159, 212 | UI foreground, CTAs, hero text | Sagan's "Earth as a pale blue dot" — instantly recognizable, safe, trustworthy |
| **Primary Dark** | Deep Navy | `#1F3A52` | 31, 58, 82 | Text, backgrounds, authority | Depth without coldness; evokes both night sky and deep-water intelligence |
| **Meta Accent** | Prism Gold | `#E8B85C` | 232, 184, 92 | Highlights, network nodes, success states | Light-frequency separation; signals "intelligence refraction" |
| **Secondary** | Orbit Gray | `#4A5568` | 74, 85, 104 | Dividers, borders, tertiary text | Neutral gravity; supports primary/accent without competition |

### 2. Extended Palette (Network & Movement)

| Role | Hex | RGB | Usage | Notes |
|------|-----|-----|-------|-------|
| **Alert Red** | `#C94A4A` | 201, 74, 74 | Threat, error, halt trajectories | Warm red; feels urgent without coldness |
| **Success Green** | `#5DB85D` | 93, 184, 93 | Positive trajectory, verified nodes | Balanced saturation; not neon |
| **Warning Amber** | `#D9A84D` | 217, 168, 77 | Caution, orbit deviation | Muted warmth; aligns with gold accent family |
| **Info Cyan** | `#4DA8D9` | 77, 168, 217 | Information, data flows | Lighter pale blue; feels exploratory |
| **Orbit Black** | `#0F1419` | 15, 20, 25 | Text on light, deepest backgrounds | Near-black; prevents harsh contrast |
| **Space White** | `#F8F9FA` | 248, 249, 250 | UI backgrounds, card fills, text on dark | Off-white; reduces eye strain on extended viewing |

### 3. Semantic Color Mapping

```
🌐 Network Nodes
├─ Active Node    → Pale Blue (#5B9FD4)
├─ Verified Node  → Success Green (#5DB85D)
├─ Unknown Node   → Orbit Gray (#4A5568)
└─ Threat Node    → Alert Red (#C94A4A)

🚀 Trajectory States
├─ Ascending      → Prism Gold (#E8B85C)
├─ Stable Orbit   → Pale Blue (#5B9FD4)
├─ Descending     → Alert Red (#C94A4A)
└─ Deviation      → Warning Amber (#D9A84D)

📊 Data Visualization
├─ Primary Series → Pale Blue (#5B9FD4)
├─ Secondary      → Info Cyan (#4DA8D9)
├─ Accent         → Prism Gold (#E8B85C)
└─ Baseline       → Orbit Gray (#4A5568)
```

### 4. Dark Mode Adaptation

Dark mode uses **inverted relationships** while preserving legibility:

| Element | Light | Dark | Contrast Ratio |
|---------|-------|------|-----------------|
| Body text | Deep Navy `#1F3A52` | Space White `#F8F9FA` | 12.5:1 (AAA) |
| Primary button | Pale Blue `#5B9FD4` | Pale Blue `#5B9FD4` | 4.8:1 (AA) |
| Card background | Space White `#F8F9FA` | `#1A1E25` (darker than black) | — |
| Border | Orbit Gray `#4A5568` | `#2E3440` (lighter gray) | — |

---

## II. TYPOGRAPHY SYSTEM

### 1. Font Stack

#### Display & Headlines (Caloto + Fallbacks)

```css
/* Astronautisté Display Family */
font-family: 'Caloto', 'Segoe UI', 'Inter', -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
font-weight: 700; /* Bold for presence */
letter-spacing: -0.02em; /* Tight for sophistication */
```

**Rationale**: Caloto is a geometric sans with subtle warmth—it suggests both precision (network nodes) and approachability (rocket dreams). Falls back to modern system fonts.

#### Body & UI (Inter + Fallbacks)

```css
/* Astronautisté Text Family */
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
font-weight: 400;
letter-spacing: 0;
line-height: 1.5; /* Generous leading for readability */
```

**Rationale**: Inter's humanist forms and optical sizing ensure clarity at all scales—perfect for dense intelligence dashboards and readable at small sizes on mobile.

#### Code & Data (JetBrains Mono)

```css
/* Monospace for Intelligence Output */
font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
font-size: 0.875rem; /* Slightly smaller than body */
line-height: 1.6; /* Extra height for code blocks */
```

### 2. Type Scale

```
Titan   (4xl)   │ 3.5rem │ 56px  │ Hero titles, banner headlines
───────────────┼────────┼───────┼──────────────────────────
Hero    (3xl)   │ 2.8rem │ 44px  │ Section titles, major CTAs
───────────────┼────────┼───────┼──────────────────────────
Display (2xl)   │ 2rem   │ 32px  │ Subsection titles
───────────────┼────────┼───────┼──────────────────────────
Title   (xl)    │ 1.5rem │ 24px  │ Card titles, navigation labels
───────────────┼────────┼───────┼──────────────────────────
Subtitle(lg)    │ 1.125rem│18px  │ Card subtitles, emphasis
───────────────┼────────┼───────┼──────────────────────────
Body    (base)  │ 1rem   │ 16px  │ Paragraph text, UI labels
───────────────┼────────┼───────┼──────────────────────────
Small   (sm)    │ 0.875rem│14px  │ Captions, metadata, hints
───────────────┼────────┼───────┼──────────────────────────
Tiny    (xs)    │ 0.75rem│ 12px  │ Timestamps, data badges
```

### 3. Type Hierarchy with Examples

```
┌─────────────────────────────────────────────────────────┐
│ TITAN (3.5rem) | Caloto 700 | Letter-spacing -0.02em   │
│ Astronautisté. Explore Intelligence Networks.           │
├─────────────────────────────────────────────────────────┤
│ HERO (2.8rem) | Caloto 700 | Letter-spacing -0.02em    │
│ Network Topology. Trustworthy Insight.                  │
├─────────────────────────────────────────────────────────┤
│ DISPLAY (2rem) | Caloto 600 | Letter-spacing -0.01em   │
│ Nodes. Edges. Perspectives.                             │
├─────────────────────────────────────────────────────────┤
│ BODY (1rem) | Inter 400 | Line-height 1.5              │
│ Explore the network topology. Verify sources through    │
│ triangulation. Build confidence in your intelligence.   │
├─────────────────────────────────────────────────────────┤
│ SMALL (0.875rem) | Inter 500 | Letter-spacing 0.01em   │
│ Status: Verified • Source: 3/7 triangles • Updated 2h ago
└─────────────────────────────────────────────────────────┘
```

---

## III. ICON & SYMBOL LANGUAGE

### 1. Core Symbol Family (Deriving from Network & Rocket Metaphors)

| Symbol | Name | Base Shape | Meaning | Usage |
|--------|------|-----------|---------|-------|
| **⬢** | Node | Hexagon | Intelligence unit, verified fact | Network diagrams, entity cards, key data points |
| **→** | Edge | Arrow | Connection, trust flow, trajectory | Relationship indicators, navigation, data lineage |
| **◉** | Orbit | Concentric circles | Cycle, monitoring, continuous operation | Refresh indicators, cyclic processes, live data |
| **▲** | Trajectory | Triangle pointing up | Positive movement, ascent, discovery | Growth charts, success states, "ascending knowledge" |
| **⚡** | Pulse | Lightning bolt (geometric) | Alert, anomaly, sudden change | Real-time events, critical updates, threshold breaches |
| **◆** | Prism | Diamond (4-pointed) | Refraction, perspective shift, truth separation | Data analysis, filter operations, intelligence refinement |
| **⊡** | Gate | Double square | Verification, passage, threshold | Authentication, validation gates, checkpoints |
| **≈** | Wave | Three horizontal waves | Data flow, communication, signal | Streaming data, broadcasts, propagation |
| **⭐** | Star (filled) | 5-pointed star | Excellence, landmark, achievement | Trusted sources, high-confidence findings, key players |
| **🚀** | Rocket | Simple outline rocket | Launch, aspiration, exploration | Call-to-action, new capabilities, begin investigation |

### 2. Icon Construction Rules

**Grid**: All icons fit a 24×24 base grid (scales to 16px, 32px, 48px, 64px)

**Stroke Width**: 
- Primary icons: 1.5px stroke
- Secondary icons: 1px stroke
- Data visualization: 2px for clarity at small scale

**Corner Radius**:
- Geometric shapes: 0–2px (sharp corners emphasize precision)
- Buttons/containers: 4–8px (suggests approachability)

**Color Application**:
- Monochrome (primary task): Inherit from text color
- Semantic (status/alert): Use palette colors (green for success, red for threat)
- Network nodes: Pale Blue default, with state-based modulation

### 3. Icon Set Specification

**Essential Icons (16 total)** for MVP:

```
Navigation & UI (6):
├─ home, dashboard, settings, help, bell (notifications), menu

Network & Intelligence (6):
├─ node (verified), connection, network-map, cluster, expand, collapse

Action & Status (4):
├─ launch, filter, verify, export
```

**Extended Set (20 additional)** for Phases 2–3:
```
Data Intelligence (8):
├─ entity, relationship, timeline, heatmap, metric, anomaly, drill-down, export-report

Rocket & Exploration (6):
├─ rocket-launch, orbit, space-station, landing, trajectory, mission

Domain-Specific (6):
├─ threat, compliance, jurisdiction, source-quality, investigation, case
```

### 4. Icon Usage Patterns

#### Network Node Example
```
✓ Verified entity
Node icon + checkmark overlay + Pale Blue fill + Success Green outline
Size: 32px | Context: Entity card avatar

✗ Unverified entity
Node icon + question-mark overlay + Orbit Gray fill + Warning Amber outline
Size: 32px | Context: Unknown actor in investigation
```

#### Trajectory/Growth Chart
```
Ascending trajectory
Triangle ▲ + Pale Blue to Prism Gold gradient
Rotated 0° (straight up) for primary growth
Rotated ±15° for secondary metrics
```

---

## IV. COMPOSITION & LAYOUT RULES

### 1. Rule of Thirds for Key Content

**Application**: High-impact hero sections, dashboard layouts, investigation detail views

```
Layout Grid (16:9 aspect ratio):
┌──────────┬──────────┬──────────┐
│          │          │          │
│    1/3   │   1/3    │   1/3    │
│          │          │          │
├──────────┼──────────┼──────────┤
│          │          │          │
│    1/3   │   1/3    │   1/3    │  ← Primary call-to-action
│          │          │          │
├──────────┼──────────┼──────────┤
│          │          │          │
│    1/3   │   1/3    │   1/3    │
│          │          │          │
└──────────┴──────────┴──────────┘

Key Points (visual anchors):
⬤ = 1/3 intersection points
Position critical UI elements (hero title, CTA button, hero image) at these intersections
```

### 2. Whitespace System (8px Base Unit)

```
Spacing Scale:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
xs:  4px  │ Tight spacing within dense UI
sm:  8px  │ Element padding, small gaps
md: 16px  │ Component spacing, card margins
lg: 24px  │ Section spacing, major separations
xl: 32px  │ Page margins, wide gaps
xxl: 48px │ Hero section breathing room
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Usage Pattern (CSS):
p, li         { margin-bottom: 1rem (md) }
.card         { padding: 1.5rem (lg) }
.section      { margin: 2rem 0 (lg) }
hero-content  { margin-top: 3rem (xl) }
```

### 3. Network Grid Topology (For Data Visualization Backgrounds)

**Optional background pattern** for dashboard pages:

```
Subtle hexagonal grid (30% opacity, Orbit Gray #4A5568):
┌─────────────────────────────────────────┐
│      ╱╲      ╱╲      ╱╲      ╱╲         │
│    ╱    ╲  ╱    ╲  ╱    ╲  ╱    ╲       │
│  ╱      ╱╲╲      ╱╲╲      ╱╲╲      ╲    │  ← Pale 30% opacity
│ ╱      ╱  ╱╲╲    ╱  ╱╲╲    ╱  ╱╲╲    ╲  │
│        ╱  ╱    ╲╱    ╱    ╲╱    ╱    ╲  │
│                                        │
│ This pattern:                          │
│ • Suggests network topology            │
│ • Doesn't distract from content        │
│ • Scales responsively                  │
│ • Disappears on mobile (too busy)      │
└─────────────────────────────────────────┘
```

**SVG definition** (reusable):
```html
<defs>
  <pattern id="network-grid" x="30" y="30" patternUnits="userSpaceOnUse">
    <path d="M15,0 L30,8.66 L30,25.98 L15,34.64 L0,25.98 L0,8.66 Z" 
          fill="none" stroke="#4A5568" stroke-width="1" opacity="0.3"/>
  </pattern>
</defs>
```

### 4. Information Architecture Hierarchy

**Visual Hierarchy Depth** (Prismatic network metaphor):

```
Layer 0: Hero / Entry Point
├─ Large hero image or visualization (16:9)
├─ Titan headline (3.5rem)
└─ Subheading + CTA (Hero 2.8rem + interactive button)

Layer 1: Main Content (Primary Nodes)
├─ Section title (Display 2rem)
├─ 3-4 key cards/components (content cards with icons)
└─ Whitespace boundary (xl spacing)

Layer 2: Supporting Detail (Secondary Nodes)
├─ Subsection title (Title xl)
├─ Related content (Body text + small cards)
└─ Less visual prominence

Layer 3: Metadata & Context (Tertiary Nodes)
├─ Timestamps, source links, confidence scores (Small sm)
├─ Breadcrumbs, tags, filters
└─ Minimal color (Orbit Gray)
```

---

## V. BRAND ASSET TEMPLATES

### Template 1: Hero Poster (2560×1440 / 16:9)

**Use Case**: Landing page hero, social media banner, conference material

```
┌──────────────────────────────────────────────────┐
│                                                  │
│  ┌────────────────────────────────────────┐     │
│  │ ASTRONAUTISTÉ                          │ 1/3 │
│  │ Explore Intelligence Networks          │ ver │
│  │ Through Trusted Topology               │ tical
│  │                                        │     │
│  │ [LAUNCH INVESTIGATION] ─────────→      │     │
│  └────────────────────────────────────────┘     │
│                                                  │
│  ┌──────────────────────────────────────────┐   │
│  │   Network visualization:                  │ 2/3
│  │   ◉─→⬢─→⬢                                │ vert
│  │   │   ↓   ↓                               │
│  │   ⬢─→◉─→⬢                                │
│  │   │   ↓   ↓                               │
│  │   ⬢   ⬢   ◉                               │
│  │   (Animated circles pulsing)              │
│  └──────────────────────────────────────────┘   │
│                                                  │
└──────────────────────────────────────────────────┘

Color Palette:
├─ Background: Space White (#F8F9FA)
├─ Title: Deep Navy (#1F3A52)
├─ Subheading: Orbit Gray (#4A5568)
├─ Network: Pale Blue (#5B9FD4) + Prism Gold (#E8B85C)
└─ CTA Button: Pale Blue with 2px Deep Navy border
```

**Specifications**:
- Font: Caloto 700 (Titan) for headline
- Network graphic: SVG (scalable, light <50KB)
- Animation: Gentle node pulse (2s cycle, ease-in-out)
- Responsive breakpoints: 1920×1080 (desktop), 1280×720 (tablet), 720×405 (mobile)

---

### Template 2: Investigation Card (360×480 / 3:4)

**Use Case**: Case listing, investigation discovery, dashboard widget

```
┌──────────────────────────────────────┐
│  ◉  [Status: Verified]               │ Orbit Gray
├──────────────────────────────────────┤
│                                      │
│  NODE IDENTIFIER                     │ Title (xl)
│  Target Entity Profile               │ Subtitle (lg)
│                                      │
├──────────────────────────────────────┤
│  ⬢─→⬢─→⬢                           │ Network
│  │   ↓   ↓                           │ 8px padding
│  ⬢─→◉                                │ (Pale Blue)
│                                      │
├──────────────────────────────────────┤
│ Evidence: 7/10 sources triangulated  │ Small (sm)
│ Confidence: ████████░░ 80%           │ Orbit Gray
│ Last updated: 2h ago                 │
│                                      │
│ [INVESTIGATE]  [+ ADD TO CASE]      │ CTA buttons
└──────────────────────────────────────┘

Border: 1px Orbit Gray (#4A5568)
Shadow: 0 2px 8px rgba(15, 20, 25, 0.1)  [depth without heaviness]
Hover: +4px shadow lift, scale(1.02)
```

---

### Template 3: Mobile Hero (750×1334 / 9:16)

**Use Case**: Mobile app splash, onboarding screen, phone preview

```
┌─────────────────┐
│                 │
│  [< BACK] LOGO  │  Status bar area
│                 │
├─────────────────┤
│                 │
│    🚀           │  64px rocket icon
│  ASTRONAUTISTÉ  │  Caloto 2.8rem
│                 │  Deep Navy
│  Explore        │
│  Intelligence   │  Subtitle (lg)
│                 │  Orbit Gray
├─────────────────┤
│                 │
│  ◉─→⬢          │  Simplified network
│  ↓  ↓           │  (3 nodes only)
│  ⬢  ◉           │  Pale Blue
│                 │
├─────────────────┤
│                 │
│ [INVESTIGATE]   │  Full-width button
│                 │  CTA styling
│ Trusted by      │  Social proof
│ Security Experts│  (Small text)
│                 │
└─────────────────┘
```

**Mobile-specific adjustments**:
- Reduce hero network to 3–4 nodes (avoid clutter)
- Full-width buttons (touch-friendly, 44px min height)
- Simplified color palette (reduce cognitive load on small screen)
- Remove grid background (causes moiré patterns on mobile)

---

### Template 4: Social Media (1200×628 / 16:9 LinkedIn, 1080×1350 / 4:5 Instagram)

**LinkedIn Version (1200×628)**:
```
┌────────────────────────────────────────────────────┐
│ ◉─→⬢─→⬢    ASTRONAUTISTÉ                         │
│ │   ↓   ↓    Network Intelligence for             │
│ ⬢─→◉     Everyone                                │
│ │   ↓                                              │
│ ⬢   ◉     → Launch your investigation →           │
│                                                    │
│ Visit: astronautiste.io                           │
└────────────────────────────────────────────────────┘

Colors: Space White background, Pale Blue nodes, Deep Navy text
Font: Caloto for headline, Inter for body
CTA: Hyperlinked text at bottom
Aspect: 1200×628 (LinkedIn native)
```

**Instagram Version (1080×1350)**:
```
┌──────────────────┐
│    🚀            │  Larger rocket
│ ASTRONAUTISTÉ    │  Pale Blue
│                  │
│ Network          │  Series of 9 posts:
│ Intelligence     │  Post 1: Hero + CTA
│ for Everyone     │  Posts 2–5: Feature deep-dives
│                  │  Posts 6–8: User testimonials
│ ◉→⬢→⬢           │  Post 9: Call-to-action
│ │ ↓ ↓            │
│ ⬢→◉→⬢           │
│                  │
│ #Intelligence    │  Hashtags
│ #Security        │  (min 20 chars, max 30 chars each)
└──────────────────┘
```

---

### Template 5: Dashboard Layout (1920×1080 / 16:9)

**Use Case**: Intelligence dashboard, investigation hub, network explorer

```
┌─────────────────────────────────────────────────────────────────┐
│ Logo  [Dashboard]  [Investigations]  [Network]  [Settings]      │ Navigation bar
├─────────────────────────────────────────────────────────────────┤ (Deep Navy bg)
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐   │
│  │  Quick Stats    │  │  Active Cases   │  │  Real-time   │   │
│  │  ════════════   │  │  ════════════   │  │  Network     │   │
│  │                 │  │                 │  │              │   │ 3-column layout
│  │ 147 Verified    │  │ 8 in progress   │  │  ◉─→⬢─→⬢    │   │ (1/3 each)
│  │ 23 Anomalies    │  │ 2 paused        │  │  │   ↓   ↓    │   │
│  │ 92% Confidence  │  │ 12 completed    │  │  ⬢─→◉      │   │
│  └─────────────────┘  └─────────────────┘  └──────────────┘   │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ Investigation Log                                         │ │
│  │ ══════════════════════════════════════════════════════   │ │ Full-width
│  │ 12:45 — Node A verified against source B (90% match)    │ │ card below
│  │ 12:30 — Anomaly detected: unusual connection pattern   │ │
│  │ 12:15 — Case #847 advanced to high confidence           │ │
│  │ 12:00 — Incoming data stream: 1,247 new entities       │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

Layout grid:
├─ Header: 64px (navigation + branding)
├─ Content: Remaining height
│  ├─ 3 cards (md spacing between)
│  └─ Full-width log table (lg spacing above)
└─ Sidebar: Optional (collapsed on mobile)

Background: Space White with subtle network grid (30% opacity)
Card shadows: 0 2px 8px rgba(15, 20, 25, 0.08)
```

---

## VI. DESIGN DO'S & DON'Ts

### DO's ✓

1. **DO use the pale blue + navy duet for trust-building**
   - Primary copy: Deep Navy on Space White
   - Interactive elements: Pale Blue with Navy accents
   - Inspires both confidence ("navy = authority") and approachability ("pale blue = open sky")

2. **DO nest icons within hexagons for network contexts**
   - Makes abstract data feel tangible (a "node" has structure)
   - Hexagons naturally tile (visual coherence in network diagrams)
   - 24px base = scales cleanly to 32, 48, 64px

3. **DO leverage rule-of-thirds for hero layouts**
   - Places call-to-action buttons at 2/3 vertical intersection
   - Centers images at 1/3 intersection (focal depth)
   - Feels instinctively balanced without being rigid

4. **DO employ consistent whitespace in dense dashboards**
   - 8px/16px/24px rhythm prevents visual chaos
   - Intelligence professionals scan faster when breathing room exists
   - Guides the eye naturally through hierarchy

5. **DO use rocket/star iconography sparingly, at moments of aspiration**
   - "Launch Investigation" CTA button
   - "Start New Case" entry point
   - "Explore Network" navigation
   - Too much = cartoonish; too little = cold

### DON'Ts ✗

1. **DON'T mix Pale Blue + Prism Gold for body copy**
   - Both are mid-saturation; together they vibrate
   - Use gold sparingly: highlights, accent nodes, success states
   - Gold should occupy <5% of visual weight

2. **DON'T force the hexagon grid into every background**
   - Busy dashboards need it removed entirely
   - Mobile screens: never use (causes moiré + poor readability)
   - Limit to "serene" pages (landing, onboarding, hero sections)

3. **DON'T scale icons linearly below 16px**
   - 16px is the floor; below that, switch to simpler glyphs or text labels
   - Stroke weight should thicken at small scales (1px → 1.5px at 12px icon size)
   - Never use anti-aliasing at <14px icon sizes

4. **DON'T stack more than 3 hierarchy levels in navigation**
   - Astronautisté = exploration, not bureaucracy
   - If you need 4+ levels, you've missed a domain boundary
   - Collapse related items into expandable groups (e.g., "Intelligence" > "OSINT Tools")

5. **DON'T use the full 10-color palette in one mockup**
   - Stick to: Deep Navy + Space White + Pale Blue (core)
   - Add max 2 of: Prism Gold, Orbit Gray, semantic colors (alert/success/warning)
   - Fewer colors = stronger identity, faster decisions

---

## VII. FIGMA/SKETCH EXPORT STRUCTURE

### Directory Organization

```
astronautiste-design-system/
├── 📁 1_Brand_Guidelines/
│   ├─ Logo_Lockup.fig
│   ├─ Color_Palette.fig
│   ├─ Typography_Scale.fig
│   └─ Icon_Library.fig
│
├── 📁 2_Component_Library/
│   ├─ Buttons.fig (primary, secondary, tertiary, sizes: sm/md/lg)
│   ├─ Cards.fig (entity, investigation, data, network node)
│   ├─ Navigation.fig (breadcrumbs, tabs, sidebar, top-bar)
│   ├─ Forms.fig (text input, select, textarea, validation states)
│   ├─ Tables.fig (sortable, filterable, dense/spacious modes)
│   └─ Modals.fig (alert, form, confirmation, sizes)
│
├── 📁 3_Templates/
│   ├─ Landing_Page_Hero.fig (1x desktop, 1x mobile variant)
│   ├─ Investigation_Card.fig (3:4 aspect, hover states)
│   ├─ Mobile_Onboarding.fig (9:16, 3 screens)
│   ├─ Dashboard_Layout.fig (16:9, 3-column grid)
│   ├─ Social_Media_Templates.fig (LinkedIn 16:9, Instagram 4:5)
│   └─ Poster_Print.fig (2560×1440, print-ready)
│
├── 📁 4_Utilities/
│   ├─ Spacing_Grid.fig (8px base, visual ruler)
│   ├─ Network_SVG_Patterns.fig (hexagonal grid, node pack)
│   ├─ Typography_Styles.fig (Caloto scale, Inter scale, Mono scale)
│   └─ Color_Mixer.fig (semantic mappings, state variations)
│
├── 📁 5_Exports/
│   ├─ SVG/
│   │  ├─ Icons/
│   │  │  ├─ node.svg
│   │  │  ├─ edge.svg
│   │  │  ├─ orbit.svg
│   │  │  ├─ trajectory.svg
│   │  │  ├─ rocket.svg
│   │  │  └─ [16 more core icons]
│   │  └─ Patterns/
│   │     ├─ network-grid-light.svg
│   │     ├─ network-grid-dark.svg
│   │     ├─ hexagon-pack.svg
│   │     └─ trajectory-arc.svg
│   │
│   ├─ CSS/
│   │  ├─ astronautiste-colors.css
│   │  ├─ astronautiste-typography.css
│   │  ├─ astronautiste-spacing.css
│   │  └─ astronautiste-components.css (button, card, etc.)
│   │
│   ├─ Figma_Libraries.fig
│   │  (Shared components library, version-controlled)
│   │
│   └─ Design_Tokens.json
│      (For design-to-dev handoff: colors, sizes, radii, shadows)
│
└── 📄 README.md (quickstart, versioning, export dates)
```

### Figma File Structure (Per File)

Each .fig file uses this frame hierarchy:

```
Figma File: Buttons.fig
├─ 📑 [REFERENCE] Colors & Styles
│  └─ Visual legend of all colors, shadows, text styles used
│
├─ 📑 PRIMARY BUTTON
│  ├─ Frame: [Default]
│  │  ├─ Component: Button/Primary/Medium
│  │  └─ Label: "Launch Investigation"
│  ├─ Frame: [Hover]
│  │  └─ Component: Button/Primary/Medium (shadow lifted, scale 1.02)
│  ├─ Frame: [Disabled]
│  │  └─ Component: Button/Primary/Medium (50% opacity, no interaction)
│  └─ Frame: [States Grid] (3×2 showing all size combos)
│
├─ 📑 SECONDARY BUTTON
│  ├─ [Default], [Hover], [Disabled], [States Grid]
│
├─ 📑 ICON BUTTON
│  └─ [Variants for each of 16 icons, 3 sizes each]
│
└─ 📑 USAGE EXAMPLES
   ├─ Frame: "Form with Primary Button"
   ├─ Frame: "Card with Secondary Button"
   └─ Frame: "Modal with Icon Buttons"
```

### Design Tokens Export (JSON)

```json
{
  "astronautiste": {
    "colors": {
      "primary": {
        "pale-blue": { "value": "#5B9FD4", "rgb": "91, 159, 212" },
        "deep-navy": { "value": "#1F3A52", "rgb": "31, 58, 82" },
        "prism-gold": { "value": "#E8B85C", "rgb": "232, 184, 92" }
      },
      "neutral": {
        "orbit-gray": { "value": "#4A5568", "rgb": "74, 85, 104" },
        "space-white": { "value": "#F8F9FA", "rgb": "248, 249, 250" },
        "orbit-black": { "value": "#0F1419", "rgb": "15, 20, 25" }
      },
      "semantic": {
        "success": { "value": "#5DB85D", "rgb": "93, 184, 93" },
        "alert": { "value": "#C94A4A", "rgb": "201, 74, 74" },
        "warning": { "value": "#D9A84D", "rgb": "217, 168, 77" },
        "info": { "value": "#4DA8D9", "rgb": "77, 168, 217" }
      }
    },
    "typography": {
      "font-families": {
        "display": "Caloto",
        "body": "Inter",
        "mono": "JetBrains Mono"
      },
      "scale": {
        "titan": { "size": "3.5rem", "weight": 700, "line-height": 1.1 },
        "hero": { "size": "2.8rem", "weight": 700, "line-height": 1.2 },
        "display": { "size": "2rem", "weight": 600, "line-height": 1.3 },
        "body": { "size": "1rem", "weight": 400, "line-height": 1.5 }
      }
    },
    "spacing": {
      "xs": "4px",
      "sm": "8px",
      "md": "16px",
      "lg": "24px",
      "xl": "32px",
      "xxl": "48px"
    },
    "radius": {
      "sharp": "0px",
      "tight": "2px",
      "soft": "4px",
      "rounded": "8px"
    },
    "shadow": {
      "subtle": "0 2px 8px rgba(15, 20, 25, 0.08)",
      "medium": "0 4px 16px rgba(15, 20, 25, 0.12)",
      "strong": "0 8px 32px rgba(15, 20, 25, 0.16)"
    }
  }
}
```

### Version Control & Handoff

**Figma Shared Library Setup**:
```
Main Library File: astronautiste-master.fig
├─ All components (buttons, cards, nav, forms, etc.)
├─ Published to team workspace
├─ Versioning: Major.Minor (e.g., 1.0, 1.1, 2.0)
└─ Changelog in file description + published release notes

Consuming Files (Design Projects):
├─ Link to: astronautiste-master.fig
├─ Inherit components automatically
├─ Local overrides tracked (yellow warning badge)
└─ Update all via "Update components" button
```

**Export Pipeline** (Figma → Code):

```bash
# Automated SVG export (via Figma API or plugin)
npx @figma/export --file-id <ID> --format=svg --out=src/icons/

# Design tokens export (via Figma Tokens plugin)
npm run export:design-tokens > src/design-tokens.json

# CSS generation (from tokens)
npm run build:css --tokens=src/design-tokens.json --out=src/astronautiste.css
```

---

## VIII. IMPLEMENTATION ROADMAP

### Phase 1: Foundations (Weeks 1–2)

- [ ] Create color palette & typography files (Figma)
- [ ] Define 16-icon core set + export as SVG
- [ ] Build Figma component library (buttons, cards, nav)
- [ ] Export design tokens (JSON) for dev team
- [ ] Create CSS variables stylesheet

### Phase 2: Templates (Weeks 3–4)

- [ ] Hero poster template (desktop + mobile variants)
- [ ] Investigation card template + hover states
- [ ] Dashboard layout template (16:9)
- [ ] Social media templates (LinkedIn, Instagram)
- [ ] Publish Figma shared library

### Phase 3: Refinement (Weeks 5–6)

- [ ] Extended icon set (20 additional icons)
- [ ] Dark mode refinement + contrast testing
- [ ] Brand guidelines document (PDF for external use)
- [ ] Developer handoff guide (CSS + component mapping)
- [ ] User testing on key templates

### Phase 4: Ecosystem (Weeks 7+)

- [ ] Implement in production (prismatic_web)
- [ ] Storybook component library (interactive docs)
- [ ] Animation specifications (Lottie files for key interactions)
- [ ] Accessibility audit (WCAG 2.1 AAA for core components)
- [ ] Launch brand voice & tone guide (companion to visual system)

---

## IX. QUICK REFERENCE CHEAT SHEET

### Brand Essence
- **Motto**: "Explore Intelligence Networks. Trustworthy Topology."
- **Core Colors**: Pale Blue (#5B9FD4) + Deep Navy (#1F3A52)
- **Typography**: Caloto (headlines) + Inter (body) + JetBrains Mono (code)
- **Spacing**: 8px base unit (xs/sm/md/lg/xl/xxl)
- **Grid**: 3-column for desktop, 1-column for mobile, always 16:9 heroes

### Icon System
- **Core**: 16 essential icons (node, edge, orbit, trajectory, etc.)
- **Grid**: 24px base, scales to 16/32/48/64px
- **Stroke**: 1.5px primary, 1px secondary, 2px data viz

### Semantic Colors
| State | Color | Hex |
|-------|-------|-----|
| Success | Green | #5DB85D |
| Alert | Red | #C94A4A |
| Warning | Amber | #D9A84D |
| Info | Cyan | #4DA8D9 |

### Type Hierarchy
| Role | Size | Font | Weight |
|------|------|------|--------|
| Headline | 3.5rem | Caloto | 700 |
| Subhead | 2rem | Caloto | 600 |
| Body | 1rem | Inter | 400 |
| Caption | 0.875rem | Inter | 500 |

---

## X. APPENDIX: DESIGN INSPIRATION SOURCES

**Visual References**:
- Carl Sagan's "Pale Blue Dot" photography (NASA) — minimalism, perspective
- Network topology diagrams from intelligence agencies (geometry, clarity)
- Modern rocket design (SpaceX, Blue Origin) — sleek, aspirational
- Swiss design tradition — grid-based, functional, elegant
- Japanese minimalism — empty space as design element

**Color Psychology**:
- Pale Blue: Trust, calm, exploration, sky (positive associations)
- Deep Navy: Authority, stability, depth, intelligence
- Prism Gold: Refraction, separation, precision, value
- Orbit Gray: Neutrality, balance, cosmic void

---

## Document Metadata

**Version**: 1.0.0  
**Date**: 2026-06-15  
**Author**: Design System Team  
**Status**: Ready for Implementation  
**Next Review**: 2026-08-15  
**Maintainer**: design@astronautiste.io

---

**Astronautisté Visual System** © 2026. All rights reserved. For internal use and licensed partners only.
