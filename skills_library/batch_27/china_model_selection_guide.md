---
title: china-model-selection-guide
url: https://skills.sh/hexbee/hello-skills/china-model-selection-guide
---

# china-model-selection-guide

skills/hexbee/hello-skills/china-model-selection-guide
china-model-selection-guide
Installation
$ npx skills add https://github.com/hexbee/hello-skills --skill china-model-selection-guide
SKILL.md
China Model Selection Guide

Follow this flow to recommend models. Load references/china-model-selection-guide.md for the full Chinese playbook, scenarios, strengths, and prompt templates.

Quick Triage

Answer two questions first, then give a primary pick.

Identify core input type
Visual-first input (UI mockups, screenshots, sketches): prefer Doubao-Seed-2.0-Code
Very long text or many files (dozens of docs, full codebase): prefer Kimi-K2.5
Structured engineering prompts (clear coding requirements, Shell commands): prefer GLM-5 or MiniMax-M2.5
Identify task complexity
Complex reasoning or autonomous planning (system design, codebase refactor): prefer GLM-5
Cross-language engineering (Python/C++, Java/Go): prefer MiniMax-M2.5
Clear task but heavy execution (UI-to-code, template generation): prefer Doubao-Seed-2.0-Code
Tie-Break Rules

When multiple models fit, decide in this order.

Satisfy hard constraints first: vision, long-context, cross-language, agentic planning
Then compare cost and latency: pick better price/performance at similar quality
Finally split by phase: allow multi-model routing inside one project
Composite Task Routing

Use this default pipeline.

Planning: GLM-5 for architecture, decomposition, interfaces, schema decisions
Build:
Frontend and visual replication: Doubao-Seed-2.0-Code
Backend scripts, cross-language tasks, terminal automation: MiniMax-M2.5
Integration debugging: route hard cross-module issues back to GLM-5
Documentation handoff: send codebase and large document sets to Kimi-K2.5
Output Format

Always include these in recommendations.

Decision: primary model + fallback model
Rationale: map to input type, complexity, and constraints
Risks: likely weak points and rollback strategy
Execution: a ready-to-use prompt draft
References
Full guide and examples (Chinese): references/china-model-selection-guide.md
Weekly Installs
14
Repository
hexbee/hello-skills
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass