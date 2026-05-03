---
title: react-optimise
url: https://skills.sh/pproenca/dot-skills/react-optimise
---

# react-optimise

skills/pproenca/dot-skills/react-optimise
react-optimise
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill react-optimise
SKILL.md
React Optimise Best Practices

Application-level performance optimization guide for React applications. Contains 43 rules across 8 categories, prioritized by impact from critical (React Compiler, bundle optimization) to incremental (memory management).

When to Apply
Optimizing React application performance or bundle size
Adopting or troubleshooting React Compiler v1.0
Splitting bundles and configuring code splitting
Improving Core Web Vitals (INP, LCP, CLS)
Profiling render performance and identifying bottlenecks
Fixing memory leaks in long-lived single-page applications
Optimizing data fetching patterns and eliminating waterfalls
Rule Categories
Category	Impact	Rules	Key Topics
React Compiler Mastery	CRITICAL	6	Compiler-friendly code, bailout detection, incremental adoption
Bundle & Loading	CRITICAL	6	Route splitting, barrel elimination, dynamic imports, prefetching
Rendering Optimization	HIGH	6	Virtualization, children pattern, debouncing, CSS containment
Data Fetching Performance	HIGH	5	Waterfall elimination, route preloading, SWR, deduplication
Core Web Vitals	MEDIUM-HIGH	5	INP yielding, LCP priority, CLS prevention, image optimization
State & Subscription Performance	MEDIUM-HIGH	5	Context splitting, selectors, atomic state, derived state
Profiling & Measurement	MEDIUM	5	DevTools profiling, flame charts, CI budgets, production builds
Memory Management	LOW-MEDIUM	5	Effect cleanup, async cancellation, closure leaks, heap analysis
Quick Reference

Critical patterns — get these right first:

Write compiler-friendly components to unlock automatic 2-10x optimization
Split code at route boundaries to reduce initial bundle by 40-70%
Eliminate barrel files to enable tree shaking
Detect and fix silent compiler bailouts

Common mistakes — avoid these anti-patterns:

Reading refs during render (breaks compiler optimization)
Importing entire libraries when only using one function
Not profiling before optimizing (targeting the wrong bottleneck)
Missing effect cleanup (subscription memory leaks)
Table of Contents
React Compiler Mastery — CRITICAL
1.1 Detect and Fix Silent Compiler Bailouts — CRITICAL (prevents losing automatic memoization)
1.2 Isolate Side Effects from Render for Compiler Correctness — CRITICAL (prevents compiler from producing incorrect cached output)
1.3 Remove Manual Memoization After Compiler Adoption — CRITICAL (20-40% code reduction in component files)
1.4 Use Incremental Compiler Adoption with Directives — CRITICAL (enables safe rollout without full codebase migration)
1.5 Use Ref Access Patterns That Enable Compilation — CRITICAL (maintains compiler optimization for ref-using components)
1.6 Write Compiler-Friendly Component Patterns — CRITICAL (2-10x automatic render optimization)
Bundle & Loading — CRITICAL
2.1 Configure Dependencies for Effective Tree Shaking — CRITICAL (50-90% dead code elimination in dependencies)
2.2 Eliminate Barrel Files to Enable Tree Shaking — CRITICAL (200-800ms import cost eliminated)
2.3 Enforce Bundle Size Budgets with Analysis Tools — CRITICAL (prevents gradual bundle size regression)
2.4 Prefetch Likely Next Routes on Interaction — CRITICAL (200-1000ms faster perceived navigation)
2.5 Split Code at Route Boundaries with React.lazy — CRITICAL (40-70% reduction in initial bundle size)
2.6 Use Dynamic Imports for Heavy Libraries — CRITICAL (100-500KB removed from critical path)
Rendering Optimization — HIGH
3.1 Avoid Inline Object Creation in JSX Props — HIGH (prevents unnecessary child re-renders)
3.2 Debounce Expensive Derived Computations — HIGH (50-200ms saved per keystroke)
3.3 Use CSS Containment to Isolate Layout Recalculation — HIGH (60-90% layout recalc reduction)
3.4 Use Children Pattern to Prevent Parent Re-Renders — HIGH (eliminates re-renders of static subtrees)
3.5 Use Stable Keys for List Rendering Performance — HIGH (O(n) DOM mutations to O(1) moves)
3.6 Virtualize Long Lists with TanStack Virtual — HIGH (O(n) to O(1) DOM nodes)
Data Fetching Performance — HIGH
4.1 Abort Stale Requests on Navigation or Re-fetch — HIGH (prevents stale data display)
4.2 Deduplicate Identical In-Flight Requests — HIGH (50-80% fewer network requests)
4.3 Eliminate Sequential Data Fetch Waterfalls — HIGH (2-5x faster page loads)
4.4 Preload Data at Route Level Before Component Mounts — HIGH (200-1000ms eliminated)
4.5 Use Stale-While-Revalidate for Cache Freshness — HIGH (0ms perceived load for returning visitors)
Core Web Vitals — MEDIUM-HIGH
5.1 Instrument Real User Monitoring with web-vitals — MEDIUM-HIGH (enables data-driven optimization)
5.2 Optimize Images with Responsive Sizing and Lazy Loading — MEDIUM-HIGH (40-70% bandwidth reduction)
5.3 Optimize Interaction to Next Paint with Yielding — MEDIUM-HIGH (INP from 500ms+ to under 200ms)
5.4 Optimize Largest Contentful Paint with Priority Loading — MEDIUM-HIGH (200-1000ms LCP improvement)
5.5 Prevent Cumulative Layout Shift with Size Reservations — MEDIUM-HIGH (CLS from 0.25+ to under 0.1)
State & Subscription Performance — MEDIUM-HIGH
6.1 Derive State Instead of Syncing for Zero Extra Renders — MEDIUM-HIGH (eliminates double-render cycle)
6.2 Separate Server State from Client State Management — MEDIUM-HIGH (reduces state management code by 40%)
6.3 Split Contexts to Isolate High-Frequency Updates — MEDIUM-HIGH (5-50x fewer re-renders)
6.4 Use Atomic State for Independent Reactive Values — MEDIUM-HIGH (3-10x fewer unnecessary re-renders)
6.5 Use Selector-Based Subscriptions for Granular Updates — MEDIUM-HIGH (reduces re-renders to only affected components)
Profiling & Measurement — MEDIUM
7.1 Benchmark with Production Builds Only — MEDIUM (prevents false positives from dev-mode overhead)
7.2 Enforce Performance Budgets in CI — MEDIUM (catches 90% of perf issues before merge)
7.3 Profile Before Optimizing to Target Real Bottlenecks — MEDIUM (10x more effective optimization effort)
7.4 Read Flame Charts to Identify Hot Render Paths — MEDIUM (identifies exact function causing 80% of render time)
7.5 Use React Performance Tracks for Render Analysis — MEDIUM (pinpoints render bottlenecks in minutes)
Memory Management — LOW-MEDIUM
8.1 Avoid Closure-Based Memory Leaks in Event Handlers — LOW-MEDIUM (prevents MB-scale memory retention)
8.2 Cancel Async Operations on Unmount — LOW-MEDIUM (prevents stale updates and memory retention)
8.3 Clean Up Effects to Prevent Subscription Memory Leaks — LOW-MEDIUM (prevents linear memory growth)
8.4 Dispose Heavy Resources in Cleanup Functions — LOW-MEDIUM (prevents 5-50MB per resource retention)
8.5 Use Heap Snapshots to Detect Component Retention — LOW-MEDIUM (identifies 10-100MB memory growth)
References
https://react.dev
https://react.dev/blog/2025/10/07/react-compiler-1
https://web.dev/articles/vitals
https://tanstack.com/virtual
https://developer.chrome.com/docs/devtools/performance
Related Skills
For React 19 API best practices, see react skill
For Next.js App Router optimization, see nextjs-16-app-router skill
For client-side form handling, see react-hook-form skill
Weekly Installs
167
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass