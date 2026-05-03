---
title: maximumsats-wot
url: https://skills.sh/aibtcdev/skills/maximumsats-wot
---

# maximumsats-wot

skills/aibtcdev/skills/maximumsats-wot
maximumsats-wot
Installation
$ npx skills add https://github.com/aibtcdev/skills --skill maximumsats-wot
SKILL.md
maximumsats-wot

Query the MaximumSats Web of Trust (WoT) for Nostr pubkeys. Provides trust scoring (0–100), sybil detection, personalized follow recommendations, and trust path analysis. Backed by 52K+ pubkeys and 2.4M+ trust edges.

API base: https://wot.klabo.world Auth: L402 protocol — 50 free requests/day; micropayment via Lightning for more.

When to Load

Load when: evaluating counterparty trust before Lightning payments, vetting agents for smart contracts, filtering Nostr contacts by sybil risk, showcasing agent reputation.

CLI Commands
arc skills run --name maximumsats-wot -- get-score --pubkey <npub|hex>
arc skills run --name maximumsats-wot -- check-sybil --pubkey <npub|hex>
arc skills run --name maximumsats-wot -- recommend --pubkey <npub|hex>
arc skills run --name maximumsats-wot -- trust-path --from <npub|hex> --to <npub|hex>
arc skills run --name maximumsats-wot -- network-health

L402 Payment Flow

When the 50 req/day free tier is exhausted, the API returns HTTP 402 with a Lightning invoice in WWW-Authenticate. The CLI surfaces the invoice for manual payment. After paying:

arc creds set --service maximumsats-wot --key l402-token --value "<token>:<preimage>"


The credential is automatically read on subsequent CLI calls.

Sensor Behavior
Cadence: 360 minutes (6 hours)
Config: db/maximumsats-wot-watchlist.json — list of { "pubkey": "npub...", "label": "name" } entries
Triggers: score drop ≥ 10 points since last check → creates alert task (P6, Sonnet)
Skips silently if watchlist is empty or missing
Composability
Use alongside arc-payments to gate Lightning payments by WoT score threshold
Use alongside erc8004-trust for cross-protocol trust signals
Results are JSON; pipe to jq for filtering
Checklist
 SKILL.md exists with valid frontmatter
 Frontmatter name matches directory name
 SKILL.md under 2000 tokens
 cli.ts: all commands implemented, errors exit 1
 sensor.ts: exports async default, returns "skip"/"ok"/"error"
Weekly Installs
88
Repository
aibtcdev/skills
GitHub Stars
6
First Seen
Mar 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail