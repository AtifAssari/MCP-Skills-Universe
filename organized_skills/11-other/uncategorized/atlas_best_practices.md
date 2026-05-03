---
rating: ⭐⭐⭐
title: atlas-best-practices
url: https://skills.sh/0xbigboss/claude-code/atlas-best-practices
---

# atlas-best-practices

skills/0xbigboss/claude-code/atlas-best-practices
atlas-best-practices
Installation
$ npx skills add https://github.com/0xbigboss/claude-code --skill atlas-best-practices
SKILL.md
Atlas Best Practices

Atlas supports declarative and versioned schema workflows. Keep this file minimal and load only the reference file needed for the current task.

Workflow Selection
Use declarative workflow when desired schema state is the source of truth.
Use versioned workflow when migration files are required for auditing and staged deployments.
Use baseline workflow when onboarding an existing database.
Default Execution Flow
Confirm the target env in atlas.hcl.
Confirm dev is configured and isolated from production.
Plan first, then lint/test/validate, then apply.
Run production changes through CI/CD or approved deployment workflow.
Quick Commands
# Declarative
atlas schema apply --env local

# Versioned
atlas migrate diff add_change --env local
atlas migrate lint --env local --latest 1
atlas migrate apply --env local

# Integrity
atlas migrate validate --env local
atlas migrate status --env local

Reference Map
core-workflows.md Use for environment config, schema-as-code patterns, declarative vs versioned workflows, baselining, and ORM provider loading.
safety-and-quality.md Use for lint analyzers, transaction modes, schema tests, pre-execution checks, and CI patterns.
atlas-v1-1-features.md Use for Atlas v1.1 coverage (released on 2026-02-03), including security as code, declarative data, new drivers/platform support, Slack integration, schema exporters, and MySQL TLS.
cli-agent-gaps.md Use for Atlas CLI capabilities and edge cases agents often miss: planning workflows, migration directory maintenance commands, URL/TLS pitfalls, feature availability, and version policy constraints.
Guardrails
Keep credentials out of source files; prefer Atlas data sources and input variables.
Require explicit review for destructive or data-dependent migrations.
Fail loudly on unsupported drivers, missing dev URLs, or unknown environment names.
Weekly Installs
119
Repository
0xbigboss/claude-code
GitHub Stars
43
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn