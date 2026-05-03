---
rating: ⭐⭐
title: rspack-v2-upgrade
url: https://skills.sh/rstackjs/agent-skills/rspack-v2-upgrade
---

# rspack-v2-upgrade

skills/rstackjs/agent-skills/rspack-v2-upgrade
rspack-v2-upgrade
Installation
$ npx skills add https://github.com/rstackjs/agent-skills --skill rspack-v2-upgrade
SKILL.md
Rspack 1.x to v2 Upgrade
Workflow

Confirm current setup

Read package.json to identify Rspack packages in use.
Locate the Rspack config file (commonly rspack.config.(ts|js|mjs|cjs)).

Open the official migration guide

Use the official guide as the single source of truth:
https://rspack.rs/guide/migration/rspack_1.x

Plan required changes

Compare the current project config with the migration guide.
List breaking changes that apply to the project’s current config and plugins.
Note any removed or renamed options, defaults, or plugin APIs.

Update dependencies

Upgrade Rspack packages to v2: @rspack/core, @rspack/cli, @rspack/dev-server, @rspack/plugin-react-refresh.

Apply migration changes

Update the Rspack config and related code according to the official guide.
Remove deprecated or unsupported options.

Validate

Run build and dev commands.
Run project tests or type checks.
Fix any warnings or errors surfaced by the new version.
Weekly Installs
171
Repository
rstackjs/agent-skills
GitHub Stars
65
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass