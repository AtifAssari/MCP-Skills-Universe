---
rating: ⭐⭐
title: pma-bun
url: https://skills.sh/zzci/skills/pma-bun
---

# pma-bun

skills/zzci/skills/pma-bun
pma-bun
Installation
$ npx skills add https://github.com/zzci/skills --skill pma-bun
SKILL.md
Bun Project Implementation Guide

Use this skill together with /pma. /pma controls workflow, approval, and task tracking; this guide defines the implementation baseline after approval.

Keep this entry file small. Load only the relevant reference packs.

Scope

For PMA-managed Bun backends, API services, and internal tools. A SPA shipped alongside the API (same repo) is supported via a sibling web/ directory and pma-web — it does not require a Bun workspace.

Not for frontend-only SPAs, Node-specific runtime guides, or non-PMA workflows.

Loading Order
Always load references/baseline.md first.
Load references/runtime.md for bootstrap flow, config, root resolution, HTTP server, docs, logging, PID lock, and dev/prod split.
Load references/data-and-testing.md for Drizzle, SQLite-first storage, libSQL driver setup, migration fallback, repository patterns, and testing.
Load references/delivery.md for compile flow, embedded assets, CI gates, observability, Docker, security, and Git workflow.
Quick Routing
New project setup or repo restructuring (single API / API + sibling SPA / monorepo): references/baseline.md
app.ts / index.ts / optional dev.ts, OpenAPIHono, config, startup, graceful shutdown, logging, PID lock, Bun-specific nsl invocation: references/runtime.md (full nsl protocol → /pma references/dev-environment.md; multi-app workspace setup → /pma docs/monorepo-example.md)
Schema design, SQLite setup, migration embedding, repositories, test setup: references/data-and-testing.md
Compile pipeline, binary delivery, static assets, CI, Docker, PR readiness: references/delivery.md
Reference Packs
references/baseline.md Scope, layout choice (single API vs monorepo vs API + sibling SPA), required quality gates, scripts, conventions, and implementation workflow.
references/runtime.md Formatting and TypeScript defaults, config loading, bootstrap structure, OpenAPIHono setup, middleware, logging, docs routes, and runtime lifecycle.
references/data-and-testing.md Drizzle with SQLite-first storage, migration strategy, repository boundaries, and testing rules.
references/delivery.md Compile pipeline, security patterns, observability, CI pipeline, Docker, workspace rules, and Git conventions.

If the repository intentionally diverges, keep the deviation explicit in the proposal and consistent across scripts, docs, and CI.

Weekly Installs
80
Repository
zzci/skills
GitHub Stars
2
First Seen
Mar 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass