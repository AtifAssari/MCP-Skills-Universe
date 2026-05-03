---
title: x402lint
url: https://skills.sh/rawgroundbeef/x402lint/x402lint
---

# x402lint

skills/rawgroundbeef/x402lint/x402lint
x402lint
Installation
$ npx skills add https://github.com/rawgroundbeef/x402lint --skill x402lint
SKILL.md
x402lint

Validate and create x402 payment configurations. The x402 protocol defines how HTTP 402 responses communicate payment requirements to clients.

For full protocol details, field rules, registries, and error codes, read references/protocol-spec.md.

Workflow
Determine task type: Validating an existing config? -> Follow "Validation" below Creating a new config? -> Follow "Creation" below Debugging a failing config? -> Follow "Debugging" below
Validation

Validate using the x402lint SDK in the project at packages/x402lint/.

import { check } from './packages/x402lint/src/index'

const result = check({
  body: configObject,           // or parse from header
  headers: { 'payment-required': base64String }
})

// result.valid        - boolean
// result.errors       - ValidationIssue[] (blocking)
// result.warnings     - ValidationIssue[] (non-blocking)
// result.normalized   - canonical v2 shape
// result.summary      - display-ready per-accept entries with registry data


For strict mode (warnings become errors): check(response, { strict: true })

Also available: validate(input) for raw config objects, extractConfig(response) for parsing HTTP responses.

Creation

When creating an x402 config, always produce v2 format. Template:

{
  "x402Version": 2,
  "accepts": [
    {
      "scheme": "exact",
      "network": "<CAIP-2 identifier>",
      "amount": "<atomic units as string>",
      "asset": "<token contract address>",
      "payTo": "<recipient address with proper checksum>",
      "maxTimeoutSeconds": 300
    }
  ],
  "resource": {
    "url": "<the protected resource URL>",
    "method": "GET"
  }
}

Critical rules when generating configs
amount: Always a string of digits in atomic units (e.g., "1000000" for 1 USDC with 6 decimals). Never use decimal notation.
network: Always CAIP-2 format (namespace:reference). Use registry from protocol-spec.md. Never use simple names like "base".
EVM payTo/asset: Use EIP-55 checksummed addresses (mixed-case). All-lowercase is valid but not recommended.
Solana payTo/asset: Use base58 addresses (32-44 characters).
maxTimeoutSeconds: Always include; positive integer. 300 is a safe default.
resource: Always include with at least a url.
Common network + asset combinations

Base (USDC):

{ "network": "eip155:8453", "asset": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913" }


Base Sepolia testnet (USDC):

{ "network": "eip155:84532", "asset": "0x036CbD53842c5426634e7929541eC2318f3dCF7e" }


Avalanche (USDC):

{ "network": "eip155:43114", "asset": "0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E" }


Solana Mainnet (USDC):

{ "network": "solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp", "asset": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v" }

HTTP 402 endpoint pattern
// Express/Node example
app.get('/api/premium', (req, res) => {
  // Check for valid payment proof in request...
  // If no payment, return 402:
  res.status(402).json({
    x402Version: 2,
    accepts: [{
      scheme: "exact",
      network: "eip155:8453",
      amount: "1000000",
      asset: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
      payTo: "0xYourChecksummedAddress",
      maxTimeoutSeconds: 300
    }],
    resource: {
      url: "https://yourapi.com/api/premium",
      method: "GET"
    }
  })
})


Alternative: deliver via Payment-Required header with base64-encoded JSON body.

Debugging

When a config fails validation:

Run check() or validate() against the config
Inspect result.errors -- each has code, field, message, and optional fix
Common issues and fixes:
INVALID_NETWORK_FORMAT: Use CAIP-2, e.g., "eip155:8453" not "base"
INVALID_AMOUNT: Must be digit-only string in atomic units, not "1.5" or 1000000
BAD_EVM_CHECKSUM: Fix address casing per EIP-55
MISSING_PAY_TO / MISSING_ASSET: Required fields omitted
LEGACY_FORMAT: Config is v1; normalize to v2 with normalize()
Apply the fix suggestion from each issue when available
Re-validate after fixes
Weekly Installs
14
Repository
rawgroundbeef/x402lint
GitHub Stars
4
First Seen
Feb 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass