---
title: moneydevkit
url: https://skills.sh/openagentsinc/openagents/moneydevkit
---

# moneydevkit

skills/openagentsinc/openagents/moneydevkit
moneydevkit
Installation
$ npx skills add https://github.com/openagentsinc/openagents --skill moneydevkit
SKILL.md
Money Dev Kit
Overview

Integrate Lightning payment workflows using Money Dev Kit. Use this skill when tasks involve setting up @moneydevkit/agent-wallet for autonomous agents, wiring @moneydevkit/nextjs or @moneydevkit/replit checkout flows, bootstrapping credentials via @moneydevkit/create, validating MDK environment variables, or applying hybrid architecture constraints (hosted API plus self-custodial node).

Environment
Requires bash, curl, and Node.js 20+.
Requires internet access to npm and Money Dev Kit services.

Use this skill for implementation tasks, not high-level Lightning theory.

Workflow
Choose the right integration path first:
agent-wallet path for autonomous agents and CLI automation (no API account required).
nextjs or replit checkout path for hosted checkout UI and product catalog workflows (requires credentials).
Run preflight checks:
scripts/check-mdk-prereqs.sh agent-wallet for wallet automation path.
scripts/check-mdk-prereqs.sh checkout for API/checkout path.
Execute the selected path:
Agent wallet flow from agent-wallet-operations.
Checkout flow from checkout-integration.
Apply architecture and custody constraints:
Use architecture-and-self-hosting before finalizing deployment.
Explicitly handle mnemonic custody, API key handling, and self-hosted vs hosted service decisions.
Verify outcome:
For wallet path: can receive, send, and inspect payments with JSON responses.
For checkout path: can create checkout, render hosted checkout page, expose /api/mdk, and verify paid status.
Quick Commands
# Agent wallet path (signet recommended for testing)
npx @moneydevkit/agent-wallet@latest init --network signet
npx @moneydevkit/agent-wallet@latest status
npx @moneydevkit/agent-wallet@latest balance

# Checkout path credential bootstrap
npx @moneydevkit/create@latest

Reference Files
agent-wallet-operations: no-account self-custodial CLI workflow.
checkout-integration: Next.js/Replit wiring, env vars, and checkout loop.
architecture-and-self-hosting: hybrid model, trust boundaries, and self-host knobs.
Weekly Installs
36
Repository
openagentsinc/openagents
GitHub Stars
410
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn