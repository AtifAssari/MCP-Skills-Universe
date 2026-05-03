---
title: markstream-nuxt
url: https://skills.sh/simon-he95/markstream-vue/markstream-nuxt
---

# markstream-nuxt

skills/simon-he95/markstream-vue/markstream-nuxt
markstream-nuxt
Installation
$ npx skills add https://github.com/simon-he95/markstream-vue --skill markstream-nuxt
SKILL.md
Markstream Nuxt

Use this skill when the host app is Nuxt and SSR boundaries matter.

Workflow
Confirm the repo is Nuxt 3 or 4.
Install markstream-vue plus only the optional peers required by the requested features.
Keep browser-only peers behind client-only boundaries.
Prefer <client-only> wrappers, .client plugins, or guarded setup paths.
Import markstream-vue/index.css from a client-safe app shell or plugin.
Start with content, and move to nodes plus final only when the UI is streaming.
Validate with the smallest relevant Nuxt dev, build, or typecheck command.
Default Decisions
SSR safety comes before feature completeness.
Avoid import-time access to browser globals from server code paths.
Treat Monaco, Mermaid workers, and similar heavy peers as client-only unless the repo already has a proven SSR pattern.
Useful Doc Targets
docs/nuxt-ssr.md
docs/guide/installation.md
docs/guide/usage.md
docs/guide/troubleshooting.md
Weekly Installs
29
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