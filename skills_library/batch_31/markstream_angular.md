---
title: markstream-angular
url: https://skills.sh/simon-he95/markstream-vue/markstream-angular
---

# markstream-angular

skills/simon-he95/markstream-vue/markstream-angular
markstream-angular
Installation
$ npx skills add https://github.com/simon-he95/markstream-vue --skill markstream-angular
SKILL.md
Markstream Angular

Use this skill when the host app is Angular and the task is to adopt the Angular package cleanly.

Workflow
Confirm the repo is Angular.
Install markstream-angular plus only the requested optional peers.
Import markstream-angular/index.css from the app shell.
Add katex/dist/katex.min.css when math is enabled.
Prefer standalone Angular integration.
Use MarkstreamAngularComponent in imports and keep examples signal-friendly.
Start with [content].
Use [final], [codeBlockStream], and other streaming inputs only when the UI actually streams.
Use [customHtmlTags] and [customComponents] for trusted tag workflows.
Validate with the smallest useful Angular dev or build command.
Default Decisions
Standalone Angular first, NgModule-era patterns only when the repo still depends on them.
Treat streaming flags as opt-in.
Keep optional peers minimal and explicit.
Useful Doc Targets
docs/guide/angular-quick-start.md
docs/guide/angular-installation.md
docs/guide/playground.md
docs/guide/troubleshooting.md
Weekly Installs
22
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