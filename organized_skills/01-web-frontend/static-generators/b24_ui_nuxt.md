---
rating: ⭐⭐
title: b24-ui-nuxt
url: https://skills.sh/bitrix24/b24ui/b24-ui-nuxt
---

# b24-ui-nuxt

skills/bitrix24/b24ui/b24-ui-nuxt
b24-ui-nuxt
Installation
$ npx skills add https://github.com/bitrix24/b24ui --skill b24-ui-nuxt
SKILL.md
Bitrix24 UI

Vue component library built on Reka UI + Tailwind CSS + Tailwind Variants. Works with Nuxt, Vue (Vite), Laravel (Vite + Inertia), and AdonisJS (Vite + Inertia).

LLMs.txt

For component API details (props, slots, events, full documentation, examples), use the Bitrix24 UI documentation. If not already configured, add it.

When you need to know what a component accepts or how its API works, use the Bitrix24 UI documentation. This skill teaches you when to use which component and how to build well.

Core rules (always apply)
Always wrap the app in B24App — required for toasts, tooltips, and programmatic overlays. Accepts a locale prop for i18n.
Always use semantic colors — text-description, bg-elevated, border-muted, etc. Never use raw Tailwind palette colors like text-gray-500.
Read generated theme files for slot names — Nuxt: .nuxt/ui/<component>.ts, Vue: node_modules/.b24ui-nuxt/b24ui/<component>.ts. These show every slot, variant, and default class for any component.
Override priority (highest wins): b24ui prop / class prop → global config → theme defaults.
See icons guideline for find icons.
How to use this skill

Based on the task, load the relevant reference files before writing any code. Don't load everything — only what's needed.

Reference files

Guidelines — design decisions and conventions:

design-system — semantic colors, theming, brand customization, variants, the b24ui prop
component-selection — decision matrices: when to use Modal vs Slideover, Select vs SelectMenu, Toast vs Alert, etc.
conventions — coding patterns, slot naming, items arrays, composables, keyboard shortcuts
forms — form validation, field layout, error handling, Standard Schema
icons — import icon and use it

Layouts — full page structure patterns:

landing — landing pages
dashboard — admin UI with sidebar and panels

Recipes — complete patterns for common tasks:

data-tables — tables with filters, pagination, sorting, selection
overlays — modals, slideovers, drawers, command palette
navigation — headers, sidebars, breadcrumbs, tabs

Quick reference:

components — categorized component index for finding the right component name
Routing table
Task	Load these references
Build application for Bitrix24 / a dashboard / admin UI	conventions, component-selection, dashboard
Build a landing page	design-system, conventions, landing
Add a settings page	conventions, forms
Create a login / signup form	conventions, forms, auth
Display data in a table	conventions, component-selection, data-tables
Add a chat interface	conventions, chat
Add a modal, slideover, or drawer	conventions, component-selection, overlays
Build site navigation	conventions, component-selection, navigation
Add a rich text editor	conventions, editor
General UI work	conventions, component-selection
Installation
Nuxt
pnpm add @bitrix24/b24ui-nuxt @bitrix24/b24icons-vue tailwindcss

// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@bitrix24/b24ui-nuxt'],
  css: ['~/assets/css/main.css']
})

/* app/assets/css/main.css */
@import "tailwindcss";
@import "@bitrix24/b24ui-nuxt";

<!-- app.vue -->
<template>
  <B24App>
    <NuxtPage />
  </B24App>
</template>

Vue (Vite)
pnpm add @bitrix24/b24ui-nuxt @bitrix24/b24icons-vue tailwindcss

// vite.config.ts
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import bitrix24UIPluginVite from '@bitrix24/b24ui-nuxt/vite'

export default defineConfig({
  plugins: [
    vue(),
    bitrix24UIPluginVite()
  ]
})

// src/main.ts
import './assets/main.css'
import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import b24UiPlugin from '@bitrix24/b24ui-nuxt/vue-plugin'
import App from './App.vue'

const app = createApp(App)
const router = createRouter({
  routes: [],
  history: createWebHistory()
})

app.use(router)
app.use(b24UiPlugin)
app.mount('#app')

/* src/assets/css/main.css */
@import "tailwindcss";
@import "@bitrix24/b24ui-nuxt";

<!-- src/App.vue -->
<template>
  <B24App>
    <RouterView />
  </B24App>
</template>


Add class="isolate" to your root <div id="app"> in index.html. For Inertia: use b24ui({ router: 'inertia' }) in vite.config.ts.

Weekly Installs
18
Repository
bitrix24/b24ui
GitHub Stars
31
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn