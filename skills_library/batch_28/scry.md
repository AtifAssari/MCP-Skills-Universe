---
title: scry
url: https://skills.sh/exopriors/skills/scry
---

# scry

skills/exopriors/skills/scry
scry
Installation
$ npx skills add https://github.com/exopriors/skills --skill scry
SKILL.md
Scry Skill

Scry gives you read-only SQL access to the ExoPriors public corpus via a single HTTP endpoint. You write Postgres SQL against a curated scry.* schema and get JSON rows back. There is no ORM, no GraphQL, no pagination token -- just SQL. Use GET /v1/stats or GET /v1/scry/context for live corpus counts instead of relying on static numbers in docs.

Skill generation: 2026041201

A) When to use / not use

Use this skill when:

Searching, filtering, or aggregating content across the ExoPriors corpus
Running lexical (BM25) or hybrid searches
Exploring author networks, public cross-platform identities, or publication patterns
Navigating the OpenAlex academic graph (authors, citations, institutions, concepts)
Creating shareable artifacts from query results
Emitting structured agent judgements about entities or external references

Do NOT use this skill when:

The user wants semantic/vector search composition or embedding algebra (use the scry-vectors skill)
The user wants LLM-based reranking (use the scry-rerank skill)
The user is querying their own local database
B) Golden Rules

Context handshake first. At session start, call GET /v1/scry/context?skill_generation=2026041201. This endpoint is public; you do not need a key for the handshake itself. Use the returned offerings block for the current product summary budgets, canonical env var, default skill, and specialized skill catalog. Read offerings.portable_entry as the canonical /scry flow: context -> schema -> route -> query. Read offerings.payments as the payment-role contract: it tells you which protocols are live vs planned, which ones fund the reusable prepaid ledger, which ones are hot-path query payment vs delegated authorization, and which authenticated control-plane endpoints expose reusable instruments and stored mandate artifacts. Read offerings.accelerator_families and offerings.relation_accelerator_policies as the accelerator contract: they tell you which relations are canonical defaults versus optional convenience helpers, which tracked objects gate them, and what fallback surfaces to use. If you need a concise shareable bootstrap prompt for another agent, use offerings.public_agent_prompt.copy_text instead of paraphrasing your own. If you need deeper docs, use offerings.canonical_doc_path, each skill's repo_path, and reference_paths instead of guessing where the maintained docs live. If you cache descriptive bootstrap context across turns or sessions, also track surface_context_generation and refresh when it changes. Read lexical_search.status, lexical_search.status_basis, and lexical_search.last_known_status as well. If status_basis is observability_lag and last_known_status is healthy, global scry.search* is still the default unless the task is recency-critical or results look wrong. Pivot to source-local scry.* / mv_* surfaces or semantic retrieval when the confirmed status is rebuilding, degraded, or unavailable, or when a stale snapshot's last known status is not healthy. If you are validating deploy/runtime conformance from this repo rather than just using the surface, run the canonical proof command:

cd src/api
SCRY_API_KEY=... cargo run --features cli --bin scry-contract-audit -- --output json


This proof is strict by default: any non-pass manifest drift or bounded probe failure exits non-zero. The default agent-experience-e2e run now includes the same manifest conformance audit after signed-in continuity. If should_update_skill=true, tell the user to run npx skills update. If the response reports client_skill_generation: null while you're using packaged skills, or if local instructions still mention legacy ExoPriors hostnames or legacy console routes, treat the install as stale and ask the user to run npx skills update before more debugging.

Schema first. ALWAYS call GET /v1/scry/schema before writing SQL. Never guess column names or types. The schema endpoint returns live column metadata and row-count estimates for every view.

If the task targets publication-first Parquet datasets rather than the live Scry SQL corpus, call GET /v1/scry/datasets, inspect GET /v1/scry/datasets/{id}, and then use POST /v1/scry/datasets/{id}/resolve before writing SQL. The resolve response gives you short-lived DuckDB-ready HTTPS URLs and bootstrap SQL.

Check operational status when search looks wrong. If lexical search, materialized-view freshness, or corpus behavior seems off, call GET /v1/scry/index-view-status with any Scry key before assuming the query or schema is wrong. If /v1/scry/context marks a relation as fast_path or conditional, do not rely on it until the required tracked objects are healthy.

Clarify ambiguous intent before broad or likely-expensive queries. If the request is vague ("search Reddit for X", "find things about Y"), ask one short clarification question about the goal/output format before running expensive SQL.

Start with a cheap probe. Before any query likely to run >5s, run GET /v1/scry/price plus /v1/scry/estimate and/or a tight exploratory query (LIMIT 20 plus scoped source/window filters), then scale only after confirming relevance. Use GET /v1/scry/price/history when you need to know whether the current base fee is a spike or the recent norm; it defaults to the trailing 6 hours and rejects windows wider than 24 hours.

Treat congested queries as budget-bounded. Scry queries are free unless there is congestion. When there is congestion, Scry reserves nanodollar credits up front and derives a runtime timeout from the authorized spend envelope. The runtime enforces that envelope with a live-burn watchdog first and a timeout fallback second. Lead with the simplified surface: use X-Scry-Budget as the primary per-query cost control, eager and patient as the two execution modes, and GET /v1/scry/account as the one-stop status check before or after broad or expensive query work. Use GET /v1/scry/pricing plus /v1/scry/estimate when you need the live cost details behind that surface. When acting under a stored delegated mandate, also send X-Scry-Subject-Agent: <agent-id> so Scry can apply the matching query_access mandate cap. Under congestion, eager mode uses uniform clearing: winners pay the epoch clearing price, not their full submitted maximum. The account's stored max_bid_multiplier from GET / PATCH /v1/scry/preferences still caps the effective eager bid before admission. Agents that prefer to wait can switch pricing_mode to patient, which keeps FIFO ordering and runs at base price when capacity opens. Use the payment_surface block in /v1/scry/pricing to distinguish live direct query payment (x402) and live account-funding rails (stripe_checkout, crypto_topup) from control-plane / future artifacts (stripe_acp, ap2, visa_tap, mastercard_agent_pay). Read payment_surface.card_funding and payment_surface.card_funding_read_order before assuming cards are either fully blocked or fully API-native; the contract is a one-time setup handoff, then API-only saved-method funding. When delegated funding or agent authorization matters, inspect GET /v1/billing/auto-topup, GET /v1/billing/payment-instruments, and GET /v1/billing/payment-mandates rather than assuming those artifacts are hidden inside the query surface. backward-compat note: older clients may still use X-Scry-Max-Cost, X-Scry-Max-Exposure, X-Scry-Bid, or pricing_mode: "dynamic" | "queue", but new integrations should lead with X-Scry-Budget and eager / patient.

Choose lexical SQL vs semantic explicitly. Use scry.search_federated(...), source-native scry.search_* helpers, or other lexical SQL when the user wants fast provenance-bearing first results. Widen into broader SQL when you need joins, aggregation, or full control over filters. For conceptual intent ("themes", "things like", "similar to"), route to scry-vectors first, then optionally hybridize.

LIMIT always. Every query MUST include a LIMIT clause. Max 10,000 rows. Queries without LIMIT are rejected by the SQL validator.

Prefer canonical surfaces with tight filters. scry.entities is large enough that you should not scan it blindly. Use scry.search* for lexical retrieval, scry.chunk_embeddings for chunk-level semantic retrieval, scry.entity_embeddings or scry.entities_with_embeddings only when you want one entity-level vector row per entity, scry.embedding_coverage to inspect public vs staged vs ready source/kind coverage, source-local scry.*_embeddings views when you need the exact semantic owner table, and source-native tables or aliases such as scry.hackernews, scry.wikipedia, scry.pubmed, scry.repec, scry.kalshi, scry.nih_reporter, scry.govinfo_crec, scry.offshoreleaks, scry.openalex, scry.bluesky, scry.reddit_posts, scry.forum_posts, scry.huggingface, scry.huggingface_papers, scry.huggingface_collections, scry.huggingface_discussions, scry.huggingface_accounts, scry.huggingface_models, scry.huggingface_datasets, scry.huggingface_spaces, scry.huggingface_repo_text_artifacts, scry.huggingface_paper_artifacts, scry.kalshi_markets, scry.nih_reporter_projects, scry.govinfo_crec_granules, scry.hackernews_items, scry.wikipedia_articles, scry.pubmed_papers, scry.repec_records, scry.openalex_works, scry.bluesky_posts, scry.mailing_list_messages, scry.openlibrary_*, scry.stackexchange, scry.caselaw, scry.gutenberg_books, scry.wikidata_items, scry.wikidata_claims, and scry.kl3m when a corpus no longer lives canonically in scry.entities. Reach for a specific mv_* convenience view only when /v1/scry/schema confirms it is healthy and useful for the task.

For Hugging Face specifically, prefer scry.search_huggingface() when you need one discovery-first entry point across repos, artifacts, papers, collections, discussions, accounts, and paper-artifact hops.

For package registry search, use scry.search_packages(query, registries, limit_n) for cross-registry discovery across npm, PyPI, crates.io, RubyGems, Go modules, NuGet, Maven, Hex.pm, Packagist, pub.dev, CocoaPods, conda-forge, JSR, and Homebrew. Individual per-registry functions are also available (see schema guide).

For cross-platform social search, use scry.social_search(query, mode, limit_n) which searches Twitter, Bluesky, StackExchange, and mailing lists in one call.

Cross-table composition is normal. If the best records live in multiple source-native tables, combine them in one SQL statement with CTEs, UNION ALL, and joins through scry.source_records. This is the intended contract, not a workaround.

Filter dangerous content. On scry.entities, scry.entities_with_embeddings, and scry.chunk_embeddings, include WHERE content_risk IS DISTINCT FROM 'dangerous' unless the user explicitly asks for unfiltered results. If a source-native view does not expose content_risk, join it to scry.entities on entity_id and filter there. Dangerous content contains adversarial prompt-injection content.

Raw SQL, not JSON. POST /v1/scry/query takes Content-Type: text/plain with raw SQL in the body. Not JSON-wrapped SQL.

File rough edges promptly. If Scry blocks the task, misses an obvious result set, or exposes a rough edge, submit a brief note to POST /v1/feedback?feedback_type=suggestion|bug|other&channel=scry_skill using Content-Type: text/plain by default (text/markdown also works). Do not silently work around it. Logged-in users can review their submissions with GET /v1/feedback.

For full query limits, timeout policies, and degradation strategies, see Shared Guardrails.

B.1 API Key Setup (Canonical)

Recommended default for less-technical users: in the directory where you launch the agent, store SCRY_API_KEY in .env so skills and copied prompts use the same place. Canonical key naming for this skill:

Env var: SCRY_API_KEY
Anonymous bootstrap key format: scry_anon_* from POST /v1/scry/anonymous-key
Personal key format: personal Scry API key with Scry access
Recommended anonymous client header: X-Scry-Client-Tag: <short-stable-tag>

Durable machine bootstrap paths:

Operator-provisioned (default for non-wallet agents): a signed-in human operator calls POST /v1/auth/api-keys, creates a Scry-scoped key, hands the secret to the agent, and the agent stores it in SCRY_API_KEY.
Wallet-native: POST /v1/auth/agent/signup for agents that already have an EVM wallet; the response returns a session token plus API key.

Both paths end with the same Authorization: Bearer $SCRY_API_KEY contract.

printf '%s\n' 'SCRY_API_KEY=<your key>' >> .env
set -a && source .env && set +a


Verify:

echo "$SCRY_API_KEY"


Anonymous bootstrap flow when the user wants immediate public access without signup:

CLIENT_TAG="${SCRY_CLIENT_TAG:-dev-laptop}"
ANON_KEY="$(curl -s https://api.scry.io/v1/scry/anonymous-key -X POST -H "X-Scry-Client-Tag: $CLIENT_TAG" | python3 -c 'import json,sys; print(json.load(sys.stdin)[\"api_key\"])')"
curl -s https://api.scry.io/v1/scry/schema \
  -H "Authorization: Bearer $ANON_KEY" \
  -H "X-Scry-Client-Tag: $CLIENT_TAG"
curl -s https://api.scry.io/v1/scry/query \
  -H "Authorization: Bearer $ANON_KEY" \
  -H "X-Scry-Client-Tag: $CLIENT_TAG" \
  -H "Content-Type: text/plain" \
  --data "SELECT 1 LIMIT 1"


Use this for fast trial access only. The anonymous bootstrap lane is intentionally generous for the first few queries and then degrades. For sustained usage, prefer a personal Scry API key. Keep the same X-Scry-Client-Tag value on the same device when staying anonymous so the backend can distinguish a real first-use session from abuse behind shared IPs. The same anonymous key can also call POST /v1/scry/embed, GET /v1/scry/vectors, and DELETE /v1/scry/vectors/{name}. Those handles stay bound to the current anonymous session rather than a durable account namespace.

If using packaged skills, keep them current:

npx skills add exopriors/skills
npx skills update

B.1a Lexical SQL quickstart

Use lexical SQL helpers when the user wants fast first-pass discovery without building a larger query first.

curl -s https://api.scry.io/v1/scry/query \
  -H "Authorization: Bearer $SCRY_API_KEY" \
  -H "Content-Type: text/plain" \
  --data "SELECT * FROM scry.search_federated('mechanistic interpretability', NULL, NULL, 5, 2) LIMIT 5"


Use scry.search_federated(...) or a source-native scry.search_* helper for quick lexical discovery, then widen into broader SQL when you need joins, aggregation, or exact control.

B.1b x402 Query-Only Access

POST /v1/scry/query still supports standard x402, but it is now an explicit paid path rather than the default no-auth bootstrap path. Use x402 when the user already has an x402-capable client or wallet and only wants direct paid query execution. For public trial use, use POST /v1/scry/anonymous-key. For schema/context, shares, judgements, feedback, or repeated multi-endpoint usage, prefer a personal Scry API key.

The x402 flow is challenge-first. If x402 is enabled and the request has no Authorization header, the first unsigned POST /v1/scry/query returns 402 Payment Required with machine-readable payment requirements. When the caller also sends X-Scry-Budget, Scry asks the wallet to fund at least that budget (subject to the configured x402 base quantum). After settlement, the paid amount converts into reusable Scry credits on the shared ledger, so overpayment remains available for later queries instead of being lost.

If the agent already has an EVM wallet and wants wallet-native durable identity plus a reusable key, use POST /v1/auth/agent/signup first. If it does not have a wallet, have a signed-in operator create a Scry-scoped key via POST /v1/auth/api-keys and hand it to the agent. Both paths end with the same Bearer-key contract.

Minimal client shape:

import { wrapFetchWithPayment } from 'x402-fetch';

const paidFetch = wrapFetchWithPayment(fetch, walletClient);
const resp = await paidFetch('https://api.scry.io/v1/scry/query', {
  method: 'POST',
  headers: { 'content-type': 'text/plain' },
  body: 'SELECT 1 LIMIT 1',
});

B.1c Query Budgeting

When there is congestion, these are the key billing controls:

X-Scry-Budget: <nanodollars> is the primary per-query cost control. Send it on /v1/scry/estimate and /v1/scry/query when you want one number to bound the estimate check, runtime authorization, and eager-mode bid cap.
GET /v1/scry/account is the one-stop billing status check. It returns balance, current mode, max budget, today's spend/query count, live base fee, live utilization, and whether auto-topup is enabled.
GET /v1/scry/preferences returns the caller's persisted pricing_mode (eager or patient) and max_bid_multiplier.
PATCH /v1/scry/preferences updates pricing_mode and max_bid_multiplier. Use pricing_mode: "patient" when the user wants FIFO waiting at base price during congestion instead of bidding into the eager auction.
GET /v1/scry/price returns the live base_fee, utilization, load_pressure, recommended_max_fee, and current epoch metadata. Use it right before deciding whether to run now in eager mode or wait in patient.
GET /v1/scry/price/history returns sampled epoch_id / timestamp / base_fee / utilization history plus sampling metadata for large windows. If no bounds are provided it returns the trailing 6 hours, and requests wider than 24 hours are rejected.
GET /v1/scry/price/stream returns an SSE feed with price events at epoch cadence and ping keepalives while no new epoch arrives.
GET /v1/scry/spend returns the authenticated caller's own spend history: total_credits_spent, query_count, avg_cost_per_query, and recent per-query cost breakdowns.
GET /v1/scry/pricing returns the live query access contract (free_unless_congested), whether congestion pricing is currently active, the live compute rate, bandwidth rate, load multiplier, reservation headroom, bid thresholds, the congestion-admission auction contract, and the budget-enforcement contract.
GET /v1/scry/pricing also exposes the x402 base funding quantum and the fact that x402 funding now scales off X-Scry-Budget when that header is present.
GET /v1/scry/account returns the authenticated funding summary. Read funding.card_funding first when the question is "can this agent use cards right now?" because it makes the current card state explicit (requires_operator_setup, saved_method_ready, auto_topup_attention_required, auto_topup_active, or disabled) and lists the next endpoints to call.
Funding-control endpoints such as GET /v1/scry/account, POST /v1/billing/agent-topup, POST /v1/billing/payment-mandates, and PATCH /v1/billing/auto-topup require account or billing scope.
POST /v1/scry/estimate returns estimated_cost_nanodollars, suggested_reserve_nanodollars, authorized_exposure_nanodollars, exposure_timeout_ms, and a bid-adjusted upper-bound cost_breakdown.
POST /v1/scry/query?receipt=summary or ?receipt=full returns an optional execution receipt inline with the result. Use summary when you only need the stable ID, SQL fingerprint, and main cost/runtime facts; use full when you want the estimate, billing, execution, and structured security details in one object.
GET /v1/scry/query-receipts/{id} re-hydrates the durable query receipt for the authenticated caller from scry_query_log. Raw SQL is omitted by default; add ?include_sql=true when the owner explicitly needs the original statement back.
X-Scry-Subject-Agent: <agent-id> activates delegated query policy. If the authenticated account has a matching active query_access mandate, Scry applies that mandate's max_query_exposure as an additional cap and returns a delegated_authorization object. If not, /v1/scry/query fails with delegated_authorization_required.
Cards are a two-stage rail, not a zero-setup hot path.
POST /v1/billing/setup-payment-method creates a Stripe Checkout setup session that saves a card without charging it and returns setup_url for one operator browser visit. After completion, the card is persisted as a payment instrument and set as the default. This is the entry point for enabling Stripe-backed auto-topup and agent-topup.
POST /v1/billing/agent-topup charges the default stored payment instrument for a pricing tier amount, granting credits immediately. Designed for agent-initiated funding without browser interaction and requires only a saved payment method.
Recurring Stripe rescue is a separate opt-in that requires an active auto_topup mandate via POST /v1/billing/payment-mandates plus PATCH /v1/billing/auto-topup.
GET /v1/billing/auto-topup and PATCH /v1/billing/auto-topup control Stripe-backed replenishment into the same prepaid ledger. If enabled with a verified default Stripe payment method plus an active auto_topup mandate, /v1/scry/query gets one off-session topup attempt after an insufficient_credits reservation failure and then retries reservation once.
GET /v1/billing/auto-topup/eligibility explains why recurring saved-method funding is not yet ready when funding.card_funding.state reports auto_topup_attention_required.
GET /v1/billing/pricing returns available credit pricing tiers with id, usd_cents, credits (nanodollars), and display_label.
GET /v1/billing/payment-instruments lists saved payment methods.
Live funding rails are x402, Stripe saved-method funding, and crypto topup. stripe_acp, ap2, visa_tap, and mastercard_agent_pay are control-plane / future artifact layers, not interchangeable live funding rails.
In eager mode, uniform clearing means the charged priority fee comes from the lowest winning bid in the epoch, not from every winner's submitted max bid.
max_bid_multiplier clamps the effective eager bid before the request enters the auction.
Billable bandwidth uses the executor-tracked streamed row payload bytes, not the outer HTTP/JSON envelope. Full response-body size still matters for delivery limits and alerts.
backward-compat note: legacy clients may still send X-Scry-Max-Cost, X-Scry-Max-Exposure, X-Scry-Bid, or pricing_mode: "dynamic" | "queue". New integrations should lead with X-Scry-Budget, eager, patient, and GET /v1/scry/account.

Useful response headers from POST /v1/scry/query:

x-scry-cost: charged nanodollars for the completed query when congestion pricing applies
x-scry-receipt-id: stable execution-receipt id when receipt mode is enabled
x-scry-authorized-exposure: the hard exposure authorization applied to this run
x-scry-reserved: the reserved/pre-authorized nanodollar amount
x-scry-exposure-timeout-ms: exposure-derived runtime cutoff
x-scry-bid-accepted / x-scry-bid-charged: submitted max bid vs clearing-price multiplier actually charged
x-scry-admission / x-scry-admission-wait-ms: whether the request started immediately or through a congestion epoch, plus the admission wait
X-Scry-Base-Fee: current epoch base-fee multiplier used to price compute
X-Scry-Priority-Fee: congestion premium implied by the accepted clearing price
X-Scry-Compute-Units: normalized compute units charged for the query
X-Scry-Utilization: price-epoch utilization snapshot
X-Scry-Epoch: current price epoch id
X-Scry-Budget-Remaining: credits or free-tier budget remaining after a congestion-priced settlement

If a congestion-priced query runs into its spend envelope, the API returns 402 with query_exposure_exhausted. That is enforced by live runtime burn first, with the exposure timeout as fallback. The fix is to narrow the query or raise X-Scry-Budget, not to keep retrying the same request unchanged.

C) Quickstart

One end-to-end example: find recent high-scoring LessWrong posts about RLHF.

Step 1: Get dynamic context + update advisory
GET https://api.scry.io/v1/scry/context?skill_generation=2026041201
Authorization: Bearer $SCRY_API_KEY

Step 2: Get schema
GET https://api.scry.io/v1/scry/schema
Authorization: Bearer $SCRY_API_KEY

Step 3: Run query
POST https://api.scry.io/v1/scry/query
Authorization: Bearer $SCRY_API_KEY
Content-Type: text/plain

WITH hits AS (
  SELECT id FROM scry.search('RLHF reinforcement learning human feedback',
    kinds=>ARRAY['post'], limit_n=>100)
)
SELECT e.uri, e.title, e.original_author, e.original_timestamp, e.score
FROM hits h
JOIN scry.entities e ON e.id = h.id
WHERE e.source = 'lesswrong'
ORDER BY e.score DESC NULLS LAST, e.original_timestamp DESC
LIMIT 20


Response shape:

{
  "columns": ["uri", "title", "original_author", "original_timestamp", "score"],
  "rows": [["https://...", "My RLHF Post", "author", "2025-01-15T...", 142], ...],
  "row_count": 20,
  "duration_ms": 312,
  "truncated": false
}


Source-native cross-table example:

WITH hn AS (
  SELECT 'hackernews'::text AS source, hn_id::text AS external_id, score
  FROM scry.search_hackernews_items('interpretability', kinds => ARRAY['post'], limit_n => 20)
),
wiki AS (
  SELECT 'wikipedia'::text AS source, page_id::text AS external_id, score
  FROM scry.search_wikipedia_articles('interpretability', limit_n => 20)
),
hits AS (
  SELECT * FROM hn
  UNION ALL
  SELECT * FROM wiki
)
SELECT h.source, r.uri, r.title, h.score
FROM hits h
JOIN scry.source_records r
  ON r.source = h.source
 AND r.external_id = h.external_id
ORDER BY h.score DESC
LIMIT 20;

D) Decision Tree
User wants to search the ExoPriors corpus?
  |
  +-- Ambiguous / conceptual ask? --> Clarify intent first, then use
  |     scry-vectors for semantic search (optionally hybridize with lexical)
  |
  +-- By keywords/phrases? --> scry.search() (BM25 lexical over canonical content_text)
  |     +-- Specific forum?  --> join/filter `source` explicitly (or use a healthy source-local view if schema confirms it)
  |     +-- Reddit?          --> START with scry.reddit_subreddit_stats /
  |                              scry.reddit_clusters() / scry.reddit_embeddings
  |                              and trust /v1/scry/schema status before
  |                              using direct retrieval helpers
  |     +-- Large result?    --> scry.search_ids() (up to 2000 lexical IDs; join for fields)
  |
  +-- By structured filters (source, date, author)? --> Direct SQL on MVs
  |
  +-- By semantic similarity? --> (scry-vectors skill, not this one)
  |
  +-- Hybrid (keywords + semantic rerank)? --> scry.hybrid_search() or
  |     lexical CTE + JOIN scry.chunk_embeddings
  |
  +-- Author/people lookup? --> scry.actors, scry.people, scry.person_accounts
  |                            (conservative public account links)
  |
  +-- Academic graph (OpenAlex)? --> scry.openalex_find_authors(),
  |     scry.openalex_find_works(), etc. (see schema-guide.md)
  |
  +-- Bluesky / Twitter / Open Library text lookup? --> scry.search_bluesky_posts(),
  |     scry.search_twitter_posts(), scry.search_openlibrary_editions(),
  |     scry.search_openlibrary_works(), scry.search_openlibrary_authors()
  |
  +-- Need to share results? --> POST /v1/scry/shares
  |
  +-- Need to emit a structured observation? --> POST /v1/scry/judgements
  |
  +-- Scry blocked / missing obvious results? --> POST /v1/feedback

E) Recipes
E0. Context handshake + skill update advisory
curl -s "https://api.scry.io/v1/scry/context?skill_generation=2026041201" \
  -H "Authorization: Bearer $SCRY_API_KEY"


If response includes "should_update_skill": true, ask the user to run: npx skills update. If the response shows "client_skill_generation": null while the session is using packaged Scry skills, or if local instructions still point at legacy ExoPriors hostnames or legacy console routes, stop and ask the user to run npx skills update before deeper debugging. If response includes "lexical_search": {...}, read status, status_basis, and last_known_status together. When status = "stale" and status_basis = "observability_lag" with last_known_status = "healthy", global lexical search is still the default unless the task is recency-critical or the results look wrong. Prefer source-local scry.* surfaces or scry.entities_with_embeddings when the confirmed status is rebuilding, degraded, or unavailable, or when a stale snapshot's last known status is not healthy. Use /v1/scry/index-view-status for detailed live timing before blaming the query.

E0b. Submit feedback when Scry blocks the task
curl -s "https://api.scry.io/v1/feedback?feedback_type=bug&channel=scry_skill" \
  -H "Authorization: Bearer $SCRY_API_KEY" \
  -H "Content-Type: text/plain" \
  --data $'## What happened\n- Query: ...\n- Problem: ...\n\n## Why it matters\n- ...\n\n## Suggested fix\n- ...'


Success response includes a receipt id. Logged-in users can review their own submissions with:

curl -s "https://api.scry.io/v1/feedback?limit=10" \
  -H "Authorization: Bearer $SCRY_API_KEY"

E1. Lexical search (BM25)
WITH c AS (
  SELECT id FROM scry.search('your query here',
    kinds=>ARRAY['post'], limit_n=>100)
)
SELECT e.uri, e.title, e.original_author, e.original_timestamp
FROM c JOIN scry.entities e ON e.id = c.id
WHERE e.content_risk IS DISTINCT FROM 'dangerous'
LIMIT 50


Default kinds if omitted: ['post','paper','document','webpage','twitter_thread','grant']. scry.search() broadens once to kinds=>ARRAY['comment'] if that default returns 0 rows. Pass explicit kinds for strict scope (for example comment-only or tweet-only). For source scoping, join back to scry.entities and filter source explicitly. Healthy source-specific MVs can still be useful for source-native score fields such as base_score, but they are optional convenience slices rather than the default path.

E2. Reddit-specific discovery
SELECT subreddit, total_count, latest
FROM scry.reddit_subreddit_stats
WHERE subreddit IN ('MachineLearning', 'LocalLLaMA')
ORDER BY total_count DESC


For semantic Reddit retrieval over the embedding-covered subset, use scry.reddit_embeddings or scry.search_reddit_posts_semantic(...).

Direct retrieval helpers (scry.reddit_posts, scry.reddit_comments, scry.mv_reddit_*, scry.search_reddit_posts(...), scry.search_reddit_comments(...)) are currently degraded on the public instance. Check /v1/scry/schema status before using them.

E3. Source-filtered materialized view query
SELECT entity_id, uri, title, original_author, score, original_timestamp
FROM scry.arxiv_papers
WHERE original_timestamp >= '2025-01-01'
ORDER BY original_timestamp DESC
LIMIT 50


score is not the useful ranking axis for arXiv. Sort by original_timestamp, primary_category, or downstream citation proxies instead.

E4. Author activity across sources
SELECT e.source::text, COUNT(*) AS docs, MAX(e.original_timestamp) AS latest
FROM scry.entities e
WHERE e.original_author ILIKE '%yudkowsky%'
  AND e.content_risk IS DISTINCT FROM 'dangerous'
GROUP BY e.source::text
ORDER BY docs DESC
LIMIT 20

E5. Recent entity kind distribution for a source
SELECT kind::text, COUNT(*)
FROM scry.hackernews_items
WHERE original_timestamp >= '2025-01-01'
GROUP BY kind::text
ORDER BY 2 DESC
LIMIT 20


Source-native corpora follow the same pattern:

SELECT kind::text, COUNT(*)
FROM scry.wikipedia_articles
WHERE original_timestamp >= '2025-01-01'
GROUP BY kind::text
ORDER BY 2 DESC
LIMIT 20


Removing the date bound turns this into a large base-table aggregation. Run /v1/scry/estimate first or prefer source-specific MVs when they already cover the question.

E6. Hybrid search (lexical + semantic rerank in SQL)
WITH c AS (
  SELECT id FROM scry.search('deceptive alignment',
    kinds=>ARRAY['post'], limit_n=>200)
)
SELECT e.uri, e.title, e.original_author,
       emb.embedding_voyage4 <=> @p_deadbeef_topic AS distance
FROM c
JOIN scry.entities e ON e.id = c.id
JOIN scry.chunk_embeddings emb ON emb.entity_id = c.id AND emb.chunk_index = 0
WHERE e.content_risk IS DISTINCT FROM 'dangerous'
ORDER BY distance
LIMIT 50


Requires a stored embedding handle (@p_deadbeef_topic). See scry-vectors skill for creating handles.

E7. Cost estimation before execution
curl -s -X POST https://api.scry.io/v1/scry/estimate \
  -H "Authorization: Bearer $SCRY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sql": "SELECT arxiv_id, title FROM scry.arxiv_papers LIMIT 1000"}'


Returns EXPLAIN (FORMAT JSON) output. Use this for expensive queries before committing. It does not prove BM25 helper health: if scry.search* fails, check /v1/scry/index-view-status and /v1/scry/schema status as well. The /v1/scry/context handshake now also exposes lexical_search.status, status_basis, and last_known_status so you can distinguish stale observability from confirmed lexical trouble before issuing fallbacks.

E8. Create a shareable artifact
# 1. Run query and capture results
# 2. POST share
curl -s -X POST https://api.scry.io/v1/scry/shares \
  -H "Authorization: Bearer $SCRY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "kind": "query",
    "title": "Top RLHF posts on LessWrong",
    "summary": "20 highest-scored LW posts mentioning RLHF.",
    "payload": {
      "sql": "...",
      "result": {"columns": [...], "rows": [...]}
    }
  }'


Kinds: query, rerank, insight, chat, markdown. Progressive update: create stub immediately, then PATCH /v1/scry/shares/{slug}. Rendered at: https://scry.io/scry/share/{slug}.

E9. Emit a structured agent judgement
curl -s -X POST https://api.scry.io/v1/scry/judgements \
  -H "Authorization: Bearer $SCRY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "emitter": "my-agent",
    "judgement_kind": "topic_classification",
    "target_external_ref": "arxiv:2401.12345",
    "summary": "Paper primarily about mechanistic interpretability.",
    "payload": {"primary_topic": "mech_interp", "confidence_detail": "title+abstract match"},
    "confidence": 0.88,
    "tags": ["arxiv", "mech_interp"],
    "privacy_level": "self"
  }'


Exactly one target required: target_entity_id, target_actor_id, target_judgement_id, or target_external_ref. Public judgements must target target_entity_id, target_actor_id, or target_judgement_id; target_external_ref is limited to self or group privacy. Judgement-on-judgement: use target_judgement_id to chain observations.

E10. People / author lookup
-- Per-source author grouping
SELECT a.handle, a.display_name, a.source::text, COUNT(*) AS docs
FROM scry.entities e
JOIN scry.actors a ON a.id = e.author_actor_id
WHERE e.source = 'twitter'
GROUP BY a.handle, a.display_name, a.source::text
ORDER BY docs DESC
LIMIT 50

E11. Thread navigation (replies)
-- Find all replies to a root post
SELECT id, uri, title, original_author, original_timestamp
FROM scry.entities
WHERE anchor_entity_id = 'ROOT_ENTITY_UUID'
ORDER BY original_timestamp
LIMIT 100


anchor_entity_id is the root subject; parent_entity_id is the direct parent.

E12. Count estimation (safe pattern)

Avoid COUNT(*) on large tables. Instead, use schema endpoint row estimates or:

SELECT reltuples::bigint AS estimated_rows
FROM pg_class
WHERE relname = 'mv_lesswrong_posts'
LIMIT 1


Note: pg_class access is blocked on the public Scry SQL surface. Use /v1/scry/schema instead.

F) Error Handling

See references/error-reference.md for the full catalogue. Key patterns:

HTTP	Code	Meaning	Action
400	invalid_request	SQL parse error, missing LIMIT, bad params	Fix query
401	unauthorized	Missing or invalid API key	Check key
402	insufficient_credits	Token budget exhausted	Notify user
429	rate_limited	Too many requests	Respect Retry-After header
503	service_unavailable	Scry pool down or overloaded	Wait and retry

Auth + timeout diagnostics for CLI users:

If curl shows HTTP 000, that is client-side timeout/network abort, not a server HTTP status. Check --max-time and retry with /v1/scry/estimate first.
If you see 401 with "Invalid authorization format", check for whitespace/newlines in the key: KEY_CLEAN="$(printf '%s' \"$SCRY_API_KEY\" | tr -d '\\r\\n')" then use Authorization: Bearer $KEY_CLEAN.

Quota fallback strategy:

If 429: wait Retry-After seconds, retry once.
If 402: tell the user their token budget is exhausted.
If 503: retry after 30s with exponential backoff (max 3 attempts).
If query times out: simplify (use MV instead of full table, reduce LIMIT, add tighter WHERE filters).
G) Output Contract

When this skill completes a query task, return a consistent structure:

## Scry Result

**Query**: <natural language description>
**SQL**: ```sql <the SQL that ran> ```
**Rows returned**: <N> (truncated: <yes/no>)
**Duration**: <N>ms

<formatted results table or summary>

**Share**: <share URL if created>
**Caveats**: <any data quality notes, e.g., "score is NULL for arXiv">

Handoff Contract

Produces: JSON with columns, rows, row_count, duration_ms, truncated Feeds into:

rerank: ensure SQL returns id and content_text columns for candidate sets
scry-vectors: save entity IDs for embedding lookup and semantic reranking Receives from: none (entry point for SQL-based corpus access)
Related Skills
scry-vectors -- embed concepts as @handles, search by cosine distance, debias with vector algebra
scry-rerank -- LLM-powered multi-attribute reranking of candidate sets via pairwise comparison

For detailed schema documentation, see references/schema-guide.md. For the full pattern library, see references/query-patterns.md. For error codes and quota details, see references/error-reference.md.

Weekly Installs
41
Repository
exopriors/skills
GitHub Stars
3
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykWarn