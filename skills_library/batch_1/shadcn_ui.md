---
title: shadcn-ui
url: https://skills.sh/jezweb/claude-skills/shadcn-ui
---

# shadcn-ui

skills/jezweb/claude-skills/shadcn-ui
shadcn-ui
Installation
$ npx skills add https://github.com/jezweb/claude-skills --skill shadcn-ui
Summary

Install and configure shadcn/ui components in themed React projects with guided component selection and common UI patterns.

Requires tailwind-theme-builder to have set up CSS variables, ThemeProvider, and dark mode infrastructure first
Covers 20+ components organized by category: foundation (button, input, card), forms (form, textarea, select), feedback (toast, alert), overlays (dialog, sheet, popover), data display (table, tabs), and navigation
Documents installation order, external dependencies (react-hook-form, zod, sonner, @tanstack/react-table), and four critical gotchas (Radix Select empty strings, React Hook Form null handling, Lucide icon tree-shaking, Dialog width overrides)
Includes recipes for contact forms, data tables, modal CRUD, navigation, and settings pages; customization via semantic CSS tokens and variant extension
SKILL.md
shadcn/ui Components

Add shadcn/ui components to a themed React project. This skill runs AFTER tailwind-theme-builder has set up CSS variables, ThemeProvider, and dark mode. It handles component installation, customisation, and combining components into working patterns.

Prerequisite: Theme infrastructure must exist (CSS variables, components.json, cn() utility). Use tailwind-theme-builder first if not set up.

Installation Order

Install components in dependency order. Foundation components first, then feature components:

Foundation (install first)
pnpm dlx shadcn@latest add button
pnpm dlx shadcn@latest add input label
pnpm dlx shadcn@latest add card

Feature Components (install as needed)
# Forms
pnpm dlx shadcn@latest add form        # needs: react-hook-form, zod, @hookform/resolvers
pnpm dlx shadcn@latest add textarea select checkbox switch

# Feedback
pnpm dlx shadcn@latest add toast        # needs: sonner
pnpm dlx shadcn@latest add alert badge

# Overlay
pnpm dlx shadcn@latest add dialog sheet popover dropdown-menu

# Data Display
pnpm dlx shadcn@latest add table        # for data tables, also: @tanstack/react-table
pnpm dlx shadcn@latest add tabs separator avatar

# Navigation
pnpm dlx shadcn@latest add navigation-menu command

External Dependencies
Component	Requires
Form	react-hook-form, zod, @hookform/resolvers
Toast	sonner
Data Table	@tanstack/react-table
Command	cmdk
Date Picker	date-fns (optional)

Install external deps separately: pnpm add react-hook-form zod @hookform/resolvers

Known Gotchas

These are documented corrections that prevent common bugs:

Radix Select — No Empty Strings
// Don't use empty string values
<SelectItem value="">All</SelectItem>           // BREAKS

// Use sentinel value
<SelectItem value="__any__">All</SelectItem>    // WORKS
const actual = value === "__any__" ? "" : value

React Hook Form — Null Values
// Don't spread {...field} — it passes null which Input rejects
<Input
  value={field.value ?? ''}
  onChange={field.onChange}
  onBlur={field.onBlur}
  name={field.name}
  ref={field.ref}
/>

Lucide Icons — Tree-Shaking
// Don't use dynamic import — icons get tree-shaken in production
import * as LucideIcons from 'lucide-react'
const Icon = LucideIcons[iconName]  // BREAKS in prod

// Use explicit map
import { Home, Users, Settings, type LucideIcon } from 'lucide-react'
const ICON_MAP: Record<string, LucideIcon> = { Home, Users, Settings }
const Icon = ICON_MAP[iconName]

Dialog Width Override
// Default sm:max-w-lg won't be overridden by max-w-6xl
<DialogContent className="max-w-6xl">       // DOESN'T WORK

// Use same breakpoint prefix
<DialogContent className="sm:max-w-6xl">    // WORKS

Customising Components

shadcn components use semantic CSS tokens from your theme. To customise:

Variant extension

Add custom variants by editing the component file in src/components/ui/:

// button.tsx — add a "brand" variant
const buttonVariants = cva("...", {
  variants: {
    variant: {
      default: "bg-primary text-primary-foreground",
      brand: "bg-brand text-brand-foreground hover:bg-brand/90",
      // ... existing variants
    },
  },
})

Colour overrides

Use semantic tokens from your theme — never raw Tailwind colours:

// Don't use raw colours
<Button className="bg-blue-500">             // WRONG

// Use semantic tokens
<Button className="bg-primary">              // RIGHT
<Card className="bg-card text-card-foreground">  // RIGHT

Workflow
Step 1: Assess Needs

Determine what UI patterns the project needs:

Need	Components
Forms with validation	Form, Input, Label, Select, Textarea, Button, Toast
Data display with sorting	Table, Badge, Pagination
Admin CRUD interface	Dialog, Form, Table, Button, Toast
Marketing/landing page	Card, Button, Badge, Separator
Settings/preferences	Tabs, Form, Switch, Select, Toast
Navigation	NavigationMenu (desktop), Sheet (mobile), ModeToggle
Step 2: Install Components

Install foundation first, then feature components for the identified needs. Use the commands above.

Step 3: Build Recipes

Combine components into working patterns. See references/recipes.md for complete working examples:

Contact Form — Form + Input + Textarea + Button + Toast
Data Table — Table + Column sorting + Pagination + Search
Modal CRUD — Dialog + Form + Button
Navigation — Sheet + NavigationMenu + ModeToggle
Settings Page — Tabs + Form + Switch + Select + Toast
Step 4: Customise

Apply project-specific colours and variants using semantic tokens from the theme.

Reference Files
When	Read
Choosing components, install commands, props	references/component-catalogue.md
Building complete UI patterns	references/recipes.md
Weekly Installs
2.4K
Repository
jezweb/claude-skills
GitHub Stars
759
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass