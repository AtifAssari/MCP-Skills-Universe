---
title: tanstack-integration-best-practices
url: https://skills.sh/deckardger/tanstack-agent-skills/tanstack-integration-best-practices
---

# tanstack-integration-best-practices

skills/deckardger/tanstack-agent-skills/tanstack-integration-best-practices
tanstack-integration-best-practices
Installation
$ npx skills add https://github.com/deckardger/tanstack-agent-skills --skill tanstack-integration-best-practices
Summary

Architectural patterns for coordinating TanStack Query, Router, and Start across full-stack applications.

Covers setup, data flow, caching, and SSR integration with 13 rules organized by priority and category
Emphasizes loader-based data fetching with ensureQueryData, suspense queries in components, and server functions as query sources
Provides unified caching and invalidation strategies to prevent duplication and ensure single source of truth
Includes automatic SSR dehydration/hydration setup and per-request QueryClient patterns for server-side rendering
SKILL.md
TanStack Integration Best Practices

Guidelines for integrating TanStack Query, Router, and Start together effectively. These patterns ensure optimal data flow, caching coordination, and type safety across the stack.

When to Apply
Setting up a new TanStack Start project
Integrating TanStack Query with TanStack Router
Configuring SSR with query hydration
Coordinating caching between router and query
Setting up type-safe data fetching patterns
Rule Categories by Priority
Priority	Category	Rules	Impact
CRITICAL	Setup	3 rules	Foundational configuration
CRITICAL	SSR Integration	1 rule	Router + Query SSR setup
HIGH	Data Flow	4 rules	Correct data fetching patterns
MEDIUM	Caching	3 rules	Performance optimization
MEDIUM	SSR	2 rules	Additional SSR patterns
Quick Reference
Setup (Prefix: setup-)
setup-query-client-context — Pass QueryClient through router context
setup-provider-wrapping — Correctly wrap with QueryClientProvider
setup-stale-time-coordination — Coordinate staleTime between router and query
Data Flow (Prefix: flow-)
flow-loader-query-pattern — Use loaders with ensureQueryData
flow-suspense-query-component — Use useSuspenseQuery in components
flow-mutations-invalidation — Coordinate mutations with query invalidation
flow-server-functions-queries — Use server functions for query functions
Caching (Prefix: cache-)
cache-single-source — Let TanStack Query manage caching
cache-preload-coordination — Coordinate preloading between router and query
cache-invalidation-patterns — Unified invalidation patterns
SSR Integration (Prefix: ssr-)
ssr-dehydrate-hydrate — Use setupRouterSsrQueryIntegration for automatic SSR
Additional SSR (Prefix: ssr-)
ssr-per-request-client — Create QueryClient per request
ssr-streaming-queries — Handle streaming with queries
How to Use

Each rule file in the rules/ directory contains:

Explanation — Why this pattern matters
Bad Example — Anti-pattern to avoid
Good Example — Recommended implementation
Context — When to apply or skip this rule
Full Reference

See individual rule files in rules/ directory for detailed guidance and code examples.

Weekly Installs
1.2K
Repository
deckardger/tans…t-skills
GitHub Stars
151
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass