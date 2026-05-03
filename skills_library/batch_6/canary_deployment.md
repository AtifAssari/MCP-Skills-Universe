---
title: canary-deployment
url: https://skills.sh/aj-geddes/useful-ai-prompts/canary-deployment
---

# canary-deployment

skills/aj-geddes/useful-ai-prompts/canary-deployment
canary-deployment
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill canary-deployment
SKILL.md
Canary Deployment
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Deploy new versions gradually to a small percentage of users, monitor metrics for issues, and automatically rollback or proceed based on predefined thresholds.

When to Use
Low-risk gradual rollouts
Real-world testing with live traffic
Automatic rollback on errors
User impact minimization
A/B testing integration
Metrics-driven deployments
High-traffic services
Quick Start

Minimal working example:

# canary-deployment-istio.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-v1
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      version: v1
  template:
    metadata:
      labels:
        app: myapp
        version: v1
    spec:
      containers:
        - name: myapp
          image: myrepo/myapp:1.0.0
          ports:
            - containerPort: 8080

---
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Istio-based Canary Deployment	Istio-based Canary Deployment
Kubernetes Native Canary Script	Kubernetes Native Canary Script
Metrics-Based Canary Analysis	Metrics-Based Canary Analysis
Automated Canary Promotion	Automated Canary Promotion
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
260
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn