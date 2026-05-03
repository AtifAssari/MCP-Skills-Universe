---
rating: ⭐⭐
title: siwa
url: https://skills.sh/bankrbot/skills/siwa
---

# siwa

skills/bankrbot/skills/siwa
siwa
Installation
$ npx skills add https://github.com/bankrbot/skills --skill siwa
SKILL.md
SIWA SDK

Sign-In With Agent (SIWA) lets AI agents authenticate with services using their ERC-8004 onchain identity.

Install
npm install @buildersgarden/siwa

Skills
Agent-Side (Signing)

Choose based on your wallet provider:

Bankr — Bankr Agent API wallets
Server-Side (Verification)
Server-Side Verification — Next.js, Express, Hono, Fastify
SDK Modules
Import	Description
@buildersgarden/siwa	Core: signSIWAMessage, verifySIWA, createSIWANonce
@buildersgarden/siwa/signer	Signer factories
@buildersgarden/siwa/erc8128	ERC-8128 HTTP signing/verification
@buildersgarden/siwa/receipt	HMAC receipt helpers
@buildersgarden/siwa/nonce-store	Nonce stores (Memory, Redis, KV)
@buildersgarden/siwa/next	Next.js middleware
@buildersgarden/siwa/express	Express middleware
@buildersgarden/siwa/hono	Hono middleware
@buildersgarden/siwa/fastify	Fastify middleware
Links
Latest version of this skill
Documentation
ERC-8004
ERC-8128
Weekly Installs
51
Repository
bankrbot/skills
GitHub Stars
1.1K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn