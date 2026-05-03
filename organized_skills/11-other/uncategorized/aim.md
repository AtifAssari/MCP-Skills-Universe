---
rating: ⭐⭐⭐
title: aim
url: https://skills.sh/open-horizon-labs/skills/aim
---

# aim

skills/open-horizon-labs/skills/aim
aim
Installation
$ npx skills add https://github.com/open-horizon-labs/skills --skill aim
SKILL.md
/aim

Clarify the outcome you want. An aim is a change in user behavior, not a feature shipped. First step in Intent-Execution-Review.

The aim IS the abstraction. Clarifying what behavior to change abstracts the business domain itself. Features are mechanism; the aim is why they matter.

When to Use
Starting new work — before problem-statement or problem-space
Scope feels fuzzy — you can describe what but not why
Multiple solutions seem valid — aim reveals which moves the needle
Work has drifted — check alignment
Team is misaligned — surfaces hidden assumptions

Skip when: You already have a crisp aim. Move to /problem-statement or /problem-space.

The Aim Process
Step 1: State the Desired Behavior Change

Start with the user, not the system.

"Users will [specific behavior] instead of [current behavior]."

Bad: "Add dark mode toggle" Good: "Users can work comfortably at night without eye strain"

Bad: "Improve onboarding flow" Good: "New users reach their first value moment within 5 minutes"

Key distinction: Features are outputs. Behavior changes are outcomes. If users don't become more capable, shipping more output doesn't rescue the work.

Step 2: Identify the Mechanism

The mechanism is your hypothesis — the causal lever you believe produces the behavior change.

Mechanism: [What you're changing]
Hypothesis: [Why you believe it will produce the outcome]
Assumptions: [What must be true for this to work]


If you listed zero assumptions, that is a red flag, not a clean bill of health. Every mechanism rests on premises. Name at least one or explain why none exist.

Watch for abstract qualities (simplicity, speed, clarity) posing as aims — these are mechanisms, not outcomes. Ask what they enable that their absence blocks.

Step 3: Define the Feedback Signal

How will you know if the aim is achieved?

"We'll know it's working when [observable signal]."

Signals must be observable, timely, and attributable to your mechanism.

Step 4: Set Guardrails

What constraints bound this work? What would cause you to stop?

Guardrail: [boundary]
Reason: [why this matters]
Trigger: [when to revisit]

Output Format
## Aim Statement

**Aim:** [One sentence: the behavior change you want]

**Current State:** [What users do now]
**Desired State:** [What users will do after]

### Mechanism
**Change:** [What you're building/changing]
**Hypothesis:** [Why you believe this produces the outcome]
**Assumptions:** [What must be true]

### Feedback
**Signal:** [How you'll know it's working]
**Timeframe:** [When you'll have signal]

### Guardrails
- [Guardrail 1]
- [Guardrail 2]


Later phases carry forward the aim's explicit fields — outcome, mechanism, assumptions, feedback signal, guardrails — as the contract the rest of the workflow preserves.

Session Persistence

If session name provided (/aim auth-refactor): reads/writes .oh/auth-refactor.md directly. If no session name provided (/aim): offer to save with suggested name from git branch or aim content.

Reads: existing session file; prior skill outputs for context. Writes: aim statement (outcome, mechanism, assumptions, feedback signal, guardrails) as the contract later phases reuse:

## Aim
**Updated:** <timestamp>

[aim statement content]


If the section exists, replace it.

Position in Framework

Comes after: Nothing — aim is the entry point. Leads to: /problem-space to map the terrain, or /solution-space if the problem is already clear. Can loop back from: /salvage (restart with learning), /review (if aim has drifted).

Weekly Installs
71
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