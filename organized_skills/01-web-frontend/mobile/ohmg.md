---
rating: ⭐⭐
title: ohmg
url: https://skills.sh/supercent-io/skills-template/ohmg
---

# ohmg

skills/supercent-io/skills-template/ohmg
ohmg
Installation
$ npx skills add https://github.com/supercent-io/skills-template --skill ohmg
Summary

Multi-agent orchestrator for coordinating specialized domain agents across PM, Frontend, Backend, Mobile, QA, and Debug roles.

Spawns and coordinates six specialized agents (PM, Frontend, Backend, Mobile, QA, Debug) with role-specific triggers and capabilities
Uses Serena Memory for structured cross-agent state management and real-time observability via terminal and web dashboards
Supports multi-CLI vendor integration (Gemini, Claude, Codex) with per-agent CLI mapping in configuration
Includes interactive setup, system diagnostics, and agent spawning via explicit /coordinate commands or direct CLI invocation
SKILL.md
oh-my-ag (ohmg) - Multi-Agent Orchestrator
When to use this skill
Coordinating complex multi-domain projects
Parallelizing tasks across multiple AI agents (PM, Frontend, Backend, etc.)
Using Serena Memory for cross-agent state management
Setting up real-time observability dashboards for agent workflows
Integrating multi-CLI vendors (Gemini, Claude, Codex) in a single project
1. Core Concepts
Specialized Agents
Agent	Specialization	Triggers
Workflow Guide	Coordinates complex projects	"multi-domain", "complex project"
PM Agent	Requirements, task decomposition	"plan", "break down"
Frontend Agent	React/Next.js, styling	"UI", "component", "styling"
Backend Agent	API, database, auth	"API", "database", "auth"
Debug Agent	Bug diagnosis, RCA	"bug", "error", "crash"
Serena Memory

Orchestrator writes structured state to .serena/memories/ for real-time monitoring and cross-agent coordination.

2. Installation & Setup
Prerequisites
Bun (CLI and dashboards)
uv (Serena setup)
Interactive Setup
bunx oh-my-ag


Select project type to install relevant skills to .agent/skills/.

Verification
bunx oh-my-ag doctor

3. Usage Patterns
Explicit Coordination
/coordinate


PM planning → agent spawning → QA review.

Spawning Agents via CLI
# Spawn backend agent for a specific task
oh-my-ag agent:spawn backend "Implement auth API" session-01

Dashboard Monitoring
Terminal: bunx oh-my-ag dashboard
Web: bunx oh-my-ag dashboard:web (http://localhost:9847)
4. MCP Connection & Bridging
SSE Mode (Shared Server)

If environment needs stdio-to-http bridging:

bunx oh-my-ag bridge http://localhost:12341/sse

5. Configuration

Configure per-agent CLI mapping in .agent/config/user-preferences.yaml:

agent_cli_mapping:
  frontend: gemini
  backend: codex
  pm: claude
  qa: claude

Quick Reference
Command	Action
bunx oh-my-ag	Interactive installer
/setup	Agent-side configuration
bunx oh-my-ag doctor	System check & repair
bunx oh-my-ag update	Update skills
bunx oh-my-ag usage	Show quota usage
Weekly Installs
10.4K
Repository
supercent-io/sk…template
GitHub Stars
88
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass