---
title: markstream-vue2-cli
url: https://skills.sh/simon-he95/markstream-vue/markstream-vue2-cli
---

# markstream-vue2-cli

skills/simon-he95/markstream-vue/markstream-vue2-cli
markstream-vue2-cli
Installation
$ npx skills add https://github.com/simon-he95/markstream-vue --skill markstream-vue2-cli
SKILL.md
Markstream Vue 2 CLI

Use this skill when the host app is Vue 2 on Vue CLI or another Webpack 4-style stack.

Workflow
Confirm the repo uses Vue 2 plus Vue CLI or Webpack 4-era tooling.
Install markstream-vue2 and only the peers required for the requested features.
Import markstream-vue2/dist/index.css in the app shell.
Avoid Vite-style ?worker imports.
Use createKaTeXWorkerFromCDN(...) and createMermaidWorkerFromCDN(...) when workers are needed.
Prefer stable code block defaults over brittle Monaco wiring.
MarkdownCodeBlockNode plus stream-markdown is safer than Monaco in Webpack 4-era repos.
Validate with the smallest useful local dev or build command.
Default Decisions
Treat Monaco and worker-heavy setups as opt-in and fragile on Webpack 4.
Prefer CDN workers over bundler workers for Mermaid and KaTeX.
Keep the Vue 2 composition-api shim explicit when the repo is on Vue 2.6.
Useful Doc Targets
docs/guide/vue2-quick-start.md
docs/guide/vue2-installation.md
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