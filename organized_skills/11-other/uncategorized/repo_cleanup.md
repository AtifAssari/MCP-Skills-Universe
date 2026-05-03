---
rating: ⭐⭐
title: repo-cleanup
url: https://skills.sh/nickcrew/claude-ctx-plugin/repo-cleanup
---

# repo-cleanup

skills/nickcrew/claude-ctx-plugin/repo-cleanup
repo-cleanup
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill repo-cleanup
SKILL.md
Repo Cleanup
Overview

Establish a safe, repeatable cleanup workflow for code, dependencies, docs, tests, and sprint artifacts. Minimize risk by validating usage, archiving before deletion, and verifying with tests.

When to Use
Repository bloat (generated artifacts, caches, unused files)
Dead code or unused dependencies suspected
Docs drifted from actual behavior
Tests are brittle, redundant, or mislocated
Sprint closure needs structured archiving

Avoid when:

Active incident response is ongoing
The target area lacks owners or rollback coverage
Quick Reference
Task	Load reference
Code cleanup	skills/repo-cleanup/references/code-cleanup.md
Dependency cleanup	skills/repo-cleanup/references/deps-cleanup.md
Docs cleanup	skills/repo-cleanup/references/docs-cleanup.md
Test cleanup	skills/repo-cleanup/references/test-cleanup.md
Sprint archive	skills/repo-cleanup/references/archive-sprint.md
Workflow
Define scope and safety mode (safe vs aggressive).
Capture baseline state (git status, key tests, backups).
Load the relevant reference file(s) for the target area.
Execute cleanup steps with usage checks before removal.
Validate changes (tests, build, lint, or doc checks).
Report outcomes (actions taken, risks, follow-ups).
Output
Summary of actions and files touched
Validation results and remaining risks
Follow-up recommendations or backlog items
Common Mistakes
Deleting without confirming usage or regenerability
Skipping baseline tests and rollback checkpoints
Removing dependencies without updating build/test scripts
Collapsing docs without preserving entry points
Weekly Installs
78
Repository
nickcrew/claude…x-plugin
GitHub Stars
15
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass