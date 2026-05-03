---
rating: ⭐⭐
title: tenero
url: https://skills.sh/aibtcdev/skills/tenero
---

# tenero

skills/aibtcdev/skills/tenero
tenero
Installation
$ npx skills add https://github.com/aibtcdev/skills --skill tenero
SKILL.md
Tenero Skill

Provides real-time market analytics for tokens, wallets, DEXs, and markets via the Tenero API (formerly STXTools). All endpoints are read-only and require no authentication. Data covers Stacks, Spark, and SportsFun chains.

Usage
bun run tenero/tenero.ts <subcommand> [options]

Subcommands
token-info

Get token details including metadata, price, and volume.

bun run tenero/tenero.ts token-info --token <address> [--chain <chain>]


Options:

--token (required) — Token contract address (e.g. SP1AY6K3PQV5MRT6R4S671NWW2FRVPKM0BR162CT6.leo-token)
--chain (optional) — Chain to query (default: stacks)

Output:

{
  "contract_id": "SP1AY6K3PQV5MRT6R4S671NWW2FRVPKM0BR162CT6.leo-token",
  "symbol": "LEO",
  "name": "Leo",
  "decimals": 6,
  "price_usd": "0.0012",
  "price_stx": "0.0042",
  "volume_24h_usd": "45000",
  "market_cap_usd": "1200000"
}

market-summary

Get token market summary including price history, volume, and liquidity.

bun run tenero/tenero.ts market-summary --token <address> [--chain <chain>]


Options:

--token (required) — Token contract address
--chain (optional) — Chain to query (default: stacks)

Output:

{
  "contract_id": "SP1AY6K3PQV5MRT6R4S671NWW2FRVPKM0BR162CT6.leo-token",
  "price_usd": "0.0012",
  "price_change_1h": "1.2",
  "price_change_24h": "-3.5",
  "price_change_7d": "12.4",
  "volume_24h_usd": "45000",
  "liquidity_usd": "350000",
  "holders": 1842
}

market-stats

Get overall market statistics including total volume, market cap, and active tokens.

bun run tenero/tenero.ts market-stats [--chain <chain>]


Options:

--chain (optional) — Chain to query (default: stacks)

Output:

{
  "total_volume_24h_usd": "2500000",
  "total_market_cap_usd": "85000000",
  "active_tokens": 342,
  "total_trades_24h": 18420,
  "unique_traders_24h": 3210
}

top-gainers

Get top gaining tokens by price change percentage over the past 24 hours.

bun run tenero/tenero.ts top-gainers [--chain <chain>] [--limit <number>]


Options:

--chain (optional) — Chain to query (default: stacks)
--limit (optional) — Maximum number of results (default: 10)

Output:

[
  {
    "contract_id": "SP1AY6K3PQV5MRT6R4S671NWW2FRVPKM0BR162CT6.leo-token",
    "symbol": "LEO",
    "price_usd": "0.0012",
    "price_change_24h": "42.5",
    "volume_24h_usd": "45000"
  }
]

top-losers

Get top losing tokens by price change percentage over the past 24 hours.

bun run tenero/tenero.ts top-losers [--chain <chain>] [--limit <number>]


Options:

--chain (optional) — Chain to query (default: stacks)
--limit (optional) — Maximum number of results (default: 10)

Output:

[
  {
    "contract_id": "SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.arkadiko-token",
    "symbol": "DIKO",
    "price_usd": "0.045",
    "price_change_24h": "-18.3",
    "volume_24h_usd": "12000"
  }
]

wallet-holdings

Get wallet token holdings with current USD value. Uses the active wallet address if --address is omitted.

bun run tenero/tenero.ts wallet-holdings [--address <stx_address>] [--chain <chain>]


Options:

--address (optional) — Stacks address to check (uses active wallet if omitted)
--chain (optional) — Chain to query (default: stacks)

Output:

{
  "address": "SP2X0TZ59D5SZ8ACQ6YMCHHNR2ZN51Z32E2CJ173",
  "total_value_usd": "1250.42",
  "holdings": [
    {
      "contract_id": "SP1AY6K3PQV5MRT6R4S671NWW2FRVPKM0BR162CT6.leo-token",
      "symbol": "LEO",
      "balance": "1000000",
      "value_usd": "1.20"
    }
  ]
}

wallet-trades

Get wallet trade history. Uses the active wallet address if --address is omitted.

bun run tenero/tenero.ts wallet-trades [--address <stx_address>] [--chain <chain>] [--limit <number>]


Options:

--address (optional) — Stacks address to check (uses active wallet if omitted)
--chain (optional) — Chain to query (default: stacks)
--limit (optional) — Maximum number of results (default: 20)

Output:

[
  {
    "tx_id": "0xabc123...",
    "timestamp": "2024-01-15T12:00:00Z",
    "type": "swap",
    "token_in": "STX",
    "token_out": "LEO",
    "amount_in_usd": "10.00",
    "amount_out_usd": "9.85"
  }
]

trending-pools

Get trending DEX pools by volume within a timeframe.

bun run tenero/tenero.ts trending-pools [--timeframe <1h|6h|24h>] [--chain <chain>] [--limit <number>]


Options:

--timeframe (optional) — Time window: 1h, 6h, or 24h (default: 24h)
--chain (optional) — Chain to query (default: stacks)
--limit (optional) — Maximum number of results (default: 10)

Output:

[
  {
    "pool_id": "SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.univ2-share-fee-to",
    "token_x": "STX",
    "token_y": "LEO",
    "volume_usd": "85000",
    "liquidity_usd": "420000",
    "fee_24h_usd": "255"
  }
]

whale-trades

Get large/whale trades above a threshold value.

bun run tenero/tenero.ts whale-trades [--chain <chain>] [--limit <number>]


Options:

--chain (optional) — Chain to query (default: stacks)
--limit (optional) — Maximum number of results (default: 10)

Output:

[
  {
    "tx_id": "0xdef456...",
    "timestamp": "2024-01-15T11:45:00Z",
    "wallet": "SP2X0TZ59D5SZ8ACQ6YMCHHNR2ZN51Z32E2CJ173",
    "type": "buy",
    "token": "ALEX",
    "amount_usd": "25000"
  }
]

holder-stats

Get token holder distribution and statistics.

bun run tenero/tenero.ts holder-stats --token <address> [--chain <chain>]


Options:

--token (required) — Token contract address
--chain (optional) — Chain to query (default: stacks)

Output:

{
  "contract_id": "SP1AY6K3PQV5MRT6R4S671NWW2FRVPKM0BR162CT6.leo-token",
  "total_holders": 1842,
  "top_10_concentration": "45.2",
  "top_25_concentration": "62.8",
  "top_holders": [
    {
      "address": "SP2X0TZ59D5SZ8ACQ6YMCHHNR2ZN51Z32E2CJ173",
      "balance": "50000000",
      "percentage": "5.0"
    }
  ]
}

search

Search tokens, pools, and wallets by name or address fragment.

bun run tenero/tenero.ts search --query <string> [--chain <chain>]


Options:

--query (required) — Search query string (token name, symbol, or address)
--chain (optional) — Chain to query (default: stacks)

Output:

{
  "tokens": [
    {
      "contract_id": "SP1AY6K3PQV5MRT6R4S671NWW2FRVPKM0BR162CT6.leo-token",
      "symbol": "LEO",
      "name": "Leo"
    }
  ],
  "pools": [],
  "wallets": []
}

Notes
All endpoints are read-only — no API key or wallet required for most subcommands
wallet-holdings and wallet-trades use the active unlocked wallet address when --address is omitted
The --chain option supports stacks (default), spark, and sportsfun
Response data is passed through directly from the Tenero API data field
Base URL: https://api.tenero.io
Weekly Installs
127
Repository
aibtcdev/skills
GitHub Stars
5
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn