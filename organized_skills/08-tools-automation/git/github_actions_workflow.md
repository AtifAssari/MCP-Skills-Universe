---
rating: ⭐⭐
title: github-actions-workflow
url: https://skills.sh/aj-geddes/useful-ai-prompts/github-actions-workflow
---

# github-actions-workflow

skills/aj-geddes/useful-ai-prompts/github-actions-workflow
github-actions-workflow
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill github-actions-workflow
SKILL.md
GitHub Actions Workflow
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Create powerful GitHub Actions workflows to automate testing, building, security scanning, and deployment processes directly from your GitHub repository.

When to Use
Continuous integration and testing
Build automation
Security scanning and analysis
Dependency updates
Automated deployments
Release management
Code quality checks
Quick Start

Minimal working example:

# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [16.x, 18.x, 20.x]
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node ${{ matrix.node-version }}
        uses: actions/setup-node@v3
        with:
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Complete CI/CD Workflow	Complete CI/CD Workflow
Automated Release Workflow	Automated Release Workflow
Docker Build and Push	Docker Build and Push
Best Practices
✅ DO
Use caching for dependencies (npm, pip, Maven)
Run tests in parallel with matrix strategy
Require status checks on protected branches
Use environment secrets and variables
Implement conditional jobs with if:
Lint and format before testing
Set explicit permissions with permissions
Use runner labels for specific hardware
Cache Docker layers for faster builds
❌ DON'T
Store secrets in workflow files
Run untrusted code in workflows
Use secrets.* with pull requests from forks
Hardcode credentials or tokens
Miss error handling with continue-on-error
Create overly complex workflows
Skip testing on pull requests
Weekly Installs
392
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