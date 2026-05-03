---
title: nuxt
url: https://skills.sh/onmax/nuxt-skills/nuxt
---

# nuxt

skills/onmax/nuxt-skills/nuxt
nuxt
Installation
$ npx skills add https://github.com/onmax/nuxt-skills --skill nuxt
Summary

Nuxt 4+ development guidance covering server routes, file-based routing, middleware, composables, and configuration patterns.

Organized reference files for API endpoints, server middleware, routing, middleware/plugins, Nuxt composables, components, and configuration
Includes h3 v1 helpers for validation, WebSocket, and SSE; Nitro v2 patterns; and typed router support
Highlights Nuxt 4 breaking changes (NuxtPage vs Nuxt, getRouterParam, useRequestURL) with migration examples
Cross-references related skills (vue, nuxt-ui, nuxthub, nuxt-content, nuxt-modules) to avoid duplication and keep token usage efficient
SKILL.md
Nuxt 4+ Development

Progressive guidance for Nuxt 4+ projects (v4.3+) with latest patterns and conventions.

When to Use

Working with:

Server routes (API endpoints, server middleware, server utils)
File-based routing (pages, layouts, route groups)
Nuxt middleware (route guards, navigation)
Nuxt plugins (app extensions)
Nuxt-specific features (auto-imports, layers, modules)
Available Guidance

Read specific files based on current work:

references/server.md - API routes, server middleware, validation (Zod), WebSocket, SSE
references/routing.md - File-based routing, route groups, typed router, definePage
references/middleware-plugins.md - Route middleware, plugins, app lifecycle
references/nuxt-composables.md - Nuxt composables (useRequestURL, useFetch, navigation)
references/nuxt-components.md - NuxtLink, NuxtImg, NuxtTime (prefer over HTML elements)
references/nuxt-config.md - Configuration, modules, auto-imports, layers

For Vue composables: See vue skill composables.md (VueUse, Composition API patterns) For UI components: use nuxt-ui skill For database/storage: use nuxthub skill For content-driven sites: use nuxt-content skill For creating modules: use nuxt-modules skill For project scaffolding/CI: use ts-library skill

Loading Files

Consider loading these reference files based on your task:

 references/server.md - if creating API endpoints or server middleware
 references/routing.md - if setting up pages, layouts, or route groups
 references/nuxt-composables.md - if using Nuxt composables (useFetch, useRequestURL, etc.)
 references/middleware-plugins.md - if working with middleware or plugins
 references/nuxt-components.md - if using Nuxt components (NuxtLink, NuxtImg, etc.)
 references/nuxt-config.md - if editing nuxt.config.ts
 references/project-setup.md - if setting up CI/ESLint/build tools

DO NOT load all files at once. Load only what's relevant to your current task.

Quick Start
// server/api/hello.get.ts
import { z } from 'zod'

export default defineEventHandler(async (event) => {
  const { name } = await getValidatedQuery(event, z.object({
    name: z.string().default('world'),
  }).parse)
  return { message: `Hello ${name}` }
})

Nuxt 4 vs Older Versions

You are working with Nuxt 4+. Key differences:

Old (Nuxt 2/3)	New (Nuxt 4)
<Nuxt />	<NuxtPage />
context.params	getRouterParam(event, 'name')
window.origin	useRequestURL().origin
String routes	Typed router with route names
Separate layouts/	Parent routes with <slot>

If you're unsure about Nuxt 4 patterns, read the relevant guidance file first.

Latest Documentation

When to fetch latest docs:

New Nuxt 4 features not covered here
Module-specific configuration
Breaking changes or deprecations
Advanced use cases

Official sources:

Nuxt: https://nuxt.com/docs
h3 (server engine): https://v1.h3.dev/
Nitro: https://nitro.build/
Token Efficiency

Main skill: ~300 tokens. Each sub-file: ~800-1500 tokens. Only load files relevant to current task.

Weekly Installs
6.0K
Repository
onmax/nuxt-skills
GitHub Stars
649
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn