---
title: shadcn
url: https://skills.sh/markhamsquareventures/essentials/shadcn
---

# shadcn

skills/markhamsquareventures/essentials/shadcn
shadcn
Installation
$ npx skills add https://github.com/markhamsquareventures/essentials --skill shadcn
SKILL.md
shadcn/ui
Instructions

This project uses shadcn/ui with the New York style variant. Components are built on Radix UI primitives with Tailwind CSS styling.

Configuration
Style: new-york
Base color: neutral
Icons: lucide-react
Components location: resources/js/components/ui/
Utils location: resources/js/lib/utils.ts
Adding New Components

Use the shadcn CLI to add components:

npx shadcn@latest add <component-name>


Examples:

npx shadcn@latest add table
npx shadcn@latest add tabs
npx shadcn@latest add calendar


Do NOT manually create shadcn components - always use the CLI to ensure correct styling and dependencies.

Available Components

Components already installed in this project:

alert
alert-dialog
avatar
badge
breadcrumb
button
card
checkbox
collapsible
dialog
dropdown-menu
input, input-otp
label
navigation-menu
select
separator
sheet
sidebar
skeleton
sonner (toast notifications)
spinner
toggle, toggle-group
tooltip
Using Components

Always import from @/components/ui/:

Button Variants

{/_ Sizes _/} Small Default Large

Form Patterns

Use Label + Input together, with proper error styling:

Dialog Pattern
Toast Notifications

Use Sonner for toast notifications:

// Success toast.success('Changes saved successfully');

// Error toast.error('Something went wrong');

// With description toast.success('Project created', { description: 'Your new project is ready to use.', });

The cn() Utility

Use cn() from @/lib/utils to merge Tailwind classes conditionally:

Icons

Use Lucide React for icons:

Weekly Installs
26
Repository
markhamsquareve…sentials
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass