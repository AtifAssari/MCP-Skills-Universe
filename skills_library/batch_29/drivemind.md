---
title: drivemind
url: https://skills.sh/yuzc-001/drivemind/drivemind
---

# drivemind

skills/yuzc-001/drivemind/drivemind
drivemind
Installation
$ npx skills add https://github.com/yuzc-001/drivemind --skill drivemind
SKILL.md
DriveMind

DriveMind is the layer for keeping meaningful human-AI work from degrading over time.

Its job is to:

preserve execution integrity during long or important work
preserve clear boundaries under pressure
preserve continuity across pauses and context breaks
prevent stuck work from collapsing into fake motion
turn real work into reusable future strength

If none of those are at risk, do not keep DriveMind active.

Trigger boundary
Activate when
the user asks to keep pushing, stay steady, or not stop too early
the task is long-running, high-value, or likely to cross session boundaries
the work risks goal drift, boundary drift, or continuity loss
the agent is stuck and needs diagnosis before pushing harder
the user asks to review, capture the lesson, define a next-time rule, or resume later
the work should leave behind reusable residue: review, handoff, memory, lesson, or SOP
Do not activate when
the task is simple and direct execution is enough
no meaningful continuity or boundary problem exists
the work does not need persistence, review, or handoff
invoking DriveMind would add process without changing the real next action

If unsure, prefer normal execution.

Main path

Follow this path and stop at the first sufficient stabilization.

Step 0 — Detect the real degradation risk

Ask:

What is most likely to degrade if this work continues without DriveMind discipline?

Choose the primary risk:

goal drift
boundary drift
continuity decay
stuck degeneration
closure failure

If no meaningful degradation risk is present, stop. This task does not need DriveMind.

Step 1 — Stabilize the active thread

State the shortest useful version of:

current objective
what matters most right now
the main blocker, uncertainty, or boundary
the next action

Do not produce process theater. Stabilize the thread in the fewest words that actually help.

Step 2 — Preserve boundary integrity

If risk, authority, or irreversible impact is in play:

do not silently cross the boundary
distinguish continue vs switch path vs escalate
ask the smallest focused question needed for authorization

Read references/boundary-preservation.md when boundary handling becomes central.

Step 3 — Recover from stuckness before pushing harder

If the work is stuck:

diagnose the real blocker first
prefer the smallest action that restores momentum or reduces uncertainty
do not substitute frantic activity for progress

Read references/stuck-recovery.md when blockage, retry, or false motion is central.

Step 4 — Preserve continuity when the work may pause

If the work may cross a session boundary or resume later:

capture the minimum state needed for high-fidelity continuation
preserve objective, current state, blocker, next action, and boundary condition

Read references/continuity-preservation.md when handoff or resume fidelity matters.

Step 5 — Close with compounding residue

After meaningful work, or when the user asks to review, capture the smallest reusable residue that will make future work stronger:

review
lesson
next-time rule
handoff note
memory / SOP residue when appropriate

Read references/closure-compounding.md when the value of the task depends on what remains after it ends.

Output style

When DriveMind is active, default to outputs that make the work easier to continue.

Preferred structure:

current objective or judgment
what changed / what matters / what blocks
next action
boundary or escalation point, if any
reusable residue, if relevant

Keep it natural. Keep it short when short is enough. Do not turn every response into a framework recital.

Default rules

Use these only when they materially change the work:

preserve the thread before adding new motion
diagnose before retrying harder
pressure changes tempo, not authorization
continuity must preserve reasoning, not just surface state
a finished task should leave behind stronger future defaults when the work was meaningful
Reference files

Read only when needed.

File	Read when
references/drift-prevention.md	the task risks losing objective, priority, or thread coherence
references/boundary-preservation.md	authority, risk, or irreversible impact is becoming central
references/continuity-preservation.md	the work may pause, hand off, or resume later
references/stuck-recovery.md	the work is blocked and may be slipping into fake motion
references/closure-compounding.md	the task should leave behind review, memory, lesson, or next-time residue
references/residue-selection.md	deciding whether the right residue is a rule, lesson, diary note, handoff note, review, or SOP fragment
references/mode-guide.md	deciding whether normal / execution / intensive mode materially changes behavior
Keep in mind

DriveMind should make meaningful work more stable and more reusable. If it is only adding ceremony, it is failing.

Weekly Installs
16
Repository
yuzc-001/drivemind
GitHub Stars
27
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass