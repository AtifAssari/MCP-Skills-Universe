---
rating: ⭐⭐
title: servicenow-agent-skills
url: https://skills.sh/aatrey882/servicenow-agent-skills/servicenow-agent-skills
---

# servicenow-agent-skills

skills/aatrey882/servicenow-agent-skills/servicenow-agent-skills
servicenow-agent-skills
Installation
$ npx skills add https://github.com/aatrey882/servicenow-agent-skills --skill servicenow-agent-skills
SKILL.md
ServiceNow Agent Skills Suite

This is a multi-skill suite. Each sub-skill contains its own SKILL.md with hard rules, reference files, and example assets. Do not pre-load all sub-skills. Read only the one that matches the current task.

Sub-Skill Router
Task Signal	Sub-Skill to Read
.now.ts files, Fluent SDK imports, @servicenow/sdk/core, Table/ACL/BusinessRule metadata, now.config.json	./sn-sdk-fluent/SKILL.md
GlideRecord, Script Includes, Business Rules (legacy), Client Scripts, g_form, g_user, gs.log	./sn-scripting/SKILL.md
now-sdk CLI commands, project scaffolding, OAuth/Basic auth setup, environment configuration	./sn-sdk-setup/SKILL.md
Hard Rules
Route before generating. Identify the workspace type (Fluent SDK vs. legacy scripting vs. setup) and read the matching sub-skill's SKILL.md before writing any code.
Never mix paradigms. If the workspace contains now.config.json or .now.ts files, the project uses the Fluent SDK — do not generate GlideRecord code. If the workspace has no Fluent markers, use sn-scripting.
One sub-skill per task. Each sub-skill has its own reference files and examples. Read from the active sub-skill only — do not cross-reference between them unless explicitly directed by that skill's instructions.
Weekly Installs
11
Repository
aatrey882/servi…t-skills
GitHub Stars
12
First Seen
7 days ago
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykWarn