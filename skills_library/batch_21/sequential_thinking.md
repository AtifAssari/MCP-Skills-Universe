---
title: sequential-thinking
url: https://skills.sh/petbrains/mvp-builder/sequential-thinking
---

# sequential-thinking

skills/petbrains/mvp-builder/sequential-thinking
sequential-thinking
Installation
$ npx skills add https://github.com/petbrains/mvp-builder --skill sequential-thinking
SKILL.md
Sequential Thinking Methodology

Framework for using /mcp__sequential-thinking__sequentialthinking tool effectively.

Quick Assessment

Skip entirely for: Simple facts, obvious fixes, single-step answers, routine tasks

Apply when:

Problem requires 3+ logical steps
Multiple valid approaches exist
Debugging with unclear root causes
Initial confidence <70%
State transitions or causal chains involved
Core Framework
1. Initial Classification
Simple → Skip tool
Medium → 3-4 thoughts  
Complex → up to 7 thoughts


Define: initial state → goal state → success criteria

2. State-Based Reasoning

For each thought:

Current state: What's true now?
Preconditions: What must be true for next action?
Effects: How does action change state?
Verify: Valid and closer to goal?
Check: Success criteria met?
3. Thought Structure
Thought N: [Hypothesis/Analysis/Action]
- State: [explicit]
- Logic: [deduction|induction|abduction|causal]  
- Confidence: X%
- Next: [what this enables]

4. Decision Points

Branch (branch_from_thought + unique branch_id):

Confidence <60% WITH alternative
Contradiction found
Equal validity paths (Δ<10%)

Revise (is_revision=true + revises_thought):

Fundamental error
Precondition false
Better approach (>20% gain)

Extend (needs_more_thoughts=true):

Approaching limit but incomplete
5. Quality Scoring

Start: 0 | Minimum: 5 points

Positive: Clear mechanism (+2), Verified assumption (+2), Resolved contradiction (+2), Valid transition (+1)

Negative: Circular reasoning (-3), Invalid transition (-3), Unverified assumption (-2), Logical leap (-1)

If <5 after 3 thoughts → reassess approach

6. Convergence Rules
Thoughts 1-2: Explore breadth (20%)
Thoughts 3-5: Deep dive (60%)
Thoughts 6-7: Verify only (20%)

Terminate when: 7 thoughts reached | Confidence >90% for 2 consecutive | Cycling detected | Success met

Code-Specific Additions

Track: Variable states, Pre/postconditions, Resource constraints, Error paths

Verify: Execution traces, Edge cases, Resource cleanup, Thread safety

Natural Language Integration

Use markers like:

"Let me work through this systematically..."
"This leads me to consider..."
"A potential issue here is..."

Never expose: Internal scores, Framework mechanics, Artificial confidence percentages

Meta-Rules
Admit uncertainty rather than guess
Each thought must advance solution
No pure repetition
Don't fake confidence to avoid branching
Weekly Installs
12
Repository
petbrains/mvp-builder
GitHub Stars
10
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass