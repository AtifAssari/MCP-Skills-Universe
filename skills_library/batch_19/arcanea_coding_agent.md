---
title: arcanea-coding-agent
url: https://skills.sh/frankxai/arcanea/arcanea-coding-agent
---

# arcanea-coding-agent

skills/frankxai/arcanea/arcanea-coding-agent
arcanea-coding-agent
Installation
$ npx skills add https://github.com/frankxai/arcanea --skill arcanea-coding-agent
SKILL.md
Arcanea Coding Agent Skill
Overview

This skill transforms opencode into an Arcanean creative workspace, giving you access to 64 specialized agents for creative projects directly within your editor.

Installation
# In opencode, the skill is automatically available when in Arcanea directory
# Or manually enable:
opencode skill enable arcanea-coding-agent

Features
64 Specialized Agents - Access all elemental courts
Inline Invocation - @agent mentions in any file
Workflow Support - Multi-agent orchestration
Context Awareness - Agents know your current file/project
Real-time Streaming - See agent responses as they generate
Cache & Learning - Faster responses over time
Usage
Basic Agent Invocation

Type in any file or chat:

@ignition help me brainstorm ideas for this function

Context-Aware Help

Select code, then invoke:

@refinement improve this selected code

Multi-Agent Workflows
@orchestration create character profile for my protagonist

Commands
Command	Description
arcanea:invoke	Invoke agent with current context
arcanea:agents	List all available agents
arcanea:workflows	Show available workflows
arcanea:mode arcane	Switch to mystical language
arcanea:mode pro	Switch to professional terms
Configuration
{
  "arcanea": {
    "mode": "arcane",
    "defaultAgent": "orchestration",
    "aiProvider": "hybrid",
    "claudeApiKey": "${CLAUDE_API_KEY}",
    "cacheEnabled": true,
    "streaming": true
  }
}

Key Agents for Coding
@structure - System architecture and design
@optimization - Performance improvements
@refinement - Code polishing and cleanup
@clarity - Documentation and explanation
@debug-exorcist - Bug hunting and fixes
Integration

This skill works with:

opencode editor commands
File context awareness
Selection-based operations
Project-wide knowledge
Learn More
Full Documentation: AGENT_ARCHITECTURE_v4.md
Claude Instructions: .claude/CLAUDE.md
UI Demo: PREMIUM_UI_DEMO.html
Weekly Installs
29
Repository
frankxai/arcanea
GitHub Stars
3
First Seen
Feb 17, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass