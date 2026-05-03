---
rating: ⭐⭐⭐
title: fdd-architecture
url: https://skills.sh/jenishshrestha/ai-skills/fdd-architecture
---

# fdd-architecture

skills/jenishshrestha/ai-skills/FDD-architecture
FDD-architecture
Installation
$ npx skills add https://github.com/jenishshrestha/ai-skills --skill FDD-architecture
SKILL.md
Feature-Driven Architecture (FDD) for React + Vite

Organizes code by business capability rather than technical type. Each feature is a self-contained module with its own components, hooks, types, and tests.

Project Structure
src/
├── features/           # Feature modules (business capabilities)
│   ├── auth/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── lib/
│   │   ├── types/
│   │   ├── index.ts   # Public API
│   │   └── auth.test.tsx
│   └── dashboard/
│       └── ...
├── shared/            # Shared infrastructure (3+ feature rule)
│   ├── components/
│   │   ├── ui/        # Primitive components (Button, Input)
│   │   ├── layouts/   # Layout wrappers (Header, Sidebar)
│   │   └── providers/ # Global providers (ThemeProvider)
│   ├── hooks/
│   ├── lib/
│   └── types/
└── app/               # App entry and routing
    ├── routes/
    └── main.tsx

React Quality Principles

These apply to all code written in this project, not just architecture.

KISS — Keep It Simple

Prefer standard React patterns over clever abstractions. If the logic is hard to follow without comments, simplify it. Don't reach for complex state management when a useState will do.

YAGNI — You Aren't Gonna Need It

Don't add "just in case" props, speculative abstractions, or premature optimizations. Build for what's needed now. If a prop has no current consumer, remove it.

Composition over Configuration

When a component accumulates 10+ boolean props, it's a sign it should be split into composable pieces using the compound component pattern:

// ❌ Configuration overload
<Card showHeader showFooter isCollapsible hasBorder variant="outlined" />

// ✅ Composition
<Card>
  <Card.Header>Title</Card.Header>
  <Card.Content>Body</Card.Content>
  <Card.Footer>Actions</Card.Footer>
</Card>

Explicit Predictability

Avoid hidden side-effects in useEffect. Prefer explicit event handlers and stable callback references. When something happens, the reader should be able to trace why without hunting through effect dependency arrays.

// ❌ Hidden side-effect — runs on every query change
useEffect(() => {
  trackAnalytics("search", { query });
}, [query]);

// ✅ Explicit — fires on user action
const handleSearch = (query: string) => {
  setQuery(query);
  trackAnalytics("search", { query });
};

Accessibility (a11y)

Every interactive element needs keyboard support, appropriate ARIA attributes, and visible focus indicators. Use semantic HTML elements (button, nav, main) over generic div with role attributes.

FDD Rules — Quick Reference
1. Feature Locality (CRITICAL)

All feature code lives inside src/features/[feature-name]/. Limit nesting to 3 levels max.

src/features/user-profile/
├── components/
│   ├── profile-card.tsx
│   └── avatar-upload.tsx
├── hooks/
│   └── use-profile.ts
├── lib/
│   └── format-name.ts
├── types/
│   └── profile.ts
├── index.ts
└── user-profile.test.tsx

2. Public API Boundary (HIGH)

Every feature exports through index.ts. Never import from a feature's internals.

// src/features/auth/index.ts
export { LoginForm } from "./components/login-form";
export { useAuth } from "./hooks/use-auth";
export type { AuthUser, AuthState } from "./types";

// ❌ Importing from internals
import { LoginButton } from "@/features/auth/components/login-button";

// ✅ Importing from public API
import { LoginButton } from "@/features/auth";

3. Import Conventions (HIGH)

Within a feature — relative paths:

import { useAuth } from "../hooks/use-auth";


Between features — aliases through public API:

import { useAuth } from "@/features/auth";


Types — always use import type:

import type { User } from "./types";

4. Naming Conventions (MEDIUM)
Kind	Convention	Example
Component files (.tsx)	PascalCase	ProductCard.tsx, DataTable.tsx
Hook files (.ts)	camelCase with use prefix	useDataTable.ts, useUserProfile.ts
Type files	kebab-case + .types.ts	product.types.ts, user-profile.types.ts
Schema files	kebab-case + .schema.ts	auth.schema.ts, product.schema.ts
Folders	kebab-case	user-profile/, data-table/
Utilities / lib / api / config	kebab-case	fetch-users.ts, utils.ts

Named imports only — no import *. See rules/naming-consistency.md for details and edge cases.

5. Shared Infrastructure (MEDIUM)

Rule of Three — only promote to src/shared/ after 3+ features use it.

1 feature → keep in feature folder
2 features → keep in original, or duplicate if logic might diverge
3+ features → move to src/shared/
6. Hook Extraction

Extract business logic from components when:

Component has 5+ lines of non-rendering logic
Logic could be reused within the feature
You need to test logic independently
// ❌ Logic mixed with UI
function ProfileCard() {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    fetch('/api/user').then(res => res.json()).then(setUser);
  }, []);
  return <div>{user?.name}</div>;
}

// ✅ Logic extracted to hook
function ProfileCard() {
  const { user, loading } = useUserProfile();
  return <div>{user?.name}</div>;
}

Deep-Dive Rules

For detailed explanations, examples, and edge cases, read the relevant rule file from rules/. Load only what you need:

Rule File	Load When
locality-co-location.md	Creating a new feature, deciding where a file belongs
locality-depth.md	Feature folder is getting deep, need to restructure
api-boundary.md	Setting up index.ts exports, reviewing cross-feature imports
intra-feature-imports.md	Deciding between relative vs absolute import path
naming-consistency.md	Naming a new file or folder
named-imports.md	Import style questions, barrel file setup
shared-global-move.md	Deciding whether to promote code to shared
shared-component-organization.md	Organizing src/shared/components/ subdirectories
hook-extraction.md	Extracting logic from a complex component
Tooling
Vite Path Aliases (vite.config.ts)
export default defineConfig({
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
      "@/features": path.resolve(__dirname, "./src/features"),
      "@/shared": path.resolve(__dirname, "./src/shared"),
    },
  },
});

TypeScript Paths (tsconfig.json)
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"],
      "@/features/*": ["./src/features/*"],
      "@/shared/*": ["./src/shared/*"]
    }
  }
}

ESLint — Enforce Public API Boundary
{
  "rules": {
    "no-restricted-imports": [
      "error",
      {
        "patterns": [
          {
            "group": ["@/features/*/components/*", "@/features/*/hooks/*"],
            "message": "Import from feature's public API (index.ts) only"
          }
        ]
      }
    ]
  }
}

Feature-Based Code Splitting (TanStack Router)
const dashboardRoute = createRoute({
  path: "/dashboard",
  component: () => import("@/features/dashboard").then((m) => m.DashboardPage),
});


For migration guides (flat structure → FDD, Next.js → Vite), see references/migration.md.

Weekly Installs
19
Repository
jenishshrestha/ai-skills
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass