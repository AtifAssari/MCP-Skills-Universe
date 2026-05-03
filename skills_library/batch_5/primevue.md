---
title: primevue
url: https://skills.sh/kindy/skills/primevue
---

# primevue

skills/kindy/skills/primevue
primevue
Installation
$ npx skills add https://github.com/kindy/skills --skill primevue
SKILL.md
PrimeVue Setup and Usage

Guide for configuring PrimeVue with Vue 3 and Vite projects, including auto-import setup and theming.

Overview

PrimeVue is a complete UI suite for Vue.js with rich components, icons, and templates. It supports both styled mode (pre-skinned themes like Aura, Lara, Nora) and unstyled mode (full styling control with Tailwind, Bootstrap, etc.).

Documentation

Official LLM-optimized documentation: https://primevue.org/llms/pages/introduction.md

Installation

Install PrimeVue and themes:

npm install primevue @primeuix/themes

Plugin Configuration

Configure PrimeVue plugin with theme in main.ts:

import { createApp } from 'vue'
import PrimeVue from 'primevue/config'
import Aura from '@primeuix/themes/aura'
import App from './App.vue'

const app = createApp(App)
app.use(PrimeVue, {
  theme: {
    preset: Aura  // Available: Aura, Lara, Nora, etc.
  }
})
app.mount('#app')

Auto Import Setup

Install auto-import dependencies:

npm install -D unplugin-vue-components @primevue/auto-import-resolver


Configure in vite.config.ts:

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import Components from 'unplugin-vue-components/vite'
import { PrimeVueResolver } from '@primevue/auto-import-resolver'

export default defineConfig({
  plugins: [
    vue(),
    Components({
      resolvers: [
        PrimeVueResolver()
      ]
    })
  ],
})

Component Usage

With auto-import configured, use components directly without manual imports:

<template>
  <Button label="Click Me" />
  <InputText v-model="value" placeholder="Enter text" />
  <DataTable :value="items" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
// No PrimeVue component imports needed - handled by auto-import

const value = ref('')
const items = ref([])
</script>

Common Components
Button: <Button label="Text" />
InputText: <InputText v-model="value" />
Dropdown: <Dropdown v-model="selected" :options="items" />
DataTable: <DataTable :value="data" />
Dialog: <Dialog v-model:visible="show" />
Card: <Card><template #title>Title</template></Card>
Theming

Available preset themes:

Aura - Modern, clean design (recommended)
Lara - Material-inspired
Nora - Minimalist

Import and apply in plugin configuration as shown above.

References
Official docs: https://primevue.org
Vite setup: https://primevue.org/llms/pages/vite.md
Auto-import: https://primevue.org/llms/pages/autoimport.md
Weekly Installs
285
Repository
kindy/skills
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass