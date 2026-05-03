---
title: coding
url: https://skills.sh/bout3fiddy/agents/coding
---

# coding

skills/bout3fiddy/agents/coding
coding
Installation
$ npx skills add https://github.com/bout3fiddy/agents --skill coding
SKILL.md
Coding (Implementation + Review)

Use this skill when the primary intent is implementation, bug fixing, refactoring, code-quality review, or technical guidance for repository code changes.

Scope and routing
Use this skill for code edits, code-quality reviews, PR feedback loops, and infra/platform implementation tasks.
If the request is planning/spec/lifecycle management, hand off to planning.
If the request is AGENTS architecture housekeeping, hand off to housekeeping.
If the request is under skills/ or edits SKILL.md, hand off to skill-creator.
For frontend framework guidance, use SolidJS references only (skills/coding/references/solidjs/...).
Mandatory smell baseline (always for code changes)

For implementation/bugfix/refactor/review operations, always open:

skills/coding/references/code-smells/index.md
skills/coding/references/code-smells/detection-signals.md

Then open specific smell files for detailed refactor guidance when detection signals match. When writing new code (not just editing), err on the side of reading more smell refs — it is cheaper to check and dismiss than to miss a smell.

Core workflow
Confirm scope, constraints, and acceptance criteria.
Load mandatory smell baseline refs.
Load domain refs relevant to the task.
Read only necessary code paths.
Implement minimal focused changes.
Self-review: check your own output against detection signals. Fix violations before presenting — especially Duplicate Code, Speculative Generality, and Long Method, which are easy to introduce organically.
Validate with targeted checks/tests.
Summarize changes, validations, and remaining risks.
Domain reference triggers (open when clearly relevant)
Code smell / maintainability / quality diagnostics:
skills/coding/references/code-smells/index.md
skills/coding/references/code-smells/smells/index.md
Work-package refactoring execution:
skills/coding/references/refactoring/index.md
SolidJS implementation/performance:
skills/coding/references/solidjs/index.md
skills/coding/references/solidjs/rules/index.md
Infra / deploy / platform ops:
skills/coding/references/platform-engineering/index.md
Auth / credentials / secret handling:
skills/coding/references/secrets-and-auth-guardrails.md
PR review bot loop / CI failure remediation:
skills/coding/references/gh-pr-review-fix.md
JS/TS runtime and toolchain:
skills/coding/references/bun.md
Quality rules
Prefer hard cutovers over fallback-first compatibility branches.
Avoid over-defensive code that obscures normal control flow.
Preserve existing architecture unless the task explicitly asks for structural change.
Add/update tests when behavior changes.
Keep edits small, cohesive, and traceable to the request.
Output expectations
Explain decisions and key trade-offs.
List changed files.
Report validations run (or why skipped).
Call out unresolved risks and follow-up actions.
Weekly Installs
61
Repository
bout3fiddy/agents
GitHub Stars
35
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn