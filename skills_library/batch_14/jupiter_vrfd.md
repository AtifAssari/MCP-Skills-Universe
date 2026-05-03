---
title: jupiter-vrfd
url: https://skills.sh/nghanyi/agent-skills/jupiter-vrfd
---

# jupiter-vrfd

skills/nghanyi/agent-skills/jupiter-vrfd
jupiter-vrfd
Installation
$ npx skills add https://github.com/nghanyi/agent-skills --skill jupiter-vrfd
SKILL.md
Jupiter Token Verification

This skill covers the public token verification submission flow.

Base URL: https://token-verification-dev-api.jup.ag
Cost: 1 JUP
Public routes covered:
GET /express/check-eligibility
GET /payments/express/craft-txn
POST /payments/express/execute
Auth: no API key required for the public submission flow
Use / Do Not Use

Use when:

checking whether a token is eligible for submission
crafting and signing the submission payment transaction
executing the submission flow
optionally updating token metadata as part of the submission

Do not use when:

the agent would need private or internal routes
the agent needs to fetch or merge existing metadata from non-public endpoints
the user wants swaps, trading, or unrelated Jupiter flows
Triggers

verify token, submit verification, check eligibility, craft payment transaction, execute payment, pay for verification

Intent Router
User intent	Endpoint	Method	Auth
Check eligibility	/express/check-eligibility?tokenId=...	GET	None
Craft payment transaction	/payments/express/craft-txn?senderAddress=...	GET	None
Sign and execute payment	/payments/express/execute	POST	None
References

Load these on demand:

API Reference for request and response shapes for the 3 public routes
Payment Execution when the user wants to submit and has confirmed the paying wallet details
Execution Notes

For submission requests in constrained agent environments:

outbound HTTP from curl or the local Node script may require sandbox approval or escalation
package installation may require approval or escalation
prefer an ESM temp workspace and node --experimental-strip-types pay.ts over npx tsx pay.ts in sandboxed Codex environments, because tsx may fail when it cannot open its IPC pipe
Agent Conversation Flow

Extract as much as possible from the user's first message. Skip questions whose answers are already present.

Step 0. Extract Upfront Parameters

Look for:

intent: explicit eligibility-only check or submission help
token mint
paying wallet address
token Twitter URL or handle
requester Twitter URL or handle
description
confirmation that the paying wallet holds at least 1 JUP plus a small amount of SOL for fees
Step 1. Route the Request

If the user explicitly asks only to check eligibility, do that and stop after the eligibility response.

Otherwise, proceed directly into the submission flow. If the user says verify, submit, apply, or similar, treat it as a submission request.

Step 2. Collect Token Mint

tokenId is always required. Validate that it is a Solana public key.

Step 3. Check Eligibility

Call:

GET {BASE_URL}/express/check-eligibility?tokenId={tokenId}


Interpret the result:

canVerify: true means the token can enter the submission flow
canVerify: false means the user cannot submit; explain verificationError
canMetadata: true means the execute endpoint can also accept a tokenMetadata update
canMetadata: false means metadata cannot be updated in this submission

For an eligibility-only request, report the result and stop here.

Step 3a. Offer Metadata Update

If canMetadata: true, ask the user whether they would also like to update their token metadata as part of this submission.

If they say yes, present the available metadata fields:

Field	Type	Description
icon	string	Token icon URL
name	string	Token name
symbol	string	Token symbol
website	string	Project website URL
telegram	string	Telegram link
twitter	string	Twitter / X URL
twitterCommunity	string	Twitter community URL
discord	string	Discord invite link
instagram	string	Instagram URL
tiktok	string	TikTok URL
circulatingSupply	string	Circulating supply value
useCirculatingSupply	boolean	Enable circulating supply display
tokenDescription	string	Token description
coingeckoCoinId	string	CoinGecko coin ID
useCoingeckoCoinId	boolean	Enable CoinGecko integration
circulatingSupplyUrl	string	URL that returns circulating supply
useCirculatingSupplyUrl	boolean	Enable supply URL
otherUrl	string	Any other relevant URL

Collect only the fields the user wants to update. Build the tokenMetadata object with just those fields plus tokenId. Do not include fields the user did not specify.

If they say no, or if canMetadata: false, skip metadata and continue.

Step 4. Resolve Local Signer Source

Only for submission requests.

Check for a local signing source in this order:

.env / .env.local contains PRIVATE_KEY or SOLANA_PRIVATE_KEY
~/.config/solana/id.json

Only confirm file paths and variable names in chat. Never print secret values. Only derive the wallet address inside the local execution script so it can verify that the signer matches walletAddress.

Step 5. Batch-Collect Remaining Parameters

Collect all missing fields in one prompt, including confirmation that the paying wallet holds at least 1 JUP plus a small amount of SOL for fees.

Field	Required	Notes
walletAddress	Yes	Paying wallet; maps to senderAddress in the API body
twitterHandle	Yes for normal submission	Full x.com or twitter.com URL
senderTwitterHandle	No	Omit if not provided
description	Yes for normal submission	Short token description

Validation rules:

wallet must be a valid Solana public key
Twitter URLs must be https://x.com/... or https://twitter.com/...
bare handles may be normalized to https://x.com/{handle} with user confirmation
omit absent optional fields instead of sending empty strings
require the user to confirm the paying wallet currently holds at least 1 JUP plus a small amount of SOL for fees before continuing
Step 6. Confirm Before Submitting

Summarize:

token mint
wallet address
token Twitter URL
requester Twitter URL if present
description
metadata fields to update, if any
cost: 1 JUP

Require an explicit final confirmation that:

the listed wallet will pay 1 JUP
that wallet has enough SOL for network fees
the user wants you to proceed with the submission now
Step 7. Submit and Report

Load Payment Execution and follow the local signing flow:

craft the unsigned transaction with GET /payments/express/craft-txn
verify the transaction contents before signing
sign locally
submit via POST /payments/express/execute

Report the returned transaction signature and whether verificationCreated / metadataCreated were set.

Input Auto-Correction
User provides	Auto-correct to	Confirm?
@handle or bare handle	https://x.com/{handle}	Yes
twitter.com/handle or x.com/handle	Add https:// prefix	Yes
token mint with surrounding spaces	Trimmed string	No
Resources
JUP Token Mint: JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN
Jupiter Docs: dev.jup.ag
Jupiter Verified: verified.jup.ag
Weekly Installs
9
Repository
nghanyi/agent-skills
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn