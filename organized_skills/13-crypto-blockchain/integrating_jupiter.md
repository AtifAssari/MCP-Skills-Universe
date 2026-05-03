---
rating: ⭐⭐
title: integrating-jupiter
url: https://skills.sh/jup-ag/agent-skills/integrating-jupiter
---

# integrating-jupiter

skills/jup-ag/agent-skills/integrating-jupiter
integrating-jupiter
Installation
$ npx skills add https://github.com/jup-ag/agent-skills --skill integrating-jupiter
SKILL.md
Jupiter API Integration

Single skill for all Jupiter APIs, optimized for fast routing and deterministic execution.

Base URL: https://api.jup.ag Auth: x-api-key from portal.jup.ag (required for Jupiter REST endpoints)

Use/Do Not Use

Use when:

The task requires choosing or calling Jupiter endpoints.
The task involves swap, lending, perps, orders, pricing, portfolio, send, studio, lock, or routing.
The user needs debugging help for Jupiter API calls.

Do not use when:

The task is generic Solana setup with no Jupiter API usage.
The task is UI-only with no API behavior decisions.
The agent context is not DeFi/crypto (generic triggers like buy, sell, trade assume a DeFi domain).

Triggers: swap, quote, gasless, best route, buy, sell, trade, convert, token exchange, jupiter api, jup.ag, ultra, metis, ultra swap, ultra api, ultra-api.jup.ag, lend, borrow, earn, yield, apy, deposit, liquidation, perps, leverage, long, short, position, futures, margin trading, limit order, trigger, price condition, dca, recurring, scheduled swaps, token metadata, token search, verification, shield, price, valuation, price feed, portfolio, positions, holdings, prediction markets, market odds, event market, invite transfer, send, clawback, create token, studio, claim fee, vesting, distribution lock, unlock schedule, dex integration, rfq integration, routing engine, status page, health check, service health, accumulate, auto-buy

Developer Quickstart
import { Connection, Keypair, VersionedTransaction } from '@solana/web3.js';

const API_KEY = process.env.JUPITER_API_KEY!;  // from portal.jup.ag
if (!API_KEY) throw new Error('Missing JUPITER_API_KEY');
const BASE = 'https://api.jup.ag';
const headers = { 'x-api-key': API_KEY };

async function jupiterFetch<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${BASE}${path}`, {
    ...init,
    headers: { ...headers, ...init?.headers },
  });
  if (res.status === 429) throw { code: 'RATE_LIMITED', retryAfter: Number(res.headers.get('Retry-After')) || 10 };
  if (!res.ok) {
    const raw = await res.text();
    let body: any = { message: raw || `HTTP_${res.status}` };
    try {
      body = raw ? JSON.parse(raw) : body;
    } catch {
      // keep text fallback body
    }
    throw { status: res.status, ...body };
  }
  return res.json();
}

// Sign and send any Jupiter transaction
async function signAndSend(
  txBase64: string,
  wallet: Keypair,
  connection: Connection,
  additionalSigners: Keypair[] = []
): Promise<string> {
  const tx = VersionedTransaction.deserialize(Buffer.from(txBase64, 'base64'));
  tx.sign([wallet, ...additionalSigners]);
  const sig = await connection.sendRawTransaction(tx.serialize(), {
    maxRetries: 0,
    skipPreflight: true,
  });
  return sig;
}

Intent Router (first step)
User intent	API family	First action
Swap/quote	Swap	GET /swap/v2/order -> sign -> POST /swap/v2/execute
Lend/borrow/yield	Lend	POST /lend/v1/earn/deposit or /withdraw
Leverage/perps	Perps	On-chain via Anchor IDL (no REST API yet)
Limit orders	Trigger	JWT auth -> POST /trigger/v2/orders/price
DCA/recurring buys	Recurring	POST /recurring/v1/createOrder -> sign -> POST /recurring/v1/execute
Token search	Tokens	GET /tokens/v2/search?query={mint}
Token verification/metadata update	Use jupiter-vrfd skill	Defer — not handled by this skill
Price lookup	Price	GET /price/v3?ids={mints}
Portfolio/positions	Portfolio	GET /portfolio/v1/positions/{address}
Prediction market integration	Prediction Markets	GET /prediction/v1/events -> POST /prediction/v1/orders
Invite send/clawback	Send	POST /send/v1/craft-send -> sign -> send to RPC
Token creation/fees	Studio	POST /studio/v1/dbc-pool/create-tx -> upload -> submit
Vesting/distribution	Lock	On-chain program LocpQgucEQHbqNABEYvBvwoxCPsSbG91A1QaQhQQqjn
DEX/RFQ integration	Routing	Choose DEX (AMM trait) vs RFQ (webhook) path
API Playbooks

Use each block as a minimal execution contract. Fetch the linked refs for full request/response shapes, TypeScript interfaces, and parameter details.

Swap
Base URL: https://api.jup.ag/swap/v2
Triggers: swap, quote, gasless, best route
Fee: Variable by pair — 0 bps (Jupiter tokens/pegged), 2 bps (SOL-Stable), 5 bps (LST-Stable), 10 bps (most pairs), 50 bps (tokens < 24h). Referral fees: 50-255 bps (Jupiter retains 20%).
Rate Limit: 50 req/10s base, scales with 24h execute volume (see Rate Limits)
Endpoints: /order (GET), /execute (POST), /build (GET, Metis-only raw instructions)
Routing: 4 routers compete — Metis (API value: iris), JupiterZ (jupiterz), Dflow (dflow), OKX (okx). Response mode field: "ultra" (all routers, default params) or "manual" (restricted by optional params). /build uses Metis only.
Gasless: Three paths — automatic (Jupiter-covered), JupiterZ (MM-covered), integrator-payer (payer param, Metis-only routing). Eligibility varies by balance, trade size, and parameters used. See Gasless docs for current thresholds and disqualifying params.
Gotchas: Signed payloads have ~2 min TTL. Transactions are immutable after receipt. Split order/execute in code and logging. Re-quote before execution when conditions may have changed. referralAccount/referralFee/receiver disable JupiterZ only (Metis/Dflow/OKX remain). payer reduces routing to Metis only (per gasless docs; routing docs group all four as disabling JupiterZ but do not itemize the additional Dflow/OKX restriction). /build transactions cannot use /execute — self-manage via RPC.
Migrating from an older integration? Use the jupiter-swap-migration skill.
Refs: Overview | Order & Execute | Build | Fees | Routing | Gasless | Migration | OpenAPI

Common error codes returned by /swap/v2/execute with recommended actions:

Code	Category	Meaning	Retryable	Action
0	Success	Transaction confirmed	—	—
-1	Execute	Missing/expired cached order	Yes	Re-quote and retry
-2	Execute	Invalid signed transaction	No	Fix transaction signing
-3	Execute	Invalid message bytes	No	Fix serialization
-1000	Aggregator	Failed landing attempt	Yes	Re-quote with adjusted params
-1001	Aggregator	Unknown error	Yes	Retry with backoff
-1002	Aggregator	Invalid transaction	No	Fix transaction construction
-1003	Aggregator	Transaction not fully signed	No	Ensure all required signers
-1004	Aggregator	Invalid block height	Yes	Re-quote (stale blockhash)
-2000	RFQ	Failed landing	Yes	Re-quote and retry
-2001	RFQ	Unknown error	Yes	Retry with backoff
-2002	RFQ	Invalid payload	No	Fix request payload
-2003	RFQ	Quote expired	Yes	Re-quote and retry
-2004	RFQ	Swap rejected	Yes	Re-quote, possibly different route
429	Rate limit	Rate limited	Yes	Exponential backoff, wait 10s window
Lend
Base URL: https://api.jup.ag/lend/v1
Triggers: lend, borrow, earn, liquidation
Programs: Earn jup3YeL8QhtSx1e253b2FDvsMNC87fDrgQZivbrndc9, Borrow jupr81YtYssSyPt8jbnGuiWon5f6x9TcDEFxYe3Bdzi
SDK: @jup-ag/lend (TypeScript)
Endpoints: /earn/deposit (POST), /earn/withdraw (POST), /earn/mint (POST), /earn/redeem (POST), /earn/deposit-instructions (POST), /earn/withdraw-instructions (POST), /earn/tokens (GET), /earn/positions (GET), /earn/earnings (GET)
Gotchas: Recompute account state before each state-changing action. Encode risk checks (health factors, liquidation boundaries) as preconditions. All deposit/withdraw/mint/redeem return base64 unsigned VersionedTransaction.
For SDK-level integration with @jup-ag/lend and @jup-ag/lend-read, use the jupiter-lend skill.
Refs: Overview | Earn | SDK | OpenAPI
Perps
Status: API is work-in-progress. No REST endpoints yet. Interact on-chain via Anchor IDL.
Triggers: perps, leverage, long, short, position
Community SDK: github.com/julianfssen/jupiter-perps-anchor-idl-parsing
Gotchas: Max 9 simultaneous positions: 3 long (SOL, wETH, wBTC) + 6 short (3 tokens x 2 collateral USDC/USDT). Validate margin/leverage against account model.
Refs: Overview | Position account | Position request
Trigger (Limit Orders)
Base URL: https://api.jup.ag/trigger/v2
Triggers: limit order, trigger, price condition
Min order: 10 USD equivalent
Auth: Dual-auth — x-api-key (all requests) + Authorization: Bearer <jwt> (order mutations). JWT obtained via challenge-response: POST /auth/challenge → sign challenge with wallet → POST /auth/verify → receive token. JWT expiry does NOT affect open orders — they continue executing.
Endpoints: /auth/challenge (POST, body: walletPubkey + type), /auth/verify (POST, body: type + walletPubkey + base58 signature), /vault (GET), /vault/register (GET), /deposit/craft (POST), /orders/price (POST create, PATCH update), /orders/price/cancel/{orderId} (POST, initiates withdrawal), /orders/price/confirm-cancel/{orderId} (POST, submits signed withdrawal + cancelRequestId), /orders/history (GET, wallet implicit via JWT)
Order types: single (one directional trigger), oco (take-profit + stop-loss pair), otoco (entry trigger + OCO). triggerCondition: "above" or "below".
Architecture: Off-chain custodial vault (Privy) per wallet. Orders invisible on-chain until execution — MEV-resistant. Triggers on USD price (not pool rate ratios). Partial fills supported.
Gotchas: Order creation is 3 steps — GET /vault/register (register if new), POST /deposit/craft (returns transaction + requestId), sign deposit tx, then POST /orders/price with depositRequestId + depositSignedTx. Cancellation is two-step — POST /cancel/{orderId} returns transaction + requestId; sign, then POST /confirm-cancel/{orderId} with signedTransaction + cancelRequestId. Response field is id (not orderId).
Refs: Overview | Create order | Order history | Manage orders | OpenAPI
Recurring (DCA)
Base URL: https://api.jup.ag/recurring/v1
Triggers: dca, recurring, scheduled swaps
Fee: 0.1% on all recurring orders
Constraints: Min 100 USD total, min 2 orders, min 50 USD per order
Pagination: 10 orders per page
Endpoints: /createOrder (POST), /cancelOrder (POST), /execute (POST), /getRecurringOrders (GET)
Gotchas: Token-2022 NOT supported. Use params.time for order scheduling; price-based ordering is not supported.
Refs: Overview | Create | Get orders | Best Practices | OpenAPI
Tokens
Base URL: https://api.jup.ag/tokens/v2
Triggers: token metadata, token search, shield
Endpoints: /search?query={q} (GET, comma-separate mints, max 100), /tag?query={tag} (GET, verified or lst), /{category}/{interval} (GET, categories: toporganicscore, toptraded, toptrending; intervals: 5m, 1h, 6h, 24h), /recent (GET)
Gotchas: Use mint address as primary identity; treat symbol/name as convenience. Surface audit.isSus and organicScore in UX.
Refs: Overview | Token info v2 | OpenAPI
Price
Base URL: https://api.jup.ag/price/v3
Triggers: price, valuation, price feed
Limit: Max 50 mint IDs per request
Endpoints: /price/v3?ids={mints} (GET, comma-separated)
Gotchas: Tokens with unreliable pricing return null or are omitted (not an error). Fail closed on missing/low-confidence data for safety-sensitive actions. Use confidenceLevel field.
Refs: Overview | Price v3 | OpenAPI
Portfolio
Base URL: https://api.jup.ag/portfolio/v1
Status: Beta — Jupiter platforms only
Triggers: portfolio, positions, holdings
Endpoints: /positions/{address} (GET), /positions/{address}?platforms={ids} (GET), /platforms (GET), /staked-jup/{address} (GET)
Gotchas: Treat empty positions as valid state. Response is beta — normalize into stable internal schema. Element types: multiple, liquidity, trade, leverage, borrowlend.
Refs: Overview | Jupiter positions | OpenAPI
Prediction Markets
Base URL: https://api.jup.ag/prediction/v1
Status: Beta (breaking changes possible)
Geo-restricted: US and South Korea IPs blocked
Price convention: 1,000,000 native units = $1.00 USD
Triggers: prediction markets, market odds, event market
Deposit mints: JupUSD (JuprjznTrTSp2UFa3ZBUFgwdAmtZCq4MQCwysN55USD), USDC
Endpoints: /events (GET), /events/search (GET), /markets/{marketId} (GET), /orderbook/{marketId} (GET), /orders (POST), /orders/status/{pubkey} (GET), /positions (GET), /positions/{pubkey} (DELETE), /positions/{pubkey}/claim (POST), /history (GET), /leaderboards (GET)
Gotchas: Check position.claimable before claiming. Winners get $1/contract.
Refs: Overview | Events | Positions | OpenAPI
Send
Base URL: https://api.jup.ag/send/v1
Status: Beta
Triggers: invite transfer, send, clawback
Supported tokens: SOL, USDC, memecoins
Endpoints: /craft-send (POST), /craft-clawback (POST), /pending-invites (GET), /invite-history (GET)
Gotchas: Dual-sign requirement — sender + recipient keypair (derived from invite code). Claims only via Jupiter Mobile (no API claiming). Never expose invite codes.
Refs: Overview | Invite code | Craft send | OpenAPI
Studio
Base URL: https://api.jup.ag/studio/v1
Status: Beta
Triggers: create token, studio, claim fee
Endpoints: /dbc-pool/create-tx (POST), /dbc-pool/submit (POST, multipart/form-data), /dbc-pool/addresses/{mint} (GET), /dbc/fee (POST), /dbc/fee/create-tx (POST)
Flow: create-tx -> upload image to presigned URL -> upload metadata to presigned URL -> sign -> submit via /dbc-pool/submit
Gotchas: Must submit via /dbc-pool/submit (not externally) for token to get a Studio page on jup.ag. Error codes: 403 = not authorized for pool, 404 = proxy account not found.
Refs: Overview | Create token | Claim fee | OpenAPI
Lock
Program ID: LocpQgucEQHbqNABEYvBvwoxCPsSbG91A1QaQhQQqjn
Triggers: vesting, distribution lock, unlock schedule
Integration: On-chain program only (no REST API)
Source: github.com/jup-ag/jup-lock
UI: lock.jup.ag
Security: Audited by OtterSec and Sec3
Gotchas: No REST API. Use instruction scripts from the repo's cli/src/bin/instructions directory.
Refs: Lock overview
Routing
Triggers: dex integration, rfq integration, routing engine
Engines: Juno (meta-aggregator), Iris (multi-hop DEX routing, powers Swap API), JupiterZ (RFQ market maker quotes)
DEX Integration (into Iris): Free, no fees. Prereqs: code health, security audit, market traction. Implement jupiter-amm-interface crate. Critical: No network calls in implementation (accounts are pre-batched and cached). Ref impl: github.com/jup-ag/rust-amm-implementation
RFQ Integration (JupiterZ): Market makers host webhook at /jupiter/rfq/quote (POST, 250ms), /jupiter/rfq/swap (POST), /jupiter/rfq/tokens (GET). Reqs: 95% fill rate, 250ms response, 55s expiry. SDK: github.com/jup-ag/rfq-webhook-toolkit
Market Listing: Instant routing for tokens < 30 days old. Normal routing (checked every 30 min) requires < 30% loss on $500 round-trip OR < 20% price impact comparing $1k vs $500.
Refs: Overview | DEX integration | RFQ integration | Market listing
Rate Limits

Swap API (dynamic, volume-based):

24h Execute Volume	Requests per 10s window
$0	50
$10,000	51
$100,000	61
$1,000,000	165

Quotas recalculate every 10 minutes. Pro plan does NOT increase Swap API limits.

Other APIs: Managed at portal level. Check portal rate limits.

On HTTP 429: Exponential backoff with jitter: delay = min(baseDelay * 2^attempt + random(0, jitter), maxDelay). Wait for 10s sliding window refresh. Do NOT burst aggressively.

Production Hardening
Auth: Fail fast if x-api-key is missing or invalid.
Timeouts: 5s for quotes, 30s for executions, plus total operation timeout.
Retries: Only transient/network/rate-limit failures with exponential backoff + jitter.
Idempotency: Swap /execute accepts same signedTransaction + requestId for up to 2 min without duplicate execution.
Validation: Validate mint addresses, amount precision, and wallet ownership before calls.
Safety: Enforce slippage and max-amount guardrails from app config.
Observability: Log requestId, API family, endpoint, latency, status, and error code.
UX resilience: Return actionable states (retry, adjust params, insufficient balance, rate limited).
Consistency: Reconcile async states (submitted vs confirmed vs failed) before final user success.
Freshness: Re-fetch referenced docs when behavior differs from expected flow.
Integration Best Practices
Start from the API-specific overview before coding endpoint calls.
Enforce auth as a hard precondition for every request. Ref: Portal setup
Design retry logic around documented rate-limit behavior, not fixed assumptions. Ref: Rate limits
Map all non-success responses to typed app errors using documented response semantics. Ref: API responses
For order-based products (Swap/Trigger/Recurring), separate create/execute/retrieve phases in code and logs.
Treat network/service health as part of runtime behavior (degrade gracefully). Ref: Status page
Cross-Cutting Error Pattern
interface JupiterResult<T> {
  ok: boolean;
  result?: T;
  error?: { code: string | number; message: string; retryable: boolean };
}

async function jupiterAction<T>(action: () => Promise<T>): Promise<JupiterResult<T>> {
  try {
    const result = await action();
    return { ok: true, result };
  } catch (error: any) {
    const code = error?.code ?? error?.status ?? 'UNKNOWN';

    // Rate limit — retry with backoff
    if (code === 429 || code === 'RATE_LIMITED') {
      return { ok: false, error: { code: 'RATE_LIMITED', message: 'Rate limited', retryable: true } };
    }

    // Swap execute errors (negative codes)
    if (typeof code === 'number' && code < 0) {
      const retryable = [-1, -1000, -1001, -1004, -2000, -2001, -2003, -2004].includes(code);
      return { ok: false, error: { code, message: error?.error ?? 'Execute failed', retryable } };
    }

    // Program errors (positive codes like 6001 = slippage)
    if (typeof code === 'number' && code > 0) {
      return { ok: false, error: { code, message: error?.error ?? 'Program error', retryable: false } };
    }

    return { ok: false, error: { code, message: error?.message ?? 'UNKNOWN_ERROR', retryable: false } };
  }
}

async function withRetry<T>(action: () => Promise<T>, maxRetries = 3): Promise<T> {
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    const result = await jupiterAction(action);
    if (result.ok) return result.result!;
    if (!result.error?.retryable || attempt === maxRetries) throw result.error;
    const delay = Math.min(1000 * 2 ** attempt + Math.random() * 500, 10000);
    await new Promise(r => setTimeout(r, delay));
  }
  throw new Error('Retry exhausted');
}

Complete Working Examples

Production-ready code snippets. Each example uses the jupiterFetch helper from the sections above; apply withRetry around execute calls in production.

Swap: End-to-End — Order -> sign -> execute -> confirm flow
Lend: USDC Deposit — Deposit into Jupiter Lend earn pool
Trigger: Limit Order — Create and execute a limit order
Price: Multi-Token Lookup — Fetch prices with confidence filtering
Fresh Context Policy

Always fetch the freshest context from referenced docs/specs before executing a playbook.

Resolve intent with Intent Router.
Before coding, fetch the playbook's linked refs (overview + API-specific docs).
If needed for validation or ambiguity, fetch the OpenAPI spec.
Treat fetched docs as source of truth over cached memory.
If fetched docs conflict with this file, follow fetched docs and note the mismatch.
If docs cannot be fetched, state that context is stale/unverified and continue with best-known guidance.
Keep auth invariant: x-api-key is required for Jupiter REST endpoints (not on-chain-only flows like Perps/Lock).
Operational References
Portal setup — API key configuration
Rate limits — Global rate limit policy
Swap routing — Router competition and parameter impact
API responses — Response format standards
Swap order & execute — Detailed error codes and response format
Status page — Service health
Documentation sitemap — Full docs index
Tool Kits — Plugin, Wallet Kit, Referral Program
Weekly Installs
336
Repository
jup-ag/agent-skills
GitHub Stars
62
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn