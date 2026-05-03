---
rating: ⭐⭐
title: pma-go
url: https://skills.sh/zzci/skills/pma-go
---

# pma-go

skills/zzci/skills/pma-go
pma-go
Installation
$ npx skills add https://github.com/zzci/skills --skill pma-go
SKILL.md
Go Project Implementation Guide

Use this skill together with /pma. /pma controls workflow, approval, and task tracking; this guide defines the implementation baseline after approval.

Keep this entry file lean. Load only the reference packs needed for the task.

Scope

For PMA-managed Go backends, API services, and CLI applications.

Not for embedded targets, library-only modules without binaries, or non-PMA projects.

Loading Order
Always load references/baseline.md first.
Load references/config-and-data.md for config layering, validation, sqlc, pgx, GORM, and migrations.
Load references/http-and-runtime.md for handlers, middleware, logging, observability, and shutdown.
Load references/delivery.md for lint, tests, task runners, security review, CI, and Git workflow.
Quick Routing
New service or CLI setup: references/baseline.md
koanf config, env mapping, DB access, migrations, repository boundaries: references/config-and-data.md
HTTP server, response envelopes, auth middleware, slog, tracing, shutdown: references/http-and-runtime.md
quality gates, lint, tests, Taskfile, security checklist, CI, PR readiness: references/delivery.md
Reference Packs
references/baseline.md Stack defaults, quality gates, layout, conventions, error model, and code quality standards.
references/config-and-data.md Config layering with koanf, validation, sqlc plus pgx, GORM alternative, and migration rules.
references/http-and-runtime.md Router structure, handler patterns, middleware, logging, observability, and graceful shutdown.
references/delivery.md Lint config, testing, task runner expectations, security checks, CI, and Git conventions.

If the repo already diverges from these defaults, make the divergence explicit and apply it consistently across code, docs, and CI.

Weekly Installs
81
Repository
zzci/skills
GitHub Stars
2
First Seen
Mar 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass