---
title: nuxt-ui
url: https://skills.sh/nuxt/ui/nuxt-ui
---

# nuxt-ui

skills/nuxt/ui/nuxt-ui
nuxt-ui
Installation
$ npx skills add https://github.com/nuxt/ui --skill nuxt-ui
Summary

125+ accessible Vue components with Tailwind CSS theming, built on Reka UI for rapid interface development.

Supports Nuxt, Vue (Vite), Laravel (Inertia), and AdonisJS with unified component API across frameworks
Includes 200,000+ Iconify icons via i-{collection}-{name} naming, with local collection support and custom icon directories
Seven semantic colors (primary, secondary, success, info, warning, error, neutral) configurable at runtime; override components via ui prop, class prop, or global config
Built-in form validation using Standard Schema (Zod, Valibot, Yup, Joi), toasts, modals, dropdowns, and five pre-built layout templates (dashboard, docs, chat, editor, page)
Composables for notifications, programmatic overlays, and keyboard shortcuts; generated theme files expose all slots and variants for deep customization
SKILL.md
Nuxt UI

Vue component library built on Reka UI + Tailwind CSS + Tailwind Variants. Works with Nuxt, Vue (Vite), Laravel (Vite + Inertia), and AdonisJS (Vite + Inertia).

MCP Server

For component API details (props, slots, events, full documentation, examples), use the Nuxt UI MCP server. If not already configured, add it:

Cursor — .cursor/mcp.json:

{ "mcpServers": { "nuxt-ui": { "type": "http", "url": "https://ui.nuxt.com/mcp" } } }


Claude Code:

claude mcp add --transport http nuxt-ui https://ui.nuxt.com/mcp


Key MCP tools:

search_components — find components by name, description, or category (no params = list all)
search_composables — find composables by name or description (no params = list all)
search_icons — search Iconify icons (defaults to lucide), returns i-{prefix}-{name} names
get_component — full component documentation with usage examples
get_component_metadata — props, slots, events (lightweight, no docs content)
get_example — real-world code examples

When you need to know what a component accepts or how its API works, use the MCP. This skill teaches you when to use which component and how to build well.

Core rules (always apply)
Always wrap the app in UApp — required for toasts, tooltips, and programmatic overlays. Accepts a locale prop for i18n.
Always use semantic colors — text-default, bg-elevated, border-muted, etc. Never use raw Tailwind palette colors like text-gray-500.
Read generated theme files for slot names — Nuxt: .nuxt/ui/<component>.ts, Vue: node_modules/.nuxt-ui/ui/<component>.ts. These show every slot, variant, and default class for any component.
Override priority (highest wins): ui prop / class prop → global config → theme defaults.
Icons use i-{collection}-{name} format — lucide is the default collection. Use the MCP search_icons tool to find icons, or browse at icones.js.org.
How to use this skill

Based on the task, load the relevant reference files before writing any code. Don't load everything — only what's needed.

Reference files

Guidelines — design decisions and conventions:

design-system — semantic colors, theming, brand customization, variants, the ui prop
component-selection — decision matrices: when to use Modal vs Slideover, Select vs SelectMenu, Toast vs Alert, etc.
conventions — coding patterns, slot naming, items arrays, composables, keyboard shortcuts
forms — form validation, field layout, error handling, Standard Schema

Layouts — full page structure patterns:

landing — landing pages, blog, changelog, pricing
dashboard — admin UI with sidebar and panels
docs — documentation sites with navigation and TOC
chat — AI chat with Vercel AI SDK
editor — rich text editor with toolbars

Recipes — complete patterns for common tasks:

data-tables — tables with filters, pagination, sorting, selection
auth — login, signup, forgot password forms
overlays — modals, slideovers, drawers, command palette
navigation — headers, sidebars, breadcrumbs, tabs

Quick reference:

components — categorized component index for finding the right component name
Routing table
Task	Load these references
Build a landing page	design-system, conventions, landing
Build a dashboard / admin UI	conventions, component-selection, dashboard
Add a settings page	conventions, forms
Create a login / signup form	conventions, forms, auth
Display data in a table	conventions, component-selection, data-tables
Customize theme / brand colors	design-system
Add a chat interface	conventions, chat
Add a modal, slideover, or drawer	conventions, component-selection, overlays
Build site navigation	conventions, component-selection, navigation
Build a documentation site	conventions, docs
Add a rich text editor	conventions, editor
General UI work	conventions, component-selection
Installation
Nuxt
pnpm add @nuxt/ui tailwindcss

// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@nuxt/ui'],
  css: ['~/assets/css/main.css']
})

/* app/assets/css/main.css */
@import "tailwindcss";
@import "@nuxt/ui";

<!-- app.vue -->
<template>
  <UApp>
    <NuxtPage />
  </UApp>
</template>

Vue (Vite)
pnpm add @nuxt/ui tailwindcss

// vite.config.ts
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import ui from '@nuxt/ui/vite'

export default defineConfig({
  plugins: [
    vue(),
    ui()
  ]
})

// src/main.ts
import './assets/css/main.css'
import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import ui from '@nuxt/ui/vue-plugin'
import App from './App.vue'

const app = createApp(App)
const router = createRouter({
  routes: [],
  history: createWebHistory()
})

app.use(router)
app.use(ui)
app.mount('#app')

/* src/assets/css/main.css */
@import "tailwindcss";
@import "@nuxt/ui";

<!-- src/App.vue -->
<template>
  <UApp>
    <RouterView />
  </UApp>
</template>


Add class="isolate" to your root <div id="app"> in index.html. For Inertia: use ui({ router: 'inertia' }) in vite.config.ts.

Weekly Installs
10.5K
Repository
nuxt/ui
GitHub Stars
6.5K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn