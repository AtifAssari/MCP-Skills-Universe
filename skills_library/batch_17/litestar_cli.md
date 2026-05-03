---
title: litestar-cli
url: https://skills.sh/alti3/litestar-skills/litestar-cli
---

# litestar-cli

skills/alti3/litestar-skills/litestar-cli
litestar-cli
Installation
$ npx skills add https://github.com/alti3/litestar-skills --skill litestar-cli
SKILL.md
CLI
Execution Workflow
Ensure app autodiscovery works (canonical module layout) or define explicit app import path.
Standardize litestar commands in project scripts and team docs.
Separate local development commands from production runtime commands.
Extend CLI only when command reuse materially improves team workflows.
Implementation Rules
Keep one canonical entrypoint for commands and deployment.
Avoid hidden env assumptions; make required env vars explicit.
Pin command flags in scripts to avoid accidental behavior drift.
Prefer explicit app targets in CI/CD for reproducibility.
Example Pattern
# Autodiscovery mode
litestar run

# Explicit app target mode
litestar --app path.to.app:app run

Validation Checklist
Confirm litestar run and other core commands resolve the correct app.
Confirm schema-related CLI commands run in CI without manual steps.
Confirm command aliases/scripts behave consistently across environments.
Cross-Skill Handoffs
Use litestar-app-setup when autodiscovery or app factory layout is broken.
Use litestar-openapi for schema generation quality, not just CLI invocation.
Litestar References
https://docs.litestar.dev/latest/usage/cli.html
Weekly Installs
14
Repository
alti3/litestar-skills
GitHub Stars
5
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass