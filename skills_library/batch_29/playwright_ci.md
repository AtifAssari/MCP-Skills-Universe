---
title: playwright-ci
url: https://skills.sh/testdino-hq/playwright-skill/playwright-ci
---

# playwright-ci

skills/testdino-hq/playwright-skill/playwright-ci
playwright-ci
Installation
$ npx skills add https://github.com/testdino-hq/playwright-skill --skill playwright-ci
SKILL.md
Playwright CI/CD

Ship reliable tests in every pipeline — CI-specific patterns for speed, stability, and actionable reports.

9 guides covering CI/CD setup, parallel execution, containerized runs, reporting, and infrastructure patterns for all major CI providers.

Golden Rules
retries: 2 in CI only — surface flakiness in pipelines, not locally
traces: 'on-first-retry' — capture rich debugging artifacts without slowing every run
Shard across runners — --shard=N/M splits tests evenly; scale horizontally, not vertically
Cache browser binaries — ~/.cache/ms-playwright keyed on Playwright version
Upload artifacts on failure — traces, screenshots, and HTML reports as CI artifacts
Use the official Docker image — mcr.microsoft.com/playwright:v* has all OS deps pre-installed
Global setup for auth — run login once in globalSetup, reuse storageState across workers
Fail fast, debug later — keep CI runs short; use trace viewer and HTML reports to investigate
Guide Index
CI Providers
Provider	Guide
GitHub Actions	ci-github-actions.md
GitLab CI	ci-gitlab.md
CircleCI / Azure DevOps / Jenkins	ci-other.md
Execution & Scaling
Topic	Guide
Parallel execution & sharding	parallel-and-sharding.md
Docker & containers	docker-and-containers.md
Multi-project config	projects-and-dependencies.md
Reporting & Setup
Topic	Guide
Reports & artifacts	reporting-and-artifacts.md
Code coverage	test-coverage.md
Global setup/teardown	global-setup-teardown.md
Weekly Installs
90
Repository
testdino-hq/pla…ht-skill
GitHub Stars
220
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn