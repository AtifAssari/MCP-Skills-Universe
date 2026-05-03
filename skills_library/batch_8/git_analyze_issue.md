---
title: git:analyze-issue
url: https://skills.sh/neolabhq/context-engineering-kit/git:analyze-issue
---

# git:analyze-issue

skills/neolabhq/context-engineering-kit/git:analyze-issue
git:analyze-issue
Installation
$ npx skills add https://github.com/neolabhq/context-engineering-kit --skill git:analyze-issue
SKILL.md

Please analyze GitHub issue #$ARGUMENTS and create a technical specification.

Follow these steps:

Check if the issue is already loaded:

Look for the issue file in ./specs/issues/ folder
File naming pattern: <number-padded-to-3-digits>-<kebab-case-title>.md
If not found, fetch the issue details from GitHub (see step 2)

Fetch the issue details (if not already loaded):

Read .claude/commands/load-issues.md to understand how to fetch issue details
Save the issue file following the load-issues.md format

Understand the requirements thoroughly

Review related code and project structure

Create a technical specification with the format below

Technical Specification for Issue #$ARGUMENTS
Issue Summary
Title: [Issue title from GitHub]
Description: [Brief description from issue]
Labels: [Labels from issue]
Priority: [High/Medium/Low based on issue content]
Problem Statement

[1-2 paragraphs explaining the problem]

Technical Approach

[Detailed technical approach]

Implementation Plan
[Step 1]
[Step 2]
[Step 3]
Test Plan
Unit Tests:
[test scenario]
Component Tests:
[test scenario]
Integration Tests:
[test scenario]
Files to Modify
Files to Create
Existing Utilities to Leverage
Success Criteria
 [criterion 1]
 [criterion 2]
Out of Scope
[item 1]
[item 2]

Remember to follow our strict TDD principles, KISS approach, and 300-line file limit.

IMPORTANT: After completing your analysis, SAVE the full technical specification to: ./specs/issues/<number-padded-to-3-digits>-<kebab-case-title>.specs.md

For example, for issue #7 with title "Make code review trigger on any *.SQL and .sh file changes", save to: ./specs/issues/007-make-code-review-trigger-on-sql-sh-changes.specs.md

After saving, provide a brief summary to the user confirming:

Issue number and title analyzed
File path where the specification was saved
Key highlights from the specification (2-3 bullet points)
Weekly Installs
419
Repository
neolabhq/contex…ring-kit
GitHub Stars
942
First Seen
Feb 19, 2026