---
rating: ⭐⭐
title: polymarket-knowledge
url: https://skills.sh/cyl19970726/poly-sdk/polymarket-knowledge
---

# polymarket-knowledge

skills/cyl19970726/poly-sdk/polymarket-knowledge
polymarket-knowledge
Installation
$ npx skills add https://github.com/cyl19970726/poly-sdk --skill polymarket-knowledge
SKILL.md
Polymarket Knowledge
Overview

Comprehensive reference for Polymarket CLOB API integration, focusing on order management and real-time event handling.

Quick Reference
Order Types
Type	Behavior	Use Case
GTC	Good Till Cancelled	Maker orders, liquidity provision
GTD	Good Till Date	Time-limited orders
FOK	Fill Or Kill	Must fill completely or cancel
FAK	Fill And Kill	Fill what you can, cancel rest
Order Requirements
Minimum order value: $1 USDC
Minimum shares: 5
Tick size: 0.01 (prices must be 0.01, 0.02, ... 0.99)
Order State Machine

See references/order-state-machine.md for complete state diagram and transitions.

States: PENDING → OPEN → PARTIALLY_FILLED → FILLED/CANCELLED/EXPIRED

API Status Mapping:

live → OPEN
matched (partial) → PARTIALLY_FILLED
matched (full) → FILLED
delayed → PENDING
cancelled → CANCELLED
expired → EXPIRED
WebSocket Events

See references/websocket-events.md for field mappings and examples.

Key Endpoints:

Market: wss://ws-subscriptions-clob.polymarket.com/ws/market
User: wss://ws-subscriptions-clob.polymarket.com/ws/user (authenticated)

USER_ORDER Event Types: PLACEMENT, UPDATE, CANCELLATION USER_TRADE Statuses: MATCHED, MINED, CONFIRMED, RETRYING, FAILED

Common Pitfalls
Wrong field names: API uses matched_amount not matched_size, size_matched not matched_size
Wrong endpoint: USER events require /ws/user, not /ws/market
USDC type: Polymarket uses USDC.e (bridged), not native USDC
Resources
references/order-state-machine.md - State transitions and validation
references/websocket-events.md - WebSocket field mappings
references/api-field-mappings.md - API response field reference
Weekly Installs
28
Repository
cyl19970726/poly-sdk
GitHub Stars
1.3K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn