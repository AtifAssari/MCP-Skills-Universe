---
title: code-review
url: https://skills.sh/popup-studio-ai/bkit-claude-code/code-review
---

# code-review

skills/popup-studio-ai/bkit-claude-code/code-review
code-review
Installation
$ npx skills add https://github.com/popup-studio-ai/bkit-claude-code --skill code-review
SKILL.md
Code Review Skill

Skill for code quality analysis and review

Arguments
Argument	Description	Example
[file]	Review specific file	/code-review src/lib/auth.ts
[directory]	Review entire directory	/code-review src/features/
[pr]	PR review (PR number)	/code-review pr 123
Review Categories
1. Code Quality
Duplicate code detection
Function/file complexity analysis
Naming convention check
Type safety verification
2. Bug Detection
Potential bug pattern detection
Null/undefined handling check
Error handling inspection
Boundary condition verification
3. Security
XSS/CSRF vulnerability check
SQL Injection pattern detection
Sensitive information exposure check
Authentication/authorization logic review
4. Performance
N+1 query pattern detection
Unnecessary re-render check
Memory leak pattern detection
Optimization opportunity identification
Review Output Format
## Code Review Report

### Summary
- Files reviewed: N
- Issues found: N (Critical: N, Major: N, Minor: N)
- Score: N/100

### Critical Issues
1. [FILE:LINE] Issue description
   Suggestion: ...

### Major Issues
...

### Minor Issues
...

### Recommendations
- ...

Agent Integration

This Skill calls the code-analyzer Agent for in-depth code analysis.

Agent	Role
code-analyzer	Code quality, security, performance analysis
Usage Examples
# Review specific file
/code-review src/lib/auth.ts

# Review entire directory
/code-review src/features/user/

# PR review
/code-review pr 42

# Review current changes
/code-review staged

Confidence-Based Filtering

code-analyzer Agent uses confidence-based filtering:

Confidence	Display	Description
High (90%+)	Always shown	Definite issues
Medium (70-89%)	Selectively shown	Possible issues
Low (<70%)	Hidden	Uncertain suggestions
PDCA Integration
Phase: Check (Quality verification)
Trigger: Auto-suggested after implementation
Output: docs/03-analysis/code-review-{date}.md
Weekly Installs
58
Repository
popup-studio-ai…ude-code
GitHub Stars
523
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass