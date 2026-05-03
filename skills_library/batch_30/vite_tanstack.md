---
title: vite-tanstack
url: https://skills.sh/jsonlee12138/prompts/vite-tanstack
---

# vite-tanstack

skills/jsonlee12138/prompts/vite-tanstack
vite-tanstack
Installation
$ npx skills add https://github.com/jsonlee12138/prompts --skill vite-tanstack
SKILL.md
Vite + TanStack Configuration Guide

Provides configuration references for TanStack libraries in a Vite + React + TypeScript project.

Modules

Four optional modules — load only what's needed:

Module	What it covers
router	Vite plugin, createRouter, RouterProvider, type registration, VSCode settings
query	QueryClient init, QueryClientProvider
form	Form provider setup
table	react-table initialization

All modules share a unified DevTools setup via @tanstack/react-devtools + @tanstack/devtools-vite.

Argument Parsing

From $ARGUMENTS:

Module names: router, query, form, table (space-separated, any combination)
all — load all four modules
No arguments — ask user which modules they need using AskUserQuestion (multiSelect)

Examples:

/vite-tanstack router query → load router.md + query.md
/vite-tanstack all → load all four references
/vite-tanstack → ask which modules are needed
Shared Configuration
Package Dependencies

dependencies:

@tanstack/react-devtools
@tanstack/react-router           (if router)
@tanstack/react-router-devtools  (if router)
@tanstack/react-query            (if query)
@tanstack/react-query-devtools   (if query)
@tanstack/react-form             (if form)
@tanstack/react-form-devtools    (if form)
@tanstack/react-table            (if table)


devDependencies:

@tanstack/devtools-vite
@tanstack/router-plugin          (if router)

Vite Plugin: Unified DevTools

In vite.config.ts, always register the devtools plugin:

import { devtools } from '@tanstack/devtools-vite';

export default defineConfig({
  plugins: [
    devtools({
      removeDevtoolsOnBuild: true,
    }),
    // ... other plugins
  ],
});

main.tsx: TanStackDevtools Component

In main.tsx, the TanStackDevtools component wraps all module-specific devtools panels as plugins:

import { TanStackDevtools } from '@tanstack/react-devtools';

// Inside render tree:
<TanStackDevtools
  plugins={[
    // Add each module's devtools panel as a plugin here
    // See individual module references for specifics
  ]}
/>


Component nesting order: QueryClientProvider wraps TanStackDevtools + RouterProvider. Each module reference shows its specific position.

Module References

Load these based on requested modules:

Router: See references/router.md for Vite plugin, router creation, type registration, VSCode settings, and Router DevTools panel
Query: See references/query.md for QueryClient initialization, provider setup, and Query DevTools panel
Form: See references/form.md for Form provider setup and Form DevTools panel
Table: See references/table.md for react-table initialization
Compliance Checklist

When reviewing or writing TanStack config code, verify:

 @tanstack/devtools-vite plugin registered in vite.config.ts with removeDevtoolsOnBuild: true
 TanStackDevtools component present in render tree with appropriate module panels
 Each module's provider is registered in correct nesting order
 TypeScript module augmentation declared for router (if using router)
 VSCode settings configured for generated files (if using router)
Weekly Installs
15
Repository
jsonlee12138/prompts
GitHub Stars
1
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass