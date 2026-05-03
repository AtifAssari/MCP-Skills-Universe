---
title: wordpress-router
url: https://skills.sh/wordpress/agent-skills/wordpress-router
---

# wordpress-router

skills/wordpress/agent-skills/wordpress-router
wordpress-router
Installation
$ npx skills add https://github.com/wordpress/agent-skills --skill wordpress-router
Summary

Classify WordPress codebases and route to the correct workflow for plugins, themes, blocks, and core checkouts.

Runs automated project triage to identify repo type (plugin, theme, block theme, Gutenberg blocks, WP core) and available tooling
Outputs classification results and decision tree routing to domain-specific skills based on user intent and project kind
Requires repo root access and bash/Node filesystem operations; some workflows need WP-CLI
Targets WordPress 6.9+ with PHP 7.2.24+; confirms version constraints before delegating to downstream skills
SKILL.md
WordPress Router
When to use

Use this skill at the start of most WordPress tasks to:

identify what kind of WordPress codebase this is (plugin vs theme vs block theme vs WP core checkout vs full site),
pick the right workflow and guardrails,
delegate to the most relevant domain skill(s).
Inputs required
Repo root (current working directory).
The user’s intent (what they want changed) and any constraints (WP version targets, WP.com specifics, release requirements).
Procedure
Run the project triage script:
node skills/wp-project-triage/scripts/detect_wp_project.mjs
Read the triage output and classify:
primary project kind(s),
tooling available (PHP/Composer, Node, @wordpress/scripts),
tests present (PHPUnit, Playwright, wp-env),
any version hints.
Route to domain workflows based on user intent + repo kind:
For the decision tree, read: skills/wordpress-router/references/decision-tree.md.
Apply guardrails before making changes:
Confirm any version constraints if unclear.
Prefer the repo’s existing tooling and conventions for builds/tests.
Verification
Re-run the triage script if you create or restructure significant files.
Run the repo’s lint/test/build commands that the triage output recommends (if available).
Failure modes / debugging
If triage reports kind: unknown, inspect:
root composer.json, package.json, style.css, block.json, theme.json, wp-content/.
If the repo is huge, consider narrowing scanning scope or adding ignore rules to the triage script.
Escalation
If routing is ambiguous, ask one question:
“Is this intended to be a WordPress plugin, a theme (classic/block), or a full site repo?”
Weekly Installs
1.3K
Repository
wordpress/agent-skills
GitHub Stars
1.4K
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass