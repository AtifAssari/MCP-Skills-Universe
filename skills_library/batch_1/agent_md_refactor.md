---
title: agent-md-refactor
url: https://skills.sh/softaworks/agent-toolkit/agent-md-refactor
---

# agent-md-refactor

skills/softaworks/agent-toolkit/agent-md-refactor
agent-md-refactor
Installation
$ npx skills add https://github.com/softaworks/agent-toolkit --skill agent-md-refactor
Summary

Refactor bloated agent instruction files into organized, linked documentation using progressive disclosure.

Analyzes existing AGENTS.md, CLAUDE.md, or similar files to identify contradictions, extract essentials, and categorize remaining instructions across 3–8 focused topic files
Keeps root file minimal (under 50 lines) with only universal project info and links to detailed guidelines organized by topic (TypeScript, testing, code style, git workflow, architecture)
Flags redundant, vague, or outdated instructions for deletion and provides templates for both root and linked files to ensure consistency
Follows a five-phase process: find contradictions, identify essentials, group remaining content, create file structure, and prune unnecessary instructions
SKILL.md
Agent MD Refactor

Refactor bloated agent instruction files (AGENTS.md, CLAUDE.md, COPILOT.md, etc.) to follow progressive disclosure principles - keeping essentials at root and organizing the rest into linked, categorized files.

Triggers

Use this skill when:

"refactor my AGENTS.md" / "refactor my CLAUDE.md"
"split my agent instructions"
"organize my CLAUDE.md file"
"my AGENTS.md is too long"
"progressive disclosure for my instructions"
"clean up my agent config"
Quick Reference
Phase	Action	Output
1. Analyze	Find contradictions	List of conflicts to resolve
2. Extract	Identify essentials	Core instructions for root file
3. Categorize	Group remaining instructions	Logical categories
4. Structure	Create file hierarchy	Root + linked files
5. Prune	Flag for deletion	Redundant/vague instructions
Process
Phase 1: Find Contradictions

Identify any instructions that conflict with each other.

Look for:

Contradictory style guidelines (e.g., "use semicolons" vs "no semicolons")
Conflicting workflow instructions
Incompatible tool preferences
Mutually exclusive patterns

For each contradiction found:

## Contradiction Found

**Instruction A:** [quote]
**Instruction B:** [quote]

**Question:** Which should take precedence, or should both be conditional?


Ask the user to resolve before proceeding.

Phase 2: Identify the Essentials

Extract ONLY what belongs in the root agent file. The root should be minimal - information that applies to every single task.

Essential content (keep in root):

Category	Example
Project description	One sentence: "A React dashboard for analytics"
Package manager	Only if not npm (e.g., "Uses pnpm")
Non-standard commands	Custom build/test/typecheck commands
Critical overrides	Things that MUST override defaults
Universal rules	Applies to 100% of tasks

NOT essential (move to linked files):

Language-specific conventions
Testing guidelines
Code style details
Framework patterns
Documentation standards
Git workflow details
Phase 3: Group the Rest

Organize remaining instructions into logical categories.

Common categories:

Category	Contents
typescript.md	TS conventions, type patterns, strict mode rules
testing.md	Test frameworks, coverage, mocking patterns
code-style.md	Formatting, naming, comments, structure
git-workflow.md	Commits, branches, PRs, reviews
architecture.md	Patterns, folder structure, dependencies
api-design.md	REST/GraphQL conventions, error handling
security.md	Auth patterns, input validation, secrets
performance.md	Optimization rules, caching, lazy loading

Grouping rules:

Each file should be self-contained for its topic
Aim for 3-8 files (not too granular, not too broad)
Name files clearly: {topic}.md
Include only actionable instructions
Phase 4: Create the File Structure

Output structure:

project-root/
├── CLAUDE.md (or AGENTS.md)     # Minimal root with links
└── .claude/                      # Or docs/agent-instructions/
    ├── typescript.md
    ├── testing.md
    ├── code-style.md
    ├── git-workflow.md
    └── architecture.md


Root file template:

# Project Name

One-sentence description of the project.

## Quick Reference

- **Package Manager:** pnpm
- **Build:** `pnpm build`
- **Test:** `pnpm test`
- **Typecheck:** `pnpm typecheck`

## Detailed Instructions

For specific guidelines, see:
- [TypeScript Conventions](.claude/typescript.md)
- [Testing Guidelines](.claude/testing.md)
- [Code Style](.claude/code-style.md)
- [Git Workflow](.claude/git-workflow.md)
- [Architecture Patterns](.claude/architecture.md)


Each linked file template:

# {Topic} Guidelines

## Overview
Brief context for when these guidelines apply.

## Rules

### Rule Category 1
- Specific, actionable instruction
- Another specific instruction

### Rule Category 2
- Specific, actionable instruction

## Examples

### Good
\`\`\`typescript
// Example of correct pattern
\`\`\`

### Avoid
\`\`\`typescript
// Example of what not to do
\`\`\`

Phase 5: Flag for Deletion

Identify instructions that should be removed entirely.

Delete if:

Criterion	Example	Why Delete
Redundant	"Use TypeScript" (in a .ts project)	Agent already knows
Too vague	"Write clean code"	Not actionable
Overly obvious	"Don't introduce bugs"	Wastes context
Default behavior	"Use descriptive variable names"	Standard practice
Outdated	References deprecated APIs	No longer applies

Output format:

## Flagged for Deletion

| Instruction | Reason |
|-------------|--------|
| "Write clean, maintainable code" | Too vague to be actionable |
| "Use TypeScript" | Redundant - project is already TS |
| "Don't commit secrets" | Agent already knows this |
| "Follow best practices" | Meaningless without specifics |

Execution Checklist
[ ] Phase 1: All contradictions identified and resolved
[ ] Phase 2: Root file contains ONLY essentials
[ ] Phase 3: All remaining instructions categorized
[ ] Phase 4: File structure created with proper links
[ ] Phase 5: Redundant/vague instructions removed
[ ] Verify: Each linked file is self-contained
[ ] Verify: Root file is under 50 lines
[ ] Verify: All links work correctly

Anti-Patterns
Avoid	Why	Instead
Keeping everything in root	Bloated, hard to maintain	Split into linked files
Too many categories	Fragmentation	Consolidate related topics
Vague instructions	Wastes tokens, no value	Be specific or delete
Duplicating defaults	Agent already knows	Only override when needed
Deep nesting	Hard to navigate	Flat structure with links
Examples
Before (Bloated Root)
# CLAUDE.md

This is a React project.

## Code Style
- Use 2 spaces
- Use semicolons
- Prefer const over let
- Use arrow functions
... (200 more lines)

## Testing
- Use Jest
- Coverage > 80%
... (100 more lines)

## TypeScript
- Enable strict mode
... (150 more lines)

After (Progressive Disclosure)
# CLAUDE.md

React dashboard for real-time analytics visualization.

## Commands
- `pnpm dev` - Start development server
- `pnpm test` - Run tests with coverage
- `pnpm build` - Production build

## Guidelines
- [Code Style](.claude/code-style.md)
- [Testing](.claude/testing.md)
- [TypeScript](.claude/typescript.md)

Verification

After refactoring, verify:

Root file is minimal - Under 50 lines, only universal info
Links work - All referenced files exist
No contradictions - Instructions are consistent
Actionable content - Every instruction is specific
Complete coverage - No instructions were lost (unless flagged for deletion)
Self-contained files - Each linked file stands alone
Weekly Installs
3.7K
Repository
softaworks/agent-toolkit
GitHub Stars
1.7K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass