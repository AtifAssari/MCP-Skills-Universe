---
title: accelint-ts-best-practices
url: https://skills.sh/gohypergiant/agent-skills/accelint-ts-best-practices
---

# accelint-ts-best-practices

skills/gohypergiant/agent-skills/accelint-ts-best-practices
accelint-ts-best-practices
Installation
$ npx skills add https://github.com/gohypergiant/agent-skills --skill accelint-ts-best-practices
SKILL.md
JavaScript and TypeScript Best Practices

Comprehensive coding standards for JavaScript and TypeScript applications, designed for AI agents and LLMs working with modern JavaScript/TypeScript codebases.

Note: This skill focuses on general best practices, TypeScript patterns, and safety. For performance optimization, use the accelint-ts-performance skill instead.

When to Use This Skill

This skill provides expert-level patterns for JavaScript and TypeScript code. Load AGENTS.md to scan rule summaries and identify relevant optimizations for your task.

How to Use

This skill uses a progressive disclosure structure to minimize context usage:

1. Start with the Overview (AGENTS.md)

Read AGENTS.md for a concise overview of all rules with one-line summaries organized by category.

2. Load Specific Rules as Needed

When you identify a relevant pattern or issue, load the corresponding reference file for detailed implementation guidance:

Quick Start:

quick-start.md - Complete workflow examples with before/after code

General Best Practices:

naming-conventions.md - Descriptive names, qualifier ordering, boolean prefixes
functions.md - Function size, parameters, explicit values
control-flow.md - Early returns, flat structure, block style
state-management.md - const vs let, immutability, pure functions
return-values.md - Return zero values instead of null/undefined
misc.md - Line endings, defensive programming, technical debt
code-duplication.md - Extract common patterns, DRY principle, when to consolidate

TypeScript:

any.md - Avoid any, use unknown or generics
enums.md - Use as const objects instead of enum
type-vs-interface.md - Prefer type over interface

Safety:

input-validation.md - Validate external data with schemas
assertions.md - Split assertions, include values
error-handling.md - Handle all errors explicitly
error-messages.md - User-friendly vs developer-specific messages

Performance:

For performance optimization tasks, use the accelint-ts-performance skill for comprehensive profiling workflows and optimization patterns

Documentation:

For documentation tasks, use the accelint-ts-documentation skill for comprehensive JSDoc and comment guidance
3. Apply the Pattern

Each reference file contains:

❌ Incorrect examples showing the anti-pattern
✅ Correct examples showing the optimal implementation
Explanations of why the pattern matters
4. Use the Report Template

When this skill is invoked, use the standardized report format:

Template: assets/output-report-template.md

The report format provides:

Executive Summary with impact assessment
Severity levels (Critical, High, Medium, Low) for prioritization
Impact analysis (potential bugs, type safety, maintainability, runtime failures)
Categorization (Type Safety, Safety, State Management, Return Values, Code Quality)
Pattern references linking to detailed guidance in references/
Phase 2 summary table for tracking all issues

When to use the audit template:

Skill invoked directly via /accelint-ts-best-practices <path>
User asks to "review code quality" or "audit code" across file(s), invoking skill implicitly

When NOT to use the report template:

User asks to "fix this type error" (direct implementation)
User asks "what's wrong with this code?" (answer the question)
User requests specific fixes (apply fixes directly without formal report)
Weekly Installs
146
Repository
gohypergiant/ag…t-skills
GitHub Stars
11
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass