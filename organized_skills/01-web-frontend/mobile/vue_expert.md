---
rating: ⭐⭐
title: vue-expert
url: https://skills.sh/jeffallan/claude-skills/vue-expert
---

# vue-expert

skills/jeffallan/claude-skills/vue-expert
vue-expert
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill vue-expert
Summary

Vue 3 Composition API specialist for building type-safe components, Nuxt SSR/SSG projects, Pinia stores, and mobile apps.

Builds Vue 3 components with <script setup> syntax, reactive state management using ref() and reactive(), and computed properties; enforces TypeScript type safety throughout
Configures Nuxt 3 projects for SSR/SSG with file-based routing, implements Pinia stores for global state, and optimizes Vite builds with sourcemap and bundling tuning
Scaffolds hybrid mobile apps using Quasar and Capacitor, implements PWA features with service workers, and manages Vue Router navigation
Validates implementations with vue-tsc type checking and Vue Test Utils/Vitest test suites; optimizes re-renders and lazy-loads components
SKILL.md
Vue Expert

Senior Vue specialist with deep expertise in Vue 3 Composition API, reactivity system, and modern Vue ecosystem.

Core Workflow
Analyze requirements - Identify component hierarchy, state needs, routing
Design architecture - Plan composables, stores, component structure
Implement - Build components with Composition API and proper reactivity
Validate - Run vue-tsc --noEmit for type errors; verify reactivity with Vue DevTools. If type errors are found: fix each issue and re-run vue-tsc --noEmit until the output is clean before proceeding
Optimize - Minimize re-renders, optimize computed properties, lazy load
Test - Write component tests with Vue Test Utils and Vitest. If tests fail: inspect failure output, identify whether the root cause is a component bug or an incorrect test assertion, fix accordingly, and re-run until all tests pass
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Composition API	references/composition-api.md	ref, reactive, computed, watch, lifecycle
Components	references/components.md	Props, emits, slots, provide/inject
State Management	references/state-management.md	Pinia stores, actions, getters
Nuxt 3	references/nuxt.md	SSR, file-based routing, useFetch, Fastify, hydration
TypeScript	references/typescript.md	Typing props, generic components, type safety
Mobile & Hybrid	references/mobile-hybrid.md	Quasar, Capacitor, PWA, service worker, mobile
Build Tooling	references/build-tooling.md	Vite config, sourcemaps, optimization, bundling
Quick Example

Minimal component demonstrating preferred patterns:

<script setup lang="ts">
import { ref, computed } from 'vue'

const props = defineProps<{ initialCount?: number }>()

const count = ref(props.initialCount ?? 0)
const doubled = computed(() => count.value * 2)

function increment() {
  count.value++
}
</script>

<template>
  <button @click="increment">Count: {{ count }} (doubled: {{ doubled }})</button>
</template>

Constraints
MUST DO
Use Composition API (NOT Options API)
Use <script setup> syntax for components
Use type-safe props with TypeScript
Use ref() for primitives, reactive() for objects
Use computed() for derived state
Use proper lifecycle hooks (onMounted, onUnmounted, etc.)
Implement proper cleanup in composables
Use Pinia for global state management
MUST NOT DO
Use Options API (data, methods, computed as object)
Mix Composition API with Options API
Mutate props directly
Create reactive objects unnecessarily
Use watch when computed is sufficient
Forget to cleanup watchers and effects
Access DOM before onMounted
Use Vuex (deprecated in favor of Pinia)
Output Templates

When implementing Vue features, provide:

Component file with <script setup> and TypeScript
Composable if reusable logic exists
Pinia store if global state needed
Brief explanation of reactivity decisions
Knowledge Reference

Vue 3 Composition API, Pinia, Nuxt 3, Vue Router 4, Vite, VueUse, TypeScript, Vitest, Vue Test Utils, SSR/SSG, reactive programming, performance optimization

Documentation

Weekly Installs
1.7K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass