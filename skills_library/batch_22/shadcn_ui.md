---
title: shadcn-ui
url: https://skills.sh/faqndo97/ai-skills/shadcn-ui
---

# shadcn-ui

skills/faqndo97/ai-skills/shadcn-ui
shadcn-ui
Installation
$ npx skills add https://github.com/faqndo97/ai-skills --skill shadcn-ui
SKILL.md

<essential_principles>

How shadcn/ui Works

shadcn/ui is NOT a component library - it's a collection of re-usable components you copy into your project and own. This philosophy changes everything about how you work with it.

1. You Own the Code

Components are copied directly into your components/ui/ directory. You can and should modify them. Don't wrap components - edit them directly. This is intentional.

# Install a component
npx shadcn@latest add button

# Components land in your project
# src/components/ui/button.tsx

2. Composition Over Monoliths

Build complex UIs by composing primitives. Every component follows consistent patterns:

Radix UI primitives for accessibility
CVA (class-variance-authority) for variants
cn() utility for conditional classes
data-slot attributes for styling hooks
// Composition pattern - build from primitives
<Dialog>
  <DialogTrigger asChild>
    <Button variant="outline">Open</Button>
  </DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Title</DialogTitle>
      <DialogDescription>Description</DialogDescription>
    </DialogHeader>
    {/* Content */}
    <DialogFooter>
      <Button>Save</Button>
    </DialogFooter>
  </DialogContent>
</Dialog>

3. The asChild Pattern

Use asChild prop to merge behavior onto a different element. Critical for navigation, forms, and custom triggers.

// asChild merges Button behavior onto Link
<Button asChild>
  <Link href="/dashboard">Dashboard</Link>
</Button>

// asChild on DialogTrigger
<DialogTrigger asChild>
  <Button>Open Dialog</Button>
</DialogTrigger>

4. Variant-Driven Design

Use CVA for consistent variant APIs. Every button, badge, and alert follows this pattern:

const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md...", // Base
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground",
        destructive: "bg-destructive text-white",
        outline: "border bg-background",
        ghost: "hover:bg-accent",
      },
      size: {
        default: "h-9 px-4",
        sm: "h-8 px-3",
        lg: "h-10 px-6",
        icon: "size-9",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

5. CSS Variables for Theming

All colors use CSS variables. Theme by changing variables, not component code:

/* Light mode */
:root {
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;
  --primary: 222.2 47.4% 11.2%;
  --primary-foreground: 210 40% 98%;
}

/* Dark mode */
.dark {
  --background: 222.2 84% 4.9%;
  --foreground: 210 40% 98%;
}

6. React 19 Patterns

shadcn/ui uses modern React patterns - no forwardRef (React 19), data-slot attributes, and function components:

// Modern pattern (no forwardRef in React 19)
function Button({ className, variant, size, asChild = false, ...props }) {
  const Comp = asChild ? Slot : "button"
  return (
    <Comp
      data-slot="button"
      className={cn(buttonVariants({ variant, size, className }))}
      {...props}
    />
  )
}


</essential_principles>

Add a new shadcn component to the project
Build a form with validation
Build a data table with sorting/filtering
Customize an existing component
Create a compound component
Add animations/transitions
Set up or modify theming
Debug a component issue
Something else

Then read the matching workflow from workflows/ and follow it.

After reading the workflow, follow it exactly.

<verification_loop>

After Every Change
TypeScript compiles?
bunx tsc --noEmit


Component renders? Check the dev server - no console errors

Accessibility check:

Keyboard navigation works
Focus states visible
ARIA attributes present
Visual check:
Matches design intent
Works in light/dark mode
Responsive on mobile

Report: "TypeScript: ✓ | Renders: ✓ | A11y: ✓ | Visual: ✓" </verification_loop>

<reference_index>

Domain Knowledge

All in references/:

Core:

core-components.md - Button, Input, Label, Card, Badge, etc.
composition-patterns.md - asChild, Slot, compound components

Forms:

form-components.md - Form, Field, Input, Select, Combobox, etc.
form-validation.md - Zod, React Hook Form, TanStack Form

Data Display:

data-table.md - TanStack Table integration
data-components.md - Kanban, Gantt, List, Calendar

Navigation:

navigation-components.md - Sidebar, Tabs, Breadcrumb, Command

Overlays:

overlay-components.md - Dialog, Sheet, Drawer, Popover, Tooltip

Feedback:

feedback-components.md - Toast/Sonner, Alert, Progress, Skeleton

Hooks:

hooks.md - useLocalStorage, useMediaQuery, useDebounce, etc.

Animation:

animation-patterns.md - Framer Motion, micro-interactions

Theming:

theming.md - CSS variables, dark mode, color system

Advanced:

cli-registry.md - CLI commands, custom registries
accessibility.md - WCAG compliance, keyboard navigation </reference_index>

<workflows_index>

Workflows

All in workflows/:

File	Purpose
add-component.md	Install and configure a shadcn component
build-form.md	Build forms with validation
build-data-table.md	Build tables with TanStack Table
customize-component.md	Modify existing components
build-compound-component.md	Create new compound components
add-animations.md	Add Framer Motion animations
setup-theming.md	Configure theming and dark mode
debug-component.md	Troubleshoot component issues
</workflows_index>	
Weekly Installs
14
Repository
faqndo97/ai-skills
GitHub Stars
32
First Seen
1 day ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass