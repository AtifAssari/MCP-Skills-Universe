---
title: infrastructure-cost-optimization
url: https://skills.sh/aj-geddes/useful-ai-prompts/infrastructure-cost-optimization
---

# infrastructure-cost-optimization

skills/aj-geddes/useful-ai-prompts/infrastructure-cost-optimization
infrastructure-cost-optimization
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill infrastructure-cost-optimization
SKILL.md
Infrastructure Cost Optimization
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Reduce infrastructure costs through intelligent resource allocation, reserved instances, spot instances, and continuous optimization without sacrificing performance.

When to Use
Cloud cost reduction
Budget management and tracking
Resource utilization optimization
Multi-environment cost allocation
Waste identification and elimination
Reserved instance planning
Spot instance integration
Quick Start

Minimal working example:

# cost-optimization-setup.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cost-optimization-scripts
  namespace: operations
data:
  analyze-costs.sh: |
    #!/bin/bash
    set -euo pipefail

    echo "=== AWS Cost Analysis ==="

    # Get daily cost trend
    echo "Daily costs for last 7 days:"
    aws ce get-cost-and-usage \
      --time-period Start=$(date -d '7 days ago' +%Y-%m-%d),End=$(date +%Y-%m-%d) \
      --granularity DAILY \
      --metrics "BlendedCost" \
      --group-by Type=DIMENSION,Key=SERVICE \
      --query 'ResultsByTime[*].[TimePeriod.Start,Total.BlendedCost.Amount]' \
      --output table

    # Find unattached resources
    echo -e "\n=== Unattached EBS Volumes ==="
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
AWS Cost Optimization Configuration	AWS Cost Optimization Configuration
Kubernetes Cost Optimization	Kubernetes Cost Optimization
Cost Monitoring Dashboard	Cost Monitoring Dashboard
Best Practices
✅ DO
Follow established patterns and conventions
Write clean, maintainable code
Add appropriate documentation
Test thoroughly before deploying
❌ DON'T
Skip testing or validation
Ignore error handling
Hard-code configuration values
Weekly Installs
273
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