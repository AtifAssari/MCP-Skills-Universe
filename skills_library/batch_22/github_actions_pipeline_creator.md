---
title: github-actions-pipeline-creator
url: https://skills.sh/patricio0312rev/skills/github-actions-pipeline-creator
---

# github-actions-pipeline-creator

skills/patricio0312rev/skills/github-actions-pipeline-creator
github-actions-pipeline-creator
Installation
$ npx skills add https://github.com/patricio0312rev/skills --skill github-actions-pipeline-creator
SKILL.md
GitHub Actions Pipeline Creator

Build production-ready GitHub Actions workflows with best practices.

Basic CI Workflow
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

# Cancel in-progress runs for same workflow
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  lint:
    name: Lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"

      - name: Install dependencies
        run: npm ci

      - name: Run ESLint
        run: npm run lint

      - name: Run Prettier
        run: npm run format:check

      - name: Run TypeScript
        run: npm run type-check

  test:
    name: Test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test -- --coverage

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/coverage-final.json
          flags: unittests
          fail_ci_if_error: true

  build:
    name: Build
    runs-on: ubuntu-latest
    needs: [lint, test]
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"

      - name: Install dependencies
        run: npm ci

      - name: Build
        run: npm run build
        env:
          NODE_ENV: production

      - name: Upload build artifacts
        uses: actions/upload-artifact@v4
        with:
          name: dist
          path: dist/
          retention-days: 7

Matrix Strategy
test:
  name: Test
  runs-on: ${{ matrix.os }}
  strategy:
    matrix:
      os: [ubuntu-latest, macos-latest, windows-latest]
      node-version: [18, 20, 21]
      exclude:
        # Skip Windows + Node 18 (slow)
        - os: windows-latest
          node-version: 18
    fail-fast: false

  steps:
    - uses: actions/checkout@v4

    - name: Setup Node.js ${{ matrix.node-version }}
      uses: actions/setup-node@v4
      with:
        node-version: ${{ matrix.node-version }}
        cache: "npm"

    - run: npm ci
    - run: npm test

Advanced Caching
- name: Cache dependencies
  uses: actions/cache@v3
  with:
    path: |
      ~/.npm
      node_modules
      .next/cache
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-npm-

- name: Cache build
  uses: actions/cache@v3
  with:
    path: |
      dist
      .cache
    key: build-${{ github.sha }}
    restore-keys: |
      build-

Docker Build & Push
docker:
  name: Build & Push Docker
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3

    - name: Login to Docker Hub
      uses: docker/login-action@v3
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}

    - name: Extract metadata
      id: meta
      uses: docker/metadata-action@v5
      with:
        images: mycompany/myapp
        tags: |
          type=ref,event=branch
          type=ref,event=pr
          type=semver,pattern={{version}}
          type=sha

    - name: Build and push
      uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        labels: ${{ steps.meta.outputs.labels }}
        cache-from: type=registry,ref=mycompany/myapp:buildcache
        cache-to: type=registry,ref=mycompany/myapp:buildcache,mode=max

Deployment Workflow
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]
  workflow_dispatch:
    inputs:
      environment:
        description: "Environment to deploy to"
        required: true
        type: choice
        options:
          - staging
          - production

jobs:
  deploy:
    name: Deploy to ${{ github.event.inputs.environment || 'staging' }}
    runs-on: ubuntu-latest
    environment:
      name: ${{ github.event.inputs.environment || 'staging' }}
      url: https://${{ steps.deploy.outputs.url }}

    steps:
      - uses: actions/checkout@v4

      - name: Download artifacts
        uses: actions/download-artifact@v4
        with:
          name: dist
          path: dist/

      - name: Deploy to Vercel
        id: deploy
        uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          vercel-args: ${{ github.event.inputs.environment == 'production' && '--prod' || '' }}

Failure Diagnostics
- name: Run tests
  id: test
  run: npm test
  continue-on-error: true

- name: Upload test results
  if: always()
  uses: actions/upload-artifact@v4
  with:
    name: test-results
    path: |
      test-results/
      coverage/

- name: Comment PR with results
  if: failure() && github.event_name == 'pull_request'
  uses: actions/github-script@v7
  with:
    script: |
      github.rest.issues.createComment({
        issue_number: context.issue.number,
        owner: context.repo.owner,
        repo: context.repo.repo,
        body: '❌ Tests failed. Check the [test results](${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }})'
      })

- name: Fail if tests failed
  if: steps.test.outcome == 'failure'
  run: exit 1

Composite Actions
# .github/actions/setup-node/action.yml
name: "Setup Node.js with Cache"
description: "Setup Node.js and restore cache"

inputs:
  node-version:
    description: "Node.js version"
    required: false
    default: "20"

runs:
  using: "composite"
  steps:
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: ${{ inputs.node-version }}
        cache: "npm"

    - name: Install dependencies
      shell: bash
      run: npm ci
# Usage in workflow:
# - uses: ./.github/actions/setup-node
#   with:
#     node-version: '20'

Conditional Jobs
lint:
  if: github.event_name == 'pull_request'
  runs-on: ubuntu-latest
  steps: [...]

deploy:
  if: github.ref == 'refs/heads/main' && github.event_name == 'push'
  needs: [build, test]
  runs-on: ubuntu-latest
  steps: [...]

Best Practices
Cache dependencies: Speeds up 3-5x
Parallel jobs: Run lint/test/build concurrently
Matrix strategy: Test multiple versions/platforms
Fail fast: Stop on first failure (or not)
Upload artifacts: Debug failures
Concurrency control: Cancel outdated runs
Secrets management: Never log secrets
Status checks: Require passing CI
Output Checklist
 Lint job configured
 Test job with coverage
 Build job with artifacts
 Deploy job with environments
 Caching strategy implemented
 Matrix builds (if needed)
 Failure diagnostics
 PR comments on failure
 Docker build (if needed)
 Status badges in README
Weekly Installs
100
Repository
patricio0312rev/skills
GitHub Stars
35
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass