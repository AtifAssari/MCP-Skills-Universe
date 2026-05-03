---
title: vue-pinia-best-practices
url: https://skills.sh/hyf0/vue-skills/vue-pinia-best-practices
---

# vue-pinia-best-practices

skills/hyf0/vue-skills/vue-pinia-best-practices
vue-pinia-best-practices
Originally fromvuejs-ai/skills
Installation
$ npx skills add https://github.com/hyf0/vue-skills --skill vue-pinia-best-practices
Summary

Vue Pinia state management patterns, common reactivity pitfalls, and store setup best practices.

Covers three core areas: store initialization, reactivity patterns, and state management conventions
Addresses frequent gotchas including destructuring breaking reactivity, method binding issues, and missing state in DevTools or SSR
Provides guidance on filter persistence, URL-based ephemeral state, and scaling Pinia for production applications
Includes troubleshooting references for "getActivePinia was called" errors and setup store state visibility problems
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
1.7K
Repository
hyf0/vue-skills
GitHub Stars
2.3K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass