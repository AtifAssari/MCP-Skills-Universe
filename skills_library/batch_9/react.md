---
title: react
url: https://skills.sh/pproenca/dot-skills/react
---

# react

skills/pproenca/dot-skills/react
react
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill react
SKILL.md
React 19 Best Practices

Comprehensive performance optimization guide for React 19/19.2 applications. Contains 41 rules across 8 categories, prioritized by impact from critical (concurrent rendering, server components) to incremental (component patterns).

When to Apply
Writing new React components or refactoring existing ones
Optimizing re-render performance or bundle size
Using concurrent features (useTransition, useDeferredValue, Activity)
Setting up Server Components or server/client boundaries
Implementing form actions, optimistic updates, or data fetching
Configuring React Compiler for automatic memoization
Reviewing React code for common anti-patterns
Rule Categories
Category	Impact	Rules	Key Topics
Concurrent Rendering	CRITICAL	6	useTransition, useDeferredValue, Activity, batching
Server Components	CRITICAL	6	RSC boundaries, data fetching, streaming
Actions & Forms	HIGH	5	Form actions, useActionState, useOptimistic
Data Fetching	HIGH	5	use() hook, cache(), Suspense, error boundaries
State Management	MEDIUM-HIGH	5	Derived values, context optimization, useReducer
Memoization & Performance	MEDIUM	5	React Compiler, useMemo, useCallback, React.memo
Effects & Events	MEDIUM	5	useEffectEvent, cleanup, external stores
Component Patterns	LOW-MEDIUM	4	Composition, controlled vs uncontrolled, key reset
Quick Reference

Critical patterns — get these right first:

Fetch data in Server Components, not Client Components
Push 'use client' boundaries as low as possible
Use startTransition for expensive non-blocking updates
Use <Activity> to preserve state across tab/page switches

Common mistakes — avoid these anti-patterns:

Creating promises inside Client Components for use() (causes infinite loops)
Memoizing everything (use React Compiler v1.0+ instead)
Using effects for derived state or user event handling
Placing 'use client' too high in the component tree
Table of Contents
Concurrent Rendering — CRITICAL
1.1 Use Activity for Pre-Rendering and State Preservation — HIGH (eliminates navigation re-render cost, preserves user input state)
1.2 Avoid Suspense Fallback Thrashing — HIGH (prevents 200-500ms layout shift flicker)
1.3 Leverage Automatic Batching for Fewer Renders — HIGH (batches multiple setState calls into a single render in all contexts)
1.4 Use useDeferredValue for Derived Expensive Values — CRITICAL (prevents jank in derived computations)
1.5 Use useTransition for Non-Blocking Updates — CRITICAL (maintains <50ms input latency during heavy state updates)
1.6 Write Concurrent-Safe Components — MEDIUM-HIGH (prevents bugs in concurrent rendering)
Server Components — CRITICAL
2.1 Avoid Client-Only Libraries in Server Components — MEDIUM-HIGH (prevents build errors, correct component placement)
2.2 Enable Streaming with Nested Suspense — MEDIUM-HIGH (progressive loading, faster TTFB)
2.3 Fetch Data in Server Components — CRITICAL (significantly reduces client JS bundle, eliminates client-side data waterfalls)
2.4 Minimize Server/Client Boundary Crossings — CRITICAL (reduces serialization overhead, smaller bundles)
2.5 Pass Only Serializable Props to Client Components — HIGH (prevents runtime errors, ensures correct hydration)
2.6 Use Composition to Mix Server and Client Components — HIGH (maintains server rendering for static content)
Actions & Forms — HIGH
3.1 Use Form Actions Instead of onSubmit — HIGH (forms work without JS loaded, eliminates e.preventDefault() boilerplate)
3.2 Use useActionState for Form State Management — HIGH (declarative form handling, automatic pending states)
3.3 Use useFormStatus for Submit Button State — MEDIUM-HIGH (proper loading indicators, prevents double submission)
3.4 Use useOptimistic for Instant UI Feedback — HIGH (0ms perceived latency for mutations, automatic rollback on server failure)
3.5 Validate Forms on Server with Actions — MEDIUM (prevents client-only validation bypass, single source of truth for form errors)
Data Fetching — HIGH
4.1 Fetch Data in Parallel with Promise.all — MEDIUM-HIGH (eliminates waterfalls, 2-5x faster)
4.2 Use cache() for Request Deduplication — HIGH (eliminates duplicate fetches per server request)
4.3 Use Error Boundaries with Suspense — MEDIUM (isolates failures to individual components, prevents full-page crashes)
4.4 Use Suspense for Declarative Loading States — HIGH (eliminates loading state boilerplate, enables parallel data fetch coordination)
4.5 Use the use() Hook for Promises in Render — HIGH (eliminates useEffect+useState fetch pattern, integrates with Suspense boundaries)
State Management — MEDIUM-HIGH
5.1 Calculate Derived Values During Render — MEDIUM (eliminates sync bugs, simpler code)
5.2 Split Context to Prevent Unnecessary Re-renders — MEDIUM (reduces re-renders from context changes)
5.3 Use Functional State Updates for Derived Values — MEDIUM-HIGH (prevents stale closures, stable callbacks)
5.4 Use Lazy Initialization for Expensive Initial State — MEDIUM-HIGH (prevents expensive computation on every render)
5.5 Use useReducer for Complex State Logic — MEDIUM (eliminates impossible state combinations, enables unit-testable state logic)
Memoization & Performance — MEDIUM
6.1 Avoid Premature Memoization — MEDIUM (removes 0.1-0.5ms per-render overhead from unnecessary memoization)
6.2 Leverage React Compiler for Automatic Memoization — MEDIUM (automatic optimization, less manual code)
6.3 Use React.memo for Expensive Pure Components — MEDIUM (skips expensive re-renders, 5-50ms savings per unchanged component)
6.4 Use useCallback for Stable Function References — MEDIUM (prevents child re-renders from reference changes)
6.5 Use useMemo for Expensive Calculations — MEDIUM (skips O(n) recalculations on re-renders with unchanged dependencies)
Effects & Events — MEDIUM
7.1 Always Clean Up Effect Side Effects — MEDIUM (prevents memory leaks, stale callbacks)
7.2 Avoid Effects for Derived State and User Events — MEDIUM (eliminates sync bugs, simpler code)
7.3 Avoid Object and Array Dependencies in Effects — MEDIUM (prevents infinite loops, unnecessary re-runs)
7.4 Use useEffectEvent for Non-Reactive Logic — MEDIUM (prevents unnecessary effect re-runs from non-reactive value changes)
7.5 Use useSyncExternalStore for External Subscriptions — MEDIUM (prevents tearing in concurrent rendering, ensures SSR-safe external state)
Component Patterns — LOW-MEDIUM
8.1 Choose Controlled vs Uncontrolled Appropriately — LOW-MEDIUM (prevents form state sync bugs, enables real-time validation)
8.2 Prefer Composition Over Props Explosion — LOW-MEDIUM (reduces prop drilling depth, enables independent component reuse)
8.3 Use Key to Reset Component State — LOW-MEDIUM (forces full component remount, eliminates stale state after identity changes)
8.4 Use Render Props for Inversion of Control — LOW-MEDIUM (enables parent-controlled rendering without child prop explosion)
References
https://react.dev
https://react.dev/blog/2024/12/05/react-19
https://react.dev/blog/2025/10/01/react-19-2
https://react.dev/blog/2025/10/07/react-compiler-1
https://react.dev/learn/you-might-not-need-an-effect
https://github.com/facebook/react
Related Skills
For Next.js 16 App Router, see nextjs-16-app-router skill
For client-side form handling, see react-hook-form skill
For data caching with TanStack Query, see tanstack-query skill
Weekly Installs
261
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass