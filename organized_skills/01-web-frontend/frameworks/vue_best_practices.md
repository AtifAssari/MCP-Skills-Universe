---
rating: ⭐⭐
title: vue-best-practices
url: https://skills.sh/uni-helper/skills/vue-best-practices
---

# vue-best-practices

skills/uni-helper/skills/vue-best-practices
vue-best-practices
Installation
$ npx skills add https://github.com/uni-helper/skills --skill vue-best-practices
SKILL.md

Vue 3 best practices, common gotchas, and performance optimization.

Reactivity
Accessing ref() values without .value in scripts → See ref-value-access
Destructuring reactive() objects, losing reactivity → See reactive-destructuring
Choosing between ref() and reactive() for state → See prefer-ref-over-reactive
Accessing refs inside arrays and collections → See refs-in-collections-need-value
Large objects or external library data overhead → See shallow-ref-for-performance
Using nested refs in template expressions → See template-ref-unwrapping-top-level
Comparing reactive objects with === operator → See reactivity-proxy-identity-hazard
Library instances breaking in reactive state → See reactivity-markraw-for-non-reactive
Expecting watchers to fire for each state change → See reactivity-same-tick-batching
Integrating external state management libraries → See reactivity-external-state-integration
Tracing unexpected re-renders and state updates → See reactivity-debugging-hooks
Deriving state with watchEffect instead of computed → See reactivity-computed-over-watcheffect-mutations
Computed
Computed getter is making API calls or mutations → See computed-no-side-effects
Mutating computed values causes lost changes unexpectedly → See computed-return-value-readonly
Computed property doesn't update when expected → See computed-conditional-dependencies
Sorting or reversing arrays destroys original data → See computed-array-mutation
Expensive operations running too frequently every render → See computed-vs-methods-caching
Trying to pass arguments to computed properties → See computed-no-parameters
Complex conditions bloating inline class bindings → See computed-properties-for-class-logic
Watchers
Need to watch a reactive object property → See watch-reactive-property-getter
Large nested data structures causing performance issues → See watch-deep-performance
Async operations overwriting with stale data → See watch-async-cleanup
Creating watchers inside async callbacks → See watch-async-creation-memory-leak
Dependencies accessed after await not tracking → See watcheffect-async-dependency-tracking
Need to access updated DOM in watchers → See watch-flush-timing
Uncertain whether to use watch or watchEffect → See watch-vs-watcheffect
Duplicating initial calls and watch callbacks → See watch-immediate-option
Can't compare old and new values correctly → See watch-deep-same-object-reference
Template refs appearing null or stale → See watcheffect-flush-post-for-refs
Components
Prop values being changed from a child component → See props-are-read-only
Parent can't access child ref data in script setup → See component-ref-requires-defineexpose
Child component throws "component not found" error → See local-components-not-in-descendants
Click listener doesn't fire on custom component → See click-events-on-components
HTML template parsing breaks Vue component syntax → See in-dom-template-parsing-caveats
Grandparent can't listen to grandchild emitted events → See component-events-dont-bubble
Wrong component renders due to naming collisions → See component-naming-conflicts
Distinguishing Vue components from native elements → See component-naming-pascalcase
Parent styles don't apply to multi-root component → See multi-root-component-class-attrs
Recursive component needs to reference itself → See self-referencing-component-name
Bundle includes components that aren't used → See prefer-local-component-registration
Tight coupling through component ref access → See prefer-props-emit-over-component-refs
Props & Emits
Boolean prop not parsing as expected → See prop-boolean-casting-order
Composable doesn't update when props change → See prop-composable-reactivity-loss
Variables referenced in defineProps cause errors → See prop-defineprops-scope-limitation
Destructured props not updating watchers → See prop-destructured-watch-getter
Prop validation needs component instance data → See prop-validation-before-instance
Component emits undeclared event causing warnings → See declare-emits-for-documentation
defineEmits used inside function or conditional → See defineEmits-must-be-top-level
defineEmits has both type and runtime arguments → See defineEmits-no-runtime-and-type-mixed
Event name inconsistency in templates and scripts → See emit-kebab-case-in-templates
Event payloads need validation during development → See emit-validation-for-complex-payloads
Native event listeners not responding to clicks → See native-event-collision-with-emits
Component event fires twice when clicking → See undeclared-emits-double-firing
Templates
Rendering untrusted user content as HTML → See v-html-xss-security
Filtering or conditionally hiding list items → See no-v-if-with-v-for
List items disappearing or swapping state unexpectedly → See v-for-key-attribute
Getting template compilation errors with statements → See template-expressions-restrictions
Dynamic directive arguments not working properly → See dynamic-argument-constraints
Functions in templates modifying data unexpectedly → See template-functions-no-side-effects
v-else elements rendering unconditionally always → See v-else-must-follow-v-if
Child components in loops showing undefined data → See v-for-component-props
Array order changing after sorting or reversing → See v-for-computed-reverse-sort
Getting off-by-one errors with range iteration → See v-for-range-starts-at-one
Performance issues with filtered or sorted lists → See v-for-use-computed-for-filtering
"Cannot read property of undefined" runtime errors → See v-if-null-check-order
Deciding between v-if and v-show for conditionals → See v-if-vs-v-show-performance
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
Need to handle v-model modifiers in child → See definemodel-hidden-modifier-props
Object property changes not syncing to parent → See definemodel-object-mutation-no-emit
Need to use updated value immediately after change → See definemodel-value-next-tick
Real-time search/validation broken for Chinese/Japanese input → See v-model-ime-composition
Number input returns empty string instead of zero → See v-model-number-modifier-behavior
Migrating Vue 2 components to Vue 3 → See v-model-vue3-breaking-changes
Custom checkbox values not submitted in forms → See checkbox-true-false-value-form-submission
Events & Modifiers
Chaining multiple event modifiers produces unexpected results → See event-modifier-order-matters
Need to handle same event only one time → See event-once-modifier-for-single-use
Keyboard shortcuts fire with unintended modifier combinations → See exact-modifier-for-precise-shortcuts
Keyboard shortcuts don't fire with system modifier keys → See keyup-modifier-timing
Using left-handed mouse or non-standard input devices → See mouse-button-modifiers-intent
Preventing default browser action and scroll performance together → See no-passive-with-prevent
Lifecycle
Lifecycle hooks don't execute asynchronously → See lifecycle-hooks-synchronous-registration
DOM access fails before component mounts → See lifecycle-dom-access-timing
Memory leaks from unremoved event listeners → See cleanup-side-effects
SSR rendering differs from client hydration → See lifecycle-ssr-awareness
Expensive operations slow performance drastically → See updated-hook-performance
DOM reads return stale values after state changes → See dom-update-timing-nexttick
Slots
Accessing child component data in slot content → See slot-render-scope-parent-only
Mixing named and scoped slots together → See slot-named-scoped-explicit-default
Using v-slot on native HTML elements → See slot-v-slot-on-components-or-templates-only
Empty wrapper elements rendering unnecessarily → See slot-conditional-rendering-with-slots
Scoped slot props lack TypeScript type safety → See slot-define-slots-for-typescript
Rendering empty component slots without defaults → See slot-fallback-content-default-values
Wrapper components breaking child slot functionality → See slot-forwarding-to-child-components
Confused about which slot content goes where → See slot-implicit-default-content
Expecting name property in scoped slot props → See slot-name-reserved-prop
Choosing between renderless components and composables → See slot-renderless-components-vs-composables
Provide/Inject
Injected values not updating when provider changes → See provide-inject-reactivity-not-automatic
Calling provide after async operations fails silently → See provide-inject-synchronous-setup
String keys collide in large applications → See provide-inject-symbol-keys
Tracing where provided values come from → See provide-inject-debugging-challenges
Multiple components share same default object → See provide-inject-default-value-factory
State mutations scattered across components → See provide-inject-mutations-in-provider
Passing props through many component layers → See avoid-prop-drilling-use-provide-inject
Attrs
Both internal and fallthrough event handlers execute → See attrs-event-listener-merging
Accessing hyphenated attributes in JavaScript code → See attrs-hyphenated-property-access
Watching fallthrough attributes for changes with watch() → See attrs-not-reactive
Explicit attributes overwritten by fallthrough values → See fallthrough-attrs-overwrite-vue3
Attributes applying to wrong element in wrappers → See inheritattrs-false-for-wrapper-components
Composables
Composable has unexpected side effects affecting external state → See composable-avoid-hidden-side-effects
Composable called outside setup context or asynchronously → See composable-call-location-restrictions
Building complex logic from smaller focused composables → See composable-composition-pattern
Inconsistent composable names or destructuring loses reactivity → See composable-naming-return-pattern
Composable has many optional parameters or confusing argument order → See composable-options-object-pattern
Need to prevent uncontrolled mutations of composable state → See composable-readonly-state
Composable reactive dependency not updating when input changes → See composable-tovalue-inside-watcheffect
Unsure whether logic belongs in composable or utility function → See composable-vs-utility-functions
Composition API
Optimizing production bundle size and performance → See composition-api-bundle-size-minification
Composition API code becoming scattered and hard to maintain → See composition-api-code-organization
Fixing naming conflicts and unclear data origins in mixins → See composition-api-mixins-replacement
Applying functional patterns incorrectly to Vue state → See composition-api-not-functional-programming
Gradually migrating large Options API codebase → See composition-api-options-api-coexistence
Lifecycle hooks failing silently after async operations → See composition-api-script-setup-async-context
Coming from React, over-engineering Vue patterns unnecessarily → See composition-api-vs-react-hooks-differences
Parent component refs unable to access exposed properties → See define-expose-before-await
Directives
Storing state across directive hooks → See directive-arguments-read-only
Applying custom directives to Vue components → See directive-avoid-on-components
Creating intervals or event listeners in directives → See directive-cleanup-in-unmounted
Simplifying directives with identical behavior → See directive-function-shorthand
Using custom directives in script setup → See directive-naming-v-prefix
Choosing between custom and built-in directives → See directive-prefer-declarative-templating
Deciding between directives and components → See directive-vs-component-decision
Migrating Vue 2 directives to Vue 3 → See directive-vue2-migration-hooks
Transitions
Wrapping multiple elements or components in transitions → See transition-single-element-slot
Transitioning between same element types without animation → See transition-key-for-same-element
Using JavaScript animations without calling done callback → See transition-js-hooks-done-callback
Animating lists with TransitionGroup without unique keys → See transition-group-key-requirement
Performance problems with janky list animations → See transition-animate-transform-opacity
Move animations failing on inline list elements → See transition-group-flip-inline-elements
List items jumping instead of smoothly animating → See transition-group-move-animation-position-absolute
Vue 2 to Vue 3 transition layout breaks unexpectedly → See transition-group-no-default-wrapper-vue3
Trying to sequence list animations with mode prop → See transition-group-no-mode-prop
Creating cascading delays for list item animations → See transition-group-staggered-animations
Overlapping elements or layout jumping during transitions → See transition-mode-out-in
Nested transition animations cutting off prematurely → See transition-nested-duration
Reusable transition components with scoped styles breaking → See transition-reusable-scoped-style
RouterView transitions unexpectedly animating on page load → See transition-router-view-appear
Mixing CSS transitions and animations causing timing issues → See transition-type-when-mixed
Component cleanup not firing during fast transition replacements → See transition-unmount-hook-timing
Animation
Need to animate elements staying in DOM → See animation-class-based-technique
Animations not triggering on content changes → See animation-key-for-rerender
Building interactive animations with user input → See animation-state-driven-technique
Animating list changes causing noticeable lag → See animation-transitiongroup-performance
KeepAlive
Using KeepAlive without proper cache limits or cleanup → See keepalive-memory-management
KeepAlive include/exclude props not matching cached components → See keepalive-component-name-requirement
Need to programmatically remove component from KeepAlive cache → See keepalive-no-cache-removal-vue3
Users see stale cached content when expecting fresh page data → See keepalive-router-fresh-vs-cached
Child components mount twice with nested Vue Router routes → See keepalive-router-nested-double-mount
Memory grows when combining KeepAlive with Transition animations → See keepalive-transition-memory-leak
Dynamic component state resets when switching between them → See dynamic-components-with-keepalive
Async Components
Setting up Vue Router route component loading → See async-component-vue-router
Async component options ignored by parent Suspense → See async-component-suspense-control
Network failures or timeouts loading components → See async-component-error-handling
Improving Time to Interactive with SSR apps → See async-component-hydration-strategies
Template refs undefined after component reactivation → See async-component-keepalive-ref-issue
Loading spinner flashing on fast networks → See async-component-loading-delay
Render Functions
Render function from setup doesn't update reactively → See rendering-render-function-return-from-setup
Same vnode appearing multiple times in tree → See render-function-vnodes-must-be-unique
Rendering lists in render functions without keys → See render-function-v-for-keys-required
Implementing .stop, .prevent in render functions → See render-function-event-modifiers
Two-way binding on components in render functions → See render-function-v-model-implementation
Using string names for components in render functions → See rendering-resolve-component-for-string-names
Accessing vnode internals like el or shapeFlag → See render-function-avoid-internal-vnode-properties
Creating simple stateless presentational components → See render-function-functional-components
Applying custom directives in render functions → See render-function-custom-directives
Excessive rerenders from watchers or deep watchers → See rendering-excessive-rerenders-watch-vs-computed
Choosing render functions over templates → See rendering-prefer-templates-over-render-functions
Migrating Vue 2 render functions to Vue 3 → See rendering-render-function-h-import-vue3
Passing slot content to h() incorrectly → See rendering-render-function-slots-as-functions
Understanding Vue's vdom optimization blocks → See rendering-understand-vdom-block-structure
Teleport
Teleport target element not found in DOM → See teleport-target-must-exist
Teleported content breaks SSR hydration → See teleport-ssr-hydration
Modal breaks with parent CSS transforms → See teleport-css-positioning-issues
Content needs different layout on mobile → See teleport-disabled-for-responsive
Unsure if props/events work through teleport → See teleport-logical-hierarchy-preserved
Multiple modals targeting same container → See teleport-multiple-to-same-target
Scoped styles not applying to teleported content → See teleport-scoped-styles-limitation
Suspense
Need to handle async errors from Suspense components → See suspense-no-builtin-error-handling
Want to track Suspense loading states programmatically → See suspense-events-for-state-tracking
Planning Suspense usage in production applications → See suspense-experimental-api-stability
Fallback not showing when content changes → See suspense-fallback-not-immediate-on-revert
Nesting Suspense components together → See suspense-nested-suspensible-prop
Combining Suspense with Router, Transition, KeepAlive → See suspense-nesting-order-with-router
Nested async component not showing loading indicator → See suspense-revert-only-on-root-change
Multiple async components in single Suspense → See suspense-single-child-requirement
Using Suspense with server-side rendering → See suspense-ssr-hydration-issues
TypeScript
Declaring props with TypeScript in composition API components → See ts-defineprops-type-based-declaration
Providing default values to mutable prop types → See ts-withdefaults-mutable-factory-function
Typing reactive state with ref unwrapping concerns → See ts-reactive-no-generic-argument
Accessing DOM elements after component mounts → See ts-template-ref-null-handling
Typing refs to child Vue components → See ts-component-ref-typeof-instancetype
Using custom directives with TypeScript support → See ts-custom-directive-type-augmentation
Declaring component events with full type safety → See ts-defineemits-type-based-syntax
Handling optional boolean props in TypeScript → See ts-defineprops-boolean-default-false
Using imported types safely in defineProps → See ts-defineprops-imported-types-limitations
Handling DOM events with strict TypeScript checking → See ts-event-handler-explicit-typing
Sharing data between components with type safety → See ts-provide-inject-injection-key
Storing Vue components in reactive state → See ts-shallowref-for-dynamic-components
Working with union types in Vue templates → See ts-template-type-casting
SSR
User data leaking between server requests → See state-ssr-cross-request-pollution
HTML differs between server and client renders → See ssr-hydration-mismatch-causes
Code runs on both server and browser environments → See ssr-platform-specific-apis
Custom directives not displaying on server-rendered HTML → See ssr-custom-directive-getssrprops
Performance
Many list items re-rendering unnecessarily during state changes → See perf-props-stability-update-optimization
Rendering hundreds or thousands of items causing DOM performance issues → See perf-virtualize-large-lists
Static content re-evaluated on every parent component update → See perf-v-once-v-memo-directives
List performance degrading from deeply nested component structure → See perf-avoid-component-abstraction-in-lists
Computed properties returning objects triggering effects unexpectedly → See perf-computed-object-stability
Page load metrics suffering from client-side JavaScript execution delay → See perf-ssr-ssg-for-page-load
SFC (Single File Components)
Trying to use named exports from component script blocks → See sfc-named-exports-forbidden
Starting a Vue project with a build setup → See sfc-recommended-for-build-projects
Styling child component elements with scoped CSS → See sfc-scoped-css-child-component-styling
Styling content added dynamically with v-html → See sfc-scoped-css-dynamic-content
Optimizing scoped CSS selector performance → See sfc-scoped-css-performance
Styling content passed through component slots → See sfc-scoped-css-slot-content
Variables not updating in template after changes → See sfc-script-setup-reactivity
Organizing component template, logic, and styles → See sfc-separation-of-concerns-colocate
Binding inline styles with property names → See style-binding-camelcase
Building Tailwind classes with string concatenation → See tailwind-dynamic-class-generation
Plugins
Debugging why global properties cause naming conflicts → See plugin-global-properties-sparingly
Plugin not working or inject returns undefined → See plugin-install-before-mount
Global properties not available in setup function → See plugin-prefer-provide-inject-over-global-properties
Creating a new Vue plugin from scratch → See plugin-structure-install-method
Preventing collisions between multiple plugins → See plugin-symbol-injection-keys
Global properties missing TypeScript autocomplete support → See plugin-typescript-type-augmentation
App Configuration
App configuration methods not working after mount call → See configure-app-before-mount
Need to chain app configuration methods after mount → See mount-return-value
Vue only controlling specific page sections → See multiple-app-instances
Migrating dynamic component registration to Vite → See dynamic-component-registration-vite
Weekly Installs
364
Repository
uni-helper/skills
GitHub Stars
58
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn