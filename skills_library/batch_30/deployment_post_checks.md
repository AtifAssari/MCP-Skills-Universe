---
title: deployment-post-checks
url: https://skills.sh/jsonlee12138/easy-deployment/deployment-post-checks
---

# deployment-post-checks

skills/jsonlee12138/easy-deployment/deployment-post-checks
deployment-post-checks
Installation
$ npx skills add https://github.com/jsonlee12138/easy-deployment --skill deployment-post-checks
SKILL.md
Deployment Post Checks
Read smoke result JSON.
Optionally merge metrics result JSON.
Apply thresholds and return success or rollback-required status.
Command
python3 skills/deployment-post-checks/scripts/post_check.py --smoke-file smoke.json
python3 skills/deployment-post-checks/scripts/post_check.py --smoke-file smoke.json --metrics-file metrics.json --min-success-rate 99 --max-p95-latency 500

Weekly Installs
8
Repository
jsonlee12138/ea…ployment
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass