---
title: rspress-v2-upgrade
url: https://skills.sh/rstackjs/agent-skills/rspress-v2-upgrade
---

# rspress-v2-upgrade

skills/rstackjs/agent-skills/rspress-v2-upgrade
rspress-v2-upgrade
Installation
$ npx skills add https://github.com/rstackjs/agent-skills --skill rspress-v2-upgrade
SKILL.md
Rspress v1 to v2 Upgrade
Workflow

Confirm current setup

Read package.json to identify Rspress and plugin packages in use.
Locate the Rspress config file (commonly rspress.config.(ts|js|mjs|cjs)).
Check for custom theme files and MDX usage.

Open the official upgrade guide

Use the v1 → v2 guide as the source of truth:
https://rspress.rs/guide/migration/rspress-1-x

Plan the upgrade path

List breaking changes that apply to the project's current config, plugins, and theme.
Note any removed or renamed packages, options, and APIs.

Update dependencies

Replace rspress with @rspress/core@^2.0.0.
Remove packages now built into @rspress/core (e.g. rspress, @rspress/plugin-shiki, @rspress/plugin-auto-nav-sidebar, @rspress/plugin-container-syntax, @rspress/plugin-last-updated, @rspress/plugin-medium-zoom, @rspress/theme-default, @rspress/runtime).
Bump remaining Rspress plugins to latest versions via npx taze major --include /rspress/ -w -r.
Ensure Node.js >= 20.9.0.

Apply config and code changes

Update import paths (rspress/runtime → @rspress/core/runtime, rspress/theme → @rspress/core/theme, @rspress/theme-default → @rspress/core/theme-original).
If the project has a custom theme (in theme directory), use @rspress/core/theme-original to import the original theme components.
Update the Rspress config to match v2 options and defaults.
Remove deprecated or unsupported settings.

Validate

Run the build and dev server.
Fix any warnings or errors that appear in the new version. If errors or warnings occur, please refer to the Official Upgrade Guide and first check if it's caused by any omitted or incomplete migration steps.
Weekly Installs
67
Repository
rstackjs/agent-skills
GitHub Stars
65
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass