---
rating: ⭐⭐⭐
title: component-organization
url: https://skills.sh/loxosceles/ai-dev/component-organization
---

# component-organization

skills/loxosceles/ai-dev/component-organization
component-organization
Installation
$ npx skills add https://github.com/loxosceles/ai-dev --skill component-organization
SKILL.md
Frontend Component Organization

This is a reference pattern. Learn from the approach, adapt to your context — don't copy verbatim.

Problem: Frontend projects grow into disorganized directories where related files are hard to find and shared code has no clear home.

Solution: Organize by type (components, hooks, lib, types), with subdirectories for grouping related items within each type.

Pattern
frontend/
├── app/                 # Framework routing (Next.js app dir, Nuxt pages, etc.)
│   ├── layout.tsx
│   └── page.tsx
├── components/          # All components
│   ├── ui/              # Base primitives (Button, Input, Modal)
│   ├── UserProfile.tsx
│   ├── DashboardChart.tsx
│   └── PostCard.tsx
├── hooks/               # Custom hooks
│   ├── use-auth.ts
│   ├── use-dashboard.ts
│   └── use-debounce.ts
├── lib/                 # Utilities, services, business logic
│   ├── api/             # API client, fetch helpers
│   ├── auth/            # Auth context, cookie handling
│   └── utils/           # Pure helper functions
├── queries/             # Data fetching (GraphQL queries, API calls)
├── types/               # Shared type definitions
│   ├── user.ts
│   └── post.ts
└── public/              # Static assets


Key Rules:

Components live in components/, grouped by subdirectory when related (e.g., ui/)
Hooks live in hooks/, one hook per file
Business logic lives in lib/, organized by domain subdirectory
Types shared across files live in types/
Base UI primitives (buttons, inputs, modals) live in components/ui/
Why This Pattern?

Benefits:

Predictable: Know exactly where to look — all hooks in hooks/, all components in components/
Reusability: Components used across multiple features are easy to find and share
Scalability: Adding a new hook or component has an obvious home
Natural for component libraries: Matches how shared UI kits are structured

When to use subdirectories within a type:

components/ui/ — base primitives reused everywhere
lib/auth/ — multiple files for one domain (context + utils + types)
lib/api/ — API client, interceptors, helpers
When to Split
New file in components/: When UI is reused or the parent component exceeds ~200 lines
New file in hooks/: When stateful logic is reused or clutters a component
New subdirectory in lib/: When a domain has 2+ related files (service + utils, context + helpers)
Move to components/ui/: When a component is purely presentational with no business logic
Progressive Improvement

If the developer corrects a behavior that this skill should have prevented, suggest a specific amendment to this skill to prevent the same correction in the future.

Weekly Installs
39
Repository
loxosceles/ai-dev
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass