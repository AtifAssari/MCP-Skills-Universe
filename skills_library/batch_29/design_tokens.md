---
title: design-tokens
url: https://skills.sh/phrazzld/claude-config/design-tokens
---

# design-tokens

skills/phrazzld/claude-config/design-tokens
design-tokens
Installation
$ npx skills add https://github.com/phrazzld/claude-config --skill design-tokens
SKILL.md
Design Tokens

Design tokens are the single source of truth for design decisions.

Philosophy
CSS-first: Define tokens in CSS @theme, not JavaScript config
Semantic naming: --color-primary not --color-blue-500
Brand-tinted neutrals: Add imperceptible brand hue (chroma 0.005-0.02), not pure gray
OKLCH colors: Perceptually uniform, better than RGB/HSL
Why Tailwind CSS 4 @theme
CSS-native (no build step overhead)
Type-safe auto-completion
CSS variable integration (var(--color-primary))
Dark mode built-in

Migration from Tailwind 3: Delete tailwind.config.js, move to CSS @theme.

Basic @theme Structure
@import "tailwindcss";

@theme {
  /* Brand hue - single source of truth */
  --brand-hue: 250;

  /* Colors - OKLCH with semantic names */
  --color-primary: oklch(0.6 0.2 var(--brand-hue));
  --color-background: oklch(0.995 0.005 var(--brand-hue));  /* Brand-tinted */
  --color-foreground: oklch(0.15 0.02 var(--brand-hue));

  /* Typography */
  --font-sans: "Inter Variable", system-ui, sans-serif;
  --font-size-base: 1rem;

  /* Spacing (8-point grid) */
  --spacing-md: 1rem;
  --radius-md: 0.5rem;
}

Best Practices
Do
Use semantic names (--color-primary)
Use OKLCH colors
Tint neutrals with brand hue
Follow 8-point spacing grid
Support dark mode from start
Create component tokens
Don't
Hardcode values
Use pure grays (chroma 0)
Use generic fonts (Inter/Roboto)
Skip dark mode
Create too many tokens initially
Dark Mode Pattern

Same brand hue, inverted lightness:

@theme {
  --brand-hue: 250;
  --color-background: oklch(0.995 0.005 var(--brand-hue));

  @media (prefers-color-scheme: dark) {
    --color-background: oklch(0.12 0.015 var(--brand-hue));
  }
}

References

Detailed patterns:

references/color-system.md — OKLCH, semantic colors, brand-tinted neutrals
references/typography.md — Type scale, font pairings, font loading
references/spacing.md — 8-point grid, radius, shadows, breakpoints, z-index
references/dark-mode.md — System preference, manual toggle, component
references/component-tokens.md — Button, input, card, animation, WebGL
Integration

Design tokens provide the foundation; frontend-design provides aesthetic direction.

Load design-tokens for the system
Load frontend-design for aesthetic execution
Result: Consistent system + distinctive design

"Design tokens are contracts between design and development."

Weekly Installs
25
Repository
phrazzld/claude-config
GitHub Stars
8
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass