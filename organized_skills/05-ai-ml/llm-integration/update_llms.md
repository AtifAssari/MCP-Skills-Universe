---
rating: ⭐⭐⭐
title: update-llms
url: https://skills.sh/github/awesome-copilot/update-llms
---

# update-llms

skills/github/awesome-copilot/update-llms
update-llms
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill update-llms
Summary

Maintain accurate llms.txt files that guide LLMs through repository documentation and structure.

Analyzes current repository state against the official llms.txt specification to identify outdated, missing, or incorrect file references
Organizes essential documentation into logical H2 sections (Documentation, Specifications, Examples, Configuration, Optional) with properly formatted markdown links
Validates compliance with https://llmstxt.org/ format requirements including H1 header, blockquote summary, and relative path links
Removes outdated references, adds new documentation files, and reorganizes sections to improve LLM navigation while maintaining human readability
SKILL.md
Update LLMs.txt File

Update the existing llms.txt file in the root of the repository to reflect changes in documentation, specifications, or repository structure. This file provides high-level guidance to large language models (LLMs) on where to find relevant content for understanding the repository's purpose and specifications.

Primary Directive

Update the existing llms.txt file to maintain accuracy and compliance with the llms.txt specification while reflecting current repository structure and content. The file must remain optimized for LLM consumption while staying human-readable.

Analysis and Planning Phase

Before updating the llms.txt file, you must complete a thorough analysis:

Step 1: Review Current File and Specification
Read the existing llms.txt file to understand current structure
Review the official specification at https://llmstxt.org/ to ensure continued compliance
Identify areas that may need updates based on repository changes
Step 2: Repository Structure Analysis
Examine the current repository structure using appropriate tools
Compare current structure with what's documented in existing llms.txt
Identify new directories, files, or documentation that should be included
Note any removed or relocated files that need to be updated
Step 3: Content Discovery and Change Detection
Identify new README files and their locations
Find new documentation files (.md files in /docs/, /spec/, etc.)
Locate new specification files and their purposes
Discover new configuration files and their relevance
Find new example files and code samples
Identify any changes to existing documentation structure
Step 4: Create Update Plan

Based on your analysis, create a structured plan that includes:

Changes needed to maintain accuracy
New files to be added to the llms.txt
Outdated references to be removed or updated
Organizational improvements to maintain clarity
Implementation Requirements
Format Compliance

The updated llms.txt file must maintain this exact structure per the specification:

H1 Header: Single line with repository/project name (required)
Blockquote Summary: Brief description in blockquote format (optional but recommended)
Additional Details: Zero or more markdown sections without headings for context
File List Sections: Zero or more H2 sections containing markdown lists of links
Content Requirements
Required Elements
Project Name: Clear, descriptive title as H1
Summary: Concise blockquote explaining the repository's purpose
Key Files: Essential files organized by category (H2 sections)
File Link Format

Each file link must follow: [descriptive-name](relative-url): optional description

Section Organization

Organize files into logical H2 sections such as:

Documentation: Core documentation files
Specifications: Technical specifications and requirements
Examples: Sample code and usage examples
Configuration: Setup and configuration files
Optional: Secondary files (special meaning - can be skipped for shorter context)
Content Guidelines
Language and Style
Use concise, clear, unambiguous language
Avoid jargon without explanation
Write for both human and LLM readers
Be specific and informative in descriptions
File Selection Criteria

Include files that:

Explain the repository's purpose and scope
Provide essential technical documentation
Show usage examples and patterns
Define interfaces and specifications
Contain configuration and setup instructions

Exclude files that:

Are purely implementation details
Contain redundant information
Are build artifacts or generated content
Are not relevant to understanding the project
Execution Steps
Step 1: Current State Analysis
Read the existing llms.txt file thoroughly
Examine the current repository structure completely
Compare existing file references with actual repository content
Identify outdated, missing, or incorrect references
Note any structural issues with the current file
Step 2: Content Planning
Determine if the primary purpose statement needs updates
Review and update the summary blockquote if needed
Plan additions for new files and directories
Plan removals for outdated or moved content
Reorganize sections if needed for better clarity
Step 3: File Updates
Update the existing llms.txt file in the repository root
Maintain compliance with the exact format specification
Add new file references with appropriate descriptions
Remove or update outdated references
Ensure all links are valid relative paths
Step 4: Validation
Verify continued compliance with https://llmstxt.org/ specification
Check that all links are valid and accessible
Ensure the file still serves as an effective LLM navigation tool
Confirm the file remains both human and machine readable
Quality Assurance
Format Validation
✅ H1 header with project name
✅ Blockquote summary (if included)
✅ H2 sections for file lists
✅ Proper markdown link format
✅ No broken or invalid links
✅ Consistent formatting throughout
Content Validation
✅ Clear, unambiguous language
✅ Comprehensive coverage of essential files
✅ Logical organization of content
✅ Appropriate file descriptions
✅ Serves as effective LLM navigation tool
Specification Compliance
✅ Follows https://llmstxt.org/ format exactly
✅ Uses required markdown structure
✅ Implements optional sections appropriately
✅ File located at repository root (/llms.txt)
Update Strategy
Addition Process

When adding new content:

Identify the appropriate section for new files
Create clear, descriptive names for links
Write concise but informative descriptions
Maintain alphabetical or logical ordering within sections
Consider if new sections are needed for new content types
Removal Process

When removing outdated content:

Verify files are actually removed or relocated
Check if relocated files should be updated rather than removed
Remove entire sections if they become empty
Update cross-references if needed
Reorganization Process

When restructuring content:

Maintain logical flow from general to specific
Keep essential documentation in primary sections
Move secondary content to "Optional" section if appropriate
Ensure new organization improves LLM navigation

Example structure for llms.txt:

# [Repository Name]

> [Concise description of the repository's purpose and scope]

[Optional additional context paragraphs without headings]

## Documentation

- [Main README](README.md): Primary project documentation and getting started guide
- [Contributing Guide](CONTRIBUTING.md): Guidelines for contributing to the project
- [Code of Conduct](CODE_OF_CONDUCT.md): Community guidelines and expectations

## Specifications

- [Technical Specification](spec/technical-spec.md): Detailed technical requirements and constraints
- [API Specification](spec/api-spec.md): Interface definitions and data contracts

## Examples

- [Basic Example](examples/basic-usage.md): Simple usage demonstration
- [Advanced Example](examples/advanced-usage.md): Complex implementation patterns

## Configuration

- [Setup Guide](docs/setup.md): Installation and configuration instructions
- [Deployment Guide](docs/deployment.md): Production deployment guidelines

## Optional

- [Architecture Documentation](docs/architecture.md): Detailed system architecture
- [Design Decisions](docs/decisions.md): Historical design decision records

Success Criteria

The updated llms.txt file should:

Accurately reflect the current repository structure and content
Maintain compliance with the llms.txt specification
Provide clear navigation to essential documentation
Remove outdated or incorrect references
Include new important files and documentation
Maintain logical organization for easy LLM consumption
Use clear, unambiguous language throughout
Continue to serve both human and machine readers effectively
Weekly Installs
8.4K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn