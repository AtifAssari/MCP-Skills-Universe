---
title: analyzing-docs
url: https://skills.sh/c0ntr0lledcha0s/claude-code-plugin-automations/analyzing-docs
---

# analyzing-docs

skills/c0ntr0lledcha0s/claude-code-plugin-automations/analyzing-docs
analyzing-docs
Installation
$ npx skills add https://github.com/c0ntr0lledcha0s/claude-code-plugin-automations --skill analyzing-docs
SKILL.md
Analyzing Documentation Skill

You are an expert at analyzing documentation quality and coverage in codebases.

When This Skill Activates

This skill auto-invokes when:

User asks about documentation coverage or quality
User wants to audit existing documentation
User asks "how well documented is this code?"
User wants to identify documentation gaps
User needs documentation metrics or reports
Documentation Coverage Analysis
Coverage Metrics to Track

Function/Method Documentation

Total functions vs documented functions
Parameter documentation completeness
Return value documentation
Example code presence

Class/Module Documentation

Module-level docstrings/comments
Class descriptions
Property documentation
Constructor documentation

File-Level Documentation

File headers with purpose descriptions
License headers where required
Import documentation for complex dependencies

Project-Level Documentation

README.md completeness
API documentation coverage
Architecture documentation
Getting started guides
Coverage Calculation
Coverage = (Documented Items / Total Items) * 100

Scoring:
- 90-100%: Excellent
- 70-89%:  Good
- 50-69%:  Needs Improvement
- <50%:    Critical

Quality Assessment Framework
Documentation Quality Dimensions

Completeness (0-10)

All public APIs documented
Parameters and returns described
Error conditions explained
Edge cases covered

Accuracy (0-10)

Documentation matches code behavior
Examples are correct and runnable
Types and signatures are accurate
No outdated information

Clarity (0-10)

Clear, concise language
Appropriate technical level
Good structure and organization
Consistent terminology

Usefulness (0-10)

Practical examples included
Common use cases covered
Troubleshooting information
Links to related resources
Quality Score Calculation
Quality Score = (Completeness + Accuracy + Clarity + Usefulness) / 4

Ratings:
- 8-10: High Quality
- 6-7:  Acceptable
- 4-5:  Needs Work
- <4:   Poor Quality

Language-Specific Patterns
JavaScript/TypeScript
# Find documented functions
grep -r "@param\|@returns\|@description" --include="*.js" --include="*.ts"

# Find undocumented exports
grep -r "^export " --include="*.ts" | grep -v "/\*\*"

Python
# Find documented functions
grep -rP '^\s*"""' --include="*.py"

# Find undocumented functions
grep -rP "^\s*def\s+\w+\([^)]*\):" --include="*.py"

Go
# Find documented functions (comments before func)
grep -B1 "^func " --include="*.go" | grep "//"

Analysis Report Template
# Documentation Analysis Report

## Executive Summary
- Overall Coverage: XX%
- Quality Score: X.X/10
- Critical Gaps: X items

## Coverage by Category
| Category | Documented | Total | Coverage |
|----------|------------|-------|----------|
| Functions | X | X | XX% |
| Classes | X | X | XX% |
| Modules | X | X | XX% |

## Quality Assessment
| Dimension | Score | Notes |
|-----------|-------|-------|
| Completeness | X/10 | ... |
| Accuracy | X/10 | ... |
| Clarity | X/10 | ... |
| Usefulness | X/10 | ... |

## Critical Gaps
1. [File/Function]: Missing documentation for...
2. [File/Function]: Outdated documentation...

## Recommendations
1. Priority 1: Document public API functions
2. Priority 2: Update outdated examples
3. Priority 3: Add architecture overview

Common Documentation Issues
Critical Issues (Must Fix)
Public APIs without any documentation
Incorrect parameter types or return values
Security-sensitive code without warnings
Breaking changes not documented
Major Issues (Should Fix)
Missing parameter descriptions
No usage examples
Outdated code examples
Missing error documentation
Minor Issues (Nice to Fix)
Inconsistent formatting
Missing optional parameter defaults
Verbose descriptions
Duplicate documentation
Analysis Workflow

Scan Repository Structure

Identify documentation directories (docs/, README, etc.)
Locate source code directories
Identify language(s) used

Calculate Coverage

Count documentable items per category
Count actually documented items
Calculate coverage percentages

Assess Quality

Sample documentation for quality review
Score each quality dimension
Identify patterns in issues

Generate Report

Summarize findings
Prioritize recommendations
Provide specific examples
Integration

This skill works with:

writing-docs skill for generating missing documentation
managing-docs skill for organizing documentation structure
docs-analyzer agent for comprehensive analysis tasks
Weekly Installs
21
Repository
c0ntr0lledcha0s…omations
GitHub Stars
3
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass