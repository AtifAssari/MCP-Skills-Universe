---
title: tanstack-vue-query-skilld
url: https://skills.sh/harlan-zw/vue-ecosystem-skills/tanstack-vue-query-skilld
---

# tanstack-vue-query-skilld

skills/harlan-zw/vue-ecosystem-skills/tanstack-vue-query-skilld
tanstack-vue-query-skilld
Installation
$ npx skills add https://github.com/harlan-zw/vue-ecosystem-skills --skill tanstack-vue-query-skilld
SKILL.md
TanStack/query @tanstack/vue-query@5.100.7

Tags: alpha: 5.0.0-alpha.91, beta: 5.0.0-beta.35, rc: 5.0.0-rc.16

References: Docs

API Changes

This section documents version-specific API changes — prioritize recent major/minor releases.

BREAKING: useQueries() returns Ref<T[]> instead of Reactive<T[]> — Vue 2.7+ compatibility fix that aligns with other composables. Destructuring return value now requires unwrapping ref or using toRefs(). Update: const { data } = useQueries(...) becomes const { data } = useQueries(...).value or const { data } = toRefs(useQueries(...))[0] source

NEW: Composables support injectionContext — useQuery, useMutation, and other composables can now run in functions with injection context (e.g., router navigation guards), not just component setup(). Must use within effectScope to prevent memory leaks source

NEW: Options getter functions in useQuery — pass reactive getters to queryKey and enabled options to track changes without computed(). Example: useQuery({ queryKey: () => ['posts', userId.value], enabled: () => isReady.value }) source

NEW: Options getter functions extended to additional composables — useInfiniteQuery, useMutation, usePrefetchQuery, and usePrefetchInfiniteQuery now support reactive getters for all reactive options source

NEW: enableDevtoolsV6Plugin option for Traditional Devtools — integrate with Vue DevTools v6+ for custom inspector and timeline events. Enable: app.use(VueQueryPlugin, { enableDevtoolsV6Plugin: true }). Both v6 and v7 supported source

EXPERIMENTAL: experimental_createQueryPersister — persist individual queries to storage (AsyncStorage, LocalStorage, custom). Separate package @tanstack/query-persist-client-core. Includes persistQueryByKey(), retrieveQuery(), restoreQueries(), persisterGc() utilities. Respects staleTime on restore source

EXPERIMENTAL: broadcastQueryClient plugin — sync query cache across browser tabs and windows via message broadcasting. Experimental API, separate package, subject to change source

Also changed: Vue 3.3+ now required (was 3.x) · suspense() method on useQuery return for explicit await · VueQueryPlugin initialization unchanged · Query options now support getters alongside refs and values

Best Practices

Always use queryOptions() helper when defining query configurations, rather than passing objects directly to useQuery — this enables TypeScript inference, prevents queryKey/queryFn mismatches at runtime, and allows safe reuse with queryClient methods like getQueryData() and invalidateQueries() source

Pass reactive values (Ref or computed) directly into the queryKey array, not their .value — Vue Query automatically tracks reactive dependencies and refetches when they change source

Accept MaybeRefOrGetter<T> in composable parameters instead of string values — this allows callers to pass refs, plain values, or reactive getters (() => props.userId) without wrapper code, giving maximum flexibility source

Use computed(() => props.property) for derived state from component props, not direct property access — property access on reactive objects loses reactivity, but computed captures it in the query's reactive tracking source

Include all external variables used in queryFn in the queryKey — treat the query key like a dependency array; missing dependencies cause stale data and prevent proper cache invalidation source

Create a single QueryClient instance at app initialization, not inside components — the client holds the cache for the entire app lifecycle, and recreating it loses all cached data source

Destructure only the fields you actually use from query results; avoid object rest destructuring (...rest) — rest destructuring subscribes to all fields, triggering unnecessary re-renders on any cache change source

Use skipToken in a computed queryFn for conditional queries instead of enabled — this is more elegant for complex conditions and makes the intent clearer that the query should not run at all source

Provide placeholderData as a function that queries other cache entries — this allows rendering stale detail data while fresh data loads, creating seamless UX transitions source

Set gcTime: Infinity in server-side QueryClient defaults to prevent memory accumulation — the server creates isolated clients per request and should rely on automatic cleanup rather than manual garbage collection source

Use queryClient.setMutationDefaults() to define default mutation functions keyed by mutationKey — this enables persisted mutations to resume after a page reload by replaying the same function source

Call toRefs() on the result of useQueries with combine before destructuring — the combined result is wrapped in a Ref for Vue 2 compatibility, and destructuring directly loses reactivity source

Prefetch infinite query pages with the pages option and provide getNextPageParam — this pre-fills multiple pages into the cache, reducing pagination load states and waterfalls source

Use a computed() expression for the enabled option when the condition depends on reactive state — this keeps the query automatically in sync with changing conditions without manual tracking source

Weekly Installs
107
Repository
harlan-zw/vue-e…m-skills
GitHub Stars
158
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass