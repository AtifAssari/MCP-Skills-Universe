---
title: build
url: https://skills.sh/juliusbrussee/cavekit/build
---

# build

skills/juliusbrussee/cavekit/build
build
Installation
$ npx skills add https://github.com/juliusbrussee/cavekit --skill build
SKILL.md
build — implement spec

Single-thread native plan→execute. You are main Claude. No swarm.

LOAD
Read SPEC.md. If missing → tell user to invoke the spec skill first. Stop.
Read FORMAT.md once if not loaded.
Parse invocation args:
§T.n → that task only
--next → lowest-numbered row with status . or ~
--all or empty → every . row in §T order
PLAN

Native plan mode. For chosen task(s):

Cite every §V invariant that applies. Plan must respect all.
Cite every §I interface touched. Plan must preserve shape.
List files to create / edit.
List tests to add or update (one per invariant touched).
Name verification command (test, build, lint).

Show plan. Wait for user OK unless auto mode.

EXECUTE

Per task in order:

Flip §T.n status cell . → ~. Just write to SPEC.md.
Edit code per plan.
Run verification command.
Pass → flip ~ → x. Next task.
Fail → invoke backprop skill. Do NOT retry blindly.
FAIL → BACKPROP

On test/build failure:

Read failure output.
Ask: is failure (a) my code bug, (b) spec wrong, or (c) unspecified edge case?
If (a) → fix code, re-run. No spec change.
If (b) or (c) → invoke spec skill with bug: <cause> first, let it update §V and §B, then resume build against updated spec.

Rule: never silently fix root-cause without considering backprop. §B is the memory that stops recurrence.

WRITE POLICY
Only flip §T status. No other SPEC.md edits from build.
Other spec edits → invoke spec skill.
Commit after each §T completes. Message: T<n>: <goal line> + §V cites.
VERIFICATION

Task x only if:

Verification command exits 0.
New test(s) added per plan.
No §V invariant regressed (run full test suite at end).
NON-GOALS
No sub-agents. No parallel workers. Main thread only.
No progress dashboards. cat SPEC.md | grep §T is the dashboard.
No speculative work beyond chosen task scope.
Weekly Installs
600
Repository
juliusbrussee/cavekit
GitHub Stars
815
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass