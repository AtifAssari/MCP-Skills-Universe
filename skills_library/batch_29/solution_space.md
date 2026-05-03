---
title: solution-space
url: https://skills.sh/open-horizon-labs/skills/solution-space
---

# solution-space

skills/open-horizon-labs/skills/solution-space
solution-space
Installation
$ npx skills add https://github.com/open-horizon-labs/skills --skill solution-space
SKILL.md
/solution-space

Explore candidate solutions before committing. The trap is defending the first workable idea.

Sits between Problem Statement and Implementation. You have the problem framed; now map approaches before picking one.

When to Use
Problem is understood — you have a clear problem statement
Multiple approaches viable — not obvious which path is best
About to start coding — pause and explore first
Patches accumulating — third config flag for the same bug
Attached to first idea — that's the warning sign

Skip when: Still clarifying the problem. Use /problem-statement first.

The Local Maximum Trap

Exploration is cheap. The failure mode is defending the first solution that works.

Signs you're stuck on a local maximum:

First solution is the only one considered
Explaining why alternatives won't work before trying them
Acting as crafter (defending) rather than editor (filtering)
Implementation details discussed before approaches compared
The Escalation Ladder

Not all problems need redesigns. The ladder finds the right altitude.

Level 1: Band-Aid Fix

Patch the symptom. Fine under deadline pressure; toxic as habit. Signal: "This will break again" Example: Null check. Catch exception. Hardcode edge case.

Level 2: Local Optimum

Optimize within current assumptions. Classic refactor trap — improves what exists without questioning it. Signal: "Cleaner but the same shape" Example: Extract method. Add parameter. Refactor for readability.

Level 3: Reframe

Question the problem statement. Different framing yields different solutions, often revealing the actual constraint. Signal: "What if the problem is..." Example: "We need faster cache invalidation" becomes "Why do we cache this at all?"

Level 4: Redesign

Change the system so the problem doesn't exist. Problems dissolve rather than get solved. Signal: "With this change, we wouldn't need to..." Example: Instead of fixing sync conflicts, make the data flow unidirectional.

The Process
Step 1: State the Problem (Confirm)

"The problem we're solving is: [statement]. The key constraint is: [constraint]. The critical assumption is: [assumption]. Success looks like: [outcome or signal]."

If you can't state this clearly, go back to /problem-statement. Start from explicit constraints and assumptions, not fuzzy recollection.

Step 2: Generate Candidates (Breadth)

List at least 3-4 candidates before evaluating any:

## Candidate Solutions

### Option A: [Name]
- Approach: [Brief description]
- Level: [Band-Aid / Local Optimum / Reframe / Redesign]
- Trade-off: [Main cost]

### Option B: [Name]
...


Rules:

No evaluation yet — generation only
Include at least one approach from a higher level than your instinct
Include the "obvious" solution even if you don't like it
Include status quo when it's a real option — sharpens comparison, makes cost of inaction explicit
Maximize variance early; breadth is exploratory fuel

With RNA MCP: If oh_search_context is available, call it with problem statement + active outcome + phase: "solution-space" before generating candidates. Surface relevant metis — prior evaluations, approaches tried, recurring patterns. Human selects what to carry; selected metis informs the candidate list. This prevents proposing solutions already tried and rejected.

Step 3: Evaluate Trade-offs (Depth)

Before scoring, define the scoring function: what matters most, which constraints eliminate early, how user value is recognized. Then prune aggressively.

With RNA MCP: If oh_search_context is available, call it with the active outcome to surface applicable guardrails. These are constraints that rule options out before evaluation, not trade-offs — fold confirmed guardrails as hard constraints. Do not auto-apply metis as constraints; surface it and let the human decide weight.

For each candidate:

Does it solve the stated problem? (Not a related problem)
Does it increase user value or produce more output?
How does it score against key constraints and success signal?
Implementation cost? (Time, complexity, risk)
Maintenance cost? (Ongoing burden)
Second-order effects? (New problems created)
Future optionality? (Options enabled or closed)
Step 4: Recommend with Reasoning
## Recommendation

**Approach:** [Selected option]
**Level:** [Band-Aid / Local Optimum / Reframe / Redesign]

**Why this one:**
- [Reason 1]
- [Reason 2]

**Why not the others:**
- Option A: [Reason rejected]
- Option B: [Reason rejected]

**Known trade-offs we're accepting:**
- [Trade-off 1]
- [Trade-off 2]

Step 5: Check for Local Maximum
Did I defend my first idea or explore?
Is there a higher-level approach I dismissed too quickly?
Am I optimizing the wrong thing?

Landing on the first idea after exploration is fine. The danger is never looking.

Output Format
## Solution Space Analysis

**Problem:** [One sentence]
**Key Constraint:** [The binding constraint]
**Critical Assumption:** [The assumption that most threatens this recommendation if false]
**Success Signal:** [What later phases should verify]
**Scoring Function:** [How options are compared/pruned, including user-value criteria]

If Critical Assumption is blank, the recommendation is untested. Every non-trivial recommendation depends on something that could be wrong. Name it.

### Candidates Considered

| Option | Level | Approach | Trade-off |
|--------|-------|----------|-----------|
| A | [Level] | [Brief] | [Cost] |
| B | [Level] | [Brief] | [Cost] |
| C | [Level] | [Brief] | [Cost] |

### Evaluation

**Option A: [Name]**
- Solves stated problem: [Yes/Partially/No]
- Implementation cost: [Low/Medium/High]
- Maintenance burden: [Low/Medium/High]
- Second-order effects: [Description]

[Repeat for each option]

### Recommendation

**Selected:** Option [X] - [Name]
**Level:** [Band-Aid / Local Optimum / Reframe / Redesign]

**Ladders back to:** [the higher-level objective or outcome this recommendation serves]
**Tactic justification:** [why this is a good tactic for that objective under current constraints]

**Rationale:** [Why this approach fits the constraints]

**Accepted trade-offs:**
- [Trade-off 1]
- [Trade-off 2]

### Execution Contract

**Preserve:**
- [criterion or behavior later phases must preserve]
- [criterion or behavior later phases must preserve]

**Verify later via:**
- [signal `/execute` and `/ship` should be able to check]

### Readiness Gate

**Ready to deepen because:** [why this is ready to move from exploration into execution]
**Invalidated if:** [what evidence or discovery would make this direction wrong]
**Stop/Pivot if:** [what signal should cause us to halt or return to solution-space]

### Needs Human Verification
Claims or decisions in this recommendation that the model cannot self-check:
- [assumption that needs independent confirmation before commitment]
- [one-way decision that should not proceed on model confidence alone]

This section routes questions to the real human checkpoint (PR review, stakeholder approval, manual verification) rather than pretending an inline model field can substitute for independent judgment.

### Implementation Notes

[Any specific considerations for the selected approach]



If this recommendation involves a one-way or hard-to-reverse decision (architecture, public API, data model, external commitment), invoke /dissent before moving to /execute. Cheap exploration means the cost of challenge is low; the cost of an unchallenged wrong commitment is not.

Session Persistence

If session name provided (/solution-space auth-refactor): reads/writes .oh/auth-refactor.md directly. If no session name provided (/solution-space): offer to save with suggested name from git branch or problem being solved.

Reads: existing session file; prior outputs — Aim, Problem Statement, Problem Space — to understand constraints. Writes: solution space analysis so /execute can reuse selected approach, critical assumption, success signal, scoring function, execution contract, and readiness gate:

## Solution Space
**Updated:** <timestamp>

[solution space analysis and recommendation]

Position in Framework

Comes after: /problem-statement (need a framed problem to evaluate against). Leads to: /execute to implement, or /dissent to challenge the recommendation. Can loop back to: /problem-statement (if exploration reveals the problem is mis-framed).

Weekly Installs
72
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