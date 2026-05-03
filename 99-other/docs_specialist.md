---
title: docs-specialist
url: https://skills.sh/mwguerra/claude-code-plugins/docs-specialist
---

# docs-specialist

skills/mwguerra/claude-code-plugins/docs-specialist
docs-specialist
Installation
$ npx skills add https://github.com/mwguerra/claude-code-plugins --skill docs-specialist
SKILL.md
Documentation Specialist Skill
Overview

This skill provides specialized expertise in technical documentation: generating docs from code, detecting drift between docs and implementation, validating quality, and applying consistent templates.

Documentation Reference

CRITICAL: Before working on documentation tasks, consult:

docs-specialist/skills/docs-specialist/references/documentation-patterns.md
Expertise Areas
1. Code-to-Docs Generation

Analyze source code and generate documentation automatically:

Process:

Scan code files (routes, models, components, services)
Extract structure (classes, functions, signatures)
Parse existing comments (JSDoc, docstrings)
Apply appropriate template
Generate formatted documentation
2. Docs-to-Code Sync Detection

Compare documentation against code to find discrepancies:

Status	Symbol	Meaning
Implemented	✅	Code matches documentation exactly
Partial	⚠️	Code exists but differs from docs
Not Implemented	❌	Documented but missing in code
Undocumented	📝	In code but not documented
3. Documentation Validation

Check quality, accuracy, and completeness:

Link integrity (internal and external)
Code example accuracy
Structure and formatting
Completeness by doc type
Technical accuracy against code
4. Template System

Apply consistent templates for different documentation types:

Template	Use For
readme	Project README
api-endpoint	REST API endpoint
component	UI component
model	Database model
service	Service class
guide	How-to guide
architecture	Architecture decision record
changelog	Release changelog
Commands
Command	Purpose
/docs-specialist:docs	Validate, generate, update, and check status
/docs-specialist:sync	Detect and fix drift between docs and code
/docs-specialist:template	List, view, and apply documentation templates
/docs-specialist:init	Create documentation folder structure
/docs-specialist:doctor	Diagnose and fix documentation issues

See each command's file for full syntax and options.

Working Principles
Accuracy First
Always verify against source code
Test code examples before documenting
Flag assumptions or uncertainties
Update immediately when code changes
Code Analysis Approach

When analyzing code for documentation:

Parse file structure (AST when possible)
Extract public interfaces first
Include type information
Find usage examples in tests
Respect existing documentation comments
Sync Detection Approach

When comparing docs to code:

Build inventory of documented items
Build inventory of code items
Match by name/path/signature
Categorize matches (exact, partial, missing)
Detail differences for partial matches
Documentation Standards
File Organization
docs/
├── README.md               # Documentation hub
├── api/                    # API reference
├── guides/                 # User guides
├── architecture/           # System design
└── development/            # Developer docs

Markdown Conventions
ATX-style headers (#)
Code blocks with language specification
Relative links for internal references
One sentence per line (for diffs)
Code Examples
Complete, runnable examples
Include imports/setup
Show expected output
Highlight key lines
Tool-Specific Files

Keep these in their original locations (DO NOT move to /docs):

CLAUDE.md - Root directory
.claude/commands/*.md - Command definitions
.claude/agents/*.md - Agent definitions
.cursorrules - Cursor AI configuration
Version Control
Use conventional commits: docs: description
Link doc commits to code commits when related
Group related documentation updates
Quality Checklist

Before considering documentation complete:

 All code examples tested and working
 Technical accuracy confirmed against code
 Links valid and correct
 Formatting consistent
 Procedures complete and actionable
 Sync check passes
 Validation score above threshold
Common Workflows
"I wrote new code, need docs"
/docs-specialist:docs generate <path>

"I changed code, update docs"
/docs-specialist:sync check
/docs-specialist:sync fix

"Audit documentation quality"
/docs-specialist:docs validate
/docs-specialist:sync check

"Set up docs for new project"
/docs-specialist:init
/docs-specialist:docs generate all

"Pre-release check"
/docs-specialist:doctor --check
/docs-specialist:sync check
/docs-specialist:docs validate

Success Metrics

Excellent documentation is:

Accurate - Reflects current code reality
Complete - Covers all necessary topics
In Sync - No drift from implementation
Clear - Easy to understand
Maintainable - Easy to update
Actionable - Readers can accomplish goals
Weekly Installs
19
Repository
mwguerra/claude…-plugins
GitHub Stars
29
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass