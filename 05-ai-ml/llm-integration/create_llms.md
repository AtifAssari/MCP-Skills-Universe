---
rating: ⭐⭐⭐
title: create-llms
url: https://skills.sh/github/awesome-copilot/create-llms
---

# create-llms

skills/github/awesome-copilot/create-llms
create-llms
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill create-llms
Summary

Generates a specification-compliant llms.txt file that guides LLMs through repository structure and documentation.

Analyzes repository layout, identifies key files (READMEs, specs, examples, configuration), and catalogs documentation structure before generation
Creates llms.txt following the official specification at https://llmstxt.org/ with H1 project name, blockquote summary, and organized H2 file sections
Organizes files into logical categories (Documentation, Specifications, Examples, Configuration, Optional) with descriptive relative links and brief explanations
Validates output for format compliance, valid links, and effective LLM navigation before placement in repository root
SKILL.md
Create LLMs.txt File from Repository Structure

Create a new llms.txt file from scratch in the root of the repository following the official llms.txt specification at https://llmstxt.org/. This file provides high-level guidance to large language models (LLMs) on where to find relevant content for understanding the repository's purpose and specifications.

Primary Directive

Create a comprehensive llms.txt file that serves as an entry point for LLMs to understand and navigate the repository effectively. The file must comply with the llms.txt specification and be optimized for LLM consumption while remaining human-readable.

Analysis and Planning Phase

Before creating the llms.txt file, you must complete a thorough analysis:

Step 1: Review llms.txt Specification
Review the official specification at https://llmstxt.org/ to ensure full compliance
Understand the required format structure and guidelines
Note the specific markdown structure requirements
Step 2: Repository Structure Analysis
Examine the complete repository structure using appropriate tools
Identify the primary purpose and scope of the repository
Catalog all important directories and their purposes
List key files that would be valuable for LLM understanding
Step 3: Content Discovery
Identify README files and their locations
Find documentation files (.md files in /docs/, /spec/, etc.)
Locate specification files and their purposes
Discover configuration files and their relevance
Find example files and code samples
Identify any existing documentation structure
Step 4: Create Implementation Plan

Based on your analysis, create a structured plan that includes:

Repository purpose and scope summary
Priority-ordered list of essential files for LLM understanding
Secondary files that provide additional context
Organizational structure for the llms.txt file
Implementation Requirements
Format Compliance

The llms.txt file must follow this exact structure per the specification:

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
Step 1: Repository Analysis
Examine the repository structure completely
Read the main README.md to understand the project
Identify all documentation directories and files
Catalog specification files and their purposes
Find example files and configuration files
Step 2: Content Planning
Determine the primary purpose statement
Write a concise summary for the blockquote
Group identified files into logical categories
Prioritize files by importance for LLM understanding
Create descriptions for each file link
Step 3: File Creation
Create the llms.txt file in the repository root
Follow the exact format specification
Include all required sections
Use proper markdown formatting
Ensure all links are valid relative paths
Step 4: Validation
Verify compliance with https://llmstxt.org/ specification
Check that all links are valid and accessible
Ensure the file serves as an effective LLM navigation tool
Confirm the file is both human and machine readable
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
Example Structure Template
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

The created llms.txt file should:

Enable LLMs to quickly understand the repository's purpose
Provide clear navigation to essential documentation
Follow the official llms.txt specification exactly
Be comprehensive yet concise
Serve both human and machine readers effectively
Include all critical files for project understanding
Use clear, unambiguous language throughout
Organize content logically for easy consumption
Weekly Installs
8.6K
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