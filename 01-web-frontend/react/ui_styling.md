---
rating: ⭐⭐
title: ui-styling
url: https://skills.sh/mrgoonie/claudekit-skills/ui-styling
---

# ui-styling

skills/mrgoonie/claudekit-skills/ui-styling
ui-styling
Installation
$ npx skills add https://github.com/mrgoonie/claudekit-skills --skill ui-styling
Summary

Beautiful, accessible UIs combining shadcn/ui components, Tailwind CSS utilities, and canvas-based visual design.

Pre-built accessible components via shadcn/ui (dialogs, forms, tables, navigation) with copy-paste distribution and full TypeScript support
Utility-first Tailwind CSS styling with mobile-first responsive design, dark mode, and zero runtime overhead
Comprehensive theming system using CSS variables for consistent design tokens across colors, spacing, and typography
Canvas-based visual design layer for sophisticated compositions, posters, and brand materials with philosophy-driven aesthetics
Automation scripts for component installation and config generation, plus detailed reference guides for accessibility patterns and responsive layouts
SKILL.md
UI Styling Skill

Comprehensive skill for creating beautiful, accessible user interfaces combining shadcn/ui components, Tailwind CSS utility styling, and canvas-based visual design systems.

Reference
shadcn/ui: https://ui.shadcn.com/llms.txt
Tailwind CSS: https://tailwindcss.com/docs
When to Use This Skill

Use when:

Building UI with React-based frameworks (Next.js, Vite, Remix, Astro)
Implementing accessible components (dialogs, forms, tables, navigation)
Styling with utility-first CSS approach
Creating responsive, mobile-first layouts
Implementing dark mode and theme customization
Building design systems with consistent tokens
Generating visual designs, posters, or brand materials
Rapid prototyping with immediate visual feedback
Adding complex UI patterns (data tables, charts, command palettes)
Core Stack
Component Layer: shadcn/ui
Pre-built accessible components via Radix UI primitives
Copy-paste distribution model (components live in your codebase)
TypeScript-first with full type safety
Composable primitives for complex UIs
CLI-based installation and management
Styling Layer: Tailwind CSS
Utility-first CSS framework
Build-time processing with zero runtime overhead
Mobile-first responsive design
Consistent design tokens (colors, spacing, typography)
Automatic dead code elimination
Visual Design Layer: Canvas
Museum-quality visual compositions
Philosophy-driven design approach
Sophisticated visual communication
Minimal text, maximum visual impact
Systematic patterns and refined aesthetics
Quick Start
Component + Styling Setup

Install shadcn/ui with Tailwind:

npx shadcn@latest init


CLI prompts for framework, TypeScript, paths, and theme preferences. This configures both shadcn/ui and Tailwind CSS.

Add components:

npx shadcn@latest add button card dialog form


Use components with utility styling:

import { Button } from "@/components/ui/button"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"

export function Dashboard() {
  return (
    <div className="container mx-auto p-6 grid gap-6 md:grid-cols-2 lg:grid-cols-3">
      <Card className="hover:shadow-lg transition-shadow">
        <CardHeader>
          <CardTitle className="text-2xl font-bold">Analytics</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <p className="text-muted-foreground">View your metrics</p>
          <Button variant="default" className="w-full">
            View Details
          </Button>
        </CardContent>
      </Card>
    </div>
  )
}

Alternative: Tailwind-Only Setup

Vite projects:

npm install -D tailwindcss @tailwindcss/vite

// vite.config.ts
import tailwindcss from '@tailwindcss/vite'
export default { plugins: [tailwindcss()] }

/* src/index.css */
@import "tailwindcss";

Component Library Guide

Comprehensive component catalog with usage patterns, installation, and composition examples.

See: references/shadcn-components.md

Covers:

Form & input components (Button, Input, Select, Checkbox, Date Picker, Form validation)
Layout & navigation (Card, Tabs, Accordion, Navigation Menu)
Overlays & dialogs (Dialog, Drawer, Popover, Toast, Command)
Feedback & status (Alert, Progress, Skeleton)
Display components (Table, Data Table, Avatar, Badge)
Theme & Customization

Theme configuration, CSS variables, dark mode implementation, and component customization.

See: references/shadcn-theming.md

Covers:

Dark mode setup with next-themes
CSS variable system
Color customization and palettes
Component variant customization
Theme toggle implementation
Accessibility Patterns

ARIA patterns, keyboard navigation, screen reader support, and accessible component usage.

See: references/shadcn-accessibility.md

Covers:

Radix UI accessibility features
Keyboard navigation patterns
Focus management
Screen reader announcements
Form validation accessibility
Tailwind Utilities

Core utility classes for layout, spacing, typography, colors, borders, and shadows.

See: references/tailwind-utilities.md

Covers:

Layout utilities (Flexbox, Grid, positioning)
Spacing system (padding, margin, gap)
Typography (font sizes, weights, alignment, line height)
Colors and backgrounds
Borders and shadows
Arbitrary values for custom styling
Responsive Design

Mobile-first breakpoints, responsive utilities, and adaptive layouts.

See: references/tailwind-responsive.md

Covers:

Mobile-first approach
Breakpoint system (sm, md, lg, xl, 2xl)
Responsive utility patterns
Container queries
Max-width queries
Custom breakpoints
Tailwind Customization

Config file structure, custom utilities, plugins, and theme extensions.

See: references/tailwind-customization.md

Covers:

@theme directive for custom tokens
Custom colors and fonts
Spacing and breakpoint extensions
Custom utility creation
Custom variants
Layer organization (@layer base, components, utilities)
Apply directive for component extraction
Visual Design System

Canvas-based design philosophy, visual communication principles, and sophisticated compositions.

See: references/canvas-design-system.md

Covers:

Design philosophy approach
Visual communication over text
Systematic patterns and composition
Color, form, and spatial design
Minimal text integration
Museum-quality execution
Multi-page design systems
Utility Scripts

Python automation for component installation and configuration generation.

shadcn_add.py

Add shadcn/ui components with dependency handling:

python scripts/shadcn_add.py button card dialog

tailwind_config_gen.py

Generate tailwind.config.js with custom theme:

python scripts/tailwind_config_gen.py --colors brand:blue --fonts display:Inter

Best Practices
Component Composition: Build complex UIs from simple, composable primitives
Utility-First Styling: Use Tailwind classes directly; extract components only for true repetition
Mobile-First Responsive: Start with mobile styles, layer responsive variants
Accessibility-First: Leverage Radix UI primitives, add focus states, use semantic HTML
Design Tokens: Use consistent spacing scale, color palettes, typography system
Dark Mode Consistency: Apply dark variants to all themed elements
Performance: Leverage automatic CSS purging, avoid dynamic class names
TypeScript: Use full type safety for better DX
Visual Hierarchy: Let composition guide attention, use spacing and color intentionally
Expert Craftsmanship: Every detail matters - treat UI as a craft
Reference Navigation

Component Library

references/shadcn-components.md - Complete component catalog
references/shadcn-theming.md - Theming and customization
references/shadcn-accessibility.md - Accessibility patterns

Styling System

references/tailwind-utilities.md - Core utility classes
references/tailwind-responsive.md - Responsive design
references/tailwind-customization.md - Configuration and extensions

Visual Design

references/canvas-design-system.md - Design philosophy and canvas workflows

Automation

scripts/shadcn_add.py - Component installation
scripts/tailwind_config_gen.py - Config generation
Common Patterns

Form with validation:

import { useForm } from "react-hook-form"
import { zodResolver } from "@hookform/resolvers/zod"
import * as z from "zod"
import { Form, FormField, FormItem, FormLabel, FormControl, FormMessage } from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

const schema = z.object({
  email: z.string().email(),
  password: z.string().min(8)
})

export function LoginForm() {
  const form = useForm({
    resolver: zodResolver(schema),
    defaultValues: { email: "", password: "" }
  })

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(console.log)} className="space-y-6">
        <FormField control={form.control} name="email" render={({ field }) => (
          <FormItem>
            <FormLabel>Email</FormLabel>
            <FormControl>
              <Input type="email" {...field} />
            </FormControl>
            <FormMessage />
          </FormItem>
        )} />
        <Button type="submit" className="w-full">Sign In</Button>
      </form>
    </Form>
  )
}


Responsive layout with dark mode:

<div className="min-h-screen bg-white dark:bg-gray-900">
  <div className="container mx-auto px-4 py-8">
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <Card className="bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700">
        <CardContent className="p-6">
          <h3 className="text-xl font-semibold text-gray-900 dark:text-white">
            Content
          </h3>
        </CardContent>
      </Card>
    </div>
  </div>
</div>

Resources
shadcn/ui Docs: https://ui.shadcn.com
Tailwind CSS Docs: https://tailwindcss.com
Radix UI: https://radix-ui.com
Tailwind UI: https://tailwindui.com
Headless UI: https://headlessui.com
v0 (AI UI Generator): https://v0.dev
Weekly Installs
424
Repository
mrgoonie/claude…t-skills
GitHub Stars
2.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass