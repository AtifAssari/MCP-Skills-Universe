---
rating: ⭐⭐
title: logosdx
url: https://skills.sh/logosdx/monorepo/logosdx
---

# logosdx

skills/logosdx/monorepo/logosdx
logosdx
Installation
$ npx skills add https://github.com/logosdx/monorepo --skill logosdx
SKILL.md
LogosDX Skill

Use this skill for LogosDX setup and integration. Read only the reference file(s) needed for the task.

Quick Start
Identify package scope (dom, fetch, hooks, localize, observer, state-machine, storage, react, utils).
Open the matching file from references/.
Implement with strict typing and lifecycle cleanup.
Run project checks (typecheck/tests) before finishing.
Critical Rules
Define type shapes first (headers, params, state, events, storage schema, locale shape).
Use attempt()/attemptSync() for all I/O and error-prone operations — storage, fetch, invoke sources, queue processors, DOM mutations. Never use try-catch. The error tuple is the only sanctioned error handling pattern (see references/utils.md).
Always clean up resources (cleanup(), off(), destroy()).
Keep React hook methods at component top level only.
Task Routing
Task	Reference
DOM manipulation, CSS, attributes, events, behaviors, viewport	references/dom.md
Lifecycle hooks, middleware, plugins, priority chains	references/hooks.md
HTTP client, retry, cache, dedupe, rate-limit, lifecycle events	references/fetch.md
i18n, translations, ICU pluralization, Intl formatting, locale switching	references/localize.md
Typed events, async generators, queues, observation, relay	references/observer.md
Finite state machines, guards, async invoke, StateHub coordination	references/state-machine.md
Storage CRUD, key scoping, events, custom drivers	references/storage.md
React factories, hooks, provider composition, API hooks	references/react.md
Error tuples, flow control, memoization, typed helpers, unit conversion	references/utils.md
Cross-package design (start here, then open package-specific files)	references/REFERENCE.md
Weekly Installs
13
Repository
logosdx/monorepo
GitHub Stars
8
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass