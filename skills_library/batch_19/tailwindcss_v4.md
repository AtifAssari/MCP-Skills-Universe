---
title: tailwindcss-v4
url: https://skills.sh/tlq5l/tailwindcss-v4-skill/tailwindcss-v4
---

# tailwindcss-v4

skills/tlq5l/tailwindcss-v4-skill/tailwindcss-v4
tailwindcss-v4
Installation
$ npx skills add https://github.com/tlq5l/tailwindcss-v4-skill --skill tailwindcss-v4
SKILL.md
Tailwind CSS v4 Skill

CSS-first configuration, new directives, migration from v3.

Quick Reference
v4 Entry Point
@import "tailwindcss";


NOT the v3 way:

/* ❌ These cause errors in v4 */
@tailwind base;
@tailwind components;
@tailwind utilities;

Key Directives
Directive	Purpose
@theme	Define design tokens (colors, spacing, fonts)
@utility	Create custom utility classes
@variant	Define custom variants (hover, focus, etc.)
@source	Control class detection and safelisting
@reference	Import for @apply without emitting CSS
Theme Configuration (CSS-first)
@import "tailwindcss";

@theme {
  --color-primary: #3b82f6;
  --color-secondary: #64748b;
  --font-display: "Inter", sans-serif;
  --spacing-18: 4.5rem;
}


NOT tailwind.config.js:

// ❌ v3 pattern - don't use in v4
module.exports = {
  theme: {
    extend: {
      colors: { primary: '#3b82f6' }
    }
  }
}

Custom Utilities
@utility content-auto {
  content-visibility: auto;
}

/* Functional utility must end in -* */
@utility tab-* {
  --tab-size: --value(--spacing-*, [integer]);
  tab-size: var(--tab-size);
}

Custom Variants

Use @custom-variant to define new variants (not @variant).

@custom-variant hocus (&:hover, &:focus);

/* Dark mode with class strategy */
@custom-variant dark (&:is(.dark *));

/* Body block with @slot */
@custom-variant hocus {
  &:hover, &:focus { @slot; }
}

Theme Configuration
@theme {
  --color-primary: #3b82f6;

  /* Clear namespace */
  --color-*: initial;
}

Theme Flags
default: Merge with default theme
inline: Emit variables to output
static: Use values but don't emit vars
reference: Use values but don't emit CSS
@theme inline {
  --font-sans: "SF Pro Text", system-ui;
}

New Gradient Syntax
<!-- v4 preferred - supports interpolation color space -->
<div class="bg-linear-to-r/oklch from-blue-500 to-purple-500"></div>

<!-- Also: bg-linear-to-b, bg-radial, bg-conic -->

New Variants
@min-[400px]: / @max-[600px]: (Container queries)
starting: (@starting-style)
details-content: (::details-content)
inverted-colors:, noscript:, print:
Safelisting Classes
/* Inline safelist */
@source inline("bg-red-500 text-white hidden");

/* From external source */
@source "../content/**/*.md";

Migration from v3
v3	v4
@tailwind base/components/utilities	@import "tailwindcss"
tailwind.config.js theme.extend	@theme { --color-* }
PostCSS tailwindcss plugin	@tailwindcss/postcss
@apply with config values	@reference import first
PostCSS Setup
// postcss.config.js
export default {
  plugins: {
    '@tailwindcss/postcss': {}  // NOT 'tailwindcss'
  }
}

Vite Setup
// vite.config.ts
import tailwindcss from '@tailwindcss/vite'

export default {
  plugins: [tailwindcss()]
}


Sources: Tailwind v4 Docs, GitHub

Weekly Installs
51
Repository
tlq5l/tailwindc…v4-skill
GitHub Stars
2
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass