---
rating: ⭐⭐
title: vite-browser
url: https://skills.sh/maplecity1314/vite-browser/vite-browser
---

# vite-browser

skills/maplecity1314/vite-browser/vite-browser
vite-browser
Installation
$ npx skills add https://github.com/maplecity1314/vite-browser --skill vite-browser
SKILL.md
vite-browser

Route to one focused skill as early as possible. Do not run all skills by default.

Skill routing
General app bug, component/state confusion, unknown broken UI:
skills/vite-browser-core-debug/SKILL.md
HMR/reload loops, recent code change caused failure, full reloads, stack mapping, "which update caused this":
skills/vite-browser-runtime-diagnostics/SKILL.md
API/data mismatch, request failures, wrong payload, auth/cookie/CORS regressions:
skills/vite-browser-network-regression/SKILL.md
Pre-merge/pre-release final verification:
skills/vite-browser-release-smoke/SKILL.md
Routing rules
Start with core-debug when the symptom is broad or unclear.
Switch immediately to runtime-diagnostics if the issue is tied to a recent edit, HMR, refresh, reload, or Vite runtime instability.
Switch to network-regression if the main symptom is bad data, missing data, request failure, or request/response mismatch.
Use release-smoke only for final validation or sign-off, not root-cause discovery.

If two skills apply:

core-debug -> runtime-diagnostics
core-debug -> network-regression
runtime-diagnostics -> network-regression only if runtime diagnosis suggests the visible failure is downstream of an API problem
Shared bootstrap for all routed skills
vite-browser open <url>
vite-browser detect
vite-browser errors --mapped --inline-source
vite-browser logs


Treat errors --mapped --inline-source as the primary error read when reproducing live runtime failures in v0.3.3+. It can surface browser-side runtime errors even when the Vite overlay is absent, and its output now pairs more reliably with propagation diagnosis in live Vue repros.

Then continue with the selected specialized skill and stop using the router skill.

Command groups (current CLI)
Browser
vite-browser open <url> [--cookies-json <file>]
vite-browser close
vite-browser goto <url>
vite-browser back
vite-browser reload

Framework
vite-browser detect
vite-browser vue tree [id]
vite-browser vue pinia [store]
vite-browser vue router
vite-browser react tree [id]
vite-browser react store list
vite-browser react store inspect <name>
vite-browser react hook health
vite-browser react hook inject
vite-browser react commits [--limit <n>]
vite-browser react commits clear
vite-browser svelte tree [id]

Runtime and Diagnosis
vite-browser vite runtime
vite-browser vite hmr
vite-browser vite hmr trace --limit <n>
vite-browser vite hmr clear
vite-browser vite module-graph [--filter <txt>] [--limit <n>]
vite-browser vite module-graph trace [--filter <txt>] [--limit <n>]
vite-browser vite module-graph clear
vite-browser errors --mapped --inline-source
vite-browser correlate errors [--window <ms>]
vite-browser correlate errors --mapped --inline-source
vite-browser correlate renders [--window <ms>]
vite-browser diagnose propagation [--window <ms>]
vite-browser diagnose hmr [--window <ms>] [--limit <n>]

Utilities
vite-browser network [idx]
vite-browser screenshot
vite-browser eval <script>


Install CLI:

npm install -g @presto1314w/vite-devtools-browser
npx playwright install chromium


Install skill:

npx skills add MapleCity1314/vite-browser

Weekly Installs
14
Repository
maplecity1314/v…-browser
GitHub Stars
8
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn