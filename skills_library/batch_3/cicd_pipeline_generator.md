---
title: cicd-pipeline-generator
url: https://skills.sh/ailabs-393/ai-labs-claude-skills/cicd-pipeline-generator
---

# cicd-pipeline-generator

skills/ailabs-393/ai-labs-claude-skills/cicd-pipeline-generator
cicd-pipeline-generator
Installation
$ npx skills add https://github.com/ailabs-393/ai-labs-claude-skills --skill cicd-pipeline-generator
SKILL.md
CI/CD Pipeline Generator
Overview

Generate production-ready CI/CD pipeline configuration files for various platforms (GitHub Actions, GitLab CI, CircleCI, Jenkins). This skill provides templates and guidance for setting up automated workflows that handle linting, testing, building, and deployment for modern web applications, particularly Node.js/Next.js projects.

Core Capabilities
1. Platform Selection

Choose the appropriate CI/CD platform based on project requirements:

GitHub Actions: Best for GitHub-hosted projects with native integration
GitLab CI/CD: Ideal for GitLab repositories with complex pipeline needs
CircleCI: Optimized for Docker workflows and fast build times
Jenkins: Suitable for self-hosted, highly customizable environments

Refer to references/platform-comparison.md for detailed platform comparisons, pros/cons, and use case recommendations.

2. Pipeline Configuration Generation

Generate pipeline configs following these principles:

Pipeline Stages

Structure pipelines with these standard stages:

Install Dependencies

Checkout code from repository
Setup runtime environment (Node.js version)
Restore cached dependencies
Install dependencies with npm ci
Cache dependencies for future runs

Lint

Run ESLint for code quality
Run TypeScript type checking
Fail fast on linting errors

Test

Execute unit tests
Execute integration tests
Generate code coverage reports
Upload coverage to reporting services (Codecov, Coveralls)

Build

Create production build
Verify build succeeds
Store build artifacts

Deploy

Deploy to staging (develop branch)
Deploy to production (main branch)
Run post-deployment smoke tests
Caching Strategy

Implement effective caching to speed up builds:

# Cache node_modules based on package-lock.json
cache:
  key: ${{ hashFiles('package-lock.json') }}
  paths:
    - node_modules/
    - .npm/

Environment Variables

Configure necessary environment variables:

NODE_ENV: Set to production for builds
Platform-specific tokens: Store as secrets
Build-time variables: Pass to build process
3. Template Usage

Use provided templates from assets/ directory:

GitHub Actions Template (assets/github-actions-nodejs.yml):

Multi-job workflow with lint, test, build, deploy
Matrix builds for multiple Node.js versions (optional)
Vercel deployment integration
Artifact uploading
Code coverage reporting

GitLab CI Template (assets/gitlab-ci-nodejs.yml):

Multi-stage pipeline
Dependency caching
Manual production deployment
Automatic staging deployment
Coverage reporting

To use a template:

Copy the appropriate template file
Place in the correct location:
GitHub Actions: .github/workflows/ci.yml
GitLab CI: .gitlab-ci.yml
Customize deployment targets, environment variables, and branch names
Add required secrets to platform settings
4. Deployment Configuration
Vercel Deployment

For GitHub Actions:

- uses: amondnet/vercel-action@v25
  with:
    vercel-token: ${{ secrets.VERCEL_TOKEN }}
    vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
    vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
    vercel-args: '--prod'


Required Secrets:

VERCEL_TOKEN: Get from Vercel account settings
VERCEL_ORG_ID: From Vercel project settings
VERCEL_PROJECT_ID: From Vercel project settings
Netlify Deployment
- run: |
    npm install -g netlify-cli
    netlify deploy --prod --dir=.next
  env:
    NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
    NETLIFY_SITE_ID: ${{ secrets.NETLIFY_SITE_ID }}

AWS S3 + CloudFront
- uses: aws-actions/configure-aws-credentials@v4
  with:
    aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    aws-region: us-east-1

- run: |
    aws s3 sync .next/static s3://${{ secrets.S3_BUCKET }}/static
    aws cloudfront create-invalidation --distribution-id ${{ secrets.CF_DIST_ID }} --paths "/*"

5. Testing Integration

Configure test execution with proper reporting:

Jest Configuration:

- name: Run tests with coverage
  run: npm test -- --coverage --coverageReporters=text --coverageReporters=lcov

- name: Upload coverage
  uses: codecov/codecov-action@v4
  with:
    files: ./coverage/lcov.info
    flags: unittests


Fail Fast Strategy:

# Run quick tests first
jobs:
  lint:  # Fails in ~30 seconds
  test:  # Fails in ~2 minutes
  build: # Fails in ~5 minutes
    needs: [lint, test]
  deploy:
    needs: [build]

6. Branch-Based Workflows

Implement different behaviors per branch:

Feature Branches / PRs:

Run lint + test only
No deployment
Add PR comments with test results

Develop Branch:

Run lint + test + build
Deploy to staging environment
Automatic deployment

Main Branch:

Run lint + test + build
Deploy to production
Manual approval (optional)
Create release tags

Example:

deploy_staging:
  if: github.ref == 'refs/heads/develop'
  # Deploy to staging

deploy_production:
  if: github.ref == 'refs/heads/main'
  environment: production  # Requires manual approval
  # Deploy to production

Workflow Decision Tree

Follow this decision tree to generate the appropriate pipeline:

Which platform?

GitHub → Use assets/github-actions-nodejs.yml
GitLab → Use assets/gitlab-ci-nodejs.yml
CircleCI/Jenkins → Adapt GitHub Actions template
Unsure → Consult references/platform-comparison.md

What stages are needed?

Always include: Lint, Test, Build
Optional: Security scanning, E2E tests, performance tests
Add deployment stage if deploying from CI

Which deployment platform?

Vercel → Use Vercel deployment examples
Netlify → Use Netlify CLI approach
AWS → Use AWS Actions/CLI
Custom → Implement custom deployment script

What triggers?

On push to main/develop
On pull request
On tag creation
Manual workflow dispatch

What environment variables needed?

Platform tokens (Vercel, Netlify, AWS)
API keys for external services
Build-time environment variables
Feature flags
Best Practices
Security
Store all secrets in platform secret management (never in code)
Use least-privilege tokens (read-only when possible)
Rotate secrets regularly
Audit secret access permissions
Never log secrets (use *** masking)
Performance
Cache dependencies aggressively
Parallelize independent jobs
Use matrix builds for multi-version testing
Fail fast: Run quick checks before slow ones
Optimize Docker layer caching
Reliability
Pin exact Node.js versions (18.x not just 18)
Commit lockfiles (package-lock.json)
Add retry logic for flaky external services
Set reasonable timeouts (10-15 minutes max)
Use continue-on-error for non-critical steps
Maintainability
Add comments explaining complex logic
Use reusable workflows/templates
Keep configs DRY (Don't Repeat Yourself)
Version control all pipeline changes
Document required secrets in README
Common Patterns
Multi-Environment Deployment
deploy_staging:
  environment: staging
  if: github.ref == 'refs/heads/develop'

deploy_production:
  environment: production
  if: github.ref == 'refs/heads/main'
  needs: [deploy_staging]

Matrix Testing
strategy:
  matrix:
    node-version: [16.x, 18.x, 20.x]
    os: [ubuntu-latest, windows-latest]

Conditional Steps
- name: Deploy
  if: github.event_name == 'push' && github.ref == 'refs/heads/main'
  run: npm run deploy

Artifact Management
- name: Upload build
  uses: actions/upload-artifact@v4
  with:
    name: build-output
    path: .next/
    retention-days: 7

- name: Download build
  uses: actions/download-artifact@v4
  with:
    name: build-output

Troubleshooting
Pipeline Failures
Check action/job logs for error messages
Verify environment variables and secrets are set
Test commands locally before adding to pipeline
Check for platform-specific issues in documentation
Slow Builds
Verify cache is working (check cache hit/miss logs)
Parallelize independent jobs
Use faster runners if available
Optimize dependency installation
Deployment Failures
Verify deployment tokens are valid
Check platform status pages
Review deployment logs
Test deployment commands locally
Resources
Templates (assets/)
github-actions-nodejs.yml: Complete GitHub Actions workflow
gitlab-ci-nodejs.yml: Complete GitLab CI pipeline
Reference Documentation (references/)
platform-comparison.md: Detailed comparison of CI/CD platforms, deployment targets, best practices, and common patterns
Example Usage

User Request: "Create a GitHub Actions workflow that runs tests and deploys to Vercel"

Steps:

Copy assets/github-actions-nodejs.yml template
Create .github/workflows/ directory if it doesn't exist
Save as .github/workflows/ci.yml
Update deployment section with Vercel credentials
Add secrets to GitHub repository settings:
VERCEL_TOKEN
VERCEL_ORG_ID
VERCEL_PROJECT_ID
Commit and push to trigger workflow

User Request: "Set up GitLab CI with staging and production environments"

Steps:

Copy assets/gitlab-ci-nodejs.yml template
Save as .gitlab-ci.yml in repository root
Configure GitLab CI/CD variables:
VERCEL_TOKEN
Other deployment credentials
Review manual approval settings for production
Commit to trigger pipeline
Advanced Configuration
Monorepo Support
paths:
  - 'apps/frontend/**'
  - 'packages/**'

Scheduled Runs
on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM

External Service Integration
- name: Notify Slack
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}

Security Scanning
- name: Run security audit
  run: npm audit --audit-level=moderate

- name: Check for vulnerabilities
  uses: snyk/actions/node@master
  env:
    SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

Weekly Installs
556
Repository
ailabs-393/ai-l…e-skills
GitHub Stars
357
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass