---
title: laravel-inertia-react-structure
url: https://skills.sh/freekmurze/dotfiles/laravel-inertia-react-structure
---

# laravel-inertia-react-structure

skills/freekmurze/dotfiles/laravel-inertia-react-structure
laravel-inertia-react-structure
Installation
$ npx skills add https://github.com/freekmurze/dotfiles --skill laravel-inertia-react-structure
SKILL.md
Laravel Inertia React Frontend Structure

Based on Spatie's conventions for structuring production Laravel Inertia React applications.

Directory Structure

Four base directories under resources/js:

resources/js/
├── common/       # Generic, reusable code portable across projects
├── modules/      # Project-specific code shared across multiple pages
├── pages/        # Inertia page components
└── shadcn/       # Auto-generated shadcn/ui components (if used)


common vs modules: ask "Does it relate to a domain or feature?" If yes → modules. If it's generic and project-agnostic → common.

Naming Conventions
Components and React contexts: PascalCase (e.g. Button.tsx, AuthContext.tsx)
Other files (helpers, hooks, constants, stores): camelCase (e.g. useAuth.ts, formatDate.ts)
Directories: kebab-case (e.g. date-picker/, user-management/)
Module Organization

Small modules have a few top-level files. Larger modules organize by type:

modules/agenda/
├── components/
├── contexts/
├── constants/
├── helpers/
├── hooks/
├── stores/
└── types.ts          # or types/ directory if large


The common/ directory follows the same structure.

Pages Directory

Pages mirror the URL structure. Components are suffixed with Page.

pages/
├── layouts/              # Global layouts
├── admin/
│   ├── layouts/          # Section-specific layouts
│   ├── users/
│   │   ├── components/   # Page-specific partials
│   │   ├── helpers/
│   │   ├── IndexPage.tsx
│   │   └── EditPage.tsx
│   └── DashboardPage.tsx
└── auth/
    ├── LoginPage.tsx
    └── RegisterPage.tsx

React Component Conventions

Use function declarations (not const arrow functions) and named exports exclusively:

// Correct
export function Button({ variant, className }: ButtonProps) {
  return <button className={cn(variant, className)}>Click</button>;
}

// Wrong: const + default export
const Button = ({ variant }) => { ... };
export default Button;


One component per file. No barrel files (index.ts re-exports).

Import Organization

Two blocks separated by a blank line: library imports first, then application imports. Use absolute paths with aliases (@/):

import { useState } from "react";
import { cn } from "@/common/helpers/cn";

import { useAgenda } from "@/modules/agenda/hooks/useAgenda";
import { AgendaItem } from "@/modules/agenda/components/AgendaItem";

Props

Sort alphabetically, with className and children last:

interface DialogProps {
  onClose: () => void;
  open: boolean;
  title: string;
  className?: string;
  children: React.ReactNode;
}

Stylesheets

Use Tailwind. Single app.css for most projects. Larger projects split into:

resources/css/
├── base/
├── components/
└── utilities/

Multi-Zone Applications

For apps with distinct sections (e.g. admin/client), introduce apps/:

resources/js/
├── common/           # Shared across all zones
├── modules/          # Global modules shared across zones
├── apps/
│   ├── admin/
│   │   ├── modules/  # Admin-specific modules
│   │   ├── pages/
│   │   └── app.tsx
│   └── client/
│       ├── modules/  # Client-specific modules
│       ├── pages/
│       └── app.tsx
└── shadcn/

shadcn/ui Usage

Abstract shadcn components into simpler, project-specific implementations rather than using the low-level API directly in application code. Place abstractions in common/ or modules/ as appropriate.

Weekly Installs
18
Repository
freekmurze/dotfiles
GitHub Stars
939
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass