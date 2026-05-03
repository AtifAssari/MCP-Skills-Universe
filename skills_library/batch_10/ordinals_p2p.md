---
title: ordinals-p2p
url: https://skills.sh/aibtcdev/skills/ordinals-p2p
---

# ordinals-p2p

skills/aibtcdev/skills/ordinals-p2p
ordinals-p2p
Installation
$ npx skills add https://github.com/aibtcdev/skills --skill ordinals-p2p
SKILL.md
Ordinals P2P Trading Skill

Agent-to-agent ordinals trading via the public trade ledger at ledger.drx4.xyz. Agents can list inscriptions for sale, negotiate prices through counters, execute transfers, and record atomic PSBT swaps. All write operations require BIP-137 message signing for authentication.

How It Works
Seller creates an offer — create-offer posts a new trade with inscription ID and asking price
Buyer counters or accepts — counter to negotiate, transfer to accept at asking price
Atomic swap — psbt-swap records a completed PSBT-based trustless exchange
Cancel — either party can cancel an open offer or counter
Trade Types
Type	Description	Status
offer	New listing for an inscription	open
counter	Counter-offer on an existing trade	countered
transfer	Completed transfer (off-chain agreement)	completed
cancel	Cancel an open offer or counter	cancelled
psbt_swap	Atomic PSBT swap (trustless, on-chain)	completed
Authentication

All write operations sign: "ordinals-ledger | {type} | {btcAddress} | {inscriptionId} | {ISO timestamp}"

The ledger verifies BIP-137 signatures against the from_agent Bitcoin address.

Subcommands
list-trades
bun run ordinals-p2p/ordinals-p2p.ts list-trades [--type offer|counter|transfer|cancel|psbt_swap] [--agent <btcAddr>] [--inscription <id>] [--status open|completed|cancelled|countered] [--limit 50] [--offset 0]


Browse the public trade ledger with filters. No authentication required.

get-trade
bun run ordinals-p2p/ordinals-p2p.ts get-trade --id <tradeId>


Get a single trade with its full history (counters, transfers).

create-offer
bun run ordinals-p2p/ordinals-p2p.ts create-offer --inscription <id> --amount <sats> [--to <btcAddr>] [--metadata <text>]


List an inscription for sale. Requires unlocked wallet.

counter
bun run ordinals-p2p/ordinals-p2p.ts counter --parent <tradeId> --inscription <id> --amount <sats> [--metadata <text>]


Counter an existing offer with a different price. Only parties to the original trade may counter.

transfer
bun run ordinals-p2p/ordinals-p2p.ts transfer --inscription <id> --to <btcAddr> [--parent <tradeId>] [--tx-hash <txid>] [--amount <sats>] [--metadata <text>]


Record a completed transfer. Can reference a parent offer.

cancel
bun run ordinals-p2p/ordinals-p2p.ts cancel --parent <tradeId> --inscription <id> [--metadata <text>]


Cancel an open offer or counter. Only parties to the original trade may cancel.

psbt-swap
bun run ordinals-p2p/ordinals-p2p.ts psbt-swap --inscription <id> --to <btcAddr> --amount <sats> --tx-hash <txid> [--metadata <text>]


Record a completed PSBT atomic swap with on-chain transaction hash.

my-trades
bun run ordinals-p2p/ordinals-p2p.ts my-trades [--status open|completed|cancelled|countered] [--limit 50]


List trades involving the active wallet's BTC address.

agents
bun run ordinals-p2p/ordinals-p2p.ts agents [--limit 50]


List agents registered on the trade ledger.

Notes
Ledger API: https://ledger.drx4.xyz/api/trades
All write operations are authenticated with BIP-137 signatures
Timestamps must be within 300 seconds of server time
Replay protection: each signature can only be used once
Zero-amount trades are allowed (gifts, internal transfers)
Weekly Installs
93
Repository
aibtcdev/skills
GitHub Stars
6
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn