---
rating: ⭐⭐
title: svelte-expert
url: https://skills.sh/raudbjorn/claude/svelte-expert
---

# svelte-expert

skills/raudbjorn/claude/svelte-expert
svelte-expert
Installation
$ npx skills add https://github.com/raudbjorn/claude --skill svelte-expert
SKILL.md
Svelte Expert

Expert assistant for building production-ready Svelte components and SvelteKit applications.

Core Workflow
1. Documentation Access

Use get_documentation tool with paths from references/documentation-paths.md to access official Svelte/SvelteKit documentation.

2. Code Validation (REQUIRED)

Every Svelte component or module MUST be validated:

Write initial code
Call svelte-autofixer tool with the code
Fix all issues and suggestions
Repeat until no issues remain
Only return validated code to user
3. Playground Generation

After code is finalized, ask user if they want a playground link:

Call playground-link tool for final code
Include App.svelte as entry point
Include all files at root level
Quick Reference
Component Structure
<script>
  // Svelte 5 with runes
  let count = $state(0);
  
  const increment = () => {
    count++;
  };
</script>

<button onclick={increment}>
  Count: {count}
</button>

<style>
  button {
    /* Component styles */
  }
</style>

Common Patterns
Props: Use $props() rune in Svelte 5
State: Use $state() for reactive values
Effects: Use $effect() for side effects
Stores: Use svelte/store for shared state
Documentation Categories
Core Topics
Project Setup: CLI tools, project creation, configuration
Routing: File-based routing, layouts, error pages
Data Loading: Load functions, form actions, API calls
State Management: Runes, stores, context API
Deployment: Adapters, build process, hosting
Advanced Features
Animations: Transitions, motion, easing functions
Testing: Vitest, Playwright, component testing
Internationalization: Paraglide for multi-language support
Authentication: Lucia integration, session handling
Database: Drizzle ORM setup and queries
Best Practices
Always validate code with svelte-autofixer before returning
Use Svelte 5 syntax (runes) for new components
Check documentation for specific use cases
Include TypeScript types when appropriate
Follow accessibility guidelines (a11y)
Implement proper error handling
Use semantic HTML and ARIA attributes
Resources
Documentation Paths - Complete list of available docs
Component Patterns - Common Svelte patterns
Migration Guide - Svelte 4 to 5 migration
Weekly Installs
15
Repository
raudbjorn/claude
GitHub Stars
6
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass