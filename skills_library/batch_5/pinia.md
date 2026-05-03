---
title: pinia
url: https://skills.sh/uni-helper/skills/pinia
---

# pinia

skills/uni-helper/skills/pinia
pinia
Originally fromantfu/skills
Installation
$ npx skills add https://github.com/uni-helper/skills --skill pinia
SKILL.md
Pinia

Pinia is the official state management library for Vue, designed to be intuitive and type-safe. It supports both Options API and Composition API styles, with first-class TypeScript support and devtools integration.

The skill is based on Pinia v3.0.4, generated at 2026-01-28.

Core References
Topic	Description	Reference
Stores	Defining stores, state, getters, actions, storeToRefs, subscriptions	core-stores
Features
Extensibility
Topic	Description	Reference
Plugins	Extend stores with custom properties, state, and behavior	features-plugins
Composability
Topic	Description	Reference
Composables	Using Vue composables within stores (VueUse, etc.)	features-composables
Composing Stores	Store-to-store communication, avoiding circular dependencies	features-composing-stores
Best Practices
Topic	Description	Reference
Testing	Unit testing with @pinia/testing, mocking, stubbing	best-practices-testing
Outside Components	Using stores in navigation guards, plugins, middlewares	best-practices-outside-component
Advanced
Topic	Description	Reference
SSR	Server-side rendering, state hydration	advanced-ssr
Nuxt	Nuxt integration, auto-imports, SSR best practices	advanced-nuxt
HMR	Hot module replacement for development	advanced-hmr
Key Recommendations
Prefer Setup Stores for complex logic, composables, and watchers
Use storeToRefs() when destructuring state/getters to preserve reactivity
Actions can be destructured directly - they're bound to the store
Call stores inside functions not at module scope, especially for SSR
Add HMR support to each store for better development experience
Use @pinia/testing for component tests with mocked stores
Weekly Installs
324
Repository
uni-helper/skills
GitHub Stars
58
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass