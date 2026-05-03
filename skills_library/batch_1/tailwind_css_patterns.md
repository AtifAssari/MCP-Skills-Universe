---
title: tailwind-css-patterns
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/tailwind-css-patterns
---

# tailwind-css-patterns

skills/giuseppe-trisciuoglio/developer-kit/tailwind-css-patterns
tailwind-css-patterns
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill tailwind-css-patterns
Summary

Utility-first CSS framework patterns for responsive, component-based styling with Tailwind v4.1+.

Covers responsive design with mobile-first breakpoints, flexbox/grid layouts, spacing scales, typography, colors, and interactive states
Includes CSS-first configuration via @theme directive, custom utilities, and container queries for modern styling workflows
Provides 10+ component patterns (cards, navigation, forms, modals) with accessibility guidelines and dark mode support
Supports React/Vue/Svelte integration with practical examples for extracting reusable styled components
SKILL.md
Tailwind CSS Development Patterns

Expert guide for building modern, responsive user interfaces with Tailwind CSS utility-first framework. Covers v4.1+ features including CSS-first configuration, custom utilities, and enhanced developer experience.

Overview

Provides actionable patterns for responsive, accessible UIs with Tailwind CSS v4.1+. Covers utility composition, dark mode, component patterns, and performance optimization.

When to Use
Styling React/Vue/Svelte components
Building responsive layouts and grids
Implementing design systems
Adding dark mode support
Optimizing CSS workflow
Quick Reference
Responsive Breakpoints
Prefix	Min Width	Description
sm:	640px	Small screens
md:	768px	Tablets
lg:	1024px	Desktops
xl:	1280px	Large screens
2xl:	1536px	Extra large
Common Patterns
<!-- Center content -->
<div class="flex items-center justify-center min-h-screen">
  Content
</div>

<!-- Responsive grid -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
  <!-- Items -->
</div>

<!-- Card component -->
<div class="bg-white rounded-lg shadow-lg p-6">
  <h3 class="text-xl font-bold">Title</h3>
  <p class="text-gray-600">Description</p>
</div>

Instructions
Start Mobile-First: Write base styles for mobile, add responsive prefixes (sm:, md:, lg:) for larger screens
Use Design Tokens: Leverage Tailwind's spacing, color, and typography scales
Compose Utilities: Combine multiple utilities for complex styles
Extract Components: Create reusable component classes for repeated patterns
Configure Theme: Customize design tokens in tailwind.config.js or using @theme
Verify Changes: Test at each breakpoint using DevTools responsive mode. Check for visual regressions and accessibility issues before committing.
Examples
Responsive Card Component
function ProductCard({ product }: { product: Product }) {
  return (
    <div className="bg-white rounded-lg shadow-lg overflow-hidden sm:flex">
      <img className="h-48 w-full object-cover sm:h-auto sm:w-48" src={product.image} />
      <div className="p-6">
        <h3 className="text-lg font-semibold">{product.name}</h3>
        <button className="mt-4 px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700">
          Add to Cart
        </button>
      </div>
    </div>
  );
}

Dark Mode Toggle
<div class="bg-white dark:bg-gray-900 text-gray-900 dark:text-white">
  <h1 class="dark:text-white">Title</h1>
</div>

Form Input
<input
  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
  placeholder="you@example.com"
/>

Best Practices
Consistent Spacing: Use Tailwind's spacing scale (4, 8, 12, 16, etc.)
Color Palette: Stick to Tailwind's color system for consistency
Component Extraction: Extract repeated patterns into reusable components
Utility Composition: Prefer utility classes over @apply for maintainability
Semantic HTML: Use proper HTML elements with Tailwind classes
Performance: Ensure content paths include all template files for optimal purging
Accessibility: Include focus styles, ARIA labels, and respect user preferences (reduced-motion)
Troubleshooting
Classes Not Applying
Check content paths: Ensure all template files are included in content: [] in config
Verify build: Run npm run build to regenerate purged CSS
Dev mode: Use npx tailwindcss -o with --watch flag for live updates
Responsive Styles Not Working
Order matters: Responsive prefixes must come before non-responsive (e.g., md:flex not flex md:flex)
Check breakpoint values: Verify breakpoints match your design requirements
DevTools: Use browser DevTools responsive mode to test at each breakpoint
Dark Mode Issues
Verify config: Ensure darkMode: 'class' or 'media' is set correctly
Toggle implementation: Use document.documentElement.classList.toggle('dark') for class strategy
Initial flash: Add dark class to <html> before body renders
Constraints and Warnings
Class Proliferation: Long class strings reduce readability; extract into components
Content Paths: Misconfigured paths cause classes to be purged in production
Arbitrary Values: Use sparingly; prefer design tokens for consistency
Specificity Issues: Avoid @apply with complex selectors
Dark Mode: Requires correct configuration (class or media strategy)
Browser Support: Check Tailwind docs for compatibility notes
References
references/layout-patterns.md — Flexbox, grid, spacing, typography, colors
references/component-patterns.md — Cards, navigation, forms, modals, React patterns
references/responsive-design.md — Responsive patterns, dark mode, container queries
references/animations.md — Transitions, transforms, built-in animations, motion preferences
references/performance.md — Bundle optimization, CSS optimization, production builds
references/accessibility.md — Focus management, screen readers, color contrast, ARIA
references/configuration.md — CSS-first config, JavaScript config, plugins, presets
references/reference.md — Additional reference materials
External Resources
Tailwind CSS Docs
Tailwind UI
Tailwind Play
Weekly Installs
10.3K
Repository
giuseppe-trisci…oper-kit
GitHub Stars
233
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass