---
rating: ⭐⭐
title: mlflow-agent
url: https://skills.sh/mlflow/skills/mlflow-agent
---

# mlflow-agent

skills/mlflow/skills/mlflow-agent
mlflow-agent
Installation
$ npx skills add https://github.com/mlflow/skills --skill mlflow-agent
SKILL.md
MLflow Agent

Master dispatcher for MLflow workflows. Reads user intent and invokes the right sub-skill.

Trigger

Use when the user wants to do anything with MLflow but hasn't specified which skill to use.

Process
Read the user's request and identify intent
Map to the appropriate skill:
Tracing / instrumentation → instrumenting-with-mlflow-tracing
Evaluation / scoring → agent-evaluation
Debug a trace → analyze-mlflow-trace
Debug a chat session → analyze-mlflow-chat-session
Search traces → retrieving-mlflow-traces
Metrics / costs → querying-mlflow-metrics
Getting started → mlflow-onboarding
Docs / API questions → searching-mlflow-docs
If intent is unclear, ask ONE clarifying question, then dispatch
Invoke the matched skill using the Skill tool
Key Rules
Never do the work yourself — always dispatch to the appropriate sub-skill
One clarifying question maximum before dispatching
If the user says "evaluate AND trace", dispatch tracing first, then evaluation
If the user's request spans multiple skills, handle them in logical order (setup → instrument → evaluate)
Weekly Installs
95
Repository
mlflow/skills
GitHub Stars
36
First Seen
Mar 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass