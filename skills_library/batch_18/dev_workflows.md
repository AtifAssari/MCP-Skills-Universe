---
title: dev-workflows
url: https://skills.sh/nickcrew/claude-ctx-plugin/dev-workflows
---

# dev-workflows

skills/nickcrew/claude-ctx-plugin/dev-workflows
dev-workflows
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill dev-workflows
SKILL.md
Dev Workflows
Overview

Unify build, test, and DX improvement workflows so they are repeatable and reliable. Focus on safe execution, clear diagnostics, and actionable follow-ups.

When to Use
Running builds or resolving build failures
Executing tests or analyzing test failures
Improving onboarding, tooling, or developer workflows

Avoid when:

The task is pure code implementation
A full release process is required (use release-prep)
Quick Reference
Task	Load reference
Build workflows	skills/dev-workflows/references/build.md
Test workflows	skills/dev-workflows/references/test.md
DX improvements	skills/dev-workflows/references/dx.md
Workflow
Select the workflow type: build, test, or DX.
Load the matching reference file.
Execute with monitoring and capture diagnostics.
Apply fixes or improvements as needed.
Verify outcomes and document next steps.
Output
Execution summary (status, errors, next steps)
Suggested follow-ups or improvements
Common Mistakes
Skipping baseline environment checks
Running tests without capturing failing output
Changing DX workflows without documenting impact
Weekly Installs
50
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