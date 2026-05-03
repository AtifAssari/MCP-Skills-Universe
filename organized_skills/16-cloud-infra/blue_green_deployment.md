---
rating: ⭐⭐⭐
title: blue-green-deployment
url: https://skills.sh/aj-geddes/useful-ai-prompts/blue-green-deployment
---

# blue-green-deployment

skills/aj-geddes/useful-ai-prompts/blue-green-deployment
blue-green-deployment
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill blue-green-deployment
SKILL.md
Blue-Green Deployment
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Deploy applications using blue-green deployment patterns to maintain two identical production environments, enabling instant traffic switching and rapid rollback capabilities.

When to Use
Zero-downtime releases
High-risk deployments
Complex application migrations
Database schema changes
Rapid rollback requirements
A/B testing with environment separation
Staged rollout strategies
Quick Start

Minimal working example:

# blue-green-setup.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: blue-green-config
  namespace: production
data:
  switch-traffic.sh: |
    #!/bin/bash
    set -euo pipefail

    CURRENT_ACTIVE="${1:-blue}"
    TARGET="${2:-green}"
    ALB_ARN="arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/myapp-alb/1234567890abcdef"

    echo "Switching traffic from $CURRENT_ACTIVE to $TARGET..."

    # Get target group ARNs
    BLUE_TG=$(aws elbv2 describe-target-groups \
      --load-balancer-arn "$ALB_ARN" \
      --query "TargetGroups[?Tags[?Key=='Name' && Value=='blue']].TargetGroupArn" \
      --output text)

    GREEN_TG=$(aws elbv2 describe-target-groups \
      --load-balancer-arn "$ALB_ARN" \
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Blue-Green with Load Balancer	Blue-Green with Load Balancer
Blue-Green Rollback Script	Blue-Green Rollback Script
Monitoring and Validation	Monitoring and Validation
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
267
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