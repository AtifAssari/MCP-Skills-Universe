---
rating: ⭐⭐⭐
title: problem-space
url: https://skills.sh/open-horizon-labs/skills/problem-space
---

# problem-space

skills/open-horizon-labs/skills/problem-space
problem-space
Installation
$ npx skills add https://github.com/open-horizon-labs/skills --skill problem-space
SKILL.md
/problem-space

Map the terrain where solutions live. What are we optimizing? What constraints are real? Which can be questioned?

Problem space precedes solution space. Jump to code too early and you build the wrong thing fast.

When to Use
Starting new work — before implementation, understand what you're solving
Hitting repeated blockers — same problems in different forms
Patches accumulating — third config flag for the same bug means you're treating symptoms
Estimates off by 10× — the problem isn't understood
Agent talking itself out of constraints — "for this prototype we don't have time" when the constraint matters

Skip when: Problem is well-understood and you're in execution. Problem space is for grounding, not stalling.

The Problem Space Process
Step 1: State the Objective Function

What are we optimizing? Not the feature — the outcome.

"We are optimizing for [outcome]."

"Build a login page" is a feature. "Reduce time-to-first-value for new users" is an objective.

What behavior change indicates success?
What metric moves if this works?
What problem disappears if we get this right?
Step 2: Map the Constraints

List what we treat as fixed. Be explicit about each constraint's nature:

Constraint: [the boundary]
Type: [hard | soft | assumed]
Reason: [why it exists]
Questioning: [could this be false?]


Hard — physics, regulations, signed contracts. Don't bend. Soft — organizational decisions, technical debt, time pressure. Negotiable. Assumed — "we've always done it this way." Question these.

The trap: agents talk themselves out of constraints. "For this prototype we don't have time" is often false when code generation takes 15 minutes. Ground in what's fixed.

With RNA MCP: If oh_search_context is available, call it with the objective/domain and phase: "problem-space". Surface guardrails as already-settled constraints (hard, with source attribution). Present remaining candidates for human confirmation before finalizing the constraints table.

Step 3: Identify the Terrain
Systems involved? — existing code, external APIs, data stores
Who is affected? — users, operators, downstream systems
Blast radius? — if this goes wrong, what breaks?
Precedents? — solved before? Where?

With RNA MCP: If oh_search_context is available, call it with the problem domain and phase: "problem-space". Surface relevant metis entries as candidate precedents with provenance — human selects what to carry. Dismissed items are excluded from the final map.

Step 4: Surface Hidden Assumptions

Every problem space has embedded assumptions. Make them visible:

"We assume [assumption]. If this is false, [consequence]."

Zero assumptions listed is not "clean" — it means you haven't looked. Name at least one or explain why the problem space has no hidden premises.

Step 5: Check for X-Y Problems

Are we solving the real problem (X) or the user's attempted solution (Y)?

Signs of X-Y mismatch:

Request is oddly specific for a simple goal
You're building something that feels like a workaround
"How do I do [technique]?" without explaining why

If potential X-Y problem detected:

"The user asked for [Y], but the underlying need might be [X]."

If constraints, assumptions, or open questions still feel implicit after this step, you're not ready for /solution-space. Force the unknowns into the artifact.

Output Format
## Problem Space Map

**Date:** [timestamp]
**Scope:** [what area this covers]

### Objective
[What we're optimizing for - the outcome, not the feature]

### Constraints

| Constraint | Type | Reason | Question? |
|------------|------|--------|-----------|
| [boundary] | hard/soft/assumed | [why] | [could this be false?] |

### Terrain
- **Systems:** [what's involved]
- **Stakeholders:** [who's affected]
- **Blast radius:** [what breaks if wrong]
- **Precedents:** [existing solutions to examine]

### Assumptions Made Explicit
1. [assumption] - if false: [consequence]
2. [assumption] - if false: [consequence]

### Open Questions
- [unknown that must be answered before solution-space]
- [unknown that can be carried with explicit risk]

Zero open questions is suspicious. If you have none, say why — a problem space with no unknowns has either been deeply investigated or insufficiently examined.

### X-Y Check
- **Stated need (Y):** [what was asked for]
- **Underlying need (X):** [what might be needed]
- **Confidence:** [high/medium/low that Y=X]

### Ready for Solution Space?
[yes/no] - [why or what's missing]

Session Persistence

If session name provided (/problem-space auth-refactor): reads/writes .oh/auth-refactor.md directly. If no session name provided (/problem-space): offer to save with suggested name from git branch or exploration topic.

Reads: existing session file; prior outputs — especially Aim and Problem Statement — to ground exploration. Writes: problem space map so later phases reuse explicit constraints, assumptions, and open questions:

## Problem Space
**Updated:** <timestamp>

[problem space map content]

Position in Framework

Comes after: /aim (know your destination before mapping terrain). Leads to: /problem-statement to frame the specific challenge, or /solution-space if already well-framed. Can loop back from: /salvage (constraints were wrong), /review (keeps hitting same blockers).

Weekly Installs
76
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