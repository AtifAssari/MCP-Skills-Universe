---
title: markstream-vue
url: https://skills.sh/simon-he95/markstream-vue/markstream-vue
---

# markstream-vue

skills/simon-he95/markstream-vue/markstream-vue
markstream-vue
Installation
$ npx skills add https://github.com/simon-he95/markstream-vue --skill markstream-vue
SKILL.md
Markstream Vue 3

Use this skill when the host app is plain Vue 3, typically Vite-based, and not Nuxt.

Workflow
Confirm the repo is Vue 3 and not Nuxt.
Install markstream-vue plus only the optional peers required by the requested features.
Import markstream-vue/index.css after resets.
In Tailwind or UnoCSS projects, keep Markstream styles inside @layer components.
Start with <MarkdownRender :content="markdown" />.
Switch to nodes plus final only for streaming, SSE, or high-frequency updates.
Use custom-id plus scoped setCustomComponents(...) for overrides.
Validate with the smallest useful dev, build, or typecheck command.
Default Decisions
Vue 3 apps default to content.
Prefer local component registration unless the repo already uses a shared plugin entry.
When Monaco code blocks need app-level preloading, import preloadCodeBlockRuntime from markstream-vue. Existing getUseMonaco() preloads remain valid; do not import stream-monaco directly just to warm workers.
If the host is actually Nuxt, leave SSR-specific setup to markstream-nuxt.
Useful Doc Targets
docs/guide/quick-start.md
docs/guide/installation.md
docs/guide/usage.md
docs/guide/component-overrides.md
Weekly Installs
77
Repository
simon-he95/mark…ream-vue
GitHub Stars
2.3K
First Seen
Mar 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass