---
rating: ⭐⭐⭐
title: openclaw-self-healing
url: https://skills.sh/ramsbaby/openclaw-self-healing/openclaw-self-healing
---

# openclaw-self-healing

skills/ramsbaby/openclaw-self-healing/openclaw-self-healing
openclaw-self-healing
Installation
$ npx skills add https://github.com/ramsbaby/openclaw-self-healing --skill openclaw-self-healing
Summary

4-tier autonomous self-healing system for OpenClaw Gateway with Claude Code as AI emergency doctor.

Escalates through watchdog monitoring, HTTP health checks with retries, AI-powered diagnosis via Claude Code, and Discord/Telegram alerts for human intervention
Captures persistent learning documentation (symptom to solution mappings) and reasoning logs for explainable AI decision-making
Includes metrics dashboard for tracking recovery success rates, timing, and trends across incidents
Requires tmux, Claude Code CLI, and jq; integrates with macOS LaunchAgent for continuous background operation
SKILL.md
OpenClaw Self-Healing System

"The system that heals itself — or calls for help when it can't."

A 4-tier autonomous self-healing system for OpenClaw Gateway.

Architecture
Level 1: Watchdog (180s)     → Process monitoring (OpenClaw built-in)
Level 2: Health Check (300s) → HTTP 200 + 3 retries
Level 3: Claude Recovery     → 30min AI-powered diagnosis 🧠
Level 4: Discord Alert       → Human escalation

What's Special (v2.0)
World's first Claude Code as Level 3 emergency doctor
Persistent Learning - Automatic recovery documentation (symptom → cause → solution → prevention)
Reasoning Logs - Explainable AI decision-making process
Multi-Channel Alerts - Discord + Telegram support
Metrics Dashboard - Success rate, recovery time, trending analysis
Production-tested (verified recovery Feb 5-6, 2026)
macOS LaunchAgent integration
Quick Setup
1. Install Dependencies
brew install tmux
npm install -g @anthropic-ai/claude-code

2. Configure Environment
# Copy template to OpenClaw config directory
cp .env.example ~/.openclaw/.env

# Edit and add your Discord webhook (optional)
nano ~/.openclaw/.env

3. Install Scripts
# Copy scripts
cp scripts/*.sh ~/openclaw/scripts/
chmod +x ~/openclaw/scripts/*.sh

# Install LaunchAgent
cp launchagent/com.openclaw.healthcheck.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.openclaw.healthcheck.plist

4. Verify
# Check Health Check is running
launchctl list | grep openclaw.healthcheck

# View logs
tail -f ~/openclaw/memory/healthcheck-$(date +%Y-%m-%d).log

Scripts
Script	Level	Description
gateway-healthcheck.sh	2	HTTP 200 check + 3 retries + escalation
emergency-recovery.sh	3	Claude Code PTY session for AI diagnosis (v1)
emergency-recovery-v2.sh	3	Enhanced with learning + reasoning logs (v2) ⭐
emergency-recovery-monitor.sh	4	Discord/Telegram notification on failure
metrics-dashboard.sh	-	Visualize recovery statistics (NEW)
Configuration

All settings via environment variables in ~/.openclaw/.env:

Variable	Default	Description
DISCORD_WEBHOOK_URL	(none)	Discord webhook for alerts
OPENCLAW_GATEWAY_URL	http://localhost:18789/	Gateway health check URL
HEALTH_CHECK_MAX_RETRIES	3	Restart attempts before escalation
EMERGENCY_RECOVERY_TIMEOUT	1800	Claude recovery timeout (30 min)
Testing
Test Level 2 (Health Check)
# Run manually
bash ~/openclaw/scripts/gateway-healthcheck.sh

# Expected output:
# ✅ Gateway healthy

Test Level 3 (Claude Recovery)
# Inject a config error (backup first!)
cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.bak

# Wait for Health Check to detect and escalate (~8 min)
tail -f ~/openclaw/memory/emergency-recovery-*.log

Links
GitHub: https://github.com/Ramsbaby/openclaw-self-healing
Docs: https://github.com/Ramsbaby/openclaw-self-healing/tree/main/docs
License

MIT License - do whatever you want with it.

Built by @ramsbaby + Jarvis 🦞

Weekly Installs
837
Repository
ramsbaby/opencl…-healing
GitHub Stars
36
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketFail
SnykWarn