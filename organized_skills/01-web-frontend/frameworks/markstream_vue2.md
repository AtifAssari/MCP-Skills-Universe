---
rating: ⭐⭐
title: markstream-vue2
url: https://skills.sh/simon-he95/markstream-vue/markstream-vue2
---

# markstream-vue2

skills/simon-he95/markstream-vue/markstream-vue2
markstream-vue2
Installation
$ npx skills add https://github.com/simon-he95/markstream-vue --skill markstream-vue2
SKILL.md
Markstream Vue 2

Use this skill when the host app is Vue 2 and not specifically a Vue CLI / Webpack 4 edge case.

Workflow
Confirm the repo is Vue 2.6 or 2.7.
Install markstream-vue2.
Add @vue/composition-api only when the repo is Vue 2.6 and uses Composition API patterns.
Import markstream-vue2/index.css after resets.
Start with <MarkdownRender :content="markdown" />.
Use scoped custom component mappings when the task needs overrides or trusted tags.
Validate with the smallest useful dev or build command.
Default Decisions
Vue 2.7 can use built-in Composition API support.
Vue 2.6 needs @vue/composition-api only when the codebase actually relies on Composition API.
If the repo is Vue CLI / Webpack 4, prefer markstream-vue2-cli.
If the repo is Vue 2 plus Vite worker imports, prefer markstream-vue2-vite.
Useful Doc Targets
docs/guide/vue2-quick-start.md
docs/guide/vue2-installation.md
docs/guide/vue2-components.md
docs/guide/troubleshooting.md
Weekly Installs
21
Repository
simon-he95/mark…ream-vue
GitHub Stars
2.3K
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass