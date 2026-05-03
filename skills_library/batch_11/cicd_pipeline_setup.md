---
title: cicd-pipeline-setup
url: https://skills.sh/aj-geddes/useful-ai-prompts/cicd-pipeline-setup
---

# cicd-pipeline-setup

skills/aj-geddes/useful-ai-prompts/cicd-pipeline-setup
cicd-pipeline-setup
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill cicd-pipeline-setup
SKILL.md
CI/CD Pipeline Setup
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build automated continuous integration and deployment pipelines that test code, build artifacts, run security checks, and deploy to multiple environments with minimal manual intervention.

When to Use
Automated code testing and quality checks
Containerized application builds
Multi-environment deployments
Release management and versioning
Automated security scanning
Performance testing integration
Artifact management and registry
Quick Start

Minimal working example:

# .github/workflows/deploy.yml
name: Build and Deploy

on:
  push:
    branches:
      - main
      - develop
  pull_request:
    branches:
      - main
  workflow_dispatch:

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [18.x, 20.x]

    steps:
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
GitHub Actions Workflow	GitHub Actions Workflow
GitLab CI Pipeline	GitLab CI Pipeline
Jenkins Pipeline	Jenkins Pipeline
CI/CD Script	CI/CD Script
Best Practices
✅ DO
Fail fast with early validation
Run tests in parallel when possible
Use caching for dependencies
Implement proper secret management
Gate production deployments with approval
Monitor and alert on pipeline failures
Use consistent environment configuration
Implement infrastructure as code
❌ DON'T
Store credentials in pipeline configuration
Deploy without automated tests
Skip security scanning
Allow long-running pipelines
Mix staging and production pipelines
Ignore test failures
Deploy directly to main branch
Skip health checks after deployment
Weekly Installs
327
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass