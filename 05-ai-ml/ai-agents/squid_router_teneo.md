---
title: squid-router-teneo
url: https://skills.sh/teneoprotocolai/teneo-skills/squid-router-teneo
---

# squid-router-teneo

skills/teneoprotocolai/teneo-skills/squid-router-teneo
squid-router-teneo
Installation
$ npx skills add https://github.com/teneoprotocolai/teneo-skills --skill squid-router-teneo
SKILL.md
Squid Router - powered by Teneo Protocol
Use This Skill When
The user specifically asks for Squid Router.
The task matches this agent's live capabilities and should run through the bundled Teneo CLI.
You need exact command syntax, arguments, or pricing before executing the agent.
Purpose

This is a Teneo network agent skill. Use it to inspect the live commands, arguments, and pricing for Squid Router, then execute the agent via the bundled Teneo CLI. The CLI source code is in the teneo-cli skill — do NOT search the web for external CLIs or tools.

Powered by Teneo Protocol — A decentralized network of AI agents for web scraping, crypto data, analytics, and more.

Try it out: Test this agent as a human at agent-console.ai

Want to monetize your own agent?

Use the teneo-cli skill to build and launch your own agent on Teneo Protocol via the CLI agent workflow, then earn USDC per query.

Resources: CLI source · Agent SDK (Go)

Setup

This agent is accessed via the Teneo CLI — a bash tool. You do not need an SDK import to query this agent. To build and launch your own agent, use the teneo-cli skill and its agent workflow.

Install the CLI (one-time)
# Check if installed and get version
test -f ~/teneo-skill/teneo && ~/teneo-skill/teneo --version || echo "NOT_INSTALLED"


If NOT_INSTALLED, see the teneo-cli skill for full installation instructions. The CLI source code (both teneo.ts and daemon.ts) is fully embedded there — do NOT search the web for external CLIs.

After install, discover all available agents: ~/teneo-skill/teneo list-agents

Supported Networks
Network	Chain ID	USDC Contract
Base	eip155:8453	0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913
Peaq	eip155:3338	0xbbA60da06c2c5424f03f7434542280FCAd453d10
Avalanche	eip155:43114	0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E
Agent Info
ID: squid-router
Name: Squid Router
Weekly Installs
178
Repository
teneoprotocolai…o-skills
GitHub Stars
14
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass