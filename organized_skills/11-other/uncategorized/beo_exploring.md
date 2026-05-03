---
rating: ⭐⭐
title: beo-exploring
url: https://skills.sh/minhtri2710/skills/beo-exploring
---

# beo-exploring

skills/minhtri2710/skills/beo-exploring
beo-exploring
Installation
$ npx skills add https://github.com/minhtri2710/skills --skill beo-exploring
SKILL.md
Beo Exploring
Overview

Exploring is the decision-extraction phase. Use it to turn a partially formed request into a planning-usable CONTEXT.md.

See ../reference/references/shared-hard-gates.md § Shared References Convention.

Core principle: ask until planning can proceed without guessing.

CONTEXT.md becomes the source of truth for downstream planning, validation, execution, and review.

Hard Gates
Default Exploring Loop
read any existing context and prior learnings
classify the scope and likely gray areas
classify the feature domain (SEE, CALL, RUN, READ, or ORGANIZE)
run a codebase scout: use that domain classification to identify likely artifacts, protocols, templates, or entry points, then read 2-3 relevant files to ground gray areas in existing repo patterns
repeat until all gray areas are resolved: a. ask one focused behavioral question b. wait for the user's response — do not continue until the user answers c. annotate gray areas with existing context when available d. lock decisions explicitly as they emerge
write a sanitized CONTEXT.md
self-check for planning readiness, then hand off to beo-planning

Use ../reference/references/learnings-read-protocol.md when you need the canonical prior-learnings read flow. Use ../reference/references/artifact-conventions.md#slug-lifecycle when updating the epic description safely.

Scope Classification

Classify the feature as Quick, Standard, or Deep and record that classification in the exploring output.

Quick uses the canonical definition in ../reference/references/pipeline-contracts.md.
Standard is the default path for normal feature work.
Deep applies when the work spans multiple systems or needs extra discovery depth.

Quick work still needs gray-area discovery, but it must still satisfy the canonical Quick definition from ../reference/references/pipeline-contracts.md and it skips self-review.

Read Existing Context First

Before asking new questions:

read existing CONTEXT.md when present
inspect the epic description
determine whether decisions are already locked

If CONTEXT.md already contains the needed locked decisions, verify it and continue toward planning. Do not re-ask settled questions just because the feature is being resumed.

Gray-Area Discovery

Look for uncertainties that would materially change planning or execution, such as:

failure behavior
edge cases and empty states
permissions and visibility
migration or compatibility behavior
latency or performance expectations
out-of-scope boundaries

Keep the exploration concrete and answerable. A good exploration question should be answerable in 1-2 sentences and should change downstream decisions.

Classify the feature domain (SEE, CALL, RUN, READ, or ORGANIZE) using the categories in references/gray-area-probes.md. Each round, review the candidate probes for the relevant category and ask exactly one question — the single most valuable probe for the current state of the conversation. After the user responds, reassess and ask the next most valuable probe if gaps remain. Never batch multiple probes into a single message.

Default-Proposal Pattern

If the user says "I don't know" or "whatever you think":

state the uncertainty plainly
propose one concrete default
explain the consequence in behavioral terms
ask for confirmation before locking it
Lock Decisions Explicitly

As answers emerge, assign stable IDs and confirm them.

Example shape:

D1: retry behavior after overnight failure
D2: empty-state behavior for first-time users
D3: permission rule for non-admin access

Do not treat an answer as locked until it has been explicitly confirmed or accepted as the default.

CONTEXT.md Requirements

Write CONTEXT.md using references/context-template.md. All 8 sections are required. If a section is empty, write N/A.

The goal is not to preserve the original conversation. The goal is to preserve the decisions that planning must trust.

Planning-Readiness Check

Before handoff, confirm all of these are true:

every material gray area has been resolved or scoped out
a planner could explain the feature using CONTEXT.md
no unanswered question would change the high-level plan

If any of these fail, keep exploring.

Self-Review

For Standard and Deep work, run one fresh-eyes self-review pass on the CONTEXT.md draft before handoff.

The reviewer checks:

all material gray areas are resolved or explicitly scoped out
no locked decisions contradict each other
D-IDs are assigned consistently
outstanding questions are split correctly between "Resolve Before Planning" and "Deferred to Planning"

Allow at most one retry iteration. If the draft still fails after that retry, flag the unresolved gray areas to the user and ask them to either resolve each flagged item or explicitly mark it as out-of-scope. Do not offer a "proceed anyway" option — the HARD-GATE requiring all material gray areas to be resolved or scoped out still applies.

Quick work is exempt from this self-review step.

Handoff

When exploring is complete:

write CONTEXT.md
update .beads/STATE.json
report how many decisions were locked and what remains out of scope
hand off to beo-planning

Exploring STATE.json uses the canonical 12-field schema from ../reference/references/state-and-handoff-protocol.md (see Example F). Set phase: "exploring", status: "planning-needs-approach", tasks: "none", next: "beo-planning", planning_mode: "unknown", and phase_name to a human-readable feature summary. Exploring does not create execution beads — its deliverable is decision clarity.

Context Budget

Follow ../reference/references/shared-hard-gates.md § Context Budget Protocol. Skill-specific checkpoint items: locked decisions and open questions.

Red Flags & Anti-Patterns

Red flags to catch early:

if you find fewer than 2 meaningful gray areas for non-trivial work, verify that you have not skipped edge cases or scope boundaries
do not spend excessive time circling a single unresolved question; lock what is known and mark the rest for planning only when the remaining uncertainty is truly planning-shaped
do not skip exploring for non-Quick feature work just because the request sounds simple; only work classified as Quick scope by beo-router (via new-quick-intake state) may bypass exploring

Read references/context-template.md when creating or updating CONTEXT.md to ensure correct structure and required fields. Read references/gray-area-probes.md when a user's answer is ambiguous or incomplete and you need targeted follow-up questions.

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