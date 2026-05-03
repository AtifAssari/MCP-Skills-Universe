---
title: beo-debugging
url: https://skills.sh/minhtri2710/skills/beo-debugging
---

# beo-debugging

skills/minhtri2710/skills/beo-debugging
beo-debugging
Installation
$ npx skills add https://github.com/minhtri2710/skills --skill beo-debugging
SKILL.md
Beo Debugging
Overview

Debugging resolves blockers and failures systematically. Use it to classify the problem, reproduce it, isolate root cause, apply the right fix path, and capture the pattern.

See ../reference/references/shared-hard-gates.md § Shared References Convention.

Core principle: triage -> reproduce -> diagnose -> fix -> learn. Do not guess.

Hard Gates
Default Debugging Loop
read prior learnings — use the canonical learnings-read protocol (../reference/references/learnings-read-protocol.md) before investigating. 30-40% of recurring failures are already documented. QMD/Obsidian first, flat-file fallback when unavailable.
classify the issue clearly
reproduce it or state why reproduction is not yet possible
diagnose until the root cause fits in one sentence
apply the right fix path
capture the pattern and route back cleanly

Use references/debugging-operations.md for the exact known-pattern check, reproduction flow, fix split, blocker handling, and checkpoint behavior. Use references/diagnostic-checklist.md for the ordered sub-checks. Use references/message-templates.md when reporting blockers or results to the orchestrator via Agent Mail.

Triage and Diagnosis

The output of triage should be a one-line classification such as [TYPE] in [component]: [symptom]. Then work through reproduction and diagnosis in order.

Fix Path

Fix beads must still use the shared Reactive Fix Bead Template from ../reference/references/bead-description-templates.md.

Learn

After the fix path is clear or a blocker is confirmed, capture the pattern using the debug-note flow in references/debugging-operations.md, including the debug_attempted labeling rule.

Escalation and Timeout
If a blocker remains unresolved after one rescue attempt, leave the bead in blocked status with a comment documenting the blocker details, then pause and report to the user for direction. Do not silently retry indefinitely.
Handoff

After debugging resolves the root cause and the fix is verified, route based on origin:

Origin	Route
beo-executing (worker hit a blocker)	Route back to beo-executing to resume the execution loop
beo-reviewing (review found a defect)	Route back to beo-reviewing to continue the review cycle
beo-swarming (worker blocker during swarm)	Return findings to the swarm orchestrator via the worker’s blocker comment; the coordinator decides whether to unblock, reassign, or escalate
beo-router (standalone debugging session)	Hand back to beo-router with findings in STATE.json so router can re-route
Direct user invocation	If a direct fix was applied, summarize what changed and ask for user confirmation before further routing. Otherwise, present findings and recommended fix to the user; do not auto-route without user confirmation

If the issue remains unresolved after escalation, report the blocker clearly and pause for user direction. Do not spin; report once, then pause.

For blocker-specific handling details, see references/debugging-operations.md.

Context Budget

Follow ../reference/references/shared-hard-gates.md § Context Budget Protocol. Skill-specific checkpoint: see references/debugging-operations.md for the full procedure.

Red Flags & Anti-Patterns
Fixing symptoms instead of root cause — if the error recurs, return to diagnosis
Skipping reproduction — never diagnose from the error message alone
Not checking critical-patterns.md first — 30-40% of recurring failures are already documented
Committing fixes without verification using the exact failing command
Silently patching CONTEXT.md decision violations to make tests pass
Calling the first visible error the root cause — walk the full error chain
Ignoring blocked work instead of classifying and reporting it cleanly
Weekly Installs
15
Repository
minhtri2710/skills
GitHub Stars
1
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass