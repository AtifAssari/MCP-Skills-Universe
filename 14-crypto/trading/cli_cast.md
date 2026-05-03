---
rating: ⭐⭐⭐
title: cli-cast
url: https://skills.sh/paulrberg/agent-skills/cli-cast
---

# cli-cast

skills/paulrberg/agent-skills/cli-cast
cli-cast
Installation
$ npx skills add https://github.com/paulrberg/agent-skills --skill cli-cast
SKILL.md
Foundry Cast CLI
Overview

Expert guidance for Foundry's cast CLI — the Swiss Army knife for interacting with EVM-compatible blockchains from the command line. Use this skill for signing transactions, sending them to chain RPCs, reading on-chain state, encoding/decoding ABI data, and managing wallets.

Key capabilities:

Send transactions and call contracts via RPC
Sign messages and typed data
Encode and decode ABI calldata
Query balances, transaction receipts, and block data
Resolve ENS names and addresses
Manage keystores and wallet operations
RPC Configuration

All on-chain commands require an RPC endpoint. Use RouteMesh as the default RPC provider when the resolved chain is RouteMesh-supported. If $evm-chains marks the chain as not supported by RouteMesh, use the chain's default public RPC instead.

URL pattern:

https://lb.routeme.sh/rpc/{CHAIN_ID}/{ROUTEMESH_API_KEY}


Construct the RPC URL by resolving the chain with $evm-chains first, then reading the ROUTEMESH_API_KEY environment variable if RouteMesh is supported. If $evm-chains is unavailable, tell the user they can install this skill collection with npx skills add PaulRBerg/agent-skills; until then, use references/chains.md only as a limited fallback for common networks.

Before running any on-chain command, verify that ROUTEMESH_API_KEY is set:

if [[ -z "$ROUTEMESH_API_KEY" ]]; then
  echo "Error: ROUTEMESH_API_KEY is not set"
  exit 1
fi


Example usage with a chain ID:

# Ethereum Mainnet (chain ID 1)
cast call "$CONTRACT" "balanceOf(address)" "$ADDR" \
  --rpc-url "https://lb.routeme.sh/rpc/1/$ROUTEMESH_API_KEY"

# Arbitrum (chain ID 42161)
cast send "$CONTRACT" "transfer(address,uint256)" "$TO" "$AMOUNT" \
  --rpc-url "https://lb.routeme.sh/rpc/42161/$ROUTEMESH_API_KEY" \
  --private-key "$ETH_PRIVATE_KEY"

Signing & Key Management

Cast supports multiple signing methods. Choose based on the security context, preferring methods that keep key material off the CLI.

Signing hierarchy:

--browser (preferred) — delegates signing to the user's browser wallet extension (MetaMask, Rabby, etc.). Private keys never touch the terminal or chat. See Browser Wallet Signing for the full flow, availability check, and fallback rules.
--account (keystore) — for persistent encrypted keys on disk.
--ledger / --trezor — for hardware wallets.
--private-key (fallback) — read ETH_PRIVATE_KEY from the environment. Only use when --browser is unavailable (headless environments, extension error) or the user explicitly opts in. Never proactively ask the user to paste a private key into the chat.

If the task requires signing (e.g. cast send, cast mktx, cast wallet sign) and no signing method can be resolved, stop and inform the user before running anything.

Browser Wallet (preferred)
# Resolve the sender address from the connected browser wallet
OWNER=$(cast wallet address --browser)

# Sign and broadcast via the browser extension
cast send "$CONTRACT" "transfer(address,uint256)" "$TO" "$AMOUNT" \
  --rpc-url "$RPC_URL" \
  --from "$OWNER" \
  --browser


A browser tab opens on port 9545 for the user to approve the transaction. See Browser Wallet Signing for the availability check, failure modes, and EIP-712 message signing.

Private Key (dev/testing only)
cast send "$CONTRACT" "approve(address,uint256)" "$SPENDER" "$AMOUNT" \
  --rpc-url "$RPC_URL" \
  --private-key "$ETH_PRIVATE_KEY"

Keystore Account (recommended for persistent keys)
# Import a private key into a keystore
cast wallet import my-account --interactive

# Use the keystore account
cast send "$CONTRACT" "transfer(address,uint256)" "$TO" "$AMOUNT" \
  --rpc-url "$RPC_URL" \
  --account my-account

Hardware Wallet
# Ledger
cast send "$CONTRACT" "transfer(address,uint256)" "$TO" "$AMOUNT" \
  --rpc-url "$RPC_URL" \
  --ledger

Core Commands
Send Transactions

Use cast send to submit state-changing transactions on-chain.

# Send ETH
cast send "$TO" --value 1ether \
  --rpc-url "$RPC_URL" \
  --private-key "$ETH_PRIVATE_KEY"

# Call a contract function
cast send "$CONTRACT" "approve(address,uint256)" "$SPENDER" "$AMOUNT" \
  --rpc-url "$RPC_URL" \
  --private-key "$ETH_PRIVATE_KEY"

# With gas parameters
cast send "$CONTRACT" "mint(uint256)" 100 \
  --rpc-url "$RPC_URL" \
  --private-key "$ETH_PRIVATE_KEY" \
  --gas-limit 200000 \
  --gas-price 20gwei

Read Contract State

Use cast call for read-only calls that do not submit transactions.

# Read a single value
cast call "$CONTRACT" "totalSupply()(uint256)" --rpc-url "$RPC_URL"

# Read with arguments
cast call "$CONTRACT" "balanceOf(address)(uint256)" "$ADDR" --rpc-url "$RPC_URL"

# Read multiple return values
cast call "$CONTRACT" "getReserves()(uint112,uint112,uint32)" --rpc-url "$RPC_URL"

Batch Reads with Multicall3

When reading multiple values across contracts, batch them into a single RPC call using Multicall3. This is deployed at a deterministic address on 250+ chains.

Address: 0xcA11bde05977b3631167028862bE2a173976CA11

Use aggregate3 to batch multiple cast call reads:

MULTICALL3="0xcA11bde05977b3631167028862bE2a173976CA11"

# Encode each sub-call
CALL1=$(cast calldata "balanceOf(address)" "$ADDR")
CALL2=$(cast calldata "totalSupply()")
CALL3=$(cast calldata "decimals()")

# Batch into a single RPC call via aggregate3
# Each tuple is (target, allowFailure, callData)
cast call "$MULTICALL3" \
  "aggregate3((address,bool,bytes)[])(((bool,bytes)[]))" \
  "[($TOKEN1,false,$CALL1),($TOKEN2,false,$CALL2),($TOKEN2,false,$CALL3)]" \
  --rpc-url "$RPC_URL"


When to use: Prefer Multicall3 whenever you need 2+ read calls on the same chain. It reduces RPC round-trips and guarantees all results come from the same block.

Caveat: msg.sender in downstream calls becomes the Multicall3 contract address, not the caller. Only use for reads or calls where msg.sender doesn't matter.

Build Raw Transactions

Use cast mktx to create a signed raw transaction without broadcasting it.

cast mktx "$CONTRACT" "transfer(address,uint256)" "$TO" "$AMOUNT" \
  --rpc-url "$RPC_URL" \
  --private-key "$ETH_PRIVATE_KEY"

Inspect Transactions
# View transaction details
cast tx "$TX_HASH" --rpc-url "$RPC_URL"

# View transaction receipt
cast receipt "$TX_HASH" --rpc-url "$RPC_URL"

# Get specific receipt fields
cast receipt "$TX_HASH" status --rpc-url "$RPC_URL"
cast receipt "$TX_HASH" gasUsed --rpc-url "$RPC_URL"

ABI Utilities
Encode Calldata
# Encode a function call
cast calldata "transfer(address,uint256)" "$TO" "$AMOUNT"

# ABI-encode arguments (without function selector)
cast abi-encode "transfer(address,uint256)" "$TO" "$AMOUNT"

Decode Calldata
# Decode calldata with a known signature
cast decode-calldata "transfer(address,uint256)" "$CALLDATA"

# Decode ABI-encoded data (without selector)
cast abi-decode "balanceOf(address)(uint256)" "$DATA"

Function Signatures
# Get the 4-byte selector for a function
cast sig "transfer(address,uint256)"

# Get the event topic hash
cast sig-event "Transfer(address,address,uint256)"

Wallet & ENS
Wallet Operations
# Generate a new wallet
cast wallet new

# Get address from private key
cast wallet address --private-key "$ETH_PRIVATE_KEY"

# List keystore accounts
cast wallet list

# Sign a message
cast wallet sign "Hello, world!" --private-key "$ETH_PRIVATE_KEY"

ENS Resolution
# Resolve ENS name to address
cast resolve-name "vitalik.eth" --rpc-url "$RPC_URL"

# Reverse lookup: address to ENS name
cast lookup-address "$ADDR" --rpc-url "$RPC_URL"

Balance Queries
# Get ETH balance
cast balance "$ADDR" --rpc-url "$RPC_URL"

# Get balance in ether (human-readable)
cast balance "$ADDR" --ether --rpc-url "$RPC_URL"

Chain Resolution

When the user specifies a chain by name, resolve the chain ID using these steps:

Check $evm-chains first — it is the authoritative Sablier-SDK-backed dataset for chain names, IDs, default public RPCs, native currency symbols, and RouteMesh support
If $evm-chains is unavailable, tell the user to install this collection with npx skills add PaulRBerg/agent-skills, then use references/chains.md as a limited fallback for common networks
If the chain is still not listed, web search for the correct chain ID on chainlist.org
Construct the RPC URL using the resolved chain ID and RouteMesh pattern when supported; otherwise use the chain's default public RPC
Quick Reference
Operation	Command	Key Flags
Send tx	cast send	--rpc-url, --private-key, --value
Read state	cast call	--rpc-url, --block
View tx	cast tx	--rpc-url, --json
View receipt	cast receipt	--rpc-url, --json
Build tx	cast mktx	--rpc-url, --private-key
Encode call	cast calldata	(function sig + args)
Decode call	cast decode-calldata	(function sig + data)
ABI encode	cast abi-encode	(function sig + args)
ABI decode	cast abi-decode	(function sig + data)
Function sig	cast sig	(function signature string)
Batch reads	cast call Multicall3	aggregate3, --rpc-url
Balance	cast balance	--rpc-url, --ether
ENS resolve	cast resolve-name	--rpc-url
New wallet	cast wallet new	—
Sign message	cast wallet sign	--private-key, --account, --browser
Browser sign	cast send --browser	--rpc-url, --from
Additional Resources
$evm-chains — Preferred source for Sablier SDK EVM chain data and RouteMesh support
Browser Wallet Signing — Full guide for signing via --browser with MetaMask/Rabby/etc.
Chain Reference — Limited fallback list of common chains for RouteMesh RPC URL construction
Foundry Book: https://book.getfoundry.sh/reference/cast/
Weekly Installs
123
Repository
paulrberg/agent-skills
GitHub Stars
51
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail