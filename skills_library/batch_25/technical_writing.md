---
title: technical-writing
url: https://skills.sh/dauquangthanh/hanoi-rainbow/technical-writing
---

# technical-writing

skills/dauquangthanh/hanoi-rainbow/technical-writing
technical-writing
Installation
$ npx skills add https://github.com/dauquangthanh/hanoi-rainbow --skill technical-writing
SKILL.md
Technical Writing

Creates professional technical documentation with clear structure, appropriate detail level, and user-focused content.

Workflow
1. Identify Documentation Type

Determine which type of documentation is needed:

API Documentation - REST, GraphQL, webhooks, authentication
User Guides - Features, how-tos, troubleshooting
Tutorials - Learning-focused with hands-on examples
Architecture Documents - System design, technical decisions
README Files - Project overview, quick start
Release Notes - Changes, migrations, breaking changes
Technical Specifications - Requirements, constraints

For detailed templates and patterns: Load documentation-types-and-workflows.md

2. Gather Context

Collect essential information before writing:

Audience - Developers, end-users, managers, administrators
Technical depth - Beginner, intermediate, advanced
Scope - Codebase/APIs/systems to document
Standards - Style guides or organizational requirements
Related docs - Existing documentation to reference or integrate with
3. Structure Content

Apply clear organization principles:

Lead with overview/introduction
Use descriptive heading hierarchy (H1 → H2 → H3)
Include table of contents for documents with >3 sections
Group related information logically
Place examples immediately after concepts
Add diagrams/visuals for complex workflows
4. Write Clear Content

Follow core writing principles:

Active voice - "The API returns..." not "The response is returned..."
Specificity - "Response time < 200ms" not "Fast response"
Define acronyms - "API (Application Programming Interface)" on first use
Consistent terminology - Same terms throughout document
Imperative instructions - "Run the command" not "You should run..."
Show examples - Provide code/output for every concept

For comprehensive style guidance: Load writing-guidelines.md

5. Add Code Examples

Code example requirements:

Specify language in code blocks: python,javascript
Show complete, runnable examples (not fragments)
Include input/output pairs
Add explanatory comments for complex logic
Test all code before publishing
6. Review and Validate

Quality assurance checklist:

✓ Verify technical accuracy
✓ Test all code examples
✓ Check clarity and completeness
✓ Ensure consistent terminology
✓ Validate all links and references
Documentation Templates
README Files

Essential components for project documentation:

# Project Name
Brief description of what the project does

## Features
- Key feature 1
- Key feature 2
- Key feature 3

## Installation
[step-by-step installation commands]

## Quick Start
[minimal working example]

## Configuration
[environment variables or config options]

## License
[license type]

Release Notes

Structure for version releases:

# Version X.X.X - YYYY-MM-DD

## Summary
[High-level overview of this release]

## New Features
- Feature description (#issue-number)
- Feature description (#issue-number)

## Bug Fixes
- Fix description (#issue-number)
- Fix description (#issue-number)

## Breaking Changes
⚠️ **Change that breaks compatibility**
Migration guide: [step-by-step migration instructions]

## Deprecations
- Deprecated feature (will be removed in vX.X)

Quality Standards

Documentation quality checklist before publishing:

 Accuracy - All technical details are correct
 Completeness - All necessary topics covered
 Clarity - Target audience can understand content
 Examples - Working code included and tested
 Structure - Logical organization with clear headings
 Consistency - Terminology and formatting consistent
 Links - All hyperlinks are valid
 Grammar - No spelling or grammatical errors
 Current - Version numbers and dates up-to-date
Common Pitfalls to Avoid
Assuming knowledge - Define all acronyms and technical terms
Vague instructions - Be specific with concrete examples
Missing error scenarios - Document errors and solutions
Outdated examples - Test and update code regularly
Inconsistent terminology - Use identical terms throughout
Missing prerequisites - List all requirements upfront
Poor formatting - Use headings, lists, code blocks properly
No examples - Always include working code samples
Wrong audience level - Match technical depth to readers
Dense text - Break into scannable sections with clear headings
Reference Files
documentation-types-and-workflows.md - Complete templates and patterns for API docs, user guides, tutorials, architecture docs, and technical specifications
writing-guidelines.md - Detailed style rules for clarity, active voice, specificity, consistency, heading hierarchy, code formatting, and lists
Weekly Installs
24
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