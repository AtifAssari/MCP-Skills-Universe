---
title: github-workflow
url: https://skills.sh/mindrally/skills/github-workflow
---

# github-workflow

skills/mindrally/skills/github-workflow
github-workflow
Installation
$ npx skills add https://github.com/mindrally/skills --skill github-workflow
SKILL.md
GitHub Workflow Best Practices

You are an expert in GitHub workflows, including pull requests, code reviews, GitHub Actions, issue management, and repository best practices.

Core Principles
Use pull requests for all code changes to enable review and discussion
Automate workflows with GitHub Actions for CI/CD
Maintain clear issue tracking and project management
Follow security best practices for repository access and secrets
Document repositories thoroughly with README and contributing guidelines
Pull Request Best Practices
Creating Effective Pull Requests

Keep PRs small and focused

One feature or fix per PR
Aim for under 400 lines of changes when possible
Split large features into stacked PRs

Write descriptive PR titles

Use conventional commit style: feat: add user authentication
Be specific about what the PR accomplishes

PR Description Template

## Summary
Brief description of changes and motivation.

## Changes
- Bullet points of specific changes made

## Testing
- How the changes were tested
- Steps to reproduce/verify

## Related Issues
Closes #123

## Screenshots (if applicable)


Link related issues

Use Closes #123 or Fixes #123 to auto-close issues
Reference related issues with #123
Stacked Pull Requests

For complex features, use stacked PRs:

Create a base feature branch
Create subsequent PRs that build on each other
Merge in order from base to top
Keep each PR small and reviewable
Code Review Guidelines
As a Reviewer
Review promptly - Respond within 24 hours when possible
Be constructive - Focus on improvement, not criticism
Ask questions - Seek to understand before suggesting changes
Prioritize feedback:
Blocking: Security issues, bugs, breaking changes
Important: Performance, maintainability
Nice-to-have: Style preferences, minor improvements
Comment Conventions

Use prefixes to indicate comment severity:

blocking: Must be addressed before merge
suggestion: Recommended improvement
question: Seeking clarification
nit: Minor style or preference (optional to address)
praise: Positive feedback on good code
Example Review Comments
blocking: This SQL query is vulnerable to injection.
Please use parameterized queries.

suggestion: Consider extracting this logic into a separate
function for better testability.

nit: Prefer `const` over `let` here since this value
is never reassigned.

Approval Criteria
All blocking comments addressed
Tests pass
CI/CD checks pass
At least one approval from code owner
GitHub Actions
Workflow Best Practices

Use workflow templates

name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm test


Cache dependencies

- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}


Use reusable workflows

jobs:
  call-workflow:
    uses: ./.github/workflows/reusable.yml
    with:
      environment: production
    secrets: inherit


Set appropriate timeouts

jobs:
  build:
    timeout-minutes: 10

Security in Actions
Use secrets for sensitive data
Pin action versions with SHA: uses: actions/checkout@a5ac7e51b41094c92402da3b24376905380afc29
Limit GITHUB_TOKEN permissions
Review third-party actions before use
permissions:
  contents: read
  pull-requests: write

Issue Management
Issue Templates

Create .github/ISSUE_TEMPLATE/ with templates:

Bug Report:

---
name: Bug Report
about: Report a bug
labels: bug
---

## Description
Clear description of the bug.

## Steps to Reproduce
1. Step one
2. Step two

## Expected Behavior
What should happen.

## Actual Behavior
What actually happens.

## Environment
- OS:
- Browser:
- Version:


Feature Request:

---
name: Feature Request
about: Suggest a new feature
labels: enhancement
---

## Problem
Describe the problem this feature would solve.

## Proposed Solution
Describe your proposed solution.

## Alternatives Considered
Other approaches you've considered.

Labels

Use consistent labels:

bug, enhancement, documentation
good first issue, help wanted
priority: high, priority: medium, priority: low
status: in progress, status: blocked
Repository Management
Branch Protection Rules

Configure for main branch:

Require pull request reviews
Require status checks to pass
Require conversation resolution
Require signed commits (optional)
Restrict force pushes
CODEOWNERS File
# .github/CODEOWNERS
* @default-team
/docs/ @docs-team
/src/api/ @backend-team
*.js @frontend-team

Security Best Practices

Enable security features

Dependabot alerts and updates
Code scanning with CodeQL
Secret scanning

Manage secrets properly

Use repository or organization secrets
Rotate secrets regularly
Never commit secrets to code

Access control

Use teams for permissions
Follow principle of least privilege
Audit access regularly
Automation Recommendations
Auto-merge for Dependabot
name: Dependabot auto-merge
on: pull_request

permissions:
  contents: write
  pull-requests: write

jobs:
  dependabot:
    runs-on: ubuntu-latest
    if: github.actor == 'dependabot[bot]'
    steps:
      - name: Auto-merge minor updates
        run: gh pr merge --auto --squash "$PR_URL"
        env:
          PR_URL: ${{ github.event.pull_request.html_url }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}

Release Automation

Use semantic-release or release-please for automated releases based on conventional commits.

Weekly Installs
282
Repository
mindrally/skills
GitHub Stars
88
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass