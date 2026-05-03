---
rating: ⭐⭐
title: qwik-expert
url: https://skills.sh/oimiragieo/agent-studio/qwik-expert
---

# qwik-expert

skills/oimiragieo/agent-studio/qwik-expert
qwik-expert
Installation
$ npx skills add https://github.com/oimiragieo/agent-studio --skill qwik-expert
SKILL.md
Qwik Expert
qwik and tailwind best practices

When reviewing or writing code, apply these guidelines:

Use $ suffix for lazy-loaded functions
Utilize useSignal() for reactive state
Implement Tailwind CSS classes for styling
Use @apply directive in CSS files for reusable styles
Implement responsive design using Tailwind's responsive classes
Utilize Tailwind's configuration file for customization
Leverage TypeScript for type safety
Use Vite's fast HMR for development
qwik city routing

When reviewing or writing code, apply these guidelines:

Utilize Qwik City for routing when applicable
qwik folder structure

When reviewing or writing code, apply these guidelines:

Recommended folder structure:

src/ components/ routes/ global.css root.tsx entry.ssr.tsx public/ tailwind.config.js postcss.config.js vite.config.ts tsconfig.json

qwik functional components preference

When reviewing or writing code, apply these guidelines:

Always prefer functional components in Qwik files.
qwik js best practices

When reviewing or writing code, apply these guidelines:

Use $ suffix for lazy-loaded functions
Utilize useSignal() for reactive state
Implement useStore() for complex state objects
Use useResource$() for data fetching
Implement useTask$() for side effects
Utilize useVisibleTask$() for browser-only code
qwik js error handling optimization

When reviewing or writing code, apply these guidelines:

Implement proper error boundaries
Utilize Qwik City for routing when applicable
Use Qwik's built-in optimization features
Implement lazy-loading for improved performance
qwik js folder structure

When reviewing or writing code, apply these guidelines:

Use the following folder structure:

src/ components/ routes/ global.css root.tsx entry.ssr.tsx public/ vite.config.ts tsconfig.json

qwik js general preferences

When reviewing or writing code, apply these guidelines:

Always prefer functional components in Qwik files
Use TypeScript for type safety
Leverage Qwik's resumability model for optimal performance
Minimize client-side JavaScript via lazy loading
Consolidated Skills

This expert skill consolidates 1 individual skills:

qwik-expert
Iron Laws
ALWAYS use the $ suffix for event handlers and lazy-loaded functions — without it, Qwik cannot extract them for resumability and forces full hydration.
NEVER access browser APIs (window, document, localStorage) in component body code — use useVisibleTask$() to scope browser-only code and prevent SSR errors.
ALWAYS use useSignal() for reactive primitive state and useStore() for complex objects — plain variables are not reactive and will not trigger re-renders.
NEVER import large client-side libraries at the top level — use dynamic import() or lazy-load via $ to preserve Qwik's zero-JS-on-load advantage.
ALWAYS prefer functional components — Qwik's resumability model is designed exclusively for functional component paradigms; class components have no first-class support.
Anti-Patterns
Anti-Pattern	Why It Fails	Correct Approach
Using event handlers without $ suffix	Handler cannot be lazy-extracted; forces hydration and defeats resumability	Always use onClick$, onInput$, useTask$() etc. with $ suffix
Accessing window/document in component body	Throws during SSR where browser globals don't exist	Wrap browser-only code in useVisibleTask$() which runs client-side only
Using plain variables for reactive state	Variable changes don't trigger UI updates; components become stale	Use useSignal() for primitives; useStore() for objects
Top-level importing of large client libraries	Bundles library into initial JS payload; destroys zero-JS advantage	Use dynamic import() inside task handlers; lazy-load with $
Writing class-based components	Not supported by Qwik's serialization and resumability pipeline	Always use functional components with component$()
Memory Protocol (MANDATORY)

Before starting:

cat .claude/context/memory/learnings.md


After completing: Record any new patterns or exceptions discovered.

ASSUME INTERRUPTION: Your context may reset. If it's not in memory, it didn't happen.

Weekly Installs
61
Repository
oimiragieo/agent-studio
GitHub Stars
25
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail