---
rating: ⭐⭐
title: vue-testing-best-practices
url: https://skills.sh/hyf0/vue-skills/vue-testing-best-practices
---

# vue-testing-best-practices

skills/hyf0/vue-skills/vue-testing-best-practices
vue-testing-best-practices
Originally fromantfu/skills
Installation
$ npx skills add https://github.com/hyf0/vue-skills --skill vue-testing-best-practices
Summary

Comprehensive Vue.js testing guidance covering unit, component, and end-to-end testing strategies.

Addresses 11 common testing challenges including async handling, composable testing, Pinia store setup, Suspense components, and Teleport queries
Recommends Vitest for unit and component testing infrastructure, with Playwright as the preferred E2E framework
Covers black-box component testing patterns to reduce brittleness during refactoring, async/await synchronization, and snapshot test pitfalls
Includes guidance on browser vs. Node.js test runners for DOM verification and real event simulation
SKILL.md

Vue.js testing best practices, patterns, and common gotchas.

Testing
Setting up test infrastructure for Vue 3 projects → See testing-vitest-recommended-for-vue
Tests keep breaking when refactoring component internals → See testing-component-blackbox-approach
Tests fail intermittently with race conditions → See testing-async-await-flushpromises
Composables using lifecycle hooks or inject fail to test → See testing-composables-helper-wrapper
Getting "injection Symbol(pinia) not found" errors in tests → See testing-pinia-store-setup
Components with async setup won't render in tests → See testing-suspense-async-components
Snapshot tests keep passing despite broken functionality → See testing-no-snapshot-only
Choosing end-to-end testing framework for Vue apps → See testing-e2e-playwright-recommended
Tests need to verify computed styles or real DOM events → See testing-browser-vs-node-runners
Testing components created with defineAsyncComponent fails → See async-component-testing
Teleported modal content can't be found in wrapper queries → See teleport-testing-complexity
Reference
Vue.js Testing Guide
Vue Test Utils
Vitest Documentation
Playwright Documentation
Weekly Installs
1.4K
Repository
hyf0/vue-skills
GitHub Stars
2.3K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass