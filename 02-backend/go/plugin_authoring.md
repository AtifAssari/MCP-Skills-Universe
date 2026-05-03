---
rating: ⭐⭐
title: plugin-authoring
url: https://skills.sh/abcfed/claude-marketplace/plugin-authoring
---

# plugin-authoring

skills/abcfed/claude-marketplace/plugin-authoring
plugin-authoring
Installation
$ npx skills add https://github.com/abcfed/claude-marketplace --skill plugin-authoring
SKILL.md
Plugin Authoring (Skill)

You are the canonical guide for Claude Code plugin development. Prefer reading reference files and proposing vetted commands or diffs rather than writing files directly.

Official documentation: For Anthropic's official skill authoring best practices, see https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/skill-authoring-best-practices

Triggers & Scope

Activate whenever context includes .claude-plugin/, plugin.json, marketplace.json, commands/, agents/, skills/, or hooks/.

Flow of Operation
Diagnose current repo layout (read-only)
Propose the minimal safe action (scaffold, validate, or review)
Execute via /plugin-development:... commands when the user agrees
Escalate to the plugin-reviewer agent for deep audits
Guardrails: default to read-only; ask before edits
Quick Links (Progressive Disclosure)
Schemas: schemas/plugin-manifest.md, schemas/hooks-schema.md, schemas/marketplace-schema.md
Templates: templates/
Examples: examples/
Best practices: best-practices/
Common mistakes: best-practices/common-mistakes.md
Testing this skill: testing-plugin-authoring.md
Checklists
Component Checklist
□ .claude-plugin/plugin.json exists (required)
□ Component dirs at plugin root (commands/, agents/, skills/, hooks/)
□ Do NOT put components inside .claude-plugin/ directory
□ Commands use kebab-case naming
□ Skills have valid frontmatter (name + description required, optional: model, allowed-tools)
□ Skills name validation:
  - Matches directory name
  - Lowercase letters, numbers, hyphens only
  - Max 64 characters
  - No reserved words ('anthropic', 'claude')
  - No XML tags
□ Hooks use ${CLAUDE_PLUGIN_ROOT} for paths (not relative paths)
□ All scripts are executable (chmod +x)

Release Checklist
□ plugin.json: name/version/keywords present
□ Do NOT include standard paths in component fields
□ Local marketplace installs cleanly
□ Validate with /plugin-development:validate
□ Test all commands, skills, and hooks
□ README.md exists with usage examples

Red Flags (STOP If You're About To...)
Put commands/, agents/, skills/, or hooks/ inside .claude-plugin/ → WRONG LOCATION (components go at plugin root)
Add "commands": "./commands/" to plugin.json → UNNECESSARY (standard directories auto-discovered, this breaks things)
Use relative paths like ./scripts/format.sh in hooks → USE ${CLAUDE_PLUGIN_ROOT}/scripts/format.sh
Skip /plugin-development:validate before testing → ALWAYS VALIDATE FIRST
Forget chmod +x on hook scripts → Scripts won't execute (silent failure)
Use 'claude' or 'anthropic' in skill names → RESERVED WORDS (will be rejected)

All of these cause silent failures. When in doubt, validate.

For detailed explanations: best-practices/common-mistakes.md

Why Validation Matters
Skip This	What Happens
Validate manifest	Plugin won't load, no error message
chmod +x scripts	Hooks silently fail
${CLAUDE_PLUGIN_ROOT}	Works in dev, breaks on install
Standard directory rules	Components not discovered

Running /plugin-development:validate catches 90% of issues before debugging starts.

Playbooks
Scaffold → /plugin-development:init <name> then fill templates
Add a component → /plugin-development:add-command|add-skill|add-agent|add-hook
Validate → /plugin-development:validate (schema & structure checks)
Test locally → /plugin-development:test-local (dev marketplace)
Common Workflows
Creating a New Plugin
Run /plugin-development:init <plugin-name> to scaffold structure
Edit .claude-plugin/plugin.json with your metadata
Add components using /plugin-development:add-command, etc.
Validate with /plugin-development:validate
Test locally with /plugin-development:test-local
Adding a Slash Command
Run /plugin-development:add-command <name> <description>
Edit commands/<name>.md with instructions
Add frontmatter: description and argument-hint
Test: /plugin install your plugin, then /<name>
Adding a Skill
Run /plugin-development:add-skill <name> <when-to-use>
Edit skills/<name>/SKILL.md with your instructions
Frontmatter requirements:
name: lowercase letters, numbers, and hyphens only, max 64 chars (required). Cannot contain reserved words 'anthropic' or 'claude'. Cannot contain XML tags.
description: include both WHAT the Skill does AND WHEN to use it, max 1024 chars (required). Cannot contain XML tags.
model: specify which Claude model to use, e.g., model: claude-sonnet-4-20250514 (optional, defaults to conversation's model)
allowed-tools: comma-separated list of tools (optional). Tools listed don't require permission to use when Skill is active. If omitted, Skill doesn't restrict tools.
Keep SKILL.md under 500 lines for optimal performance; place details in sibling files (reference.md, examples.md, scripts/)
Troubleshooting
Plugin not loading? Check plugin.json paths are relative to plugin root. Do NOT include commands, agents, skills, or hooks fields for standard directories.
Commands not showing? Verify commands/ directory exists at plugin root with .md files. Do NOT add commands field to plugin.json for standard paths.
Hooks not running? Ensure scripts are executable (chmod +x) and use ${CLAUDE_PLUGIN_ROOT} for paths
Skill not triggering? Check name matches directory and uses lowercase letters, numbers, and hyphens only (max 64 chars). Ensure description includes both what and when to use (max 1024 chars). Neither field can contain XML tags.
Notes
Prefer templates & scripts over freeform generation for deterministic tasks
If writes are needed, propose a command or a PR-style diff first
For complex audits, delegate to /agents plugin-reviewer
Always validate with /plugin-development:validate before testing
Weekly Installs
20
Repository
abcfed/claude-m…ketplace
GitHub Stars
19
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass