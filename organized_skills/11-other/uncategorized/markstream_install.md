---
rating: ⭐⭐
title: markstream-install
url: https://skills.sh/simon-he95/markstream-vue/markstream-install
---

# markstream-install

skills/simon-he95/markstream-vue/markstream-install
markstream-install
Installation
$ npx skills add https://github.com/simon-he95/markstream-vue --skill markstream-install
SKILL.md
Markstream Install

Use this skill when the task is "add markstream to an app" or "fix a broken markstream install".

Read references/scenarios.md before making dependency choices.

Workflow
Detect the target framework and CSS stack.
Check package.json, app entry files, Tailwind or UnoCSS config, and whether the repo is SSR or streaming-focused.
Choose the package that matches the host app: markstream-vue, markstream-vue2, markstream-react, or markstream-angular.
Install the smallest peer set that matches the requested features.
Add peers only for features the user actually needs: Monaco, Mermaid, D2, KaTeX, or lightweight highlighting via stream-markdown.
Do not install every optional peer by default.
For Vue 3 Monaco preloading, use preloadCodeBlockRuntime from markstream-vue so the renderer runtime knows Monaco is warm. Existing getUseMonaco() calls are still compatible.
Fix CSS order.
Put reset styles before Markstream styles.
In Tailwind or UnoCSS projects, place markstream-*/index.css inside @layer components.
Import katex/dist/katex.min.css when math is enabled.
Add the smallest working render example.
Use content for static or low-frequency rendering.
Use nodes plus final when the app receives streaming updates.
Keep customization scoped.
If the task requires overrides, prefer customId / custom-id plus scoped setCustomComponents(...).
Validate.
Run the smallest relevant build, typecheck, test, or docs build command.
Report which peers were installed, where CSS lives, and whether the repo should later adopt nodes.
Default Decisions
Prefer the minimal peer set over "install everything".
Prefer content unless the app is clearly SSE, chat, token-streaming, or worker-preparsed.
Treat CSS order as a first-class part of installation, not a later cleanup.
When the request includes SSR, explicitly gate browser-only peers behind client-only boundaries.
Useful Doc Targets
docs/guide/installation.md
docs/guide/usage.md
docs/guide/troubleshooting.md
docs/guide/component-overrides.md
Weekly Installs
44
Repository
simon-he95/mark…ream-vue
GitHub Stars
2.3K
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass