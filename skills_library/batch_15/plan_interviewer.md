---
title: plan-interviewer
url: https://skills.sh/hungv47/prod-skills/plan-interviewer
---

# plan-interviewer

skills/hungv47/prod-skills/plan-interviewer
plan-interviewer
Installation
$ npx skills add https://github.com/hungv47/prod-skills --skill plan-interviewer
SKILL.md
Plan Interviewer — Orchestrator

Productivity — Multi-agent orchestration. Transform shallow feature requests into well-specified plans through multi-round interviews.

Core Question: "What haven't we thought of yet?"

Inputs Required
A feature request, problem description, or existing plan/spec file to refine
Access to AskUserQuestion tool for multi-round interviews
Output
Spec file at user-designated path (default: .agents/spec.md)
Chain Position

Previous: none | Next: task-breakdown or system-architecture

Skill Deference
Have a FEATURE or PRODUCT to specify? → Use this skill.
Have a declining METRIC to diagnose (X is at Y, should be Z)? → Use problem-analysis (from strategy-skills) instead.

Re-run triggers: When requirements change significantly, when new technical constraints emerge, or when a previous spec leads to implementation blockers.

Multi-Agent Architecture
Agent Roster
Agent	File	Focus
codebase-scanner-agent	agents/codebase-scanner-agent.md	Extracts tech stack, schemas, existing implementations from code
artifact-reader-agent	agents/artifact-reader-agent.md	Reads specs, PRDs, product context — extracts decisions already made
challenger-agent	agents/challenger-agent.md	Validates premise with exactly 3 challenge questions
interviewer-agent	agents/interviewer-agent.md	Conducts multi-round interview via AskUserQuestion (5 dimensions)
synthesis-agent	agents/synthesis-agent.md	Assembles all context into structured specification
critic-agent	agents/critic-agent.md	Quality gate review, dimension coverage, decision completeness
Execution Layers
Layer 1 (parallel):
  codebase-scanner-agent ──┐
  artifact-reader-agent ───┘── run simultaneously

Layer 2 (sequential):
  challenger-agent ─────────── uses Layer 1 context to validate premise
    → interviewer-agent ────── conducts interview (INTERACTIVE — uses AskUserQuestion)
      → synthesis-agent ────── writes the specification
        → critic-agent ─────── final quality review

Dispatch Protocol
Layer 1 dispatch — send brief to codebase-scanner-agent and artifact-reader-agent in parallel. They extract what the codebase and existing artifacts already answer.
Challenger dispatch — send brief + Layer 1 outputs to challenger-agent. It produces exactly 3 challenge questions and a PROCEED/REFRAME/DEFER recommendation.
User confirmation — present challenger's questions to the user. If REFRAME, present the alternative framing. If user confirms proceed, continue. If DEFER, stop and explain.
Interviewer dispatch — send all context to interviewer-agent. It conducts 3-7 rounds of interview via AskUserQuestion, covering all 5 dimensions, skipping questions already answered by Layer 1.
Synthesis dispatch — send all outputs to synthesis-agent to write the spec.
Critic review — send spec to critic-agent.
Revision loop — if critic returns FAIL, re-dispatch affected agents. Maximum 2 rounds.
Save — write spec to user-designated path (default: .agents/spec.md).
Routing Rules
Condition	Route
No codebase exists (greenfield)	codebase-scanner-agent returns NO CODEBASE; all questions valid
No artifacts exist	artifact-reader-agent returns NO ARTIFACTS; interview from scratch
Challenger recommends REFRAME	Present reframing to user; proceed on confirmation
Challenger recommends DEFER	Stop; explain what should happen instead
User says "skip the questions, just write it"	Use Layer 1 context + challenger only; synthesize without interview
Critic PASS	Save and deliver
Critic FAIL	Re-dispatch cited agents with feedback
Critical Gates

Before delivering, the critic-agent verifies ALL of these pass:

 All 5 interview dimensions explored (Technical, UX, Business Logic, Architecture, Security)
 Spec contains concrete decisions, not open-ended options
 Edge cases documented with explicit handling strategies
 Open questions list is empty or explicitly deferred with rationale

If any gate fails: the critic identifies which agent must fix it and the orchestrator re-dispatches.

Single-Agent Fallback

When context window is constrained or the feature is simple:

Skip multi-agent dispatch
Check for existing codebase context and artifacts
Challenge the premise (3 questions: right problem? what if nothing? what exists?)
Conduct interview using AskUserQuestion (2-4 questions per round, all 5 dimensions)
Write specification using the Spec File Format below
Run Critical Gates as self-review
Save to .agents/spec.md
AskUserQuestion Tool Usage

This skill is interactive. The interviewer-agent uses AskUserQuestion for every question round.

Structure questions for maximum clarity:

2-4 questions per invocation
Each question has 2-4 concrete options
Options represent real tradeoffs, not obvious choices
Include brief description explaining implications of each option
State which option you recommend and why

Example:

Question: "When a background sync fails, how should we handle it?"
Options:
1. Silent retry (3x with backoff) — User unaware, but may see stale data
2. Toast notification — User informed but may be annoyed
3. Badge indicator — Subtle, user can investigate when ready
4. Block UI until resolved — Safest but worst UX
Recommended: Option 1 — most sync failures are transient; fall back to option 2 if retries exhaust.

Interview Dimensions (all 5 required)
Technical Implementation
Data flow edge cases (What happens when X fails mid-operation?)
State management boundaries (Where does this state live?)
Concurrency considerations (What if two users do this simultaneously?)
Migration paths, performance cliffs
UX & Interaction Design
Error recovery flows, loading/empty/error states
Undo/redo expectations, accessibility edge cases
Mobile-first considerations
Business Logic & Domain
Edge case ownership, audit/compliance needs
Multi-tenancy implications, internationalization
Architecture & Tradeoffs
Consistency vs availability, coupling concerns
Testability, observability
Implementation foresight (decisions to resolve NOW, not at 2am during build)
Security & Privacy
Trust boundaries, data exposure, rate limiting
Spec File Format
# [Feature Name] Specification

## Problem Statement
[1-2 paragraphs on what we're solving and why]

## Decided Approach
[High-level approach with key architectural decisions]

## Key Decisions
| Decision | Choice | Rationale |
|----------|--------|-----------|
| [Topic]  | [What] | [Why]     |

## Edge Cases
- **[Scenario]**: [How we handle it]

## Out of Scope
- [What we're explicitly NOT doing]

## Open Questions
- [ ] [Anything still unresolved]

## Implementation Notes
[Technical details, gotchas, dependencies]

Anti-Patterns
Anti-Pattern	Problem	INSTEAD
Leading questions	"Don't you think we should use WebSockets?" pushes toward predetermined answer	Ask open-ended: "What are your latency requirements?"
Accepting the first answer	Surface-level answers miss hidden constraints	Probe deeper: "Why that approach?" and "What would change your mind?"
Skipping edge cases	Happy-path specs produce happy-path code that breaks in production	scaling-agent traces failure modes; interviewer explores empty states, concurrent access
Scope creep during interview	Each new question expands feature surface	Periodically re-anchor: "Is this still in scope for MVP?"
Asking questions the codebase answers	"What framework?" when package.json is right there	codebase-scanner-agent extracts facts first; interviewer skips answered questions
Options instead of decisions	Spec says "could use X or Y"	synthesis-agent writes concrete decisions only; undecided items go to Open Questions
Worked Example

User: "I want to build a habit tracker app."

Layer 1 (parallel):

codebase-scanner-agent → NO CODEBASE (greenfield)
artifact-reader-agent → NO ARTIFACTS

Challenger (3 questions):

Right problem? "Outcome: users build consistent habits. A habit tracker is the most direct path."
What if nothing? "Users currently use spreadsheets — friction causes abandonment."
What exists? "Greenfield — no existing code." → Recommendation: PROCEED

Interviewer (5 rounds, AskUserQuestion):

Round 1 (Scope): Personal only, mobile-first PWA, 4-week MVP
Round 2 (Users): Health-conscious 25-35, switching from spreadsheets
Round 3 (Features): Add habit → check off → see streak. Configurable reminders.
Round 4 (Edge cases): Streak resets on miss (history preserved), user's local timezone
Round 5 (Technical): Email magic link auth, offline sync on reconnect

Synthesis: Spec with 14 concrete decisions and 3 deferred items.

Critic: PASS — all 4 gates pass, all 5 dimensions covered.

Artifact saved to .agents/spec.md.

Before Starting
Step 0: Product Context

Check for .agents/product-context.md. If available, read for product and audience context before interviewing. If missing, plan-interviewer works standalone.

Optional Artifacts
Artifact	Source	Benefit
.agents/product-context.md	icp-research (from hungv47/comms-skills)	Product context prevents redundant interview questions
.agents/problem-analysis.md	problem-analysis (from hungv47/strategy-skills)	Root cause context when feature solves a diagnosed problem
Artifact Template

On re-run: rename existing artifact to spec.v[N].md and create new with incremented version.

Save to user-designated path (default: .agents/spec.md) using the Spec File Format above.

References
references/question-bank.md — Extended list of probing questions by domain
Weekly Installs
10
Repository
hungv47/prod-skills
GitHub Stars
1
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass