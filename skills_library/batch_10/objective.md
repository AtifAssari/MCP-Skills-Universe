---
title: objective
url: https://skills.sh/dagster-io/erk/objective
---

# objective

skills/dagster-io/erk/objective
objective
Installation
$ npx skills add https://github.com/dagster-io/erk --skill objective
SKILL.md
Objective Skill
Overview

Objectives are coordination documents for goals requiring multiple plans/PRs to complete. Unlike erk-prs (single executable implementations), objectives track progress across related work and capture lessons learned along the way.

Scope range:

Small: Feature requiring 2-3 related PRs
Medium: Refactor spanning several plans
Large: Long-running strategic direction emitting many plans
Objective vs Erk-Plan
Aspect	Erk-Plan	Objective
Purpose	Single executable implementation	Coordinate 2+ related plans/PRs
Scope	One PR or tightly-coupled change	Multiple plans toward coherent goal
Body	Machine-parseable metadata	Human-readable markdown
Comments	Session context dumps	Action logs + lessons
Label	erk-pr	erk-objective
Tooling	erk pr dispatch/implement	Manual updates via comments
Key Design Principles
Human-first - Plain markdown, no machine-generated metadata
Incremental capture - Each action gets its own comment
Lessons as first-class - Every action comment includes lessons learned
Clear roadmap - Status visible at a glance in the body
Body stays current via reconciliation - After every PR landing, agents audit prose sections against what was actually implemented and correct stale information
Steelthread-first - Each phase starts with minimal vertical slice proving the concept works
One PR per phase - Each phase is sized for a coherent single PR
Always shippable - System remains functional after each merged PR
Body is source of truth - Body always contains complete current state; comments are the changelog
Two-step for all changes - Every addition (context, decisions, phases) gets a comment AND body update
Context over code - Provide references to patterns, not prescriptive implementations
Session handoff ready - Body should be self-contained for any session to pick up and implement
Quick Reference
Creating an Objective
gh issue create --title "Objective: [Title]" --label "erk-objective" --body "$(cat <<'EOF'
# Objective: [Title]

> [1-2 sentence summary]

## Goal

[What success looks like - concrete end state]

## Design Decisions

1. **[Decision name]**: [What was decided]

## Roadmap

### Phase 1: [Name] Steelthread (1 PR)

Minimal vertical slice proving the concept works.

| Node | Description | Status | PR |
|------|-------------|--------|-----|
| 1.1 | [Minimal infrastructure] | pending | |
| 1.2 | [Wire into one command] | pending | |

**Test:** [End-to-end acceptance test for steelthread]

### Phase 2: Complete [Name] (1 PR)

Fill out remaining functionality.

| Node | Description | Status | PR |
|------|-------------|--------|-----|
| 2.1 | [Extend to remaining commands] | pending | |
| 2.2 | [Full test coverage] | pending | |

**Test:** [Full acceptance criteria]

EOF
)"

Logging an Action

Post an action comment after completing work. See format.md for full template.

gh issue comment <issue-number> --body "$(cat <<'EOF'
## Action: [Brief title]
**Date:** YYYY-MM-DD | **PR:** #123 | **Phase/Node:** 1.2
### What Was Done
### Lessons Learned
### Roadmap Updates
EOF
)"


After posting, update the issue body (roadmap statuses, reconcile stale prose sections).

Updating Node Details

Update node description, slug, or reason using update-objective-node:

# Update description
erk exec update-objective-node 8470 --node 1.3 --description "Revised description"

# Set slug
erk exec update-objective-node 8470 --node 1.3 --slug "revised-slug"

# Skip with comment
erk exec update-objective-node 8470 --node 1.3 --status skipped --comment "Superseded by new approach"

# Combine multiple updates
erk exec update-objective-node 8470 --node 2.1 --description "New desc" --slug "new-slug" --status planning

Adding Nodes

Add new nodes to an existing objective's roadmap:

# Add to existing phase (auto-assigns next ID, e.g., 1.4)
erk exec add-objective-node 8470 --phase 1 --description "Clean up dead code"

# With explicit slug and dependencies
erk exec add-objective-node 8470 --phase 2 \
  --description "Integration tests" \
  --slug integration-tests \
  --depends-on 2.1 --depends-on 2.2

# With comment for adding
erk exec add-objective-node 8470 --phase 1 \
  --description "Handle edge case" \
  --comment "Discovered during re-evaluation"

Updating Node Status

Always use the programmatic command — never manually edit YAML or prose tables:

erk exec update-objective-node <issue> --node <id> --status <status>
erk exec update-objective-node <issue> --node <id> --pr '#1234'


Then validate: erk objective check <issue-number>

Viewing an Objective

View an objective's dependency graph, dependencies, and next node:

# CLI
erk objective view <issue-number>

# Slash command (in-session)
/local:objective-view <issue-number>

Spawning an Erk-Plan

To implement a specific roadmap node, create an erk-pr that references the objective:

erk pr create --file plan.md --title "Implement [node description]"

Workflow Summary
Create objective - When starting multi-plan work
Inspect progress - View dependency graph and next node
Log actions - After completing each significant piece of work
Update body - Keep roadmap status current, reconcile stale prose after each PR landing
Spawn erk-prs - For individual implementation nodes
Close - When goal achieved or abandoned (proactively ask when all nodes done)
Resources
references/
format.md - Complete templates, examples, and update patterns
workflow.md - Creating objectives, spawning plans, steelthread structuring
updating.md - Quick reference for the two-step update workflow
closing.md - Closing triggers and procedures
Weekly Installs
65
Repository
dagster-io/erk
GitHub Stars
81
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn