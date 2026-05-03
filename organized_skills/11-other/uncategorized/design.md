---
rating: ⭐⭐⭐
title: design
url: https://skills.sh/alexanderstephenthompson/claude-hub/design
---

# design

skills/alexanderstephenthompson/claude-hub/design
design
Installation
$ npx skills add https://github.com/alexanderstephenthompson/claude-hub --skill design
SKILL.md
Design Skill

Version: 1.0 Source: Design Standards

Non-negotiable design and user interface standards. These are not preferences—they are requirements.

The Problem

AI agents produce UI that looks plausible but diverges from itself. Each session picks slightly different spacing, heading levels, element choices, and state handling — creating interfaces where similar components feel inconsistent. A card uses <h3> here but <h4> there; a button has hover states in one place but not another. These standards ensure every UI element follows the same design language regardless of which session built it.

Consumption
Builders: Read ## Builder Checklist before writing any HTML, CSS, or JSX. Design token usage and semantic HTML are constraints, not suggestions.
Refactorers: Use ## Enforced Rules to find design violations. Read narrative sections for correct element selection and token usage.
Both: Narrative sections are the authoritative standard. Checklist and rules table are compressed views of the same content.
Scope and Boundaries

This skill covers:

Design system philosophy and principles
Design token usage and enforcement
Semantic HTML patterns (element selection)
CSS formatting and quality rules
Component states (hover, focus, active, disabled)
Layout philosophy (Grid vs Flexbox selection)
Responsive design principles and breakpoints
Premium UI philosophy and anti-patterns

Defers to other skills:

web-accessibility: Deep WCAG compliance, screen reader patterns, ARIA usage, keyboard navigation
web-css: CSS architecture, file organization, naming conventions (BEM), dark mode implementation

Use this skill when: You need design principles, token enforcement, or semantic HTML guidance. Use web-accessibility when: You need WCAG compliance, screen reader support, or focus management. Use web-css when: You need CSS organization, variable architecture, or responsive implementation details.

Core Principles
Users First — Prioritize user needs, workflows, and ease of use
Meticulous Craft — Precision and polish in every UI element
Speed & Performance — Fast load times, snappy interactions
Simplicity & Clarity — Clean interface, unambiguous labels
Focus & Efficiency — Help users achieve goals quickly
Consistency — Uniform design language throughout
Accessibility (WCAG AA) — Inclusive design for all users
Opinionated Defaults — Thoughtful defaults reduce decision fatigue
Design System (Single Source of Truth)
Critical Rules
ALWAYS use design tokens — NEVER use hardcoded values
All values come from styles/global.css — Single source of truth for CSS variables
No magic numbers — Every color, spacing, size uses a CSS variable
Examples
/* ✅ Correct - Uses design tokens */
.button {
  padding: var(--space-sm) var(--space-md);
  font-size: var(--font-size-body);
  background: var(--color-primary);
  border-radius: var(--radius-sm);
  box-shadow: var(--shadow-sm);
}

/* ❌ Wrong - Hardcoded values */
.button {
  padding: 8px 16px;           /* Use var(--space-sm) var(--space-md) */
  font-size: 14px;             /* Use var(--font-size-body) */
  background: #3B82F6;         /* Use var(--color-primary) */
  border-radius: 4px;          /* Use var(--radius-sm) */
}

What the Design System Contains
Complete color palette (neutrals, semantic, dark mode)
Full typography scale (fonts, sizes, weights, line heights)
Spacing system (4px base)
Border radii
Shadows
Z-index layers
Animation durations and easings
Icon sizes
Breakpoint values
Semantic HTML
Required Practices
Use semantic tags: <header>, <nav>, <main>, <article>, <section>, <footer>
Buttons for actions (<button>), links for navigation (<a>)
Forms use <form>, <label>, <input>, <select>, <textarea>
Lists use <ul>, <ol>, <li> (not divs with bullets)
Headings follow hierarchy: <h1> → <h2> → <h3> (no skipping)
Images have descriptive alt text
Tables use proper markup for tabular data
Examples
<!-- ✅ Good - Semantic HTML -->
<article class="product-card">
  <header>
    <h2>Product Name</h2>
  </header>
  <img src="..." alt="Product description">
  <p>Product description goes here.</p>
  <footer>
    <button type="button">Add to Cart</button>
  </footer>
</article>

<!-- ❌ Bad - Non-semantic divs -->
<div class="prd-crd">
  <div class="hdr">
    <div class="ttl">Product Name</div>
  </div>
  <div class="img"></div>
  <div class="btn">Add to Cart</div>
</div>

HTML Cleanliness
Headings Are for Structure

Headings (<h1>-<h6>) define document structure, not visual styling.

<!-- ❌ Wrong - Using heading for font size -->
<h3>Sale Price</h3>  <!-- Not a section heading, just wants bold text -->

<!-- ✅ Right - Use a class for styling -->
<p class="price-label">Sale Price</p>

No Class Bloat

Elements should have 1-3 classes. More than 4 is a smell — consolidate into a semantic class.

<!-- ❌ Bad - Class soup -->
<button class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:ring-2">
  Submit
</button>

<!-- ✅ Good - Semantic class (styling lives in CSS) -->
<button class="btn btn--primary">
  Submit
</button>

No Inline Styles

HTML describes structure. CSS handles presentation. Keep them separated.

// ❌ Bad - Inline styles
<div style={{ marginTop: '16px', padding: '8px' }}>

// ✅ Good - CSS class
<div className="card-section">


Only exception: Truly dynamic values computed at runtime. Even then, prefer CSS custom properties.

CSS Quality
Formatting Rules
One property per line
Use design tokens (CSS variables), not hardcoded values
Logical property order: Positioning → Box Model → Typography → Visual → Animation
Descriptive class names (BEM or semantic naming)
Generous spacing between rule sets
Comments for complex sections
Example
/* ✅ Good - Human-readable */
.product-card {
  display: flex;
  flex-direction: column;
  gap: var(--space-md);
  padding: var(--space-lg);
  background-color: var(--color-neutral-50);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
}

.product-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
  transition: all var(--duration-fast) var(--easing-standard);
}

Component States (Required)

All interactive components MUST have these five states:

State	Requirement	Example
Default	Base appearance	Normal button
Hover	Visual feedback on mouse over	Background darkens
Active	Visual feedback when pressed	Slight scale down
Focus	Clear focus indicator (keyboard nav)	outline: 2px solid var(--color-focus); outline-offset: 2px;
Disabled	Visually distinct, non-interactive	Grayed out, low opacity
Layout Philosophy
CSS Grid vs Flexbox
Layout Need	Tool	Example
Page structure	Grid (named areas)	Header, sidebar, main, footer
Section layout	Grid (named areas)	Two-column content, form layout
Component structure	Grid (named areas)	Card internals, modal layout
Navigation items	Flexbox	Top nav items, menu items
Gallery/flowing items	Flexbox	Image grid, card gallery, tag list

Default to Grid for structure. Use Flexbox when items need to flow, distribute, or wrap.

Grid with Named Areas (Primary Layout Method)
#app-layout {
  display: grid;
  grid-template-columns: 200px 1fr;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
  gap: var(--space-md);
}

#header { grid-area: header; }
#sidebar { grid-area: sidebar; }
#main { grid-area: main; }
#footer { grid-area: footer; }

White Space
Use ample negative space to improve clarity
Consistent spacing using design tokens
Accessibility (WCAG AA)
Required Standards

Color Contrast

Normal text: 4.5:1 minimum
Large text (18px+): 3:1 minimum

Keyboard Navigation

All functionality available via keyboard
Logical tab order
Focus indicators visible

Screen Reader Support

Proper ARIA labels
Semantic HTML
Skip links for navigation

Form Labels

All inputs have associated labels
Error messages linked to inputs
Respect User Preferences
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}

Responsive Design
Mobile-First Breakpoints
/* Mobile: 0-767px (base styles, no media query needed) */

/* Tablet: 768px and up */
@media (min-width: 768px) { }

/* Desktop: 1024px and up */
@media (min-width: 1024px) { }

/* Large Desktop: 1280px and up */
@media (min-width: 1280px) { }


Never use: @media (max-width: ...) — Always use min-width (mobile-first)

Container max-widths
Mobile: 100% (with padding)
Tablet: 768px
Desktop: 1024px
Large: 1280px
Premium UI Philosophy

We follow S-Tier SaaS standards (Stripe, Airbnb, Linear):

Sophisticated typography with perfect spacing
Premium color palettes with subtle gradients
Purposeful animations (150-300ms)
Delightful micro-interactions
Meticulous attention to detail

Goal: Make every interface feel premium. Subtle sophistication over flashy effects.

Anti-Patterns (DO NOT DO THESE)
Anti-Pattern	Why Bad	Do Instead
Floating labels	Confusing	Labels above inputs
Inline validation	Annoying	Validate on blur/submit
Generic error messages	Unhelpful	Specific, actionable errors
Tooltips for critical info	Easy to miss	Show directly
Disabled buttons without explanation	Frustrating	Show why disabled
Custom scrollbars	Inconsistent UX	System scrollbars
Hamburger menu on desktop	Hides navigation	Full nav on desktop
Builder Checklist

Before writing UI code governed by this skill, verify your plan against these constraints. Builders read this section before writing code; refactorers use the Enforced Rules table and full narrative instead.

Design System
 ALL values use design tokens
 No magic numbers or hardcoded colors
 Design system is source of truth
Semantic HTML
 Semantic tags used appropriately
 Buttons for actions, links for navigation
 Heading hierarchy followed
 Alt text on all images
CSS
 Human-readable formatting
 Design tokens used throughout
 Logical property order
Component States
 Default state implemented
 Hover state implemented
 Active state implemented
 Focus state implemented
 Disabled state implemented
Accessibility
 Color contrast meets WCAG AA
 Keyboard navigation works
 Screen reader tested
 Focus indicators visible
 Form labels present
Responsive
 Mobile-first approach
 Standard breakpoints used
 Works on all screen sizes
Anti-Patterns Avoided
 No floating labels
 No inline validation
 No generic errors
 No tooltips for critical info
 No unexplained disabled buttons
 No custom scrollbars
 No hamburger on desktop
Enforced Rules

These rules are deterministically checked by check.js (clean-team). When updating these standards, update the corresponding check.js rules to match — and vice versa.

Rule ID	Severity	What It Checks
no-inline-style	error	style="..." attributes in HTML
no-jsx-inline-style	warn	style={{...}} in JSX
button-type-required	error	<button> without type attribute
doctype-required	error	Missing <!DOCTYPE html>
max-classes	warn	More than 4 classes on an element
References
references/semantic-html.md — Complete semantic HTML guide
references/css-formatting.md — CSS best practices
references/accessibility-guide.md — WCAG AA compliance
references/responsive-breakpoints.md — Responsive design patterns
Assets
assets/component-states-checklist.md — State implementation guide
assets/anti-patterns.md — Detailed anti-pattern explanations
assets/layout-examples.md — CSS Grid and Flexbox examples
Scripts
scripts/validate_design_tokens.py — Check for hardcoded values
scripts/check_accessibility.py — Basic a11y validation
Weekly Installs
23
Repository
alexanderstephe…aude-hub
GitHub Stars
1
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass