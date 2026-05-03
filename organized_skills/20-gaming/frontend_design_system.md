---
title: frontend-design-system
url: https://skills.sh/bilalmk/todo_correct/frontend-design-system
---

# frontend-design-system

skills/bilalmk/todo_correct/frontend-design-system
frontend-design-system
Installation
$ npx skills add https://github.com/bilalmk/todo_correct --skill frontend-design-system
SKILL.md
Frontend Design System

Build modern, accessible, responsive web applications using industry-leading design systems and best practices.

Core Capabilities
1. Design System Selection

When users ask "which UI library should I use" or need design system guidance:

Read the comparison guide:

references/design-system-comparison.md


Decision workflow:

Identify project requirements (bundle size, customization, speed)
Review comparison table for best match
Provide installation commands
Recommend component set for the use case

Quick recommendations:

Todo apps / Modern SaaS: shadcn/ui + Tailwind
Quick prototypes: Chakra UI or Mantine
Enterprise dashboards: Material UI or Ant Design
Custom designs: Headless UI + Tailwind
TypeScript-heavy: Mantine
2. Responsive Layout Design

When users need mobile-friendly layouts or responsive components:

Read the patterns guide:

references/responsive-design-patterns.md


Core principles:

Always use mobile-first approach
Follow standard breakpoints: sm (640px), md (768px), lg (1024px), xl (1280px)
Use grid for card layouts: grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3
Use flexbox for navigation: flex flex-col md:flex-row
Scale typography: text-sm md:text-base lg:text-lg
3. Tailwind CSS Patterns

When building with Tailwind CSS:

Read Tailwind patterns:

references/tailwind-patterns.md


Common patterns to apply:

Cards: rounded-lg border bg-card text-card-foreground shadow-sm p-6
Buttons: inline-flex items-center justify-center rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground hover:bg-primary/90
Inputs: flex h-10 w-full rounded-md border border-input bg-background px-3 py-2
Dark mode: bg-white dark:bg-slate-950 text-slate-900 dark:text-slate-50
4. shadcn/ui Components

When using shadcn/ui (recommended for most projects):

Read component reference:

references/shadcn-components.md


Essential components for todo apps:

npx shadcn-ui@latest add button card input form dialog badge tabs checkbox


Use provided templates:

Task card: assets/todo-card-template.tsx
Task form: assets/task-form-template.tsx

Pattern: Compose components

import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"

<Card>
  <CardHeader>
    <CardTitle>Title</CardTitle>
  </CardHeader>
  <CardContent>
    <p>Content</p>
    <Button>Action</Button>
  </CardContent>
</Card>

5. Material UI Implementation

When users choose Material UI:

Read MUI patterns:

references/material-ui-patterns.md


Setup theme first:

import { ThemeProvider, createTheme } from '@mui/material/styles'

const theme = createTheme({
  palette: {
    primary: { main: '#1976d2' },
  },
})

<ThemeProvider theme={theme}>
  <App />
</ThemeProvider>


Use sx prop for styling:

<Box sx={{ p: 2, mt: 4, borderRadius: 2 }}>

6. Chakra UI Implementation

When users choose Chakra UI:

Read Chakra patterns:

references/chakra-ui-patterns.md


Key advantages:

Style props: <Box bg="blue.500" p={4} borderRadius="md">
Dark mode built-in: useColorMode(), useColorModeValue()
Responsive arrays: <Box w={['100%', '50%', '33%']}>

Layout with Stack:

<VStack spacing={4} align="stretch">
  <Card>Item 1</Card>
  <Card>Item 2</Card>
</VStack>

7. Form Design & Validation

When building forms with validation:

Use template:

assets/task-form-template.tsx


Pattern: React Hook Form + Zod

import { useForm } from "react-hook-form"
import { zodResolver } from "@hookform/resolvers/zod"
import * as z from "zod"

const schema = z.object({
  title: z.string().min(3),
})

const form = useForm({
  resolver: zodResolver(schema),
})


Always include:

Field labels (<FormLabel>)
Error messages (<FormMessage>)
Helper text (<FormDescription>)
Disabled states for loading
Proper accessibility attributes
8. Accessibility Patterns

Always apply:

Semantic HTML: <button> not <div onClick>
ARIA labels: aria-label="Delete task"
Screen reader text: <span className="sr-only">Hidden</span>
Keyboard navigation: Focus states, tab order
Color contrast: WCAG AA minimum (4.5:1)
Touch targets: Minimum 44x44px
9. Dark Mode Implementation

Tailwind approach:

<div className="bg-white dark:bg-slate-950">
<p className="text-slate-900 dark:text-slate-50">

// Theme toggle
import { useTheme } from "next-themes"
const { theme, setTheme } = useTheme()


Chakra UI approach:

const { colorMode, toggleColorMode } = useColorMode()
const bg = useColorModeValue('white', 'gray.800')


Material UI approach:

const theme = createTheme({
  palette: {
    mode: prefersDarkMode ? 'dark' : 'light',
  },
})

10. Component Templates

When building todo apps or similar UIs:

Available templates:

Task Card (assets/todo-card-template.tsx)

Includes: Checkbox, priority badges, tags, due dates, dropdown menu
Variants: Card view, list item view
Features: Hover states, accessibility

Task Form (assets/task-form-template.tsx)

Includes: Title, description, priority, due date, tags
Validation: React Hook Form + Zod
Variants: Dialog form, inline form

Usage:

# Read template
Read: assets/todo-card-template.tsx

# Adapt to project's design system
# Modify imports and styling as needed

Workflow Guide
For New Projects

Select Design System

Read: references/design-system-comparison.md
Consider: Bundle size, customization needs, team experience
Provide recommendation with rationale

Setup Theme/Config

Install dependencies
Configure theme (colors, typography, spacing)
Setup dark mode if needed

Build Core Components

Start with layout (Container, Grid)
Add navigation
Implement forms
Create card/list components

Apply Responsive Patterns

Read: references/responsive-design-patterns.md
Mobile-first breakpoints
Test at key viewports

Add Accessibility

Semantic HTML
ARIA labels
Keyboard navigation
Screen reader support
For Todo App Specifically
Choose design system (recommend shadcn/ui)
Install core components:
npx shadcn-ui@latest add button card input form dialog badge tabs checkbox

Use templates:
Copy assets/todo-card-template.tsx
Copy assets/task-form-template.tsx
Customize colors/spacing to match brand
Add responsive layouts from references/responsive-design-patterns.md
Implement dark mode
For Existing Projects
Audit current design system
Identify pain points (bundle size, customization limits, etc.)
If migrating:
Read comparison guide for alternatives
Plan incremental migration
Start with new components
If optimizing:
Apply patterns from references
Improve responsiveness
Add accessibility features
Quick Reference
Common Tasks

"Make this responsive" → Read: references/responsive-design-patterns.md → Apply mobile-first breakpoints → Use grid/flexbox patterns

"Add dark mode" → For Tailwind: Use dark: prefix → For Chakra: Use useColorMode() → For MUI: Configure theme palette mode

"Which UI library?" → Read: references/design-system-comparison.md → Provide recommendation based on requirements

"Build a form with validation" → Use: assets/task-form-template.tsx → Adapt to project's design system → Add custom fields as needed

"Create task card" → Use: assets/todo-card-template.tsx → Modify for specific features

Design Tokens Reference

Spacing scale: 2, 4, 6, 8, 12, 16, 24, 32, 48, 64 (px in 4px increments)

Typography scale: xs (12px), sm (14px), base (16px), lg (18px), xl (20px), 2xl (24px), 3xl (30px)

Breakpoints: sm (640px), md (768px), lg (1024px), xl (1280px), 2xl (1536px)

Border radius: sm (4px), md (8px), lg (16px), full (9999px)

Anti-Patterns to Avoid

❌ Desktop-first responsive design (always start mobile) ❌ Hardcoded colors (use design tokens/theme) ❌ Div soup (use semantic HTML) ❌ Missing accessibility (always include ARIA, focus states) ❌ Inconsistent spacing (use design system scale) ❌ Non-interactive elements with onClick (use button/a) ❌ Tiny touch targets on mobile (<44px)

Resources Summary
Tailwind patterns: references/tailwind-patterns.md
shadcn/ui components: references/shadcn-components.md
Material UI patterns: references/material-ui-patterns.md
Chakra UI patterns: references/chakra-ui-patterns.md
Design system comparison: references/design-system-comparison.md
Responsive patterns: references/responsive-design-patterns.md
Task card template: assets/todo-card-template.tsx
Task form template: assets/task-form-template.tsx
Weekly Installs
38
Repository
bilalmk/todo_correct
GitHub Stars
1
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass