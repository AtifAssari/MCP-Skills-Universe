---
title: sveltekit-structure
url: https://skills.sh/spences10/svelte-skills-kit/sveltekit-structure
---

# sveltekit-structure

skills/spences10/svelte-skills-kit/sveltekit-structure
sveltekit-structure
Installation
$ npx skills add https://github.com/spences10/svelte-skills-kit --skill sveltekit-structure
Summary

SvelteKit routing, layouts, error handling, and SSR structure guidance.

File-based routing with +page.svelte for pages, +layout.svelte for nested wrappers, +error.svelte for error boundaries, and +server.ts for API endpoints
Nested layouts apply to all child routes; use route groups with (name) folders to organize without affecting URLs
Error boundaries and pending UI patterns via +error.svelte placement and svelte:boundary component-level error/pending states
SSR and hydration guidance including browser-only code detection and client-side considerations
SKILL.md
SvelteKit Structure
Quick Start

File types: +page.svelte (page) | +layout.svelte (wrapper) | +error.svelte (error boundary) | +server.ts (API endpoint)

Routes: src/routes/about/+page.svelte → /about | src/routes/posts/[id]/+page.svelte → /posts/123

Layouts: Apply to all child routes. +layout.svelte at any level wraps descendants.

Example
src/routes/
├── +layout.svelte              # Root layout (all pages)
├── +page.svelte                # Homepage /
├── about/+page.svelte          # /about
└── dashboard/
    ├── +layout.svelte          # Dashboard layout (dashboard pages only)
    ├── +page.svelte            # /dashboard
    └── settings/+page.svelte   # /dashboard/settings

<!-- +layout.svelte -->
<script>
	let { children } = $props();
</script>

<nav><!-- Navigation --></nav>
<main>{@render children()}</main>
<footer><!-- Footer --></footer>

Reference Files
file-naming.md - File naming conventions
layout-patterns.md - Nested layouts
error-handling.md - +error.svelte placement
svelte-boundary.md - Component-level error/pending
ssr-hydration.md - SSR and browser-only code
Notes
Layouts: {@render children()} | Errors: +error.svelte above failing route
Groups: (name) folders don't affect URL | Client-only: check browser
Last verified: 2025-01-11
Weekly Installs
462
Repository
spences10/svelt…ills-kit
GitHub Stars
77
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail