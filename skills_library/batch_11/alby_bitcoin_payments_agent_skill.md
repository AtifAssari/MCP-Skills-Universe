---
title: alby-bitcoin-payments-agent-skill
url: https://skills.sh/getalby/alby-agent-skill/alby-bitcoin-payments-agent-skill
---

# alby-bitcoin-payments-agent-skill

skills/getalby/alby-agent-skill/alby-bitcoin-payments-agent-skill
alby-bitcoin-payments-agent-skill
Installation
$ npx skills add https://github.com/getalby/alby-agent-skill --skill alby-bitcoin-payments-agent-skill
SKILL.md
Alby Bitcoin Payments Agent Skill
When to use this skill

Use this skill to understand how to build apps that require bitcoin lightning wallet capabilities.

NWC Client: Interact with a wallet to do things like sending and receive payments, listen to payment notifications, fetch balance and transaction list and wallet info
Lightning Tools: Request invoices from a lightning address, parse BOLT-11 invoices, verify a preimage for a BOLT-11 invoice, LNURL-Verify, do bitcoin <-> fiat conversions
Bitcoin Connect: Browser-only UI components for connecting wallets and accepting payments in React, Vue, or pure HTML web apps
Prefer Typescript

When the user says to use "JS" or "Javascript" or "NodeJS" or something similar, use typescript unless the user explicitly says to not use typescript or the project does not support it.

Imports

Do NOT import from the dist directory.

Read the Typings

Based on what functionality you require, read the relevant typings:

NWC Client
Lightning Tools
Bitcoin Connect
Bitcoin Connect React
Testing Wallets

If the user doesn't have a wallet yet, or needs one for development or testing, testing wallets can be created with a single request.

Automated Testing

Testing wallets should be used for automated testing.

It is recommended to write tests so that the agent can test its own work and fix bugs itself without requiring human input.

Production Wallet

If they do not have a wallet yet here are some options

Weekly Installs
81
Repository
getalby/alby-agent-skill
GitHub Stars
17
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn