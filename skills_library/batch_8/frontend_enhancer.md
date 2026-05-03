---
title: frontend-enhancer
url: https://skills.sh/ailabs-393/ai-labs-claude-skills/frontend-enhancer
---

# frontend-enhancer

skills/ailabs-393/ai-labs-claude-skills/frontend-enhancer
frontend-enhancer
Installation
$ npx skills add https://github.com/ailabs-393/ai-labs-claude-skills --skill frontend-enhancer
SKILL.md
Frontend Enhancer
Overview

The Frontend Enhancer skill transforms Next.js applications into visually stunning, modern web experiences. It provides production-ready components, comprehensive design guidelines, curated color palettes, smooth animations, and flexible layout templates optimized for responsiveness and accessibility.

When to Use This Skill

Invoke this skill when:

Improving the visual appearance of an existing application
Creating new UI components with modern styling
Selecting color schemes and design themes
Adding animations and transitions
Building responsive layouts for different screen sizes
Implementing hero sections, feature grids, or landing pages
Enhancing user experience with better visual hierarchy
Applying consistent design patterns across an application
Core Capabilities
1. Component Library

Use pre-built, production-ready React components with multiple variants and states:

Button Component (assets/button-variants.tsx):

Variants: primary, secondary, outline, ghost, danger
Sizes: sm, md, lg
Loading states with animated spinner
Full TypeScript support
Accessibility features built-in

Card Component (assets/card-variants.tsx):

Variants: default, bordered, elevated, interactive
Subcomponents: CardHeader, CardTitle, CardDescription, CardContent, CardFooter
Hover effects and transitions
Flexible padding options

Input Components (assets/input-variants.tsx):

Text inputs with validation states
Textarea component
Left/right icon support
Error and helper text display
Label integration
Full accessibility support

Implementation workflow:

Copy the desired component file from assets/ to your project's components directory
Ensure the cn utility function exists (see assets/utils-cn.ts)
Customize colors, spacing, or variants to match your brand
Import and use the component in your pages
2. Layout Templates

Use pre-designed, responsive layout patterns for common page sections:

Hero Section (assets/layout-hero-section.tsx):

Three variants: centered, split, minimal
Support for CTAs (primary and secondary)
Optional background gradients
Image/illustration support
Built-in animations

Feature Grid (assets/layout-feature-grid.tsx):

Configurable columns (2, 3, or 4)
Icon integration
Staggered animations
Hover effects
Fully responsive

Implementation workflow:

Copy the layout component from assets/ to your components directory
Customize the props and content to match your needs
Integrate with your existing pages
Adjust styling as needed for your brand
3. Design System Guidelines

Reference comprehensive design principles for consistent, professional interfaces:

Design Principles (references/design_principles.md):

Visual hierarchy best practices
Spacing and rhythm guidelines
Typography recommendations
Color theory and usage
Consistency standards
Responsiveness strategies
Accessibility guidelines (WCAG AA/AAA)
Common layout patterns

When to reference:

Starting a new design
Making decisions about visual hierarchy
Ensuring accessibility compliance
Establishing consistency across the app
Reviewing design quality

How to use: Read references/design_principles.md to understand best practices, then apply them to your specific design challenges. The document covers both theory and practical implementation.

4. Color Palettes

Access professionally curated color schemes optimized for modern web applications:

Available Palettes (references/color_palettes.md):

Corporate Blue - Professional, trustworthy (business apps, SaaS)
Vibrant Purple - Creative, modern (creative tools, portfolios)
Minimalist Gray - Clean, sophisticated (minimalist designs)
Warm Sunset - Energetic, friendly (consumer apps, e-commerce)
Ocean Fresh - Calm, professional (health, finance apps)
Dark Mode - Modern, eye-friendly (developer tools, dashboards)

Each palette includes:

Primary and secondary colors
Accent colors
Background and surface colors
Text colors (primary and secondary)
Semantic colors (success, warning, error)
Border colors

Implementation options:

Tailwind CSS: Add colors to tailwind.config.js (examples provided)
CSS Variables: Use custom properties in global CSS (examples provided)
Inline styles: Reference hex codes directly in components

Selection workflow:

Review references/color_palettes.md to see all available palettes
Consider your application's purpose and brand identity
Choose a palette that matches your goals
Implement using Tailwind config or CSS variables
Adjust specific colors if needed to match your brand
5. Animations and Transitions

Add smooth, professional animations using pre-built CSS classes and keyframes:

Animation Library (assets/animations.css):

Fade animations (fadeIn, fadeOut, fadeInUp, fadeInDown)
Slide animations (slideInLeft, slideInRight)
Scale animations (scaleIn, scaleOut)
Utility animations (bounce, pulse, spin)
Skeleton loading (shimmer effect)
Hover effects (lift, glow, scale)
Stagger delays for list animations

Accessibility: All animations respect prefers-reduced-motion for accessibility compliance.

Implementation workflow:

Copy assets/animations.css to your global CSS file (or create a separate animations file)
Apply utility classes like animate-fade-in-up, hover-lift, etc.
Use stagger classes for sequential animations in lists
Customize duration and easing if needed

Best practices:

Keep animations subtle (200-300ms for micro-interactions)
Use animations to guide user attention
Avoid excessive motion that distracts
Always test with prefers-reduced-motion enabled
Enhancement Workflow

Follow this systematic approach when enhancing a frontend application:

Step 1: Assess Current State
Identify areas lacking visual polish
Note inconsistent styling patterns
Check responsive behavior
Review accessibility issues
Evaluate color scheme and typography
Step 2: Select Design Direction
Choose a color palette from references/color_palettes.md
Review design principles in references/design_principles.md
Decide on component variants and styles
Plan layout improvements
Step 3: Implement Foundation
Set up the cn utility function (assets/utils-cn.ts)
Configure chosen color palette (Tailwind or CSS variables)
Add animation CSS (assets/animations.css) to global styles
Ensure consistent spacing scale
Step 4: Apply Components
Replace basic elements with enhanced components from assets/
Implement layout templates for key pages
Apply consistent styling across the application
Add animations and transitions
Step 5: Refine and Polish
Test responsiveness across device sizes
Verify accessibility (keyboard navigation, contrast, screen readers)
Ensure consistent hover/focus states
Optimize performance (check animation performance)
Test with prefers-reduced-motion
Step 6: Final Review
Check visual hierarchy on all pages
Verify color consistency
Test all interactive states
Validate responsive breakpoints
Review accessibility compliance
Utility Function Setup

Most components require the cn utility function for class name merging. To set it up:

Copy assets/utils-cn.ts to your project's lib/utils.ts
Install dependencies:
npm install clsx tailwind-merge

Import in components:
import { cn } from '@/lib/utils';

Responsive Design Strategy

All components and layouts follow a mobile-first approach:

Base styles - Optimized for mobile (320px+)
sm breakpoint - Small tablets (640px+)
md breakpoint - Tablets (768px+)
lg breakpoint - Desktops (1024px+)
xl breakpoint - Large desktops (1280px+)

Test each breakpoint to ensure proper layout and readability.

Accessibility Checklist

Ensure all enhanced interfaces meet these standards:

 Color contrast meets WCAG AA (4.5:1 for text)
 All interactive elements are keyboard accessible
 Focus indicators are visible and clear
 Semantic HTML is used (nav, main, article, etc.)
 Images have alt text
 Forms have proper labels
 Animations respect prefers-reduced-motion
 Touch targets are at least 44x44px
Customization Guide

To adapt components and templates to your brand:

Colors: Update color values in palette config or component files
Typography: Adjust font sizes, weights, and families
Spacing: Modify padding and margin values
Border Radius: Change rounded corners (e.g., rounded-lg to rounded-xl)
Shadows: Adjust shadow intensity (e.g., shadow-md to shadow-lg)
Animations: Modify duration and easing functions
Resources Summary

This skill includes:

references/
color_palettes.md - Six professionally designed color schemes with implementation examples
design_principles.md - Comprehensive design guidelines covering visual hierarchy, typography, accessibility, and common patterns
assets/
button-variants.tsx - Modern button component with 5 variants and 3 sizes
card-variants.tsx - Flexible card component with subcomponents
input-variants.tsx - Input and textarea components with validation states
layout-hero-section.tsx - Hero section with 3 layout variants
layout-feature-grid.tsx - Responsive feature grid with configurable columns
animations.css - Complete animation library with accessibility support
utils-cn.ts - Utility function for class name merging
Tips for Success
Start with a plan: Review design principles before making changes
Choose one palette: Stick to a single color scheme for consistency
Test on real devices: Emulators don't always show true responsive behavior
Keep it simple: Modern design favors simplicity over complexity
Prioritize accessibility: Design for all users from the start
Iterate based on feedback: Show designs to users and refine
Maintain consistency: Use the same patterns throughout your application
Performance matters: Keep animations smooth (60fps) and optimize images
Common Use Cases
Enhancing an Existing App
Select a color palette and implement it
Replace basic buttons/inputs with enhanced components
Add subtle animations to improve feedback
Review and improve spacing consistency
Ensure responsive behavior across devices
Building a Landing Page
Use hero section layout as the focal point
Add feature grid to showcase key features
Implement consistent button styles for CTAs
Add staggered animations for visual interest
Test responsiveness thoroughly
Creating a Dashboard
Use card components for data sections
Implement consistent spacing and hierarchy
Choose a professional color palette
Add skeleton loaders for data fetching
Ensure touch-friendly controls on mobile
Redesigning Forms
Replace inputs with enhanced input components
Add clear error and validation states
Ensure proper label associations
Implement loading states for submission
Test keyboard navigation flow
Weekly Installs
574
Repository
ailabs-393/ai-l…e-skills
GitHub Stars
357
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass