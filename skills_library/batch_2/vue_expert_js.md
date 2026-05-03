---
title: vue-expert-js
url: https://skills.sh/jeffallan/claude-skills/vue-expert-js
---

# vue-expert-js

skills/jeffallan/claude-skills/vue-expert-js
vue-expert-js
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill vue-expert-js
Summary

Vue 3 components and composables in JavaScript with comprehensive JSDoc type coverage, no TypeScript required.

Builds with <script setup> and .mjs modules using @typedef, @param, and @returns JSDoc annotations for full type safety without a TypeScript compiler
Covers component architecture (props, emits, slots), custom composables, Pinia state management, and Vue Router configuration entirely in vanilla JavaScript
Includes ESLint JSDoc plugin verification to ensure all public APIs have complete type annotations before testing
Supports migration from Vue 2 Options API to Composition API in JavaScript and rapid prototyping without TypeScript setup overhead
SKILL.md
Vue Expert (JavaScript)

Senior Vue specialist building Vue 3 applications with JavaScript and JSDoc typing instead of TypeScript.

Core Workflow
Design architecture — Plan component structure and composables with JSDoc type annotations
Implement — Build with <script setup> (no lang="ts"), .mjs modules where needed
Annotate — Add comprehensive JSDoc comments (@typedef, @param, @returns, @type) for full type coverage; then run ESLint with the JSDoc plugin (eslint-plugin-jsdoc) to verify coverage — fix any missing or malformed annotations before proceeding
Test — Verify with Vitest using JavaScript files; confirm JSDoc coverage on all public APIs; if tests fail, revisit the relevant composable or component, correct the logic or annotation, and re-run until the suite is green
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
JSDoc Typing	references/jsdoc-typing.md	JSDoc types, @typedef, @param, type hints
Composables	references/composables-patterns.md	custom composables, ref, reactive, lifecycle hooks
Components	references/component-architecture.md	props, emits, slots, provide/inject
State	references/state-management.md	Pinia, stores, reactive state
Testing	references/testing-patterns.md	Vitest, component testing, mocking

For shared Vue concepts, defer to vue-expert:

vue-expert/references/composition-api.md - Core reactivity patterns
vue-expert/references/components.md - Props, emits, slots
vue-expert/references/state-management.md - Pinia stores
Code Patterns
Component with JSDoc-typed props and emits
<script setup>
/**
 * @typedef {Object} UserCardProps
 * @property {string} name - Display name of the user
 * @property {number} age - User's age
 * @property {boolean} [isAdmin=false] - Whether the user has admin rights
 */

/** @type {UserCardProps} */
const props = defineProps({
  name:    { type: String,  required: true },
  age:     { type: Number,  required: true },
  isAdmin: { type: Boolean, default: false },
})

/**
 * @typedef {Object} UserCardEmits
 * @property {(id: string) => void} select - Emitted when the card is selected
 */
const emit = defineEmits(['select'])

/** @param {string} id */
function handleSelect(id) {
  emit('select', id)
}
</script>

<template>
  <div @click="handleSelect(props.name)">
    {{ props.name }} ({{ props.age }})
  </div>
</template>

Composable with @typedef, @param, and @returns
// composables/useCounter.mjs
import { ref, computed } from 'vue'

/**
 * @typedef {Object} CounterState
 * @property {import('vue').Ref<number>} count - Reactive count value
 * @property {import('vue').ComputedRef<boolean>} isPositive - True when count > 0
 * @property {() => void} increment - Increases count by step
 * @property {() => void} reset - Resets count to initial value
 */

/**
 * Composable for a simple counter with configurable step.
 * @param {number} [initial=0] - Starting value
 * @param {number} [step=1]    - Amount to increment per call
 * @returns {CounterState}
 */
export function useCounter(initial = 0, step = 1) {
  /** @type {import('vue').Ref<number>} */
  const count = ref(initial)

  const isPositive = computed(() => count.value > 0)

  function increment() {
    count.value += step
  }

  function reset() {
    count.value = initial
  }

  return { count, isPositive, increment, reset }
}

@typedef for a complex object used across files
// types/user.mjs

/**
 * @typedef {Object} User
 * @property {string}   id       - UUID
 * @property {string}   name     - Full display name
 * @property {string}   email    - Contact email
 * @property {'admin'|'viewer'} role - Access level
 */

// Import in other files with:
// /** @type {import('./types/user.mjs').User} */

Constraints
MUST DO
Use Composition API with <script setup>
Use JSDoc comments for type documentation
Use .mjs extension for ES modules when needed
Annotate every public function with @param and @returns
Use @typedef for complex object shapes shared across files
Use @type annotations for reactive variables
Follow vue-expert patterns adapted for JavaScript
MUST NOT DO
Use TypeScript syntax (no <script setup lang="ts">)
Use .ts file extensions
Skip JSDoc types for public APIs
Use CommonJS require() in Vue files
Ignore type safety entirely
Mix TypeScript files with JavaScript in the same component
Output Templates

When implementing Vue features in JavaScript:

Component file with <script setup> (no lang attribute) and JSDoc-typed props/emits
@typedef definitions for complex prop or state shapes
Composable with @param and @returns annotations
Brief note on type coverage
Knowledge Reference

Vue 3 Composition API, JSDoc, ESM modules, Pinia, Vue Router 4, Vite, VueUse, Vitest, Vue Test Utils, JavaScript ES2022+

Documentation

Weekly Installs
1.5K
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