---
title: code-audit
url: https://skills.sh/arjenschwarz/agentic-coding/code-audit
---

# code-audit

skills/arjenschwarz/agentic-coding/code-audit
code-audit
Installation
$ npx skills add https://github.com/arjenschwarz/agentic-coding --skill code-audit
SKILL.md
Code Audit

Parallel codebase quality review that orchestrates the code-simplifier and design-critic skills via subagents, then consolidates and presents findings.

Workflow
Phase 1: Parallel Analysis

Launch two general-purpose subagents in parallel using the Task tool:

Subagent A — Code Simplifier

Prompt the subagent to use the code-simplifier skill (via the Skill tool) against the current working directory. Instruct it to:

Scan source files for complexity hotspots, unnecessary abstractions, and simplification opportunities
Return a structured list of findings, each with: file path, line range, issue summary, suggested fix, and severity (high/medium/low)

Subagent B — Design Critic

Prompt the subagent to use the design-critic skill (via the Skill tool) against the current working directory. Instruct it to:

Review architecture, module boundaries, data flow, and design decisions visible in the code
Return a structured list of findings, each with: scope (file/module/system), issue summary, questions to resolve, and severity (high/medium/low)

Both subagents should focus on the current working directory and respect any project conventions in CLAUDE.md.

Phase 2: Consolidation

After both subagents complete:

Deduplicate overlapping findings (same file + same concern)
Group findings into categories:
Simplification — complexity reduction, readability
Architecture — design issues, module boundaries, abstraction problems
Shared concerns — findings flagged by both analyses
Sort by severity (high first), then by category
Phase 3: Present Report

Present findings to the user in this format:

## Code Audit: {directory name}

### Shared Concerns
{Findings flagged by both subagents — these are highest signal}

### Architecture Issues
{Design critic findings, sorted by severity}

### Simplification Opportunities
{Code simplifier findings, sorted by severity}

### Summary
- {total} findings: {high} high, {medium} medium, {low} low


Each finding should include: location, description, and suggested action.

Phase 4: Transit Tasks

After presenting the report, ask the user if they want Transit tasks created for any findings. If yes:

Create one task per actionable finding (or group related findings into a single task)
Use type chore for simplification items, bug for design issues that could cause problems
Include the finding details in the task description
Use mcp__transit__create_task to create tasks
Weekly Installs
9
Repository
arjenschwarz/ag…c-coding
GitHub Stars
18
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass