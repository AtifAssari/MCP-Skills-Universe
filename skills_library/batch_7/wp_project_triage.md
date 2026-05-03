---
title: wp-project-triage
url: https://skills.sh/wordpress/agent-skills/wp-project-triage
---

# wp-project-triage

skills/wordpress/agent-skills/wp-project-triage
wp-project-triage
Installation
$ npx skills add https://github.com/wordpress/agent-skills --skill wp-project-triage
Summary

Deterministic WordPress repository inspection with structured JSON output for workflow guidance.

Detects project kind (plugin, theme, block theme, WP core, Gutenberg, full site) and outputs a schema-validated JSON report including tooling, tests, and version hints
Runs via Node.js detector script at repo root; outputs project.kind, signals, and tooling fields to guide downstream workflows
Identifies PHP/Node tooling presence and test frameworks to inform which commands and conventions apply before making changes
Targets WordPress 6.9+ with PHP 7.2.24+; re-run after structural changes like adding theme.json or block.json
SKILL.md
WP Project Triage
When to use

Use this skill to quickly understand what kind of WordPress repo you’re in and what commands/conventions to follow before making changes.

Inputs required
Repo root (current working directory).
Procedure
Run the detector (prints JSON to stdout):
node skills/wp-project-triage/scripts/detect_wp_project.mjs
If you need the exact output contract, read:
skills/wp-project-triage/references/triage.schema.json
Use the report to select workflow guardrails:
project kind(s)
PHP/Node tooling present
tests present
version hints and sources
If the report is missing signals you need, update the detector rather than guessing.
Verification
The JSON should parse and include: project.kind, signals, and tooling.
Re-run after changes that affect structure/tooling (adding theme.json, block.json, build config).
Failure modes / debugging
If it reports unknown, check whether the repo root is correct.
If scanning is slow, add/extend ignore directories in the script.
Weekly Installs
1.2K
Repository
wordpress/agent-skills
GitHub Stars
1.4K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass