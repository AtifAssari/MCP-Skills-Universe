---
title: filament-docs
url: https://skills.sh/mwguerra/claude-code-plugins/filament-docs
---

# filament-docs

skills/mwguerra/claude-code-plugins/filament-docs
filament-docs
Installation
$ npx skills add https://github.com/mwguerra/claude-code-plugins --skill filament-docs
SKILL.md
FilamentPHP Documentation Reference Skill
Overview

This skill provides access to the complete FilamentPHP v4 official documentation. Use this skill to look up exact implementations, method signatures, and patterns before generating any Filament code.

Documentation Location

All documentation is stored in: /home/mwguerra/projects/mwguerra/claude-code-plugins/filament-specialist/skills/filament-docs/references/

Directory Structure
references/
├── actions/                    # Action buttons and modals
│   └── *.md                    # Action types and configurations
├── forms/                      # Form components
│   └── *.md                    # All form field types
├── general/
│   ├── 01-introduction/        # Getting started, installation
│   ├── 03-resources/           # CRUD resources
│   ├── 06-navigation/          # Menu and navigation
│   ├── 07-users/               # Auth and permissions
│   ├── 08-styling/             # Themes and CSS
│   ├── 09-advanced/            # Advanced patterns
│   ├── 10-testing/             # Testing guide
│   ├── 11-plugins/             # Plugin development
│   └── 12-components/          # UI components
├── infolists/                  # Infolist entries
│   └── *.md                    # Display components
├── notifications/              # Notification system
│   └── *.md                    # Toast and DB notifications
├── schemas/                    # Schema validation
│   └── *.md                    # Schema patterns
├── tables/                     # Table components
│   ├── 02-columns/             # Column types
│   └── 03-filters/             # Filter types
└── widgets/                    # Dashboard widgets
    └── *.md                    # Widget types

Usage
When to Use This Skill
Before generating any Filament component code
When troubleshooting Filament errors
To verify method signatures and parameters
To find correct import statements
To understand Filament v4 patterns
Search Workflow
Identify Topic: Determine what documentation is needed
Navigate to Folder: Go to relevant directory
Read Documentation: Extract exact patterns
Apply Knowledge: Use in code generation
Common Lookups
Topic	Directory
Resource creation	general/03-resources/
Form fields	forms/
Table columns	tables/02-columns/
Table filters	tables/03-filters/
Actions	actions/
Widgets	widgets/
Infolists	infolists/
Testing	general/10-testing/
Styling	general/08-styling/
Navigation	general/06-navigation/
Auth/Permissions	general/07-users/
Plugin Development	general/11-plugins/
Documentation Reading Pattern

When reading documentation:

Find the right file: Match component to documentation file
Read the overview: Understand the component's purpose
Extract code examples: Copy exact patterns
Note imports: Get correct use statements
Check configuration: Review options and parameters
Example Usage
Looking up TextInput field
Navigate to forms/ directory
Find text-input documentation
Extract:
Basic usage pattern
Available methods (required, email, tel, etc.)
Validation integration
Correct import statement
Looking up Table columns
Navigate to tables/02-columns/
Find specific column type
Extract:
Column configuration
Formatting options
Relationship handling
Sorting and searching
Output

After reading documentation, provide:

Exact code pattern from docs
Required imports
Configuration options
Best practices noted
Version-specific considerations
Weekly Installs
18
Repository
mwguerra/claude…-plugins
GitHub Stars
29
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn