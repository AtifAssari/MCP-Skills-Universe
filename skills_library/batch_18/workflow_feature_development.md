---
title: workflow-feature-development
url: https://skills.sh/nickcrew/claude-ctx-plugin/workflow-feature-development
---

# workflow-feature-development

skills/nickcrew/claude-ctx-plugin/workflow-feature-development
workflow-feature-development
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill workflow-feature-development
SKILL.md
Feature Development Workflow

Step-by-step process for developing features properly.

Phase 1: Design

Agents: system-architect

Design feature architecture
Identify components and boundaries
Define API contracts
Document data flow

Output: Architecture diagram, component list, API contracts

Phase 2: Planning

Agents: requirements-analyst

Break down into implementable tasks
Identify dependencies
Estimate timeline
Define acceptance criteria

Output: Task breakdown, dependency graph, timeline

Phase 3: Implementation
Implement feature following architecture
Work in small, testable increments
Commit frequently with clear messages
Phase 4: Review

Agents: code-reviewer, security-auditor

Code review for quality and standards
Security review for vulnerabilities
Focus: auth, input validation, data access

Blocking: Must pass before proceeding

Phase 5: Testing

Agents: test-automator

Unit tests (80% coverage target)
Integration tests
E2E tests for critical paths
Phase 6: Performance

Agents: performance-engineer

Validate against thresholds:

Response time: <200ms
Memory usage: <100MB
Bundle size: <500KB
Phase 7: Documentation

Agents: technical-writer

API documentation
User guide updates
Changelog entry
Phase 8: Deployment Prep

Agents: deployment-engineer

Checklist:

 Version bump
 Changelog updated
 Migration scripts ready
 Rollback plan documented
Success Criteria
 All tests pass
 Security scan clean
 Performance within limits
 Documentation complete
Rollback Plan
Revert database migrations
Restore previous version
Notify stakeholders
Weekly Installs
28
Repository
nickcrew/claude…x-plugin
GitHub Stars
15
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass