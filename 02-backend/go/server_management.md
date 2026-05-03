---
rating: ⭐⭐
title: server-management
url: https://skills.sh/sickn33/antigravity-awesome-skills/server-management
---

# server-management

skills/sickn33/antigravity-awesome-skills/server-management
server-management
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill server-management
Summary

Framework for production server operations covering process management, monitoring, logging, and scaling decisions.

Covers seven core operational areas: process management tool selection (PM2, systemd, Docker, Kubernetes), monitoring strategy with severity-based alerting, and structured log rotation practices
Provides decision matrices for scaling (vertical vs. horizontal vs. auto-scaling), health check depth, and troubleshooting priority order
Emphasizes principles over commands: auto-recovery, zero-downtime reloads, resource awareness, and security fundamentals like SSH keys and secret management
Includes anti-patterns section highlighting common mistakes (running as root, skipping monitoring, manual restarts) with recommended alternatives
SKILL.md
Server Management

Server management principles for production operations. Learn to THINK, not memorize commands.

1. Process Management Principles
Tool Selection
Scenario	Tool
Node.js app	PM2 (clustering, reload)
Any app	systemd (Linux native)
Containers	Docker/Podman
Orchestration	Kubernetes, Docker Swarm
Process Management Goals
Goal	What It Means
Restart on crash	Auto-recovery
Zero-downtime reload	No service interruption
Clustering	Use all CPU cores
Persistence	Survive server reboot
2. Monitoring Principles
What to Monitor
Category	Key Metrics
Availability	Uptime, health checks
Performance	Response time, throughput
Errors	Error rate, types
Resources	CPU, memory, disk
Alert Severity Strategy
Level	Response
Critical	Immediate action
Warning	Investigate soon
Info	Review daily
Monitoring Tool Selection
Need	Options
Simple/Free	PM2 metrics, htop
Full observability	Grafana, Datadog
Error tracking	Sentry
Uptime	UptimeRobot, Pingdom
3. Log Management Principles
Log Strategy
Log Type	Purpose
Application logs	Debug, audit
Access logs	Traffic analysis
Error logs	Issue detection
Log Principles
Rotate logs to prevent disk fill
Structured logging (JSON) for parsing
Appropriate levels (error/warn/info/debug)
No sensitive data in logs
4. Scaling Decisions
When to Scale
Symptom	Solution
High CPU	Add instances (horizontal)
High memory	Increase RAM or fix leak
Slow response	Profile first, then scale
Traffic spikes	Auto-scaling
Scaling Strategy
Type	When to Use
Vertical	Quick fix, single instance
Horizontal	Sustainable, distributed
Auto	Variable traffic
5. Health Check Principles
What Constitutes Healthy
Check	Meaning
HTTP 200	Service responding
Database connected	Data accessible
Dependencies OK	External services reachable
Resources OK	CPU/memory not exhausted
Health Check Implementation
Simple: Just return 200
Deep: Check all dependencies
Choose based on load balancer needs
6. Security Principles
Area	Principle
Access	SSH keys only, no passwords
Firewall	Only needed ports open
Updates	Regular security patches
Secrets	Environment vars, not files
Audit	Log access and changes
7. Troubleshooting Priority

When something's wrong:

Check if running (process status)
Check logs (error messages)
Check resources (disk, memory, CPU)
Check network (ports, DNS)
Check dependencies (database, APIs)
8. Anti-Patterns
❌ Don't	✅ Do
Run as root	Use non-root user
Ignore logs	Set up log rotation
Skip monitoring	Monitor from day one
Manual restarts	Auto-restart config
No backups	Regular backup schedule

Remember: A well-managed server is boring. That's the goal.

When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
513
Repository
sickn33/antigra…e-skills
GitHub Stars
36.0K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass