---
rating: ⭐⭐⭐
title: agents-subagents
url: https://skills.sh/vasilyu1983/ai-agents-public/agents-subagents
---

# agents-subagents

skills/vasilyu1983/ai-agents-public/agents-subagents
agents-subagents
Installation
$ npx skills add https://github.com/vasilyu1983/ai-agents-public --skill agents-subagents
SKILL.md
Claude Code Agents

Create and maintain Claude Code agents/subagents with predictable behavior, least-privilege tools, and explicit delegation contracts.

Quick Start
Create an agent file at .claude/agents/<agent-name>.md (kebab-case filename).
Add YAML frontmatter (required: name, description; optional: tools, model, permissionMode, skills, hooks).
Write the agent prompt: responsibilities, workflow, and an output contract.
Minimize tools: start read-only, then add only what the agent truly needs.
Test on a real task and iterate.

Minimal template:

---
name: sql-optimizer
description: Optimize SQL queries, explain tradeoffs, and propose safe indexes
tools: Read, Grep, Glob
model: sonnet
---

# SQL Optimizer

## Responsibilities
- Diagnose bottlenecks using query shape and plans when available
- Propose optimizations with risks and expected impact

## Workflow
1. Identify the slow path and data volume assumptions
2. Propose changes (query rewrite, indexes, stats) with rationale
3. Provide a verification plan

## Output Contract
- Summary (1–3 bullets)
- Recommendations (ordered)
- Verification (commands/tests to run)

Workflow (2026)
Define the agent’s scope and success criteria.
Choose a model based on risk, latency, and cost (default to sonnet for most work).
Choose tools via least privilege; avoid granting Edit/Write unless required.
If delegating with Task, define a handoff contract (inputs, constraints, output format).
Add safety rails for destructive actions and secrets.
Add a verification step (checklist, tests, or a dedicated verifier agent).
Frontmatter Fields (Summary)
name (REQUIRED): kebab-case; match filename (without .md).
description (REQUIRED): state when to invoke + what it does; include keywords users will say.
tools (OPTIONAL): explicit allow-list; prefer small, purpose-built sets.
model (OPTIONAL): haiku for fast checks, sonnet for most tasks, opus for high-stakes reasoning, inherit to match parent.
permissionMode (OPTIONAL): prefer defaults; change only with a clear reason and understand the tradeoffs.
skills (OPTIONAL): preload skill packs for domain expertise; keep the list minimal.
hooks (OPTIONAL): automate guardrails; prefer using the hooks skill for patterns and safety.

For full tool semantics and permission patterns, use references/agent-tools.md. For orchestration and anti-patterns, use references/agent-patterns.md.

2026 Best Practices (Domain Expertise)
Use small, specialized agents; avoid “god agents”.
Keep agent prompts short; put repo conventions in CLAUDE.md/project memory and domain knowledge in skills.
Budget context: pass file paths, minimal snippets, and constraints; avoid dumping long logs/code.
Use explicit handoffs for subagents: “Goal / Constraints / Inputs / Output Contract”.
Add a verifier step for risky changes (security, migrations, infra, auth).
Treat CLI fields/features as moving; verify against official docs in data/sources.json.
Validation Checklist
Frontmatter: name matches filename; description is single-line and trigger-oriented; tools are minimal; model fits risk.
Prompt: responsibilities are concrete; workflow is actionable; output contract is explicit.
Delegation: subagent briefs are specific and bounded; orchestrator verifies integration.
Safety: confirm destructive ops; avoid secrets/PII; follow repository policies.
Navigation
frameworks/shared-skills/skills/agents-subagents/references/agent-patterns.md
frameworks/shared-skills/skills/agents-subagents/references/agent-tools.md
frameworks/shared-skills/skills/agents-subagents/references/subagent-interruption-recovery.md
frameworks/shared-skills/skills/agents-subagents/data/sources.json
frameworks/shared-skills/skills/agents-skills/SKILL.md
frameworks/shared-skills/skills/agents-hooks/SKILL.md
Subagent Interruption Recovery Protocol

Interruptions are normal in multi-agent runs. Treat them as recoverable state transitions, not total failures.

Recovery Loop
Capture partial output from interrupted agent.
Classify interruption cause (manual redirect, timeout, context overflow, tool error).
Decide resume strategy:
resume same agent with narrowed scope, or
spawn replacement agent with explicit handoff from checkpoint.
Prevent duplicate work by marking completed subtasks before rerun.
Re-verify integration assumptions after recovery.
Required Checkpoint Fields
completed work
pending work
owned files
unresolved blocker
next exact command/task
Anti-Pattern

Do not restart full fan-out blindly after one interruption. Resume the smallest affected unit first.

Operational Guardrails: Subagent Orchestration

Use these defaults unless the user explicitly asks for wider fan-out.

Worktree Isolation

For parallel subagent execution, use one Git worktree per agent to prevent file conflicts and index lock contention. See AI Agent Worktrees for setup, directory conventions, safety patterns, and cleanup.

Hard Limits
Keep active subagents <= 3.
Keep each subagent scope to one responsibility and a bounded file set.
Do not let multiple subagents edit the same file in parallel.
Use one worktree per subagent when running parallel agents locally.
Handoff Template (Standard)
Goal:
Constraints:
Owned files:
Do-not-touch files:
Output format:
Definition of done:

Context-Rich Handoff Template (For Parallel/Swarm Execution)

When dispatching multiple subagents from a plan, front-load each agent with structured context. This reduces token usage, tool calls, and drift.

## Context
- Plan: [plan filename or path]
- Goals: [relevant overview from plan — what this task achieves]
- Dependencies: [prerequisite tasks + their outputs/files]
- Related tasks: [sibling tasks and their function]

## Scope
- Files to create/modify: [full paths]
- Files to read (not modify): [paths for reference only]
- Do-not-touch: [files owned by other agents]

## Acceptance Criteria
- [Criterion 1]
- [Criterion 2]
- [Test/verification command]

## Implementation Steps
1. Read the plan at [path] for full context
2. [Concrete step]
3. [Concrete step]
4. Verify: [specific check]


Why this works: Subagents have no prior context. Without front-loaded detail, they spend tokens rediscovering the codebase. With it, they execute focused work immediately.

Wave Dispatch Protocol

When executing plans with dependency graphs, use waves:

Read the dependency graph from the plan.
Identify all tasks with no unmet dependencies (Wave 1).
Launch one subagent per unblocked task (using context-rich handoff template).
Wait for all agents in the wave to complete.
Validate each agent's output before proceeding.
Identify newly unblocked tasks → launch next wave.
Repeat until all tasks complete.

Single-wave shortcut: If only one task is unblocked, launch one agent. Don't force parallelism.

Merge Discipline
Wait for subagent outputs.
Review for overlap/conflicts.
Integrate one subagent result at a time.
Run verification gates before final synthesis.
Conflict Resolution (Parallel Outputs)

When parallel agents produce conflicting changes:

Detect: Check for overlapping file edits, incompatible interface changes, or divergent assumptions.
Prioritize: The agent working on the dependency (upstream task) takes priority for shared interfaces.
Resolve: The orchestrator (not subagents) reconciles conflicts — it has the full plan context.
Re-run if needed: If conflict resolution invalidates a task's output, re-dispatch that single task with updated context.
Document: Record the conflict and resolution in the plan for traceability.
Stop Conditions

Stop and re-plan when:

two subagents propose conflicting edits to same module,
repeated retries happen without new evidence,
context window starts dropping prior decisions,
conflict resolution would require re-running more than half the completed tasks.
Fact-Checking
Use web search/web fetch to verify current external facts, versions, pricing, deadlines, regulations, or platform behavior before final answers.
Prefer primary sources; report source links and dates for volatile information.
If web access is unavailable, state the limitation and mark guidance as unverified.
Weekly Installs
61
Repository
vasilyu1983/ai-…s-public
GitHub Stars
59
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass