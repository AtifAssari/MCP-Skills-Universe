---
title: svelte-expert
url: https://skills.sh/oimiragieo/agent-studio/svelte-expert
---

# svelte-expert

skills/oimiragieo/agent-studio/svelte-expert
svelte-expert
Installation
$ npx skills add https://github.com/oimiragieo/agent-studio --skill svelte-expert
SKILL.md
Svelte Expert
svelte 5 component structure snippets

When reviewing or writing code, apply these guidelines:

Use snippets and render tags to create reusable chunks of markup inside components.
Snippets help reduce duplication and enhance maintainability.
svelte 5 general rules

When reviewing or writing code, apply these guidelines:

Always use Svelte 5 instead of Svelte 4.
Use runes for controlling reactivity; runes replace certain non-runes features and provide more explicit control over state and effects.
Treat event handlers as properties for simpler use and integration.
svelte 5 reactivity handling

When reviewing or writing code, apply these guidelines:

Prefer runes over reactive declarations ( $:) for reactivity, e.g. bind:value
Treat event handlers as properties, simplifying their use.
svelte and sveltekit general rules

When reviewing or writing code, apply these guidelines:

Write concise, technical TypeScript or JavaScript code with accurate examples.
Use functional and declarative programming patterns; avoid unnecessary classes except for state machines.
Prefer iteration and modularization over code duplication.
Structure files: component logic, markup, styles, helpers, types.
Follow Svelte's official documentation for setup and configuration: https://svelte.dev/docs
Use lowercase with hyphens for component files (e.g., components/auth-form.svelte).
Use PascalCase for component names in imports and usage.
Use camelCase for variables, functions, and props.
Implement proper component composition and reusability.
Use Svelte's props for data passing.
Leverage Svelte's reactive declarations for local state management.
Ensure proper semantic HTML structure in Svelte components.
Implement ARIA attributes where necessary.
Ensure keyboard navigation support for interactive elements.
Use Svelte's bind:this for managing focus programmatically.
Embrace Svelte's simplicity and avoid over-engineering solutions
Consolidated Skills

This expert skill consolidates 1 individual skills:

svelte-expert
Iron Laws
NEVER use Svelte 4 reactive declarations ($:) in new code — use Svelte 5 runes
ALWAYS use file-based routing and load functions for data fetching in SvelteKit
NEVER use stores for local component state — use $state and $derived runes
ALWAYS implement +error.svelte error boundaries for every route group that can fail
NEVER skip accessibility semantics — ensure ARIA attributes and keyboard navigation
Anti-Patterns
Anti-Pattern	Why It Fails	Correct Approach
Using Svelte 4 reactive syntax	Legacy patterns conflict with rune-based reactivity	Use $state(), $derived(), and $effect() runes in all new code
Global stores for local state	Unnecessary coupling; component state leaks	Use $state rune for component-local reactive state
Ignoring SvelteKit routing conventions	Manual routing breaks framework integration	Follow file-based routing; use +page.svelte and +layout.svelte
Missing +error.svelte handlers	Unhandled route errors produce blank pages	Add +error.svelte to every route group that can fail
Skipping accessibility attributes	Screen readers and keyboard users cannot use the UI	Always add ARIA labels and test keyboard navigation
Memory Protocol (MANDATORY)

Before starting:

cat .claude/context/memory/learnings.md


After completing: Record any new patterns or exceptions discovered.

ASSUME INTERRUPTION: Your context may reset. If it's not in memory, it didn't happen.

Weekly Installs
59
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