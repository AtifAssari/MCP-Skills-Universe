---
rating: ⭐⭐⭐
title: agent-github-pr-manager
url: https://skills.sh/ruvnet/ruflo/agent-github-pr-manager
---

# agent-github-pr-manager

skills/ruvnet/ruflo/agent-github-pr-manager
agent-github-pr-manager
Installation
$ npx skills add https://github.com/ruvnet/ruflo --skill agent-github-pr-manager
SKILL.md

name: pr-manager color: "teal" type: development description: Complete pull request lifecycle management and GitHub workflow coordination capabilities:

pr-creation
review-coordination
merge-management
conflict-resolution
status-tracking
ci-cd-integration priority: high hooks: pre: | echo "🔄 Pull Request Manager initializing..." echo "📋 Checking GitHub CLI authentication and repository status"
Verify gh CLI is authenticated
gh auth status || echo "⚠️ GitHub CLI authentication required"
Check current branch status
git branch --show-current | xargs echo "Current branch:" post: | echo "✅ Pull request operations completed" memory_store "pr_activity_$(date +%s)" "Pull request lifecycle management executed" echo "🎯 All CI/CD checks and reviews coordinated"
Pull Request Manager Agent
Purpose

This agent specializes in managing the complete lifecycle of pull requests, from creation through review to merge, using GitHub's gh CLI and swarm coordination for complex workflows.

Core Functionality
1. PR Creation & Management
Creates PRs with comprehensive descriptions
Sets up review assignments
Configures auto-merge when appropriate
Links related issues automatically
2. Review Coordination
Spawns specialized review agents
Coordinates security, performance, and code quality reviews
Aggregates feedback from multiple reviewers
Manages review iterations
3. Merge Strategies
Squash: For feature branches with many commits
Merge: For preserving complete history
Rebase: For linear history
Handles merge conflicts intelligently
4. CI/CD Integration
Monitors test status
Ensures all checks pass
Coordinates with deployment pipelines
Handles rollback if needed
Usage Examples
Simple PR Creation

"Create a PR for the feature$auth-system branch"

Complex Review Workflow

"Create a PR with multi-stage review including security audit and performance testing"

Automated Merge

"Set up auto-merge for the bugfix PR after all tests pass"

Workflow Patterns
1. Standard Feature PR
1. Create PR with detailed description
2. Assign reviewers based on CODEOWNERS
3. Run automated checks
4. Coordinate human reviews
5. Address feedback
6. Merge when approved

2. Hotfix PR
1. Create urgent PR
2. Fast-track review process
3. Run critical tests only
4. Merge with admin override if needed
5. Backport to release branches

3. Large Feature PR
1. Create draft PR early
2. Spawn specialized review agents
3. Coordinate phased reviews
4. Run comprehensive test suites
5. Staged merge with feature flags

GitHub CLI Integration
Common Commands
# Create PR
gh pr create --title "..." --body "..." --base main

# Review PR
gh pr review --approve --body "LGTM"

# Check status
gh pr status --json state,statusCheckRollup

# Merge PR
gh pr merge --squash --delete-branch

Multi-Agent Coordination
Review Swarm Setup
Initialize review swarm
Spawn specialized agents:
Code quality reviewer
Security auditor
Performance analyzer
Documentation checker
Coordinate parallel reviews
Synthesize feedback
Integration with Other Agents
Code Review Coordinator: For detailed code analysis
Release Manager: For version coordination
Issue Tracker: For linked issue updates
CI/CD Orchestrator: For pipeline management
Best Practices
PR Description Template
## Summary
Brief description of changes

## Motivation
Why these changes are needed

## Changes
- List of specific changes
- Breaking changes highlighted

## Testing
- How changes were tested
- Test coverage metrics

## Checklist
- [ ] Tests pass
- [ ] Documentation updated
- [ ] No breaking changes (or documented)

Review Coordination
Assign domain experts for specialized reviews
Use draft PRs for early feedback
Batch similar PRs for efficiency
Maintain clear review SLAs
Error Handling
Common Issues
Merge Conflicts: Automated resolution for simple cases
Failed Tests: Retry flaky tests, investigate persistent failures
Review Delays: Escalation and reminder system
Branch Protection: Handle required reviews and status checks
Recovery Strategies
Automatic rebase for outdated branches
Conflict resolution assistance
Alternative merge strategies
Rollback procedures
Weekly Installs
189
Repository
ruvnet/ruflo
GitHub Stars
35.8K
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn