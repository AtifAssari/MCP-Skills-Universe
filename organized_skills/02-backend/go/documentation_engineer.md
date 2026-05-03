---
rating: ⭐⭐⭐
title: documentation-engineer
url: https://skills.sh/charon-fan/agent-playbook/documentation-engineer
---

# documentation-engineer

skills/charon-fan/agent-playbook/documentation-engineer
documentation-engineer
Installation
$ npx skills add https://github.com/charon-fan/agent-playbook --skill documentation-engineer
SKILL.md
Documentation Engineer

Expert in creating clear, comprehensive, and maintainable technical documentation.

When This Skill Activates

Activates when you:

Ask to write documentation
Request README creation
Mention "docs" or "document this"
Need API documentation
Documentation Types
1. README

Every project should have a README with:

# Project Name

Brief description (what it does, why it exists)

## Quick Start

Installation and usage in 3 steps or less.

## Installation

Detailed installation instructions.

## Usage

Examples of common usage patterns.

## Configuration

Environment variables and configuration options.

## Development

How to run tests, build, and develop locally.

## Contributing

Guidelines for contributors.

## License

License information.

2. API Documentation

For each endpoint/function:

Description: What it does
Parameters: Name, type, required/optional, description
Return value: Type and structure
Errors: Possible errors and conditions
Examples: Usage examples
3. Code Comments

Comment why, not what:

// Bad: Sets the count to zero
count = 0;

// Good: Reset count for new measurement cycle
count = 0;

// Bad: Check if user is admin
if (user.role === 'admin') {

// Good: Only admins can bypass approval workflow
if (user.role === 'admin') {

4. Architecture Documentation
System overview
Component relationships
Data flow
Design decisions
Trade-offs considered
Documentation Principles
Be Clear: Use simple, direct language
Be Concise: Respect the reader's time
Be Accurate: Keep docs in sync with code
Be Complete: Cover all public interfaces
Be Current: Update docs when code changes
Writing Guidelines
Headings
Use sentence case for headings
Start with a verb or noun
Be descriptive
Code Examples
Show before/after when appropriate
Include import statements
Show expected output
Handle edge cases
Links
Use relative links for internal docs
Include anchors for sections
Test that links work
Diagrams
Use Mermaid for flowcharts and sequences
Keep diagrams simple
Add a title and legend
Documentation Checklist
README
 Project description
 Quick start guide
 Installation instructions
 Usage examples
 Configuration guide
 Contributing guidelines
Code Docs
 All public functions documented
 Parameters and returns documented
 Examples provided for complex functions
 Edge cases documented
API Docs
 All endpoints documented
 Request/response schemas
 Authentication requirements
 Error responses documented
 Rate limits documented
Scripts

Generate documentation structure:

python scripts/generate_docs.py


Validate documentation:

python scripts/validate_docs.py

References
references/readme-template.md - README template
references/api-template.md - API documentation template
references/style-guide.md - Documentation style guide
Weekly Installs
434
Repository
charon-fan/agen…playbook
GitHub Stars
49
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass