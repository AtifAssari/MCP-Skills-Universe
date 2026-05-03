---
title: gemini
url: https://skills.sh/peterfile/devpilot-agents/gemini
---

# gemini

skills/peterfile/devpilot-agents/gemini
gemini
Installation
$ npx skills add https://github.com/peterfile/devpilot-agents --skill gemini
SKILL.md
Gemini CLI Integration
Overview

Execute Gemini CLI commands with support for multiple models and flexible prompt input. Integrates Google's Gemini AI models into Claude Code workflows.

When to Use
Complex reasoning tasks requiring advanced AI capabilities
Code generation and analysis with Gemini models
Tasks requiring Google's latest AI technology
Alternative perspective on code problems
Usage

Mandatory: Run via uv with fixed timeout 7200000ms (foreground):

uv run ~/.claude/skills/gemini/scripts/gemini.py "<prompt>" [working_dir]


Optional (direct execution or using Python):

~/.claude/skills/gemini/scripts/gemini.py "<prompt>" [working_dir]
# or
python3 ~/.claude/skills/gemini/scripts/gemini.py "<prompt>" [working_dir]

Environment Variables
GEMINI_MODEL: Configure model (default: gemini-3-pro-preview)
Example: export GEMINI_MODEL=gemini-3
Timeout Control
Fixed: 7200000 milliseconds (2 hours), immutable
Bash tool: Always set timeout: 7200000 for double protection
Parameters
prompt (required): Task prompt or question
working_dir (optional): Working directory (default: current directory)
Return Format

Plain text output from Gemini:

Model response text here...


Error format (stderr):

ERROR: Error message

Invocation Pattern

When calling via Bash tool, always include the timeout parameter:

Bash tool parameters:
- command: uv run ~/.claude/skills/gemini/scripts/gemini.py "<prompt>"
- timeout: 7200000
- description: <brief description of the task>


Alternatives:

# Direct execution (simplest)
- command: ~/.claude/skills/gemini/scripts/gemini.py "<prompt>"

# Using python3
- command: python3 ~/.claude/skills/gemini/scripts/gemini.py "<prompt>"

Examples

Basic query:

uv run ~/.claude/skills/gemini/scripts/gemini.py "explain quantum computing"
# timeout: 7200000


Code analysis:

uv run ~/.claude/skills/gemini/scripts/gemini.py "review this code for security issues: $(cat app.py)"
# timeout: 7200000


With specific working directory:

uv run ~/.claude/skills/gemini/scripts/gemini.py "analyze project structure" "/path/to/project"
# timeout: 7200000


Using python3 directly (alternative):

python3 ~/.claude/skills/gemini/scripts/gemini.py "your prompt here"

Notes
Recommended: Use uv run for automatic Python environment management (requires uv installed)
Alternative: Direct execution ./gemini.py (uses system Python via shebang)
Python implementation using standard library (zero dependencies)
Cross-platform compatible (Windows/macOS/Linux)
PEP 723 compliant (inline script metadata)
Requires Gemini CLI installed and authenticated
Supports all Gemini model variants (configure via GEMINI_MODEL environment variable)
Output is streamed directly from Gemini CLI
Weekly Installs
19
Repository
peterfile/devpi…t-agents
GitHub Stars
31
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass