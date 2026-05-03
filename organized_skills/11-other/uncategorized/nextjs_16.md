---
rating: ⭐⭐
title: nextjs-16
url: https://skills.sh/fusengine/agents/nextjs-16
---

# nextjs-16

skills/fusengine/agents/nextjs-16
nextjs-16
Installation
$ npx skills add https://github.com/fusengine/agents --skill nextjs-16
SKILL.md
Next.js 16 Expert

Production-ready React framework with Server Components, streaming, and Turbopack.

Agent Workflow (MANDATORY)

Before ANY implementation, use TeamCreate to spawn 3 agents:

fuse-ai-pilot:explore-codebase - Analyze existing routes, components, and patterns
fuse-ai-pilot:research-expert - Verify latest Next.js 16 docs via Context7/Exa
mcp__context7__query-docs - Check breaking changes v15→v16

After implementation, run fuse-ai-pilot:sniper for validation.

Overview
When to Use
Building new React applications with server-first architecture
Need Server Components for optimal performance and SEO
Implementing streaming and progressive rendering
Migrating from Next.js 14/15 to version 16
Using proxy.ts for route protection (replaces middleware)
Leveraging Turbopack for faster development builds
Why Next.js 16
Feature	Benefit
Turbopack default	2-5x faster builds, 10x faster HMR, Webpack deprecated
Cache Components	Explicit caching with use cache directive
proxy.ts	Full Node.js runtime, replaces Edge middleware
React Compiler	Automatic memoization, no manual useMemo/useCallback
React 19	View Transitions, useEffectEvent, Activity component
App Router	Nested layouts, parallel routes, intercepting routes
Breaking Changes from v15
Critical Migration Points
proxy.ts replaces middleware.ts - Full Node.js runtime, not Edge
Turbopack ONLY - Webpack completely deprecated and removed
use cache directive - Replaces Partial Prerendering (PPR)
React 19 required - New hooks and View Transitions API
Async params/searchParams - Must await dynamic route params
SOLID Architecture
Module-Based Structure

Pages are thin entry points importing from feature modules:

app/page.tsx → imports from modules/public/home/
app/dashboard/page.tsx → imports from modules/auth/dashboard/
modules/cores/ → Shared services, utilities, configurations
File Conventions
page.tsx - Route UI component
layout.tsx - Shared UI wrapper
loading.tsx - Suspense loading state
error.tsx - Error boundary
not-found.tsx - 404 handling
Core Concepts
Server Components (Default)

All components are Server Components by default. Use 'use client' directive only when needed for interactivity, hooks, or browser APIs.

Caching Strategy
use cache - Mark async functions for caching
cacheTag() - Tag cached data for targeted revalidation
cacheLife() - Control cache duration (stale, revalidate, expire)
revalidateTag() - Invalidate cached data on-demand
Data Fetching

Server Components fetch data directly. Use fetch() with native caching or database queries. No need for getServerSideProps or getStaticProps.

Reference Guide
Need	Reference
Initial setup	installation.md, project-structure.md
Migration v15→v16	upgrade.md, middleware-migration.md
Routing	app-router.md, routing-advanced.md
Caching	caching.md, cache-components.md
Server Components	server-components.md, directives.md
React 19 features	react-19.md, react-compiler.md
Route protection	proxy.md, security.md
SEO/Metadata	metadata.md, metadata-files.md
Forms/Actions	forms.md, data-fetching.md
Deployment	deployment.md, environment.md
Best Practices
Server Components first - Only add 'use client' when necessary
Colocate data fetching - Fetch data where it's used
Streaming with Suspense - Wrap slow components in Suspense
proxy.ts over middleware - Full Node.js runtime for auth
Cache explicitly - Use use cache for expensive operations
Parallel routes - Load independent UI sections simultaneously
Performance
Build Optimization
Turbopack - Incremental compilation, instant HMR
React Compiler - Automatic memoization
Tree shaking - Unused code elimination
Code splitting - Automatic route-based splitting
Runtime Optimization
Streaming - Progressive HTML rendering
Partial hydration - Only hydrate interactive components
Image optimization - Automatic WebP/AVIF conversion
Font optimization - Zero layout shift with next/font
Weekly Installs
36
Repository
fusengine/agents
GitHub Stars
11
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass