---
rating: ⭐⭐⭐
title: claude-md-architect
url: https://skills.sh/samhvw8/dot-claude/claude-md-architect
---

# claude-md-architect

skills/samhvw8/dot-claude/claude-md-architect
claude-md-architect
Installation
$ npx skills add https://github.com/samhvw8/dot-claude --skill claude-md-architect
SKILL.md
CLAUDE.md Architect Skill

Generate and optimize CLAUDE.md files for software projects by analyzing codebase context and applying Anthropic engineering best practices. Creates concise, maintainable project instructions that maximize Claude Code effectiveness while minimizing token consumption.

Core Principles
Conciseness over Completeness: Treat CLAUDE.md like frequently-used prompts, not exhaustive documentation
Evidence-Based Context: Analyze actual codebase before making recommendations
Incremental Refinement: Start minimal, iterate based on effectiveness
Token Efficiency: Every line should earn its presence in the context window
Human-Readable Structure: Use clear organization with XML tags for parsing
When to Use This Skill

Activate when user requests:

"init CLAUDE.md" or "create project instructions"
"optimize" or "improve" existing CLAUDE.md
"setup Claude for my project"
Project-specific instructions for Claude Code
Starting work on a new project that needs documentation
Existing CLAUDE.md is outdated or ineffective
Quick Decision Tree
User Request
    │
    ├─→ "init" or "create" → Initialize New CLAUDE.md
    │   └─→ Follow: @refs/initialization-workflow.md
    │
    ├─→ "optimize" or "improve" → Optimize Existing CLAUDE.md
    │   └─→ Follow: @refs/optimization-patterns.md
    │
    └─→ "integrate" or "setup MCP/slash commands" → Integration
        └─→ Follow: @refs/integration-strategies.md

Workflow Overview
Initialize New CLAUDE.md

Quick Steps:

Discover - Analyze codebase (language, framework, structure, tests)
Extract - Identify code style, commands, patterns
Generate - Select template, customize for project
Validate - Verify commands, check token count
Present - Show output with explanation

Detailed Instructions: @refs/initialization-workflow.md

Optimize Existing CLAUDE.md

Quick Steps:

Analyze - Evaluate token efficiency, accuracy, relevance
Identify - Find redundancy, outdated info, generic fluff
Refactor - Apply token reduction, restructure, improve clarity
Test - Verify 40%+ token reduction, retain critical info
Present - Show before/after with metrics

Detailed Instructions: @refs/optimization-patterns.md

Token Reduction Quick Reference
Before (Verbose)
When you are implementing new features in this codebase, it's very important that you always make sure to write comprehensive tests for all the functionality you add. We use Jest as our testing framework, and we expect all new code to have at least 80% code coverage.

After (Concise)
### Testing Requirements
- New features require tests (Jest, >80% coverage)
- Unit tests: Individual functions in `src/lib/`
- Integration tests: API endpoints with Supertest


Result: 70% token reduction, same information

Template Selection Guide
Project Type	Key Indicators	Template Focus
Web App	React/Vue/Angular, frontend build	UI components, responsive design, routing
Backend API	Express/FastAPI, database, auth	RESTful conventions, validation, security
CLI Tool	Commander/Click, stdio	Commands, user experience, file operations
Library	Package exports, no app logic	API design, versioning, backward compatibility
Monorepo	Workspaces, multiple packages	Cross-package changes, workspace commands
Quality Checklist

Before presenting CLAUDE.md:

✓ File is <400 lines (prefer <250)
✓ Commands verified against package.json/Makefile
✓ Patterns match actual codebase conventions
✓ No redundant info already in README
✓ Context loading is selective, not exhaustive
✓ Structure uses clear sections with headers
✓ Examples are concrete, not generic
✓ Security/testing requirements reflect actual needs
Token Budget Guidelines
Project Complexity	Target Token Count
Simple (single-purpose tool)	100-200 tokens
Medium (standard web app)	200-400 tokens
Complex (multi-service platform)	400-800 tokens
Maximum (exception only)	1000 tokens

If approaching max, split into:

.claude/CLAUDE.md (essentials)
.claude/ARCHITECTURE.md (reference, not auto-loaded)
.claude/commands/*.md (workflows as slash commands)
Content Priority
Keep (High Value)
Project-specific commands and scripts
Code style conventions unique to this project
File organization patterns
Testing requirements and strategies
Security constraints
Performance considerations
Remove (Low Value)
Generic software engineering advice
Information already in README
Obvious best practices (DRY, SOLID, etc.)
Detailed framework explanations (use context7)
Step-by-step tutorials (link to docs)
Context Loading Strategy
Use @-syntax ONLY for:
Small, universally relevant files (<100 lines)
Configuration affecting all changes (tsconfig, .eslintrc)
Core type definitions used everywhere
Use On-Demand Loading:
When working on authentication:
  @src/lib/auth.ts
  @src/middleware/authenticate.ts

Avoid:
Loading entire directories with @src/**
Adding large files that aren't always needed
Injecting documentation that duplicates official sources
Integration with Global CLAUDE.md

User has ~/.claude/CLAUDE.md (global):

Universal principles (SOLID, DRY, YAGNI)
MCP tool documentation
Preferred communication style

Project CLAUDE.md should:

Focus exclusively on project-specific guidance
Avoid duplicating MCP tool usage (already global)
Add project-specific MCP tool applications only

Example header:

# MyProject - Development Guide

> Note: General software engineering principles are in your global CLAUDE.md.
> This guide focuses on project-specific patterns and requirements.

MCP Tool Configuration
Detect opportunities:
React/Vue/Angular imports → Suggest context7 for official docs
UI component requests → Suggest magic MCP for patterns
E2E test files → Suggest Playwright MCP for browser automation
Add to CLAUDE.md:
## MCP Tools Configuration

### context7 (Official Documentation)
Use for React hooks, Next.js routing, Prisma schema

### magic (UI Component Generation)
Use for new components, accessibility improvements

### Playwright (E2E Testing)
Use for user flows, visual regression, accessibility audits


Detailed Integration Guide: @refs/integration-strategies.md

Output Format
When Generating New CLAUDE.md
Display generated content in code block
Explain customizations based on analysis
Highlight key decisions
Suggest optional additions
Provide save location and next steps
When Optimizing Existing CLAUDE.md
Summarize issues found
Show before/after comparison for key sections
Present optimized full version
Quantify improvements (token savings %)
Suggest iteration approach

Detailed Templates: @refs/output-templates.md

Common Mistakes to Avoid
Problem	Solution
Over-Documentation	Document project-specific decisions only
Stale Information	Verify against current package.json, files
Redundant Context	Link to README, add only unique patterns
Token Waste	On-demand context by functional area
Generic Fluff	Specific patterns: "Use Zod validation, Prisma transactions"
Success Metrics
Effective CLAUDE.md
Claude requires fewer clarifying questions
Code matches project conventions on first try
Commands work without errors
User rarely provides missing context manually
Ineffective CLAUDE.md
Claude frequently asks "what framework?"
Generated code doesn't match existing style
User repeatedly provides same context files
CLAUDE.md contains info never referenced
Philosophy

Remember:

CLAUDE.md is a living document, not permanent documentation
Start minimal, add based on actual friction points
Remove guidance that doesn't improve Claude's output
Measure effectiveness: fewer questions = better CLAUDE.md

When in doubt:

Prefer concise over comprehensive
Prefer specific over generic
Prefer examples over explanations
Prefer on-demand over auto-loading
Reference Files
@refs/initialization-workflow.md - Complete guide for creating new CLAUDE.md files from scratch
@refs/optimization-patterns.md - Techniques for reducing tokens and improving effectiveness
@refs/integration-strategies.md - Integration with global config, MCP tools, slash commands
@refs/output-templates.md - Standard formats for presenting results to users

Quick Start: When user requests CLAUDE.md creation/optimization, follow the decision tree above and consult relevant reference files for detailed instructions.

Weekly Installs
109
Repository
samhvw8/dot-claude
GitHub Stars
10
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass