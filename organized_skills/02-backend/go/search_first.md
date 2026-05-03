---
rating: ⭐⭐
title: search-first
url: https://skills.sh/affaan-m/everything-claude-code/search-first
---

# search-first

skills/affaan-m/everything-claude-code/search-first
search-first
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill search-first
Summary

Systematize research-before-coding by searching existing tools, libraries, and patterns before writing custom code.

Provides a five-phase workflow: need analysis, parallel search across npm/PyPI/MCP/GitHub, evaluation, decision (adopt/extend/compose/build), and implementation
Includes a decision matrix to score candidates on functionality, maintenance, community, docs, license, and dependencies
Offers search shortcuts organized by category (development tooling, AI/LLM integration, data APIs, content publishing) and integration points with planner and architect agents
Invokes the researcher agent for non-trivial functionality discovery and structured comparison of candidates
SKILL.md
/search-first — Research Before You Code

Systematizes the "search for existing solutions before implementing" workflow.

Trigger

Use this skill when:

Starting a new feature that likely has existing solutions
Adding a dependency or integration
The user asks "add X functionality" and you're about to write code
Before creating a new utility, helper, or abstraction
Workflow
┌─────────────────────────────────────────────┐
│  1. NEED ANALYSIS                           │
│     Define what functionality is needed      │
│     Identify language/framework constraints  │
├─────────────────────────────────────────────┤
│  2. PARALLEL SEARCH (researcher agent)      │
│     ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│     │  npm /   │ │  MCP /   │ │  GitHub / │  │
│     │  PyPI    │ │  Skills  │ │  Web      │  │
│     └──────────┘ └──────────┘ └──────────┘  │
├─────────────────────────────────────────────┤
│  3. EVALUATE                                │
│     Score candidates (functionality, maint, │
│     community, docs, license, deps)         │
├─────────────────────────────────────────────┤
│  4. DECIDE                                  │
│     ┌─────────┐  ┌──────────┐  ┌─────────┐  │
│     │  Adopt  │  │  Extend  │  │  Build   │  │
│     │ as-is   │  │  /Wrap   │  │  Custom  │  │
│     └─────────┘  └──────────┘  └─────────┘  │
├─────────────────────────────────────────────┤
│  5. IMPLEMENT                               │
│     Install package / Configure MCP /       │
│     Write minimal custom code               │
└─────────────────────────────────────────────┘

Decision Matrix
Signal	Action
Exact match, well-maintained, MIT/Apache	Adopt — install and use directly
Partial match, good foundation	Extend — install + write thin wrapper
Multiple weak matches	Compose — combine 2-3 small packages
Nothing suitable found	Build — write custom, but informed by research
How to Use
Quick Mode (inline)

Before writing a utility or adding functionality, mentally run through:

Does this already exist in the repo? → rg through relevant modules/tests first
Is this a common problem? → Search npm/PyPI
Is there an MCP for this? → Check ~/.claude/settings.json and search
Is there a skill for this? → Check ~/.claude/skills/
Is there a GitHub implementation/template? → Run GitHub code search for maintained OSS before writing net-new code
Full Mode (agent)

For non-trivial functionality, launch the researcher agent:

Task(subagent_type="general-purpose", prompt="
  Research existing tools for: [DESCRIPTION]
  Language/framework: [LANG]
  Constraints: [ANY]

  Search: npm/PyPI, MCP servers, Claude Code skills, GitHub
  Return: Structured comparison with recommendation
")

Search Shortcuts by Category
Development Tooling
Linting → eslint, ruff, textlint, markdownlint
Formatting → prettier, black, gofmt
Testing → jest, pytest, go test
Pre-commit → husky, lint-staged, pre-commit
AI/LLM Integration
Claude SDK → Context7 for latest docs
Prompt management → Check MCP servers
Document processing → unstructured, pdfplumber, mammoth
Data & APIs
HTTP clients → httpx (Python), ky/got (Node)
Validation → zod (TS), pydantic (Python)
Database → Check for MCP servers first
Content & Publishing
Markdown processing → remark, unified, markdown-it
Image optimization → sharp, imagemin
Integration Points
With planner agent

The planner should invoke researcher before Phase 1 (Architecture Review):

Researcher identifies available tools
Planner incorporates them into the implementation plan
Avoids "reinventing the wheel" in the plan
With architect agent

The architect should consult researcher for:

Technology stack decisions
Integration pattern discovery
Existing reference architectures
With iterative-retrieval skill

Combine for progressive discovery:

Cycle 1: Broad search (npm, PyPI, MCP)
Cycle 2: Evaluate top candidates in detail
Cycle 3: Test compatibility with project constraints
Examples
Example 1: "Add dead link checking"
Need: Check markdown files for broken links
Search: npm "markdown dead link checker"
Found: textlint-rule-no-dead-link (score: 9/10)
Action: ADOPT — npm install textlint-rule-no-dead-link
Result: Zero custom code, battle-tested solution

Example 2: "Add HTTP client wrapper"
Need: Resilient HTTP client with retries and timeout handling
Search: npm "http client retry", PyPI "httpx retry"
Found: got (Node) with retry plugin, httpx (Python) with built-in retry
Action: ADOPT — use got/httpx directly with retry config
Result: Zero custom code, production-proven libraries

Example 3: "Add config file linter"
Need: Validate project config files against a schema
Search: npm "config linter schema", "json schema validator cli"
Found: ajv-cli (score: 8/10)
Action: ADOPT + EXTEND — install ajv-cli, write project-specific schema
Result: 1 package + 1 schema file, no custom validation logic

Anti-Patterns
Jumping to code: Writing a utility without checking if one exists
Ignoring MCP: Not checking if an MCP server already provides the capability
Over-customizing: Wrapping a library so heavily it loses its benefits
Dependency bloat: Installing a massive package for one small feature
Weekly Installs
3.1K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn