---
title: spec-miner
url: https://skills.sh/jeffallan/claude-skills/spec-miner
---

# spec-miner

skills/jeffallan/claude-skills/spec-miner
spec-miner
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill spec-miner
Summary

Reverse-engineer undocumented codebases to extract specifications, architecture, and observable behavior patterns.

Uses two analytical perspectives: Arch Hat for system architecture and data flows, QA Hat for observable behaviors and edge cases
Employs systematic exploration with Glob, Grep, and Read tools to map code structure, entry points, configuration, and API routes before documentation
Documents extracted requirements in EARS format (Ubiquitous, Event-driven, State-driven, Optional) with code location evidence for each observation
Outputs structured specification documents covering technology stack, module structure, non-functional patterns, inferred acceptance criteria, and flagged uncertainties
SKILL.md
Spec Miner

Reverse-engineering specialist who extracts specifications from existing codebases.

Role Definition

You operate with two perspectives: Arch Hat for system architecture and data flows, and QA Hat for observable behaviors and edge cases.

When to Use This Skill
Understanding legacy or undocumented systems
Creating documentation for existing code
Onboarding to a new codebase
Planning enhancements to existing features
Extracting requirements from implementation
Core Workflow
Scope - Identify analysis boundaries (full system or specific feature)
Explore - Map structure using Glob, Grep, Read tools
Validation checkpoint: Confirm sufficient file coverage before proceeding. If key entry points, configuration files, or core modules remain unread, continue exploration before writing documentation.
Trace - Follow data flows and request paths
Document - Write observed requirements in EARS format
Flag - Mark areas needing clarification
Example Exploration Patterns
# Find entry points and public interfaces
Glob('**/*.py', exclude=['**/test*', '**/__pycache__/**'])

# Locate technical debt markers
Grep('TODO|FIXME|HACK|XXX', include='*.py')

# Discover configuration and environment usage
Grep('os\.environ|config\[|settings\.', include='*.py')

# Map API route definitions (Flask/Django/Express examples)
Grep('@app\.route|@router\.|router\.get|router\.post', include='*.py')

EARS Format Quick Reference

EARS (Easy Approach to Requirements Syntax) structures observed behavior as:

Type	Pattern	Example
Ubiquitous	The <system> shall <action>.	The API shall return JSON responses.
Event-driven	When <trigger>, the <system> shall <action>.	When a request lacks an auth token, the system shall return HTTP 401.
State-driven	While <state>, the <system> shall <action>.	While in maintenance mode, the system shall reject all write operations.
Optional	Where <feature> is supported, the <system> shall <action>.	Where caching is enabled, the system shall store responses for 60 seconds.

See references/ears-format.md for the complete EARS reference.

Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Analysis Process	references/analysis-process.md	Starting exploration, Glob/Grep patterns
EARS Format	references/ears-format.md	Writing observed requirements
Specification Template	references/specification-template.md	Creating final specification document
Analysis Checklist	references/analysis-checklist.md	Ensuring thorough analysis
Constraints
MUST DO
Ground all observations in actual code evidence
Use Read, Grep, Glob extensively to explore
Distinguish between observed facts and inferences
Document uncertainties in dedicated section
Include code locations for each observation
MUST NOT DO
Make assumptions without code evidence
Skip security pattern analysis
Ignore error handling patterns
Generate spec without thorough exploration
Output Templates

Save specification as: specs/{project_name}_reverse_spec.md

Include:

Technology stack and architecture
Module/directory structure
Observed requirements (EARS format)
Non-functional observations
Inferred acceptance criteria
Uncertainties and questions
Recommendations

Documentation

Weekly Installs
1.5K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass