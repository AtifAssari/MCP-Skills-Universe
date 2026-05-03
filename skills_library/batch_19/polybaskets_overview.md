---
title: polybaskets-overview
url: https://skills.sh/adityaakr/polybaskets/polybaskets-overview
---

# polybaskets-overview

skills/adityaakr/polybaskets/polybaskets-overview
polybaskets-overview
Installation
$ npx skills add https://github.com/adityaakr/polybaskets --skill polybaskets-overview
SKILL.md
PolyBaskets Overview
What Is PolyBaskets

PolyBaskets is an ETF-style prediction market aggregator on Vara Network. It bundles multiple Polymarket outcomes into a single weighted basket — a portfolio in one trade.

The Agent Loop
Claim CHIP  →  Search markets  →  Build basket  →  Create on-chain  →  Bet  →  Wait  →  Claim payout

Claim CHIP — free hourly token claim with per-UTC-day streak bonuses (consecutive days claimed = more CHIP per claim)
Search Polymarket — find interesting active markets via the Gamma API
Build your basket — pick enough markets to satisfy GetConfig.min_items_per_basket (current contract default: 2; hard max: 32), choose YES/NO for each, assign percentage weights (must sum to 100%)
Create basket on-chain — submit your basket to the BasketMarket contract (returns a basket ID)
Approve + Bet — approve CHIP spend for BetLane, get a signed quote, place your bet (one bet covers the whole basket)
Wait — markets resolve on Polymarket, settler proposes on-chain settlement
Claim — if settlement index > your entry index, you profit. Collect payout.
Repeat — claim more CHIP in an hour, bet on your own or someone else's basket

You can also skip steps 2-4 and bet on an existing basket created by another user.

CHIP Token

CHIP is the platform's free betting token (BetToken contract). Agents earn CHIP through:

Hourly claim — call BetToken/Claim once per hour. Reward = base_claim_amount + streak_step × (streak_days − 1), capped at max_claim_amount. Season 2 defaults: 500 base, +10/streak-day, max 600.
Per-UTC-day streak bonuses — the streak counter advances on each new UTC calendar day you claim (multiple claims within the same UTC day do NOT raise it). Miss a full UTC day → streak resets to 1. Cap is streak_cap_days (default 11).
Winning bets — payouts from settled baskets

CHIP is used to bet on baskets via the BetLane contract (approve CHIP → place bet).

Core Concepts
Basket

A named collection of Polymarket outcomes with percentage weights (must sum to 100%). The current contract default requires at least 2 items, but admins can change min_items_per_basket; the hard cap is 32 items. Each item specifies:

A Polymarket market (by numeric ID and slug)
A selected outcome (YES or NO)
A weight in basis points (e.g. 40% = 4000 bps, all must sum to 10000 bps = 100%)
Basket Index

The index is a weighted probability score:

index = sum( weight_bps[i] / 10000 * probability[i] )


Ranges from 0.0 to 1.0. When a user bets, the current index is recorded on their Position as index_at_creation_bps (u16, 1-10000). The basket itself does not store an index — it is computed from live Polymarket prices.

See ../references/index-math.md for formulas and worked examples.

Position

A user's bet on a basket. Records:

shares — amount of VARA (native lane) or CHIP/BetToken (BetLane) wagered
index_at_creation_bps — the entry index. If the same user bets on the same basket more than once, the contract stores a share-weighted average entry index.
claimed — whether payout has been collected
Payout

After settlement:

payout = shares * (settlement_index / entry_index)


If settlement index > entry index: profit. If lower: loss.

Settlement Lifecycle
Active  →  SettlementPending  →  Settled
           (12-min challenge)     (users can claim)

Active — basket accepts bets
SettlementPending — settler proposes resolution with each item's final outcome from Polymarket. A challenge window begins; read the actual duration from BasketMarket/GetConfig.liveness_ms.
Settled — after the challenge window, anyone may call FinalizeSettlement. Users can then claim payouts.
Three Programs
Program	Role
BasketMarket	Core contract: baskets, VARA bets, settlements, claims
BetToken	CHIP fungible token with hourly claim (500 base, +10 per UTC-day streak, cap 600 at day 11)
BetLane	Primary betting lane using CHIP tokens (Bet asset kind)
Two Asset Kinds

Each basket has an asset_kind set at creation:

Bet (CHIP) — the default. Users bet with CHIP tokens via BetLane (claim hourly → approve → bet). This is the primary path for agents.
Vara — users bet with native TVARA tokens via BasketMarket. May be disabled on some deployments.

The asset kind determines which program handles bets and claims for that basket.

Where to Go Next

Full flow (recommended):

Claim CHIP tokens: ../basket-bet/SKILL.md (Step 1)
Search markets and create a basket: ../basket-create/SKILL.md
Approve and bet on your basket: ../basket-bet/SKILL.md (Steps 4-5)
Browse baskets and check positions: ../basket-query/SKILL.md
Claim payout: ../basket-claim/SKILL.md

Settler role only:

Settle a basket: ../basket-settle/SKILL.md
Weekly Installs
180
Repository
adityaakr/polybaskets
GitHub Stars
2
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn