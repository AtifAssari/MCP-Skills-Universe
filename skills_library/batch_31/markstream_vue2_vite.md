---
title: markstream-vue2-vite
url: https://skills.sh/simon-he95/markstream-vue/markstream-vue2-vite
---

# markstream-vue2-vite

skills/simon-he95/markstream-vue/markstream-vue2-vite
markstream-vue2-vite
Installation
$ npx skills add https://github.com/simon-he95/markstream-vue --skill markstream-vue2-vite
SKILL.md
Markstream Vue 2 Vite

Use this skill when the host app is Vue 2 and the bundler is Vite.

Workflow
Confirm the repo is Vue 2 with Vite-based tooling.
Install markstream-vue2 plus only the requested optional peers.
Import markstream-vue2/index.css after resets.
Use Vite worker imports when the repo needs bundled workers.
markstream-vue2/workers/... ?worker or ?worker&inline patterns are allowed here.
Keep Composition API decisions explicit for Vue 2.6 repos.
Validate with the smallest useful Vite dev or build command.
Default Decisions
Prefer bundled workers over CDN workers in Vite-based Vue 2 repos.
Keep UnoCSS or Tailwind resets before Markstream CSS.
Use the generic markstream-vue2 skill only when the bundler-specific choice does not matter.
Useful Doc Targets
docs/guide/vue2-quick-start.md
docs/guide/vue2-installation.md
docs/guide/tailwind.md
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