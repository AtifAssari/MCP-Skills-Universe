---
rating: ⭐⭐
title: jupiter-swap-migration
url: https://skills.sh/jup-ag/agent-skills/jupiter-swap-migration
---

# jupiter-swap-migration

skills/jup-ag/agent-skills/jupiter-swap-migration
jupiter-swap-migration
Installation
$ npx skills add https://github.com/jup-ag/agent-skills --skill jupiter-swap-migration
SKILL.md
Jupiter Swap Migration Guide

Migrate existing Jupiter swap integrations from Metis (v1) or Ultra to the unified Swap API v2.

Target Base URL: https://api.jup.ag/swap/v2 Auth: x-api-key from portal.jup.ag (unchanged)

Use/Do Not Use

Use when:

Migrating code that calls api.jup.ag/swap/v1/quote, api.jup.ag/swap/v1/swap-instructions, or ultra-api.jup.ag.
Updating Jupiter swap endpoints to v2.
Switching from Metis two-step flow to the unified /build or /order endpoint.

Do not use when:

Building a new Jupiter integration from scratch (use integrating-jupiter skill instead).
Working with non-swap Jupiter APIs (Lend, Trigger, Recurring, etc.).

Triggers: ultra, metis, ultra swap, ultra api, ultra-api.jup.ag, /ultra/v1, swap/v1, swap-instructions, migrate swap, ultra migration, metis migration, swap v1 to v2, v1 to v2, upgrade jupiter, swap-instructions deprecated, deprecated swap, old jupiter api, swap upgrade, update swap api, quote endpoint deprecated, swap stopped working, swap broken, ExactOut removed, swapMode removed, userPublicKey, parameter rename, addressLookupTable, response format changed

Migration Paths
Source	Target	Effort	When to choose
Ultra → /order	GET /swap/v2/order + POST /swap/v2/execute	Minimal (URL change only)	Default for Ultra users
Metis → /build	GET /swap/v2/build	Moderate (parameter + response mapping)	Need transaction composability
Metis → /order	GET /swap/v2/order + POST /swap/v2/execute	Moderate (flow change)	Don't need tx modification, want managed execution
Path Details

Each path has a dedicated example with before/after code, parameter mappings, and response changes:

Path 1: Ultra → /order — Minimal migration, base URL change only
Path 2: Metis → /build — Consolidates 2 calls into 1, parameter and response mapping
Path 3: Metis → /order — Flow change to managed execution with multi-router competition
Post-Migration Checklist
URL audit: Search codebase for ultra-api.jup.ag, /ultra/v1/, /swap/v1/quote, /swap/v1/swap-instructions — all should be replaced
Parameter rename: userPublicKey → taker (for /build path)
swapMode removal: V2 only supports ExactIn. If using ExactOut, redesign the flow — this mode is no longer available
slippageBps default: /build defaults to 50 bps if omitted. For /order, verify the default if your integration relies on a specific value
Response field names: Verify your code uses inputAmountResult/outputAmountResult for the /execute response (the canonical v2 field names)
ALT handling: If using /build, switch from addressLookupTableAddresses (array) to addressesByLookupTableAddress (object) — remove RPC ALT resolution code
Fee event parsing: V2 instructions don't emit fee events — update any transaction parser that depends on them
Route plan format: If parsing route plans, use bps field (canonical) instead of percent
Error codes: Update error handling to match Swap v2 error codes
Test: Run end-to-end swap on devnet/mainnet with small amount to verify
Sunset

Remove this skill once Jupiter decommissions the v1 (/swap/v1) endpoints and the Ultra (ultra-api.jup.ag) domain. At that point all integrations will already be on v2.

Review by: 2026-09-01 — check if v1/Ultra endpoints have been decommissioned.

References
Migration guide
Order & Execute
Build
Fees
Routing
OpenAPI spec
Weekly Installs
82
Repository
jup-ag/agent-skills
GitHub Stars
62
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn