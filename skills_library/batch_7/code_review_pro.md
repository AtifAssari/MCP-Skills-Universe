---
title: code-review-pro
url: https://skills.sh/onewave-ai/claude-skills/code-review-pro
---

# code-review-pro

skills/onewave-ai/claude-skills/code-review-pro
code-review-pro
Installation
$ npx skills add https://github.com/onewave-ai/claude-skills --skill code-review-pro
Summary

Comprehensive code analysis covering security vulnerabilities, performance bottlenecks, maintainability issues, and best practice violations.

Scans for critical security flaws including SQL injection, XSS, authentication gaps, unsafe deserialization, and credential exposure
Identifies performance problems such as N+1 queries, inefficient algorithms, memory leaks, and unnecessary re-renders
Evaluates code quality across duplication, function length, cyclomatic complexity, naming clarity, and error handling
Provides actionable fixes with before/after code examples, severity prioritization, and explanations of why changes matter
Covers language-specific idioms, framework conventions, SOLID principles, design patterns, and testing approaches
SKILL.md
Code Review Pro

Deep code analysis covering security, performance, maintainability, and best practices.

When to Use This Skill

Activate when the user:

Asks for a code review
Wants security vulnerability scanning
Needs performance analysis
Asks to "review this code" or "audit this code"
Mentions finding bugs or improvements
Wants refactoring suggestions
Requests best practice validation
Instructions

Security Analysis (Critical Priority)

SQL injection vulnerabilities
XSS (cross-site scripting) risks
Authentication/authorization issues
Secrets or credentials in code
Unsafe deserialization
Path traversal vulnerabilities
CSRF protection
Input validation gaps
Insecure cryptography
Dependency vulnerabilities

Performance Analysis

N+1 query problems
Inefficient algorithms (check Big O complexity)
Memory leaks
Unnecessary re-renders (React/Vue)
Missing indexes (database queries)
Blocking operations
Resource cleanup (file handles, connections)
Caching opportunities
Excessive network calls
Large bundle sizes

Code Quality & Maintainability

Code duplication (DRY violations)
Function/method length (should be <50 lines)
Cyclomatic complexity
Unclear naming
Missing error handling
Inconsistent style
Missing documentation
Hard-coded values that should be constants
God classes/functions
Tight coupling

Best Practices

Language-specific idioms
Framework conventions
SOLID principles
Design patterns usage
Testing approach
Logging and monitoring
Accessibility (for UI code)
Type safety
Null/undefined handling

Bugs and Edge Cases

Logic errors
Off-by-one errors
Race conditions
Null pointer exceptions
Unhandled edge cases
Timezone issues
Encoding problems
Floating point precision

Provide Actionable Fixes

Show specific code changes
Explain why change is needed
Include before/after examples
Prioritize by severity
Output Format
# Code Review Report

## 🚨 Critical Issues (Fix Immediately)
### 1. SQL Injection Vulnerability (line X)
**Severity**: Critical
**Issue**: User input directly concatenated into SQL query
**Impact**: Database compromise, data theft

**Current Code:**
```javascript
const query = `SELECT * FROM users WHERE email = '${userEmail}'`;


Fixed Code:

const query = 'SELECT * FROM users WHERE email = ?';
db.query(query, [userEmail]);


Explanation: Always use parameterized queries to prevent SQL injection.

⚠️ High Priority Issues
2. Performance: N+1 Query Problem (line Y)

[Details...]

💡 Medium Priority Issues
3. Code Quality: Function Too Long (line Z)

[Details...]

✅ Low Priority / Nice to Have
4. Consider Using Const Instead of Let

[Details...]

📊 Summary
Total Issues: 12
Critical: 2
High: 4
Medium: 4
Low: 2
🎯 Quick Wins

Changes with high impact and low effort:

[Fix 1]
[Fix 2]
🏆 Strengths
Good error handling in X
Clear naming conventions
Well-structured modules
🔄 Refactoring Opportunities
Extract Method: Lines X-Y could be extracted into calculateDiscount()
Remove Duplication: [specific code blocks]
📚 Resources
OWASP SQL Injection Guide
Performance Best Practices

## Examples

**User**: "Review this authentication code"
**Response**: Analyze auth logic → Identify security issues (weak password hashing, no rate limiting) → Check token handling → Note missing CSRF protection → Provide specific fixes with code examples → Prioritize by severity

**User**: "Can you find performance issues in this React component?"
**Response**: Analyze component → Identify unnecessary re-renders → Find missing useMemo/useCallback → Note large state objects → Check for expensive operations in render → Provide optimized version with explanations

**User**: "Review this API endpoint"
**Response**: Check input validation → Analyze error handling → Test for SQL injection → Review authentication → Check rate limiting → Examine response structure → Suggest improvements with code samples

## Best Practices

- Always prioritize security issues first
- Provide specific line numbers for issues
- Include before/after code examples
- Explain *why* something is a problem
- Consider the language/framework context
- Don't just criticize—acknowledge good code too
- Suggest gradual improvements for large refactors
- Link to documentation for recommendations
- Consider project constraints (legacy code, deadlines)
- Balance perfectionism with pragmatism
- Focus on impactful changes
- Group similar issues together
- Make recommendations actionable

Weekly Installs
2.1K
Repository
onewave-ai/claude-skills
GitHub Stars
107
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail