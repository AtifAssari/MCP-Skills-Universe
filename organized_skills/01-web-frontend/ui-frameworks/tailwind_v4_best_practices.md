---
rating: ⭐⭐
title: tailwind-v4-best-practices
url: https://skills.sh/jenishshrestha/ai-skills/tailwind-v4-best-practices
---

# tailwind-v4-best-practices

skills/jenishshrestha/ai-skills/tailwind-v4-best-practices
tailwind-v4-best-practices
Installation
$ npx skills add https://github.com/jenishshrestha/ai-skills --skill tailwind-v4-best-practices
SKILL.md
Tailwind CSS v4 Best Practices

Production-grade Tailwind CSS v4 with a focus on design system thinking, maintainability, and performance.

Core Principles
1. Design Tokens, Not Direct Colors

Use semantic tokens instead of Tailwind's default color palette. This enables theme switching without touching components.

<!-- ❌ Direct colors — breaks when you rebrand -->
<button class="bg-blue-500 text-white hover:bg-blue-600">
<span class="text-red-600">Error</span>

<!-- ✅ Semantic tokens — theme-aware -->
<button class="bg-primary text-primary-foreground hover:bg-primary-hover">
<span class="text-error">Error</span>

2. Semantic Utilities Over Arbitrary Values

Use the built-in scale. Reserve arbitrary values for true one-offs.

<!-- ❌ Arbitrary when a utility exists -->
<h1 class="text-[20px]">
<div class="p-[16px] gap-[24px]">

<!-- ✅ Use the scale -->
<h1 class="text-2xl">
<div class="p-4 gap-6">

3. Complete Class Names Only

Tailwind's compiler needs full class names at build time. Never construct them dynamically.

// ❌ Tailwind can't detect these
<div className={`bg-${color}-500`}>

// ✅ Complete class names or CSS variables
<div className={color === 'blue' ? 'bg-blue-500' : 'bg-red-500'}>
<div className="bg-[var(--dynamic-color)]">

4. Avoid @apply

Tailwind v4 discourages @apply. Use utility classes directly in templates, or use theme() in CSS when you need custom component classes.

/* ❌ v3 pattern */
.button { @apply px-4 py-2 bg-blue-500 text-white rounded; }

/* ✅ v4 — use theme() if you need CSS */
.button {
  padding-inline: theme(spacing.4);
  background-color: theme(colors.primary);
}

@theme Configuration

Tailwind v4 moves config from JavaScript to CSS. Define design tokens with @theme:

@import "tailwindcss";

@theme {
  /* Semantic colors using OKLCH */
  --color-primary: oklch(0.55 0.25 250);
  --color-primary-hover: oklch(0.50 0.25 250);
  --color-primary-foreground: oklch(0.98 0 0);

  --color-error: oklch(0.60 0.22 25);
  --color-success: oklch(0.65 0.18 145);

  /* Surface colors */
  --color-background: oklch(1.0 0 0);
  --color-foreground: oklch(0.20 0.01 250);
  --color-surface: oklch(0.98 0.01 250);
  --color-border: oklch(0.90 0.01 250);

  /* Typography */
  --font-family-heading: "Inter", sans-serif;
  --font-family-body: "Inter", sans-serif;
  --font-family-mono: "Fira Code", monospace;
}


For full token architecture (Primitive → Semantic → Component layers), see references/design-tokens.md.

OKLCH Colors

Tailwind v4 defaults to OKLCH for better perceptual uniformity.

oklch(lightness chroma hue / alpha)

Lightness: 0 (black) to 1 (white)
Chroma: 0 (gray) to ~0.4 (vivid)
Hue: 0-360 degrees
Alpha: 0-1 (optional)
--color-brand: oklch(0.55 0.25 270);      /* vivid purple */
--color-subtle: oklch(0.96 0.02 250);     /* muted gray */
--color-overlay: oklch(0.0 0 0 / 0.5);   /* translucent black */

v3 → v4 Class Name Renames
v3                     →  v4
───────────────────────────────
bg-gradient-to-r       →  bg-linear-to-r
bg-gradient-to-br      →  bg-linear-to-br
flex-shrink-0          →  shrink-0
flex-grow              →  grow
decoration-clone       →  box-decoration-clone
decoration-slice       →  box-decoration-slice


Run the automated upgrade: npx @tailwindcss/upgrade

Vite Setup (Fastest)
import tailwindcss from '@tailwindcss/vite'

export default {
  plugins: [tailwindcss()],
}


v4 auto-detects content — no need to configure content paths. Unused utilities are tree-shaken automatically in production.

References

Load only what you need for the current task:

Reference	Load When
design-tokens.md	Setting up token architecture, component tokens, status color patterns
theming.md	Dark mode, runtime theme switching, brand variants, user preference detection
advanced-patterns.md	Animations, grid layouts, container queries, custom utilities, plugins, performance
migration.md	Migrating a project from Tailwind v3 to v4
Weekly Installs
25
Repository
jenishshrestha/ai-skills
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass