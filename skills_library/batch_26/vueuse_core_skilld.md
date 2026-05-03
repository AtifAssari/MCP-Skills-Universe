---
title: vueuse-core-skilld
url: https://skills.sh/harlan-zw/vue-ecosystem-skills/vueuse-core-skilld
---

# vueuse-core-skilld

skills/harlan-zw/vue-ecosystem-skills/vueuse-core-skilld
vueuse-core-skilld
Installation
$ npx skills add https://github.com/harlan-zw/vue-ecosystem-skills --skill vueuse-core-skilld
SKILL.md
vueuse/vueuse @vueuse/core@14.2.1

Tags: vue2: 2.0.35, vue3: 3.0.35, demi: 4.0.0-alpha.0

References: Docs

API Changes

This section documents version-specific API changes — prioritize recent major/minor releases.

BREAKING: computedAsync — default flush changed from pre to sync in v14.0.0; code relying on deferred evaluation now runs synchronously by default source

BREAKING: useThrottleFn — aligned with traditional throttle behavior in v14.0.0 (trailing call behavior changed); previously called on both leading and trailing by default, verify options match expected behavior source

BREAKING: createSharedComposable — on client side, now returns only the shared composable (single value) instead of a tuple/object in v14.0.0 source

BREAKING: useAsyncState — in v13.7.0, globalThis.reportError is now the default onError handler; previously errors were silently swallowed if no handler was provided source

BREAKING: CJS build dropped in v13.0.0 — @vueuse/core is now ESM-only; require('@vueuse/core') no longer works source

BREAKING: Vue 3.5 is now required as a minimum peer dependency since v14.0.0 source

DEPRECATED: watchPausable — will be removed in a future version; Vue 3.5 native watch() now returns { stop, pause, resume } directly; use const { pause, resume } = watch(src, cb) instead source

DEPRECATED: computedEager — will be removed in a future version; Vue 3.4+ computed() no longer triggers dependents when the value does not change, making this unnecessary source

DEPRECATED: templateRef(key) — deprecated in v13.6.0; use Vue's built-in useTemplateRef() instead source

DEPRECATED: executeTransition() — use the new transition() function instead; UseTransitionOptions.transition option also deprecated, use easing source

DEPRECATED: breakpointsVuetify — was an alias for breakpointsVuetifyV2; now deprecated, explicitly use breakpointsVuetifyV2 or breakpointsVuetifyV3 source

DEPRECATED: asyncComputed — alias for computedAsync, removed from v14 alias exports; import as computedAsync source

NEW: refManualReset(defaultValue) — added in v14.0.0; creates a ref with a .reset() method that restores the initial value source

NEW: useCssSupports(property, value) / useCssSupports(conditionText) — added in v14.2.0; reactive wrapper for CSS.supports() source

NEW: useTimeAgoIntl(time, options) — added in v13.7.0; Intl-based time-ago formatting using Intl.RelativeTimeFormat, supports custom units source

NEW: transition(source, from, to, options) — added in v14.0.0 as the non-deprecated replacement for executeTransition; also adds interpolation option for custom interpolator functions source

NEW: ConfigurableScheduler interface + scheduler option — added in v14.2.0 to timed composables (useCountdown, useNow, useTimestamp, useTimeAgo, useTimeAgoIntl, useElementByPoint, useMemory, useVibrate); replaces deprecated per-composable interval/immediate options source

NEW: useIdle — now implements Stoppable interface (v14.0.0), returns { pause, resume, stop } in addition to previous return values source

Also changed: useIntersectionObserver rootMargin is now reactive (v14.2.0) · useElementVisibility gains initialValue option (v14.1.0) and inherits reactive rootMargin (v14.2.0) · useDropZone gains checkValidity function (v14.1.0) · useRefHistory gains shouldCommit option (v13.4.0) · useUrlSearchParams gains stringify option (v13.4.0) · watchAtMost now returns { pause, resume } (v14.0.0) · useStorageAsync gains onReady option and Promise return (v13.6.0) · useAsyncState initial value can now be a ref (v14.0.0) · useSortable gains watchElement option (v14.2.0) · useWebSocket autoConnect.delay accepts a function (v14.1.0) · useClipboardItems exposes read() method (v13.7.0) · useDraggable gains auto-scroll with container-restricted dragging (v14.2.0) · useEventSource gains serializer option (v13.8.0) · onLongPress delay can now be a function (v14.0.0) · onClickOutside target can now be a getter function (v14.0.0)

Best Practices

Pass reactive getters (() => value) as arguments instead of plain refs where possible — VueUse 9+ supports getter arguments, enabling derived reactive values without an intermediate computed (e.g. useTitle(() => isDark.value ? 'Night' : 'Day')) source

Wrap useFetch calls in createFetch for app-wide config — sets base URL, auth headers, and CORS mode once; individual call sites inherit it without re-specifying options source

Use eventFilter option with throttleFilter / debounceFilter instead of manually wrapping callbacks — applies rate-limiting at the composable level for useLocalStorage, useMouse, and other event-driven composables source

Enable mergeDefaults: true (or pass a custom merge function) on useStorage when evolving stored object schemas — without it, new default keys are undefined if absent from existing storage data source

Use StorageSerializers from @vueuse/core when the useStorage default value is null — without a serializer hint, the type cannot be inferred and serialization falls back to raw string source

Use createSharedComposable to share a single composable instance across components — avoids duplicate event listeners and state. Note: in SSR it automatically falls back to a non-shared instance per call to prevent cross-request pollution source

Use computedWithControl when a computed value should only update on specific sources, not all its reactive dependencies — computed cannot opt out of automatic dependency tracking, but computedWithControl decouples the watch source from the getter source

Wrap VueUse calls outside component scope with effectScope() and call scope.stop() for cleanup — not all composables return a stop handle; effectScope is the universal escape hatch when composables are used in stores or non-component contexts source

Pass window option to browser composables like useMouse or useScroll to target iframes or mock globals in tests — all browser API composables accept configurable global dependencies via options source

Pass a custom scheduler to time-based composables (useNow, useCountdown, etc.) to align them with useRafFn or throttle their update rate — introduced in v14.1.0 / v14.2.0; without it, timed composables run on their own internal interval independent of animation frames source

Weekly Installs
116
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