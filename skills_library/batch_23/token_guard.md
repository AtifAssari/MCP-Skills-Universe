---
title: token-guard
url: https://skills.sh/aaaaqwq/claude-code-skills/token-guard
---

# token-guard

skills/aaaaqwq/claude-code-skills/token-guard
token-guard
Installation
$ npx skills add https://github.com/aaaaqwq/claude-code-skills --skill token-guard
SKILL.md
Token Guard 💰

Stop burning money while you sleep.

Your AI agent runs 24/7. Opus costs $75/M output tokens. One overnight coding session can burn $50+ before you wake up. Token Guard watches your spend and acts before your wallet notices.

The Problem

Real costs from real users:

Scenario	Model	Cost
"Let the agent run overnight"	Opus	$50-100
"Register an email + X account"	Opus	$55 (one task!)
First week exploring	Opus	$100+
Daily heartbeat checks	Opus	$2-5/day for nothing

Most users don't realize they're burning Opus-level tokens on tasks that Haiku could handle.

What Token Guard Does
Monitor
Track token usage per day/model
Estimate costs from model pricing
Show usage history and trends
Budget
Set daily spending limits
Warning alerts at configurable threshold (default 80%)
Hard limits with auto-model-downgrade
Optimize
Model cost comparison at a glance
Routing recommendations (Opus for reasoning, Haiku for background)
Per-task cost estimation before running
Quick Start
# See current usage and model costs
bash scripts/token-guard.sh status

# Set a $10/day budget with warnings
bash scripts/token-guard.sh set-budget 10

# Set a hard limit: auto-downgrade to Haiku when exceeded
bash scripts/token-guard.sh set-budget 10 80 true claude-haiku-3-5

# Estimate cost before running a task
bash scripts/token-guard.sh estimate claude-opus-4 50000 10000 10

# Check usage history
bash scripts/token-guard.sh history 7

Model Cost Comparison
Model	Input $/1M	Output $/1M	Relative
Claude Opus 4	$15.00	$75.00	100x
Claude Sonnet 4	$3.00	$15.00	20x
Claude Haiku 3.5	$0.80	$4.00	5x
GPT-4o	$2.50	$10.00	13x
Gemini Flash	$0.075	$0.30	1x
DeepSeek	$0.27	$1.10	1.5x
Recommended Routing
Tier 1 (Reasoning/Creative):  claude-opus-4      → Use sparingly
Tier 2 (Daily work):          claude-sonnet-4     → Primary model
Tier 3 (Background/Subagent): claude-haiku-3-5    → Subagent model
Tier 4 (Bulk/Heartbeat):      gemini-2.0-flash    → Heartbeat/cron


Savings: Routing background tasks to Haiku instead of Opus = 95% cost reduction on those tasks.

For AI Agents

Add to your heartbeat or cron:

bash /path/to/token-guard/scripts/token-guard.sh monitor


When budget is exceeded with hard limit enabled, the script automatically downgrades the primary model.

Install
clawdhub install token-guard
# or: git clone https://github.com/jzOcb/token-guard

Requirements
bash 4+
python3
curl
Related
config-guard — Config validation and auto-rollback
upgrade-guard — Safe upgrades with snapshot and auto-rollback
agent-guardrails — Code-level enforcement for AI agents
Weekly Installs
31
Repository
aaaaqwq/claude-…e-skills
GitHub Stars
53
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail