---
title: nextjs
url: https://skills.sh/faqndo97/ai-skills/nextjs
---

# nextjs

skills/faqndo97/ai-skills/nextjs
nextjs
Installation
$ npx skills add https://github.com/faqndo97/ai-skills --skill nextjs
SKILL.md

<essential_principles>

How Next.js 16 Works

Next.js 16 uses the App Router with React Server Components by default. It introduces Cache Components with the "use cache" directive, Turbopack as the default bundler, and React 19.2 features.

1. Server-First Rendering

Components are Server Components by default. They:

Run only on the server
Can directly fetch data (no useEffect needed)
Cannot use hooks, event handlers, or browser APIs
Reduce client JavaScript bundle

Add 'use client' only when you need interactivity, state, or browser APIs.

2. BFF Pattern (Backend for Frontend)

Next.js acts as an intermediate layer between your React UI and backend APIs:

Server Components fetch data from Rails during render
Server Actions handle mutations by calling Rails APIs
Route Handlers provide API endpoints when needed (webhooks, external integrations)

Keep sensitive logic (tokens, API keys) in the server layer - never expose to client.

3. Cache Components (New in Next.js 16)

Next.js 16 introduces explicit, opt-in caching with the "use cache" directive:

// next.config.ts
const nextConfig = {
  cacheComponents: true,
};

"use cache"

export async function getProducts() {
  // This function is cached
  return await db.products.findMany()
}

All dynamic code runs at request time by default
Use "use cache" to opt-in to caching pages, components, and functions
Compiler automatically generates cache keys
Replaces experimental.dynamicIO and experimental.ppr flags
4. New Caching APIs

revalidateTag(tag, profile) - Now requires a cacheLife profile:

revalidateTag('products', 'max')  // Built-in profiles: 'max', 'hours', 'days'
revalidateTag('products', { revalidate: 3600 })  // Custom time


updateTag(tag) - New! Immediate refresh (read-your-writes):

import { updateTag } from 'next/cache'
// Use in Server Actions for instant UI updates
updateTag('user-profile')


refresh() - New! Refresh uncached data only:

import { refresh } from 'next/cache'
// Use in Server Actions to refresh uncached data (notifications, metrics)
refresh()

5. File-Based Conventions

Special files in app/ directory:

page.tsx - Route UI
layout.tsx - Shared wrapper (persists across navigations)
loading.tsx - Suspense fallback
error.tsx - Error boundary
route.ts - API endpoint (Route Handler)
proxy.ts - Network boundary (replaces middleware.ts)
6. Turbopack (Default Bundler)

Turbopack is now the default bundler:

2-5× faster production builds
Up to 10× faster Fast Refresh
Opt out with next dev --webpack or next build --webpack
7. React 19.2 Features

Next.js 16 includes React 19.2 with:

View Transitions - Animate elements during navigation/state updates
Activity - Hide UI with display: none while maintaining state
useEffectEvent - Extract non-reactive logic from Effects

</essential_principles>

Build a new Next.js app
Add a page or feature
Add a Server Action (mutation)
Add a Route Handler (API endpoint)
Debug an issue
Write tests
Optimize performance
Ship/deploy

Then read the matching workflow from workflows/ and follow it.

After reading the workflow, follow it exactly.

<verification_loop>

After Every Change
# 1. TypeScript compiles?
bunx tsc --noEmit

# 2. Lint passes?
bun run lint

# 3. Dev server runs?
bun run dev


Check browser for:

No hydration errors in console
No "use client" / "use server" boundary violations
Data loads correctly from Rails API

Report to user:

"TypeScript: ✓"
"Lint: ✓"
"Dev server: Running on localhost:3000"
"Ready for you to verify [specific feature]"

</verification_loop>

<reference_index>

Domain Knowledge

All in references/:

Architecture: app-router.md, project-structure.md, bff-patterns.md Components: server-components.md, client-components.md Data: data-fetching.md, server-actions.md, route-handlers.md Navigation: redirecting.md UX: loading-streaming.md, error-handling.md Configuration: environment-variables.md, scripts.md Security: security.md Quality: typescript.md, testing.md, performance.md, accessibility.md, anti-patterns.md

</reference_index>

<workflows_index>

Workflows

All in workflows/:

File	Purpose
build-new-app.md	Create Next.js 16 app from scratch
add-page.md	Add pages, components, layouts
add-server-action.md	Server Actions for mutations
add-route-handler.md	API endpoints (Route Handlers)
debug-app.md	Fix errors, hydration issues, build failures
write-tests.md	Unit, integration, E2E testing
optimize-performance.md	Core Web Vitals, bundle size, caching
ship-app.md	Deploy to Vercel, Docker, etc.

</workflows_index>

Weekly Installs
9
Repository
faqndo97/ai-skills
GitHub Stars
32
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass