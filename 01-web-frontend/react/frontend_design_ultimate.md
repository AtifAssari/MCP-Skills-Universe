---
title: frontend-design-ultimate
url: https://skills.sh/kesslerio/frontend-design-ultimate-clawhub-skill/frontend-design-ultimate
---

# frontend-design-ultimate

skills/kesslerio/frontend-design-ultimate-clawhub-skill/frontend-design-ultimate
frontend-design-ultimate
Installation
$ npx skills add https://github.com/kesslerio/frontend-design-ultimate-clawhub-skill --skill frontend-design-ultimate
SKILL.md
Frontend Design Ultimate

Create distinctive, production-grade static sites from text requirements alone. No mockups, no Figma — just describe what you want and get bold, memorable designs.

Stack: React 18 + TypeScript + Tailwind CSS + shadcn/ui + Framer Motion
Output: Vite (static HTML) or Next.js (Vercel-ready)

Quick Start
"Build a SaaS landing page for an AI writing tool. Dark theme, 
editorial typography, subtle grain texture. Pages: hero with 
animated demo, features grid, pricing table, FAQ accordion, footer."

Design Thinking (Do This First)

Before writing any code, commit to a BOLD aesthetic direction:

1. Understand Context
Purpose: What problem does this interface solve? Who uses it?
Audience: Developer tools? Consumer app? Enterprise? Creative agency?
Constraints: Performance requirements, accessibility needs, brand guidelines?
2. Choose an Extreme Tone

Pick ONE and commit fully — timid designs fail:

Tone	Characteristics
Brutally Minimal	Sparse, monochrome, massive typography, raw edges
Maximalist Chaos	Layered, dense, overlapping elements, controlled disorder
Retro-Futuristic	Neon accents, geometric shapes, CRT aesthetics
Organic/Natural	Soft curves, earth tones, hand-drawn elements
Luxury/Refined	Subtle animations, premium typography, restrained palette
Editorial/Magazine	Strong grid, dramatic headlines, whitespace as feature
Brutalist/Raw	Exposed structure, harsh contrasts, anti-design
Art Deco/Geometric	Gold accents, symmetry, ornate patterns
Soft/Pastel	Rounded corners, gentle gradients, friendly
Industrial/Utilitarian	Functional, monospace, data-dense
3. Define the Unforgettable Element

What's the ONE thing someone will remember? A hero animation? Typography treatment? Color combination? Unusual layout?

Aesthetics Guidelines
Typography — NEVER Generic

BANNED: Inter, Roboto, Arial, system fonts, Open Sans

DO: Distinctive, characterful choices that elevate the design.

Use Case	Approach
Display/Headlines	Bold personality — Clash, Cabinet Grotesk, Satoshi, Space Grotesk (sparingly), Playfair Display
Body Text	Refined readability — Instrument Sans, General Sans, Plus Jakarta Sans
Monospace/Code	DM Mono, JetBrains Mono, IBM Plex Mono
Pairing Strategy	Contrast weights (thin display + bold body), contrast styles (serif + geometric sans)

Size Progression: Use 3x+ jumps, not timid 1.5x increments.

Color & Theme

BANNED: Purple gradients on white, evenly-distributed 5-color palettes

DO:

Dominant + Sharp Accent: 70-20-10 rule (primary-secondary-accent)
CSS Variables: --primary, --accent, --surface, --text
Commit to dark OR light: Don't hedge with gray middle-grounds
High contrast CTAs: Buttons should pop dramatically
:root {
  --bg-primary: #0a0a0a;
  --bg-secondary: #141414;
  --text-primary: #fafafa;
  --text-secondary: #a1a1a1;
  --accent: #ff6b35;
  --accent-hover: #ff8555;
}

Motion & Animation

Priority: One orchestrated page load > scattered micro-interactions

High-Impact Moments:

Staggered hero reveals (animation-delay)
Scroll-triggered section entrances
Hover states that surprise (scale, color shift, shadow depth)
Smooth page transitions

Implementation:

CSS-only for simple animations
Framer Motion for React (pre-installed via init scripts)
Keep durations 200-400ms (snappy, not sluggish)
Spatial Composition

BANNED: Centered, symmetrical, predictable layouts

DO:

Asymmetry with purpose
Overlapping elements
Diagonal flow / grid-breaking
Generous negative space OR controlled density (pick one)
Off-grid hero sections
Backgrounds & Atmosphere

BANNED: Solid white/gray backgrounds

DO:

Gradient meshes (subtle, not garish)
Noise/grain textures (SVG filter or CSS)
Geometric patterns (dots, lines, shapes)
Layered transparencies
Dramatic shadows for depth
Blur effects for glassmorphism
/* Subtle grain overlay */
.grain::before {
  content: '';
  position: fixed;
  inset: 0;
  background: url("data:image/svg+xml,...") repeat;
  opacity: 0.03;
  pointer-events: none;
}

Mobile-First Patterns

See references/mobile-patterns.md for detailed CSS.

Critical Rules
Pattern	Desktop	Mobile Fix
Hero with hidden visual	2-column grid	Switch to display: flex (not grid)
Large selection lists	Horizontal scroll	Accordion with category headers
Multi-column forms	Side-by-side	Stack vertically
Status/alert cards	Inline	align-items: center + text-align: center
Feature grids	3-4 columns	Single column
Breakpoints
/* Tablet - stack sidebars */
@media (max-width: 1200px) { }

/* Mobile - full single column */
@media (max-width: 768px) { }

/* Small mobile - compact spacing */
@media (max-width: 480px) { }

Font Scaling
@media (max-width: 768px) {
  .hero-title { font-size: 32px; }      /* from ~48px */
  .section-title { font-size: 24px; }   /* from ~32px */
  .section-subtitle { font-size: 14px; } /* from ~16px */
}

Build Workflow
Option A: Vite (Pure Static)
# 1. Initialize
bash scripts/init-vite.sh my-site
cd my-site

# 2. Develop
npm run dev

# 3. Build static files
npm run build
# Output: dist/

# 4. Bundle to single HTML (optional)
bash scripts/bundle-artifact.sh
# Output: bundle.html

Option B: Next.js (Vercel Deploy)
# 1. Initialize
bash scripts/init-nextjs.sh my-site
cd my-site

# 2. Develop
npm run dev

# 3. Deploy to Vercel
vercel

Project Structure
Vite Static
my-site/
├── src/
│   ├── components/     # React components
│   ├── lib/           # Utilities, cn()
│   ├── styles/        # Global CSS
│   ├── config/
│   │   └── site.ts    # Editable content config
│   ├── App.tsx
│   └── main.tsx
├── index.html
├── tailwind.config.ts
└── package.json

Next.js
my-site/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   └── privacy/page.tsx
├── components/
├── lib/
├── config/
│   └── site.ts
└── tailwind.config.ts

Site Config Pattern

Keep all editable content in one file:

// config/site.ts
export const siteConfig = {
  name: "Acme AI",
  tagline: "Write better, faster",
  description: "AI-powered writing assistant",
  
  hero: {
    badge: "Now in beta",
    title: "Your words,\nsupercharged",
    subtitle: "Write 10x faster with AI that understands your style",
    cta: { text: "Get Started", href: "/signup" },
    secondaryCta: { text: "Watch Demo", href: "#demo" },
  },
  
  features: [
    { icon: "Zap", title: "Lightning Fast", description: "..." },
    // ...
  ],
  
  pricing: [
    { name: "Free", price: 0, features: [...] },
    { name: "Pro", price: 19, features: [...], popular: true },
  ],
  
  faq: [
    { q: "How does it work?", a: "..." },
  ],
  
  footer: {
    links: [...],
    social: [...],
  }
}

Pre-Implementation Checklist

Run this before finalizing any design:

Design Quality
 Typography is distinctive (no Inter/Roboto/Arial)
 Color palette has clear dominant + accent (not evenly distributed)
 Background has atmosphere (not solid white/gray)
 At least one memorable/unforgettable element
 Animations are orchestrated (not scattered)
Mobile Responsiveness
 Hero centers on mobile (no empty grid space)
 All grids collapse to single column
 Forms stack vertically
 Large lists use accordion (not horizontal scroll)
 Font sizes scale down appropriately
Form Consistency
 Input, select, textarea all styled consistently
 Radio/checkbox visible (check transparent-border styles)
 Dropdown options have readable backgrounds
 Labels use CSS variables (not hardcoded colors)
Accessibility
 Color contrast meets WCAG AA (4.5:1 text, 3:1 UI)
 Focus states visible
 Semantic HTML (nav, main, section, article)
 Alt text for images
 Keyboard navigation works
shadcn/ui Components

10 common components pre-installed (button, badge, card, accordion, dialog, navigation-menu, tabs, sheet, separator, avatar, alert). Add more with npx shadcn@latest add [name] or install all with npx shadcn@latest add --all.

See references/shadcn-components.md for full component reference.

Most used for landing pages:

Button, Badge — CTAs and labels
Card — Feature cards, pricing tiers
Accordion — FAQ sections
Dialog — Modals, video players
NavigationMenu — Header nav
Tabs — Feature showcases
Carousel — Testimonials
References
references/design-philosophy.md — Extended anti-AI-slop guidance
references/mobile-patterns.md — Detailed responsive CSS
references/shadcn-components.md — Component quick reference
templates/site-config.ts — Full siteConfig example
Examples
Prompt → Output

Input:

"Portfolio site for a photographer. Minimal, editorial feel. Grid gallery with lightbox, about section, contact form."

Design Decisions:

Tone: Editorial/Magazine
Typography: Cormorant Garamond (display) + Inter... wait, banned. Plus Jakarta Sans (body)
Color: Near-black bg (#0c0c0c), warm white text (#f5f5f0), copper accent (#b87333)
Unforgettable: Full-bleed hero image with text overlay that reveals on scroll
Motion: Gallery images fade in staggered on scroll

Output: Complete Next.js project with responsive gallery, lightbox component, and contact form with validation.

Based on Anthropic's frontend-design, web-artifacts-builder, and community frontend-design-v2 skills.

Weekly Installs
301
Repository
kesslerio/front…ub-skill
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass