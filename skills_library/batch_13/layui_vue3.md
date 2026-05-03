---
title: layui-vue3
url: https://skills.sh/teachingai/full-stack-skills/layui-vue3
---

# layui-vue3

skills/teachingai/full-stack-skills/layui-vue3
layui-vue3
Installation
$ npx skills add https://github.com/teachingai/full-stack-skills --skill layui-vue3
SKILL.md
When to use this skill

Use this skill whenever the user wants to:

Install and set up Layui Vue in a Vue 3 project
Use Layui Vue components (Button, Table, DatePicker, etc.)
Configure Layui Vue (theme, i18n, etc.)
Use Layer component for modals and dialogs
Implement forms with Layui Vue components
Use data tables with sorting and pagination
Handle file uploads
Create dropdowns and tooltips
Use date and time pickers
Customize component styles
Understand Layui Vue API and methods
Troubleshoot Layui Vue issues
How to use this skill

Identify the topic from the user's request and find the corresponding example file in the mapping below

Load the appropriate example file from the examples/ directory

Follow the specific instructions in that example file for syntax, structure, and best practices

Doc mapping (one-to-one with https://www.layui-vue.com/zh-CN/)

Guide (指南):

examples/getting-started.md → https://www.layui-vue.com/zh-CN/index
examples/introduce.md → https://www.layui-vue.com/zh-CN/guide/introduce

Components (组件) - examples/components/:

See component files in examples/components/ directory

Each component file maps to https://www.layui-vue.com/zh-CN/components/[component-name]

Important Notes:

Layui Vue is built for Vue 3
Components use Composition API
Supports TypeScript
Examples include both JavaScript and TypeScript versions
Each example file includes key concepts, code examples, and key points

Reference API documentation in the api/ directory when needed:

api/layer-api.md - Layer API methods
api/component-api.md - Component API reference

Use templates from the templates/ directory:

templates/installation.md - Installation templates
templates/component-usage.md - Component usage templates
1. Understanding Layui Vue

Layui Vue is a Vue 3 component library that provides a rich set of UI components, following the design philosophy of Layui.

Key Concepts:

Vue 3 Support: Built with Vue 3 Composition API
Rich Components: Button, Table, DatePicker, Layer, etc.
TypeScript: Full TypeScript support
Theme Customization: Support for theme customization
i18n: Internationalization support
2. Installation

Using npm:

npm install @layui/layui-vue


Using yarn:

yarn add @layui/layui-vue


Using pnpm:

pnpm add @layui/layui-vue

3. Basic Setup
// main.js
import { createApp } from 'vue'
import LayuiVue from '@layui/layui-vue'
import '@layui/layui-vue/lib/index.css'
import App from './App.vue'

const app = createApp(App)
app.use(LayuiVue)
app.mount('#app')

4. Basic Component Usage
<template>
  <lay-button type="primary">Button</lay-button>
</template>

<script setup>
import { LayButton } from '@layui/layui-vue'
</script>

Examples and Templates

This skill includes detailed examples organized to match the official documentation structure. All examples are in the examples/ directory (see mapping above).

To use examples:

Identify the topic from the user's request
Load the appropriate example file from the mapping above
Follow the instructions, syntax, and best practices in that file
Adapt the code examples to your specific use case

To use templates:

Reference templates in templates/ directory for common scaffolding
Adapt templates to your specific needs and coding style
API Reference

Detailed API documentation is available in the api/ directory, organized to match the official Layui Vue API documentation structure:

Layer API (api/layer-api.md)
layer.open() - Open modal/dialog
layer.close() - Close layer
layer.msg() - Show message
layer.confirm() - Show confirmation dialog
layer.load() - Show loading
layer.drawer() - Show drawer
Component API (api/component-api.md)
Component props and events
Component methods
Component slots

To use API reference:

Identify the API you need help with
Load the corresponding API file from the api/ directory
Find the API signature, parameters, return type, and examples
Reference the linked example files for detailed usage patterns
All API files include links to relevant example files in the examples/ directory
Best Practices
Use TypeScript: Take advantage of TypeScript support
Import on demand: Import only needed components
Follow component API: Use props and events correctly
Customize theme: Use theme variables for customization
Handle events: Properly handle component events
Use Layer API: Use Layer API for modals and dialogs
Resources
Official Documentation: https://www.layui-vue.com/zh-CN/index
Getting Started: https://www.layui-vue.com/zh-CN/guide/introduce
Components: https://www.layui-vue.com/zh-CN/components
GitHub Repository: https://github.com/layui-vue/layui-vue
Keywords

Layui Vue, layui-vue, Vue 3, component library, UI components, Button, Table, DatePicker, Layer, Dropdown, Tooltip, Form, Input, Select, Checkbox, Radio, Switch, Upload, 组件库, 按钮, 表格, 日期选择器, 弹层, 下拉菜单, 提示, 表单, 输入框, 选择器, 复选框, 单选框, 开关, 上传

Weekly Installs
55
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