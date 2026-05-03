---
title: genesis-tools:codebase-analysis
url: https://skills.sh/genesiscz/genesistools/genesis-tools:codebase-analysis
---

# genesis-tools:codebase-analysis

skills/genesiscz/genesistools/genesis-tools:codebase-analysis
genesis-tools:codebase-analysis
Installation
$ npx skills add https://github.com/genesiscz/genesistools --skill genesis-tools:codebase-analysis
SKILL.md
Codebase Analysis

Perform deep codebase exploration and analysis in an isolated sub-agent context. Heavy Grep/Glob operations stay separate from your main work.

Built-in Analysis Types
Type	What it finds
dependencies	Import/require graph, circular dependencies, unused imports
dead-code	Exported but never-imported functions, unreachable code paths
api-surface	Public exports, REST endpoints, RPC methods
type-safety	any types, type assertions, missing return types
error-handling	Uncaught promises, empty catch blocks, missing error boundaries
test-coverage	Files without corresponding test files, untested exports
security	Hardcoded secrets, unsanitized inputs, eval usage
patterns	Custom pattern matching (permissions, money, DTOs, etc.)
Usage
/codebase-analysis --type=<type> [--output=summary|detailed]


Examples:

/codebase-analysis --type=type-safety          # Find all `any` types and unsafe casts
/codebase-analysis --type=dead-code            # Find unused exports
/codebase-analysis --type=error-handling       # Audit error handling patterns
/codebase-analysis --type=patterns             # Custom pattern (prompted interactively)

Tools Available in Fork Context
Tool	Purpose
tools mcp-tsc <file>	TypeScript diagnostics per file via persistent LSP
tools mcp-ripgrep	Code search MCP server for structured queries
tools collect-files-for-ai <dir> -c N	Gather top N relevant files for analysis
tools files-to-prompt <dir> --cxml	Generate structured context XML
How It Works
Launches isolated agent -- intensive searching runs in parallel
Performs extensive Grep/Glob without blocking main session
Analyzes patterns and cross-references findings
Returns structured report to main session
You continue working while analysis runs
Report Format
## [Analysis Type] Report

**Scanned:** N files | **Findings:** N issues | **Severity:** High/Medium/Low

### Finding 1: [description]
- **File:** `src/utils/format.ts:L45`
- **Issue:** [what's wrong]
- **Suggestion:** [how to fix]

### Summary
| Severity | Count |
|----------|-------|
| High | N |
| Medium | N |
| Low | N |

Weekly Installs
16
Repository
genesiscz/genesistools
GitHub Stars
5
First Seen
Feb 24, 2026