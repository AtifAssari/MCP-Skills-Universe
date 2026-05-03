---
title: ci-cd
url: https://skills.sh/ahmedasmar/devops-claude-skills/ci-cd
---

# ci-cd

skills/ahmedasmar/devops-claude-skills/ci-cd
ci-cd
Installation
$ npx skills add https://github.com/ahmedasmar/devops-claude-skills --skill ci-cd
SKILL.md
CI/CD Pipelines

Comprehensive guide for CI/CD pipeline design, optimization, security, and troubleshooting across GitHub Actions, GitLab CI, and other platforms.

Core Workflows
1. Creating a New Pipeline

Decision tree:

What are you building?
├── Node.js/Frontend → GitHub: templates/github-actions/node-ci.yml | GitLab: templates/gitlab-ci/node-ci.yml
├── Python → GitHub: templates/github-actions/python-ci.yml | GitLab: templates/gitlab-ci/python-ci.yml
├── Go → GitHub: templates/github-actions/go-ci.yml | GitLab: templates/gitlab-ci/go-ci.yml
├── Docker Image → GitHub: templates/github-actions/docker-build.yml | GitLab: templates/gitlab-ci/docker-build.yml
├── Other → Follow the pipeline design pattern below


Basic pipeline structure:

# 1. Fast feedback (lint, format) - <1 min
# 2. Unit tests - 1-5 min
# 3. Integration tests - 5-15 min
# 4. Build artifacts
# 5. E2E tests (optional, main branch only) - 15-30 min
# 6. Deploy (with approval gates)


Key principles (from references/best_practices.md):

Fail fast: Run cheap validation first
Parallelize: Remove unnecessary job dependencies
Cache dependencies: Use actions/cache or GitLab cache (references/optimization.md for strategies)
Use artifacts: Build once, deploy many times
Add security scanning early: See references/devsecops.md for SAST/DAST/SCA integration
2. Optimizing Pipeline Performance

Quick wins checklist:

 Add dependency caching (50-90% faster builds)
 Remove unnecessary needs dependencies
 Add path filters to skip unnecessary runs
 Use npm ci instead of npm install
 Add job timeouts to prevent hung builds
 Enable concurrency cancellation for duplicate runs

Analyze existing pipeline:

# Use the pipeline analyzer script
python3 scripts/pipeline_analyzer.py --platform github --workflow .github/workflows/ci.yml


Common optimizations (detailed in references/optimization.md):

Slow tests: Shard tests with matrix builds
Repeated dependency installs: Add caching
Sequential jobs: Parallelize with proper needs
Full test suite on every PR: Use path filters or test impact analysis

See optimization.md for detailed caching strategies, parallelization techniques, and performance tuning.

3. Securing Your Pipeline

Essential security checklist:

 Use OIDC instead of static credentials
 Pin actions/includes to commit SHAs
 Use minimal permissions
 Enable secret scanning
 Add vulnerability scanning (dependencies, containers)
 Implement branch protection
 Separate test from deploy workflows

Quick setup - OIDC authentication:

GitHub Actions → AWS:

permissions:
  id-token: write
  contents: read

steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: arn:aws:iam::123456789:role/GitHubActionsRole
      aws-region: us-east-1


Secrets management:

Store in platform secret stores (GitHub Secrets, GitLab CI/CD Variables)
Mark as "masked" in GitLab
Use environment-specific secrets
Rotate regularly (every 90 days)
Never log secrets

See security.md for comprehensive security patterns, supply chain security, and secrets management.

4. Troubleshooting Pipeline Failures

Systematic approach:

Step 1: Check pipeline health

gh run list --limit 20    # Recent runs with status (success/failure rates)
gh run view <run-id>      # Detailed run info and failure logs
gh workflow list           # All configured workflows


Step 2: Identify the failure type

Error Pattern	Common Cause	Quick Fix
"Module not found"	Missing dependency or cache issue	Clear cache, run npm ci
"Timeout"	Job taking too long	Add caching, increase timeout
"Permission denied"	Missing permissions	Add to permissions: block
"Cannot connect to Docker daemon"	Docker not available	Use correct runner or DinD
Intermittent failures	Flaky tests or race conditions	Add retries, fix timing issues

Step 3: Enable debug logging

GitHub Actions:

# Add repository secrets:
# ACTIONS_RUNNER_DEBUG = true
# ACTIONS_STEP_DEBUG = true


GitLab CI:

variables:
  CI_DEBUG_TRACE: "true"


Step 4: Reproduce locally

# GitHub Actions - use act
act -j build

# Or Docker
docker run -it ubuntu:latest bash
# Then manually run the failing steps


See troubleshooting.md for comprehensive issue diagnosis, platform-specific problems, and solutions.

5. Implementing Deployment Workflows

Deployment pattern selection:

Pattern	Use Case	Complexity	Risk
Direct	Simple apps, low traffic	Low	Medium
Blue-Green	Zero downtime required	Medium	Low
Canary	Gradual rollout, monitoring	High	Very Low
Rolling	Kubernetes, containers	Medium	Low

Basic deployment structure:

deploy:
  needs: [build, test]
  if: github.ref == 'refs/heads/main'
  environment:
    name: production
    url: https://example.com
  steps:
    - name: Download artifacts
    - name: Deploy
    - name: Health check
    - name: Rollback on failure


Multi-environment setup:

Development: Auto-deploy on develop branch
Staging: Auto-deploy on main, requires passing tests
Production: Manual approval required, smoke tests mandatory

See best_practices.md for detailed deployment patterns and environment management.

6. Implementing DevSecOps Security Scanning

Security scanning types:

Scan Type	Purpose	When to Run	Speed	Tools
Secret Scanning	Find exposed credentials	Every commit	Fast (<1 min)	TruffleHog, Gitleaks
SAST	Find code vulnerabilities	Every commit	Medium (5-15 min)	CodeQL, Semgrep, Bandit, Gosec
SCA	Find dependency vulnerabilities	Every commit	Fast (1-5 min)	npm audit, pip-audit, Snyk
Container Scanning	Find image vulnerabilities	After build	Medium (5-10 min)	Trivy, Grype
DAST	Find runtime vulnerabilities	Scheduled/main only	Slow (15-60 min)	OWASP ZAP

Quick setup - Add security to existing pipeline:

GitHub Actions:

jobs:
  # Add before build job
  secret-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: trufflesecurity/trufflehog@main
      - uses: gitleaks/gitleaks-action@v2

  sast:
    runs-on: ubuntu-latest
    permissions:
      security-events: write
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript  # or python, go
      - uses: github/codeql-action/analyze@v3

  build:
    needs: [secret-scan, sast]  # Add dependencies


GitLab CI:

stages:
  - security  # Add before other stages
  - build
  - test

# Secret scanning
secret-scan:
  stage: security
  image: trufflesecurity/trufflehog:latest
  script:
    - trufflehog filesystem . --json --fail

# SAST
sast:semgrep:
  stage: security
  image: returntocorp/semgrep
  script:
    - semgrep scan --config=auto .

# Use GitLab templates
include:
  - template: Security/SAST.gitlab-ci.yml
  - template: Security/Dependency-Scanning.gitlab-ci.yml


Comprehensive security pipeline templates:

GitHub Actions: templates/github-actions/security-scan.yml - Complete DevSecOps pipeline with all scanning stages
GitLab CI: templates/gitlab-ci/security-scan.yml - Complete DevSecOps pipeline with GitLab security templates

Security gate pattern:

Add a security gate job that evaluates all security scan results and fails the pipeline if critical issues are found:

security-gate:
  needs: [secret-scan, sast, sca, container-scan]
  script:
    # Check for critical vulnerabilities
    # Parse JSON reports and evaluate thresholds
    # Fail if critical issues found


Language-specific security tools:

Node.js: CodeQL, Semgrep, npm audit, eslint-plugin-security
Python: CodeQL, Semgrep, Bandit, pip-audit, Safety
Go: CodeQL, Semgrep, Gosec, govulncheck

All language-specific templates now include security scanning stages. See:

templates/github-actions/node-ci.yml
templates/github-actions/python-ci.yml
templates/github-actions/go-ci.yml
templates/gitlab-ci/node-ci.yml
templates/gitlab-ci/python-ci.yml
templates/gitlab-ci/go-ci.yml

See devsecops.md for comprehensive DevSecOps guide covering all security scanning types, tool comparisons, and implementation patterns.

Quick Reference Commands
GitHub Actions
# List workflows
gh workflow list

# View recent runs
gh run list --limit 20

# View specific run
gh run view <run-id>

# Re-run failed jobs
gh run rerun <run-id> --failed

# Download logs
gh run view <run-id> --log > logs.txt

# Trigger workflow manually
gh workflow run ci.yml

# Check workflow status
gh run watch

GitLab CI
# View pipelines
gl project-pipelines list

# Pipeline status
gl project-pipeline get <pipeline-id>

# Retry failed jobs
gl project-pipeline retry <pipeline-id>

# Cancel pipeline
gl project-pipeline cancel <pipeline-id>

# Download artifacts
gl project-job artifacts <job-id>

Platform-Specific Patterns
GitHub Actions

Reusable workflows:

# .github/workflows/reusable-test.yml
on:
  workflow_call:
    inputs:
      node-version:
        required: true
        type: string

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ inputs.node-version }}


Call from another workflow:

jobs:
  test:
    uses: ./.github/workflows/reusable-test.yml
    with:
      node-version: '20'

GitLab CI

Templates with extends:

.test_template:
  image: node:20
  before_script:
    - npm ci

unit-test:
  extends: .test_template
  script:
    - npm run test:unit

integration-test:
  extends: .test_template
  script:
    - npm run test:integration


DAG pipelines with needs:

build:
  stage: build

test:unit:
  stage: test
  needs: [build]

test:integration:
  stage: test
  needs: [build]

deploy:
  stage: deploy
  needs: [test:unit, test:integration]

Diagnostic Scripts
Script	Purpose	Usage
pipeline_analyzer.py	Find optimization opportunities (caching, parallelization, outdated actions)	python3 scripts/pipeline_analyzer.py --platform github --workflow <path>

For pipeline health checks (success/failure rates, failure patterns), use gh CLI: gh run list --limit 20, gh run view <run-id>, gh workflow list.

Reference Documentation
references/best_practices.md — Pipeline design, testing, deployment patterns, artifact handling
references/security.md — Secrets management, OIDC, supply chain security, secure pipeline patterns
references/devsecops.md — SAST/DAST/SCA tooling (CodeQL, Semgrep, Trivy, Snyk), security gates
references/optimization.md — Caching strategies, parallelization, test splitting, build optimization
references/troubleshooting.md — Common issues, Docker problems, authentication, platform debugging
Templates

Starter templates in assets/templates/ for both GitHub Actions and GitLab CI:

Language/Type	GitHub Actions	GitLab CI
Node.js	github-actions/node-ci.yml	gitlab-ci/node-ci.yml
Python	github-actions/python-ci.yml	gitlab-ci/python-ci.yml
Go	github-actions/go-ci.yml	gitlab-ci/go-ci.yml
Docker	github-actions/docker-build.yml	gitlab-ci/docker-build.yml
Security	github-actions/security-scan.yml	gitlab-ci/security-scan.yml

All templates include security scanning, caching, and multi-environment deployment.

Common Patterns
Caching Dependencies

GitHub Actions:

- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
- run: npm ci


GitLab CI:

cache:
  key:
    files:
      - package-lock.json
  paths:
    - node_modules/

Matrix Builds

GitHub Actions:

strategy:
  matrix:
    os: [ubuntu-latest, macos-latest]
    node: [18, 20, 22]
  fail-fast: false


GitLab CI:

test:
  parallel:
    matrix:
      - NODE_VERSION: ['18', '20', '22']

Conditional Execution

GitHub Actions:

- name: Deploy
  if: github.ref == 'refs/heads/main' && github.event_name == 'push'


GitLab CI:

deploy:
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: manual

Getting Started
New pipeline: Start with a template from assets/templates/
Add security scanning: Use DevSecOps templates or add security stages to existing pipelines (see workflow 6 above)
Optimize existing: Run scripts/pipeline_analyzer.py
Debug issues: Check references/troubleshooting.md
Improve security: Review references/security.md and references/devsecops.md checklists
Speed up builds: See references/optimization.md
Weekly Installs
197
Repository
ahmedasmar/devo…e-skills
GitHub Stars
138
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn