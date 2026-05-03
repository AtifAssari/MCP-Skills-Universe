---
title: dissent
url: https://skills.sh/open-horizon-labs/skills/dissent
---

# dissent

skills/open-horizon-labs/skills/dissent
dissent
Installation
$ npx skills add https://github.com/open-horizon-labs/skills --skill dissent
SKILL.md
/dissent

Structured disagreement that strengthens decisions. Find flaws before the one-way door closes.

Dissent is not attack. It's actively seeking reasons you might be wrong.

When to Use

Invoke /dissent when: about to lock in a one-way door (architecture, public API, major hires), confidence is high but stakes are higher, team is converging too quickly, you're defending a position, or the path forward seems obvious.

Do not use when: Gathering initial options or brainstorming. Dissent stress-tests decisions, not generates them.

The Dissent Process
Step 1: Steel-Man the Current Approach

Before attacking, articulate the position:

"The current approach is [approach]. The reasoning is [reasoning]. The expected outcome is [outcome]. This is the best version of this position."

If you can't state it charitably, you don't understand it well enough to challenge it.

Step 2: Seek Contrary Evidence
What data would prove this approach wrong?
Who disagrees? What's their argument?
What similar approaches have failed elsewhere? Why?
What are we ignoring because it's inconvenient?

"If this approach were wrong, what would we expect to see? Are we seeing any of that?"

Step 3: Pre-Mortem

Imagine it's six months from now and this decision failed. Work backward:

"This failed because [reason]. The warning signs we ignored were [signs]. The assumption that broke was [assumption]."

Generate at least three plausible failure scenarios:

Technical failure — it doesn't work as expected
Adoption failure — it works but nobody uses it / changes nothing
Opportunity cost — it works but we should have done something else
Step 4: Surface Hidden Assumptions

Every decision rests on unstated assumptions. Find them:

What are we assuming about the user/customer?
What are we assuming about the system/codebase?
What are we assuming about timeline/resources?
What are we assuming won't change?

For each:

Assumption: [what we're taking for granted]
Evidence: [what supports this]
Risk if wrong: [what happens]
Test: [how to validate before committing]

Step 5: Decide
PROCEED — no critical flaws found; decision strengthened
ADJUST — issues surfaced that can be addressed; modify the approach
RECONSIDER — fundamental problems revealed; back to solution space

"PROCEED: The counter-argument is [X], but it's addressed by [Y]. The key assumption is [Z], which we've validated by [how]."

ADR Generation

If the decision is a one-way door and you recommend PROCEED or ADJUST, offer to create an Architecture Decision Record. The dissent report maps directly:

Dissent Section	ADR Section
Decision under review	Title
Steel-Man Position	Context
Contrary Evidence + Pre-Mortem	Options Considered
Hidden Assumptions	Consequences
Decision + Reasoning	Decision

Write to docs/adr/NNNN-<decision-slug>.md if accepted.

Output Format
## Dissent Report

**Decision under review:** [what's being challenged]
**Stakes:** [why this matters]
**Confidence before dissent:** [HIGH/MEDIUM/LOW]

### Steel-Man Position
[The best version of the current approach]

### Contrary Evidence
1. [Evidence point 1]
2. [Evidence point 2]
3. [Evidence point 3]

### Pre-Mortem Scenarios
1. **[Failure mode]:** [How this could fail]
2. **[Failure mode]:** [How this could fail]
3. **[Failure mode]:** [How this could fail]

### Hidden Assumptions
| Assumption | Evidence | Risk if Wrong | Test |
|------------|----------|---------------|------|
| [Assumption 1] | [Evidence] | [Risk] | [Test] |

### Decision

**Recommendation:** [PROCEED / ADJUST / RECONSIDER]
**Reasoning:** [Why]
**If ADJUST:** [Specific modifications]
**Confidence after dissent:** [HIGH/MEDIUM/LOW]
**Create ADR?** [Yes - offer path / No - not a one-way door]

Session Persistence

Reads: Aim, Problem Statement, Solution Space — context for the decision being challenged.

Writes: Dissent report:

## Dissent
**Updated:** <timestamp>
**Decision:** [PROCEED | ADJUST | RECONSIDER]

[dissent report content]

Position in Framework

Combines with: /solution-space (challenge the recommendation), /problem-statement (challenge the framing), /execute (before one-way doors). Leads to: PROCEED (continue with confidence), ADJUST (modify approach), or RECONSIDER (back to solution-space). This is not a phase: Dissent is an overlay you invoke when stakes are high.

Weekly Installs
85
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