---
rating: ⭐⭐
title: mb-review
url: https://skills.sh/mrvladd-d/memobank/mb-review
---

# mb-review

skills/mrvladd-d/memobank/mb-review
mb-review
Installation
$ npx skills add https://github.com/mrvladd-d/memobank --skill mb-review
SKILL.md
mb-review — Multi-expert Memory Bank review
What it does: runs independent reviewers over architecture, scope, backlog, security, and Memory Bank discipline.
Use it when: you need a clean review gate before execution, after bootstrap, or before trusting the docs.
Input: an existing .memory-bank/.
Output: reviewer reports in .tasks/TASK-MB-REVIEW/ plus a synthesized list of fixes and review verdicts.
Goal

Detect gaps, contradictions, broken traceability, and non-compliance early.

Preconditions
.memory-bank/ exists.
Process
1) Create review task folder

Create:

.tasks/TASK-MB-REVIEW/
2) Spawn reviewers (fresh contexts)

Spawn these subagents in parallel (max 5–7):

Architect — ./agents/shared-review-architect.md
Scope/RTM — ./agents/shared-review-scope.md
Plan/backlog — ./agents/shared-review-plan.md
Security — ./agents/shared-review-security.md
MBB compliance — ./agents/shared-mb-reviewer.md
Code quality (conditional: if repo has code) — ./agents/shared-review-code.md

Each reviewer must:

write a detailed report to .tasks/TASK-MB-REVIEW/
return only a short summary + verdict to the orchestrator
3) Synthesize and decide

As orchestrator:

combine findings
deduplicate
rank issues P0–P3
produce a concrete fix plan

If the repo is preparing for /autonomous:

treat unresolved P0/P1 issues as blocking
do not allow batch execution until the final verdict is APPROVE
4) Gate

If any reviewer returns REJECT:

fix MB
re-run mb-review
Definition of done
.tasks/TASK-MB-REVIEW/ contains the reviewer reports.
Orchestrator produced an actionable prioritized fix list.
Final verdict: APPROVE.
Weekly Installs
29
Repository
mrvladd-d/memobank
GitHub Stars
39
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass