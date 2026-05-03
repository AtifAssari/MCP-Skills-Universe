---
title: tailwindcss
url: https://skills.sh/hairyf/skills/tailwindcss
---

# tailwindcss

skills/hairyf/skills/tailwindcss
tailwindcss
Installation
$ npx skills add https://github.com/hairyf/skills --skill tailwindcss
Summary

Utility-first CSS framework for rapidly building custom interfaces with composed utility classes.

Covers layout (flexbox, grid, positioning, sizing, spacing), transforms, typography, visual effects, and interactivity through organized utility categories
Supports responsive design with mobile-first breakpoints, container queries, and conditional variants for state, pseudo-classes, and media queries
Tailwind v4 introduces CSS-first configuration using theme variables and directives (@theme, @utility, @custom-variant) for easier design system customization
Includes dark mode support, custom style and utility creation, and content detection for automatic class scanning
SKILL.md
Tailwind CSS

The skill is based on Tailwind CSS v4.1.18, generated at 2026-01-28.

Tailwind CSS is a utility-first CSS framework for rapidly building custom user interfaces. Instead of writing custom CSS, you compose designs using utility classes directly in your markup. Tailwind v4 introduces CSS-first configuration with theme variables, making it easier to customize your design system.

Core References
Topic	Description	Reference
Installation	Vite, PostCSS, CLI, and CDN setup	core-installation
Utility Classes	Understanding Tailwind's utility-first approach and styling elements	core-utility-classes
Theme Variables	Design tokens, customizing theme, and theme variable namespaces	core-theme
Responsive Design	Mobile-first breakpoints, responsive variants, and container queries	core-responsive
Variants	Applying utilities conditionally with state, pseudo-class, and media query variants	core-variants
Preflight	Tailwind's base styles and how to extend or disable them	core-preflight
Layout
Display & Flexbox & Grid
Topic	Description	Reference
Display	flex, grid, block, inline, hidden, sr-only, flow-root, contents	layout-display
Flexbox	flex-direction, justify, items, gap, grow, shrink, wrap, order	layout-flexbox
Grid	grid-cols, grid-rows, gap, place-items, col-span, row-span, subgrid	layout-grid
Aspect Ratio	Controlling element aspect ratio for responsive media	layout-aspect-ratio
Columns	Multi-column layout for magazine-style or masonry layouts	layout-columns
Positioning
Topic	Description	Reference
Position	Controlling element positioning with static, relative, absolute, fixed, and sticky	layout-position
Inset	Controlling placement of positioned elements with top, right, bottom, left, and inset utilities	layout-inset
Sizing
Topic	Description	Reference
Width	Setting element width with spacing scale, fractions, container sizes, and viewport units	layout-width
Height	Setting element height with spacing scale, fractions, viewport units, and content-based sizing	layout-height
Min & Max Sizing	min-width, max-width, min-height, max-height constraints	layout-min-max-sizing
Spacing
Topic	Description	Reference
Margin	Controlling element margins with spacing scale, negative values, logical properties, and space utilities	layout-margin
Padding	Controlling element padding with spacing scale, logical properties, and directional utilities	layout-padding
Overflow
Topic	Description	Reference
Overflow	Controlling how elements handle content that overflows their container	layout-overflow
Images & Replaced Elements
Topic	Description	Reference
Object Fit & Position	Controlling how images and video are resized and positioned	layout-object-fit-position
Tables
Topic	Description	Reference
Table Layout	border-collapse, table-auto, table-fixed	layout-tables
Transforms
Topic	Description	Reference
Transform Base	Base transform utilities for enabling transforms, hardware acceleration, and custom transform values	transform-base
Translate	Translating elements on x, y, and z axes with spacing scale, percentages, and custom values	transform-translate
Rotate	Rotating elements in 2D and 3D space with degree values and custom rotations	transform-rotate
Scale	Scaling elements uniformly or on specific axes with percentage values	transform-scale
Skew	Skewing elements on x and y axes with degree values	transform-skew
Typography
Topic	Description	Reference
Font & Text	Font size, weight, color, line-height, letter-spacing, decoration, truncate	typography-font-text
Text Align	Controlling text alignment with left, center, right, justify, and logical properties	typography-text-align
List Style	list-style-type, list-style-position for bullets and markers	typography-list-style
Visual
Topic	Description	Reference
Background	Background color, gradient, image, size, position	visual-background
Border	Border width, color, radius, divide, ring	visual-border
Effects	Box shadow, opacity, mix-blend, backdrop-blur, filter	visual-effects
SVG	fill, stroke, stroke-width for SVG and icon styling	visual-svg
Effects & Interactivity
Topic	Description	Reference
Transition & Animation	CSS transitions, animation keyframes, reduced motion	effects-transition-animation
Visibility & Interactivity	Visibility, cursor, pointer-events, user-select, z-index	effects-visibility-interactivity
Form Controls	accent-color, appearance, caret-color, resize	effects-form-controls
Scroll Snap	scroll-snap-type, scroll-snap-align for carousels	effects-scroll-snap
Features
Dark Mode
Topic	Description	Reference
Dark Mode	Implementing dark mode with the dark variant and custom strategies	features-dark-mode
Migration
Topic	Description	Reference
Upgrade Guide	Migrating from v3 to v4, breaking changes, rename mappings	features-upgrade
Customization
Topic	Description	Reference
Custom Styles	Adding custom styles, utilities, variants, and working with arbitrary values	features-custom-styles
Functions & Directives	Tailwind's CSS directives and functions for working with your design system	features-functions-directives
Content Detection	How Tailwind detects classes and how to customize content scanning	features-content-detection
Best Practices
Topic	Description	Reference
Utility Patterns	Managing duplication, conflicts, important modifier, when to use components	best-practices-utility-patterns
Key Recommendations
Use utility classes directly in markup - Compose designs by combining utilities
Customize with theme variables - Use @theme directive to define design tokens
Mobile-first responsive design - Use unprefixed utilities for mobile, prefixed for breakpoints
Use complete class names - Never construct classes dynamically with string interpolation
Leverage variants - Stack variants for complex conditional styling
Prefer CSS-first configuration - Use @theme, @utility, and @custom-variant over JavaScript configs
Weekly Installs
1.5K
Repository
hairyf/skills
GitHub Stars
15
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass