---
title: deployment-documentation
url: https://skills.sh/aj-geddes/useful-ai-prompts/deployment-documentation
---

# deployment-documentation

skills/aj-geddes/useful-ai-prompts/deployment-documentation
deployment-documentation
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill deployment-documentation
SKILL.md
Deployment Documentation
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Create comprehensive deployment documentation covering infrastructure setup, CI/CD pipelines, deployment procedures, and rollback strategies.

When to Use
Deployment guides
Infrastructure documentation
CI/CD pipeline setup
Configuration management
Container orchestration
Cloud infrastructure docs
Release procedures
Rollback procedures
Quick Start

Minimal working example:

# Deployment Guide

## Overview

This document describes the deployment process for [Application Name].

**Deployment Methods:**

- Manual deployment (emergency only)
- Automated CI/CD (preferred)
- Blue-green deployment
- Canary deployment

**Environments:**

- Development: https://dev.example.com
- Staging: https://staging.example.com
- Production: https://example.com

---

## Prerequisites

### Required Tools

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [GitHub Actions Workflow](references/github-actions-workflow.md) | GitHub Actions Workflow |
| [Dockerfile](references/dockerfile.md) | Dockerfile |
| [docker-compose.yml](references/docker-composeyml.md) | docker-compose.yml |
| [Deployment Manifest](references/deployment-manifest.md) | Deployment Manifest |

## Best Practices

### ✅ DO

- Use infrastructure as code
- Implement CI/CD pipelines
- Use container orchestration
- Implement health checks
- Use rolling deployments
- Have rollback procedures
- Monitor deployments
- Document emergency procedures
- Use secrets management
- Implement blue-green or canary deployments

### ❌ DON'T

- Deploy directly to production
- Skip testing before deploy
- Forget to backup before migrations
- Deploy without rollback plan
- Skip monitoring after deployment
- Hardcode credentials
- Deploy during peak hours (unless necessary)

Weekly Installs
280
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass