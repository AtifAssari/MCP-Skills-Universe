---
title: web-design-guidelines
url: https://skills.sh/supercent-io/skills-template/web-design-guidelines
---

# web-design-guidelines

skills/supercent-io/skills-template/web-design-guidelines
web-design-guidelines
Originally fromvercel-labs/agent-skills
Installation
$ npx skills add https://github.com/supercent-io/skills-template --skill web-design-guidelines
Summary

Automated UI code review against Vercel's Web Interface Guidelines.

Fetches the latest guidelines from the official Vercel repository before each review to ensure current rule compliance
Analyzes React, Vue, Svelte, HTML, CSS, and JavaScript/TypeScript files against all fetched rules
Reports violations in file:line format with actionable feedback on how to fix each issue
Supports file paths and glob patterns for flexible scope selection across projects
SKILL.md
Web Interface Guidelines Review

Review files for compliance with Vercel's Web Interface Guidelines.

When to use this skill
UI code review: check compliance with Web Interface Guidelines
Accessibility check: when asked "check accessibility"
Design audit: when asked "audit design"
UX review: when asked "review UX"
Best practices review: when asked "check my site against best practices"
How It Works
Fetch the latest guidelines from the source URL below
Read the specified files (or prompt user for files/pattern)
Check against all rules in the fetched guidelines
Output findings in the terse file:line format
Guidelines Source

Fetch fresh guidelines before each review:

https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md


Use WebFetch to retrieve the latest rules. The fetched content contains all the rules and output format instructions.

Instructions
Step 1: Fetch Guidelines

Use WebFetch:

WebFetch URL: https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
Prompt: "Extract all UI rules and guidelines"

Step 2: Analyze Files

Read and analyze the files or patterns provided by the user.

Files to analyze:

React/Vue/Svelte components
HTML files
CSS/SCSS files
TypeScript/JavaScript files
Step 3: Apply Rules

Apply all rules from the fetched guidelines to the files and output violations.

Input Format
Required info
File or pattern: file path or glob pattern to review
Input examples
Review my UI code:
- File: src/components/Button.tsx

Check accessibility:
- Pattern: src/**/*.tsx

Output Format

Follow the format specified in the guidelines (typically file:line):

src/components/Button.tsx:15 - Button should have aria-label for icon-only buttons
src/components/Modal.tsx:42 - Modal should trap focus within itself
src/pages/Home.tsx:8 - Main content should be wrapped in <main> element

Usage

When a user provides a file or pattern argument:

Fetch guidelines from the source URL above
Read the specified files
Apply all rules from the fetched guidelines
Output findings using the format specified in the guidelines

If no files specified, ask the user which files to review.

Constraints
Required Rules (MUST)
Use latest guidelines: fetch fresh guidelines from the source URL for every review
Apply all rules: check every rule from the fetched guidelines
Accurate locations: specify violation locations in file:line format
Prohibited (MUST NOT)
Use stale cache: always fetch the latest guidelines
Partial check: do not apply only some rules
Best practices
Limit file scope: be careful about context overflow when reviewing too many files at once
Prioritize: report critical issues first
Suggest fixes: include how to fix along with each violation
References
Vercel Web Interface Guidelines
WCAG 2.1 Guidelines
Metadata
Version
Current version: 1.0.0
Last updated: 2026-01-22
Supported platforms: Claude, ChatGPT, Gemini
Source: vercel/agent-skills
Related Skills
web-accessibility: WCAG accessibility implementation
ui-component-patterns: UI component patterns
Tags

#UI #review #web-interface #guidelines #vercel #design-audit #UX #frontend

Weekly Installs
10.5K
Repository
supercent-io/sk…template
GitHub Stars
88
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn