---
title: vueuse-integrations-skilld
url: https://skills.sh/harlan-zw/vue-ecosystem-skills/vueuse-integrations-skilld
---

# vueuse-integrations-skilld

skills/harlan-zw/vue-ecosystem-skills/vueuse-integrations-skilld
vueuse-integrations-skilld
Installation
$ npx skills add https://github.com/harlan-zw/vue-ecosystem-skills --skill vueuse-integrations-skilld
SKILL.md
vueuse/vueuse @vueuse/integrations@14.2.1

Tags: next: 5.0.0, alpha: 14.0.0-alpha.3, beta: 14.0.0-beta.1

References: Docs

API Changes

This section documents version-specific API changes — prioritize recent major/minor releases.

BREAKING: Requires Vue 3.5+ — v14.x now requires Vue 3.5.0 as a peer dependency for native features like useTemplateRef

BREAKING: ESM-only — dropped CommonJS (CJS) build in v13.0.0, now an ESM-only package source

BREAKING: focus-trap dependency — useFocusTrap updated peer dependency range to ^7 || ^8 in v14.2.0 source

BREAKING: universal-cookie dependency — useCookies now supports and prefers universal-cookie ^7 || ^8

BREAKING: change-case v5 — useChangeCase is now compatible with change-case v5, including internal naming changes

DEPRECATED: Alias exports — v14.0.0 deprecated alias exports in favor of original function names for consistency source

NEW: watchElement option — useSortable added watchElement in v14.2.0 to auto-reinitialize when target element changes source

NEW: updateContainerElements — useFocusTrap exposed updateContainerElements in v13.6.0 for dynamic container updates source

NEW: serializer option — useIDBKeyval added options.serializer in v13.6.0 for custom data serialization source

NEW: Component Ref support — useSortable can now accept a Vue component instance/ref as the target element since v13.1.0 source

NEW: Thenable useAxios — useAxios returns are now thenable, allowing await useAxios(...) in async contexts source

NEW: Flexible execute — useAxios execute() can now take url or config separately for manual triggers source

NEW: initialData option — useAxios added initialData to provide a default value before the request finishes source

NEW: Helper functions — moveArrayElement, insertNodeAt, and removeNode are now exported from useSortable source

Also changed: useAsyncValidator internal types · useJwt options refinement · useNProgress reactive state consistency · useSortable type misalignment fix source

Best Practices
Import functions from submodules to maximize tree-shaking efficiency and reduce the final bundle size source
// Preferred
import { useAxios } from '@vueuse/integrations/useAxios'

// Avoid
import { useAxios } from '@vueuse/integrations'

Await useAxios() directly for one-off requests as the return value is thenable, simplifying promise handling source
const { data, error } = await useAxios('/api/posts')

Enable resetOnExecute: true in useAxios options to clear stale data automatically when a new request is triggered source
const { execute } = useAxios('/api/data', { method: 'GET' }, { resetOnExecute: true })

Explicitly import useCookies in Nuxt 3 environments to avoid name collisions with Nuxt's built-in useCookie composable source
import { useCookies } from '@vueuse/integrations/useCookies'

Use autoUpdateDependencies: true with useCookies to automatically track and update dependencies for any cookie names accessed via .get() source
const { get } = useCookies(['initial'], { autoUpdateDependencies: true })

Enable the watchElement: true option in useSortable to automatically reinitialize the instance when the target element changes (e.g., with v-if) source
useSortable(el, list, { watchElement: true })

Wrap post-update logic in nextTick() after calling moveArrayElement in useSortable to ensure the DOM update has fully finished source
useSortable(el, list, {
  onUpdate: (e) => {
    moveArrayElement(list, e.oldIndex, e.newIndex)
    nextTick(() => { /* perform post-move logic */ })
  }
})

Use nextTick() before calling activate() in useFocusTrap when dealing with conditionally rendered (v-if) elements to ensure they exist in the DOM source
async function openModal() {
  show.value = true
  await nextTick()
  activate()
}

Prefer the UseFocusTrap component over the manual composable for automatic activation on mount and cleanup on unmount source
<UseFocusTrap v-if="show" :options="{ immediate: true }">
  <div class="modal">...</div>
</UseFocusTrap>

Await the .set() method returned by useIDBKeyval to ensure that the IndexedDB transaction is fully committed before proceeding source
const count = useIDBKeyval('my-count', 0)
await count.set(10)

Weekly Installs
82
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