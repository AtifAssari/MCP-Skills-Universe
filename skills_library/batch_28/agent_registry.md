---
title: agent-registry
url: https://skills.sh/matrixy/agent-registry/agent-registry
---

# agent-registry

skills/matrixy/agent-registry/agent-registry
agent-registry
Installation
$ npx skills add https://github.com/matrixy/agent-registry --skill agent-registry
SKILL.md
Contains Hooks

This skill uses Claude hooks which can execute code automatically in response to events. Review carefully before installing.

Agent Registry

Lazy-loading system for Claude Code agents. Eliminates the "~16k tokens" warning by loading agents on-demand.

CRITICAL RULE

NEVER assume agents are pre-loaded. Always use this registry to discover and load agents.

Workflow
User Request → search_agents(intent) → select best match → get_agent(name) → execute with agent

Available Commands
Command	When to Use	Example
list.js	User asks "what agents do I have" or needs overview	bun bin/list.js
search.js	Find agents matching user intent (ALWAYS do this first)	bun bin/search.js "code review security"
search-paged.js	Paged search for large registries (300+ agents)	bun bin/search-paged.js "query" --page 1 --page-size 10
get.js	Load a specific agent's full instructions	bun bin/get.js code-reviewer
Search First Pattern
Extract intent keywords from user request
Run search: bun bin/search.js "<keywords>"
Review results: Check relevance scores (0.0-1.0)
Load if needed: bun bin/get.js <agent-name>
Execute: Follow the loaded agent's instructions
Example

User: "Can you review my authentication code for security issues?"

# Step 1: Search for relevant agents
bun bin/search.js "code review security authentication"

# Output:
# Found 2 matching agents:
#   1. security-auditor (score: 0.89) - Analyzes code for security vulnerabilities
#   2. code-reviewer (score: 0.71) - General code review and best practices

# Step 2: Load the best match
bun bin/get.js security-auditor

# Step 3: Follow loaded agent instructions for the task

Installation
Step 1: Install the Skill

Quick Install (Recommended):

# Using Skills CLI (recommended)
npx skills add MaTriXy/Agent-Registry@agent-registry

# Discover skills interactively
npx skills find

# Update existing skills
npx skills update


Traditional Install:

# User-level installation
./install.sh

# OR project-level installation
./install.sh --project

# Optional: install enhanced interactive UI dependency
./install.sh --install-deps


What install.sh does:

Copies skill files to ~/.claude/skills/agent-registry/
Creates empty registry structure
Optionally installs dependencies via --install-deps (@clack/prompts for enhanced UI)
Step 2: Migrate Your Agents

Run the interactive migration script:

cd ~/.claude/skills/agent-registry
bun bin/init.js
# Optional destructive mode:
bun bin/init.js --move


Interactive selection modes:

With @clack/prompts (default): Beautiful checkbox UI with category grouping, token indicators, and paging

Arrow keys navigate, Space toggle, Enter confirm
Visual indicators: [green] <1k tokens, [yellow] 1-3k, [red] >3k
Grouped by subdirectory

Fallback: Text-based number input

Enter comma-separated numbers (e.g., 1,3,5)
Type all to migrate everything

What init.js does:

Scans ~/.claude/agents/ and .claude/agents/ for agent files
Displays available agents with metadata
Lets you interactively select which to migrate
Copies selected agents to the registry by default (--move is explicit opt-in)
Builds search index (registry.json)
Dependencies
Bun (ships with Claude Code) — zero additional dependencies for core functionality
@clack/prompts: Optional enhanced interactive selection UI (install via ./install.sh --install-deps)
Registry Location
Global: ~/.claude/skills/agent-registry/
Project: .claude/skills/agent-registry/ (optional override)

Agents not migrated remain in their original locations and load normally (contributing to token overhead).

Weekly Installs
29
Repository
matrixy/agent-registry
GitHub Stars
8
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass