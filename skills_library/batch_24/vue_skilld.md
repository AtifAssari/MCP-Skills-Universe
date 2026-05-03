---
title: vue-skilld
url: https://skills.sh/harlan-zw/vue-ecosystem-skills/vue-skilld
---

# vue-skilld

skills/harlan-zw/vue-ecosystem-skills/vue-skilld
vue-skilld
Installation
$ npx skills add https://github.com/harlan-zw/vue-ecosystem-skills --skill vue-skilld
SKILL.md
vuejs/core vue@3.6.0-beta.10

Tags: csp: 1.0.28-csp, v2-latest: 2.7.16, legacy: 2.7.16

References: Docs

API Changes

This section documents version-specific API changes — prioritize recent major/minor releases.

NEW: createVaporApp() (experimental) — new in v3.6, creates a Vapor-mode app instance without pulling in the Virtual DOM runtime; use createApp() for standard VDOM apps source

NEW: vaporInteropPlugin (experimental) — new in v3.6, install into a VDOM createApp() instance to allow Vapor components inside VDOM trees; without it, Vapor SFCs cannot be used in VDOM apps source

NEW: <script setup vapor> attribute (experimental) — new in v3.6, opts an SFC into Vapor Mode compilation; only works with <script setup>; does not support Options API, app.config.globalProperties, or getCurrentInstance() source

NEW: useTemplateRef(key) — new in v3.5, preferred replacement for plain ref variable names matching ref="key" attributes; supports dynamic string IDs at runtime unlike the old static-only pattern source

NEW: useId() — new in v3.5, generates stable unique IDs per component instance guaranteed to match between SSR and client hydration; replaces manual ID management for form/accessibility attributes source

NEW: onWatcherCleanup(fn) — new in v3.5, registers a cleanup callback inside a watch or watchEffect callback; replaces the onCleanup parameter pattern and can be called from nested functions source

NEW: hydrateOnVisible(), hydrateOnIdle(), hydrateOnInteraction(), hydrateOnMediaQuery() — new in v3.5, lazy hydration strategies passed to defineAsyncComponent({ hydrate: hydrateOnVisible() }); without the hydrate option, async components hydrate immediately source

NEW: defineModel() stable — promoted from experimental in v3.3 to stable in v3.4; automatically declares a prop and returns a mutable ref; replaces the manual defineProps + defineEmits('update:modelValue') pattern source

NEW: defineProps destructure with defaults — stabilized in v3.5 (was experimental in v3.3); const { count = 0 } = defineProps<{ count?: number }>() replaces withDefaults(defineProps<...>(), { count: 0 }); destructured vars must be wrapped in getters to pass to watch() or composables source

BREAKING: @vnodeXXX event listeners — removed in v3.4, are now a compiler error; use @vue:XXX listeners instead (e.g. @vue:mounted) source

BREAKING: Reactivity Transform ($ref, $computed, etc.) — removed in v3.4 after being deprecated in v3.3; was experimental and distinct from the now-stable props destructure feature; use Vue Macros plugin to continue using it source

BREAKING: Global JSX namespace — no longer registered by default since v3.4; set jsxImportSource: "vue" in tsconfig.json or import vue/jsx to restore it; affects TSX users only source

BREAKING: app.config.unwrapInjectedRef — removed in v3.4; ref unwrapping in inject() is now always enabled and cannot be disabled source

NEW: <Teleport defer> prop — new in v3.5, mounts the teleport after the current render cycle so the target element can be rendered by Vue in the same component tree; requires explicit defer attribute for backwards compatibility source

Also changed: defineSlots<{}>() macro NEW v3.3 for typed slot declarations · defineOptions({}) macro NEW v3.3 to set component options without a separate <script> block · toRef(() => getter) enhanced in v3.3 to accept plain values and getters · toValue() NEW v3.3 normalizes values/getters/refs to values (inverse of toRef) · v-bind same-name shorthand NEW v3.4 (:id shorthand for :id="id") · data-allow-mismatch attribute NEW v3.5 to suppress hydration mismatch warnings · useHost() / useShadowRoot() NEW v3.5 for custom element host access · v-is directive REMOVED v3.4 (use is="vue:ComponentName" instead) · reactivity system alien-signals refactor in v3.6 improves memory usage with no API changes

Best Practices

Use reactive props destructure (3.5+) with native default value syntax instead of withDefaults() — destructured variables are reactive and the compiler rewrites accesses to props.x automatically. When passing to composables or watch, wrap in a getter: watch(() => count, ...) source

Use toValue() in composables to normalize MaybeRefOrGetter<T> arguments — handles plain values, refs, and getter functions uniformly so callers can pass any form without the composable caring source

Use onWatcherCleanup() (3.5+) instead of the onCleanup callback parameter in watch and watchEffect — it can be called from any helper function in the sync execution stack, not just the top-level callback, making cleanup logic easier to extract source

Use useTemplateRef() (3.5+) instead of a plain ref with a matching variable name for template refs — supports dynamic ref IDs and provides better IDE auto-completion and type checking via @vue/language-tools 2.1 source

Use useId() (3.5+) for form element and accessibility IDs in SSR apps — generated IDs are stable across server and client renders, preventing hydration mismatches. Avoid calling inside computed() as it can cause instance conflicts source

Use shallowRef() / shallowReactive() for large immutable data structures — deep reactivity tracks every property access via proxy traps; shallow variants avoid this overhead while still reacting to root .value replacement source

Pass computed values directly as active props rather than IDs for comparison — child components re-render when any received prop changes, so passing a stable boolean avoids re-rendering every list item when only one item's active state changes source

When a computed returns a new object on every evaluation, accept oldValue and return it unchanged when data is equivalent — avoids unnecessary downstream effect triggers since Vue 3.4+ only triggers effects when the computed value reference changes source

Use defineAsyncComponent with a lazy hydration strategy (3.5+) for SSR — hydrateOnVisible(), hydrateOnIdle(), hydrateOnInteraction(), and hydrateOnMediaQuery() are tree-shakable and defer hydration until the component is actually needed

import { defineAsyncComponent, hydrateOnVisible } from 'vue'

const AsyncComp = defineAsyncComponent({
  loader: () => import('./Comp.vue'),
  hydrate: hydrateOnVisible()
})


source

(experimental) Opt in to Vapor Mode per-component with <script setup vapor> when targeting performance-sensitive UI — Vapor avoids Virtual DOM diffing entirely and achieves Solid/Svelte 5 benchmark parity, but does not support Options API, app.config.globalProperties, or getCurrentInstance(). Use vaporInteropPlugin to mix Vapor and VDOM components in an existing app source
Weekly Installs
193
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