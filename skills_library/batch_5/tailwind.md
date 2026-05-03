---
title: tailwind
url: https://skills.sh/pproenca/dot-skills/tailwind
---

# tailwind

skills/pproenca/dot-skills/tailwind
tailwind
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill tailwind
SKILL.md
Community Tailwind CSS v4 Best Practices

Comprehensive performance optimization guide for Tailwind CSS v4 applications. Contains 44 rules across 8 categories, prioritized by impact to guide automated refactoring and code generation.

When to Apply

Reference these guidelines when:

Configuring Tailwind CSS v4 build tooling (Vite plugin, PostCSS, CLI)
Writing or migrating styles using v4's CSS-first approach
Optimizing CSS bundle size and build performance
Implementing responsive designs with breakpoints or container queries
Setting up theming with @theme directive and design tokens
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Build Configuration	CRITICAL	build-
2	CSS Generation	CRITICAL	gen-
3	Bundle Optimization	HIGH	bundle-
4	Utility Patterns	HIGH	util-
5	Component Architecture	MEDIUM-HIGH	comp-
6	Theming & Design Tokens	MEDIUM	theme-
7	Responsive & Adaptive	MEDIUM	resp-
8	Animation & Transitions	LOW-MEDIUM	anim-
Quick Reference
1. Build Configuration (CRITICAL)
build-vite-plugin - Use Vite Plugin Over PostCSS
build-css-import - Use CSS Import Over @tailwind Directives
build-content-detection - Leverage Automatic Content Detection
build-node-version - Use Node.js 20+ for Optimal Performance
build-postcss-simplify - Remove Redundant PostCSS Plugins
build-cli-package - Use Correct CLI Package
2. CSS Generation (CRITICAL)
gen-css-first-config - Use CSS-First Configuration Over JavaScript
gen-avoid-theme-bloat - Avoid Excessive Theme Variables
gen-oklch-colors - Use OKLCH Color Space for Vivid Colors
gen-utility-directive - Use @utility for Custom Utilities
gen-dynamic-utilities - Use Dynamic Utility Values
gen-css-variable-syntax - Use Parentheses for CSS Variable References
3. Bundle Optimization (HIGH)
bundle-remove-unused-plugins - Remove Built-in Plugins
bundle-avoid-preprocessors - Avoid Sass/Less Preprocessors
bundle-css-minification - Enable CSS Minification in Production
bundle-avoid-cdn-production - Avoid Play CDN in Production
bundle-split-critical-css - Extract Critical CSS for Initial Render
4. Utility Patterns (HIGH)
util-renamed-utilities - Use Renamed Utility Classes
util-important-modifier - Use Trailing Important Modifier
util-variant-stacking - Use Left-to-Right Variant Stacking
util-explicit-colors - Use Explicit Border and Ring Colors
util-opacity-modifier - Use Slash Opacity Modifier
util-gradient-via-none - Use via-none to Reset Gradient Stops
5. Component Architecture (MEDIUM-HIGH)
comp-avoid-apply-overuse - Avoid Overusing @apply
comp-reference-directive - Use @reference for CSS Module Integration
comp-utility-file-scope - Understand Utility File Scope
comp-smart-sorting - Leverage Smart Utility Sorting
comp-container-customize - Customize Container with @utility
comp-custom-variant - Use @custom-variant for Custom Variant Definitions
6. Theming & Design Tokens (MEDIUM)
theme-semantic-tokens - Use Semantic Design Token Names
theme-dark-mode-class - Use Class-Based Dark Mode for Control
theme-prefix-variables - Use Prefix for Variable Namespacing
theme-runtime-variables - Leverage Runtime CSS Variables
theme-color-scheme - Set color-scheme for Native Dark Mode
theme-inline-static - Use @theme inline and @theme static for Variable Control
7. Responsive & Adaptive (MEDIUM)
resp-mobile-first - Use Mobile-First Responsive Design
resp-container-queries - Use Container Queries for Component-Level Responsiveness
resp-custom-breakpoints - Define Custom Breakpoints in @theme
resp-hover-capability - Pair Hover with Active for Touch-Friendly Interactions
resp-logical-properties - Use Logical Properties for RTL Support
8. Animation & Transitions (LOW-MEDIUM)
anim-gpu-accelerated - Use GPU-Accelerated Transform Properties
anim-starting-style - Use @starting-style for Entry Animations
anim-gradient-interpolation - Use OKLCH Gradient Interpolation
anim-3d-transforms - Use Built-in 3D Transform Utilities
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Full Compiled Document

For a complete guide with all rules expanded, see AGENTS.md.

Reference Files
File	Description
AGENTS.md	Complete compiled guide with all rules
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
278
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass