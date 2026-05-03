---
rating: ⭐⭐⭐
title: bitbucket-workflow
url: https://skills.sh/mindrally/skills/bitbucket-workflow
---

# bitbucket-workflow

skills/mindrally/skills/bitbucket-workflow
bitbucket-workflow
Installation
$ npx skills add https://github.com/mindrally/skills --skill bitbucket-workflow
SKILL.md
Bitbucket Workflow Best Practices

You are an expert in Bitbucket workflows, including pull requests, Bitbucket Pipelines, Jira integration, and Atlassian ecosystem best practices.

Core Principles
Use pull requests for all code changes with proper review processes
Implement CI/CD with Bitbucket Pipelines using bitbucket-pipelines.yml
Leverage Jira integration for seamless issue tracking
Follow branching models like Gitflow for structured development
Maintain security through branch permissions and access controls
Pull Request Best Practices
Creating Effective Pull Requests

Keep PRs focused and reviewable

One feature or fix per PR
Include context in the description

PR Title Convention

Reference Jira issue: PROJ-123: Add user authentication
Use conventional format: feat: implement login page

PR Description Template

## Summary
Brief description of changes and motivation.

## Jira Issue
[PROJ-123](https://your-org.atlassian.net/browse/PROJ-123)

## Changes
- List of specific changes made

## Testing
- How the changes were tested
- Manual testing steps

## Checklist
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] Pipeline passes

Code Review in Bitbucket
Add reviewers - Select appropriate team members
Use tasks - Create tasks for actionable feedback
Approve or request changes - Clear approval workflow
Resolve discussions - Address all feedback before merge
Merge Strategies
Merge commit: Preserves full branch history
Squash: Combines commits into single commit
Fast-forward: Linear history when possible
Bitbucket Pipelines
Basic Pipeline Configuration
image: node:20

definitions:
  caches:
    npm: ~/.npm

  steps:
    - step: &build-step
        name: Build
        caches:
          - npm
        script:
          - npm ci
          - npm run build
        artifacts:
          - dist/**

    - step: &test-step
        name: Test
        caches:
          - npm
        script:
          - npm ci
          - npm test

pipelines:
  default:
    - step: *build-step
    - step: *test-step

  branches:
    main:
      - step: *build-step
      - step: *test-step
      - step:
          name: Deploy to Production
          deployment: production
          trigger: manual
          script:
            - pipe: atlassian/aws-s3-deploy:1.1.0
              variables:
                AWS_ACCESS_KEY_ID: $AWS_ACCESS_KEY_ID
                AWS_SECRET_ACCESS_KEY: $AWS_SECRET_ACCESS_KEY
                AWS_DEFAULT_REGION: 'us-east-1'
                S3_BUCKET: 'my-bucket'
                LOCAL_PATH: 'dist'

    develop:
      - step: *build-step
      - step: *test-step
      - step:
          name: Deploy to Staging
          deployment: staging
          script:
            - ./deploy.sh staging

Pipeline Features
Parallel Steps
pipelines:
  default:
    - parallel:
        - step:
            name: Unit Tests
            script:
              - npm test:unit
        - step:
            name: Integration Tests
            script:
              - npm test:integration
        - step:
            name: Lint
            script:
              - npm run lint

Conditional Steps
pipelines:
  pull-requests:
    '**':
      - step:
          name: Build and Test
          script:
            - npm ci
            - npm test
          condition:
            changesets:
              includePaths:
                - "src/**"
                - "package.json"

Custom Pipes
pipelines:
  default:
    - step:
        name: Deploy
        script:
          - pipe: atlassian/aws-ecs-deploy:1.6.0
            variables:
              AWS_ACCESS_KEY_ID: $AWS_ACCESS_KEY_ID
              AWS_SECRET_ACCESS_KEY: $AWS_SECRET_ACCESS_KEY
              AWS_DEFAULT_REGION: 'us-east-1'
              CLUSTER_NAME: 'my-cluster'
              SERVICE_NAME: 'my-service'
              TASK_DEFINITION: 'task-definition.json'

Services for Testing
definitions:
  services:
    postgres:
      image: postgres:15
      variables:
        POSTGRES_DB: test_db
        POSTGRES_USER: test_user
        POSTGRES_PASSWORD: test_pass
    redis:
      image: redis:7

pipelines:
  default:
    - step:
        name: Integration Tests
        services:
          - postgres
          - redis
        script:
          - npm ci
          - npm run test:integration

Caching
definitions:
  caches:
    npm: ~/.npm
    pip: ~/.cache/pip
    gradle: ~/.gradle/caches

pipelines:
  default:
    - step:
        caches:
          - npm
        script:
          - npm ci
          - npm run build

Jira Integration
Smart Commits

Enable smart commits to update Jira issues from commit messages:

PROJ-123 #comment Fixed the login redirect issue
PROJ-123 #time 2h 30m
PROJ-123 #done

Branch Naming

Include Jira issue key in branch names:

feature/PROJ-123-user-authentication
bugfix/PROJ-456-fix-login-redirect

This automatically links branches to issues.

Automation Rules

Set up Jira automation:

Move issue to "In Progress" when branch created
Move issue to "In Review" when PR opened
Move issue to "Done" when PR merged
Branching Models
Gitflow in Bitbucket
pipelines:
  branches:
    main:
      - step:
          name: Deploy Production
          deployment: production
          script:
            - ./deploy.sh production

    develop:
      - step:
          name: Deploy Staging
          deployment: staging
          script:
            - ./deploy.sh staging

    'release/*':
      - step:
          name: Release Build
          script:
            - npm run build:release

    'feature/*':
      - step:
          name: Feature Build and Test
          script:
            - npm ci
            - npm test

    'hotfix/*':
      - step:
          name: Hotfix Build
          script:
            - npm ci
            - npm test

Branch Permissions

Configure in Repository settings > Branch permissions:

Main branch:

No direct pushes
Require pull request
Minimum 1 approval
Require passing builds
Require all tasks resolved

Develop branch:

Require pull request
Minimum 1 approval
Require passing builds
Repository Management
Default Reviewers

Set up default reviewers for consistent code review:

Add team leads as default reviewers
Use CODEOWNERS-like patterns
Merge Checks

Enable merge checks:

Minimum approvals
No unresolved tasks
Passing builds
No changes requested
Access Levels
Admin: Full control
Write: Push and merge
Read: Clone and view
Security Best Practices
Repository Variables

Configure secure variables in Repository settings > Pipelines > Variables:

# Reference in pipeline
script:
  - echo "Deploying with token"
  - ./deploy.sh --token=$DEPLOY_TOKEN


Variable options:

Secured: Masked in logs
Required for deployment
IP Allowlisting

Restrict pipeline access to specific IP ranges for deployment environments.

Access Tokens

Use repository or project access tokens instead of personal tokens:

Scoped to specific repositories
Easier to rotate
Better audit trail
Deployment Environments
Environment Configuration
pipelines:
  branches:
    main:
      - step:
          name: Deploy to Production
          deployment: production
          script:
            - ./deploy.sh


Configure environments in Repository settings > Deployments:

Set environment variables per environment
Configure deployment permissions
View deployment history
Deployment Permissions
Require specific user approval for production
Set up deployment windows
Enable deployment freeze periods
Atlassian Ecosystem Integration
Confluence Integration
Link repositories to Confluence spaces
Embed code snippets
Auto-update documentation from commits
Trello Integration
Connect cards to commits
Automatic card movement on PR events
Opsgenie Integration
Trigger alerts from pipeline failures
On-call notifications for deployment issues
Best Practices Summary
Use descriptive branch names with Jira keys
Configure branch permissions for main branches
Implement comprehensive pipelines with proper stages
Use pipes for common tasks (AWS, Docker, etc.)
Enable smart commits for Jira updates
Set up deployment environments with proper permissions
Use repository variables for secrets
Configure merge checks for quality gates
Leverage Atlassian integrations for seamless workflow
Weekly Installs
304
Repository
mindrally/skills
GitHub Stars
88
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass