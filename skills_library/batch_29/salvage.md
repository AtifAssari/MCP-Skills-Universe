---
title: salvage
url: https://skills.sh/open-horizon-labs/skills/salvage
---

# salvage

skills/open-horizon-labs/skills/salvage
salvage
Installation
$ npx skills add https://github.com/open-horizon-labs/skills --skill salvage
SKILL.md
/salvage

Extract learning from work before restarting. Code is cheap; learning is the asset.

When to Use

Invoke /salvage when:

Work is drifting - approach has changed direction multiple times
Scope expanding while "done" keeps fuzzing - the finish line keeps moving
Starting over feels right - but you don't want to lose what you learned

Do not use when: Work is on track and converging. Salvage is for extraction before restart, not routine reflection.

The Salvage Process
Step 1: Acknowledge the State

"This session/approach is being salvaged because [reason]. The original aim was [aim]. What happened was [reality]."

Step 2: Extract Five Things

Work through these categories. Extract what's present.

If RNA MCP is available: Before extracting, call oh_search_context with the failure domain and active phase. Was this failure predictable from the corpus? Three outcomes change what gets written:

Relevant entry existed and applied — the learning is about process (corpus not consulted), not domain. Write process metis, not domain metis.
Relevant entry existed but was insufficient — update or strengthen existing entries rather than creating near-duplicates.
Nothing found — new territory. Write fresh metis with confidence.
1. Model Shifts (What changed your understanding?)
What assumptions were wrong?
What would you tell yourself at the start of this work?

"I thought X, but Y."

2. Guardrails (Constraints discovered the hard way)
What boundaries should have been explicit from the start?
What "don't do this" rules emerged?
What edge cases bit you?

Format as explicit constraints:

Guardrail: [boundary]
Reason: [why this matters]
Trigger: [when to revisit this constraint]

3. Missing Context (What would have helped upfront?)
What questions should have been asked at the start?
What existing code/patterns should have been found first?

"If I had known about [X], I would have [Y] instead."

4. Local Practices (Hard-won lessons worth encoding)

Good local practices are:

Specific enough to be actionable, general enough to apply beyond this case
Non-obvious (not "write tests" but "this API silently returns 200 on auth failure")
Situated and decision-changing, not generic advice a foundation model already knows
5. What Worked (Don't lose the wins)
What approaches or code fragments are worth keeping?
What partial solutions could seed the restart?
Step 3: Package for Fresh Start

Synthesize the extraction into a restart kit:

## Salvage Summary

### Original Aim
[What we were trying to achieve]

### Why Salvaged
[Direct statement of what went wrong]

### Key Learnings
1. [Learning 1]
2. [Learning 2]
3. [Learning 3]

### New Guardrails
- [Guardrail 1]
- [Guardrail 2]

### Context for Restart
[What the next attempt should know before starting]

### Reusable Fragments
[Any code, patterns, or approaches worth keeping]

Step 4: Persist Learnings (if available)

Persist the metis, not the noise. Record the non-obvious constraints, anomalies, trade-offs, and local patterns that would change a later decision. Generic best-practice advice that adds no local leverage should be left out of the artifact.

If Open Horizons MCP is available:

Log to OH — Log tribal knowledge and guardrails to the graph
Update AGENTS.md — If learnings are project-wide, suggest additions
Record to RNA (if available) — oh_record_metis for new learnings (no duplicates), oh_record_guardrail_candidate for hard constraints, outcome_progress to record what was accomplished before restarting

If no persistent storage is available, output the salvage summary for the user to capture manually.

Meta-signal: If salvage repeatedly surfaces similar learnings, the corpus has the knowledge but it’s not being consulted. That pattern warrants /distill.

Output Format

Always produce a salvage summary in this structure:

## Salvage Report

**Salvaged:** [date/session identifier]
**Reason:** [why this work is being salvaged]
**Original Aim:** [what we were trying to do]

### Learnings
[Numbered list of key insights]

### New Guardrails
[Explicit constraints with reason and trigger]

### Missing Context
[What would have helped]

### Local Practices
[Hard-won wisdom to encode]

### Reusable Fragments
[Code or patterns worth keeping]

### Fresh Start Recommendation
[How to approach this next time]

Session Persistence

Reads: Everything — Aim, Problem Statement, Problem Space, Solution Space, Execute, Review — to understand what was attempted and what happened.

Writes: Salvage report seeding the next session:

## Salvage
**Updated:** <timestamp>
**Outcome:** [extracted learnings, ready for restart]

[salvage report: learnings, guardrails, context for fresh start]

Position in Framework

Comes after: /review (drift detected) or /execute (thrashing recognized). Leads to: /aim or /problem-space with fresh understanding.

Weekly Installs
69
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