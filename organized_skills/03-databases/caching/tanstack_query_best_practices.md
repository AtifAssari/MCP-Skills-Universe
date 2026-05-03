---
rating: ⭐⭐
title: tanstack-query-best-practices
url: https://skills.sh/deckardger/tanstack-agent-skills/tanstack-query-best-practices
---

# tanstack-query-best-practices

skills/deckardger/tanstack-agent-skills/tanstack-query-best-practices
tanstack-query-best-practices
Installation
$ npx skills add https://github.com/deckardger/tanstack-agent-skills --skill tanstack-query-best-practices
Summary

TanStack Query best practices for optimized data fetching, caching, mutations, and server state management in React.

Covers 32 rules across 10 categories: query keys, caching strategies, mutations, error handling, prefetching, infinite queries, SSR integration, parallel queries, performance optimization, and offline support
Each rule includes explanation, anti-patterns, recommended implementations, and contextual guidance for when to apply
Prioritized by impact: critical rules prevent cache bugs and data inconsistencies; high-priority rules ensure data integrity and UI consistency
Organized with hierarchical query key factories, targeted cache invalidation, optimistic updates with rollback context, and structural sharing patterns
SKILL.md
TanStack Query Best Practices

Comprehensive guidelines for implementing TanStack Query (React Query) patterns in React applications. These rules optimize data fetching, caching, mutations, and server state synchronization.

When to Apply
Creating new data fetching logic
Setting up query configurations
Implementing mutations and optimistic updates
Configuring caching strategies
Integrating with SSR/SSG
Refactoring existing data fetching code
Rule Categories by Priority
Priority	Category	Rules	Impact
CRITICAL	Query Keys	5 rules	Prevents cache bugs and data inconsistencies
CRITICAL	Caching	5 rules	Optimizes performance and data freshness
HIGH	Mutations	6 rules	Ensures data integrity and UI consistency
HIGH	Error Handling	3 rules	Prevents poor user experiences
MEDIUM	Prefetching	4 rules	Improves perceived performance
MEDIUM	Parallel Queries	2 rules	Enables dynamic parallel fetching
MEDIUM	Infinite Queries	3 rules	Prevents pagination bugs
MEDIUM	SSR Integration	4 rules	Enables proper hydration
LOW	Performance	4 rules	Reduces unnecessary re-renders
LOW	Offline Support	2 rules	Enables offline-first patterns
Quick Reference
Query Keys (Prefix: qk-)
qk-array-structure — Always use arrays for query keys
qk-include-dependencies — Include all variables the query depends on
qk-hierarchical-organization — Organize keys hierarchically (entity → id → filters)
qk-factory-pattern — Use query key factories for complex applications
qk-serializable — Ensure all key parts are JSON-serializable
Caching (Prefix: cache-)
cache-stale-time — Set appropriate staleTime based on data volatility
cache-gc-time — Configure gcTime for inactive query retention
cache-defaults — Set sensible defaults at QueryClient level
cache-invalidation — Use targeted invalidation over broad patterns
cache-placeholder-vs-initial — Understand placeholder vs initial data differences
Mutations (Prefix: mut-)
mut-invalidate-queries — Always invalidate related queries after mutations
mut-optimistic-updates — Implement optimistic updates for responsive UI
mut-rollback-context — Provide rollback context from onMutate
mut-error-handling — Handle mutation errors gracefully
mut-loading-states — Use isPending for mutation loading states
mut-mutation-state — Use useMutationState for cross-component tracking
Error Handling (Prefix: err-)
err-error-boundaries — Use error boundaries with useQueryErrorResetBoundary
err-retry-config — Configure retry logic appropriately
err-fallback-data — Provide fallback data when appropriate
Prefetching (Prefix: pf-)
pf-intent-prefetch — Prefetch on user intent (hover, focus)
pf-route-prefetch — Prefetch data during route transitions
pf-stale-time-config — Set staleTime when prefetching
pf-ensure-query-data — Use ensureQueryData for conditional prefetching
Infinite Queries (Prefix: inf-)
inf-page-params — Always provide getNextPageParam
inf-loading-guards — Check isFetchingNextPage before fetching more
inf-max-pages — Consider maxPages for large datasets
SSR Integration (Prefix: ssr-)
ssr-dehydration — Use dehydrate/hydrate pattern for SSR
ssr-client-per-request — Create QueryClient per request
ssr-stale-time-server — Set higher staleTime on server
ssr-hydration-boundary — Wrap with HydrationBoundary
Parallel Queries (Prefix: parallel-)
parallel-use-queries — Use useQueries for dynamic parallel queries
query-cancellation — Implement query cancellation properly
Performance (Prefix: perf-)
perf-select-transform — Use select to transform/filter data
perf-structural-sharing — Leverage structural sharing
perf-notify-change-props — Limit re-renders with notifyOnChangeProps
perf-placeholder-data — Use placeholderData for instant UI
Offline Support (Prefix: offline-)
network-mode — Configure network mode for offline support
persist-queries — Configure query persistence for offline support
How to Use

Each rule file in the rules/ directory contains:

Explanation — Why this pattern matters
Bad Example — Anti-pattern to avoid
Good Example — Recommended implementation
Context — When to apply or skip this rule
Full Reference

See individual rule files in rules/ directory for detailed guidance and code examples.

Weekly Installs
4.6K
Repository
deckardger/tans…t-skills
GitHub Stars
151
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass