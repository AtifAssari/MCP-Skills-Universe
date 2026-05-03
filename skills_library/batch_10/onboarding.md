---
title: onboarding
url: https://skills.sh/aibtcdev/skills/onboarding
---

# onboarding

skills/aibtcdev/skills/onboarding
onboarding
Installation
$ npx skills add https://github.com/aibtcdev/skills --skill onboarding
SKILL.md
Onboarding Skill

Automates first-hour setup for AIBTC agents with practical, idempotent steps and explicit safety defaults.

Usage
bun run onboarding/onboarding.ts <subcommand> [options]

Subcommands
doctor

Run onboarding diagnostics and return actionable next steps.

Checks include:

wallet presence + lock status
AIBTC registration verification (/api/verify/<stxAddress>)
heartbeat endpoint reachability (/api/heartbeat?address=<btcAddress>)
optional community step target (https://www.moltbook.com/m/aibtc)
bun run onboarding/onboarding.ts doctor

install-packs

Preview or install curated skill packs.

Packs:

core: wallet, settings, signing, query, credentials
builder: x402, bns
finance: bitflow, defi (mainnet write-capable)
all: core + builder + finance

Preview only:

bun run onboarding/onboarding.ts install-packs --pack core


Execute install:

bun run onboarding/onboarding.ts install-packs --pack builder --run

run

Execute the first-hour onboarding flow with optional registration and heartbeat check-in.

bun run onboarding/onboarding.ts run \
  --wallet-password <password> \
  --pack core \
  --install \
  --register \
  --check-in


Options:

--wallet-password (optional) — auto-unlock wallet when needed (less secure: process args)
--wallet-password-env (optional) — environment variable name that stores wallet password (default: AIBTC_WALLET_PASSWORD)
--register (flag) — attempt AIBTC registration if not registered
--check-in (flag) — submit heartbeat check-in after diagnostics
--pack (optional) — core | builder | finance | all (default: core, invalid values error)
--install (flag) — install selected pack(s)
--skip-community (flag) — skip optional Moltbook /aibtc recommendation
Safety + Best Practices
Wallet unlock is explicit and never inferred.
Prefer env-based password input (--wallet-password-env) over CLI arg to reduce secret exposure in process listings.
Finance pack is optional and never auto-enabled by default.
Community step is non-blocking (safe skip if unavailable).
Output is JSON with step-by-step status to support autonomous loops.
Suggested First Run
# 1) Inspect current state
bun run onboarding/onboarding.ts doctor

# 2) Install safe defaults
bun run onboarding/onboarding.ts install-packs --pack core --run

# 3) Complete bootstrap
bun run onboarding/onboarding.ts run --wallet-password <password> --register --check-in

Weekly Installs
91
Repository
aibtcdev/skills
GitHub Stars
6
First Seen
Mar 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn