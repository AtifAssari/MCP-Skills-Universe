---
title: vue-router-best-practices
url: https://skills.sh/vuejs-ai/skills/vue-router-best-practices
---

# vue-router-best-practices

skills/vuejs-ai/skills/vue-router-best-practices
vue-router-best-practices
Originally fromantfu/skills
Installation
$ npx skills add https://github.com/vuejs-ai/skills --skill vue-router-best-practices
Summary

Vue Router 4 patterns, navigation guards, and route-lifecycle best practices.

Covers five navigation guard patterns including async/await handling, deprecated next() function migration, and infinite redirect loop prevention
Addresses route lifecycle gotchas such as stale data when navigating with param changes and event listener cleanup on unmount
Includes guidance on component instance access in beforeRouteEnter guards and param-change detection across same-route navigation
Provides production single-page application setup recommendations
SKILL.md

Vue Router best practices, common gotchas, and navigation patterns.

Navigation Guards
Navigating between same route with different params → See router-beforeenter-no-param-trigger
Accessing component instance in beforeRouteEnter guard → See router-beforerouteenter-no-this
Navigation guard making API calls without awaiting → See router-guard-async-await-pattern
Users trapped in infinite redirect loops → See router-navigation-guard-infinite-loop
Navigation guard using deprecated next() function → See router-navigation-guard-next-deprecated
Route Lifecycle
Stale data when navigating between same route → See router-param-change-no-lifecycle
Event listeners persisting after component unmounts → See router-simple-routing-cleanup
Setup
Building production single-page application → See router-use-vue-router-for-production
Weekly Installs
5.6K
Repository
vuejs-ai/skills
GitHub Stars
2.3K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass