---
rating: ⭐⭐⭐
title: vueuse-components-skilld
url: https://skills.sh/harlan-zw/vue-ecosystem-skills/vueuse-components-skilld
---

# vueuse-components-skilld

skills/harlan-zw/vue-ecosystem-skills/vueuse-components-skilld
vueuse-components-skilld
Installation
$ npx skills add https://github.com/harlan-zw/vue-ecosystem-skills --skill vueuse-components-skilld
SKILL.md
vueuse/vueuse @vueuse/components@14.2.1

Tags: next: 5.0.0, alpha: 14.0.0-alpha.3, beta: 14.0.0-beta.1

References: Docs

API Changes

This section documents version-specific API changes for @vueuse/components — prioritize recent major/minor releases.

BREAKING: @vueuse/components v14+ requires Vue 3.5+, following core library requirements source

BREAKING: Renderless components refactored for consistency in v14.0.0. Components like OnClickOutside and OnLongPress now use an options prop for configuration and @trigger emit for actions source

BREAKING: ESM-only package — CJS build has been dropped since v13.0.0 source

DEPRECATED: VOnClickOutside is deprecated in favor of the lowercase vOnClickOutside directive source

DEPRECATED: VOnLongPress is deprecated in favor of the lowercase vOnLongPress directive source

NEW: UseDraggable supports autoScroll and restrictInView options for constrained dragging in v14.2.0 source

NEW: UseDraggable supports storageKey and storageType props for persistent element position source

NEW: vOnKeyStroke directive added for listening to keyboard events directly on elements

NEW: UseIdle default slot data now includes pause and resume methods via Stoppable implementation source

NEW: vInfiniteScroll supports reactive canLoadMore option in v14.1.0 source

NEW: UseElementVisibility added initialValue option in v14.1.0 source

NEW: UseMouseInElement supports tracking inline-level elements in v14.1.0 source

NEW: vIntersectionObserver now supports reactive rootMargin option in v14.2.0 source

NEW: UseOffsetPagination emits page-change, page-size-change, and page-count-change events

Also changed: useTransition custom interpolators · refManualReset new function · tryOnScopeDispose failSilently · useAsyncState execute result · useTimeAgoIntl custom units

Best Practices

Use the storage-key and storage-type props on the <UseDraggable> component to automatically persist element position in localStorage or sessionStorage across sessions source

Utilize the ignore option in OnClickOutside (component or directive) to pass an array of refs or CSS selectors for elements that should not trigger the handler, essential for complex UIs like nested modals source

Always provide #loading and #error slots in <UseImage> to prevent layout shifts and handle broken images gracefully, rather than managing loading states manually in the script source

Prefer createReusableTemplate over extracting small, repeated UI fragments into separate files to maintain access to local scope variables and avoid tedious prop/emit definitions source

Provide a generic type to createReusableTemplate<T>() to enable full TypeScript support and IDE autocompletion for data passed between DefineTemplate and ReuseTemplate source

Use createTemplatePromise to call complex UI elements like modals or dialogs as promises, keeping the UI definition in the template while maintaining programmatic control and clean async/await flows source

Configure @vueuse/components directives like v-on-click-outside or v-on-long-press using the [handler, options] array syntax for clean, inline logic without needing a separate setup variable for options source

<div v-if="modal" v-on-click-outside="[closeModal, { ignore: [ignoreElRef] }]">
  Hello World
</div>


Use the <UseOffsetPagination> component to handle complex pagination state; it emits clean events (page-change, page-size-change) that are more idiomatic and easier to wire up in templates than manually watching refs source

Set detectIframe: true in onClickOutside options when building global navigation or modals to ensure they close when the user clicks inside an iframe, an edge case often missed in manual implementations source

Utilize the as prop on renderable components like <UseElementBounding> or <UseFullscreen> to render them as semantically correct HTML elements (e.g., section, nav) instead of the default div source

Weekly Installs
95
Repository
harlan-zw/vue-e…m-skills
GitHub Stars
158
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn