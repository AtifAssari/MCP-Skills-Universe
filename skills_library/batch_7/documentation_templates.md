---
title: documentation-templates
url: https://skills.sh/sickn33/antigravity-awesome-skills/documentation-templates
---

# documentation-templates

skills/sickn33/antigravity-awesome-skills/documentation-templates
documentation-templates
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill documentation-templates
Summary

Standardized templates and guidelines for READMEs, API docs, code comments, and AI-friendly documentation.

Includes structured templates for README files, per-endpoint API documentation, JSDoc/TSDoc comments, and changelog formats
Provides Architecture Decision Record (ADR) template for documenting design choices and trade-offs
Covers AI-friendly documentation patterns including llms.txt format and MCP-ready documentation with clear hierarchy, examples, and diagrams
Emphasizes scannable structure, progressive detail levels, and practical guidance on when and what to document
SKILL.md
Documentation Templates

Templates and structure guidelines for common documentation types.

1. README Structure
Essential Sections (Priority Order)
Section	Purpose
Title + One-liner	What is this?
Quick Start	Running in <5 min
Features	What can I do?
Configuration	How to customize
API Reference	Link to detailed docs
Contributing	How to help
License	Legal
README Template
# Project Name

Brief one-line description.

## Quick Start

[Minimum steps to run]

## Features

- Feature 1
- Feature 2

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| PORT | Server port | 3000 |

## Documentation

- API Reference
- Architecture

## License

MIT

2. API Documentation Structure
Per-Endpoint Template
## GET /users/:id

Get a user by ID.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | User ID |

**Response:**
- 200: User object
- 404: User not found

**Example:**
[Request and response example]

3. Code Comment Guidelines
JSDoc/TSDoc Template
/**
 * Brief description of what the function does.
 * 
 * @param paramName - Description of parameter
 * @returns Description of return value
 * @throws ErrorType - When this error occurs
 * 
 * @example
 * const result = functionName(input);
 */

When to Comment
✅ Comment	❌ Don't Comment
Why (business logic)	What (obvious)
Complex algorithms	Every line
Non-obvious behavior	Self-explanatory code
API contracts	Implementation details
4. Changelog Template (Keep a Changelog)
# Changelog

## [Unreleased]
### Added
- New feature

## [1.0.0] - 2025-01-01
### Added
- Initial release
### Changed
- Updated dependency
### Fixed
- Bug fix

5. Architecture Decision Record (ADR)
# ADR-001: [Title]

## Status
Accepted / Deprecated / Superseded

## Context
Why are we making this decision?

## Decision
What did we decide?

## Consequences
What are the trade-offs?

6. AI-Friendly Documentation (2025)
llms.txt Template

For AI crawlers and agents:

# Project Name
> One-line objective.

## Core Files
- [src/index.ts]: Main entry
- [src/api/]: API routes
- [docs/]: Documentation

## Key Concepts
- Concept 1: Brief explanation
- Concept 2: Brief explanation

MCP-Ready Documentation

For RAG indexing:

Clear H1-H3 hierarchy
JSON/YAML examples for data structures
Mermaid diagrams for flows
Self-contained sections
7. Structure Principles
Principle	Why
Scannable	Headers, lists, tables
Examples first	Show, don't just tell
Progressive detail	Simple → Complex
Up to date	Outdated = misleading

Remember: Templates are starting points. Adapt to your project's needs.

When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
1.0K
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass