---
title: react
url: https://skills.sh/thongdn-it/react-agent-skills/react
---

# react

skills/thongdn-it/react-agent-skills/react
react
Installation
$ npx skills add https://github.com/thongdn-it/react-agent-skills --skill react
SKILL.md
React 19 Best Practices

Comprehensive performance optimization guide for React 19 applications. Contains 40 rules across 8 categories, prioritized by impact from critical (concurrent rendering, server components) to incremental (component patterns).

Table of Contents
Concurrent Rendering — CRITICAL
1.1 Avoid Suspense Fallback Thrashing — HIGH (prevents flickering, smoother UX)
1.2 Leverage Automatic Batching for Fewer Renders — HIGH (32% fewer renders in heavy updates)
1.3 Use useDeferredValue for Derived Expensive Values — CRITICAL (prevents jank in derived computations)
1.4 Use useTransition for Non-Blocking Updates — CRITICAL (keeps UI responsive during heavy updates)
1.5 Write Concurrent-Safe Components — MEDIUM-HIGH (prevents bugs in concurrent rendering)
Server Components — CRITICAL
2.1 Avoid Client-Only Libraries in Server Components — MEDIUM-HIGH (prevents build errors, correct component placement)
2.2 Enable Streaming with Nested Suspense — MEDIUM-HIGH (progressive loading, faster TTFB)
2.3 Fetch Data in Server Components — CRITICAL (38% less client JS, no client waterfalls)
2.4 Minimize Server/Client Boundary Crossings — CRITICAL (reduces serialization overhead, smaller bundles)
2.5 Pass Only Serializable Props to Client Components — HIGH (prevents runtime errors, ensures correct hydration)
2.6 Use Composition to Mix Server and Client Components — HIGH (maintains server rendering for static content)
Actions & Forms — HIGH
3.1 Use Form Actions Instead of onSubmit — HIGH (progressive enhancement, simpler code)
3.2 Use useActionState for Form State Management — HIGH (declarative form handling, automatic pending states)
3.3 Use useFormStatus for Submit Button State — MEDIUM-HIGH (proper loading indicators, prevents double submission)
3.4 Use useOptimistic for Instant UI Feedback — HIGH (instant perceived response, auto-rollback on failure)
3.5 Validate Forms on Server with Actions — MEDIUM (secure validation, consistent error handling)
Data Fetching — HIGH
4.1 Fetch Data in Parallel with Promise.all — MEDIUM-HIGH (eliminates waterfalls, 2-5× faster)
4.2 Use cache() for Request Deduplication — HIGH (eliminates duplicate fetches per render)
4.3 Use Error Boundaries with Suspense — MEDIUM (graceful error recovery, isolated failures)
4.4 Use Suspense for Declarative Loading States — HIGH (cleaner code, coordinated loading UI)
4.5 Use the use() Hook for Promises in Render — HIGH (cleaner async component code, Suspense integration)
State Management — MEDIUM-HIGH
5.1 Calculate Derived Values During Render — MEDIUM (eliminates sync bugs, simpler code)
5.2 Split Context to Prevent Unnecessary Re-renders — MEDIUM (reduces re-renders from context changes)
5.3 Use Functional State Updates for Derived Values — MEDIUM-HIGH (prevents stale closures, stable callbacks)
5.4 Use Lazy Initialization for Expensive Initial State — MEDIUM-HIGH (prevents expensive computation on every render)
5.5 Use useReducer for Complex State Logic — MEDIUM (clearer state transitions, easier testing)
Memoization & Performance — MEDIUM
6.1 Avoid Premature Memoization — MEDIUM (memoization has overhead, measure first)
6.2 Leverage React Compiler for Automatic Memoization — MEDIUM (automatic optimization, less manual code)
6.3 Use React.memo for Expensive Pure Components — MEDIUM (skips re-render when props unchanged)
6.4 Use useCallback for Stable Function References — MEDIUM (prevents child re-renders from reference changes)
6.5 Use useMemo for Expensive Calculations — MEDIUM (skips expensive recalculation on re-renders)
Effects & Events — MEDIUM
7.1 Always Clean Up Effect Side Effects — MEDIUM (prevents memory leaks, stale callbacks)
7.2 Avoid Effects for Derived State and User Events — MEDIUM (eliminates sync bugs, simpler code)
7.3 Avoid Object and Array Dependencies in Effects — MEDIUM (prevents infinite loops, unnecessary re-runs)
7.4 Use useEffectEvent for Non-Reactive Logic — MEDIUM (separates reactive from non-reactive code)
7.5 Use useSyncExternalStore for External Subscriptions — MEDIUM (correct subscription handling, SSR compatible)
Component Patterns — LOW-MEDIUM
8.1 Choose Controlled vs Uncontrolled Appropriately — LOW-MEDIUM (correct data flow, proper form handling)
8.2 Prefer Composition Over Props Explosion — LOW-MEDIUM (more flexible, reusable components)
8.3 Use Key to Reset Component State — LOW-MEDIUM (correct state isolation, proper resets)
8.4 Use Render Props for Inversion of Control — LOW-MEDIUM (flexible rendering, shared logic)
References
https://react.dev
https://react.dev/blog/2024/12/05/react-19
https://react.dev/blog/2025/10/01/react-19-2
https://react.dev/learn/you-might-not-need-an-effect
https://github.com/facebook/react
Related Skills
For Next.js 16 App Router, see nextjs-16-app-router skill
For client-side form handling, see react-hook-form skill
For data caching with TanStack Query, see tanstack-query skill
Weekly Installs
16
Repository
thongdn-it/reac…t-skills
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass