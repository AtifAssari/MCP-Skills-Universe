---
title: vueuse-shared-skilld
url: https://skills.sh/harlan-zw/vue-ecosystem-skills/vueuse-shared-skilld
---

# vueuse-shared-skilld

skills/harlan-zw/vue-ecosystem-skills/vueuse-shared-skilld
vueuse-shared-skilld
Installation
$ npx skills add https://github.com/harlan-zw/vue-ecosystem-skills --skill vueuse-shared-skilld
SKILL.md
vueuse/vueuse @vueuse/shared@14.2.1

Tags: next: 5.0.0, alpha: 14.0.0-alpha.3, beta: 14.0.0-beta.1

References: Docs

API Changes

This section documents version-specific API changes — prioritize recent major/minor releases.

BREAKING: Requires Vue 3.5 — v14 now requires Vue 3.5+ for native performance optimizations source

BREAKING: useThrottleFn alignment — v14 aligned with traditional throttle behavior (leading: true, trailing: false by default) source

BREAKING: ESM-only — v13 dropped CJS build support, package is now ESM-only source

BREAKING: createSharedComposable return — v14 now returns only the sharedComposable instance on the client side source

NEW: refManualReset — new function in v14 for creating refs with an explicit reset() method source

NEW: watchAtMost controls — v14 added pause, resume, and count to the return value source

NEW: tryOnScopeDispose — v14 added optional failSilently parameter to suppress errors outside of scope source

NEW: useArrayReduce type — v14.1.0 now exports the UseArrayReduceReturn type source

NEW: computedWithControl sources — v14.1.0 allows different types in watch sources array source

DEPRECATED: computedEager — v14 deprecated in favor of Vue 3.5's native computed optimizations source

DEPRECATED: watchPausable — v14 deprecated in favor of Vue's built-in watch or pausableFilter source

DEPRECATED: Alias exports — v14 deprecated secondary names like ignorableWatch in favor of primary watchIgnorable source

DEPRECATED: eagerComputed — v14 deprecated alias in favor of computedEager source

DEPRECATED: controlledComputed — v14 deprecated alias in favor of computedWithControl source

Also changed: createReactiveFn DEPRECATED · autoResetRef DEPRECATED · debouncedRef DEPRECATED · useDebounce DEPRECATED · throttledRef DEPRECATED · useThrottle DEPRECATED · controlledRef DEPRECATED · debouncedWatch DEPRECATED · ignorableWatch DEPRECATED · pausableWatch DEPRECATED · throttledWatch DEPRECATED

Best Practices

Prefer Vue 3.4+ built-in computed() over computedEager() — standard computed properties now only trigger dependencies if the return value actually changes, making eager evaluation unnecessary source

Use createSharedComposable() for SSR-safe state sharing — it automatically falls back to non-shared instances during SSR to prevent cross-request state pollution, while maintaining a singleton on the client source

Share state within the same component using provideLocal() and injectLocal() — allows accessing provided values without going through the parent/child boundary, now with full Vapor mode support source

Replace manual watchers with until() for one-time async conditions — provides a promise-based API for flow control that resolves once a ref meets a specific requirement, reducing callback nesting source

// Preferred for one-time triggers
await until(isReady).toBe(true)
doSomething()


Implement refManualReset() for easy state restoration — provides a built-in .reset() method to return the ref to its initial value, ideal for clearing forms or reset-to-default filters source

Use reactify() to transform plain utility functions into reactive ones — automatically accepts refs as arguments and returns a ComputedRef, enabling rapid development of reactive logic source

Optimize hot paths with refWithControl() using peek() and lay() — allows reading or writing a ref's value without triggering the reactivity system or tracking dependencies, minimizing unnecessary updates source

Return dual object/array APIs via makeDestructurable() — makes your custom composables more flexible by allowing users to choose between positional (array) or named (object) destructuring source

Convert state during synchronization with syncRef() custom transforms — use the transform option with ltr and rtl functions to map values between refs of different types source

// Sync a number ref with a string ref
syncRef(count, stringCount, {
  transform: {
    ltr: left => String(left),
    rtl: right => Number(right)
  }
})

Choose createGlobalState() for persistent application-wide singletons — unlike shared composables which dispose state when subscribers reach zero, global state remains alive for the entire app lifecycle source
Weekly Installs
84
Repository
harlan-zw/vue-e…m-skills
GitHub Stars
158
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass