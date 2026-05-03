---
title: vue-pinia-best-practices
url: https://skills.sh/baotoq/agent-skills/vue-pinia-best-practices
---

# vue-pinia-best-practices

skills/baotoq/agent-skills/vue-pinia-best-practices
vue-pinia-best-practices
Installation
$ npx skills add https://github.com/baotoq/agent-skills --skill vue-pinia-best-practices
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
8
Repository
baotoq/agent-skills
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass