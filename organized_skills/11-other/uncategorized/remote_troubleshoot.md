---
rating: ⭐⭐⭐
title: remote-troubleshoot
url: https://skills.sh/iceleaf916/my-cc-plugins/remote-troubleshoot
---

# remote-troubleshoot

skills/iceleaf916/my-cc-plugins/remote-troubleshoot
remote-troubleshoot
Installation
$ npx skills add https://github.com/iceleaf916/my-cc-plugins --skill remote-troubleshoot
SKILL.md
Remote Server Troubleshooting
Overview

Provides a structured workflow for troubleshooting issues on remote servers with emphasis on:

Investigation-only approach until user approval
Creating reusable helper scripts on remote server
Script-based fixes for reproducibility
Comprehensive analysis and resolution reports
Investigation Workflow
Phase 0: Information Gathering

Before starting any investigation, gather:

Remote Server Access

Server address/IP
SSH method (sshpass, keys, etc.) and credentials
Remote user

Problem Description

What is the exact issue?
When did it start?
What service/component is affected?

Context

Environment (k8s, bare metal, containerized)
Relevant config file locations
Recent changes
Phase 1: Initial Verification (Read-Only)

CRITICAL: Do NOT make any changes without user approval

Validate the reported issue actually exists:

sshpass -p<password> ssh -o StrictHostKeyChecking=no user@host "echo 'OK'"
ssh user@host "ss -tlnp | grep :<port>"
ssh user@host "systemctl status <service>"
ssh user@host "kubectl get pods -n <namespace>"


If issue cannot be reproduced, inform user and ask clarification.

Phase 2: Create Investigation Environment
ssh user@host "mkdir -p ~/troubleshoot-$(date +%Y%m%d)"

Phase 3: Deploy Helper Scripts

Generate and upload investigation scripts. Use scripts/generate_helper.sh.

Common scenarios: service status, ports, config inspection, logs.

Always execute investigation scripts, never modify actions.

Phase 4: Execute Investigation

Run helper scripts. Document:

Current state (what IS happening)
Expected state (what SHOULD happen)
Differences (the gap)
Phase 5: Analysis and Root Cause

Synthesize findings to identify root cause. Consider multiple hypotheses if unclear.

Phase 6: Propose Solution

Present to user:

Root Cause Summary
Proposed Fix (step-by-step)
Risk Assessment
Rollback Plan

WAIT for user approval before proceeding to repair.

Repair Workflow
Phase 7: Create Fix Script

Script the fix procedure. Fix script MUST:

Create backups before modifying
Apply changes in safe steps
Verify after each step
Report results clearly
Phase 8: Apply Fix
cat fix-script.sh | ssh user@host "bash -s"

Phase 9: Verification

Confirm fix resolved the issue:

Re-run initial validation
Check service/operation
Monitor logs
Phase 10: Generate Report

Use assets/report-template.md to create analysis report.

Scenarios and Patterns

See references/patterns.md for:

K8s troubleshooting patterns
Network/port issues
Service failures
Configuration mismatches
Quick Reference
# Service
systemctl status <service>
systemctl is-active <service>

# Port
ss -tlnp | grep :<port>

# Process
ps aux | grep <name>

# Logs
journalctl -u <service> -n 50 --no-pager
tail -f /var/log/<service>.log

# K8s
kubectl get pods -n <namespace>
kubectl describe pod <name> -n <namespace>
kubectl logs <pod> -n <namespace>

Resources
scripts/
generate_helper.sh - Generate investigation helper scripts
generate_fix.sh - Generate fix script templates
references/
patterns.md - Common investigation patterns
report_guide.md - Report structure guide
assets/
report-template.md - Markdown report template
Weekly Installs
11
Repository
iceleaf916/my-cc-plugins
GitHub Stars
6
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail