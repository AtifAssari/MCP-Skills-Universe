---
title: agent-harness-construction
url: https://skills.sh/affaan-m/everything-claude-code/agent-harness-construction
---

# agent-harness-construction

skills/affaan-m/everything-claude-code/agent-harness-construction
agent-harness-construction
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill agent-harness-construction
Summary

Design and optimize AI agent action spaces, tool definitions, and observation formatting for higher completion rates.

Action space quality depends on stable tool names, narrow input schemas, deterministic outputs, and avoiding catch-all tools; granularity should match operation risk (micro-tools for high-risk, macro-tools only when round-trip cost dominates.
Observation design requires every tool response to include status, summary, next_actions, and artifacts; error paths must provide root cause hints, safe retry instructions, and explicit stop conditions.
Context budgeting keeps system prompts minimal, moves large guidance into on-demand skills, and prefers file references over inlining; compaction happens at phase boundaries, not arbitrary token thresholds.
Recommends hybrid architecture combining ReAct planning with typed tool execution; track completion rate, retries per task, pass@1/pass@3, and cost per successful task to measure effectiveness.
SKILL.md
Agent Harness Construction

Use this skill when you are improving how an agent plans, calls tools, recovers from errors, and converges on completion.

Core Model

Agent output quality is constrained by:

Action space quality
Observation quality
Recovery quality
Context budget quality
Action Space Design
Use stable, explicit tool names.
Keep inputs schema-first and narrow.
Return deterministic output shapes.
Avoid catch-all tools unless isolation is impossible.
Granularity Rules
Use micro-tools for high-risk operations (deploy, migration, permissions).
Use medium tools for common edit/read/search loops.
Use macro-tools only when round-trip overhead is the dominant cost.
Observation Design

Every tool response should include:

status: success|warning|error
summary: one-line result
next_actions: actionable follow-ups
artifacts: file paths / IDs
Error Recovery Contract

For every error path, include:

root cause hint
safe retry instruction
explicit stop condition
Context Budgeting
Keep system prompt minimal and invariant.
Move large guidance into skills loaded on demand.
Prefer references to files over inlining long documents.
Compact at phase boundaries, not arbitrary token thresholds.
Architecture Pattern Guidance
ReAct: best for exploratory tasks with uncertain path.
Function-calling: best for structured deterministic flows.
Hybrid (recommended): ReAct planning + typed tool execution.
Benchmarking

Track:

completion rate
retries per task
pass@1 and pass@3
cost per successful task
Anti-Patterns
Too many tools with overlapping semantics.
Opaque tool output with no recovery hints.
Error-only output without next steps.
Context overloading with irrelevant references.
Weekly Installs
3.0K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass