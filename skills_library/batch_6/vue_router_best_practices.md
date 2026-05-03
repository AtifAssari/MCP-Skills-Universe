---
title: vue-router-best-practices
url: https://skills.sh/antfu/skills/vue-router-best-practices
---

# vue-router-best-practices

skills/antfu/skills/vue-router-best-practices
vue-router-best-practices
Installation
$ npx skills add https://github.com/antfu/skills --skill vue-router-best-practices
Summary

Vue Router 4 patterns, navigation guards, and route-lifecycle best practices.

Covers five navigation guard patterns including async/await handling, deprecated next() function migration, infinite redirect loops, and param-change detection
Addresses route-lifecycle gotchas like stale data when navigating between same routes and event listener cleanup on component unmount
Includes production SPA setup guidance and component instance access patterns in beforeRouteEnter guards
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
11.8K
Repository
antfu/skills
GitHub Stars
4.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass