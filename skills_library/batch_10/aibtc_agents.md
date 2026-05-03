---
title: aibtc-agents
url: https://skills.sh/aibtcdev/skills/aibtc-agents
---

# aibtc-agents

skills/aibtcdev/skills/aibtc-agents
aibtc-agents
Installation
$ npx skills add https://github.com/aibtcdev/skills --skill aibtc-agents
SKILL.md
aibtc-agents Skill

A community registry of agent configuration templates. Each subdirectory documents how a specific AIBTC agent is configured: which skills it uses, wallet setup, environment variables, and workflow participation.

Usage

Browse the agent configs directly:

cat aibtc-agents/<handle>/README.md


Or copy the template to start your own:

cp aibtc-agents/template/setup.md aibtc-agents/<your-handle>/README.md

Included Configs
arc0btc — Arc's reference configuration (orchestrator, 108 skills, 74 sensors)
spark0btc — Spark's config (AIBTC/DeFi specialist)
iris0btc — Iris's config (research/X integration)
loom0btc — Loom's config (CI/CD specialist)
forge0btc — Forge's config (infrastructure specialist)
secret-mars, tiny-marten, testnet-explorer — Community agent configs
Contributing

See aibtc-agents/README.md for contribution guidelines and PR requirements.

Weekly Installs
106
Repository
aibtcdev/skills
GitHub Stars
6
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn