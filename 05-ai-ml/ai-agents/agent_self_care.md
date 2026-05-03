---
rating: ⭐⭐
title: agent-self-care
url: https://skills.sh/ljt-520/openclaw-backup/agent-self-care
---

# agent-self-care

skills/ljt-520/openclaw-backup/agent-self-care
agent-self-care
Installation
$ npx skills add https://github.com/ljt-520/openclaw-backup --skill agent-self-care
SKILL.md
Agent Self-Care

Autonomous health monitoring and optimization for OpenClaw agents. Runs on cron or triggers manually.

Workflow
1. Check Sub-Agents
subagents action=list


Kill any stale sub-agents:

Running >30 min without progress
In "waiting" state
Failed/errored
2. Check Processes
process action=list


Kill hanging processes:

Running >10 min in background
No output in 5 min
3. Check Session Health
session_status


Metrics to watch:

Context usage >80% → trigger compaction
Tokens growing unbounded
Session age >2 hours → suggest refresh
4. Run Optimization Script

Execute scripts/optimize.sh which:

Clears completed cron job artifacts
Rotates logs if >50MB
Reports health metrics
5. BMAD Retrospective (every 10 runs)

After 10 executions, run:

Score last task 1-10
Identify gaps
Document improvements in memory/daily/YYYY-MM-DD.md
Feed learnings into next run
Cron Schedule

Recommended: Every 5 minutes for active agents.

{
  "name": "agent-self-care",
  "schedule": {"kind": "every", "everyMs": 300000},
  "payload": {"kind": "agentTurn", "message": "Run agent-self-care skill"},
  "sessionTarget": "isolated",
  "enabled": true
}

Output Format

Report after each run:

🔧 Self-Care Report
- Sub-agents: X active, Y killed
- Processes: X running, Y cleared
- Context: X% used
- Health: ✅ GOOD / ⚠️ WARNING
- Retrospective: SKIP / COMPLETE

Key Principles
Always clean - Never leave stalled sub-agents or processes
Proactive - Don't wait for user to ask
Document - Log issues and improvements
BMAD - Continuous self-evaluation every 10 runs
Fast - Complete in <30 seconds
Weekly Installs
9
Repository
ljt-520/openclaw-backup
GitHub Stars
1
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn