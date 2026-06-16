{% raw %}
# Astronautisté Visual System — Implementation Guide
## For Designers, Developers & Product Managers

**Version**: 1.0.0  
**Last Updated**: 2026-06-15  
**Status**: Ready to Build  

---

## TABLE OF CONTENTS

1. [Quick Start for Designers](#quick-start-for-designers)
2. [Quick Start for Developers](#quick-start-for-developers)
3. [Brand Application Checklist](#brand-application-checklist)
4. [Common Patterns Library](#common-patterns-library)
5. [Figma-to-Code Workflow](#figma-to-code-workflow)
6. [Accessibility & Performance](#accessibility--performance)
7. [FAQ & Troubleshooting](#faq--troubleshooting)

---

## QUICK START FOR DESIGNERS

### Step 1: Set Up Your Figma File

**Prerequisites**:
- Figma account (team plan recommended)
- Install fonts: Caloto, Inter, JetBrains Mono
- Download color palette reference from main Visual System doc

**Setup Checklist**:

```
☐ Create new Figma team file: "Astronautisté Design System"
☐ Set page grid to 8px (helps with spacing consistency)
☐ Create page: "[REFERENCE] Brand Guidelines"
│  ├─ Color palette visual (all 10 colors)
│  ├─ Typography scale (Titan → Tiny)
│  ├─ Icon key (16 core symbols)
│  └─ Spacing ruler (xs through xxl)
│
☐ Create page: "Components"
│  ├─ Buttons (primary, secondary, tertiary)
│  ├─ Cards (entity, investigation, network)
│  ├─ Navigation (breadcrumbs, tabs, sidebar)
│  ├─ Forms (text, select, textarea)
│  ├─ Tables (with sort/filter states)
│  └─ Modals (alert, form, confirmation)
│
☐ Create page: "Templates"
│  ├─ Landing hero (16:9 desktop + mobile)
│  ├─ Investigation card (3:4)
│  ├─ Dashboard layout (16:9)
│  └─ Social media (1:1 square, 16:9 wide, 4:5 portrait)
│
☐ Create Figma shared library (for reuse across projects)
│  ├─ Publish components
│  ├─ Set up versioning (e.g., "Astronautisté v1.0")
│  └─ Document in team wiki
```

### Step 2: Build Component Library

**For each component**, follow this structure:

```
Frame: "Button / Primary"
├─ Component: "Button/Primary/Medium" [Main component]
├─ Component: "Button/Primary/Small" [Variant: size]
├─ Component: "Button/Primary/Large" [Variant: size]
├─ Component: "Button/Primary/Medium:Hover" [Variant: state]
├─ Component: "Button/Primary/Medium:Disabled" [Variant: state]
└─ Annotations:
   ├─ "Padding: 12px 16px (sm spacing)"
   ├─ "Border radius: 4px (soft)"
   ├─ "Font: Inter 500 (16px body-sized)"
   ├─ "Shadow on hover: subtle (0 2px 8px)"
   └─ "Icon slot: 16px square left-aligned"
```

**Why this structure?**
- Variants allow developers to understand all states at a glance
- Annotations bridge design intent to code
- Consistency across all components

### Step 3: Create Design Tokens Document

**Export or manually create** a tokens file that mirrors this structure:

```json
{
  "color": {
    "primary": {
      "pale-blue": "#5B9FD4",
      "deep-navy": "#1F3A52"
    },
    "semantic": {
      "success": "#5DB85D",
      "error": "#C94A4A"
    }
  },
  "typography": {
    "headline": {
      "family": "Caloto",
      "size": "3.5rem",
      "weight": 700
    }
  },
  "spacing": {
    "sm": "8px",
    "md": "16px"
  }
}
```

**Share with developers** via:
- Figma Tokens plugin (auto-sync to code)
- Design tokens package (.json file in repo)
- CSS variables stylesheet

### Step 4: Document Patterns & Usage

For each major pattern, create a "Usage Guide" frame:

```
Frame: "Usage Guide: Node in Network"
├─ Title: "How to Use: Network Node Icon"
├─ Example 1: "Verified Entity"
│  ├─ Visual: ⬢ + checkmark + Pale Blue
│  └─ Note: "Use in entity cards, success states"
├─ Example 2: "Unknown Entity"
│  ├─ Visual: ⬢ + question + Orbit Gray
│  └─ Note: "Use when confidence < 50%"
└─ Don'ts:
   ├─ "DON'T use red + node together (confusing)"
   ├─ "DON'T scale below 24px (loses detail)"
   └─ "DON'T add shadows to nodes (breaks clarity)"
```

### Step 5: Prepare for Handoff to Developers

**Before passing to devs**, complete:

```
Handoff Checklist:
☐ All components published to Figma shared library
☐ All states documented (default, hover, active, disabled, error, etc.)
☐ Design tokens exported as JSON
☐ CSS variables generated & added to repo
☐ Icon SVGs exported (one per file)
☐ README created in Figma with:
  ├─ Component naming convention
  ├─ How to update library
  ├─ Known limitations
  └─ Contact info for design questions
☐ Storybook stories auto-generated (via Figma plugin or manual)
☐ Color contrast ratios verified (WCAG AAA for all text/button combos)
```

---

## QUICK START FOR DEVELOPERS

### Step 1: Clone Design Tokens

**Install** the design tokens package in your project:

```bash
npm install @astronautiste/design-tokens
# or
yarn add @astronautiste/design-tokens
```

**Import in your CSS entrypoint**:

```css
/* src/styles/index.css */
@import '@astronautiste/design-tokens/astronautiste.css';

/* Now all CSS variables are available */
:root {
  var(--color-primary-pale-blue): #5B9FD4;
  var(--color-primary-deep-navy): #1F3A52;
  var(--spacing-sm): 8px;
  var(--spacing-md): 16px;
}
```

**For TypeScript projects**, import types:

```typescript
import { AstronautisteTokens } from '@astronautiste/design-tokens';

const buttonColor: AstronautisteTokens['color']['primary'] = 'pale-blue';
```

### Step 2: Set Up Component Patterns

**Create a components directory structure**:

```
src/components/
├─ Button.tsx
│  ├─ PrimaryButton.tsx
│  ├─ SecondaryButton.tsx
│  └─ __tests__/
│     └─ Button.test.tsx
│
├─ Card/
│  ├─ EntityCard.tsx
│  ├─ InvestigationCard.tsx
│  ├─ NetworkCard.tsx
│  └─ Card.module.css
│
├─ Icons/
│  ├─ Node.tsx (SVG imported, composable)
│  ├─ Edge.tsx
│  ├─ Orbit.tsx
│  ├─ icons.types.ts
│  └─ index.ts
│
├─ Navigation/
│  ├─ Breadcrumbs.tsx
│  ├─ Sidebar.tsx
│  └─ Navbar.tsx
│
├─ Theme.tsx (Provide Astronautiste tokens to entire app)
└─ index.ts (Main export file)
```

### Step 3: Build Button Component

**Example: PrimaryButton.tsx**

```typescript
import React from 'react';
import styles from './Button.module.css';

interface PrimaryButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  size?: 'sm' | 'md' | 'lg';
  icon?: React.ReactNode;
  className?: string;
}

export const PrimaryButton: React.FC<PrimaryButtonProps> = ({
  children,
  onClick,
  disabled = false,
  size = 'md',
  icon,
  className,
}) => {
  return (
    <button
      className={`
        ${styles.button}
        ${styles[`button--primary`]}
        ${styles[`button--${size}`]}
        ${disabled ? styles['button--disabled'] : ''}
        ${className}
      `}
      onClick={onClick}
      disabled={disabled}
      aria-label={typeof children === 'string' ? children : undefined}
    >
      {icon && <span className={styles['button__icon']}>{icon}</span>}
      <span className={styles['button__text']}>{children}</span>
    </button>
  );
};
```

**Corresponding CSS (Button.module.css)**:

```css
.button {
  /* Base styles */
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--spacing-sm);
  
  font-family: var(--font-body);
  font-weight: 500;
  border: none;
  cursor: pointer;
  transition: all 200ms ease-in-out;
  border-radius: var(--radius-soft);
  
  /* Accessibility */
  &:focus-visible {
    outline: 2px solid var(--color-primary-pale-blue);
    outline-offset: 2px;
  }
}

.button--primary {
  background-color: var(--color-primary-pale-blue);
  color: white;
  box-shadow: var(--shadow-subtle);
  
  &:hover:not(:disabled) {
    box-shadow: var(--shadow-medium);
    transform: scale(1.02);
  }
  
  &:active:not(:disabled) {
    box-shadow: var(--shadow-subtle);
    transform: scale(0.98);
  }
}

.button--disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Size variants */
.button--sm {
  padding: 8px 12px;
  font-size: 0.875rem;
}

.button--md {
  padding: 12px 16px;
  font-size: 1rem;
}

.button--lg {
  padding: 16px 24px;
  font-size: 1.125rem;
}

.button__icon {
  display: flex;
  align-items: center;
  width: 1em;
  height: 1em;
}
```

### Step 4: Integrate Icons

**Export SVGs from Figma** → Create React components:

```typescript
// src/components/Icons/Node.tsx
import React from 'react';

interface NodeIconProps {
  size?: number;
  color?: string;
  state?: 'active' | 'verified' | 'unknown' | 'threat';
}

export const NodeIcon: React.FC<NodeIconProps> = ({
  size = 24,
  color = 'currentColor',
  state = 'active',
}) => {
  const colorMap = {
    active: '#5B9FD4',    // Pale Blue
    verified: '#5DB85D',  // Success Green
    unknown: '#4A5568',   // Orbit Gray
    threat: '#C94A4A',    // Alert Red
  };

  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke={colorMap[state] || color}
      strokeWidth={1.5}
      strokeLinecap="round"
      strokeLinejoin="round"
      role="img"
      aria-label={`Node icon: ${state}`}
    >
      <polygon points="12 2 20 6 20 18 12 22 4 18 4 6 12 2" />
    </svg>
  );
};
```

**Use throughout app**:

```tsx
<NodeIcon size={32} state="verified" />
```

### Step 5: Create Storybook Stories

**Document component behavior in Storybook**:

```typescript
// src/components/Button.stories.tsx
import { StoryFn, Meta } from '@storybook/react';
import { PrimaryButton } from './Button';
import { RocketIcon } from './Icons';

export default {
  title: 'Components/Button/Primary',
  component: PrimaryButton,
  args: {
    children: 'Launch Investigation',
  },
} as Meta;

const Template: StoryFn<typeof PrimaryButton> = (args) => (
  <PrimaryButton {...args} />
);

export const Default = Template.bind({});

export const WithIcon = Template.bind({});
WithIcon.args = {
  icon: <RocketIcon size={16} />,
};

export const Large = Template.bind({});
Large.args = {
  size: 'lg',
};

export const Disabled = Template.bind({});
Disabled.args = {
  disabled: true,
};

export const AllSizes = () => (
  <div style={{ display: 'flex', gap: '16px' }}>
    <PrimaryButton size="sm">Small</PrimaryButton>
    <PrimaryButton size="md">Medium</PrimaryButton>
    <PrimaryButton size="lg">Large</PrimaryButton>
  </div>
);
```

---

## BRAND APPLICATION CHECKLIST

### For Landing Page / Public Website

```
☐ Color Palette
  ☐ Hero section: Space White background with Pale Blue accents
  ☐ Navigation bar: Deep Navy background with Space White text
  ☐ CTA buttons: Pale Blue fill, 2px Deep Navy border (inverted on navy bg)
  ☐ Accent highlights: Prism Gold (max 5% of visual weight)

☐ Typography
  ☐ H1 (Hero headline): Caloto 700, 3.5rem, Deep Navy
  ☐ H2 (Section titles): Caloto 600, 2rem, Deep Navy
  ☐ Body: Inter 400, 1rem, Deep Navy on Space White or white on Deep Navy
  ☐ Links: Pale Blue, underlined on hover

☐ Icons
  ☐ Navigation icons: 24px, Orbit Gray (inherit hover color to Pale Blue)
  ☐ Feature cards: 48px icons (node, rocket, network) in Pale Blue
  ☐ Status badges: 16px icons (✓, ⚠️, ✗) with semantic colors

☐ Spacing & Layout
  ☐ Hero section: xl spacing (32px) top/bottom
  ☐ Card grid: md spacing (16px) between cards
  ☐ Section padding: lg spacing (24px) horizontal on desktop
  ☐ Mobile: Reduce all spacings by 50% (8px → 4px, 16px → 8px)

☐ Imagery
  ☐ Hero image: Network diagram or rocket illustration (optional)
  ☐ Background: No pattern on public web (use for internal dashboards only)
  ☐ Aspect ratio: 16:9 for hero sections, 3:4 for card images

☐ Accessibility
  ☐ Color contrast: 4.5:1 minimum for text/background
  ☐ Focus states: 2px solid outline with 2px offset
  ☐ Icon alt text: All images have descriptive alt attributes
  ☐ Keyboard nav: All interactive elements reachable via Tab key
```

### For Intelligence Dashboard (Internal)

```
☐ Color Palette
  ☐ Background: Space White with subtle network grid (30% opacity Orbit Gray)
  ☐ Cards: White fill with 1px Orbit Gray border
  ☐ Data viz: Pale Blue (primary), Info Cyan (secondary), Prism Gold (accent)
  ☐ Status indicators: Success Green, Alert Red, Warning Amber, Info Cyan

☐ Navigation
  ☐ Top bar: Deep Navy with Space White text + Pale Blue hover
  ☐ Sidebar: Space White with Deep Navy text, active item: Pale Blue background
  ☐ Breadcrumbs: Orbit Gray text with Pale Blue separators

☐ Data Cards
  ☐ Entity card: White background, node icon (32px) + title + status
  ☐ Investigation card: White background + simplified network diagram
  ☐ Metric card: Icon + number + trend indicator (↑↓→)

☐ Network Visualization
  ☐ Nodes: Hexagon with color coding (verified → green, unknown → gray, threat → red)
  ☐ Edges: 2px stroke, Orbit Gray color, opacity 60%
  ☐ Labels: Small text (sm 0.875rem), Orbit Gray, positioned above node

☐ Tables
  ☐ Header row: Deep Navy background, Space White text, sorted column highlighted in Pale Blue
  ☐ Rows: Alternating white/light gray (F8F9FA) backgrounds
  ☐ Hover: +4px box shadow, cursor pointer
  ☐ Sort arrows: 16px icons in header, Pale Blue when active

☐ Forms
  ☐ Text input: 1px Orbit Gray border, blue outline on focus
  ☐ Labels: Body weight 500, Deep Navy, above input (not floating)
  ☐ Error state: Alert Red border + error icon + small helper text (sm)
  ☐ Success state: Success Green checkmark inside input

☐ Performance
  ☐ No grid background on mobile (removes moiré effect)
  ☐ Simplify network diagrams on tablet/mobile (3–4 nodes max)
  ☐ Reduce card shadows on low-end devices (box-shadow: none; on .no-gpu class)
```

### For Mobile App (iOS/Android)

```
☐ Color Palette
  ☐ Same primary colors (Pale Blue + Deep Navy)
  ☐ Background: Space White (system light mode) or #1A1E25 (system dark mode)
  ☐ Ensure 12:1 contrast on smaller type sizes

☐ Typography
  ☐ Reduce by 10% from desktop (e.g., H1: 3rem instead of 3.5rem)
  ☐ Increase line-height by 10% (1.5 → 1.65) for readability at arm's length

☐ Touch Targets
  ☐ All buttons: 44px minimum height (iOS HIG)
  ☐ Tap area: 44×44px minimum
  ☐ Spacing between tappables: 8px minimum

☐ Layout
  ☐ Single column only (no multi-column grids on phones)
  ☐ Full-width cards with md spacing (16px margin sides)
  ☐ Bottom nav or hamburger menu (no top-heavy navigation)

☐ Icons
  ☐ Scale to 24px or 32px (never <16px on mobile)
  ☐ Use semantic colors (not monochrome) for status differentiation

☐ Network Diagrams
  ☐ Remove grid background entirely
  ☐ Simplify to 3 nodes maximum (scrollable for exploration)
  ☐ Use Pan/Zoom controls (pinch-to-zoom, double-tap to zoom-in)

☐ Dark Mode
  ☐ Invert colors programmatically (prefers-color-scheme: dark)
  ☐ Test Pale Blue + Deep Navy on dark background (ensure sufficient contrast)
```

---

## COMMON PATTERNS LIBRARY

### Pattern 1: Entity Card (Reusable)

**Purpose**: Display a single entity (person, company, domain) with quick stats

**Visual Structure**:
```
┌──────────────────────────────┐
│ ⬢ [Status Badge]             │  Orbit Gray top bar
├──────────────────────────────┤
│ ENTITY NAME                  │  Title (xl)
│ Role / Type                  │  Subtitle (lg, Orbit Gray)
├──────────────────────────────┤
│ ▪️ 7/10 sources verified     │  Small text (sm)
│ ▪️ Confidence: 85%           │  Confidence bar
│ ▪️ Last updated: 2h ago      │
├──────────────────────────────┤
│ [Investigate]  [Save]        │  CTA buttons
└──────────────────────────────┘
```

**Implementation** (React):

```tsx
interface EntityCardProps {
  name: string;
  role: string;
  status: 'verified' | 'unknown' | 'threat';
  confidence: number;
  sourceCount: number;
  onInvestigate: () => void;
}

export const EntityCard: React.FC<EntityCardProps> = ({
  name,
  role,
  status,
  confidence,
  sourceCount,
  onInvestigate,
}) => {
  const statusColors = {
    verified: '#5DB85D',
    unknown: '#4A5568',
    threat: '#C94A4A',
  };

  return (
    <div className={styles.card}>
      <div className={styles.header} style={{ borderLeftColor: statusColors[status] }}>
        <NodeIcon size={32} state={status} />
        <span className={styles.badge}>{status.toUpperCase()}</span>
      </div>

      <div className={styles.content}>
        <h3 className={styles.title}>{name}</h3>
        <p className={styles.subtitle}>{role}</p>

        <div className={styles.stats}>
          <p>{sourceCount}/10 sources verified</p>
          <div className={styles.confidenceBar}>
            <div
              className={styles.confidenceFill}
              style={{
                width: `${confidence}%`,
                backgroundColor: confidence > 75 ? '#5DB85D' : '#D9A84D',
              }}
            />
          </div>
          <p className={styles.small}>Confidence: {confidence}%</p>
        </div>

        <div className={styles.actions}>
          <PrimaryButton onClick={onInvestigate} size="sm">
            Investigate
          </PrimaryButton>
          <SecondaryButton size="sm">Save</SecondaryButton>
        </div>
      </div>
    </div>
  );
};
```

### Pattern 2: Network Node (SVG Component)

**Purpose**: Render interactive network topology with state-aware styling

**Implementation**:

```tsx
interface NetworkNodeProps {
  x: number;
  y: number;
  id: string;
  state: 'active' | 'verified' | 'unknown' | 'threat';
  label?: string;
  onNodeClick?: (id: string) => void;
  size?: number;
}

export const NetworkNode: React.FC<NetworkNodeProps> = ({
  x,
  y,
  id,
  state,
  label,
  onNodeClick,
  size = 24,
}) => {
  const colorMap = {
    active: '#5B9FD4',
    verified: '#5DB85D',
    unknown: '#4A5568',
    threat: '#C94A4A',
  };

  return (
    <g
      transform={`translate(${x}, ${y})`}
      onClick={() => onNodeClick?.(id)}
      style={{ cursor: 'pointer' }}
    >
      {/* Glow effect on hover */}
      <circle
        r={size / 2 + 4}
        fill={colorMap[state]}
        opacity="0.1"
        className={styles.glow}
      />

      {/* Main hexagon */}
      <polygon
        points={`${size / 2},0 ${size / 2 * 1.5},${size / 4} ${size / 2 * 1.5},${size * 0.75} ${size / 2},${size} 0,${size * 0.75} 0,${size / 4}`}
        fill={colorMap[state]}
        stroke={colorMap[state]}
        strokeWidth="1.5"
      />

      {/* Label below */}
      {label && (
        <text
          y={size + 16}
          textAnchor="middle"
          fontSize="12"
          fill="#4A5568"
          fontFamily="Inter, sans-serif"
        >
          {label.substring(0, 12)}
        </text>
      )}
    </g>
  );
};
```

### Pattern 3: Confidence Indicator (Badge)

**Purpose**: Show source triangulation and confidence level at a glance

**Visual**:
```
⬢ ⬢ ⬢      ✓ ✓ ✗      87%
3/7 verified sources    Confidence
```

**Implementation**:

```tsx
interface ConfidenceIndicatorProps {
  verified: number;
  total: number;
  confidencePercentage: number;
}

export const ConfidenceIndicator: React.FC<ConfidenceIndicatorProps> = ({
  verified,
  total,
  confidencePercentage,
}) => {
  const sourceIcons = Array.from({ length: total }, (_, i) => (
    <NodeIcon
      key={i}
      size={16}
      state={i < verified ? 'verified' : 'unknown'}
    />
  ));

  return (
    <div className={styles.indicator}>
      <div className={styles.sources}>{sourceIcons}</div>
      <span className={styles.label}>
        {verified}/{total} verified
      </span>
      <div className={styles.percentage}>
        {confidencePercentage}%
      </div>
    </div>
  );
};
```

---

## FIGMA-TO-CODE WORKFLOW

### Automated Workflow (Ideal)

**Setup**:
1. Install Figma Tokens plugin in Figma
2. Export tokens to JSON
3. Use Tokens Studio to sync to GitHub
4. Auto-generate CSS/JS from tokens

**Flow**:
```
Figma (update design)
  ↓
Figma Tokens plugin (auto-export)
  ↓
GitHub (PR created automatically)
  ↓
CI/CD pipeline (validate, generate CSS)
  ↓
npm publish (design-tokens package)
  ↓
Your app (update via npm)
```

**GitHub Actions example**:

```yaml
name: Sync Figma Tokens
on:
  workflow_dispatch:

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: chgibb/figma-tokens-action@v1
        with:
          figma-token: ${{ secrets.FIGMA_API_TOKEN }}
          figma-file-id: ${{ secrets.FIGMA_FILE_ID }}
          output-path: 'src/design-tokens.json'
      - run: npm run build:css
      - uses: EndBug/add-and-commit@v9
        with:
          message: 'chore: update design tokens from Figma'
```

### Manual Workflow (Fallback)

**If automation isn't available**:

1. Designer exports color/type from Figma as JSON
2. Add to `src/design-tokens.json`
3. Run: `npm run build:tokens` (generates CSS variables)
4. Commit + open PR

---

## ACCESSIBILITY & PERFORMANCE

### Color Contrast Validation

**Required ratios**:
- AAA (large): 4.5:1 (text, buttons)
- AA (large): 3:1 (decorative, graphics)
- AAA (small): 7:1 (captions, helper text)

**Test command**:
```bash
npm install -D @axe-core/cli
axe https://your-site.com --show-errors
```

**Astronautisté palette validation**:

| Combo | Light | Dark | Ratio | Level |
|-------|-------|------|-------|-------|
| Pale Blue on White | #5B9FD4 on #F8F9FA | — | 4.8:1 | AA |
| Deep Navy on White | #1F3A52 on #F8F9FA | — | 12.5:1 | AAA |
| Pale Blue on Navy | #5B9FD4 on #1F3A52 | — | 4.3:1 | AA |
| White on Deep Navy | #F8F9FA on #1F3A52 | — | 13:1 | AAA |

**CSS validation**:

```css
/* Ensure all text meets WCAG AAA */
@supports (background: oklch(0 0 0)) {
  :root {
    color-scheme: light dark;
  }

  body {
    color: var(--color-primary-deep-navy);
    background: var(--color-neutral-space-white);
  }

  /* Light mode */
  @media (prefers-color-scheme: light) {
    a { color: var(--color-primary-pale-blue); }
    a:visited { color: var(--color-semantic-warning); }
  }

  /* Dark mode */
  @media (prefers-color-scheme: dark) {
    body { background: #1a1e25; }
    a { color: #7fb3e8; } /* Lighter pale blue for dark bg */
  }
}
```

### Performance Optimization

**Icon optimization**:
```bash
# Optimize SVG icons
npm install -D svgo
svgo src/icons/*.svg --multipass

# Result: 30–50% file size reduction
```

**CSS optimization**:
```bash
# Purge unused CSS
npm install -D purgecss
purgecss --content src/**/*.tsx --css src/astronautiste.css --output dist/
```

**Lazy-load network diagrams**:
```tsx
const NetworkDiagram = React.lazy(() => import('./NetworkDiagram'));

export const Dashboard = () => (
  <Suspense fallback={<LoadingSpinner />}>
    <NetworkDiagram />
  </Suspense>
);
```

---

## FAQ & TROUBLESHOOTING

### Q: The Pale Blue looks different on my monitor vs. the design file. Why?

**A**: Color management varies by display. Use a color management tool:
```bash
# Validate your display profile
npm install -D color-compare
color-compare --hex '#5B9FD4' --compare-file astronautiste-colors.json
```

**Workaround**: Always test on multiple devices (Mac, Windows, phone). If Pale Blue looks too purple on your monitor, your display may have a blue-tinted profile.

---

### Q: Can I use different fonts for internationalization (e.g., for Cyrillic, Arabic)?

**A**: Yes. Use fallback chains:

```css
@font-face {
  font-family: 'Inter Extended';
  src: url('/fonts/inter.ttf') format('truetype'),
       url('/fonts/inter-cyrillic.ttf') format('truetype');
  unicode-range: U+0000-00FF, U+0400-04FF; /* Latin + Cyrillic */
}

body {
  font-family: 'Inter Extended', -apple-system, BlinkMacSystemFont, sans-serif;
}
```

**Figma**: Add to library as variant (e.g., "Inter / Cyrillic").

---

### Q: My development team is using Tailwind CSS. How do I integrate Astronautisté?

**A**: Create a Tailwind config with design tokens:

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        'astronautiste-pale-blue': '#5B9FD4',
        'astronautiste-deep-navy': '#1F3A52',
        'astronautiste-prism-gold': '#E8B85C',
      },
      fontFamily: {
        'astronautiste-display': ['Caloto', 'sans-serif'],
        'astronautiste-body': ['Inter', 'sans-serif'],
        'astronautiste-mono': ['JetBrains Mono', 'monospace'],
      },
      spacing: {
        'astronautiste-xs': '4px',
        'astronautiste-sm': '8px',
        'astronautiste-md': '16px',
      },
    },
  },
};
```

**Usage**:
```tsx
<button className="bg-astronautiste-pale-blue text-white font-astronautiste-display px-astronautiste-md py-astronautiste-sm rounded-astronautiste-soft">
  Launch
</button>
```

---

### Q: How do I handle dark mode?

**A**: Use CSS custom properties with `prefers-color-scheme`:

```css
:root {
  /* Light mode (default) */
  --bg-primary: #F8F9FA;
  --text-primary: #1F3A52;
  --color-primary: #5B9FD4;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg-primary: #1A1E25;
    --text-primary: #F8F9FA;
    --color-primary: #7FB3E8; /* Lighter shade for contrast on dark bg */
  }
}

body {
  background: var(--bg-primary);
  color: var(--text-primary);
}
```

**Test in DevTools**: Toggle dark mode via Settings → Rendering → Emulate CSS media feature prefers-color-scheme.

---

### Q: Which components should I prioritize building first?

**A**: MVP priority (3–4 weeks):

1. **Buttons** (Primary, Secondary) — used everywhere
2. **Cards** (Entity, Investigation) — core UI pattern
3. **Navigation** (Navbar, Breadcrumbs) — required for routing
4. **Icons** (16 core set) — visual language foundation

**Phase 2** (weeks 5–8):
5. Forms (inputs, selects, textareas)
6. Tables (with sort/filter)
7. Modals (alert, form, confirmation)

**Phase 3** (weeks 9+):
8. Network visualization
9. Advanced data viz (charts, heatmaps)
10. Accessibility audit & refinements

---

### Q: My Figma shared library has 200 components. How do I keep it manageable?

**A**: Use namespacing + versioning:

```
Button
├─ Button/Primary/Small
├─ Button/Primary/Medium
├─ Button/Primary/Large
├─ Button/Secondary/Small
└─ ...

Card
├─ Card/Entity/Default
├─ Card/Entity/Hover
├─ Card/Investigation/Default
└─ ...

v1.0 → (publish) → v1.1 → v2.0
```

**In Figma**: Right-click component → "Set as main component" → Name follows `Group/Subgroup/Variant` pattern.

**Version management**: Use numbered releases (v1.0, v1.1, v2.0). Breaking changes = major version bump. New components/colors = minor bump. Bug fixes = patch bump.

---

### Q: How do I create a design system for my team's Storybook?

**A**: Install the addon:

```bash
npm install --save-dev @storybook/addon-docs
```

**Create `.storybook/config.js`**:

```javascript
export const parameters = {
  docs: {
    theme: {
      brandTitle: 'Astronautisté Design System',
      brandUrl: 'https://astronautiste.io',
      brandImage: '/logo.svg',
      colorPrimary: '#5B9FD4',
      colorSecondary: '#1F3A52',
    },
  },
};
```

**Each component story** includes a DocsPage:

```typescript
export default {
  title: 'Components/Button',
  component: Button,
  parameters: {
    docs: {
      description: {
        component: 'Primary call-to-action button. Use for important actions like launching investigations.',
      },
    },
  },
};
```

---

## QUICK LINKS

| Resource | Link |
|----------|------|
| **Main Visual System** | `./.claude/ASTRONAUTISTE_VISUAL_SYSTEM.md` |
| **Figma Shared Library** | `https://figma.com/...` (generated after setup) |
| **Design Tokens Package** | `npm install @astronautiste/design-tokens` |
| **Storybook** | `localhost:6006` (after `npm run storybook`) |
| **WCAG Validator** | `https://www.tpgi.com/color-contrast-checker/` |
| **CSS Variables Reference** | `src/astronautiste.css` |

---

## DOCUMENT METADATA

**Version**: 1.0.0  
**Status**: Ready for Implementation  
**Last Updated**: 2026-06-15  
**Maintainer**: design@astronautiste.io  
**Next Review**: 2026-08-15

---

**Astronautisté Visual System — Implementation Guide** © 2026. Confidential.

{% endraw %}
