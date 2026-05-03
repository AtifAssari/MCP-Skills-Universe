---
title: grimoire-hyperliquid
url: https://skills.sh/franalgaba/grimoire/grimoire-hyperliquid
---

# grimoire-hyperliquid

skills/franalgaba/grimoire/grimoire-hyperliquid
grimoire-hyperliquid
Installation
$ npx skills add https://github.com/franalgaba/grimoire --skill grimoire-hyperliquid
Summary

Query Hyperliquid market data, order books, metadata, and execute withdrawals via Grimoire CLI.

Supports six command categories: mid prices, L2 order books, open orders, perpetual metadata, spot metadata, and USDC withdrawals
Output formats include JSON, table, and spell (for snapshot-based agent inputs); withdrawals require explicit user confirmation and keystore credentials
Read-only commands (mids, l2-book, open-orders, meta, spot-meta) return market snapshots; stateful withdraw action needs HYPERLIQUID_PRIVATE_KEY environment variable
Invocable via grimoire venue hyperliquid, npm/bun, or direct binary from @grimoirelabs/venues
SKILL.md
Grimoire Hyperliquid Skill

Use this skill for Hyperliquid metadata snapshots and, when explicitly requested, withdrawals.

Preferred invocations:

grimoire venue hyperliquid ...
npx -y @grimoirelabs/cli venue hyperliquid ... (no-install)
bun run packages/cli/src/index.ts venue hyperliquid ... (repo-local)
grimoire-hyperliquid ... (direct binary from @grimoirelabs/venues)

Recommended preflight:

grimoire venue doctor --adapter hyperliquid --json
Ensure HYPERLIQUID_PRIVATE_KEY is set before stateful actions (withdraw).

Use --format spell for snapshot params: blocks.

Commands

Read-only data:

grimoire venue hyperliquid mids — mid prices for all perp assets
grimoire venue hyperliquid l2-book --coin <symbol> — L2 order book for a coin
grimoire venue hyperliquid open-orders --user <address> — open orders for an address
grimoire venue hyperliquid meta — perp market metadata (universe, margin tables)
grimoire venue hyperliquid spot-meta — spot market metadata (tokens, universe)

Snapshot commands (agent-only, generate spell params: blocks):

grimoire venue hyperliquid mids-snapshot
grimoire venue hyperliquid l2-book-snapshot --coin <symbol>
grimoire venue hyperliquid open-orders-snapshot --user <address>
grimoire venue hyperliquid meta-snapshot
grimoire venue hyperliquid spot-meta-snapshot

Stateful:

grimoire venue hyperliquid withdraw --amount <usdc> --keystore <path> [--password-env <name>] [--destination <addr>]
Examples
grimoire venue hyperliquid mids --format table
grimoire venue hyperliquid mids --format spell
grimoire venue hyperliquid l2-book --coin BTC
grimoire venue hyperliquid l2-book --coin BTC --format spell
grimoire venue hyperliquid open-orders --user 0x0000000000000000000000000000000000000000
grimoire venue hyperliquid meta
grimoire venue hyperliquid mids-snapshot
grimoire venue hyperliquid l2-book-snapshot --coin BTC
grimoire venue hyperliquid meta-snapshot


Use -snapshot variants to emit params: blocks for spell inputs. These are agent-only (output suppressed in interactive mode).

Spell Actions

Hyperliquid uses custom action type with op: "order" for order placement:

hyperliquid.custom(op="order", coin="ETH", price="3500", size="0.1", side="buy", order_type="Gtc")


The adapter does not support runtime constraints (max_slippage, etc.). Order parameters are validated at the adapter boundary.

Supported TIF values: Gtc, Ioc, Alo, FrontendMarket.

Metric Surface (Spell Comparisons)

Hyperliquid exposes mid_price for symbol midpoint comparisons:

hl_mid = metric("mid_price", hyperliquid, ETH)


The third argument is the Hyperliquid symbol to read (for example ETH, BTC, SOL).

Notes
withdraw is stateful and requires explicit user confirmation plus keystore credentials.
mids, l2-book, open-orders, meta, spot-meta are read-only info calls.
Use --format spell for snapshot-based spell inputs.
Use --format json for meta/spot-meta in automation; --format table shows compact summaries for nested payloads.
anvil/cast are EVM tools and are not applicable for Hyperliquid execution/diagnostics.
Weekly Installs
1.0K
Repository
franalgaba/grimoire
GitHub Stars
5
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn