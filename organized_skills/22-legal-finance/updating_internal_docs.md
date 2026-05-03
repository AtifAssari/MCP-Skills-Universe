---
rating: ⭐⭐⭐
title: updating-internal-docs
url: https://skills.sh/streamlit/streamlit/updating-internal-docs
---

# updating-internal-docs

skills/streamlit/streamlit/updating-internal-docs
updating-internal-docs
Installation
$ npx skills add https://github.com/streamlit/streamlit --skill updating-internal-docs
SKILL.md
Updating Internal Documentation

Review internal documentation files against the actual codebase state and propose fixes for outdated, incorrect, or missing information.

When to use
After significant codebase changes (new features, refactors, tooling updates)
When documentation drift is suspected
After updating make targets, folder structure, dependencies, skills, or workflows
Key files to check

Priority files (most likely to contain codebase-specific instructions):

**/AGENTS.md - AI agent instructions
**/README.md - Package/directory documentation
.claude/skills/*/SKILL.md - Skill definitions
.claude/agents/*.md - Subagent definitions
wiki/**/*.md - Developer wiki
CONTRIBUTING.md - Contributor guide

Files to skip (synced copies, updated separately):

.github/copilot-instructions.md
.github/instructions/*.md
.cursor/rules/*.mdc
Verification checklist
 Make commands exist and work (make help)
 File and folder paths exist
 Tool/dependency references are valid
 Tool version numbers match config files (see below)
 Testing instructions are correct
 Code examples match actual patterns
 Links resolve (internal and external)
 Skill/agent cross-references use current names
 .github/workflows/AGENTS.md reflects actual workflow files
 CONTRIBUTING.md skill/agent overview matches .claude/skills/*/ and .claude/agents/
Quick verification commands
# Check path exists: test -e path && echo ok || echo missing
# Check URL reachable: curl -sI -o /dev/null -w "%{http_code}" <url>

Tool version sources
Tool	Config file
TypeScript, React, Vite, Vitest, ESLint, oxfmt, Emotion	frontend/package.json
Yarn	frontend/package.json (packageManager field)
Python, Ruff, mypy, pytest	pyproject.toml
Node.js	.nvmrc
Issue types
Type	Description
OUTDATED	Info no longer accurate (old make targets, renamed files)
INCORRECT	Factually wrong (wrong paths, invalid commands)
VERSION_MISMATCH	Documented version differs from actual
MISSING	Important info not documented
BROKEN_LINK	Links to non-existent resources
INCONSISTENT	Conflicts with other docs
Workflow
Enumerate: Find all markdown documentation files
Verify: Cross-reference documented commands, paths, and examples against the codebase
Report: Present findings grouped by priority
Fix: Apply changes after user approval
Presenting findings

List all issues and let the user choose which to fix:

Documentation Review: {SCOPE}
═══════════════════════════════════════════════════════════════

Found {N} issues across {M} files:

1. [OUTDATED] AGENTS.md:42
   Current:  `make python-check`
   Actual:   Command renamed to `make python-lint`

2. [INCORRECT] wiki/testing.md:15
   Current:  Tests in `lib/tests/unit/`
   Actual:   Path is `lib/tests/streamlit/`

3. [BROKEN_LINK] CONTRIBUTING.md:88
   Current:  Link to `./docs/setup.md`
   Actual:   File does not exist

Which issues should I fix?
Recommended: "all"
Options: "1" | "1,2,3" | "all" | "skip 3"

Rules
Verify before proposing: Always check the codebase before suggesting a fix
Minimal changes: Only change what's actually wrong
Test commands: Run commands before documenting them
Keep style consistent: Match existing documentation style
After completing review
Present all findings to user
Get approval before making changes
Apply fixes incrementally
Run /checking-changes to validate

Example summary:

Fixed 3 of 4 issues:

- #1 [OUTDATED]: Updated make command in AGENTS.md
- #2 [INCORRECT]: Fixed test path in wiki/testing.md
- #3 [BROKEN_LINK]: Removed dead link in CONTRIBUTING.md
- #4 [INCONSISTENT]: Skipped - requires manual verification

Files modified:
  AGENTS.md         |  2 +-
  wiki/testing.md   |  4 ++--
  CONTRIBUTING.md   |  1 -

Weekly Installs
37
Repository
streamlit/streamlit
GitHub Stars
44.4K
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass