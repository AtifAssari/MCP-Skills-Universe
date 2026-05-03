---
title: vue-best-practices
url: https://skills.sh/vuejs-ai/skills/vue-best-practices
---

# vue-best-practices

skills/vuejs-ai/skills/vue-best-practices
vue-best-practices
Originally fromhyf0/vue-skills
Installation
$ npx skills add https://github.com/vuejs-ai/skills --skill vue-best-practices
Summary

Standard Vue 3 workflow with Composition API, <script setup>, and TypeScript as the default approach.

Requires confirming project architecture upfront and reading core references on reactivity, SFCs, component data flow, and composables before implementation
Enforces minimal source state with ref/reactive, deriving everything possible with computed, and keeping templates declarative
Mandates component splitting when responsibilities exceed one clear purpose, with entry/root and route views kept as thin composition surfaces
Covers optional features (slots, transitions, async components, state management) only when requirements explicitly call for them
Includes a post-functionality performance optimization pass for large lists, static subtrees, and over-abstraction in hot paths
SKILL.md
Vue Best Practices Workflow

Use this skill as an instruction set. Follow the workflow in order unless the user explicitly asks for a different order.

Core Principles
Keep state predictable: one source of truth, derive everything else.
Make data flow explicit: Props down, Events up for most cases.
Favor small, focused components: easier to test, reuse, and maintain.
Avoid unnecessary re-renders: use computed properties and watchers wisely.
Readability counts: write clear, self-documenting code.
1) Confirm architecture before coding (required)
Default stack: Vue 3 + Composition API + <script setup lang="ts">.
If the project explicitly uses Options API, load vue-options-api-best-practices skill if available.
If the project explicitly uses JSX, load vue-jsx-best-practices skill if available.
1.1 Must-read core references (required)
Before implementing any Vue task, make sure to read and apply these core references:
references/reactivity.md
references/sfc.md
references/component-data-flow.md
references/composables.md
Keep these references in active working context for the entire task, not only when a specific issue appears.
1.2 Plan component boundaries before coding (required)

Create a brief component map before implementation for any non-trivial feature.

Define each component's single responsibility in one sentence.
Keep entry/root and route-level view components as composition surfaces by default.
Move feature UI and feature logic out of entry/root/view components unless the task is intentionally a tiny single-file demo.
Define props/emits contracts for each child component in the map.
Prefer a feature folder layout (components/<feature>/..., composables/use<Feature>.ts) when adding more than one component.
2) Apply essential Vue foundations (required)

These are essential, must-know foundations. Apply all of them in every Vue task using the core references already loaded in section 1.1.

Reactivity
Must-read reference from 1.1: reactivity
Keep source state minimal (ref/reactive), derive everything possible with computed.
Use watchers for side effects if needed.
Avoid recomputing expensive logic in templates.
SFC structure and template safety
Must-read reference from 1.1: sfc
Keep SFC sections in this order: <script> → <template> → <style>.
Keep SFC responsibilities focused; split large components.
Keep templates declarative; move branching/derivation to script.
Apply Vue template safety rules (v-html, list rendering, conditional rendering choices).
Keep components focused

Split a component when it has more than one clear responsibility (e.g. data orchestration + UI, or multiple independent UI sections).

Prefer smaller components + composables over one “mega component”
Move UI sections into child components (props in, events out).
Move state/side effects into composables (useXxx()).

Apply objective split triggers. Split the component if any condition is true:

It owns both orchestration/state and substantial presentational markup for multiple sections.
It has 3+ distinct UI sections (for example: form, filters, list, footer/status).
A template block is repeated or could become reusable (item rows, cards, list entries).

Entry/root and route view rule:

Keep entry/root and route view components thin: app shell/layout, provider wiring, and feature composition.
Do not place full feature implementations in entry/root/view components when those features contain independent parts.
For CRUD/list features (todo, table, catalog, inbox), split at least into:
feature container component
input/form component
list (and/or item) component
footer/actions or filter/status component
Allow a single-file implementation only for very small throwaway demos; if chosen, explicitly justify why splitting is unnecessary.
Component data flow
Must-read reference from 1.1: component-data-flow
Use props down, events up as the primary model.
Use v-model only for true two-way component contracts.
Use provide/inject only for deep-tree dependencies or shared context.
Keep contracts explicit and typed with defineProps, defineEmits, and InjectionKey as needed.
Composables
Must-read reference from 1.1: composables
Extract logic into composables when it is reused, stateful, or side-effect heavy.
Keep composable APIs small, typed, and predictable.
Separate feature logic from presentational components.
3) Consider optional features only when requirements call for them
3.1 Standard optional features

Do not add these by default. Load the matching reference only when the requirement exists.

Slots: parent needs to control child content/layout -> component-slots
Fallthrough attributes: wrapper/base components must forward attrs/events safely -> component-fallthrough-attrs
Built-in component <KeepAlive> for stateful view caching -> component-keep-alive
Built-in component <Teleport> for overlays/portals -> component-teleport
Built-in component <Suspense> for async subtree fallback boundaries -> component-suspense
Animation-related features: pick the simplest approach that matches the required motion behavior.
Built-in component <Transition> for enter/leave effects -> transition
Built-in component <TransitionGroup> for animated list mutations -> transition-group
Class-based animation for non-enter/leave effects -> animation-class-based-technique
State-driven animation for user-input-driven animation -> animation-state-driven-technique
3.2 Less-common optional features

Use these only when there is explicit product or technical need.

Directives: behavior is DOM-specific and not a good composable/component fit -> directives
Async components: heavy/rarely-used UI should be lazy loaded -> component-async
Render functions only when templates cannot express the requirement -> render-functions
Plugins when behavior must be installed app-wide -> plugins
State management patterns: app-wide shared state crosses feature boundaries -> state-management
4) Run performance optimization after behavior is correct

Performance work is a post-functionality pass. Do not optimize before core behavior is implemented and verified.

Large list rendering bottlenecks -> perf-virtualize-large-lists
Static subtrees re-rendering unnecessarily -> perf-v-once-v-memo-directives
Over-abstraction in hot list paths -> perf-avoid-component-abstraction-in-lists
Expensive updates triggered too often -> updated-hook-performance
5) Final self-check before finishing
Core behavior works and matches requirements.
All must-read references were read and applied.
Reactivity model is minimal and predictable.
SFC structure and template rules are followed.
Components are focused and well-factored, splitting when needed.
Entry/root and route view components remain composition surfaces unless there is an explicit small-demo exception.
Component split decisions are explicit and defensible (responsibility boundaries are clear).
Data flow contracts are explicit and typed.
Composables are used where reuse/complexity justifies them.
Moved state/side effects into composables if applicable
Optional features are used only when requirements demand them.
Performance changes were applied only after functionality was complete.
Weekly Installs
6.7K
Repository
vuejs-ai/skills
GitHub Stars
2.3K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass