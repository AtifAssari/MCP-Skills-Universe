---
rating: ⭐⭐
title: markdown-linter-fixer
url: https://skills.sh/s2005/markdown-linter-fixer-skill/markdown-linter-fixer
---

# markdown-linter-fixer

skills/s2005/markdown-linter-fixer-skill/markdown-linter-fixer
markdown-linter-fixer
Installation
$ npx skills add https://github.com/s2005/markdown-linter-fixer-skill --skill markdown-linter-fixer
SKILL.md
Markdown Linter Fixer
Contents
Overview
When to Use This Skill
Workflow Process
Phase 1: Environment Setup & Prerequisites
Phase 2: Diagnostic Assessment
Phase 3: Issue Analysis
Phase 4: Automatic Fixes
Phase 5: Manual Fixes
Phase 6: Verification & Reporting
Quick Reference Checklist
Key Principles
Common Scenarios
Resources
Overview

Systematically fix linting issues in *.md files using markdownlint-cli2 through a structured workflow that diagnoses, fixes automatically where possible, and guides manual fixes when needed.

When to Use This Skill

Use this skill when:

Fixing markdown linting errors in projects
Standardizing markdown formatting across multiple files
Addressing ordered list numbering issues (MD029)
Preparing markdown documentation for quality standards
Setting up markdown linting for the first time in a project
Workflow Process
Phase 1: Environment Setup & Prerequisites
Verify markdownlint-cli2 Installation

Check if markdownlint-cli2 is installed:

markdownlint-cli2 --version


If missing, install it globally via npm:

npm install -g markdownlint-cli2


Handle any permission or installation errors by suggesting:

Local installation: npm install --save-dev markdownlint-cli2
Using npx: npx markdownlint-cli2
User-specific npm directory configuration
Configuration File Check

Look for existing markdown configuration files in the project root:

.markdownlint-cli2.jsonc
.markdownlint.json
.markdownlint.yaml
.markdownlint.yml
.markdownlintrc

If none exist, create .markdownlint-cli2.jsonc with:

{
  "config": {
    "MD013": false
  },
  "ignores": []
}


This disables max line length warnings while keeping other rules active. The ignores array can be used to exclude specific files from linting (e.g., example files with intentional errors).

IMPORTANT - Configuration Policy:

Do not ignore/hide linting errors by modifying .markdownlint-cli2.jsonc
Only modify the ignores array based on:
Explicit user input or approval
Content from .gitignore file (files already ignored by git)
Always ask the user before adding files to the ignore list
Never suppress errors without user consent - fix them instead
Phase 2: Diagnostic Assessment
Initial Root-Level Scan

Run linter on root-level markdown files:

markdownlint-cli2 "*.md"


Document all issues found, including:

Error codes (e.g., MD029, MD001, MD032)
File names and line numbers
Brief description of each issue
Comprehensive Recursive Scan

Scan all markdown files including subdirectories:

markdownlint-cli2 "**/*.md"


This includes files in directories like:

docs/
guides/
Any other subdirectories containing markdown

Create a complete inventory of all issues across the project.

Phase 3: Issue Analysis
Categorize Errors by Type

Group all identified linting errors by error code:

Track frequency of each error type
Identify which errors are auto-fixable
Flag special attention areas (especially MD029, which often requires understanding indentation issues)

Common error types:

MD001: Heading levels should increment by one level at a time
MD009: Trailing spaces
MD010: Hard tabs
MD012: Multiple consecutive blank lines
MD029: Ordered list item prefix (requires special attention - often caused by improper indentation)
MD032: Lists should be surrounded by blank lines
MD047: Files should end with a single newline character

Document patterns such as:

"Found 15 MD029 errors across 5 files"
"MD032 appears in all documentation files"
"MD029 errors primarily in files with code blocks within lists"
Phase 4: Automatic Fixes
Execute Auto-Fix

Run the auto-fix command to correct all auto-fixable issues:

markdownlint-cli2 "**/*.md" --fix


This command will:

Automatically fix formatting issues where possible
Preserve original content intent
Modify files in place
Monitor for Issues

Watch for:

Errors during the fix process
Files that couldn't be modified (permissions)
Any unexpected side effects

Document what was fixed automatically versus what remains.

Phase 5: Manual Fixes
Handle MD029 Issues

For remaining MD029 (ordered list item prefix) issues:

Load and consult references/MD029-Fix-Guide.md for detailed guidance on:

Understanding the root cause: improper indentation of content between list items
Proper 4-space indentation for code blocks within lists
Indentation requirements for paragraphs, blockquotes, and nested content
Common mistakes and how to avoid them
Real-world examples showing before/after fixes
Alternative solutions and when to use them

Key insight: MD029 errors often occur when code blocks, paragraphs, or other content between list items lack proper indentation (typically 4 spaces), causing markdown parsers to break list continuity.

Apply Manual Corrections

For issues not auto-fixed:

Open affected files
Apply fixes according to error type
Maintain consistency with existing markdown style
Verify fixes don't break content
Phase 6: Verification & Reporting
Re-run Linter

Confirm all issues are resolved:

markdownlint-cli2 "**/*.md"


If no errors appear, linting is complete. If errors remain, document them for additional manual fixes.

Generate Summary Report

Provide a comprehensive summary including:

Files Processed

Total count
List of files modified
Any files skipped or with errors

Issues Fixed by Type

Count of each error type fixed
Auto-fixed vs. manually fixed
Special notes on MD029 fixes

Remaining Issues (if any)

Error codes still present
Files requiring manual attention
Recommended next steps

Completion Status

Confirmation of successful completion, or
Clear explanation of remaining work needed
Any error details with suggested solutions
Quick Reference Checklist
 Verify markdownlint availability: markdownlint-cli2 --version
 Create or validate markdownlint config (.markdownlint-cli2.jsonc preferred)
 Run diagnostics: markdownlint-cli2 "**/*.md"
 Apply auto-fixes: markdownlint-cli2 "**/*.md" --fix
 Resolve remaining issues manually using references/MD029-Fix-Guide.md and references/MD036-Guide.md as needed
 Re-run verification: markdownlint-cli2 "**/*.md"
 Summarize files changed, issue types fixed, and any remaining blockers
Key Principles
Preserve content intent: fix formatting without changing meaning.
Respect project configuration: do not override existing lint rules unless explicitly requested.
Do not suppress or hide errors without user consent; fix issues rather than masking them.
Apply progressive fixing: auto-fix first, then manual fixes for remaining issues.
Report clearly: what was found, what was fixed, and what still needs action.
Common Scenarios
User Request Pattern	Workflow Emphasis	References
"Set up markdown linting for my documentation"	Phase 1 -> Phase 2 -> Phase 4 -> Phase 6	N/A
"Fix all markdown linting errors in my project"	Phase 2 -> Phase 3 -> Phase 4 -> Phase 5 -> Phase 6	Load MD029/MD036 guides only if related errors remain
"Fix MD029" / "ordered list issues"	Phase 2 (target MD029) -> Phase 4 -> Phase 5 -> Phase 6	references/MD029-Fix-Guide.md
Resources
references/
MD029-Fix-Guide.md

Comprehensive guide for handling MD029 (ordered list item prefix) errors, focusing on the root cause: improper indentation. This reference provides:

Explanation of why MD029 errors occur (content breaking list continuity)
Proper indentation rules: 4 spaces for code blocks, paragraphs, and other content
Indentation table showing requirements for different content types
Common mistakes with clear ❌ wrong vs ✅ correct examples
Real-world before/after examples
Alternative solutions and when to use markdownlint-disable comments
Best practices for maintaining list continuity
Verification steps

Load this file when MD029 errors persist after auto-fix, or when user needs guidance on fixing ordered list issues. The guide is particularly valuable when lists contain code blocks or mixed content.

MD036-Guide.md

Comprehensive style guide for avoiding MD036 (no emphasis as heading) errors. This reference provides:

Clear explanation of the MD036 rule and why it matters
Wrong vs. correct examples showing bold text vs. proper heading syntax
Heading level hierarchy guidelines (h1 through h6)
Common violations to avoid when creating markdown files
Best practices for using headings vs. bold text
Quick checklist for markdown file creation and modification

Load this file when creating new markdown documentation or when encountering MD036 errors. Use as a reference to maintain consistent heading structure and avoid using bold text as heading substitutes.

Weekly Installs
9
Repository
s2005/markdown-…er-skill
GitHub Stars
8
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass