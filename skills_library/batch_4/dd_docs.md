---
title: dd-docs
url: https://skills.sh/datadog-labs/agent-skills/dd-docs
---

# dd-docs

skills/datadog-labs/agent-skills/dd-docs
dd-docs
Installation
$ npx skills add https://github.com/datadog-labs/agent-skills --skill dd-docs
SKILL.md
Datadog Docs

Use this skill to locate Datadog documentation and limits.

LLM-Friendly Documentation

Datadog provides an LLM-optimized documentation index at:

https://docs.datadoghq.com/llms.txt


This file contains:

Overview of all Datadog products organized by use case
Full list of documentation pages with URLs and descriptions
Direct links to Markdown sources (append .md to URLs)
How to Use llms.txt

Fetch the index to understand available documentation:

curl -s https://docs.datadoghq.com/llms.txt | head -100


Search for specific topics:

Examples:

curl -s https://docs.datadoghq.com/llms.txt | grep -i "monitors"
curl -s https://docs.datadoghq.com/llms.txt | grep -i "apm"
curl -s https://docs.datadoghq.com/llms.txt | grep -i "logs"

Fetch specific doc pages (add .md to most Datadog Docs URLs for raw content):
curl -s https://docs.datadoghq.com/monitors.md
curl -s https://docs.datadoghq.com/tracing.md

Key Documentation Sections
Topic	URL
APM/Tracing	https://docs.datadoghq.com/tracing/
Logs	https://docs.datadoghq.com/logs/
Metrics	https://docs.datadoghq.com/metrics/
Monitors	https://docs.datadoghq.com/monitors/
Dashboards	https://docs.datadoghq.com/dashboards/
Security	https://docs.datadoghq.com/security/
Synthetics	https://docs.datadoghq.com/synthetics/
RUM	https://docs.datadoghq.com/real_user_monitoring/
Incidents	https://docs.datadoghq.com/service_management/incident_management/
API Reference	https://docs.datadoghq.com/api/
Scope Guardrails
Use llms.txt for documentation lookups
Defer to official docs for feature availability and limits
Failure Handling
If docs.datadoghq.com is unreachable, check network connectivity
For region-specific docs, use appropriate site (datadoghq.eu, etc.)
Weekly Installs
471
Repository
datadog-labs/ag…t-skills
GitHub Stars
101
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass