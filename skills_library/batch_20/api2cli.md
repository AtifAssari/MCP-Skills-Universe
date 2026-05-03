---
title: api2cli
url: https://skills.sh/melvynx/api2cli/api2cli
---

# api2cli

skills/melvynx/api2cli/api2cli
api2cli
Installation
$ npx skills add https://github.com/melvynx/api2cli --skill api2cli
SKILL.md
api2cli

Turn any REST API into a standardized, agent-ready CLI.

Always use npx api2cli to run commands. Always use --json when calling generated CLIs programmatically.

Prerequisites
bun --version || curl -fsSL https://bun.sh/install | bash

Workflow

Follow all steps in order — do not skip any.

1. Search the registry first

Before generating anything, check if a CLI already exists:

npx api2cli search <query>


If the registry already has the CLI you need, install it instead of rebuilding it:

npx api2cli install <name>


See references/commands.md for filters like --type, --category, and --json.

2. Discover the API

Find the API docs or OpenAPI spec. Identify: base URL, auth type, auth header, all resources and endpoints.

3. Create the scaffold
npx api2cli create <app> --base-url <url> --auth-type bearer


See references/create.md for all flags and what gets generated.

4. Implement resources

Create ~/.cli/<app>-cli/src/resources/<resource>.ts for each API resource. Register in src/index.ts.

See references/resource-patterns.md for the CRUD template and library API.

5. Build, link, and test
npx api2cli bundle <app>
npx api2cli link <app>
<app>-cli --help
<app>-cli <resource> list --json


api2cli link adds ~/.local/bin to PATH automatically. No export PATH needed.

6. Finalize skill and README

This step is mandatory. The skill must become a real operating guide for another agent, not just a command list — no placeholders, no TODOs.

Introspect the CLI: run <app>-cli --help, then <resource> --help and <resource> <action> --help for every resource and action
Update the description: list all resource names and add domain-specific trigger phrases
Set the category: replace {{CATEGORY}} with the correct value (e.g. social-media, email, devtools)
Write the task-oriented sections: replace {{WHEN_TO_USE_HELP}}, {{CAPABILITIES_HELP}}, and {{USE_CASES_HELP}} with domain-specific guidance
Build resource tables: for each resource, create a command table with every action and its real flags (from --help output)
Add Quick Reference + Output Format: include --help commands and document the JSON envelope
Remove all placeholders: no {{...}} or <!-- TODO --> should remain
Validate: run at least one command to confirm the skill's examples are accurate

See references/skill-generation.md for the full introspection workflow, format, quality checklist, and symlink instructions.

To also link skills for OpenClaw:

npx api2cli link <app> --openclaw


See references/openclaw.md for the one-prompt setup, ClawHub publishing, API key auto-detection, and custom --skills-path usage.

Also available on ClawHub: npx clawhub install api2cli

7. Publish (when user asks)

Before any publish target, run these pre-flight checks:

Verify gh CLI is authenticated: run gh auth status. If not logged in, ask the user to run gh auth login first. Stop and wait.
Check if the CLI is already on GitHub: run git remote get-url origin in the CLI directory.
If no remote exists → the CLI is not on GitHub yet. Automatically run the GitHub publish flow first (see below) before proceeding to npm or registry publish.
If a remote exists → already on GitHub, continue.
To GitHub

Push the CLI to a public GitHub repo.

See references/publish-to-github.md for pre-flight checks, repo creation, and push workflow.

To npm

Requires the CLI to be on GitHub first (for repository field in package.json). If not on GitHub, run the GitHub publish flow above first.

Publish the CLI to the npm registry so users can npm i -g <name> or npx <name>.

See references/publish-to-npm.md for auth, package.json validation, build, verify, and publish workflow. Also see references/package-checklist.md for the field-by-field package.json reference.

To ClawHub

Publish the generated skill to ClawHub so OpenClaw users can discover and install it.

Auth: run npx clawhub login. If not authenticated, ask the user to complete login first. Stop and wait.
Push the skill: run npx clawhub publish <cli-dir>/skills/<app>-cli --slug <app>-cli
After publish, users can install with:
npx clawhub install <app>-cli


See references/openclaw.md for the full OpenClaw setup workflow.

To Sundial Hub

Publish the generated skill to the Sundial Hub so any agent (Claude Code, Cursor, Codex, etc.) can install it.

Auth: run npx sundial-hub auth status. If not authenticated, ask the user to run npx sundial-hub auth login first. Stop and wait.
Push the skill: run npx sundial-hub push <cli-dir>/skills/<app>-cli --visibility public --categories coding
After publish, users can install with:
npx sundial-hub add <sundial-username>/<app>-cli

To api2cli.dev registry

Requires the CLI to be on GitHub first. If not on GitHub, run the GitHub publish flow above first.

Register on api2cli.dev so others can install with npx api2cli install <name>.

See references/publish.md for the registry publish workflow.

Conventions
<app>-cli <resource> <action> [flags]
<app>-cli auth set|show|remove|test


--json returns: { "ok": true, "data": [...], "meta": { "total": 42 } }

Other flags: --format <text|json|csv|yaml>, --verbose, --no-color, --no-header

Exit codes: 0 = success, 1 = API error, 2 = usage error

Tokens: ~/.config/tokens/<app>-cli.txt (chmod 600)

Weekly Installs
99
Repository
melvynx/api2cli
GitHub Stars
26
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn