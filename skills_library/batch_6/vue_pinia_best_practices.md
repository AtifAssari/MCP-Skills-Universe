---
title: vue-pinia-best-practices
url: https://skills.sh/vuejs-ai/skills/vue-pinia-best-practices
---

# vue-pinia-best-practices

skills/vuejs-ai/skills/vue-pinia-best-practices
vue-pinia-best-practices
Installation
$ npx skills add https://github.com/vuejs-ai/skills --skill vue-pinia-best-practices
Summary

Vue Pinia state management patterns, store setup guidance, and reactivity best practices.

Covers store initialization, DevTools integration, and SSR considerations for setup stores
Addresses common reactivity pitfalls including destructuring breaks and method binding issues in templates
Provides patterns for ephemeral state like filters, URL synchronization, and production app conventions
References specific error scenarios with linked solutions for quick troubleshooting
SKILL.md

Pinia best practices, common gotchas, and state management patterns.

Store Setup
Getting "getActivePinia was called" error at startup → See pinia-no-active-pinia-error
Setup stores missing state in DevTools or SSR → See pinia-setup-store-return-all-state
Reactivity
Store destructuring stops updating UI reactively → See pinia-store-destructuring-breaks-reactivity
Store methods lose context in template calls → See store-method-binding-parentheses
State Patterns
Filters reset on refresh or can't be shared → See state-url-for-ephemeral-filters
Building production app without DevTools or conventions → See state-use-pinia-for-large-apps
Weekly Installs
7.1K
Repository
vuejs-ai/skills
GitHub Stars
2.3K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass