---
rating: ⭐⭐
title: gitlab-cicd-pipeline
url: https://skills.sh/aj-geddes/useful-ai-prompts/gitlab-cicd-pipeline
---

# gitlab-cicd-pipeline

skills/aj-geddes/useful-ai-prompts/gitlab-cicd-pipeline
gitlab-cicd-pipeline
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill gitlab-cicd-pipeline
SKILL.md
GitLab CI/CD Pipeline
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Create comprehensive GitLab CI/CD pipelines that automate building, testing, and deployment using GitLab Runner infrastructure and container execution.

When to Use
GitLab repository CI/CD setup
Multi-stage build pipelines
Docker registry integration
Kubernetes deployment
Review app deployment
Cache optimization
Dependency management
Quick Start

Minimal working example:

# .gitlab-ci.yml
image: node:18-alpine

variables:
  DOCKER_DRIVER: overlay2
  FF_USE_FASTZIP: "true"

stages:
  - lint
  - test
  - build
  - security
  - deploy-review
  - deploy-prod

cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .npm/

lint:
  stage: lint
  script:
    - npm install
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Complete Pipeline Configuration	Complete Pipeline Configuration
GitLab Runner Configuration	GitLab Runner Configuration
Docker Layer Caching Optimization	Docker Layer Caching Optimization
Multi-Project Pipeline	Multi-Project Pipeline
Kubernetes Deployment	Kubernetes Deployment, Performance Testing Stage, Release Pipeline with Semantic Versioning
Best Practices
✅ DO
Use stages to organize pipeline flow
Implement caching for dependencies
Use artifacts for test reports
Set appropriate cache keys
Implement conditional execution with only and except
Use needs: for job dependencies
Clean up artifacts with expire_in
Use Docker for consistent environments
Implement security scanning stages
Set resource limits for jobs
Use merge request pipelines
❌ DON'T
Run tests serially when parallelizable
Cache everything unnecessarily
Leave large artifacts indefinitely
Store secrets in configuration files
Run privileged Docker without necessity
Skip security scanning
Ignore pipeline failures
Use only: [main] without proper controls
Weekly Installs
403
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