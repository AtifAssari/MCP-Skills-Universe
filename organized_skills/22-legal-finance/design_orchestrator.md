---
rating: ⭐⭐
title: design-orchestrator
url: https://skills.sh/freeacger/loom/design-orchestrator
---

# design-orchestrator

skills/freeacger/loom/design-orchestrator
design-orchestrator
Installation
$ npx skills add https://github.com/freeacger/loom --skill design-orchestrator
SKILL.md
Design Orchestrator
Overview

This skill is the entrypoint for design-stage work.

It does not do the deep design work itself. Its job is to inspect the current design state, choose exactly one next design skill, and keep the workflow moving until the design is ready for writing-plans.

When to Use

Use this skill when:

the task needs design before implementation
the user wants to turn an idea into an implementation-ready design
the design exists, but the next step is unclear
the task needs routing between design decomposition, decision analysis, and readiness review

Do not use this skill when:

the user is asking for direct execution
the task is already in implementation planning
the task is a single-step coding or editing request
the task is a writing request such as a report, note, or summary
the task is a simple linear SOP with no real design state
Shared Design State

Assume the design workflow passes around a shared design_state with these logical fields:

problem
scope
design_tree
open_branches
decision_nodes
external_dependencies
decisions
risks
validation
status
design_target_type

Treat design_target_type as required. Do not silently infer it from an incomplete design-state input.

Core Responsibilities

Your responsibilities are:

Determine whether the task is actually in the design stage.
Inspect the current design_state and identify the single most useful next skill.
Route the task to exactly one next design skill.
Re-evaluate after each handoff until the design either becomes ready for planning or the user stops.
Prevent premature transition into writing-plans.
Routing Rules

Apply routing in this order.

1. Missing Required State

Route to design-structure when:

the task should already be in design-state form, but design_target_type is missing
a design tree exists, but the target type has not been set explicitly

In this case, do not continue to any other design skill first. The next step is to make the target type explicit.

2. No Real Tree Yet

Route to design-structure when:

there is no real design tree yet
the task is still a vague idea or feature request
scope, boundaries, core objects, or key flows are still missing
3. Derived Tree Candidate

Before routing to design-refinement, check whether the current tree is beginning to contain a second stable problem domain.

Use the shared derivation rules in ../design-tree-core/REFERENCE.md as the source of truth for this judgment.

A derived tree should be created only if all of the following are true:

the current tree is starting to answer a second distinct core question
that question appears repeatedly, not as a one-off exception
the branch now behaves like a stable decision system
a child tree can define its own scope and done criteria
deriving it will make the parent tree smaller and clearer

If those conditions are met:

route to design-structure to create a derived tree
require an explicit parent/child handoff
require the parent tree to shrink the extracted branch after derivation

If those conditions are not met:

do not derive
continue routing within the current tree
4. Explicit Decision Blocker

Route to decision-evaluation when:

there is a bounded decision node with real alternatives
the blocking issue is a concrete choice rather than an under-specified branch
5. Mostly Complete

Route to design-readiness-check when:

the design appears mostly complete
the remaining question is whether it is safe to move into implementation planning
6. Everything Else

Route to design-refinement when:

a design tree exists
major branches are still shallow, vague, or unresolved
the main need is deeper decomposition, edge-case coverage, or failure-path clarification

When design-structure has just completed the initial tree's main body:

expect that tree to be persisted before routing onward
treat design-refinement as the default next step unless a bounded decision or readiness check is the clearer blocker
Diagram Conventions

After routing, show the current workflow position as a character DAG inside a code block (no language tag):

[task-brief]
     │
     ▼
[design-orchestrator]  ← you are here
     │
     ▼
[design-structure]


Or when showing branching:

          [orchestrator]
          │    │    │
     ┌────┘    │    └────┐
     ▼         ▼         ▼
[structure] [refine] [evaluate]


Rules:

Components in [brackets], vertical flow with │ and ▼
Fan-out: ┌────┘ / └────┐; fan-in: └────┬────┘
Max width: 78 characters
Only include when routing changes or the user asks for a status overview
Entry and Exit Criteria

Enter when:

the task needs design-stage coordination
the user has not asked to skip design

Exit when:

design-readiness-check returns that the design is ready for planning
the user explicitly stops the design workflow
the task turns out not to require design-stage work after all
Handoff Rules
Never expand a branch in depth yourself if a specialized design skill should do it.
Never compare options broadly if the real next step is to structure or refine the design.
If a downstream skill changes the design materially, re-check routing instead of assuming the next step.
After design-structure completes a main tree, prefer design-refinement as the default continuation.
Only send the task to writing-plans after design-readiness-check has clearly passed.
If a downstream skill cannot be invoked in the current context, still name it explicitly as the next step and stop. Do not execute its responsibilities inline as a substitute.
Never route to more than one next step in the same turn.
Never continue a design flow that is missing design_target_type.
Never derive a new tree just because the current tree is long.
Never keep expanding a branch inline after deciding that it should become a derived tree.
Never absorb report writing, note production, or SOP drafting into design routing.
Weekly Installs
14
Repository
freeacger/loom
GitHub Stars
1
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass