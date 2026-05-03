---
rating: ⭐⭐
title: coding-guidelines-verify
url: https://skills.sh/jmerta/codex-skills/coding-guidelines-verify
---

# coding-guidelines-verify

skills/jmerta/codex-skills/coding-guidelines-verify
coding-guidelines-verify
Installation
$ npx skills add https://github.com/jmerta/codex-skills --skill coding-guidelines-verify
SKILL.md
Coding guidelines verifier
Goal

Validate that changes follow the nearest nested AGENTS.md:

default: changed files only
default: auto-fix formatting before lint/tests
monorepo-aware: each module’s AGENTS.md is the source of truth for that scope
Workflow (checklist)
Collect changed files (staged + unstaged + untracked).
For each changed file, find the nearest parent AGENTS.md.
If a file has no scoped AGENTS.md, report it (suggest running coding-guidelines-gen).
Parse the codex-guidelines block (schema: references/verifiable-block.md).
Run, per scope:
format (auto-fix) -> lint -> tests
apply simple forbid rules (globs/regex) from the block
Produce a short compliance report (template: references/report-template.md).
Automation

Use scripts/verify_guidelines.py to group scopes, run commands, and report results.

If python is not available or the script fails, tell the user and ask whether to install Python or proceed with a manual per-scope verification.
Deliverable

Provide:

The per-scope compliance report (use references/report-template.md).
Any auto-fix formatting changes applied.
Lint/test commands run and their results, plus any violations.
Weekly Installs
24
Repository
jmerta/codex-skills
GitHub Stars
126
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass