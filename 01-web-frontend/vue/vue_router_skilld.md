---
rating: ⭐⭐
title: vue-router-skilld
url: https://skills.sh/harlan-zw/vue-ecosystem-skills/vue-router-skilld
---

# vue-router-skilld

skills/harlan-zw/vue-ecosystem-skills/vue-router-skilld
vue-router-skilld
Installation
$ npx skills add https://github.com/harlan-zw/vue-ecosystem-skills --skill vue-router-skilld
SKILL.md
vuejs/router vue-router@5.0.6

Tags: next: 4.0.13, legacy: 3.6.5, edge: 4.4.0-alpha.3

References: Docs

API Changes

This section documents version-specific API changes — prioritize recent major/minor releases.

NEW: vue-router/vite — v5 ships the Vite plugin (formerly unplugin-vue-router/vite) directly in the core package; import from vue-router/vite instead source

NEW: vue-router/auto-routes — v5 export that provides the auto-generated file-based route list; previously required unplugin-vue-router as a separate package source

NEW: vue-router/unplugin — v5 export for Webpack/Rollup/esbuild plugins and utilities (VueRouterAutoImports, EditableTreeNode, createRoutesContext, etc.); previously imported from unplugin-vue-router source

NEW: DataLoaderPlugin + defineBasicLoader (experimental) — v5 adds data loaders directly to vue-router/experimental; previously in unplugin-vue-router/data-loaders. Install DataLoaderPlugin before the router with app.use(DataLoaderPlugin, { router }) source

NEW: defineColadaLoader (experimental) — Pinia Colada-backed loader available at vue-router/experimental/pinia-colada; previously unplugin-vue-router/data-loaders/pinia-colada source

NEW: NavigationResult (experimental) — class from vue-router/experimental returned inside a loader to redirect during navigation (e.g. return new NavigationResult('/login')); previously did not exist in vue-router source

NEW: Volar plugins moved to vue-router/volar/sfc-typed-router and vue-router/volar/sfc-route-blocks — previously unplugin-vue-router/volar/sfc-typed-router and unplugin-vue-router/volar/sfc-route-blocks source

NEW: TypesConfig module augmentation — v4.4+ interface used to register RouteNamedMap for typed routes; augment with declare module 'vue-router' { interface TypesConfig { RouteNamedMap: RouteNamedMap } } source

BREAKING: IIFE build no longer bundles @vue/devtools-api — v5 upgraded devtools-api to v8 which has no IIFE build; affects CDN/script-tag setups that relied on the bundled devtools source

NEW: Query params optional by default (experimental) — v5 file-based routing makes query params optional in typed routes by default source

Also changed: unplugin-vue-router types/utilities moved to vue-router/unplugin (renamed) · route-map.d.ts replaces typed-router.d.ts (renamed) · meta.loaders array on route records for manually connecting data loaders (NEW, experimental) · router.currentRoute is Ref<RouteLocationNormalizedLoaded> — access via .value (v4 BREAKING) · router.onReady() removed — use router.isReady() returning a Promise (v4 BREAKING) · scrollBehavior x/y renamed to left/top (v4 BREAKING)

Best Practices

Use route.meta directly in guards instead of iterating to.matched — Vue Router merges all ancestor meta fields non-recursively, so to.meta.requiresAuth already reflects inherited values from parent routes source

Extend the RouteMeta interface via module augmentation to type all meta fields — this enforces that every route declares required fields at compile time rather than relying on runtime checks source

Use router.beforeResolve (not beforeEach) for operations that must run after async components are resolved — it fires after all in-component guards and async route components are ready, making it the correct place for camera permission checks or final data validation source

Use inject() inside navigation guards (global or per-route) to access Pinia stores and provided values — this is supported since Vue 3.3 and avoids importing stores outside of setup context source

Avoid the next callback in guards — return values (false, a route location, or nothing) instead; next is error-prone because it must be called exactly once per code path and is considered a legacy API source

await router.push() and check the resolved value to detect navigation failures — the promise resolves to a NavigationFailure when blocked, or undefined on success; use isNavigationFailure(result, NavigationFailureType.aborted) to distinguish the specific failure type source

Set props: true (or a function) on route records to decouple components from useRoute() — components receiving params as props are reusable and testable without a router instance; use the function form (props: route => ({ query: route.query.q })) to map query params or cast types source

Watch specific route properties rather than the whole route object — useRoute() returns a reactive object, but watching it entirely triggers on any change (hash, query, params); narrow the watcher to () => route.params.id to avoid unnecessary fetches source

(experimental) Use defineBasicLoader / defineColadaLoader exported from page components for navigation-aware data fetching — loaders exported from lazy-loaded route components are automatically connected to the navigation lifecycle, block the transition until resolved, and expose isLoading/error reactively; set lazy: true for non-critical data that should not block navigation source

Weekly Installs
125
Repository
harlan-zw/vue-e…m-skills
GitHub Stars
158
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass