---
rating: ⭐⭐
title: tailwind-refactor
url: https://skills.sh/pproenca/dot-skills/tailwind-refactor
---

# tailwind-refactor

skills/pproenca/dot-skills/tailwind-refactor
tailwind-refactor
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill tailwind-refactor
SKILL.md
Community Tailwind CSS Refactoring Best Practices

Comprehensive code quality refactoring guide for Tailwind CSS applications targeting v4. Contains 50 rules across 8 categories, prioritized by migration urgency. Every transformation preserves the existing look and feel — this skill is purely about cleaner code, modern syntax, and v4 compatibility.

Companion skills: Use tailwind-ui-refactor for visual design improvements and tailwind-responsive-ui for responsive layout patterns.

When to Apply

Before manual migration: Run npx @tailwindcss/upgrade first — it handles most configuration and renamed utility changes automatically. Then use this skill for patterns the automated tool does not cover.

Reference these guidelines when:

Migrating a project from Tailwind CSS v3 to v4
Cleaning up deprecated or renamed utility classes
Consolidating verbose multi-class patterns
Replacing arbitrary values with design tokens
Removing @apply overuse in CSS files
Modernizing syntax to v4 conventions
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Configuration Migration	CRITICAL	config-
2	Deprecated Utility Replacement	CRITICAL	dep-
3	Renamed Utility Updates	HIGH	rename-
4	Class Consolidation	HIGH	class-
5	Arbitrary Value Cleanup	MEDIUM-HIGH	arb-
6	Syntax Modernization	MEDIUM	syntax-
7	@apply & Architecture Cleanup	MEDIUM	arch-
8	Modern Feature Adoption	LOW-MEDIUM	adopt-
Quick Reference
1. Configuration Migration (CRITICAL)
config-import-directive - Replace @tailwind directives with @import
config-css-theme - Migrate tailwind.config.js to CSS @theme
config-theme-function - Replace theme() function with CSS variables
config-theme-inline - Use @theme inline for non-utility design tokens
config-utility-directive - Replace @layer utilities with @utility
config-postcss-plugin - Update PostCSS plugin to @tailwindcss/postcss
config-content-autodetect - Remove manual content configuration
config-custom-variant - Migrate addVariant to @custom-variant
config-preflight-defaults - Account for Preflight default changes in v4
2. Deprecated Utility Replacement (CRITICAL)
dep-opacity-modifiers - Replace -opacity- with opacity modifiers (/50)
dep-flex-shorthand - Replace flex-shrink/flex-grow with shrink/grow
dep-text-ellipsis - Replace overflow-ellipsis with text-ellipsis
dep-decoration-utilities - Replace decoration-slice/clone with box-decoration-*
dep-transform-composites - Replace transform-none with individual resets
dep-transition-properties - Update transition-[transform] to individual properties
3. Renamed Utility Updates (HIGH)
rename-shadow-scale - Update shadow utilities to new scale
rename-blur-scale - Update blur utilities to new scale
rename-rounded-scale - Update border radius utilities to new scale
rename-ring-width - Replace ring with ring-3 for v3 default
rename-gradient-utilities - Replace bg-gradient-* with bg-linear-*
rename-outline-hidden - Replace outline-none with outline-hidden
4. Class Consolidation (HIGH)
class-size-utility - Replace matching w-* h-* with size-*
class-gap-over-space - Prefer gap-* over space-x/y-* in flex/grid
class-inset-shorthand - Replace top/right/bottom/left with inset-*
class-border-color-explicit - Add explicit border color for v4 default change
class-ring-color-explicit - Add explicit ring color for v4 default change
class-redundant-display - Remove redundant display classes
class-hidden-priority - Remove display overrides for hidden attribute
class-container-utility - Replace container plugin config with @utility
5. Arbitrary Value Cleanup (MEDIUM-HIGH)
arb-hex-to-theme - Replace arbitrary hex colors with theme tokens
arb-spacing-to-scale - Replace arbitrary spacing with theme scale
arb-dynamic-classes - Avoid dynamic class name construction
arb-breakpoint-to-theme - Replace arbitrary breakpoints with @theme
arb-zindex-to-scale - Replace arbitrary z-index with defined scale
6. Syntax Modernization (MEDIUM)
syntax-css-variable-parens - Update CSS variable syntax from brackets to parentheses
syntax-variant-stacking - Update variant stacking to left-to-right order
syntax-important-modifier - Use trailing ! for important modifier
syntax-grid-arbitrary - Use underscores in grid arbitrary values
syntax-gradient-preservation - Reset gradient stops explicitly in variants
syntax-hover-media-query - Account for hover variant media query wrapping
7. @apply & Architecture Cleanup (MEDIUM)
arch-apply-to-component - Extract @apply blocks into framework components
arch-layer-to-utility - Replace @layer components with @utility
arch-scoped-reference - Use @reference for @apply in scoped styles
arch-safelist-to-source - Replace safelist with @source inline()
arch-domain-composition - Reserve Tailwind for primitives, compose for domain
8. Modern Feature Adoption (LOW-MEDIUM)
adopt-container-queries - Use container queries instead of viewport breakpoints
adopt-not-variant - Use not-* variant for negated conditions
adopt-in-variant - Use in-* variant to simplify parent-state styling
adopt-field-sizing - Use field-sizing-content for auto-resizing textareas
adopt-starting-variant - Use starting variant for entry animations without JS
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Reference Files
File	Description
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
149
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass