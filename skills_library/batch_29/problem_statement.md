---
title: problem-statement
url: https://skills.sh/open-horizon-labs/skills/problem-statement
---

# problem-statement

skills/open-horizon-labs/skills/problem-statement
problem-statement
Installation
$ npx skills add https://github.com/open-horizon-labs/skills --skill problem-statement
SKILL.md
/problem-statement

Define the framing. Change the statement, change the solution space.

A problem statement is not the problem — it's the lens. Different framings open different solution spaces. The right framing makes good solutions obvious; the wrong framing makes them invisible.

When to Use
Starting new work — before solutions, articulate what you're solving
Solutions feel off — proposed solutions seem convoluted or like workarounds
Oscillating on approach — direction keeps changing; framing might be wrong
Suspected X-Y problem — someone asks for a specific solution but underlying need is unclear
Requirements expanding — scope creep signals framing mismatch
After /aim but before /solution-space — aim defines outcome, problem statement frames challenge

Skip when: You have a crisp problem statement. Move to /solution-space.

The Framing Process
Step 1: Surface the Current Framing

"The problem is currently framed as: [how it's being described]"

Capture: the stated problem, embedded assumptions, what's treated as fixed vs. changeable.

Step 2: Detect X-Y Problems

Watch for X-Y pattern: someone asks for Y (attempted solution) when they need X (real problem).

Signs of X-Y mismatch:

Request oddly specific for a simple goal
Solution feels like a workaround
"How do I do [technique]?" without explaining why
Convoluted multi-step approach to something simple

If detected:

"You're asking for [Y], but the underlying need seems to be [X]. Is that right?"

Step 3: Separate WHAT from HOW

A good problem statement articulates WHAT needs to change, not HOW.

Wrong (solution)	Right (problem)
"Add a caching layer to reduce latency"	"Page loads take 3+ seconds; users abandon before content appears"
"Refactor the auth module"	"Adding a new auth provider takes 2 weeks and touches 6 files"

Test: Does it describe a symptom or a solution? Could someone unfamiliar with the codebase understand what's wrong? Does it leave room for multiple approaches?

Step 4: Identify Constraints and Flexibility

Hard — regulatory, physics, existing user commitments. Soft — "we've always done it this way," technical debt, team preferences.

Questions to surface flexibility:

What would we do if [constraint] didn't exist?
Who decided [constraint] was fixed? Can we revisit?
Cost of violating vs. cost of keeping?
Step 5: Craft the Problem Statement

[Who] needs [what outcome] because [why it matters], but currently [what's blocking].

Good statements are crisp (1-2 sentences), outcome-focused, testable, and solution-agnostic.

Bad	Good
"The API is slow"	"API responses take 800ms; our SLA requires 200ms"
"We need microservices"	"Deploying a fix requires coordinating 4 teams and takes 2 weeks"
"Users don't understand the UI"	"40% of support tickets are 'how do I X' where X is a core feature"
"We need better tests"	"Last 3 production incidents were caught by users, not tests"
Step 6: Validate the Framing
State it to someone else — if they immediately suggest a solution, framing is too narrow
Invert it — what would the world look like if this problem didn't exist?
Zoom out — is this a symptom of a larger problem?
Zoom in — is this multiple problems masquerading as one?
Output Format
## Problem Statement

**Current framing:** [How the problem is currently being described]

**Reframed as:** [Your crisp problem statement]

**The shift:** [What changed in how we see it]

### Constraints
- **Hard:** [Actually immovable constraints]
- **Soft:** [Constraints that feel fixed but might be flexible]

### Assumptions Being Tested
- [assumption embedded in this framing]

Every framing rests on assumptions. If you listed zero, either the framing is trivial or you haven't surfaced what it depends on. Name at least one.

### What this framing enables
[What solution approaches become visible with this framing]

### What this framing excludes
[What approaches are off the table—and whether that's intentional]

### Signal This Framing Is Wrong
[What we would see if this framing is a symptom, not the problem]

Session Persistence

If session name provided (/problem-statement auth-refactor): reads/writes .oh/auth-refactor.md directly. If no session name provided (/problem-statement): offer to save with suggested name from git branch or problem topic.

Reads: existing session file; prior outputs — especially Aim — to ground the framing. Writes: problem statement so solution-space can reuse framing, assumptions, and invalidation signal:

## Problem Statement
**Updated:** <timestamp>

[problem statement content]


If the section exists, replace it. If not, append after Aim section.

Position in Framework

Comes after: /aim and /problem-space (know where you're going and what terrain you're in). Leads to: /solution-space to explore approaches, or /dissent if the framing feels too easy. Can loop back from: /solution-space (if exploration reveals the problem is mis-framed).

Weekly Installs
73
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