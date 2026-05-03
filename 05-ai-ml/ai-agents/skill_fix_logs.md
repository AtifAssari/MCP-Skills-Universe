---
title: skill-fix-logs
url: https://skills.sh/duc01226/easyplatform/skill-fix-logs
---

# skill-fix-logs

skills/duc01226/easyplatform/skill-fix-logs
skill-fix-logs
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill skill-fix-logs
SKILL.md

[IMPORTANT] Use TaskCreate to break ALL work into small tasks BEFORE starting.

Quick Summary

Goal: Fix a skill based on error analysis from its logs.txt file.

Workflow:

Read — Analyze the skill's logs.txt for errors and failures
Diagnose — Identify root cause of skill malfunction
Fix — Apply corrections to SKILL.md, scripts, or references
Verify SYNC compliance — Ensure fix doesn't break SYNC tag balance or remove inline protocols
Enhance — Call /prompt-enhance on the fixed SKILL.md if structural changes were made
Test — Run the skill again to verify fix

Key Rules:

Focus on the specific errors reported in logs
When fixing SKILL.md structure: maintain SYNC tag balance, keep inline protocols
MUST ATTENTION call /prompt-enhance if structural changes were made to SKILL.md
STOP after 3 failed fix attempts — report outcomes, ask user before #4
Mission

Fix the agent skill based on logs.txt file (project root).

$ARGUMENTS

Rules
If given nothing → use AskUserQuestion for clarifications
If given a URL → use Explore subagent to explore all internal links
If given a GitHub URL → use repomix + parallel Explore subagents
When modifying SKILL.md: verify <!-- SYNC:tag --> blocks remain balanced
Reference canonical protocols: .claude/skills/shared/sync-inline-versions.md
Closing Reminders
IMPORTANT MUST ATTENTION break work into small todo tasks using TaskCreate BEFORE starting
IMPORTANT MUST ATTENTION preserve SYNC tag balance when editing SKILL.md
IMPORTANT MUST ATTENTION call /prompt-enhance on SKILL.md after structural fixes
IMPORTANT MUST ATTENTION STOP after 3 failed fix attempts — report outcomes, ask user before #4
IMPORTANT MUST ATTENTION cite file:line evidence for every claim (confidence >80% to act)
Weekly Installs
34
Repository
duc01226/easyplatform
GitHub Stars
6
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn