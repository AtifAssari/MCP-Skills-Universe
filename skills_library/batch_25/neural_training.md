---
title: neural-training
url: https://skills.sh/ruvnet/ruflo/neural-training
---

# neural-training

skills/ruvnet/ruflo/neural-training
neural-training
Installation
$ npx skills add https://github.com/ruvnet/ruflo --skill neural-training
SKILL.md
Neural Training Skill
Purpose

Train and optimize neural patterns using SONA, MoE, and EWC++ systems.

When to Trigger
Training new patterns
Optimizing agent routing
Knowledge consolidation
Pattern recognition tasks
Intelligence Pipeline
RETRIEVE — Fetch relevant patterns via HNSW (150x-12,500x faster)
JUDGE — Evaluate with verdicts (success$failure)
DISTILL — Extract key learnings via LoRA
CONSOLIDATE — Prevent catastrophic forgetting via EWC++
Components
Component	Purpose	Performance
SONA	Self-optimizing adaptation	<0.05ms
MoE	Expert routing	8 experts
HNSW	Pattern search	150x-12,500x
EWC++	Prevent forgetting	Continuous
Flash Attention	Speed	2.49x-7.47x
Commands
Train Patterns
npx claude-flow neural train --model-type moe --epochs 10

Check Status
npx claude-flow neural status

View Patterns
npx claude-flow neural patterns --type all

Predict
npx claude-flow neural predict --input "task description"

Optimize
npx claude-flow neural optimize --target latency

Best Practices
Use pretrain hook for batch learning
Store successful patterns after completion
Consolidate regularly to prevent forgetting
Route based on task complexity
Weekly Installs
189
Repository
ruvnet/ruflo
GitHub Stars
35.8K
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass