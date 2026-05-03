---
rating: ⭐⭐
title: learn-rule
url: https://skills.sh/rohitg00/pro-workflow/learn-rule
---

# learn-rule

skills/rohitg00/pro-workflow/learn-rule
learn-rule
Installation
$ npx skills add https://github.com/rohitg00/pro-workflow --skill learn-rule
SKILL.md
Learn Rule

Capture a lesson from the current session into permanent memory.

Trigger

Use when the user says "remember this", "add to rules", "don't do that again", or after a mistake is identified.

Workflow
Identify the lesson — what mistake was made? What should happen instead?
Format the rule with full context.
Propose the addition and wait for user approval.
After approval, persist to LEARNED section or project memory.
Format
[LEARN] Category: One-line rule
Mistake: What went wrong
Correction: How it was fixed

Categories
Category	Examples
Navigation	File paths, finding code, wrong file edited
Editing	Code changes, patterns, wrong approach
Testing	Test approaches, coverage gaps, flaky tests
Git	Commits, branches, merge issues
Quality	Lint, types, style violations
Context	When to clarify, missing requirements
Architecture	Design decisions, wrong abstractions
Performance	Optimization, O(n^2) loops, memory
Example
Recent mistake: Edited wrong utils.ts file

[LEARN] Navigation: Confirm full path when multiple files share a name.

Add to LEARNED section? (y/n)

Guardrails
Always wait for user approval before persisting.
Keep rules to one line — specific and actionable.
Bad: "Write good code". Good: "Always use snake_case for database columns".
Include the mistake context so the rule makes sense later.
Output
The proposed [LEARN] rule with category
Confirmation after persisting
Weekly Installs
28
Repository
rohitg00/pro-workflow
GitHub Stars
2.0K
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass