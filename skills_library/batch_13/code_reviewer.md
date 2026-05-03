---
title: code-reviewer
url: https://skills.sh/beshkenadze/claude-skills-marketplace/code-reviewer
---

# code-reviewer

skills/beshkenadze/claude-skills-marketplace/code-reviewer
code-reviewer
Installation
$ npx skills add https://github.com/beshkenadze/claude-skills-marketplace --skill code-reviewer
SKILL.md
Code Reviewer
Overview

Provides comprehensive code review capabilities including quality analysis, security scanning, and best practice recommendations.

Instructions

When reviewing code:

Read the code thoroughly before making any suggestions
Identify issues by category:
Security vulnerabilities (OWASP Top 10)
Performance concerns
Code style and readability
Logic errors and bugs
Missing error handling
Prioritize feedback from critical to minor
Suggest fixes with concrete code examples
Review Categories
Security
SQL injection, XSS, command injection
Authentication/authorization flaws
Sensitive data exposure
Insecure dependencies
Performance
N+1 queries
Memory leaks
Unnecessary computations
Missing caching opportunities
Quality
DRY violations
SOLID principle violations
Complex conditionals
Missing tests
Examples
Example: Security Review

User Request: "Review this login function for security issues"

Response Format:

## Security Review: login()

### Critical Issues
1. **SQL Injection** (Line 15)
   - Current: `query = f"SELECT * FROM users WHERE email='{email}'"`
   - Fix: Use parameterized queries

### Recommendations
- Add rate limiting
- Implement account lockout

Guidelines
Do
Be specific with line numbers when possible
Provide working code examples for fixes
Prioritize actionable feedback
Acknowledge good patterns when found
Read entire file before commenting
Don't
Nitpick style issues (leave to linters)
Block on subjective preferences
Review generated/vendored code
Make vague suggestions without examples
Weekly Installs
10
Repository
beshkenadze/cla…ketplace
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass