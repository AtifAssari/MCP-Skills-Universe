---
title: nuxt
url: https://skills.sh/antfu/skills/nuxt
---

# nuxt

skills/antfu/skills/nuxt
nuxt
Installation
$ npx skills add https://github.com/antfu/skills --skill nuxt
Summary

Full-stack Vue framework with SSR, file-based routing, auto-imports, and universal deployment via Nitro.

Covers core concepts including directory structure, configuration, CLI commands, file-based routing with middleware and layouts, and data fetching with useFetch and useAsyncData
Supports three rendering modes: universal SSR, client-side SPA, and hybrid rendering with route-level control
Includes auto-import systems for composables and components, built-in components like NuxtLink and NuxtPage, and server routes powered by Nitro
Provides state management via useState composable, module authoring with Nuxt Kit, and deployment across Node.js, serverless, and edge platforms
SKILL.md

Nuxt is a full-stack Vue framework that provides server-side rendering, file-based routing, auto-imports, and a powerful module system. It uses Nitro as its server engine for universal deployment across Node.js, serverless, and edge platforms.

The skill is based on Nuxt 3.x, generated at 2026-01-28.

Core
Topic	Description	Reference
Directory Structure	Project folder structure, conventions, file organization	core-directory-structure
Configuration	nuxt.config.ts, app.config.ts, runtime config, environment variables	core-config
CLI Commands	Dev server, build, generate, preview, and utility commands	core-cli
Routing	File-based routing, dynamic routes, navigation, middleware, layouts	core-routing
Data Fetching	useFetch, useAsyncData, $fetch, caching, refresh	core-data-fetching
Modules	Creating and using Nuxt modules, Nuxt Kit utilities	core-modules
Deployment	Platform-agnostic deployment with Nitro, Vercel, Netlify, Cloudflare	core-deployment
Features
Topic	Description	Reference
Composables Auto-imports	Vue APIs, Nuxt composables, custom composables, utilities	features-composables
Components Auto-imports	Component naming, lazy loading, hydration strategies	features-components-autoimport
Built-in Components	NuxtLink, NuxtPage, NuxtLayout, ClientOnly, and more	features-components
State Management	useState composable, SSR-friendly state, Pinia integration	features-state
Server Routes	API routes, server middleware, Nitro server engine	features-server
Rendering
Topic	Description	Reference
Rendering Modes	Universal (SSR), client-side (SPA), hybrid rendering, route rules	rendering-modes
Best Practices
Topic	Description	Reference
Data Fetching Patterns	Efficient fetching, caching, parallel requests, error handling	best-practices-data-fetching
SSR & Hydration	Avoiding context leaks, hydration mismatches, composable patterns	best-practices-ssr
Advanced
Topic	Description	Reference
Layers	Extending applications with reusable layers	advanced-layers
Lifecycle Hooks	Build-time, runtime, and server hooks	advanced-hooks
Module Authoring	Creating publishable Nuxt modules with Nuxt Kit	advanced-module-authoring
Weekly Installs
14.1K
Repository
antfu/skills
GitHub Stars
4.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn