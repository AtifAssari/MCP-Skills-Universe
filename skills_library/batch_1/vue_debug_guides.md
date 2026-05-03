---
title: vue-debug-guides
url: https://skills.sh/hyf0/vue-skills/vue-debug-guides
---

# vue-debug-guides

skills/hyf0/vue-skills/vue-debug-guides
vue-debug-guides
Installation
$ npx skills add https://github.com/hyf0/vue-skills --skill vue-debug-guides
Summary

Comprehensive Vue 3 debugging reference covering reactivity, components, templates, lifecycle, SSR, and 100+ common runtime issues.

Organized by feature area (reactivity, computed, watchers, components, templates, forms, lifecycle, SSR, TypeScript, and more) with direct links to specific error scenarios and fixes
Covers Vue 3 specific gotchas including ref unwrapping, proxy identity hazards, v-model composition events, template ref timing, and hydration mismatches
Addresses async patterns, watcher cleanup, lifecycle hook timing, and memory leak prevention across composables and event listeners
Includes SSR and TypeScript debugging guidance for universal code, type safety with generics, and cross-request state pollution
SKILL.md

Vue 3 debugging and error handling for runtime issues, warnings, async failures, and hydration bugs. For development best practices and common gotchas, use vue-best-practices.

Reactivity
Tracing unexpected re-renders and state updates → See reactivity-debugging-hooks
Ref values not updating due to missing .value access → See ref-value-access
State stops updating after destructuring reactive objects → See reactive-destructuring
Refs inside arrays, Maps, or Sets not unwrapping → See refs-in-collections-need-value
Nested refs rendering as [object Object] in templates → See template-ref-unwrapping-top-level
Reactive proxy identity comparisons always return false → See reactivity-proxy-identity-hazard
Third-party instances breaking when proxied → See reactivity-markraw-for-non-reactive
Watchers only firing once per tick unexpectedly → See reactivity-same-tick-batching
Computed
Computed getter triggers mutations or requests unexpectedly → See computed-no-side-effects
Mutating computed values causes changes to disappear → See computed-return-value-readonly
Computed value never updates after conditional logic → See computed-conditional-dependencies
Sorting or reversing arrays breaks original state → See computed-array-mutation
Passing parameters to computed properties fails → See computed-no-parameters
Watchers
Async operations overwriting with stale data → See watch-async-cleanup
Creating watchers inside async callbacks → See watch-async-creation-memory-leak
Watcher never triggers for reactive object properties → See watch-reactive-property-getter
Async watchEffect misses dependencies after await → See watcheffect-async-dependency-tracking
DOM reads are stale inside watcher callbacks → See watch-flush-timing
Deep watchers report identical old/new values → See watch-deep-same-object-reference
watchEffect runs before template refs update → See watcheffect-flush-post-for-refs
Components
Child component throws "component not found" error → See local-components-not-in-descendants
Click listener doesn't fire on custom component → See click-events-on-components
Parent can't access child ref data in script setup → See component-ref-requires-defineexpose
HTML template parsing breaks Vue component syntax → See in-dom-template-parsing-caveats
Wrong component renders due to naming collisions → See component-naming-conflicts
Parent styles don't apply to multi-root component → See multi-root-component-class-attrs
Props & Emits
Variables referenced in defineProps cause errors → See prop-defineprops-scope-limitation
Component emits undeclared event causing warnings → See declare-emits-for-documentation
defineEmits used inside function or conditional → See defineEmits-must-be-top-level
defineEmits has both type and runtime arguments → See defineEmits-no-runtime-and-type-mixed
Native event listeners not responding to clicks → See native-event-collision-with-emits
Component event fires twice when clicking → See undeclared-emits-double-firing
Templates
Getting template compilation errors with statements → See template-expressions-restrictions
"Cannot read property of undefined" runtime errors → See v-if-null-check-order
Dynamic directive arguments not working properly → See dynamic-argument-constraints
v-else elements rendering unconditionally always → See v-else-must-follow-v-if
Mixing v-if with v-for causes precedence bugs and migration breakage → See no-v-if-with-v-for
Template function calls mutating state cause unpredictable re-render bugs → See template-functions-no-side-effects
Child components in loops showing undefined data → See v-for-component-props
Array order changing after sorting or reversing → See v-for-computed-reverse-sort
List items disappearing or swapping state unexpectedly → See v-for-key-attribute
Getting off-by-one errors with range iteration → See v-for-range-starts-at-one
v-show or v-else not working on template elements → See v-show-template-limitation
Template Refs
Ref becomes null when element is conditionally hidden → See template-ref-null-with-v-if
Ref array indices don't match data array in loops → See template-ref-v-for-order
Refactoring template ref names breaks silently in code → See use-template-ref-vue35
Forms & v-model
Initial form values not showing when using v-model → See v-model-ignores-html-attributes
Textarea content changes not updating the ref → See textarea-no-interpolation
iOS users cannot select dropdown first option → See select-initial-value-ios-bug
Parent and child components have different values → See define-model-default-value-sync
Object property changes not syncing to parent → See definemodel-object-mutation-no-emit
Real-time search/validation broken for Chinese/Japanese input → See v-model-ime-composition
Number input returns empty string instead of zero → See v-model-number-modifier-behavior
Custom checkbox values not submitted in forms → See checkbox-true-false-value-form-submission
Events & Modifiers
Chaining multiple event modifiers produces unexpected results → See event-modifier-order-matters
Keyboard shortcuts don't fire with system modifier keys → See keyup-modifier-timing
Keyboard shortcuts fire with unintended modifier combinations → See exact-modifier-for-precise-shortcuts
Combining passive and prevent modifiers breaks event behavior → See no-passive-with-prevent
Lifecycle
Memory leaks from unremoved event listeners → See cleanup-side-effects
DOM access fails before component mounts → See lifecycle-dom-access-timing
DOM reads return stale values after state changes → See dom-update-timing-nexttick
SSR rendering differs from client hydration → See lifecycle-ssr-awareness
Lifecycle hooks registered asynchronously never run → See lifecycle-hooks-synchronous-registration
Slots
Accessing child component data in slot content returns undefined values → See slot-render-scope-parent-only
Mixing named and scoped slots together causes compilation errors → See slot-named-scoped-explicit-default
Using v-slot on native HTML elements causes compilation errors → See slot-v-slot-on-components-or-templates-only
Unexpected content placement from implicit default slot behavior → See slot-implicit-default-content
Scoped slot props missing expected name property → See slot-name-reserved-prop
Wrapper components breaking child slot functionality → See slot-forwarding-to-child-components
Provide/Inject
Calling provide after async operations fails silently → See provide-inject-synchronous-setup
Tracing where provided values come from → See provide-inject-debugging-challenges
Injected values not updating when provider changes → See provide-inject-reactivity-not-automatic
Multiple components share same default object → See provide-inject-default-value-factory
Attrs
Both internal and fallthrough event handlers execute → See attrs-event-listener-merging
Explicit attributes overwritten by fallthrough values → See fallthrough-attrs-overwrite-vue3
Attributes applying to wrong element in wrappers → See inheritattrs-false-for-wrapper-components
Composables
Composable called outside setup context or asynchronously → See composable-call-location-restrictions
Composable reactive dependency not updating when input changes → See composable-tovalue-inside-watcheffect
Composable mutates external state unexpectedly → See composable-avoid-hidden-side-effects
Destructuring composable returns breaks reactivity unexpectedly → See composable-naming-return-pattern
Composition API
Lifecycle hooks failing silently after async operations → See composition-api-script-setup-async-context
Parent component refs unable to access exposed properties → See define-expose-before-await
Functional-programming patterns break expected Vue reactivity behavior → See composition-api-not-functional-programming
React Hook mental model causes incorrect Composition API usage → See composition-api-vs-react-hooks-differences
Animation
Animations fail to trigger when DOM nodes are reused → See animation-key-for-rerender
TransitionGroup list updates feel laggy under load → See animation-transitiongroup-performance
TypeScript
Mutable prop defaults leak state between component instances → See ts-withdefaults-mutable-factory-function
reactive() generic typing causes ref unwrapping mismatches → See ts-reactive-no-generic-argument
Template refs throw null access errors before mount or after v-if unmount → See ts-template-ref-null-handling
Optional boolean props behave as false instead of undefined → See ts-defineprops-boolean-default-false
Imported defineProps types fail with unresolvable or complex type references → See ts-defineprops-imported-types-limitations
Untyped DOM event handlers fail under strict TypeScript settings → See ts-event-handler-explicit-typing
Dynamic component refs trigger reactive component warnings → See ts-shallowref-for-dynamic-components
Union-typed template expressions fail type checks without narrowing → See ts-template-type-casting
Async Components
Route components misconfigured with defineAsyncComponent lazy loading → See async-component-vue-router
Network failures or timeouts loading components → See async-component-error-handling
Template refs undefined after component reactivation → See async-component-keepalive-ref-issue
Render Functions
Render function output stays static after state changes → See rendering-render-function-return-from-setup
Reused vnode instances render incorrectly → See render-function-vnodes-must-be-unique
String component names render as HTML elements → See rendering-resolve-component-for-string-names
Accessing vnode internals breaks on Vue updates → See render-function-avoid-internal-vnode-properties
Vue 2 render function patterns crash in Vue 3 → See rendering-render-function-h-import-vue3
Slot content not rendering from h() → See rendering-render-function-slots-as-functions
KeepAlive
Child components mount twice with nested Vue Router routes → See keepalive-router-nested-double-mount
Memory grows when combining KeepAlive with Transition animations → See keepalive-transition-memory-leak
Transitions
JavaScript transition hooks hang without done callback → See transition-js-hooks-done-callback
Move animations fail on inline list elements → See transition-group-flip-inline-elements
List items jump instead of smoothly animating → See transition-group-move-animation-position-absolute
Vue 2 to Vue 3 TransitionGroup wrapper changes break layout → See transition-group-no-default-wrapper-vue3
Nested transitions cut off before finishing → See transition-nested-duration
Scoped styles stop working in reusable transition wrappers → See transition-reusable-scoped-style
RouterView transitions animate unexpectedly on first render → See transition-router-view-appear
Mixing CSS transitions and animations causes timing issues → See transition-type-when-mixed
Cleanup hooks missed during rapid transition swaps → See transition-unmount-hook-timing
Teleport
Teleport target element not found in DOM → See teleport-target-must-exist
Teleported content breaks SSR hydration → See teleport-ssr-hydration
Scoped styles not applying to teleported content → See teleport-scoped-styles-limitation
Suspense
Need to handle async errors from Suspense components → See suspense-no-builtin-error-handling
Using Suspense with server-side rendering → See suspense-ssr-hydration-issues
Async component loading/error UI ignored under Suspense → See async-component-suspense-control
SSR
HTML differs between server and client renders → See ssr-hydration-mismatch-causes
User state leaks between requests from shared singleton stores → See state-ssr-cross-request-pollution
Browser-only APIs crash server rendering in universal code paths → See ssr-platform-specific-apis
Performance
List children re-render unnecessarily because parent passes unstable props → See perf-props-stability-update-optimization
Computed objects retrigger effects despite equivalent values → See perf-computed-object-stability
SFC (Single File Components)
Trying to use named exports from component script blocks → See sfc-named-exports-forbidden
Variables not updating in template after changes → See sfc-script-setup-reactivity
Scoped styles not applying to child component elements → See sfc-scoped-css-child-component-styling
Scoped styles not applying to dynamic v-html content → See sfc-scoped-css-dynamic-content
Scoped styles not applying to slot content → See sfc-scoped-css-slot-content
Tailwind classes missing when built dynamically → See tailwind-dynamic-class-generation
Recursive components not rendering due to name conflicts → See self-referencing-component-name
Plugins
Debugging why global properties cause naming conflicts → See plugin-global-properties-sparingly
Plugin not working or inject returns undefined → See plugin-install-before-mount
Plugin global properties are unavailable in setup-based components → See plugin-prefer-provide-inject-over-global-properties
Plugin type augmentation mistakes break ComponentCustomProperties typing → See plugin-typescript-type-augmentation
App Configuration
App configuration methods not working after mount call → See configure-app-before-mount
Chaining app config off mount() fails because mount returns component instance → See mount-return-value
require.context-based component auto-registration fails in Vite → See dynamic-component-registration-vite
Weekly Installs
12.9K
Repository
hyf0/vue-skills
GitHub Stars
2.3K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn