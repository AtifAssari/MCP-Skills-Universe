---
title: project-docs
url: https://skills.sh/s-hiraoku/synapse-a2a/project-docs
---

# project-docs

skills/s-hiraoku/synapse-a2a/project-docs
project-docs
Installation
$ npx skills add https://github.com/s-hiraoku/synapse-a2a --skill project-docs
SKILL.md
Project Docs

This skill helps you keep documentation correct, minimal, and aligned with the codebase.

What To Document
User-facing behavior changes
New CLI flags, environment variables, configuration changes
Protocol/API changes, request/response shapes
Operational guidance (troubleshooting, limitations, safety workflows)
Doc Update Workflow
Identify the code changes and their user-visible effects.
Locate the canonical docs (README vs guides vs references).
Update docs with minimal churn, matching existing style.
Cross-check examples against current CLI help / code.
Run relevant tests and include them in the update note.
Consistency Checks
Option names match actual CLI flags (--help output if available).
Defaults are correct and stated once (avoid duplication across docs).
Examples are runnable and do not rely on project-private paths.
Terminology is consistent across README/guides/references.
Subagent Invocation (docs-excellence-architect)

Use the Task tool to delegate a doc-focused review to a specialized subagent:

subagent_type: docs-excellence-architect

Provide:

The doc files to touch
The code changes that need to be reflected
The desired doc structure (where each piece should live)

Example prompt:

Review and update docs for the following changes:
- <change 1>
- <change 2>
Target files:
- README.md
- guides/*.md
- docs/*.md
Constraints:
- Minimal churn, match local style
- Ensure examples are accurate and consistent
Deliverables:
- Proposed edits (diff-style)
- A checklist of what was verified

Maintenance Guidelines
Prefer short sections with concrete examples.
Avoid repeating the same definition in multiple files.
When a doc becomes a reference, move it to a single canonical location and link to it.
Weekly Installs
63
Repository
s-hiraoku/synapse-a2a
GitHub Stars
4
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass