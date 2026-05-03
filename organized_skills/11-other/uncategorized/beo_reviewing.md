---
rating: ⭐⭐
title: beo-reviewing
url: https://skills.sh/minhtri2710/skills/beo-reviewing
---

# beo-reviewing

skills/minhtri2710/skills/beo-reviewing
beo-reviewing
Installation
$ npx skills add https://github.com/minhtri2710/skills --skill beo-reviewing
SKILL.md

See ../reference/references/shared-hard-gates.md § Shared References Convention.

Beo Reviewing
Overview

Reviewing is the final quality gate after execution. Its job is to verify that the implemented final execution scope is safe, aligned with locked decisions, and actually acceptable to the user before the feature passes quality criteria.

Core principle: review finds truth, not excuses.

Communication Standard

All review outputs (specialist findings, P1/P2/P3 classifications) must follow ../reference/references/communication-standard.md: plain language first, evidence with quotes or path:line, concrete failure scenario, and smallest fix.

Hard Gates
Default Review Loop
confirm review is allowed for the final execution scope
run automated specialist review
classify findings by severity and create follow-up work when needed
run human UAT against locked decisions and exit-state claims
announce pass or fail: on pass, hand off to beo-compounding; on fail with fixable issues, loop through reactive fixes; on fail with unfixable issues, route back to the appropriate skill
hand off to compounding only when review is truly complete

Use references/reviewing-operations.md for the exact prerequisite checks, artifact verification, UAT handling, and finishing sequence. Use references/review-specialist-prompts.md for the five-specialist review structure and severity rules.

Quick Mode: For Quick-scope features (see ../reference/references/pipeline-contracts.md), skip specialist subagents, do a quick manual artifact check, explicit per-claim user confirmation (Quick mode skips specialist subagents, not the UAT requirement), then run build/test/lint and close. See references/reviewing-operations.md Section 6 for details.

Review Prerequisites

Confirm the final execution scope is actually complete and all required artifacts are available before starting review. See references/reviewing-operations.md Section 1 for the exact prerequisite checks.

Scope Rule

Review the executed scope only. For multi-phase work, that means the final approved scope for the feature only when no later phases remain. If later phases still exist, do not finish the feature in review; route back to planning-aware flow instead.

Automated Specialist Review

Run the canonical five-specialist review defined in references/review-specialist-prompts.md. The review must cover, at minimum:

implementation correctness
contract / interface safety
test and verification adequacy
architecture / maintainability risk
user-facing or workflow regression risk

Use the reference file for the exact prompts and dispatch structure. Do not treat code inspection alone as sufficient evidence; review findings about tests, build, lint, runtime behavior, or generated artifacts must be backed by concrete verification evidence.

Severity Semantics

Do not collapse the P1/P2/P3 categories. Their placement and blocking behavior matter. See references/review-specialist-prompts.md for the severity table and rules.

Reactive Fix Loop

Reactive fixes are part of finishing the current feature. P2 and P3 work are not. See references/reviewing-operations.md and references/review-specialist-prompts.md for the exact P1 fix-and-re-review cycle. Do not patch implementation directly inside review just to save time. Route fixes back through execution with proper bookkeeping.

Human UAT

Human UAT is not optional. Review automated findings first, then walk the user through the implemented outcome against locked decisions and exit-state claims.

Use the canonical review/UAT approval rules from ../reference/references/approval-gates.md (items 3 and 6). Use references/reviewing-operations.md Section 4 for the exact UAT loop and outcome handling.

Intent Changes During UAT

If the user says the implementation is wrong because the desired behavior changed:

update CONTEXT.md to reflect the new decision
if the change is minor and does not alter architecture or sequencing, create follow-up work using the proper severity path
if the change is major, stop review, strip approved, and route back to beo-planning

Do not patch over a changed feature definition inside review. Do not misclassify changed user intent as a normal defect; treat it as a planning/context change and route accordingly.

Finishing Rules

Use references/reviewing-operations.md Section 5 for the exact conditions, finish sequence, artifact verification, and final reporting. When review passes with non-blocking follow-up work, keep P2/P3 items outside the current epic unless the user explicitly wants them folded into the same feature closure path.

Handoff

Only after review genuinely passes:

close the epic in br: br close <EPIC_ID>
write fresh state using ../reference/references/state-and-handoff-protocol.md
set the state to status: "learnings-pending" and next: "beo-compounding"
announce that the review gate has passed and hand off to beo-compounding

The epic must be closed before writing learnings-pending state. Compounding assumes a closed epic and will reject an open one.

Do not hand off to compounding while P1 fixes, unresolved UAT, or planning-level intent changes remain.

Context Budget

Follow ../reference/references/shared-hard-gates.md § Context Budget Protocol. Skill-specific checkpoint items: review progress, open findings by severity, UAT status, and whether review is waiting on execution, planning, or user confirmation.

Red Flags & Anti-Patterns

Do not collapse severity levels, skip artifact verification because the implementation "looks fine," or let automated review substitute for explicit human UAT.

Weekly Installs
19
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