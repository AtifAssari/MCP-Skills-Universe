---
rating: ⭐⭐
title: markstream-react
url: https://skills.sh/simon-he95/markstream-vue/markstream-react
---

# markstream-react

skills/simon-he95/markstream-vue/markstream-react
markstream-react
Installation
$ npx skills add https://github.com/simon-he95/markstream-vue --skill markstream-react
SKILL.md
Markstream React

Use this skill when the host app is React or Next and the task is to wire Markstream safely.

Workflow
Confirm the repo is React, Next, or another React-based host.
Install markstream-react plus only the requested optional peers.
Import markstream-react/index.css from the app shell or client entry.
Start with content.
Move to nodes plus final only when the UI receives streaming or high-frequency updates.
Respect SSR boundaries in Next.
Prefer use client, dynamic imports with ssr: false, or other client-only boundaries when browser-only peers are involved.
Use scoped Markstream overrides before custom parser work.
Validate with the smallest useful dev, build, or typecheck command.
Default Decisions
Renderer wiring first, migration cleanup second.
If the repo already uses react-markdown, pair this skill with markstream-migration.
Prefer the smallest client-only boundary that solves the SSR issue.
Useful Doc Targets
docs/guide/react-quick-start.md
docs/guide/react-installation.md
docs/guide/react-markdown-migration.md
docs/guide/component-overrides.md
Weekly Installs
24
Repository
simon-he95/mark…ream-vue
GitHub Stars
2.3K
First Seen
Mar 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass