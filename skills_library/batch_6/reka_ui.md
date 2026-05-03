---
title: reka-ui
url: https://skills.sh/onmax/nuxt-skills/reka-ui
---

# reka-ui

skills/onmax/nuxt-skills/reka-ui
reka-ui
Installation
$ npx skills add https://github.com/onmax/nuxt-skills --skill reka-ui
Summary

Unstyled, accessible Vue 3 component primitives with WAI-ARIA compliance and composition patterns.

Provides 30+ headless components across forms, overlays, menus, data tables, and date pickers, each split into composable parts (Root, Trigger, Content, Portal)
Supports controlled state via v-model and uncontrolled via default* props; includes asChild for rendering as child elements without wrapper overhead
Built-in virtualization for large lists, context injection for child access, and forceMount for animation library integration
Auto-import resolvers available for Nuxt and Vite; recently added Rating component, ScrollArea glimpse mode, and stepSnapping for TimeField
SKILL.md
Reka UI

Unstyled, accessible Vue 3 component primitives. WAI-ARIA compliant. Previously Radix Vue.

Current version: v2.8.0 (January 2026)

When to Use
Building headless/unstyled components from scratch
Need WAI-ARIA compliant components
Using Nuxt UI, shadcn-vue, or other Reka-based libraries
Implementing accessible forms, dialogs, menus, popovers

For Vue patterns: use vue skill

Available Guidance
File	Topics
references/components.md	Component index by category (Form, Date, Overlay, Menu, Data, etc.)
components/*.md	Per-component details (dialog.md, select.md, etc.)

Guides (see reka-ui.com): Styling, Animation, Composition, SSR, Namespaced, Dates, i18n, Controlled State, Inject Context, Virtualization, Migration

Loading Files

Consider loading these reference files based on your task:

 references/components.md - if browsing component index by category or searching for specific components

DO NOT load all files at once. Load only what's relevant to your current task.

For styled Nuxt components built on Reka UI: use nuxt-ui skill

Key Concepts
Concept	Description
asChild	Render as child element instead of wrapper, merging props/behavior
Controlled/Uncontrolled	Use v-model for controlled, default* props for uncontrolled
Parts	Components split into Root, Trigger, Content, Portal, etc.
forceMount	Keep element in DOM for animation libraries
Virtualization	Optimize large lists (Combobox, Listbox, Tree) with virtual scrolling
Context Injection	Access component context from child components
Installation
// nuxt.config.ts (auto-imports all components)
export default defineNuxtConfig({
  modules: ['reka-ui/nuxt']
})

import { RekaResolver } from 'reka-ui/resolver'
// vite.config.ts (with auto-import resolver)
import Components from 'unplugin-vue-components/vite'

export default defineConfig({
  plugins: [
    vue(),
    Components({ resolvers: [RekaResolver()] })
  ]
})

Basic Patterns
<!-- Dialog with controlled state -->
<script setup>
import { DialogRoot, DialogTrigger, DialogPortal, DialogOverlay, DialogContent, DialogTitle, DialogDescription, DialogClose } from 'reka-ui'
const open = ref(false)
</script>

<template>
  <DialogRoot v-model:open="open">
    <DialogTrigger>Open</DialogTrigger>
    <DialogPortal>
      <DialogOverlay class="fixed inset-0 bg-black/50" />
      <DialogContent class="fixed left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 bg-white p-6 rounded">
        <DialogTitle>Title</DialogTitle>
        <DialogDescription>Description</DialogDescription>
        <DialogClose>Close</DialogClose>
      </DialogContent>
    </DialogPortal>
  </DialogRoot>
</template>

<!-- Select with uncontrolled default -->
<SelectRoot default-value="apple">
  <SelectTrigger>
    <SelectValue placeholder="Pick fruit" />
  </SelectTrigger>
  <SelectPortal>
    <SelectContent>
      <SelectViewport>
        <SelectItem value="apple"><SelectItemText>Apple</SelectItemText></SelectItem>
        <SelectItem value="banana"><SelectItemText>Banana</SelectItemText></SelectItem>
      </SelectViewport>
    </SelectContent>
  </SelectPortal>
</SelectRoot>

<!-- asChild for custom trigger element -->
<DialogTrigger as-child>
  <button class="my-custom-button">Open</button>
</DialogTrigger>

Recent Updates (v2.6.0-v2.8.0)
New component: Rating (v2.8.0)
ScrollArea: Added "glimpse" scrollbar mode (v2.8.0)
PopperContent: Added hideShiftedArrow prop (v2.8.0)
TimeField: Added stepSnapping support (v2.8.0)
Breaking: weekStartsOn now locale-independent for date components (v2.8.0)
Virtualization: estimateSize accepts function for Listbox/Tree (v2.7.0)
Composables: useLocale, useDirection exposed (v2.6.0)
Select: disableOutsidePointerEvents prop on Content (v2.7.0)
Toast: disableSwipe prop (v2.6.0)
Resources
Reka UI Docs
GitHub
Nuxt UI (styled Reka components)
shadcn-vue (styled Reka components)

Token efficiency: ~350 tokens base, components.md index ~100 tokens, per-component ~50-150 tokens

Weekly Installs
6.0K
Repository
onmax/nuxt-skills
GitHub Stars
649
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass