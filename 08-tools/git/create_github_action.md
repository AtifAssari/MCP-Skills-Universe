---
title: create-github-action
url: https://skills.sh/richfrem/agent-plugins-skills/create-github-action
---

# create-github-action

skills/richfrem/agent-plugins-skills/create-github-action
create-github-action
Installation
$ npx skills add https://github.com/richfrem/agent-plugins-skills --skill create-github-action
SKILL.md

Follow the create-github-action skill workflow to scaffold a traditional deterministic GitHub Actions CI/CD workflow (no AI at runtime).

Inputs
$ARGUMENTS — optional workflow type or purpose (e.g. test, build, deploy, lint, release, security). Omit to start with discovery.
Steps
If $ARGUMENTS specifies a workflow type, use it to seed Phase 1 discovery
Follow the create-github-action phased workflow: confirm trigger events, runner OS, required secrets/environment variables, job steps, and caching strategy
Generate the .github/workflows/<name>.yml file
Report the workflow path and setup instructions (secrets to configure, badges, etc.)
Output

.github/workflows/<name>.yml with complete job definitions, trigger events, permissions, and inline comments explaining each step.

Edge Cases
If $ARGUMENTS is empty: begin with workflow type discovery
If the use case involves AI agents at runtime: redirect to create-agentic-workflow
If secrets or environment variables are required: list them explicitly without values
Weekly Installs
22
Repository
richfrem/agent-…s-skills
GitHub Stars
2
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass