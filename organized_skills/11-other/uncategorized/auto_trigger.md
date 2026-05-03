---
rating: ⭐⭐
title: auto-trigger
url: https://skills.sh/charon-fan/agent-playbook/auto-trigger
---

# auto-trigger

skills/charon-fan/agent-playbook/auto-trigger
auto-trigger
Installation
$ npx skills add https://github.com/charon-fan/agent-playbook --skill auto-trigger
SKILL.md
Auto-Trigger Hooks

This skill defines automatic trigger relationships between skills. When a skill completes its workflow, it should automatically trigger the next skill in the chain.

Hook Definitions
PRD Creation Chain
prd_complete:
  triggers:
    - skill: self-improving-agent
      mode: background
      condition: PRD file exists and is complete
    - skill: session-logger
      mode: auto
      context: "PRD created for {feature_name}"

prd_implemented:
  triggers:
    - skill: session-logger
      mode: auto
      context: "Implemented PRD: {feature_name}"

Implementation Chain
implementation_complete:
  triggers:
    - skill: code-reviewer
      mode: ask_first
      message: "Implementation complete. Run code review?"
    - skill: create-pr
      mode: auto
      condition: changes_staged

Session Management
session_start:
  auto_triggers:
    - skill: session-logger
      action: create_session_file

session_end:
  auto_triggers:
    - skill: session-logger
      action: update_session_file

Hook Format in Skills

To add auto-trigger capability to a skill, add to its front matter:

---
name: my-skill
description: Skill description
allowed-tools: Read, Write, Edit
hooks:
  before_start:
    - trigger: session-logger
      mode: auto
      context: "Start {skill_name}"
  after_complete:
    - trigger: self-improving-agent
      mode: background
    - trigger: session-logger
      mode: auto
  on_error:
    - trigger: self-improving-agent
      mode: background
---

Implementation Guide

When a skill completes its workflow:

Check hooks in its own front matter (before_start, after_complete, on_error, on_progress)
For each hook:
If mode: auto, trigger immediately
If mode: background, trigger without waiting
If mode: ask_first, ask user before triggering
If condition: exists, check it first
Pass context to the triggered skill
Example Integration
prd-planner should add:
---
name: prd-planner
description: Creates PRDs using persistent file-based planning...
allowed-tools: Read, Write, Edit, Bash, Grep, Glob, AskUserQuestion, WebSearch
hooks:
  after_complete:
    - trigger: self-improving-agent
      mode: background
      context: "PRD created at {prd_file}"
    - trigger: session-logger
      mode: auto
      context: "PRD creation complete"
---

self-improving-agent already has:
---
name: self-improving-agent
description: Universal self-improvement that learns from all skill experiences...
allowed-tools: Read, Write,Edit, Bash, Grep, Glob, WebSearch
hooks:
  after_complete:
    - trigger: create-pr
      mode: ask_first
      condition: skills_modified
    - trigger: session-logger
      mode: auto
      context: "Self-improvement cycle complete"
  on_error:
    - trigger: self-improving-agent
      mode: background
---

create-pr should add:
---
name: create-pr
description: Creates pull requests with bilingual documentation updates...
allowed-tools: Read, Write, Edit, Bash, Grep, AskUserQuestion
hooks:
  after_complete:
    - trigger: session-logger
      mode: auto
      context: "PR created: {pr_title}"
---

Chain Visualization
┌──────────────┐
│ prd-planner  │
└──────┬───────┘
       │ after_complete
       ├──→ self-improving-agent (background)
       │         └──→ create-pr (ask_first)
       │                  └──→ session-logger (auto)
       └──→ session-logger (auto)

Error Correction Chain
on_error:
  triggers:
    - skill: self-improving-agent
      mode: background
      context: "Error occurred in {skill_name}"
    - skill: session-logger
      mode: auto
      context: "Error captured for {skill_name}"

Important Rules
Don't create infinite loops - Ensure chains terminate
Ask before major actions - Use mode: ask_first for PRs, deployments
Background tasks - Use mode: background for non-blocking tasks
Pass context - Always include relevant context to triggered skills
Weekly Installs
433
Repository
charon-fan/agen…playbook
GitHub Stars
49
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass