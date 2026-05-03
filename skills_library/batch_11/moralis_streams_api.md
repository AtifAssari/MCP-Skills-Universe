---
title: moralis-streams-api
url: https://skills.sh/moralisweb3/onchain-skills/moralis-streams-api
---

# moralis-streams-api

skills/moralisweb3/onchain-skills/moralis-streams-api
moralis-streams-api
Installation
$ npx skills add https://github.com/moralisweb3/onchain-skills --skill moralis-streams-api
SKILL.md
CRITICAL: Read Rule Files Before Implementing

The #1 cause of bugs is using wrong HTTP methods or stream configurations.

For EVERY endpoint:

Read rules/{EndpointName}.md
Check HTTP method (PUT for create, POST for update, DELETE for delete)
Verify stream ID format (UUID, not hex)
Use hex chain IDs (0x1, 0x89), not names (eth, polygon)

Reading Order:

This SKILL.md (core patterns)
Endpoint rule file in rules/
Pattern references in references/ (for edge cases only)
Setup
API Key (optional)

Never ask the user to paste their API key into the chat. Instead:

Check if MORALIS_API_KEY is set in the environment (try running [ -n "$MORALIS_API_KEY" ] && echo "API key is set" || echo "API key is NOT set").
If not set, offer to create the .env file with an empty placeholder: MORALIS_API_KEY=
Tell the user to open the .env file and paste their key there themselves.
Let them know: without the key, you won't be able to test or call the Moralis API on their behalf.

If they don't have a key yet, point them to admin.moralis.com/register (free, no credit card).

Environment Variable Discovery

The .env file location depends on how skills are installed:

Create the .env file in the project root (same directory the user runs Claude Code from). Make sure .env is in .gitignore.

Verify Your Key
curl "https://api.moralis-streams.com/streams/evm?limit=10" \
  -H "X-API-Key: $MORALIS_API_KEY"

Base URL
https://api.moralis-streams.com


Important: Different from Data API (deep-index.moralis.io).

Authentication

All requests require: X-API-Key: $MORALIS_API_KEY

HTTP Methods (CRITICAL)
Action	Method	Endpoint
Create stream	PUT	/streams/evm
Update stream	POST	/streams/evm/{id}
Delete stream	DELETE	/streams/evm/{id}
Get streams	GET	/streams/evm
Replace addresses	PATCH	/streams/evm/{id}/address

Common mistake: Using POST to create streams. Use PUT instead.

Stream Types
Type	Description
tx	Native transactions
log	Contract event logs
erc20transfer	ERC20 token transfers
erc20approval	ERC20 approvals
nfttransfer	NFT transfers
internalTx	Internal transactions
Quick Reference: Most Common Patterns
Stream ID Format (ALWAYS UUID)
// WRONG - Hex format
"0x1234567890abcdef"

// CORRECT - UUID format
"YOUR_STREAM_ID"

Chain IDs (ALWAYS hex)
"0x1"     // Ethereum
"0x89"    // Polygon
"0x38"    // BSC
"0xa4b1"  // Arbitrum
"0xa"     // Optimism
"0x2105"  // Base

Event Signatures (topic0)
"Transfer(address,address,uint256)"   // ERC20/NFT Transfer
"Approval(address,address,uint256)"   // ERC20 Approval

Status Values (lowercase only)
"active"      // CORRECT - normal operating state
"paused"      // CORRECT - manually paused
"error"       // CORRECT - auto-set when webhook success rate <70%
"terminated"  // CORRECT - unrecoverable, after 24h in error
"ACTIVE"      // WRONG

Common Pitfalls (Top 5)
Using POST to create streams - Use PUT instead
Wrong base URL - Use api.moralis-streams.com, NOT deep-index.moralis.io
Hex stream ID - Must be UUID format, not hex
String chain names - Use hex (0x1), not names (eth)
Uppercase status - Use lowercase ("active", "paused")
Not returning 200 on test webhook - Stream won't start unless your endpoint returns 2xx on the test webhook sent during create/update

See references/CommonPitfalls.md for complete reference.

Triggers (Read-Only Contract Calls)

Enrich webhook data with on-chain reads (e.g., balanceOf). Triggers execute view/pure functions and attach results to webhook events. Supports dynamic selectors ($contract, $from, $to). See references/Triggers.md for complete reference with examples.

Native Balances in Webhooks

Configure getNativeBalances to include native token balances (ETH, BNB, etc.) in webhook payloads. Requires Business plan+. See references/UsefulStreamOptions.md for configuration details.

Delivery and Error Handling
Two webhooks per event: Unconfirmed (confirmed: false) + Confirmed (confirmed: true). Idempotent handlers required.
Streams auto-terminate after 24 hours in error state (webhook success rate <70%). This is unrecoverable — you must create a new stream.
Test webhook: Sent on every create/update. Must return 200 or stream won't start.

See references/DeliveryGuarantees.md and references/ErrorHandling.md.

Webhook Security

Webhooks are signed with your streams secret (different from API key).

Header: x-signature
Algorithm: sha3(JSON.stringify(body) + secret)
const verifySignature = (req, secret) => {
  const provided = req.headers["x-signature"];
  const generated = web3.utils.sha3(JSON.stringify(req.body) + secret);
  if (generated !== provided) throw new Error("Invalid Signature");
};


See references/WebhookSecurity.md for complete examples.

Testing Endpoints
WEBHOOK_URL="https://your-server.com/webhook"

# List streams (requires limit)
curl "https://api.moralis-streams.com/streams/evm?limit=100" \
  -H "X-API-Key: $MORALIS_API_KEY"

# Create stream (PUT, not POST)
curl -X PUT "https://api.moralis-streams.com/streams/evm" \
  -H "X-API-Key: $MORALIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "webhookUrl": "'${WEBHOOK_URL}'",
    "description": "Test stream",
    "tag": "test",
    "topic0": ["Transfer(address,address,uint256)"],
    "allAddresses": false,
    "chainIds": ["0x1"]
  }'

# Pause stream (POST to status)
curl -X POST "https://api.moralis-streams.com/streams/evm/<stream_id>/status" \
  -H "X-API-Key: $MORALIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"status": "paused"}'

Quick Troubleshooting
Issue	Cause	Solution
"400 Bad Request"	Invalid config	Check webhookUrl, topic0 format, chainIds
"404 Not Found"	Wrong stream ID	Verify UUID format
"Method Not Allowed"	Wrong HTTP method	PUT for create, POST for update
"Missing limit"	GET /streams/evm	Add ?limit=100
"No webhooks"	Stream paused	Check status is "active"
Endpoint Catalog

Complete list of all 20 Streams API endpoints organized by category.

Stream Management

Create, update, delete, and manage streams.

Endpoint	Description
AddAddressToStream	Add address to stream
CreateStream	Create stream
DeleteAddressFromStream	Delete address from stream
DeleteStream	Delete stream
DuplicateStream	Duplicate stream
GetAddresses	Get addresses by stream
GetHistory	Get history
GetLogs	Get logs
GetSettings	Get project settings
GetStats	Get project stats
GetStatsByStreamId	Get project stats by Stream ID
GetStream	Get a specific evm stream.
GetStreamBlockDataByNumber	Get webhook data returned on the block number with provided stream config
GetStreamBlockDataToWebhookByNumber	Send webhook based on a specific block number using stream config and addresses.
GetStreams	Get streams
ReplaceAddressFromStream	Replaces address from stream
UpdateStream	Update stream
UpdateStreamStatus	Update stream status
Status & Settings

Pause/resume streams and configure settings.

Endpoint	Description
SetSettings	Set project settings
History & Analytics

Stream history, replay, statistics, logs, and block data.

Endpoint	Description
ReplayHistory	Replay history
Listen to All Addresses

Set allAddresses: true with a topic0 and abi to monitor an event across every contract on a chain (e.g., all ERC20 transfers network-wide). Requires higher-tier plans. See references/ListenToAllAddresses.md for complete examples, ABI templates, and gotchas.

Example: Create ERC20 Transfer Monitor
curl -X PUT "https://api.moralis-streams.com/streams/evm" \
  -H "X-API-Key: $MORALIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "webhookUrl": "https://your-server.com/webhook",
    "description": "Monitor ERC20 transfers",
    "tag": "erc20-monitor",
    "topic0": ["Transfer(address,address,uint256)"],
    "allAddresses": true,
    "chainIds": ["0x1", "0x89"],
    "advancedOptions": [{
      "topic0": "Transfer(address,address,uint256)",
      "includeNativeHash": true
    }]
  }'

Pagination

List endpoints use cursor-based pagination:

# First page
curl "...?limit=100" -H "X-API-Key: $KEY"

# Next page
curl "...?limit=100&cursor=<cursor>" -H "X-API-Key: $KEY"

Supported Chains

All major EVM chains: Ethereum (0x1), Polygon (0x89), BSC (0x38), Arbitrum (0xa4b1), Optimism (0xa), Base (0x2105), Avalanche (0xa86a), and more.

See references/StreamConfiguration.md for complete chain ID list.

Reference Documentation
references/CommonPitfalls.md - Complete pitfalls reference
references/DeliveryGuarantees.md - At-least-once delivery, dual webhooks, confirmation blocks, test webhooks
references/ErrorHandling.md - Retry schedule, error/terminated states, rate limits, re-org handling
references/FAQ.md - Streams API frequently asked questions
references/FilterStreams.md - Webhook data filtering to reduce noise
references/ListenToAllAddresses.md - Monitor events across all contracts on a chain
references/MonitorMultipleAddresses.md - Multi-address monitoring patterns
references/ReplayFailedWebhooks.md - Replay failed webhook guide
references/StreamConfiguration.md - Stream config reference
references/Triggers.md - Read-only contract call enrichment (balanceOf, etc.)
references/Tutorials.md - Real-world examples and tutorials
references/UsefulStreamOptions.md - Advanced stream configuration options
references/WebhookResponseBody.md - Webhook payload structure
references/WebhookSecurity.md - Signature verification
See Also
Endpoint rules: rules/*.md files
Data API: @moralis-data-api for querying blockchain state
Weekly Installs
83
Repository
moralisweb3/onc…n-skills
GitHub Stars
8
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn