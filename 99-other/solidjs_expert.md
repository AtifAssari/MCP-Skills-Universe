---
title: solidjs-expert
url: https://skills.sh/oimiragieo/agent-studio/solidjs-expert
---

# solidjs-expert

skills/oimiragieo/agent-studio/solidjs-expert
solidjs-expert
Installation
$ npx skills add https://github.com/oimiragieo/agent-studio --skill solidjs-expert
SKILL.md
Solidjs Expert
solidjs complex state management

When reviewing or writing code, apply these guidelines:

Utilize createStore() for complex state management.
solidjs conditional and list rendering

When reviewing or writing code, apply these guidelines:

Implement Show and For components for conditional and list rendering.
solidjs data fetching

When reviewing or writing code, apply these guidelines:

Use createResource() for data fetching.
solidjs derived values management

When reviewing or writing code, apply these guidelines:

Implement createMemo() for derived values.
solidjs error boundaries

When reviewing or writing code, apply these guidelines:

Implement proper error boundaries
solidjs folder structure

When reviewing or writing code, apply these guidelines:

Use the following folder structure: src/ components/ pages/ styles/ App.jsx index.jsx
solidjs functional components

When reviewing or writing code, apply these guidelines:

Always use functional components in SolidJS.
solidjs functional components preference

When reviewing or writing code, apply these guidelines:

Always use functional components instead of class components.
solidjs jsx templates

When reviewing or writing code, apply these guidelines:

Use JSX for component templates
solidjs lazy loading

When reviewing or writing code, apply these guidelines:

Implement lazy-loading for improved performance
solidjs naming conventions

When reviewing or writing code, apply these guidelines:

Follow Solid.js naming conventions and best practices
solidjs optimization features

When reviewing or writing code, apply these guidelines:

Use Solid's built-in optimization features
solidjs project folder structure

When reviewing or writing code, apply these guidelines:

Enforce the following folder structure:

src/ components/ pages/ utils/ types/ App.tsx index.tsx

solidjs reactive primitives

When reviewing or writing code, apply these guidelines:

Use createSignal() for simple reactive state
Use createEffect() for side effects that depend on reactive state
Leverage fine-grained reactivity — avoid unnecessary re-renders
Consolidated Skills

This expert skill consolidates 1 individual skills:

solidjs-expert
Iron Laws
NEVER use React patterns like useState/useEffect in SolidJS — signals and effects work differently
ALWAYS wrap stores in createStore for nested reactive state, not plain objects
NEVER destructure props directly — always access via the props object to preserve reactivity
ALWAYS use For, Show, Switch, and Match components for reactive rendering, not .map()
NEVER assume DOM manipulation happens in render functions — SolidJS runs render once, effects update
Anti-Patterns
Anti-Pattern	Why It Fails	Correct Approach
Using React mental model	SolidJS uses fine-grained reactivity, not virtual DOM diffing	Learn SolidJS signals, memos, and effects as distinct primitives
Destructuring props	Loses reactivity tracking on accessed properties	Access props directly: props.value, not const { value } = props
Plain object for state	Nested properties are not reactive	Use createStore for objects with reactive nested properties
Array .map() in JSX	Non-reactive; full re-render on any array change	Use the <For> component for reactive list rendering
Reading signals outside tracking scope	Effect does not re-run when signal changes	Access signals only inside createEffect, createMemo, or JSX
Memory Protocol (MANDATORY)

Before starting:

cat .claude/context/memory/learnings.md


After completing: Record any new patterns or exceptions discovered.

ASSUME INTERRUPTION: Your context may reset. If it's not in memory, it didn't happen.

Weekly Installs
41
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