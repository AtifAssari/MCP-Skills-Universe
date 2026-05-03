---
rating: ⭐⭐⭐
title: visual designer
url: https://skills.sh/daffy0208/ai-dev-standards/visual-designer
---

# visual designer

skills/daffy0208/ai-dev-standards/Visual Designer
Visual Designer
Installation
$ npx skills add https://github.com/daffy0208/ai-dev-standards --skill 'Visual Designer'
SKILL.md
Visual Designer

Great design is invisible - users notice when it's bad, not when it's good.

Core Principle

Consistency over creativity.

Visual design serves the user experience. Every color, font, and spacing decision should have a purpose.

Phase 1: Color Systems
Color Theory Basics

Color Wheel:

Complementary: Opposite colors (blue + orange) - high contrast
Analogous: Adjacent colors (blue + green + teal) - harmonious
Triadic: Three evenly spaced colors - balanced
Monochromatic: Shades of one color - safe, minimal
Creating a Color Palette

60-30-10 Rule:

60% Primary color (dominant)
30% Secondary color (supporting)
10% Accent color (call-to-action)

Example Palette:

/* Primary (60%) - Backgrounds, large areas */
--color-primary-50: #eff6ff;
--color-primary-100: #dbeafe;
--color-primary-200: #bfdbfe;
--color-primary-500: #3b82f6; /* Main brand color */
--color-primary-600: #2563eb;
--color-primary-900: #1e3a8a;

/* Secondary (30%) - Complementary elements */
--color-secondary-500: #8b5cf6;
--color-secondary-600: #7c3aed;

/* Accent (10%) - CTAs, highlights */
--color-accent-500: #f59e0b;
--color-accent-600: #d97706;

/* Neutrals - Text, borders */
--color-gray-50: #f9fafb;
--color-gray-100: #f3f4f6;
--color-gray-300: #d1d5db;
--color-gray-500: #6b7280;
--color-gray-700: #374151;
--color-gray-900: #111827;

/* Semantic colors */
--color-success: #10b981;
--color-warning: #f59e0b;
--color-error: #ef4444;
--color-info: #3b82f6;

Accessible Color Contrast

WCAG Requirements:

Normal text (< 18pt): 4.5:1 contrast ratio
Large text (≥ 18pt or 14pt bold): 3:1 contrast ratio
UI components: 3:1 contrast ratio
/* ✅ Good: Sufficient contrast (8:1) */
.text {
  color: #111827; /* gray-900 */
  background: #ffffff;
}

/* ❌ Bad: Insufficient contrast (2.1:1) */
.text-bad {
  color: #d1d5db; /* gray-300 */
  background: #ffffff;
}


Tools:

Coolors.co - Generate palettes
Color Contrast Checker
Adobe Color
Dark Mode Strategy
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #f9fafb;
  --text-primary: #111827;
  --text-secondary: #6b7280;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg-primary: #111827;
    --bg-secondary: #1f2937;
    --text-primary: #f9fafb;
    --text-secondary: #9ca3af;
  }
}


Dark Mode Checklist:

 Reduce pure white (#fff) → use off-white (#f9fafb)
 Reduce pure black (#000) → use dark gray (#111827)
 Increase contrast on dark backgrounds
 Test with actual dark mode users
 Support system preference
Phase 2: Typography
Font Pairing Principles

Golden Rule: Maximum 2 fonts

Heading font: Distinctive, attention-grabbing
Body font: Readable, neutral

Popular Pairings:

/* Modern & Clean */
--font-heading: 'Inter', sans-serif;
--font-body: 'Inter', sans-serif;

/* Classic & Professional */
--font-heading: 'Playfair Display', serif;
--font-body: 'Source Sans Pro', sans-serif;

/* Tech & Minimal */
--font-heading: 'Space Grotesk', sans-serif;
--font-body: 'IBM Plex Sans', sans-serif;

/* Creative & Friendly */
--font-heading: 'Poppins', sans-serif;
--font-body: 'Open Sans', sans-serif;

Type Scale (Modular Scale)

Base size: 16px (1rem) Scale ratio: 1.25 (Major Third)

--text-xs: 0.64rem; /* 10.24px */
--text-sm: 0.8rem; /* 12.8px */
--text-base: 1rem; /* 16px */
--text-lg: 1.25rem; /* 20px */
--text-xl: 1.563rem; /* 25px */
--text-2xl: 1.953rem; /* 31.25px */
--text-3xl: 2.441rem; /* 39px */
--text-4xl: 3.052rem; /* 48.83px */
--text-5xl: 3.815rem; /* 61px */

/* Font weights */
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;

Line Height & Spacing
/* Headings: Tighter line-height */
h1,
h2,
h3 {
  line-height: 1.2;
}

/* Body text: Comfortable reading */
p {
  line-height: 1.6;
  max-width: 65ch; /* 65 characters max for readability */
}

/* Small text: More line-height */
.text-sm {
  line-height: 1.8;
}

/* Letter spacing */
.heading {
  letter-spacing: -0.02em; /* Tighter */
}

.uppercase {
  letter-spacing: 0.05em; /* Wider for all-caps */
}

Responsive Typography
/* Fluid typography */
h1 {
  font-size: clamp(2rem, 5vw, 3.5rem);
}

/* Or breakpoint-based */
h1 {
  font-size: 2rem;
}

@media (min-width: 768px) {
  h1 {
    font-size: 3rem;
  }
}

@media (min-width: 1024px) {
  h1 {
    font-size: 3.5rem;
  }
}

Phase 3: Spacing System
8pt Grid System

Why 8pt?

Most screens are divisible by 8
Creates visual rhythm
Easier to maintain consistency
--space-1: 0.25rem; /* 4px */
--space-2: 0.5rem; /* 8px */
--space-3: 0.75rem; /* 12px */
--space-4: 1rem; /* 16px */
--space-5: 1.25rem; /* 20px */
--space-6: 1.5rem; /* 24px */
--space-8: 2rem; /* 32px */
--space-10: 2.5rem; /* 40px */
--space-12: 3rem; /* 48px */
--space-16: 4rem; /* 64px */
--space-20: 5rem; /* 80px */
--space-24: 6rem; /* 96px */


Usage:

/* Component padding */
.button {
  padding: var(--space-3) var(--space-6); /* 12px 24px */
}

/* Section spacing */
.section {
  padding: var(--space-16) 0; /* 64px top/bottom */
}

/* Element margins */
.heading {
  margin-bottom: var(--space-4); /* 16px */
}

.paragraph {
  margin-bottom: var(--space-6); /* 24px */
}

Vertical Rhythm
/* Consistent vertical spacing */
* + * {
  margin-top: var(--space-4);
}

/* Specific overrides */
h1 + p {
  margin-top: var(--space-6);
}

p + p {
  margin-top: var(--space-4);
}

Phase 4: Layout & Composition
Visual Hierarchy

Establish importance through:

Size: Larger = more important
Weight: Bolder = more important
Color: Brighter = more important
Spacing: More space = more important
/* Primary heading */
h1 {
  font-size: var(--text-4xl);
  font-weight: var(--font-bold);
  color: var(--text-primary);
  margin-bottom: var(--space-8);
}

/* Secondary heading */
h2 {
  font-size: var(--text-2xl);
  font-weight: var(--font-semibold);
  color: var(--text-primary);
  margin-bottom: var(--space-4);
}

/* Body text */
p {
  font-size: var(--text-base);
  font-weight: var(--font-normal);
  color: var(--text-secondary);
  margin-bottom: var(--space-4);
}

/* Supporting text */
.caption {
  font-size: var(--text-sm);
  color: var(--text-tertiary);
}

Grid Systems

12-Column Grid:

.container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-4);
}

/* Full width */
.col-12 {
  grid-column: span 12;
}

/* Half width */
.col-6 {
  grid-column: span 6;
}

/* Third width */
.col-4 {
  grid-column: span 4;
}

/* Responsive */
@media (max-width: 768px) {
  .col-6 {
    grid-column: span 12; /* Stack on mobile */
  }
}

Whitespace (Negative Space)
/* ❌ Cramped */
.card-bad {
  padding: 8px;
}

/* ✅ Breathing room */
.card-good {
  padding: var(--space-8); /* 32px */
}

/* Content spacing */
.content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--space-4); /* Side padding */
}

Responsive Breakpoints
/* Mobile first */
:root {
  --breakpoint-sm: 640px; /* Small devices */
  --breakpoint-md: 768px; /* Tablets */
  --breakpoint-lg: 1024px; /* Laptops */
  --breakpoint-xl: 1280px; /* Desktops */
  --breakpoint-2xl: 1536px; /* Large screens */
}

/* Usage */
@media (min-width: 768px) {
  .container {
    padding: var(--space-8);
  }
}

Phase 5: Visual Polish
Shadows & Elevation
/* Elevation levels */
--shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
--shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.15);

/* Usage */
.card {
  box-shadow: var(--shadow-md);
  transition: box-shadow 0.2s;
}

.card:hover {
  box-shadow: var(--shadow-lg);
}

Border Radius
--radius-sm: 0.25rem; /* 4px - small elements */
--radius-md: 0.5rem; /* 8px - buttons, inputs */
--radius-lg: 0.75rem; /* 12px - cards */
--radius-xl: 1rem; /* 16px - modals */
--radius-full: 9999px; /* Fully rounded */

/* Usage */
.button {
  border-radius: var(--radius-md);
}

.avatar {
  border-radius: var(--radius-full);
}

Transitions & Animations
/* Transition timing */
--transition-fast: 150ms;
--transition-base: 200ms;
--transition-slow: 300ms;

/* Easing functions */
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);

/* Button hover */
.button {
  transition: all var(--transition-base) var(--ease-in-out);
}

.button:hover {
  transform: translateY(-1px);
  box-shadow: var(--shadow-lg);
}

/* Fade in */
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.fade-in {
  animation: fadeIn var(--transition-slow) var(--ease-out);
}

Design Principles
1. Contrast

Create clear distinction between elements

/* ✅ Good contrast */
.hero {
  background: var(--color-primary-600);
  color: white;
}

/* ❌ Poor contrast */
.hero-bad {
  background: #ddd;
  color: #aaa;
}

2. Alignment

Align elements to create order

/* ✅ Aligned */
.container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

3. Repetition

Repeat visual elements for consistency

/* Consistent button styles */
.button {
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  font-weight: var(--font-semibold);
}

4. Proximity

Group related elements

/* Form fields grouped */
.form-group {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  margin-bottom: var(--space-6);
}

Component Design Patterns
Buttons
/* Primary button */
.btn-primary {
  background: var(--color-primary-600);
  color: white;
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  font-weight: var(--font-semibold);
  border: none;
  cursor: pointer;
  transition: all var(--transition-base);
}

.btn-primary:hover {
  background: var(--color-primary-700);
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}

/* Secondary button */
.btn-secondary {
  background: transparent;
  color: var(--color-primary-600);
  border: 2px solid var(--color-primary-600);
}

/* Ghost button */
.btn-ghost {
  background: transparent;
  color: var(--text-primary);
}

.btn-ghost:hover {
  background: var(--color-gray-100);
}

Cards
.card {
  background: white;
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  box-shadow: var(--shadow-md);
  transition: all var(--transition-base);
}

.card:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

Forms
.input {
  width: 100%;
  padding: var(--space-3) var(--space-4);
  border: 2px solid var(--color-gray-300);
  border-radius: var(--radius-md);
  font-size: var(--text-base);
  transition: border-color var(--transition-base);
}

.input:focus {
  outline: none;
  border-color: var(--color-primary-500);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.input:invalid {
  border-color: var(--color-error);
}

Design Tools
Color Tools
Coolors - Generate palettes
Color Hunt - Curated palettes
Adobe Color - Color wheel
Contrast Checker
Typography Tools
Google Fonts
Font Pair - Font combinations
Type Scale - Generate type scales
Design Systems
Tailwind CSS - Utility-first CSS
Radix Colors - Color system
Open Color - Color scheme
Visual Design Checklist
Colors
 Primary, secondary, accent colors defined
 Neutral grays (50-900) defined
 Semantic colors (success, warning, error)
 All text meets WCAG contrast requirements
 Dark mode colors defined
Typography
 1-2 fonts maximum
 Type scale defined (8-10 sizes)
 Font weights specified
 Line heights set appropriately
 Max-width for readability (65ch)
Spacing
 8pt grid system used
 Consistent spacing scale
 Adequate whitespace
 Vertical rhythm maintained
Components
 Button styles consistent
 Form inputs styled consistently
 Cards have proper elevation
 Hover states defined
 Focus states visible
Responsive
 Mobile-first approach
 Breakpoints defined
 Touch targets ≥ 44px
 Text scales appropriately
Related Resources

Skills:

design-system-architect - Building design systems
ux-designer - User experience design
accessibility-engineer - Color contrast, readability

External:

Refactoring UI
Design Systems Repo
Laws of UX

Good design makes the product easy to use. Great design makes it disappear. 🎨

Weekly Installs
–
Repository
daffy0208/ai-de…tandards
GitHub Stars
27
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass