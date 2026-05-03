---
title: swarm-planner
url: https://skills.sh/am-will/codex-skills/swarm-planner
---

# swarm-planner

skills/am-will/codex-skills/swarm-planner
swarm-planner
Installation
$ npx skills add https://github.com/am-will/codex-skills --skill swarm-planner
Summary

Generates dependency-aware implementation plans optimized for parallel multi-agent execution.

Creates atomic, independently executable tasks with explicit dependency declarations to maximize parallelization across agents
Requires codebase investigation, documentation retrieval for external libraries, and clarifying questions before planning to eliminate ambiguity
Structures plans with task IDs, dependency arrays, descriptions, file locations, and validation criteria; includes visual dependency graphs and parallel execution wave groupings
Spawns a subagent review step to catch missing dependencies, ordering issues, and gaps before finalizing the plan
SKILL.md
Swarm-Ready Planner

Create implementation plans with explicit task dependencies optimized for parallel agent execution. This skill can be ran inside or outside of Plan Mode.

Core Principles
Explore Codebase: Investigate architecture, patterns, existing implementations, dependencies, and frameworks in use.
Fresh Documentation First: Use Context7 for ANY external library, framework, or API before planning tasks
Ask Questions: Clarify ambiguities and seek clarification on scope, constraints, or priorities throughout the planning process. At any time.
Explicit Dependencies: Every task declares what it depends on, enabling maximum parallelization
Atomic Tasks: Each task is independently executable by a single agent
Review Before Yield: A subagent reviews the plan for gaps before finalizing
Process
1. Research

Codebase investigation:

Architecture, patterns, existing implementations
Dependencies and frameworks in use
1a. Optional: Stop to Clarification Questions
If the architecture is unclear or missing STOP AND YIELD to the user, and request user input (AskUserQuestions) before moving on. Always offer recommendations for clarification questions.
If architecture is present, skip 1a and move onto next step.
2. Documentation

Documentation retrieval (REQUIRED for external dependencies):

Use Context7 skill or MCP to fetch current docs for any libraries/frameworks or APIs that are or will be used in project. If Context7 is not available, use web search.

This ensures version-accurate APIs, correct parameters, and current best practices.

3. STOP and Request User Input

When anything is unclear or could reasonably be done multiple ways:

Stop and ask clarifying questions immediately
Do not make assumptions about scope, constraints, or priorities
Questions should reduce risk and eliminate ambiguity
Always offer recommendations for clarification questions.
Use request_user_input or AskUserQuestion tool if available.
4. Create Dependency-Aware Plan

Structure the plan with explicit task dependencies using this format:

Task Dependency Format

Each task MUST include:

id: Unique identifier (e.g., T1, T2.1)
depends_on: Array of task IDs that must complete first (empty [] for root tasks)
description: What the task accomplishes
location: File paths involved
validation: acceptance criteria

Example:

T1: [depends_on: []] Create database schema migration
T2: [depends_on: []] Install required packages
T3: [depends_on: [T1]] Create repository layer
T4: [depends_on: [T1]] Create service interfaces
T5: [depends_on: [T3, T4]] Implement business logic
T6: [depends_on: [T2, T5]] Add API endpoints
T7: [depends_on: [T6]] Write integration tests


Tasks with empty/satisfied dependencies can run in parallel (T1, T2 above).

4. Save Plan

Save to <topic>-plan.md in the CWD.

5. Subagent Review

After saving, spawn a subagent to review the plan:

Review this implementation plan for:
1. Missing dependencies between tasks
2. Ordering issues that would cause failures
3. Missing error handling or edge cases
4. Gaps, holes, gotchas.

Provide specific, actionable feedback. Do not ask questions.

Plan location: [file path]
Context: [brief context about the task]


If the subagent provides actionable feedback, revise the plan before yielding.

Plan Template
# Plan: [Task Name]

**Generated**: [Date]

## Overview
[Summary of task and approach]

## Prerequisites
- [Tools, libraries, access needed]

## Dependency Graph



[Visual representation of task dependencies] T1 ──┬── T3 ──┐ │ ├── T5 ── T6 ── T7 T2 ──┴── T4 ──┘


## Tasks

### T1: [Name]
- **depends_on**: []
- **location**: [file paths]
- **description**: [what to do]
- **validation**: [how to verify]
- **status**: Not Completed
- **log**: [leave empty, to be filled out later]
- **files edited/created**: [leave empty, to be filled out later]

### T2: [Name]
- **depends_on**: []
- **location**: [file paths]
- **description**: [what to do]
- **validation**: [how to verify]
- **status**: Not Completed
- **log**: [leave empty, to be filled out later]
- **files edited/created**: [leave empty, to be filled out later]

### T3: [Name]
- **depends_on**: [T1]
- **location**: [file paths]
- **description**: [what to do]
- **validation**: [how to verify]
- **status**: Not Completed
- **log**: [leave empty, to be filled out later]
- **files edited/created**: [leave empty, to be filled out later]

[... continue for all tasks ...]

## Parallel Execution Groups

| Wave | Tasks | Can Start When |
|------|-------|----------------|
| 1 | T1, T2 | Immediately |
| 2 | T3, T4 | Wave 1 complete |
| 3 | T5 | T3, T4 complete |
| ... | ... | ... |

## Testing Strategy
- [How to test]
- [What to verify]

## Risks & Mitigations
- [What could go wrong + how to handle]

Important
Every task must have explicit depends_on field
Root tasks (no dependencies) can be executed in parallel immediately
Do NOT implement - only create the plan
Always use Context7 for external dependencies before finalizing tasks
Always ask questions where ambiguity exists
Weekly Installs
1.2K
Repository
am-will/codex-skills
GitHub Stars
907
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn