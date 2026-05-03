---
title: vueuse
url: https://skills.sh/onmax/nuxt-skills/vueuse
---

# vueuse

skills/onmax/nuxt-skills/vueuse
vueuse
Installation
$ npx skills add https://github.com/onmax/nuxt-skills --skill vueuse
Summary

Essential Vue Composition utilities for state, sensors, browser APIs, and common patterns.

200+ composables across 12 categories including state persistence, mouse tracking, keyboard input, network requests, animations, and array operations
Auto-imports in Nuxt via @vueuse/nuxt module; manual imports required for Vue 3 standalone
SSR-safe composables return sensible defaults on server; use isClient guard or onMounted wrapper for browser-only APIs
Common patterns include useLocalStorage for persistence, useMouse for position tracking, refDebounced for value debouncing, and createSharedComposable for singleton instances
SKILL.md
VueUse

Collection of essential Vue Composition utilities. Check VueUse before writing custom composables - most patterns already implemented.

Current stable: VueUse 14.x for Vue 3.5+

Installation

Vue 3:

pnpm add @vueuse/core


Nuxt:

pnpm add @vueuse/nuxt @vueuse/core

// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@vueuse/nuxt'],
})


Nuxt module auto-imports composables - no import needed.

Categories
Category	Examples
State	useLocalStorage, useSessionStorage, useRefHistory
Elements	useElementSize, useIntersectionObserver, useResizeObserver
Browser	useClipboard, useFullscreen, useMediaQuery
Sensors	useMouse, useKeyboard, useDeviceOrientation
Network	useFetch, useWebSocket, useEventSource
Animation	useTransition, useInterval, useTimeout
Component	useVModel, useVirtualList, useTemplateRefsList
Watch	watchDebounced, watchThrottled, watchOnce
Reactivity	createSharedComposable, toRef, toReactive
Array	useArrayFilter, useArrayMap, useSorted
Time	useDateFormat, useNow, useTimeAgo
Utilities	useDebounce, useThrottle, useMemoize
Quick Reference

Load composable files based on what you need:

Working on...	Load file
Finding a composable	references/composables.md
Specific composable	composables/<name>.md
Loading Files

Consider loading these reference files based on your task:

 references/composables.md - if searching for VueUse composables by category or functionality

DO NOT load all files at once. Load only what's relevant to your current task.

Common Patterns

State persistence:

const state = useLocalStorage('my-key', { count: 0 })


Mouse tracking:

const { x, y } = useMouse()


Debounced ref:

const search = ref('')
const debouncedSearch = refDebounced(search, 300)


Shared composable (singleton):

const useSharedMouse = createSharedComposable(useMouse)

SSR Gotchas

Many VueUse composables use browser APIs unavailable during SSR.

Check with isClient:

import { isClient } from '@vueuse/core'

if (isClient) {
  // Browser-only code
  const { width } = useWindowSize()
}


Wrap in onMounted:

const width = ref(0)

onMounted(() => {
  // Only runs in browser
  const { width: w } = useWindowSize()
  width.value = w.value
})


Use SSR-safe composables:

// These check isClient internally
const mouse = useMouse() // Returns {x: 0, y: 0} on server
const storage = useLocalStorage('key', 'default') // Uses default on server


@vueuse/nuxt auto-handles SSR - composables return safe defaults on server.

Target Element Refs

When targeting component refs instead of DOM elements:

import type { MaybeElementRef } from '@vueuse/core'

// Component ref needs .$el to get DOM element
const compRef = ref<ComponentInstance>()
const { width } = useElementSize(compRef) // ❌ Won't work

// Use MaybeElementRef pattern
import { unrefElement } from '@vueuse/core'

const el = computed(() => unrefElement(compRef)) // Gets .$el
const { width } = useElementSize(el) // ✅ Works


Or access $el directly:

const compRef = ref<ComponentInstance>()

onMounted(() => {
  const el = compRef.value?.$el as HTMLElement
  const { width } = useElementSize(el)
})

Weekly Installs
2.1K
Repository
onmax/nuxt-skills
GitHub Stars
649
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass