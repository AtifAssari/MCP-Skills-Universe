---
rating: ⭐⭐⭐
title: execute
url: https://skills.sh/open-horizon-labs/skills/execute
---

# execute

skills/open-horizon-labs/skills/execute
execute
Installation
$ npx skills add https://github.com/open-horizon-labs/skills --skill execute
SKILL.md
/execute

Bridge from Solution Space to shipped code. Pre-flight, build, detect drift, salvage if needed.

Execute sits within Intent → Execution → Review. It contains an inner loop: build, check alignment, course-correct or salvage.

When to Use

Invoke /execute when aim is clear, solution is chosen, context is loaded, and you're ready to build.

Do not use when: Aim is unclear (/aim), still exploring (/solution-space), or problem is ambiguous (/problem-space, /problem-statement).

The Execute Process
Step 1: Pre-flight Check

Before writing code, verify alignment:

Pre-flight Checklist:
[ ] Aim is clear - what outcome am I producing?
[ ] Constraints known - what must I NOT break?
[ ] Context loaded - do I have the codebase understanding I need?
[ ] Scope bounded - what am I specifically doing (and NOT doing)?
[ ] Success criteria - how will I know when I'm done?
[ ] Readiness clear - why am I deepening now, what invalidates this direction, and what should trigger a stop/pivot?


If any box can't be checked, stop and address it first.

If the work involves a one-way or hard-to-reverse decision and /dissent has not been run, flag it now. Cheap exploration before commitment is the point of the workflow; skipping challenge before a one-way door is the most expensive version of saving time.

Make the phase shift explicit:

"The task is [task]. The aim is [aim]. This ladders back to [selected approach or parent objective]. I'm specifically doing [scope]. I will NOT be touching [out of scope]. Success looks like [criteria]. I'm ready to deepen because [reason]. This direction is invalidated if [condition]. I will stop or pivot if [trigger]."

Those declared success criteria become the delivery contract for later phases: /ship should be able to verify what was promised, not just whether something deployed.

Step 2: Build

Do the work. Keep it focused.

Work in small, testable increments
Stay within declared scope
If scope expands, pause and reassess (see Drift Detection)

During build:

Make the change
Verify it works (tests, manual check, whatever's appropriate)
Run review if available (sg review or equivalent)
Handle review findings (fix trivial, create tasks for non-trivial)
Commit with clear message
Step 3: Detect Drift

Periodically check alignment:

Drift signals: scope expanding, touching unplanned files, "while I'm here" thoughts, approach reversing direction, protecting sunk-cost code.

When you notice drift:

Drift Check:
- Original aim: [aim]
- What I'm doing now: [current work]
- Gap: [describe the divergence]
- Verdict: [aligned | minor drift | significant drift | lost]


Aligned: Continue. Minor drift: Note it, refocus if needed. Significant drift: Pause — refocus, get confirmation, or salvage. Lost: Invoke /salvage immediately.

Step 4: Salvage if Needed

When to stop: approach has reversed 3+ times, scope keeps expanding, you're oscillating not converging, the finish line keeps moving.

Don't fight lost work. Extract the learning and restart clean. Invoke /salvage.

Output Format

When execution completes successfully:

## Execution Complete

**Task:** [what was done]
**Aim achieved:** [how it maps to the original aim]

### Declared Success Criteria
- [criterion 1]
- [criterion 2]

### Delivered Characteristics
- [characteristic/result]: [met | partially met | deferred]

### Changes
- [file/component]: [what changed and why]

### Verification
- [how it was tested/verified]

### Needs Human Verification
Claims that the model asserted but cannot independently confirm:
- [characteristic that was claimed met but not externally observed]
- [assumption that was carried forward without independent test]

If this section is empty, say why.

### Notes
- [anything relevant for future work]


When drift triggers a pause:

## Execution Paused - Drift Detected

**Original aim:** [aim]
**Current state:** [where things stand]
**Drift:** [what diverged and why]

### Options
1. [option 1]
2. [option 2]
3. Salvage and restart

Recommendation: [your assessment]

Session Persistence

Reads: Aim, Problem Statement, Solution Space — essential for drift detection.

Writes: Execute status with declared success criteria and delivered characteristics:

## Execute
**Updated:** <timestamp>
**Status:** [pre-flight | in-progress | drift-detected | complete]

[execution notes, declared criteria, delivered characteristics, drift observations]

Position in Framework

Comes after: /solution-space (you need a chosen approach to execute). Leads to: /ship to deliver, /review to verify, /salvage if drifting. Can loop back to: /aim or /problem-space via /salvage when the approach isn't working.

Weekly Installs
74
Repository
open-horizon-labs/skills
GitHub Stars
1
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass