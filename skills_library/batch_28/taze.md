---
title: taze
url: https://skills.sh/hairyf/skills/taze
---

# taze

skills/hairyf/skills/taze
taze
Installation
$ npx skills add https://github.com/hairyf/skills --skill taze
SKILL.md

The skill is based on taze (latest README on GitHub) as of 2026-02-24.

taze is a lightweight CLI for upgrading dependencies in JavaScript/TypeScript projects and monorepos. It focuses on safe-by-default version bumps, powerful filtering, and configuration via flags or taze.config.(js|ts) so agents can orchestrate dependency maintenance workflows.

This skill is written for agents that:

Need to review or perform dependency upgrades using taze
Work in monorepos and must keep workspace packages in sync
Must follow safety policies around tests, lint/typecheck, and upgrade strategy
Core References
Topic	Description	Reference
Overview & CLI modes	taze goals, install-free usage, major/minor/patch modes	core-overview
Monorepo support	-r recursive mode, workspaces, local packages	core-monorepo
Features
Configuration & Filtering
Topic	Description	Reference
Config file usage	taze.config.js/ts, defineConfig, options mapping	features-config-file
Filters & peer deps	--include/--exclude, locked deps, --peer, dep fields	features-filters-and-peer-deps
Best Practices & Upgrade Policy
Topic	Description	Reference
Safe upgrade workflow	When to upgrade, required checks (tests, e2e, lint, typecheck), major-default policy with fallback	best-practices-upgrade-strategy
Weekly Installs
56
Repository
hairyf/skills
GitHub Stars
15
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass