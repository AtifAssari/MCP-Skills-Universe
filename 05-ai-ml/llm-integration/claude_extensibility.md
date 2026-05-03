---
rating: ⭐⭐⭐
title: claude-extensibility
url: https://skills.sh/samhvw8/dot-claude/claude-extensibility
---

# claude-extensibility

skills/samhvw8/dot-claude/claude-extensibility
claude-extensibility
Installation
$ npx skills add https://github.com/samhvw8/dot-claude --skill claude-extensibility
SKILL.md
Claude Code Extensibility

CRUD operations for agents, skills, and output styles following Anthropic best practices.

Related Skills

IMPORTANT: When creating or editing prompts, use prompt-enhancer skill to improve quality.

Skill("prompt-enhancer")  → Enhance skill/agent prompt content

Core Principles
Simplicity: Direct tool calls, avoid complex abstractions
Focus: Single, clear responsibility per extension
Conciseness: Target <500 lines, use progressive disclosure
Efficiency: Optimize for token usage and response time
Extension Types
Type	Invocation	Purpose	Location
Agents	Task tool	Specialized sub-processes	.claude/agents/
Skills	Model-invoked (autonomous)	Domain knowledge	.claude/skills/{name}/
Output Styles	/output-style command	Modify main agent behavior	.claude/output-styles/
Agent Development

Reference: references/agent-development.md - Full YAML structure, model/tool selection, system prompt patterns, optimization techniques.

Quick Start: Agent
---
name: agent-name
description: Use this agent when [use case]. Use PROACTIVELY for [triggers].\n\nExamples:\n<example>\nContext: [situation]\nuser: [request]\nassistant: [response]\n<commentary>[reasoning]</commentary>\n</example>
tools: Grep, Glob, Read, Bash
model: haiku
permissionMode: default
skills: skill-name
---

# Agent Name

Brief mission statement.

## Core Strategy

### 1. Phase Name
Approach and techniques

<format>
Expected output structure
</format>

YAML Fields
Field	Required	Description
name	Yes	Lowercase, hyphens (e.g., code-reviewer)
description	Yes	Single line with \n for newlines, include examples
tools	No	Comma-separated; inherits all if omitted
model	No	haiku, sonnet, opus, inherit (default: sonnet)
permissionMode	No	default, acceptEdits, bypassPermissions, plan, ignore
skills	No	Comma-separated skill names to auto-load
Model Selection
Model	Use When	Target Time
haiku	Fast tasks, exploration, search	< 3s
sonnet	Balanced, most use cases	< 10s
opus	Complex reasoning, architecture	< 30s
inherit	Match main conversation model	varies
Built-in Subagents
Agent	Model	Tools	Purpose
general-purpose	Sonnet	All	Complex research, multi-step operations
plan	Sonnet	Read, Glob, Grep, Bash	Research in plan mode
Explore	Haiku	Read-only	Fast codebase search (quick/medium/very thorough)
Agent Locations
Location	Scope	Priority
.claude/agents/	Project	Highest
~/.claude/agents/	User (all projects)	Lower
Plugin agents/	Plugin-specific	Varies
--agents CLI flag	Session only	Medium
CLI-Defined Agents
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer. Use proactively after code changes.",
    "prompt": "You are a senior code reviewer...",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  }
}'

Resumable Agents

Continue previous conversations:

Each execution gets unique agentId
Transcript stored in agent-{agentId}.jsonl
Resume with previous agentId to continue with full context
Skill Development

Reference: references/skill-development.md - Full structure, trigger patterns, hook system.

Quick Start: Skill
---
name: skill-name
description: "[What it does]. [Technologies]. Capabilities: [list]. Actions: [verbs]. Keywords: [triggers]. Use when: [scenarios]."
allowed-tools: Read, Grep, Glob
---

# Skill Name

## Purpose
What this skill helps with

## When to Use
Specific scenarios and conditions

## Key Information
Guidance, patterns, examples

YAML Fields
Field	Required	Description
name	Yes	Lowercase, hyphens, max 64 chars
description	Yes	WHAT + WHEN format, max 1024 chars, quoted
allowed-tools	No	Restrict tool access (security)
Description Format (WHAT + WHEN)

Structure:

"[Core purpose]. [Technologies/Stack]. Capabilities: [list]. Actions: [verbs]. Keywords: [triggers]. Use when: [scenarios]."


Good example:

description: "Extract text and tables from PDF files, fill forms, merge documents. Formats: .pdf. Tools: pypdf, pdfplumber. Capabilities: text extraction, form filling, document merging. Actions: extract, fill, merge PDFs. Keywords: PDF, form, document, pypdf, pdfplumber. Use when: working with PDF files, extracting data from documents, filling PDF forms."


Bad examples:

description: Helps with documents  # Too vague
description: PDF skill  # Missing WHEN triggers

Tool Access Control

Restrict Claude's tools with allowed-tools:

---
name: safe-reader
description: "Read-only file access. Use when viewing code without modifications."
allowed-tools: Read, Grep, Glob
---

Skill Locations
Location	Scope
.claude/skills/{name}/SKILL.md	Project (shared via git)
~/.claude/skills/{name}/SKILL.md	User (all projects)
Plugin skills/	Plugin-bundled
Skill Structure
my-skill/
├── SKILL.md (required)
├── references/ (optional - detailed docs)
├── scripts/ (optional - utilities)
└── templates/ (optional - templates)

Output Styles

Modify Claude Code's main agent behavior.

Quick Start: Output Style
---
name: My Custom Style
description: Brief description of behavior
keep-coding-instructions: true
---

# Custom Style Instructions

You are an interactive CLI tool that helps users...

## Specific Behaviors
[Define assistant behavior...]

YAML Fields
Field	Purpose	Default
name	Display name	Filename
description	UI description	None
keep-coding-instructions	Retain coding instructions	false
Built-in Styles
Default: Standard software engineering
Explanatory: Educational insights between tasks
Learning: Collaborative with TODO(human) markers
Output Style Locations
User: ~/.claude/output-styles/
Project: .claude/output-styles/
Usage
/output-style              # Access menu
/output-style explanatory  # Switch directly

Testing
Key Question: Does it activate when expected?

Agent Testing:

Task(
  subagent_type="agent-name",
  description="Test task",
  prompt="Detailed test prompt"
)


Skill Testing:

Test prompts that SHOULD trigger
Test prompts that should NOT trigger
Debug with: claude --debug
Common Workflows
Create Agent
Create .claude/agents/{name}.md
Write YAML frontmatter (name, description, tools, model)
Write system prompt (<500 lines)
Test with Task tool
Optimize based on performance
Create Skill
Create .claude/skills/{name}/SKILL.md
Write YAML frontmatter with WHAT + WHEN description
Write content (<500 lines)
Use Skill("prompt-enhancer") to improve prompt
Add reference files for detailed content
Test: Does it activate when expected?
Optimize Extension
Measure baseline (lines, token usage, response time)
Move details to reference files
Use Skill("prompt-enhancer") to improve prompts
Remove second-person voice
Use code blocks over prose
Add XML structure
Test and verify improvements
Best Practices
Anthropic Guidelines

✅ 500-line rule: Keep SKILL.md and agent prompts under 500 lines ✅ Progressive disclosure: Use reference files for detailed content ✅ Proactive language: Include "use PROACTIVELY" in descriptions ✅ WHAT + WHEN descriptions: Both capability and triggers ✅ Test first: Build 3+ evaluations before extensive documentation ✅ Least privilege: Limit tools to necessary set

Anti-Patterns

❌ Vague descriptions without triggers ❌ Over 500 lines without references ❌ Second-person voice ("you should...") ❌ All tools when subset suffices ❌ No examples in agent descriptions

Quick Reference

Agent Model Selection:

Haiku: Fast, simple tasks (< 3s)
Sonnet: Balanced, most use cases (< 10s)
Opus: Complex reasoning (< 30s)
Inherit: Match main conversation

File Locations:

Agents: .claude/agents/*.md
Skills: .claude/skills/{name}/SKILL.md
Output Styles: .claude/output-styles/*.md

Management Commands:

/agents - Interactive agent management
/output-style - Switch output styles

Status: Production Ready | Lines: ~200 | Progressive Disclosure: ✅

Weekly Installs
39
Repository
samhvw8/dot-claude
GitHub Stars
10
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass