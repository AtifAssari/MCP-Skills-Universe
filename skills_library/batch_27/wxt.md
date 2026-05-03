---
title: wxt
url: https://skills.sh/timeraa/skills/wxt
---

# wxt

skills/timeraa/skills/wxt
wxt
Installation
$ npx skills add https://github.com/timeraa/skills --skill wxt
SKILL.md
WXT - Browser Extension Framework
When to Use

Apply this skill when:

Project has wxt.config.ts in root
Code uses defineBackground, defineContentScript, defineUnlistedScript
package.json has wxt as a dependency
Entrypoints directory contains extension entry files
Code imports from #imports or wxt/*
Quick Reference
Topic	Reference
Configuration, manifest, env vars, TypeScript	references/config.md
Entrypoints (background, HTML pages, unlisted)	references/entrypoints.md
Content scripts (UI, main world, SPA)	references/content-scripts.md
Storage API, defineItem, migrations, watchers	references/storage.md
Messaging (cross-context communication)	references/messaging.md
Testing with WxtVitest and fakeBrowser	references/testing.md
WXT modules (using and creating)	references/modules.md
Multi-browser builds and runtime detection	references/multi-browser.md
Vue, React, Svelte, Solid setup	references/frontend-frameworks.md
Common patterns and anti-patterns	references/patterns.md
Most Common Pattern
// entrypoints/background.ts
export default defineBackground({
  main() {
    // ALL runtime code must be inside main() - cannot be async
    browser.runtime.onInstalled.addListener(() => {
      console.log('Extension installed');
    });
  },
});


Critical: main() cannot be async. Code outside main() runs at build time in Node.js.

Weekly Installs
17
Repository
timeraa/skills
GitHub Stars
3
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn