---
rating: ⭐⭐⭐
title: agentic-workflow-guide
url: https://skills.sh/aktsmm/agent-skills/agentic-workflow-guide
---

# agentic-workflow-guide

skills/aktsmm/agent-skills/agentic-workflow-guide
agentic-workflow-guide
Installation
$ npx skills add https://github.com/aktsmm/agent-skills --skill agentic-workflow-guide
SKILL.md
Agentic Workflow Guide

Design, review, and improve agent workflows based on proven principles.

この SKILL の基本姿勢は、agent を増やすことではなく、必要最小の primitive で解くこと。 context が膨らんだときも、まずは split / compact / reference 化を考え、いきなり multi-agent にしない。

Primitive First

Do not start with multi-agent by default.

Single focused slash task -> Prompt
Always-on or file-scoped guidance -> Instruction
Reusable workflow with bundled assets -> Skill
Persona, tool restrictions, delegation, or handoffs -> Agent
Deterministic enforcement -> Hook

If the ask does not require an Agent, stop and use the simpler primitive.

Selection details: references/customization-decision.md

When to Use
Action	Triggers
Create	New .agent.md, workflow architecture, scaffolding
Review	Orchestrator not delegating, design principle check, context overflow
Update	Adding Handoffs, improving delegation, tool configuration
Debug	Agent not found, subagent not working, picker visibility, access control
Decide	Determining whether multi-agent is justified or a simpler primitive is enough
Core Principles
Simplicity First: より単純な primitive で解けるなら agent 化しない
SSOT / SRP: 情報源と責務の分割を守る
Fail Fast: エラーは早く止める
Feedback Loop: 各段で検証できるようにする
Context Discipline: context が膨らんだら compact / split / retrieve を検討する

Principle details: references/design-principles.md

Pattern Selection
Prompt Chaining: 順序のある段階処理
Routing: 入力タイプで分岐する処理
Parallelization: 独立タスクを並列で進める処理
Orchestrator-Workers: 動的に subtasks を分解する処理
Evaluator-Optimizer: 品質基準を満たすまで反復する処理

Every loop needs explicit stop conditions.

Pattern details: references/workflow-patterns/overview.md

Design Workflow
Extract from conversation Repeated behavior, tool preferences, workflow shape, and obvious specialization を先に拾う。
Choose primitive + scope Prompt / instruction / skill / agent / hook と workspace / profile を決める。
Clarify only the gaps 挙動を変える曖昧さだけ聞く。
Check escalation agent や multi-agent が本当に必要か確認する。
Choose pattern complexity が上がるなら pattern を明示して設計する。
Review before expanding split / compact / reference 化で済まないかを見る。
Implement and iterate 最初から完成形を狙わず、弱い箇所を見つけて詰める。
Escalation Rules
L0: Single Prompt
L1: Prompt + Instructions
L2: Single Agent
L3: Multi-Agent

Prefer the lowest level that solves the problem cleanly.

Quick signals:

Prompt > 50 lines
Steps > 5
"missed" / "overlooked" errorsが続く
Multiple responsibilities in one agent
Context > 70%

Threshold details: references/splitting-criteria.md

Review Gates
 Primitive choice is simpler than agent if possible
 Single responsibility per agent is preserved
 Errors can be detected and stopped early
 Results are verifiable at each step
 Context can be compacted or split before adding more orchestration

Full checklist: references/review-checklist.md

Reference Map
Topic	Reference
Primitive decision	references/customization-decision.md
Design principles	references/design-principles.md
Workflow patterns	references/workflow-patterns/overview.md
Splitting criteria	references/splitting-criteria.md
Review checklist	references/review-checklist.md
Context management	references/context-engineering.md
Agent guide / template	references/agent-guide.md, references/agent-template.md
Handoffs / placement	references/handoffs-guide.md, references/vscode-agent-placement.md
Hooks	references/hooks-guide.md
Evaluation	references/agent-evaluation.md
Examples / scaffold	references/scaffold-usage.md, references/examples/
External links	references/external-resources.md
External References

Keep a small curated set here for first-hop reading. The longer link list stays in references/external-resources.md.

GitHub Docs: Chat in IDE
VS Code Docs: Custom Agents
GitHub Docs: Create custom agents
Anthropic: Building Effective Agents
Anthropic: Effective Context Engineering
Anthropic: Writing Tools for Agents
agent Quick Fix

Problem: Orchestrator says "I'll delegate" but does work directly.

Solution: Use MUST/MANDATORY language. See agent-guide.md.

## MANDATORY: Sub-agent Delegation
You MUST use agent for each file. Do NOT read files directly.

Tools Reference

→ references/agent-template.md

Purpose	VS Code Copilot	Claude Code
Shell	execute/runInTerminal	Bash
Read	read/readFile	Read
Edit	edit/editFiles	Write
Subagent	agent	Task
Web fetch	web/fetch	(MCP)
Done Criteria
 Primitive and scope selected intentionally
 Workflow pattern selected and confirmed with user
 .agent.md file created with clear Role/Workflow/Done Criteria
 Design principles checklist passed
 Agent registered in AGENTS.md (if applicable)
Weekly Installs
96
Repository
aktsmm/agent-skills
GitHub Stars
11
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn