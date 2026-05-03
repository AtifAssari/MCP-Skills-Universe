---
title: enterprise-agent-ops
url: https://skills.sh/affaan-m/everything-claude-code/enterprise-agent-ops
---

# enterprise-agent-ops

skills/affaan-m/everything-claude-code/enterprise-agent-ops
enterprise-agent-ops
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill enterprise-agent-ops
Summary

Operational controls for long-lived agent workloads with observability, security, and lifecycle management.

Covers four operational domains: runtime lifecycle (start, pause, stop, restart), observability (logs, metrics, traces), safety controls (scopes, permissions, kill switches), and change management (rollout, rollback, audit)
Enforces baseline controls including immutable deployment artifacts, least-privilege credentials, environment-level secret injection, and hard timeouts with retry budgets
Tracks key metrics: success rate, mean retries per task, time to recovery, cost per task, and failure class distribution
Includes structured incident response: freeze rollouts, capture traces, isolate failures, patch safely, run regression and security checks, then resume gradually
Integrates with PM2, systemd, container orchestrators, and CI/CD gates
SKILL.md
Enterprise Agent Ops

Use this skill for cloud-hosted or continuously running agent systems that need operational controls beyond single CLI sessions.

Operational Domains
runtime lifecycle (start, pause, stop, restart)
observability (logs, metrics, traces)
safety controls (scopes, permissions, kill switches)
change management (rollout, rollback, audit)
Baseline Controls
immutable deployment artifacts
least-privilege credentials
environment-level secret injection
hard timeout and retry budgets
audit log for high-risk actions
Metrics to Track
success rate
mean retries per task
time to recovery
cost per successful task
failure class distribution
Incident Pattern

When failure spikes:

freeze new rollout
capture representative traces
isolate failing route
patch with smallest safe change
run regression + security checks
resume gradually
Deployment Integrations

This skill pairs with:

PM2 workflows
systemd services
container orchestrators
CI/CD gates
Weekly Installs
2.6K
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