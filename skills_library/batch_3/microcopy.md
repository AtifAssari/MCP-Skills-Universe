---
title: microcopy
url: https://skills.sh/lobehub/lobehub/microcopy
---

# microcopy

skills/lobehub/lobehub/microcopy
microcopy
Installation
$ npx skills add https://github.com/lobehub/lobehub --skill microcopy
Summary

Collaborative agent UI copy guidelines for LobeHub, covering buttons, errors, onboarding, and user-facing text in English and Chinese.

Fixed terminology table ensures consistency across 18 key terms (Workspace, Agent, Integration, etc.) in both languages
Brand principles emphasize clarity, multi-agent collaboration, and explainability; writing rules favor short sentences, strong verbs, and actionable next steps
Human warmth calibrated to context: 80/20 information-to-warmth by default, shifting to 70/30 for first-time users, empty states, failures, and long waits
Error messaging framework requires three elements: what happened, optional explanation, and clear next action (Retry, View details, Settings, or support)
Includes ready-to-use copy patterns for getting started, long waits, failures, and collaboration scenarios
SKILL.md
LobeHub UI Microcopy Guidelines

Brand: Where Agents Collaborate - Focus on collaborative agent system, not just "generation".

Fixed Terminology
Chinese	English
空间	Workspace
助理	Agent
群组	Group
上下文	Context
记忆	Memory
连接器	Integration
技能	Skill
助理档案	Agent Profile
话题	Topic
文稿	Page
社区	Community
资源	Resource
库	Library
模型服务商	Provider
评测	Evaluation
基准	Benchmark
数据集	Dataset
用例	Test Case
Brand Principles
Create: One sentence → usable Agent; clear next step
Collaborate: Multi-agent; shared Context; controlled
Evolve: Remember with consent; explainable; replayable
Writing Rules
Clarity first: Short sentences, strong verbs, minimal adjectives
Layered: Main line (simple) + optional detail (precise)
Consistent verbs: Create / Connect / Run / Pause / Retry / View details
Actionable: Every message tells next step; avoid generic "OK/Cancel"
Human Warmth (Balanced)

Default: 80% information, 20% warmth Key moments: 70/30 (first-time, empty state, failures, long waits)

Hard cap: At most half sentence of warmth, followed by clear next step.

Order:

Acknowledge situation (no judgment)
Restore control (pause/replay/edit/undo/clear Memory)
Provide next action

Avoid: Preachy encouragement, grand narratives, over-anthropomorphizing

Patterns

Getting started:

"Starting with one sentence is enough. Describe your goal."
"Not sure where to begin? Tell me the outcome."

Long wait:

"Running… You can switch tasks—I'll notify you when done."
"This may take a few minutes. To speed up: reduce Context / switch model."

Failure:

"That didn't run through. Retry, or view details to fix."
"Connection failed. Re-authorize in Settings, or try again later."

Collaboration:

"Align everyone to the same Context."
"Different opinions are fine. Write the goal first."
Errors/Exceptions

Must include:

What happened
(Optional) Why
What user can do next

Provide: Retry / View details / Go to Settings / Contact support / Copy logs

Never blame user. Put error codes in "Details".

Weekly Installs
748
Repository
lobehub/lobehub
GitHub Stars
75.9K
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass