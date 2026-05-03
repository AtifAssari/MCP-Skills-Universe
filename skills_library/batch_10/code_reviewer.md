---
title: code-reviewer
url: https://skills.sh/nodnarbnitram/claude-code-extensions/code-reviewer
---

# code-reviewer

skills/nodnarbnitram/claude-code-extensions/code-reviewer
code-reviewer
Installation
$ npx skills add https://github.com/nodnarbnitram/claude-code-extensions --skill code-reviewer
SKILL.md
Code Reviewer

Perform comprehensive code reviews focusing on quality, security, and maintainability.

Instructions
Read the target files using the Read tool
Search for patterns and related code using Grep
Find related files using Glob
Analyze code against the review checklist
Provide structured feedback with severity levels
Review Checklist
Code Quality
 Code is simple and readable
 Functions and variables are well-named
 No duplicated code (DRY principle)
 Appropriate comments for complex logic
 Consistent code style
Security
 No exposed secrets or API keys
 Input validation implemented
 SQL injection prevention
 XSS prevention for web code
 Proper authentication/authorization checks
Error Handling
 Errors are caught and handled appropriately
 Meaningful error messages
 No silent failures
 Proper logging for debugging
Performance
 No obvious performance bottlenecks
 Efficient algorithms and data structures
 Appropriate caching where needed
 Database queries are optimized
Testing
 Adequate test coverage
 Edge cases are tested
 Tests are readable and maintainable
Output Format

Organize feedback by severity:

Critical (Must Fix)

Issues that could cause security vulnerabilities, data loss, or crashes.

Warning (Should Fix)

Issues that could cause bugs, poor performance, or maintenance problems.

Suggestion (Consider)

Improvements for readability, consistency, or best practices.

Example Feedback
### Critical
- **SQL Injection vulnerability** in `user_service.py:45`
  - User input passed directly to query without sanitization
  - Fix: Use parameterized queries

### Warning
- **Missing error handling** in `api_client.py:23`
  - Network errors will crash the application
  - Fix: Add try/catch with appropriate error response

### Suggestion
- Consider extracting the validation logic in `validators.py:78-95` into a separate function for reusability

Weekly Installs
48
Repository
nodnarbnitram/c…tensions
GitHub Stars
8
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass