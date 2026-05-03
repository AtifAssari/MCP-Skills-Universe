---
title: react-refactor
url: https://skills.sh/pproenca/dot-skills/react-refactor
---

# react-refactor

skills/pproenca/dot-skills/react-refactor
react-refactor
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill react-refactor
SKILL.md
React Refactor Best Practices

Architectural refactoring guide for React applications. Contains 40 rules across 7 categories, prioritized by impact from critical (component and state architecture) to incremental (refactoring safety).

When to Apply
Refactoring existing React codebases or planning large-scale restructuring
Reviewing PRs for architectural issues and code smells
Decomposing oversized components into focused units
Extracting reusable hooks from component logic
Improving testability of React code
Reducing coupling between feature modules
Rule Categories
Category	Impact	Rules	Key Topics
Component Architecture	CRITICAL	8	Compound components, headless pattern, composition over props, client boundaries
State Architecture	CRITICAL	7	Colocation, state machines, URL state, derived values
Hook Patterns	HIGH	6	Single responsibility, naming, dependency stability, composition
Component Decomposition	HIGH	6	Scroll test, extraction by change reason, view/logic separation
Coupling & Cohesion	MEDIUM	4	Dependency injection, circular deps, stable imports, barrel-free
Data & Side Effects	MEDIUM	4	Server-first fetch, TanStack Query, error boundaries
Refactoring Safety	LOW-MEDIUM	5	Characterization tests, behavior testing, integration tests
Quick Reference

Critical patterns — get these right first:

Use compound components instead of props explosion
Colocate state with the components that use it
Use state machines for complex UI workflows
Separate container logic from presentational components

Common mistakes — avoid these anti-patterns:

Lifting state to App when only one component reads it
Using context for rapidly-changing values
Monolithic hooks that fetch + transform + cache
Testing implementation details instead of behavior
Table of Contents
Component Architecture — CRITICAL
1.1 Apply Interface Segregation to Component Props — CRITICAL (prevents 30-50% of unnecessary re-renders)
1.2 Colocate Files by Feature Instead of Type — CRITICAL (reduces cross-directory navigation by 70%)
1.3 Convert Render Props to Custom Hooks — CRITICAL (eliminates 2-4 levels of nesting)
1.4 Extract Headless Components for Logic Reuse — CRITICAL (5x more reuse scenarios)
1.5 Prefer Composition Over Props Explosion — CRITICAL (reduces prop count by 50-70%)
1.6 Separate Container Logic from Presentational Components — CRITICAL (enables independent testing)
1.7 Use Compound Components for Implicit State Sharing — CRITICAL (reduces API surface by 60%)
1.8 Push Client Boundaries to Leaf Components — HIGH (keeps 60-80% server-rendered)
State Architecture — CRITICAL
2.1 Colocate State with Components That Use It — CRITICAL (reduces prop passing by 60%)
2.2 Derive Values Instead of Syncing State — CRITICAL (eliminates double-render cycle)
2.3 Lift State Only When Multiple Components Read It — CRITICAL (eliminates unnecessary parent re-renders)
2.4 Use Context for Rarely-Changing Values Only — CRITICAL (5-50x fewer re-renders)
2.5 Use State Machines for Complex UI Workflows — CRITICAL (reduces valid states from 2^n to N)
2.6 Use URL Parameters as State for Shareable Views — CRITICAL (enables deep linking and sharing)
2.7 Use useReducer for Multi-Field State Transitions — CRITICAL (eliminates impossible states)
Hook Patterns — HIGH
3.1 Avoid Object and Array Dependencies in Custom Hooks — HIGH (prevents effect re-execution every render)
3.2 Compose Hooks Instead of Nesting Them — HIGH (flattens dependency graph)
3.3 Extract Logic into Custom Hooks When Behavior Is Nameable — HIGH (40-60% shorter components)
3.4 Follow Hook Naming Conventions for Discoverability — HIGH (reduces navigation time by 40%)
3.5 Keep Custom Hooks to a Single Responsibility — HIGH (3x easier to test)
3.6 Stabilize Hook Dependencies with Refs and Callbacks — HIGH (prevents infinite loops)
Component Decomposition — HIGH
4.1 Apply the Scroll Test to Identify Oversized Components — HIGH (3x faster code review)
4.2 Complete Component Extraction Without Half-Measures — HIGH (enables independent testing and reuse)
4.3 Extract Components by Independent Change Reasons — HIGH (70% fewer files touched per change)
4.4 Extract Pure Functions from Component Bodies — HIGH (10x faster unit tests)
4.5 Inline Premature Abstractions Before Re-Extracting — HIGH (40-60% simpler code)
4.6 Separate View Layer from Business Logic — HIGH (5x faster test suite)
Coupling & Cohesion — MEDIUM
5.1 Break Circular Dependencies with Intermediate Modules — MEDIUM (eliminates undefined-at-import-time bugs)
5.2 Import from Stable Public API Surfaces Only — MEDIUM (enables internal refactoring)
5.3 Use Barrel-Free Feature Modules for Clean Dependencies — MEDIUM (200-800ms build reduction)
5.4 Use Dependency Injection for External Services — MEDIUM (3x faster test setup)
Data & Side Effects — MEDIUM
6.1 Fetch Data on the Server by Default — MEDIUM (reduces client JS by 30-60%)
6.2 Place Error Boundaries at Data Fetch Granularity — MEDIUM (errors isolated to affected section)
6.3 Use Context Module Pattern for Action Colocation — MEDIUM (centralizes data mutations)
6.4 Use TanStack Query for Client-Side Server State — MEDIUM (eliminates 80% of fetch boilerplate)
Refactoring Safety — LOW-MEDIUM
7.1 Avoid Snapshot Tests for Refactored Components — LOW-MEDIUM (eliminates false test failures)
7.2 Extract Pure Functions to Increase Testability — LOW-MEDIUM (10x faster test execution)
7.3 Prefer Integration Tests for Component Verification — LOW-MEDIUM (catches 40% more bugs)
7.4 Test Component Behavior Not Implementation Details — LOW-MEDIUM (5x fewer test updates)
7.5 Write Characterization Tests Before Refactoring — LOW-MEDIUM (catches 90% of unintended changes)
References
https://react.dev
https://react.dev/learn/thinking-in-react
https://kentcdodds.com/blog/application-state-management-with-react
https://testing-library.com/docs/guiding-principles
https://patterns.dev
Related Skills
For React 19 API best practices, see react skill
For application performance optimization, see react-optimise skill
For client-side form handling, see react-hook-form skill
Weekly Installs
307
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