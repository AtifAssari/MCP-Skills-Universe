---
rating: ⭐⭐⭐
title: design-structure
url: https://skills.sh/freeacger/loom/design-structure
---

# design-structure

skills/freeacger/loom/design-structure
design-structure
Installation
$ npx skills add https://github.com/freeacger/loom --skill design-structure
SKILL.md
Design Structure
Overview

This skill turns a vague idea into an initial design tree through a two-phase workflow:

Interactive confirmation — progressively confirm design_target_type, problem, scope, and assumptions with the user
Design tree generation — produce the design tree based on confirmed inputs

Its primary output is design_state. When the initial tree first becomes stable enough to reference safely, persist it as the authoritative design artifact in the designated directory docs/design-tree/ before handing off to the next design step.

When to Use

Use this skill when:

the user has an idea but not a design
the task lacks scope, boundaries, core objects, or key flows
there is no clear design tree yet
the current design conversation is still at the "what are we even designing?" stage
an existing tree is missing design_target_type and needs that field to be made explicit

Do not use this skill when:

a workable design tree already exists
the main need is deeper decomposition of existing branches
the main need is to compare options for one explicit decision node
the main need is to decide whether the design is ready for planning
the current tree only needs deeper refinement rather than a true derived tree
the task is a report, note, summary, or documentation rewrite
the task is a simple linear SOP with no real design-state boundary
Language Strategy

Match the design file language to the user's instruction language.

Use this priority order:

An explicit output-language request from the user
The dominant natural language of the user's current instruction
The dominant natural language of the most recent user instructions in the same task
English if the signal is weak or ambiguous

Rules:

Keep the chat response, interactive Q&A, and the design file in the same language
Translate section headings into the chosen language
Keep file paths, code identifiers, template placeholders (e.g., {{...}}), and literal config keys unchanged
Do not mix languages unless the user explicitly asks for bilingual output
Interactive Q&A in Phase 1 must also match the chosen language

Default heading examples:

If the output language is English:

Problem
Scope
Included / Excluded
Assumptions
Design Tree
Open Branches
Decision Nodes
Decisions
External Dependencies
Workflow
Phase 1: Interactive Confirmation

Confirm the foundation before generating the design tree. Proceed in order:

Design target type — confirm one of system, workflow, methodology, framework
Problem — confirm the core problem and success metrics
Scope — confirm what is included and excluded
Assumptions — confirm implicit assumptions being made

After each confirmation, update the shared design_state. Do not repeat confirmed content in subsequent conversation.

Skip a section only if the user explicitly provides it upfront (e.g., "the problem is X and the scope is Y" — confirm both in one round).

Phase 2: Design Tree Generation

Based on confirmed inputs, generate the design tree using the branch skeleton that matches design_target_type.

Use ../design-tree-core/REFERENCE.md for shared type definitions and REFERENCE.md for preferred local branch skeletons.

If a branch is not relevant, say so explicitly instead of silently omitting it.

In conversation, show only:

the tree diagram
decision nodes that need user action
open branch names
next step recommendation
Derived Tree Creation

This skill may also be used to create a derived tree when a parent tree has already identified a new stable problem domain.

Use the shared derivation and handoff rules in ../design-tree-core/REFERENCE.md as the source of truth.

When creating a derived tree, do all of the following:

Name the parent tree and the derived tree explicitly.
State the reason for derivation.
Define what the derived tree owns.
Define what the derived tree does not own.
Record the minimum parent/child handoff:
branch being extracted
inherited constraints
unresolved questions
expected output
return conditions

Do not copy the parent tree into the derived tree. Do not use derivation as a way to dump overflow detail.

Interactive Q&A
Intent-Driven Strategy

Use whatever interactive question tool is available in the current environment. Do not hardcode tool names — describe the interaction intent and constraints; the model selects the right tool based on its environment.

Constraints (cross-CLI compatible):

1–3 questions per prompt
≤ 4 options per question
Structured text (question + optional choices)

Fallback: If no dedicated question tool is available, use natural language prompts (see format templates below).

Question Types and Formats
Confirmation — state understanding, ask to verify
## Problem

Core problem: Build an internal API gateway for unified routing, authentication, and rate limiting.
Success metrics: P99 latency < 50ms, availability > 99.9%

↑ Is this correct? Anything to amend?

Scope — checklist with include/exclude markers
## Scope

My assessment:

Included ✓
- Request routing
- Authentication and authorization
- Rate limiting
- Request logging

Excluded ✗
- Service discovery
- Load balancing

↑ Any adjustments?

Decision — table with star ratings, best option first, max 4 options
## Pending Decision: Auth Mode

| Option | Rating | Pros | Cons |
|--------|--------|------|------|
| JWT (stateless) | ★★★ | Scales horizontally, no server state | Revocation is complex, token size |
| Session (stateful) | ★★ | Instant revocation, mature pattern | Requires shared storage, limited scaling |
| API Key | ★ | Simple to implement | Low security, not suitable for user-level auth |

↑ Which one? Or a different idea?

Supplement — direct question with relaxed prompt
## Supplementary Info

Expected daily request volume?

↑ Please fill in (a rough range is fine if uncertain)


Rules for all types:

One question type per message
End every question with ↑ marker to signal "your turn"
After user confirms, do not repeat the confirmed content (it is already captured in design_state and will be persisted once the tree is stable enough to reference safely)
Persistence

Use REFERENCE.md for the repo-local save and naming contract. This persistence behavior is a repo-local rule for this repository, not a shared default for the design-tree family.

When the tree first reaches a stable-to-reference threshold, save it to the designated directory docs/design-tree/ using the path docs/design-tree/<feature-slug>.md. Mark the saved document status as draft. Do this before handing off to design-refinement or any other next design step.

Design Tree Requirement

Create an initial design tree that:

makes design_target_type explicit
uses the correct branch skeleton for that target type
identifies open branches
identifies explicit decision nodes
captures assumptions rather than relying on them silently
reaches a stable-to-reference threshold before handoff
keeps the output as design_state first and the saved artifact as the authoritative persisted record

If a branch is not relevant, say so explicitly instead of silently omitting it.

Core Responsibilities

Your responsibilities are:

Clarify the real goal of the design through interactive confirmation.
Make design_target_type explicit before building the tree.
Capture scope, non-goals, and constraints.
Build an initial design tree with first-level and, where useful, second-level branches.
Identify open branches that still need refinement.
Identify explicit decision nodes that should later go to decision-evaluation.
Record assumptions instead of silently relying on them.
Flag nodes that depend on unverified external tools, APIs, libraries, or services. Perform a lightweight feasibility check (web search or doc lookup) at the time of flagging. If the dependency is clearly infeasible, mark ✗ immediately; if confirmed feasible with open questions, mark [RESEARCH] with initial findings; if fully confirmed, mark ✓.
Persist the design as soon as it first reaches a stable-to-reference threshold into the designated directory docs/design-tree/, and mark the saved document as draft.
If acting on a parent-tree handoff, create a derived tree with explicit parent/child boundaries rather than repeating the parent tree inline.
Expected Outputs
Required Output

Produce or update a design_state that includes:

design_target_type
problem
scope
design_tree
open_branches
decision_nodes
external_dependencies
status

If the tree being created is a derived tree, also include:

parent/child ownership
derivation reason
parent/child handoff
Conversation Output (concise)
Phase 1: one question at a time (see Question Types)
Phase 2: tree diagram + decision node summaries + open branch names + saved file path + draft status + next step

You are not expected to fully close every branch.

Diagram Conventions

Render the design tree as a character tree diagram inside a code block (no language tag).

Format:

design_tree
├── 1. Problem definition
│   ├── 1.1 Core problem
│   └── 1.2 Success metrics ✓
├── 2. Core flows [OPEN]
│   ├── 2.1 Happy path
│   └── 2.2 Error path
├── 3. Interfaces and data
│   └── 3.1 API contract [DRAFT]
├── 4. External integrations
│   └── 4.1 Payment SDK [RESEARCH]
└── 5. Decision points
    └── 5.1 Storage choice [DECISION]


Character rules:

Branches: ├── (middle), └── (last)
Continuation: │ (non-last parent), (last parent, 4 spaces)
Numbering: 1., 1.1 — required at first two levels
Max width: 78 characters

Status markers:

Marker	Meaning
[OPEN]	Unresolved, needs refinement or decision
[DECISION]	Decision node with multiple real options
[DRAFT]	Tentative, may change
[RESEARCH]	Depends on an external tool, API, library, or service that has passed initial feasibility check but needs deeper validation
✓	Complete / verified
✗	Rejected / out of scope

When to render: Always include a tree diagram when the design tree has 3+ branches. Omit only if the design is trivially small (1-2 branches).

Entry and Exit Criteria

Enter when:

there is no meaningful design tree yet
the request is still mostly unstructured

Exit when:

the design tree exists with enough structure for follow-on work
the main remaining work is branch refinement or explicit decision analysis
Handoff Rules
Persist the tree before any downstream design handoff once it first reaches the stable-to-reference threshold.
The first persisted version of the tree must be marked draft.
Hand off to design-refinement as the default next step when the main body exists but branches are still too shallow.
Hand off to decision-evaluation when there is a concrete decision node with real options.
Hand back to design-orchestrator if the design state changed enough that routing should be re-evaluated.
Do not continue past Phase 1 if design_target_type is still unresolved.
Do not force the conversation into option comparison before the design tree is formed.
Do not delay persistence after the stable-to-reference threshold has been reached.
Weekly Installs
12
Repository
freeacger/loom
GitHub Stars
1
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn