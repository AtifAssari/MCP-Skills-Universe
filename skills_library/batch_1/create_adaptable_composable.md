---
title: create-adaptable-composable
url: https://skills.sh/vuejs-ai/skills/create-adaptable-composable
---

# create-adaptable-composable

skills/vuejs-ai/skills/create-adaptable-composable
create-adaptable-composable
Installation
$ npx skills add https://github.com/vuejs-ai/skills --skill create-adaptable-composable
Summary

Library-grade Vue composables that accept plain values, refs, or getters as inputs.

Use MaybeRefOrGetter for read-only inputs (computed-friendly) and MaybeRef for writable two-way inputs; normalize with toValue() or toRef() inside reactive effects
Normalize inputs using toRef() for watcher sources and toValue() for non-reactive resolution to keep behavior predictable across different input types
Avoid MaybeRefOrGetter when parameters are callbacks, predicates, or comparators to prevent accidental function invocation as getters
Requires Vue 3+ or Nuxt 3+
SKILL.md
Create Adaptable Composable

Adaptable composables are reusable functions that can accept both reactive and non-reactive inputs. This allows developers to use the composable in a variety of contexts without worrying about the reactivity of the inputs.

Steps to design an adaptable composable in Vue.js:

Confirm the composable's purpose and API design and expected inputs/outputs.
Identify inputs params that should be reactive (MaybeRef / MaybeRefOrGetter).
Use toValue() or toRef() to normalize inputs inside reactive effects.
Implement the core logic of the composable using Vue's reactivity APIs.
Core Type Concepts
Type Utilities
/**
 * value or writable ref (value/ref/shallowRef/writable computed)
 */
export type MaybeRef<T = any> = T | Ref<T> | ShallowRef<T> | WritableComputedRef<T>;

/**
 * MaybeRef<T> + ComputedRef<T> + () => T
 */
export type MaybeRefOrGetter<T = any> = MaybeRef<T> | ComputedRef<T> | (() => T);

Policy and Rules
Read-only, computed-friendly input: use MaybeRefOrGetter
Needs to be writable / two-way input: use MaybeRef
Parameter might be a function value (callback/predicate/comparator): do not use MaybeRefOrGetter, or you may accidentally invoke it as a getter.
DOM/Element targets: if you want computed/derived targets, use MaybeRefOrGetter.

When MaybeRefOrGetter or MaybeRef is used:

resolve reactive value using toRef() (e.g. watcher source)
resolve non-reactive value using toValue()
Examples

Adaptable useDocumentTitle Composable: read-only title parameter

import { watch, toRef } from 'vue'
import type { MaybeRefOrGetter } from 'vue'

export function useDocumentTitle(title: MaybeRefOrGetter<string>) {
  watch(toRef(title), (t) => {
    document.title = t
  }, { immediate: true })
}


Adaptable useCounter Composable: two-way writable count parameter

import { watch, toRef } from 'vue'
import type { MaybeRef } from 'vue'

function useCounter(count: MaybeRef<number>) {
  const countRef = toRef(count)
  function add() {
    countRef.value++
  }
  return { add }
}

Weekly Installs
5.6K
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