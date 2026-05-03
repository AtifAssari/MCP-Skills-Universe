---
rating: ⭐⭐
title: go
url: https://skills.sh/anntnzrb/agents/go
---

# go

skills/anntnzrb/agents/go
go
Installation
$ npx skills add https://github.com/anntnzrb/agents --skill go
SKILL.md
Go Orchestration Skill

Execute the plan using multi-level parallelism.

Context
Extract the plan from previous messages (source of truth)
If a todo-list tool exists, use it as supplementary reference, but prioritize the conversational plan
Optional arguments provide additional context: $ARGUMENTS
Step 1 - Analyze dependencies
Identify independent tasks (can run in parallel)
Identify dependent tasks (must wait)
Group into phases; each phase contains only independent tasks
Step 2 - Orchestrate
For each phase, spawn multiple subagents concurrently using parallel spawn_agent tool calls
Each subagent prompt must include:
Full context (architectural decisions, patterns, constraints from planning)
Specific task, files, and acceptance criteria
Instruction: "Batch ALL independent tool calls in a single message"
Expected return: "Return only: OK [confirmation] or BLOCKER [blocker]"
Step 3 - Execute phases
Phase N: spawn all independent agents in one parallel batch
Wait for phase completion
Phase N+1: spawn next batch (may depend on Phase N results)
On failure: stop, report blocker, await decision
Rules
Orchestration only; do not perform file operations directly
No redundant explanations; the plan is already understood
Compact output: report phases, agents spawned, and final status
Weekly Installs
11
Repository
anntnzrb/agents
GitHub Stars
1
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass