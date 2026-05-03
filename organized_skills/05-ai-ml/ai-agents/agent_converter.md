---
rating: ⭐⭐⭐
title: agent-converter
url: https://skills.sh/qredence/skills/agent-converter
---

# agent-converter

skills/qredence/skills/agent-converter
agent-converter
Installation
$ npx skills add https://github.com/qredence/skills --skill agent-converter
SKILL.md
Agent Converter
Objective

Convert agent definitions between two formats:

Markdown format (.md with YAML frontmatter) — Rich format with explicit tool restrictions
TOML format (.toml) — Simple format for Codex agents with sandbox modes
Inputs
Source file: Path to an agent .md file (or directory of agents)
Output format: toml (default) or md
Output directory: Where to write converted files (default: same as source)
Commands
Convert single agent MD → TOML
python3 skills/agent-converter/scripts/convert_agent.py <input.md> [--output <dir>]

Convert all agents in directory
python3 skills/agent-converter/scripts/convert_agent.py --batch <input_dir> [--output <dir>]

Convert TOML → MD
python3 skills/agent-converter/scripts/convert_agent.py <input.toml> --to-md [--output <dir>]

Format Mapping
MD Frontmatter	TOML Field
name	(derived from filename)
description	Included in developer_instructions
tools	Mapped to sandbox_mode
Markdown body	developer_instructions
Tool → Sandbox Mode Mapping
Tools	Sandbox Mode
Read, Grep, Glob only	read-only
Any Write/Edit tools	allow-edits
No tools specified	allow-edits (default)
Sandbox Mode → Tool Mapping (reverse)
Sandbox Mode	Tools
read-only	Read, Grep, Glob
allow-edits	Read, Write, Edit, Bash, Glob, Grep
Example Conversion
Input: explorer.md
---
name: explorer
description: >
  Read-only codebase explorer.
tools:
  - Read
  - Grep
  - Glob
---

# Explorer — Read-Only Codebase Navigator

You are a read-only explorer agent...

Output: explorer.toml
sandbox_mode = "read-only"

developer_instructions = """
Role: Read-only codebase explorer.

Tools: Read, Grep, Glob

---

# Explorer — Read-Only Codebase Navigator

You are a read-only explorer agent...
"""

Workflow
Parse source file (MD or TOML)
Extract metadata and instructions
Map format-specific fields
Write output in target format
Report conversion summary
Error Handling
Error	Resolution
Missing frontmatter	Treat as plain markdown, use defaults
Invalid TOML	Report parse error with line number
Unknown tools	Warn and include in output as-is
File exists	Prompt user or use --force to overwrite
References
Format specification: skills/agent-converter/references/format-spec.md
Example agents: .agents/sub-agents/
Weekly Installs
13
Repository
qredence/skills
GitHub Stars
1
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass