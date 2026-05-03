---
rating: ⭐⭐
title: grafana-dashboard
url: https://skills.sh/aj-geddes/useful-ai-prompts/grafana-dashboard
---

# grafana-dashboard

skills/aj-geddes/useful-ai-prompts/grafana-dashboard
grafana-dashboard
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill grafana-dashboard
SKILL.md
Grafana Dashboard
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Design and implement comprehensive Grafana dashboards with multiple visualization types, variables, and drill-down capabilities for operational monitoring.

When to Use
Creating monitoring dashboards
Building operational insights
Visualizing time-series data
Creating drill-down dashboards
Sharing metrics with stakeholders
Quick Start

Minimal working example:

{
  "dashboard": {
    "title": "Application Performance",
    "description": "Real-time application metrics",
    "tags": ["production", "performance"],
    "timezone": "UTC",
    "refresh": "30s",
    "templating": {
      "list": [
        {
          "name": "datasource",
          "type": "datasource",
          "datasource": "prometheus"
        },
        {
          "name": "service",
          "type": "query",
          "datasource": "prometheus",
          "query": "label_values(requests_total, service)"
        }
      ]
    },
    "panels": [
      {
        "id": 1,
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Grafana Dashboard JSON	Grafana Dashboard JSON
Grafana Provisioning Configuration	Grafana Provisioning Configuration
Grafana Alert Configuration	Grafana Alert Configuration
Grafana API Client	Grafana API Client
Docker Compose Setup	Docker Compose Setup
Best Practices
✅ DO
Use meaningful dashboard titles
Add documentation panels
Implement row-based organization
Use variables for flexibility
Set appropriate refresh intervals
Include runbook links in alerts
Test alerts before deploying
Use consistent color schemes
Version control dashboard JSON
❌ DON'T
Overload dashboards with too many panels
Mix different time ranges without justification
Create without runbooks
Ignore alert noise
Use inconsistent metric naming
Set refresh too frequently
Forget to configure datasources
Leave default passwords
Weekly Installs
317
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass