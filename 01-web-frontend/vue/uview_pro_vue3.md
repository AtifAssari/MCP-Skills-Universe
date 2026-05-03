---
rating: ⭐⭐
title: uview-pro-vue3
url: https://skills.sh/teachingai/full-stack-skills/uview-pro-vue3
---

# uview-pro-vue3

skills/teachingai/full-stack-skills/uview-pro-vue3
uview-pro-vue3
Installation
$ npx skills add https://github.com/teachingai/full-stack-skills --skill uview-pro-vue3
SKILL.md
When to use this skill

Use this skill whenever the user wants to:

Build Vue 3 / uni-app mobile interfaces with uView Pro components
Use form, data display, feedback, or navigation components
Configure uView Pro theme, internationalization, or global settings
Use built-in tools (HTTP requests, storage, routing, validation, formatting)
Set up uView Pro in a new uni-app project
How to use this skill
Workflow
Install - npm install uview-pro and register in main.js
Choose component - Match the UI need to component from reference below
Load example file - Each component has a detailed example in examples/components/
Use tools - Leverage built-in utilities from examples/tools/
Quick-Start: Installation and Basic Usage
// main.js
import { createSSRApp } from 'vue'
import uView from 'uview-pro'
import App from './App.vue'

export function createApp() {
  const app = createSSRApp(App)
  app.use(uView)
  return { app }
}

Example: Form with Validation
<template>
  <u-form :model="form" :rules="rules" ref="formRef">
    <u-form-item label="Username" prop="name">
      <u-input v-model="form.name" placeholder="Enter username" />
    </u-form-item>
    <u-form-item label="Email" prop="email">
      <u-input v-model="form.email" placeholder="Enter email" />
    </u-form-item>
    <u-button type="primary" @click="submit">Submit</u-button>
  </u-form>
</template>

<script setup>
import { ref, reactive } from 'vue'

const formRef = ref(null)
const form = reactive({ name: '', email: '' })
const rules = {
  name: [{ required: true, message: 'Name is required' }],
  email: [{ required: true, message: 'Email is required' }, { type: 'email', message: 'Invalid email' }]
}

const submit = () => {
  formRef.value.validate(valid => {
    if (valid) uni.showToast({ title: 'Success!' })
  })
}
</script>

Component Categories
Category	Components	Example Files
Form	Button, Input, Form, Select, Switch, Checkbox, Radio, Upload	examples/components/form.md
Display	List, Card, Avatar, Badge, Tag, Empty	examples/components/list.md
Feedback	Toast, Modal, Loading, Popup, Drawer	examples/components/modal.md
Navigation	Tabs, NavBar, Pagination, Dropdown	examples/components/tabs.md
Tools Reference
Tool	File	Purpose
HTTP	examples/tools/http.md	Request wrapper with interceptors
Storage	examples/tools/storage.md	Local storage utilities
Router	examples/tools/router.md	Navigation helpers
Validator	examples/tools/validator.md	Form validation
API Reference
api/component-api.md - Component props, events, methods, and slots
api/tools-api.md - Utility function signatures and parameters
api/config-api.md - Global and theme configuration
Best Practices
On-demand import - Import only used components to reduce bundle size
Composition API - Prefer <script setup> for cleaner Vue 3 code
Theme variables - Customize via uView theme config rather than overriding CSS
Use built-in tools - Leverage HTTP, storage, and router utilities instead of adding extra dependencies
Test on device - Verify uni-app behavior on actual mobile devices, not just H5
Resources
Official Docs: https://uviewpro.cn/
Keywords

uView Pro, uview-pro, Vue 3, uni-app, component library, 组件库, Button, Form, List, Modal, Tabs, NavBar, mobile UI, 表单, 列表

Weekly Installs
73
Repository
teachingai/full…k-skills
GitHub Stars
349
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass