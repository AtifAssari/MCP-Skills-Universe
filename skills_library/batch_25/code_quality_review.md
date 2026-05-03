---
title: code-quality-review
url: https://skills.sh/dauquangthanh/hanoi-rainbow/code-quality-review
---

# code-quality-review

skills/dauquangthanh/hanoi-rainbow/code-quality-review
code-quality-review
Installation
$ npx skills add https://github.com/dauquangthanh/hanoi-rainbow --skill code-quality-review
SKILL.md
Code Quality Review
Overview

Conducts systematic code quality analysis across multiple dimensions: maintainability, readability, complexity, design patterns, naming conventions, code duplication, and adherence to best practices. Produces actionable feedback with severity ratings and specific improvement recommendations.

Core Capabilities
Code Smells Detection - Identifies bloaters, object-orientation abusers, change preventers, dispensables, and couplers
Complexity Analysis - Measures cyclomatic and cognitive complexity with risk assessment
Maintainability Assessment - Evaluates code maintainability index and technical debt
Design Pattern Evaluation - Reviews architectural patterns and SOLID principles
Best Practices Validation - Checks adherence to language-specific standards and conventions
Review Workflow
Step 1: Scope Assessment

Determine review scope based on change size:

Small (<100 lines): Quick correctness check, 15-30 minutes
Medium (100-500 lines): Full quality analysis, 1-2 hours
Large (>500 lines): Architectural review, break into smaller reviews if possible, 2-4 hours

For scope-specific guidance, see review-scope-guidelines.md

Step 2: Initial Assessment

Gather Context:

Identify programming language and framework
Understand project type (web app, API, library, CLI, etc.)
Note existing coding standards or style guides
Check for linter configuration files (.eslintrc, .pylintrc, checkstyle.xml, etc.)

Read the Code:

Start with entry points (main files, index files)
Review module/package organization
Check dependency management
Examine test files if available
Step 3: Quality Analysis

Analyze code across key dimensions:

Code Smells: Long methods, large classes, duplicate code, dead code, etc.
Complexity: Cyclomatic complexity (target <15), cognitive complexity, nesting depth
Maintainability: Clear naming, proper abstraction, separation of concerns
Design Patterns: Appropriate pattern usage, SOLID principles adherence
Best Practices: Language idioms, error handling, resource management

For detailed analysis criteria and thresholds, see review-workflow.md

For quality metrics and thresholds, see quality-metrics-reference.md

Step 4: Document Findings

Structure the review report with:

Executive summary with scores and top priorities
Detailed findings with severity, location, description, and recommendations
Metrics summary with current vs. target values
Prioritized recommendations (P0-P3)
Positive observations acknowledging good practices
Technical debt summary with effort estimates

For complete report structure and output guidelines, see review-report-format.md

Quality Assurance

Use the checklist to ensure comprehensive reviews:

Code organization and structure
Naming conventions and clarity
Complexity thresholds
Error handling patterns
Testing and documentation
Security considerations
Performance implications

For complete checklist, see best-practices-checklist.md

Common Pitfalls

Avoid these common review mistakes:

Focusing only on style issues instead of substantive problems
Being overly critical without actionable suggestions
Ignoring context and business constraints
Overwhelming with too many issues at once
Using vague terms without explanation
Forgetting to acknowledge good practices

For detailed guidance, see common-pitfalls-to-avoid.md

Example Patterns

For reference when identifying critical issues in your review, see examples of common high-severity problems in critical-issues.md

Weekly Installs
37
Repository
dauquangthanh/h…-rainbow
GitHub Stars
10
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass