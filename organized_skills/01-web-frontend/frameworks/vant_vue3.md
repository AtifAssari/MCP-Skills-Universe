---
rating: ⭐⭐⭐
title: vant-vue3
url: https://skills.sh/teachingai/full-stack-skills/vant-vue3
---

# vant-vue3

skills/teachingai/full-stack-skills/vant-vue3
vant-vue3
Installation
$ npx skills add https://github.com/teachingai/full-stack-skills --skill vant-vue3
SKILL.md
Vant of Vue 3
When to use this skill

Use this skill whenever the user is working with Vant for Vue 3 or asks for:

Vant installation, setup, or project initialization
Vue 3 mobile UI implementation with vant
van-button, van-cell, van-form, van-dialog, van-popup, van-toast
Vant ConfigProvider, theme variables, or theme customization
Mobile-first page structure, touch-oriented UI, or form flows based on Vant
Converting generic Vue 3 UI to Vant component usage
Reviewing or fixing existing Vant Vue 3 code

Trigger terms include:

vant
vant vue3
Vant of Vue 3.0
van-button, van-form, van-cell, van-dialog, van-toast, van-popup
ConfigProvider
theme-vars
vant 组件
Vant 主题定制
Scope and alignment

This skill is aligned to the official Vant documentation entry points:

Official website: https://vant-ui.github.io/
Official guide: https://vant-ui.github.io/vant/#/zh-CN

The local skill content only claims coverage for files that actually exist in this skill directory. Do not reference non-existent local files. If the requested Vant component is not covered by a local example file, use the official guide as the primary reference and reuse the closest local pattern.

For the exact local-to-official mapping, read:

references/official-mapping.md
How to use this skill
Step 1: Identify the request area

Map the user request to one of these areas:

Quick start / setup

Installing Vant
Importing styles
Full import vs on-demand import
Vue 3 project bootstrap

Component implementation

Button
Cell
Form
Dialog
Toast
Popup

Global config and theming

ConfigProvider
theme-vars
Theme customization

API lookup

Common props
Component props/events/methods
Global config API

Template or scaffold

Project setup template
Reusable component structure
Step 2: Load only the matching files

Use the smallest relevant set of files.

A. Quick start / setup
examples/getting-started/installation.md
examples/getting-started/basic-usage.md
templates/project-setup.md

Use these when the user asks how to install Vant, register components, import CSS, or start a Vue 3 + Vant project.

B. Covered component examples

Use only the component file that matches the user request:

Button → examples/components/button.md
Cell → examples/components/cell.md
Form → examples/components/form.md
Dialog → examples/components/dialog.md
Popup → examples/components/popup.md
Toast → examples/components/toast.md
C. Global config and theme
api/config-provider.md
examples/advanced/theme-customization.md

Use these for ConfigProvider, dark/light theme handling, theme-vars, CSS variables, or global UI behavior.

D. API lookup
api/components.md
api/config-provider.md

Use these when the user needs prop names, event names, method names, or a quick API summary.

E. Official navigation and coverage boundaries
references/official-mapping.md

Use this file when:

You need to confirm what this skill covers locally
You need to route the user from an official Vant section to a local file
You need to handle a Vant component that is not yet covered by a local example
Step 3: Follow the response workflow

When answering with this skill:

Confirm the target is Vant for Vue 3, not another Vue UI library.
Pick the matching local example or API file.
Keep code examples in Vue 3 Composition API style.
Preserve Vant naming and usage conventions:
import from vant
use van- components in templates
import vant/lib/index.css where setup requires it
Prefer mobile-first structure and touch-oriented interaction patterns.
If the requested component is not covered locally:
say that the local skill does not contain a dedicated example file for that component
route via references/official-mapping.md
use the official guide as the primary source of truth
adapt the closest covered local example style instead of inventing fake local files
Local navigation map

This is the actual local navigation surface for the skill.

Getting started
examples/getting-started/installation.md
examples/getting-started/basic-usage.md
templates/project-setup.md
Components covered locally
examples/components/button.md
examples/components/cell.md
examples/components/form.md
examples/components/dialog.md
examples/components/popup.md
examples/components/toast.md
Theme and global configuration
api/config-provider.md
examples/advanced/theme-customization.md
API summaries
api/components.md
api/config-provider.md
Official mapping
references/official-mapping.md
Working rules
Do
Use only local files that actually exist
Keep answers anchored to the official Vant guide structure
Prefer concrete component code over abstract explanation
Use script setup style for Vue 3 examples unless the user already uses another style
Mention ConfigProvider when the user asks about global theme or locale-like app-wide config
Keep code samples runnable and focused
Do not
Do not reference icon.md, tabs.md, navbar.md, or other files that do not exist in this skill
Do not pretend this skill has full local coverage for every Vant component
Do not mix Vant patterns with Element Plus, Ant Design Vue, or other UI libraries
Do not output generic Vue UI advice when the user explicitly asks for Vant
Answer patterns
If the user asks for setup

Load:

examples/getting-started/installation.md
templates/project-setup.md

Return:

install command
CSS import
registration strategy
minimal Vue 3 + Vant starter
If the user asks for a covered component

Load:

the matching file under examples/components/
api/components.md if props/events are involved

Return:

minimal example first
then props/events/method notes
then usage pitfalls if relevant
If the user asks for theme customization

Load:

api/config-provider.md
examples/advanced/theme-customization.md

Return:

ConfigProvider usage
theme-vars example
CSS variable strategy
scope and inheritance notes
If the user asks for an uncovered Vant component

Load:

references/official-mapping.md
nearest covered local file

Return:

explicit note that the local skill has no dedicated example file for that component
route to the official Vant guide section
provide a Vant-consistent example following the same conventions used in this skill
Quality checklist

Before responding, verify that:

the answer is specifically for Vant of Vue 3
all referenced local files exist
imports come from vant
examples use Vue 3 syntax
setup examples include CSS import where needed
theme answers use ConfigProvider / theme-vars consistently
Resources
Official website: https://vant-ui.github.io/
Official guide: https://vant-ui.github.io/vant/#/zh-CN
Local official mapping: references/official-mapping.md
Keywords

Vant, Vant Vue 3, Vant of Vue 3.0, Vue 3 mobile UI, van-button, van-cell, van-form, van-dialog, van-toast, van-popup, ConfigProvider, theme-vars, mobile-first UI, Vant theme, Vant setup, Vant component library, vant 组件, vant vue3, 移动端组件库, 按钮, 单元格, 表单, 对话框, 提示, 弹出层, 主题定制

Weekly Installs
136
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