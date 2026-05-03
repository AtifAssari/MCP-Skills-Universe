---
rating: ⭐⭐
title: trpc-tanstack-nextjs
url: https://skills.sh/diegojohnsonl/trpc-tanstack-nextjs/trpc-tanstack-nextjs
---

# trpc-tanstack-nextjs

skills/diegojohnsonl/trpc-tanstack-nextjs/trpc-tanstack-nextjs
trpc-tanstack-nextjs
Installation
$ npx skills add https://github.com/diegojohnsonl/trpc-tanstack-nextjs --skill trpc-tanstack-nextjs
SKILL.md
tRPC + TanStack Query + Next.js App Router

End-to-end typesafe APIs for Next.js using tRPC v11 with @trpc/tanstack-react-query adapter.

Core Setup
setup - Full setup from scratch with all modules
routers - Creating routers, procedures, middleware
client-usage - Queries, mutations, useUtils in client components
server-usage - Prefetching, hydration, getCaller in server components
Optional Integrations
better-auth-integration - Add session/user to tRPC context with Better Auth
optimistic-updates - Update UI before server confirms
infinite-queries - Cursor-based pagination
subscriptions - WebSocket real-time updates
How to Use

Read individual reference files for detailed explanations and code examples:

references/setup.md
references/routers.md
references/client-usage.md


Each reference file contains:

Code examples with imports
Usage patterns
Common variations
Common Gotchas
Cookies not sent - Add credentials: "include" to httpBatchLink fetch
Hydration mismatch - Ensure superjson transformer on both client and server
staleTime: 0 - Causes refetch on every mount; use 30s+ for most cases
Missing HydrateClient - Prefetched data won't transfer to client
cache() not used - getCaller/getQueryClient must be wrapped in React cache()
Resources
tRPC Docs
TanStack Query Docs
Weekly Installs
78
Repository
diegojohnsonl/t…k-nextjs
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass