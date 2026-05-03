---
title: vue
url: https://skills.sh/uni-helper/skills/vue
---

# vue

skills/uni-helper/skills/vue
vue
Installation
$ npx skills add https://github.com/uni-helper/skills --skill vue
SKILL.md
Vue

The skill is based on Vue 3.5+, generated at 2026-01-28.

Vue is a progressive JavaScript framework for building user interfaces. It builds on standard HTML, CSS, and JavaScript with intuitive API and world-class documentation. The Composition API with <script setup> and TypeScript is the recommended approach for building Vue applications.

Core References
Topic	Description	Reference
Reactivity System	ref, reactive, computed, watch, and watchEffect	core-reactivity
Components
Topic	Description	Reference
Props	Declare and validate component props with TypeScript	components-props
Events (Emits)	Emit custom events from components	components-emits
Slots	Pass template content to child components	components-slots
v-model	Two-way binding on custom components	components-v-model
Lifecycle Hooks	Run code at specific component lifecycle stages	components-lifecycle
Features
Script Setup & TypeScript
Topic	Description	Reference
Script Setup	Composition API syntactic sugar for SFCs	features-script-setup
TypeScript	Type-safe Vue components with Composition API	features-typescript
Reusability
Topic	Description	Reference
Composables	Encapsulate and reuse stateful logic	features-composables
Custom Directives	Low-level DOM manipulation directives	features-directives
Template Refs	Direct DOM and component instance access	features-template-refs
Advanced
Topic	Description	Reference
Provide/Inject	Dependency injection across component tree	advanced-provide-inject
Async & Suspense	Top-level await pitfalls, async components, Suspense	advanced-async-suspense
Key Recommendations
Use <script setup lang="ts"> for all components
Prefer ref() over reactive() for declaring state
Use type-based prop declarations with interfaces
Use defineModel() for v-model (3.4+)
Destructure props reactively (3.5+) for cleaner code
Extract composables for reusable stateful logic
Weekly Installs
345
Repository
uni-helper/skills
GitHub Stars
58
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass