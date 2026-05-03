---
title: ideation
url: https://skills.sh/haha0815/claude-meta-skills/ideation
---

# ideation

skills/haha0815/claude-meta-skills/ideation
ideation
Installation
$ npx skills add https://github.com/haha0815/claude-meta-skills --skill ideation
SKILL.md
Ideation

Turn ideas into validated designs. Three modes for different levels of confidence needed.

Mode Selection
Mode	When to Use	Effort
Quick	Standalone idea generation, naming, brainstorming options	Low
Collaborative	Before implementing features, components, or behavior changes	Medium
Formal Review	High-stakes decisions requiring risk reduction and peer review	High
Mode 1: Quick Ideation (Gemini API)

Generate ideas systematically using structured techniques.

Prerequisites
pip install google-generativeai
export GEMINI_API_KEY=your_api_key

Techniques

Generate Ideas:

gemini -m pro -o text -e "" "Generate 10 creative ideas for: [topic]
Requirements: mix conventional/unconventional, varying complexity, different perspectives, 2+ wild cards.
For each: brief description, key benefit, main challenge"


SCAMPER Method:

gemini -m pro -o text -e "" "Apply SCAMPER to: [product/feature/process]
- Substitute: What can be replaced?
- Combine: What can be merged?
- Adapt: What can be modified?
- Modify/Magnify: What can be enlarged or emphasized?
- Put to other uses: What else could this be used for?
- Eliminate: What can be removed?
- Reverse/Rearrange: What can be reorganized?"


Six Thinking Hats:

gemini -m pro -o text -e "" "Analyze using Six Thinking Hats:
DECISION: [what you're considering]
- White Hat (Facts): What do we know?
- Red Hat (Feelings): Gut reactions?
- Black Hat (Caution): What could go wrong?
- Yellow Hat (Optimism): Benefits?
- Green Hat (Creativity): Alternatives?
- Blue Hat (Process): Best approach?"


Reverse Brainstorming:

gemini -m pro -o text -e "" "Reverse brainstorm: How could we make [goal] FAIL?
1. List ways to guarantee failure
2. Flip each into a success strategy
3. Identify hidden risks"


Constraint Removal:

gemini -m pro -o text -e "" "Brainstorm without constraints:
PROBLEM: [your problem]
1. Unlimited budget? 2. No time limit? 3. Any technology? 4. No legacy?
Then: Which ideas can be scaled down to reality?"


Evaluate & Compare:

gemini -m pro -o text -e "" "Evaluate ideas against criteria:
IDEAS: [list]
CRITERIA: Feasibility (1-5), Impact (1-5), Effort (1-5 lower=better), Risk (1-5 lower=better)
Create comparison matrix and recommend top choice."

Mode 2: Collaborative Design (Before Implementation)

Help turn ideas into fully formed designs through natural dialogue. Use this before any creative work.

The Process

Understanding the idea:

Check current project state first (files, docs, recent commits)
Ask questions ONE AT A TIME to refine the idea
Prefer multiple choice when possible
Focus on: purpose, constraints, success criteria

Exploring approaches:

Propose 2-3 different approaches with trade-offs
Lead with your recommended option and explain why

Presenting the design:

Once you understand what you're building, present the design
Break into sections of 200-300 words
Ask after each section if it looks right
Cover: architecture, components, data flow, error handling, testing
After the Design

Documentation:

Write validated design to docs/plans/YYYY-MM-DD-<topic>-design.md
Commit the design document

Implementation (if continuing):

Ask: "Ready to set up for implementation?"
Use git worktrees for isolated workspace
Create detailed implementation plan
Key Principles
One question at a time — Don't overwhelm
Multiple choice preferred — Easier to answer
YAGNI ruthlessly — Remove unnecessary features
Explore alternatives — Always 2-3 approaches before settling
Incremental validation — Present in sections, validate each
Mode 3: Formal Design Review (Multi-Agent)

Structured, sequential multi-agent review for high-confidence decisions. Prevents blind spots, false confidence, and premature convergence.

Operating Model
One agent designs, others review
No agent may exceed its mandate
Creativity centralized, critique distributed
Process is gated and terminates by design
Agent Roles

1. Primary Designer (Lead)

Owns the design, runs collaborative ideation (Mode 2)
Maintains Decision Log
May NOT self-approve or ignore reviewer objections

2. Skeptic / Challenger

Assumes design will fail. Why?
Questions assumptions, identifies edge cases, flags YAGNI violations
May NOT propose new features or redesign

3. Constraint Guardian

Enforces: performance, scalability, reliability, security, maintainability, cost
May reject designs violating constraints
May NOT debate product goals or suggest features

4. User Advocate

Represents end user: cognitive load, usability, clarity, error handling
Flags confusing or misleading aspects
May NOT redesign architecture or add features

5. Integrator / Arbiter

Resolves conflicts, finalizes decisions, enforces exit criteria
Accepts or rejects objections
May NOT invent new ideas or add requirements
The Process

Phase 1 — Design: Primary Designer runs Mode 2 (collaborative). Initial design + Decision Log produced.

Phase 2 — Review: Agents invoked ONE AT A TIME: Skeptic → Constraint Guardian → User Advocate. Each provides scoped feedback. Designer responds to objections and updates Decision Log.

Phase 3 — Arbitration: Integrator reviews final design + Decision Log + unresolved objections. Explicitly accepts or rejects each objection with rationale.

Decision Log (Mandatory)

Must record: decision made, alternatives considered, objections raised, resolution and rationale.

Exit Criteria (Hard Stop)

ALL must be true:

Understanding Lock completed
All reviewer agents invoked
All objections resolved or explicitly rejected
Decision Log complete
Arbiter declared design acceptable

Final disposition: APPROVED, REVISE, or REJECT with rationale.

Best Practices
Quantity first — Generate many ideas before judging
Defer judgment — Don't critique during generation
Build on ideas — "Yes, and..." thinking
Embrace wild ideas — They often lead to practical ones
Set constraints — Limits boost creativity
Match mode to stakes — Quick for low-stakes, Formal for high-stakes
Weekly Installs
9
Repository
haha0815/claude…a-skills
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass