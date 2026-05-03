---
title: deployment-automation
url: https://skills.sh/aj-geddes/useful-ai-prompts/deployment-automation
---

# deployment-automation

skills/aj-geddes/useful-ai-prompts/deployment-automation
deployment-automation
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill deployment-automation
SKILL.md
Deployment Automation
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Establish automated deployment pipelines that safely and reliably move applications across development, staging, and production environments with minimal manual intervention and risk.

When to Use
Continuous deployment to Kubernetes
Infrastructure as Code deployment
Multi-environment promotion
Blue-green deployment strategies
Canary release management
Infrastructure provisioning
Automated rollback procedures
Quick Start

Minimal working example:

# helm/Chart.yaml
apiVersion: v2
name: myapp
description: My awesome application
type: application
version: 1.0.0

# helm/values.yaml
replicaCount: 3
image:
  repository: ghcr.io/myorg/myapp
  pullPolicy: IfNotPresent
  tag: "1.0.0"
service:
  type: ClusterIP
  port: 80
  targetPort: 3000
resources:
  requests:
    memory: "256Mi"
    cpu: "250m"
  limits:
    memory: "512Mi"
    cpu: "500m"
autoscaling:
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Helm Deployment Chart	Helm Deployment Chart
GitHub Actions Deployment Workflow	GitHub Actions Deployment Workflow
ArgoCD Deployment	ArgoCD Deployment
Blue-Green Deployment	Blue-Green Deployment
Best Practices
✅ DO
Use Infrastructure as Code (Terraform, Helm)
Implement GitOps workflows
Use blue-green deployments
Implement canary releases
Automate rollback procedures
Test deployments in staging first
Use feature flags for gradual rollout
Monitor deployment health
Document deployment procedures
Implement approval gates for production
Version infrastructure code
Use environment parity
❌ DON'T
Deploy directly to production
Skip testing in staging
Use manual deployment scripts
Deploy without rollback plan
Ignore health checks
Use hardcoded configuration
Deploy during critical hours
Skip pre-deployment validation
Forget to backup before deploy
Deploy from local machines
Weekly Installs
299
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn