---
title: cicd-automation
url: https://skills.sh/autumnsgrove/groveengine/cicd-automation
---

# cicd-automation

skills/autumnsgrove/groveengine/cicd-automation
cicd-automation
Installation
$ npx skills add https://github.com/autumnsgrove/groveengine --skill cicd-automation
SKILL.md
CI/CD Automation Skill
When to Activate

Activate this skill when:

Creating GitHub Actions workflows
Setting up automated testing
Configuring deployment pipelines
Adding code quality checks to CI
Automating release processes
Quick Start Workflow

Create .github/workflows/ci.yml:

name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install UV
        run: curl -LsSf https://astral.sh/uv/install.sh | sh

      - name: Add UV to PATH
        run: echo "$HOME/.cargo/bin" >> $GITHUB_PATH

      - name: Install dependencies
        run: uv sync

      - name: Run tests
        run: uv run pytest tests/ -v --cov=src

      - name: Lint with Ruff
        run: uv run ruff check src/ tests/

      - name: Check formatting
        run: uv run black --check src/ tests/

Workflow Structure
.github/
└── workflows/
    ├── ci.yml        # Tests and linting
    ├── release.yml   # Package publishing
    └── deploy.yml    # Deployment

Common Triggers
# Every push and PR
on: [push, pull_request]

# Specific branches
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

# Manual trigger
on: workflow_dispatch

# Scheduled (cron)
on:
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight

Testing with Coverage
- name: Run tests with coverage
  run: |
    uv run pytest tests/ \
      --cov=src \
      --cov-report=xml \
      --cov-report=term-missing \
      --junitxml=junit.xml

- name: Upload coverage to Codecov
  uses: codecov/codecov-action@v3
  with:
    files: ./coverage.xml
    fail_ci_if_error: true

Multi-Environment Testing
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python-version: ['3.10', '3.11', '3.12']

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install UV
        run: curl -LsSf https://astral.sh/uv/install.sh | sh

      - name: Run tests
        run: uv run pytest tests/

Caching Dependencies
- name: Cache UV dependencies
  uses: actions/cache@v3
  with:
    path: |
      ~/.cache/uv
      .venv
    key: ${{ runner.os }}-uv-${{ hashFiles('**/pyproject.toml') }}
    restore-keys: |
      ${{ runner.os }}-uv-

- name: Install dependencies
  run: uv sync

Secrets in Workflows
- name: Deploy
  env:
    API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
    DATABASE_URL: ${{ secrets.DATABASE_URL }}
  run: uv run python deploy.py


Setting up secrets:

Repository Settings → Secrets and variables → Actions
Click "New repository secret"
Add name and value
Publishing to PyPI
name: Publish

on:
  release:
    types: [published]

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install UV
        run: curl -LsSf https://astral.sh/uv/install.sh | sh

      - name: Build package
        run: uv build

      - name: Publish to PyPI
        env:
          UV_PUBLISH_TOKEN: ${{ secrets.PYPI_TOKEN }}
        run: uv publish --token $UV_PUBLISH_TOKEN

Docker Image Build
- name: Build and push Docker image
  uses: docker/build-push-action@v5
  with:
    context: .
    push: true
    tags: user/app:latest,user/app:${{ github.sha }}

Status Badges

Add to README:

![CI](https://github.com/username/repo/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/username/repo/badge.svg)](https://codecov.io/gh/username/repo)

Best Practices
DO ✅
Run tests on every push
Cache dependencies for speed
Use matrix for cross-platform testing
Separate CI from CD workflows
Use secrets for sensitive data
DON'T ❌
Skip linting in CI
Ignore test failures
Store secrets in code
Run unnecessary jobs
When to Use CI/CD

Start with:

Running tests on every push
Code quality checks (lint, format)
Security scanning

Add later:

Deployment automation
Docker builds
Documentation generation
Related Resources

See AgentUsage/ci_cd_patterns.md for complete documentation including:

Complex workflow examples
Environment-specific configs
Advanced caching strategies
Deployment patterns
Weekly Installs
64
Repository
autumnsgrove/groveengine
GitHub Stars
5
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail