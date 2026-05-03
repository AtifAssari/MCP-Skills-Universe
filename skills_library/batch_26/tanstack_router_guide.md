---
title: tanstack-router-guide
url: https://skills.sh/vcode-sh/vibe-tools/tanstack-router-guide
---

# tanstack-router-guide

skills/vcode-sh/vibe-tools/tanstack-router-guide
tanstack-router-guide
Installation
$ npx skills add https://github.com/vcode-sh/vibe-tools --skill tanstack-router-guide
SKILL.md
TanStack Router Guide (React)

TanStack Router is a fully type-safe, file-based router for React. It provides first-class search param APIs, built-in data loading with SWR caching, automatic code splitting, and 100% inferred TypeScript types. Designed for client-first SPAs with optional SSR support.

Install
npm install @tanstack/react-router
npm install -D @tanstack/router-plugin
# Optional: devtools
npm install @tanstack/react-router-devtools

Quick Start with Vite (Recommended)

1. Configure Vite:

// vite.config.ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { tanstackRouter } from '@tanstack/router-plugin/vite'

export default defineConfig({
  plugins: [
    tanstackRouter({ target: 'react', autoCodeSplitting: true }),
    react(), // Must come AFTER tanstackRouter
  ],
})


2. Create root route:

// src/routes/__root.tsx
import { createRootRoute, Link, Outlet } from '@tanstack/react-router'
import { TanStackRouterDevtools } from '@tanstack/react-router-devtools'

export const Route = createRootRoute({
  component: () => (
    <>
      <nav>
        <Link to="/" activeProps={{ className: 'font-bold' }}>Home</Link>
        <Link to="/about" activeProps={{ className: 'font-bold' }}>About</Link>
      </nav>
      <Outlet />
      <TanStackRouterDevtools />
    </>
  ),
})


3. Create routes:

// src/routes/index.tsx
import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/')({
  component: () => <div>Welcome Home!</div>,
})

// src/routes/about.tsx
export const Route = createFileRoute('/about')({
  component: () => <div>About Page</div>,
})


4. Mount the router:

// src/main.tsx
import { StrictMode } from 'react'
import ReactDOM from 'react-dom/client'
import { RouterProvider, createRouter } from '@tanstack/react-router'
import { routeTree } from './routeTree.gen'

const router = createRouter({ routeTree })

// Register router type globally for type safety
declare module '@tanstack/react-router' {
  interface Register {
    router: typeof router
  }
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)

File-Based Routing (Naming Conventions)

Routes live in src/routes/ and file names determine URL paths:

File Name	URL Path	Purpose
__root.tsx	N/A	Root layout (always rendered)
index.tsx	/	Index route
about.tsx	/about	Static route
posts.tsx	/posts	Layout route (renders Outlet)
posts.index.tsx	/posts	Index for /posts
posts.$postId.tsx	/posts/:postId	Dynamic segment
_auth.tsx	N/A	Pathless layout (wraps children, no URL)
_auth.dashboard.tsx	/dashboard	Child of pathless layout
posts_.$postId.edit.tsx	/posts/:postId/edit	Non-nested (escapes parent layout)
files.$.tsx	/files/*	Splat/catch-all route
posts.{-$category}.tsx	/posts/:category?	Optional path parameter
-utils.tsx	N/A	Excluded from routing
(group)/login.tsx	/login	Route group (organizational only)

The plugin auto-generates routeTree.gen.ts - commit this file but never edit it manually.

Navigation
import { Link, useNavigate } from '@tanstack/react-router'

// Declarative - Link component
<Link to="/posts/$postId" params={{ postId: '123' }}>View Post</Link>
<Link to="/posts" search={{ page: 2, sort: 'asc' }}>Page 2</Link>
<Link to=".." from="/posts/$postId">Back to Posts</Link>

// Active styling
<Link to="/about" activeProps={{ className: 'active' }} inactiveProps={{ className: 'dim' }}>
  About
</Link>

// Programmatic - useNavigate
const navigate = useNavigate()
navigate({ to: '/posts/$postId', params: { postId: '123' } })
navigate({ to: '/posts', search: (prev) => ({ ...prev, page: 2 }) })
navigate({ to: '..', from: '/posts/$postId' }) // Relative

Search Params (Validated & Type-Safe)
import { createFileRoute } from '@tanstack/react-router'
import { z } from 'zod'

export const Route = createFileRoute('/posts')({
  validateSearch: z.object({
    page: z.number().catch(1),
    sort: z.enum(['asc', 'desc']).optional(),
    filter: z.string().optional(),
  }),
  component: PostsPage,
})

function PostsPage() {
  const { page, sort, filter } = Route.useSearch() // Fully typed
  const navigate = Route.useNavigate()

  return (
    <button onClick={() => navigate({ search: (prev) => ({ ...prev, page: prev.page + 1 }) })}>
      Next Page
    </button>
  )
}


Search Middlewares - retain or strip params across navigations:

import { retainSearchParams, stripSearchParams } from '@tanstack/react-router'

export const Route = createFileRoute('/posts')({
  validateSearch: z.object({ page: z.number().catch(1), q: z.string().optional() }),
  search: {
    middlewares: [
      retainSearchParams(['q']),        // Keep 'q' across navigations
      stripSearchParams({ page: 1 }),    // Strip 'page' when it equals default
    ],
  },
})

Data Loading
// Basic loader with path params
export const Route = createFileRoute('/posts/$postId')({
  loader: async ({ params }) => {
    const post = await fetchPost(params.postId)
    return { post }
  },
  component: PostPage,
})

function PostPage() {
  const { post } = Route.useLoaderData() // Fully typed
  return <div>{post.title}</div>
}

// Loader with search-param dependencies
export const Route = createFileRoute('/posts')({
  validateSearch: z.object({ page: z.number().catch(1) }),
  loaderDeps: ({ search }) => ({ page: search.page }),
  loader: async ({ deps }) => fetchPosts(deps.page),
  component: PostsPage,
})


Key loader options: staleTime (SWR cache duration), shouldReload (control when to re-fetch), pendingMs/pendingMinMs (loading indicator timing), gcTime (garbage collection), loaderDeps (search-param keying).

Optional Path Parameters

Use {-$paramName} syntax for segments that may or may not exist:

// src/routes/posts.{-$category}.tsx -> /posts or /posts/tech
export const Route = createFileRoute('/posts/{-$category}')({
  component: () => {
    const { category } = Route.useParams() // category: string | undefined
    return <div>{category ? `Posts in ${category}` : 'All Posts'}</div>
  },
})

// Navigation: pass undefined to omit the segment
<Link to="/posts/{-$category}" params={{ category: undefined }}>All Posts</Link>
<Link to="/posts/{-$category}" params={{ category: 'tech' }}>Tech Posts</Link>

Router Context (Dependency Injection)
import { createRootRouteWithContext } from '@tanstack/react-router'
import type { QueryClient } from '@tanstack/react-query'

interface RouterContext {
  queryClient: QueryClient
  auth: AuthState
}

// Root route
const rootRoute = createRootRouteWithContext<RouterContext>()({
  component: RootComponent,
})

// Use in any route
export const Route = createFileRoute('/posts')({
  beforeLoad: ({ context }) => {
    // context.queryClient and context.auth available here
  },
  loader: ({ context }) => context.queryClient.ensureQueryData(postsQueryOptions()),
})

// Provide context when creating router
const router = createRouter({
  routeTree,
  context: { queryClient, auth: { user: null } },
})

Authentication (Protected Routes)
// src/routes/_auth.tsx - Pathless layout for protected routes
export const Route = createFileRoute('/_auth')({
  beforeLoad: async ({ context, location }) => {
    if (!context.auth.user) {
      throw redirect({
        to: '/login',
        search: { redirect: location.href },
      })
    }
  },
  component: () => <Outlet />,
})

// src/routes/_auth.dashboard.tsx - Protected route
export const Route = createFileRoute('/_auth/dashboard')({
  component: () => <div>Protected Dashboard</div>,
})

Error Handling
import { notFound } from '@tanstack/react-router'

export const Route = createFileRoute('/posts/$postId')({
  loader: async ({ params }) => {
    const post = await fetchPost(params.postId)
    if (!post) throw notFound()
    return { post }
  },
  notFoundComponent: () => <div>Post not found!</div>,
  errorComponent: ({ error, reset }) => (
    <div>
      <p>Error: {error.message}</p>
      <button onClick={reset}>Retry</button>
    </div>
  ),
})

// Global defaults on router
const router = createRouter({
  routeTree,
  defaultNotFoundComponent: () => <div>Page not found</div>,
  defaultErrorComponent: ({ error }) => <div>Error: {error.message}</div>,
})

Essential Hooks
Hook	Purpose
Route.useSearch()	Current validated search params
Route.useParams()	Current path params
Route.useLoaderData()	Data from route loader
Route.useRouteContext()	Route's context
Route.useNavigate()	Navigate from current route
useNavigate()	Navigate from any component
useRouter()	Access router instance
useRouterState()	Reactive router state
useMatch({ from: '/route' })	Match data for specific route
useBlocker()	Block navigation (dirty forms)

See references/api-hooks.md for all 19 hooks with full signatures.

Key Rules
Plugin order: tanstackRouter() must come BEFORE react() in Vite config
Commit routeTree.gen.ts: It's runtime code, not a build artifact
Module declaration: Always register router type for global type inference
Export as Route: File-based routes must export const Route = createFileRoute(...)
Pathless layouts: Prefix with _ (e.g., _auth.tsx) for layout-only routes
Non-nested routes: Use _ suffix to escape parent layout (e.g., posts_.$id.edit.tsx)
Ignore generated file: Add routeTree.gen.ts to .prettierignore, .eslintignore
Route matching order: Index > Static > Dynamic > Splat (automatic)
Don't export route properties: Exported components/loaders break code splitting
Validation adapters: Valibot/ArkType work directly; Zod needs zodValidator adapter
Outlet required: Every route with children must render <Outlet />; routes without a component auto-render <Outlet />
Type safety tip: Use Route.useX() methods over standalone hooks for automatic type inference
Reference Files
API
references/api-hooks.md — All 19 hooks with signatures, options, and examples
references/api-components.md — Link, Outlet, Await, Block, HeadContent, CatchNotFound, and more
references/api-functions.md — createRouter, createFileRoute, redirect, notFound, linkOptions, search middleware
references/api-router-instance.md — Router instance methods, events, and route type API
references/api-types.md — NavigateOptions, RouterState, RouteMatch, type utilities, deprecated items
Patterns
references/patterns-params.md — Path parameters, search params (Zod/Valibot/ArkType), loaderDeps, middlewares
references/patterns-links-blocking.md — Link options, custom links, navigation blocking, history types
references/patterns-data.md — Data loading, mutations, TanStack Query integration, not-found handling
references/patterns-auth.md — Authentication, RBAC, router context, preloading strategies
Configuration
references/config-bundlers.md — Vite, Webpack, Rspack, esbuild, Router CLI setup and plugin options
references/config-routing.md — File naming conventions, route matching, code-based routing
references/config-virtual-routes.md — Virtual file routes, physical routes, __virtual.ts subtrees
references/config-router-options.md — All createRouter() options: core, preloading, data loading, search, scroll, URL behavior
references/config-route-options.md — All createFileRoute/createRoute options: components, search, loader, lifecycle, head, SSR
references/config-devtools.md — DevTools modes, production devtools, IDE configuration
Advanced
references/advanced-ssr.md — SSR streaming/non-streaming, dehydration/hydration, deferred data
references/advanced-code-splitting.md — Automatic/manual splitting, split groupings, lazy routes
references/advanced-url-features.md — URL rewrites, route masking, custom search serialization
references/advanced-optimization.md — Type safety, TS performance tips, render optimizations, view transitions
references/advanced-head-scroll.md — Document head management, scroll restoration, i18n
Operations
references/troubleshooting.md — FAQ, common errors, debugging guide, performance issues
references/deployment-integrations.md — Deployment (8 platforms), environment variables, framework integrations
references/testing-migration.md — Testing setup, route testing patterns, migration guides
Weekly Installs
10
Repository
vcode-sh/vibe-tools
GitHub Stars
17
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass