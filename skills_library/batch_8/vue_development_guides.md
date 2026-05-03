---
title: vue-development-guides
url: https://skills.sh/hyf0/vue-skills/vue-development-guides
---

# vue-development-guides

skills/hyf0/vue-skills/vue-development-guides
vue-development-guides
Originally fromvuejs-ai/skills
Installation
$ npx skills add https://github.com/hyf0/vue-skills --skill vue-development-guides
Summary

Best practices and architectural patterns for Vue 3 and Nuxt 3 projects.

Emphasizes core principles: predictable state with single source of truth, explicit data flow (props down, events up), and small focused components
Requires Composition API with <script setup lang="ts"> as the default, and mandates following detailed guides for reactivity, SFC structure, and component organization
Provides a checklist-driven approach covering component splitting, composable extraction, and data flow patterns including props, emits, v-model, and provide/inject
Includes references for state management, reactivity best practices, and SFC conventions to ensure consistency across Vue and Nuxt applications
SKILL.md
Vue.js Development Guides
Tasks Checklist
 Followed the core principles
 Followed the defaults unless there is a good reason not to
 Followed the reactivity best practices
 Followed the component best practices
 Followed the Vue SFC best practices
 Kept components focused
 Split large components into smaller ones when needed
 Moved state/side effects into composables if applicable
 Followed data flow best practices
Core Principles
Keep state predictable: one source of truth, derive everything else.
Make data flow explicit: Props down, Events up for most cases.
Favor small, focused components: easier to test, reuse, and maintain.
Avoid unnecessary re-renders: use computed properties and watchers wisely.
Readability counts: write clear, self-documenting code.
Defaults (unless the user says otherwise)
Prefer the Composition API over the Options API.
Reactivity

IMPORTANT: You MUST follow the references/reactivity-guide.md for reactive state management when creating, updating a component or a composable.

Components

IMPORTANT: You MUST follow the references/sfc-guide.md for best practices when working with Vue SFCs.

Prefer Vue Single-File Components (SFC) using <script setup lang="ts"> (TypeScript) by default.
In Vue SFCs, keep sections in this order: <script> → <template> → <style>.
Keep components focused

Split a component when it has more than one clear responsibility (e.g. data orchestration + UI, or multiple independent UI sections).

Prefer smaller components + composables over one “mega component”
Move UI sections into child components (props in, events out).
Move state/side effects into composables (useXxx()).

NOTE: This rule also applies to the entry component (e.g. App.vue) in a Vue / Nuxt project by default.

Data Flow

IMPORTANT: You MUST follow the references/data-flow-guide.md for passing and receiving data between components using:

Props
Emits
v-model
provide/inject

For sharing data across the app, please follow the references/state-management-guide.md and consider using a Store for state management solution.

Weekly Installs
499
Repository
hyf0/vue-skills
GitHub Stars
2.3K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass