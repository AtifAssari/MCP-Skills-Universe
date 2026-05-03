---
title: vue-test-utils-skilld
url: https://skills.sh/harlan-zw/vue-ecosystem-skills/vue-test-utils-skilld
---

# vue-test-utils-skilld

skills/harlan-zw/vue-ecosystem-skills/vue-test-utils-skilld
vue-test-utils-skilld
Installation
$ npx skills add https://github.com/harlan-zw/vue-ecosystem-skills --skill vue-test-utils-skilld
SKILL.md
vuejs/test-utils @vue/test-utils@2.4.6

Tags: latest: 2.4.6, 2.0.0-alpha.0: 2.0.0-alpha.0, 2.0.0-alpha.1: 2.0.0-alpha.1

References: Docs

API Changes

This section documents version-specific API changes — prioritize recent major/minor releases.

BREAKING: propsData — v2 renamed to props for consistency with component definitions source

BREAKING: createLocalVue — removed in v2, use the global mounting option to install plugins, mixins, or directives source

BREAKING: mocks and stubs — moved into the global mounting option in v2 as they apply to all components source

BREAKING: destroy() — renamed to unmount() in v2 to match Vue 3 lifecycle naming source

BREAKING: findAll().at() — removed in v2; findAll() now returns a standard array of wrappers source

BREAKING: createWrapper() — removed in v2, use the new DOMWrapper() constructor for non-component elements source

BREAKING: shallowMount — v2 no longer renders default slot content for stubbed components by default source

BREAKING: find() — now only supports querySelector syntax; use findComponent() to locate Vue components source

BREAKING: setSelected and setChecked — removed in v2, functionality merged into setValue() source

BREAKING: attachToDocument — renamed to attachTo in v2 source

BREAKING: emittedByOrder — removed in v2, use emitted() instead source

NEW: renderToString() — added in v2.3.0 to support SSR testing source

NEW: enableAutoUnmount() / disableAutoUnmount() — replaces enableAutoDestroy in v2 source

DEPRECATED: scopedSlots — removed in v2 and merged into the slots mounting option source

Also changed: setValue() and trigger() return nextTick · slots scope exposed as params in string templates · is, isEmpty, isVueInstance, name, setMethods, and contains removed

Best Practices
Always await methods that return nextTick (trigger, setValue, setProps, setData) to ensure DOM updates are processed before running assertions source
// Preferred
await wrapper.find('button').trigger('click')
expect(wrapper.text()).toContain('Count: 1')

// Avoid — assertion runs before DOM update
wrapper.find('button').trigger('click')
expect(wrapper.text()).toContain('Count: 1')


Prefer get() and getComponent() over find() and findComponent() when you expect the element to exist — they throw immediately if not found, providing clearer test failures source

Use flushPromises() to resolve non-Vue asynchronous operations such as mocked API calls (axios) or external promise-based logic that Vue doesn't track source

Enable enableAutoUnmount(afterEach) in your test setup to automatically clean up wrappers after every test, preventing state pollution and memory leaks source

import { enableAutoUnmount } from '@vue/test-utils'
import { afterEach } from 'vitest'

enableAutoUnmount(afterEach)


Wrap components with async setup() in a <Suspense> component within your test to correctly handle their asynchronous initialization source

Enable config.global.renderStubDefaultSlot = true when using shallow mounting to ensure content within default slots is rendered for verification source

Prefer mount() with specific global.stubs over shallow: true to keep tests more production-like while still isolating specific complex child components source

Use global.provide to pass data to components using inject, ensuring the component tree's dependency injection works as it does in production source

Test complex composables by mounting a minimal TestComponent that calls the composable, allowing you to verify internal state via wrapper.vm source

const TestComponent = defineComponent({
  setup() {
    return { ...useMyComposable() }
  }
})
const wrapper = mount(TestComponent)
expect(wrapper.vm.someValue).toBe(true)

Stub custom directives using the vName naming convention (e.g., vTooltip: true) in the global.stubs mounting option source
Weekly Installs
94
Repository
harlan-zw/vue-e…m-skills
GitHub Stars
158
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass