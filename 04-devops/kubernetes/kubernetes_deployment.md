---
rating: ⭐⭐
title: kubernetes-deployment
url: https://skills.sh/aj-geddes/useful-ai-prompts/kubernetes-deployment
---

# kubernetes-deployment

skills/aj-geddes/useful-ai-prompts/kubernetes-deployment
kubernetes-deployment
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill kubernetes-deployment
SKILL.md
Kubernetes Deployment
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Master Kubernetes deployments for managing containerized applications at scale, including multi-container services, resource allocation, health checks, and rolling deployment strategies.

When to Use
Container orchestration and management
Multi-environment deployments (dev, staging, prod)
Auto-scaling microservices
Rolling updates and blue-green deployments
Service discovery and load balancing
Resource quota and limit management
Pod networking and security policies
Quick Start

Minimal working example:

# kubernetes-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-service
  namespace: production
  labels:
    app: api-service
    version: v1
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: api-service
  template:
    metadata:
      labels:
        app: api-service
        version: v1
      annotations:
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Complete Deployment with Resource Management	Complete Deployment with Resource Management
Deployment Script	Deployment Script
Service Account and RBAC	Service Account and RBAC
Best Practices
✅ DO
Use resource requests and limits
Implement health checks (liveness, readiness)
Use ConfigMaps for configuration
Apply security context restrictions
Use service accounts and RBAC
Implement pod anti-affinity
Use namespaces for isolation
Enable pod security policies
❌ DON'T
Use latest image tags in production
Run containers as root
Set unlimited resource usage
Skip readiness probes
Deploy without resource limits
Mix configurations in container images
Use default service accounts
Weekly Installs
453
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