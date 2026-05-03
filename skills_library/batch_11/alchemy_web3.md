---
title: alchemy-web3
url: https://skills.sh/0xgizmolab/alchemy-web3-skill/alchemy-web3
---

# alchemy-web3

skills/0xgizmolab/alchemy-web3-skill/alchemy-web3
alchemy-web3
Installation
$ npx skills add https://github.com/0xgizmolab/alchemy-web3-skill --skill alchemy-web3
SKILL.md
Alchemy Web3 Skill

Query blockchain data, NFTs, tokens, and transfers using Alchemy's production-grade APIs. Supports Ethereum, Polygon, Arbitrum, Base, Solana, and 80+ other chains.

Built by GizmoLab — Web3 development agency specializing in dApps, smart contracts, and blockchain infrastructure.

Setup
1. Get API Key
Sign up at alchemy.com (free tier available)
Create an app for your target chain
Copy your API key

💡 New to Web3 development? GizmoLab offers full-stack blockchain development services.

2. Configure
# Add to ~/.openclaw/.env
ALCHEMY_API_KEY=your_api_key_here

# Optional: Set default chain (defaults to eth-mainnet)
ALCHEMY_CHAIN=eth-mainnet

Quick Reference
Supported Chains
Chain	Endpoint Prefix
Ethereum	eth-mainnet, eth-sepolia
Polygon	polygon-mainnet, polygon-amoy
Arbitrum	arb-mainnet, arb-sepolia
Optimism	opt-mainnet, opt-sepolia
Base	base-mainnet, base-sepolia
Solana	solana-mainnet, solana-devnet
zkSync	zksync-mainnet
Linea	linea-mainnet
Scroll	scroll-mainnet
Blast	blast-mainnet

Full list: alchemy.com/docs/chains

CLI Usage
# Set your API key first
export ALCHEMY_API_KEY="your_key"

# Use the CLI
~/.openclaw/workspace/skills/alchemy-web3/scripts/alchemy.sh <command> [options]

Commands
Get ETH Balance
./alchemy.sh balance 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
# Returns: 1234.56 ETH

Get Token Balances
./alchemy.sh tokens 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
# Returns: All ERC-20 tokens held by address

Get NFTs for Owner
./alchemy.sh nfts 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
# Returns: All NFTs owned by address

Get NFT Metadata
./alchemy.sh nft-metadata 0x5180db8F5c931aaE63c74266b211F580155ecac8 1590
# Returns: Metadata for specific NFT

Get Asset Transfers
./alchemy.sh transfers 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
# Returns: Transaction history (in/out)

Get Block Info
./alchemy.sh block latest
./alchemy.sh block 12345678

Get Transaction
./alchemy.sh tx 0x123...abc

Resolve ENS
./alchemy.sh ens vitalik.eth
# Returns: 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045

Switch Chain
./alchemy.sh --chain polygon-mainnet balance 0x...
./alchemy.sh --chain arb-mainnet nfts 0x...

Direct API Examples
Node API (JSON-RPC)
# Get ETH balance
curl -X POST "https://eth-mainnet.g.alchemy.com/v2/$ALCHEMY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "eth_getBalance",
    "params": ["0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045", "latest"],
    "id": 1
  }'

NFT API
# Get NFTs for owner
curl "https://eth-mainnet.g.alchemy.com/nft/v3/$ALCHEMY_API_KEY/getNFTsForOwner?owner=vitalik.eth&pageSize=10"

# Get NFT metadata
curl "https://eth-mainnet.g.alchemy.com/nft/v3/$ALCHEMY_API_KEY/getNFTMetadata?contractAddress=0x5180db8F5c931aaE63c74266b211F580155ecac8&tokenId=1590"

# Get NFTs for collection
curl "https://eth-mainnet.g.alchemy.com/nft/v3/$ALCHEMY_API_KEY/getNFTsForContract?contractAddress=0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D&limit=10"

Token API
# Get token balances
curl -X POST "https://eth-mainnet.g.alchemy.com/v2/$ALCHEMY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "alchemy_getTokenBalances",
    "params": ["0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"],
    "id": 1
  }'

# Get token metadata
curl -X POST "https://eth-mainnet.g.alchemy.com/v2/$ALCHEMY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "alchemy_getTokenMetadata",
    "params": ["0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"],
    "id": 1
  }'

Transfers API
# Get asset transfers (transaction history)
curl -X POST "https://eth-mainnet.g.alchemy.com/v2/$ALCHEMY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "alchemy_getAssetTransfers",
    "params": [{
      "fromBlock": "0x0",
      "toBlock": "latest",
      "toAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
      "category": ["external", "erc20", "erc721", "erc1155"],
      "maxCount": "0x14"
    }],
    "id": 1
  }'

JavaScript/Node.js Examples
Using Fetch (Node 18+)
const apiKey = process.env.ALCHEMY_API_KEY;
const baseURL = `https://eth-mainnet.g.alchemy.com/v2/${apiKey}`;

// Get ETH Balance
async function getBalance(address) {
  const response = await fetch(baseURL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      jsonrpc: '2.0',
      method: 'eth_getBalance',
      params: [address, 'latest'],
      id: 1
    })
  });
  const data = await response.json();
  return parseInt(data.result, 16) / 1e18; // Convert to ETH
}

// Get NFTs
async function getNFTs(owner) {
  const url = `https://eth-mainnet.g.alchemy.com/nft/v3/${apiKey}/getNFTsForOwner?owner=${owner}`;
  const response = await fetch(url);
  return await response.json();
}

Using Alchemy SDK
npm install alchemy-sdk

import { Alchemy, Network } from 'alchemy-sdk';

const alchemy = new Alchemy({
  apiKey: process.env.ALCHEMY_API_KEY,
  network: Network.ETH_MAINNET
});

// Get NFTs
const nfts = await alchemy.nft.getNftsForOwner('vitalik.eth');
console.log(nfts.ownedNfts);

// Get token balances
const balances = await alchemy.core.getTokenBalances('vitalik.eth');
console.log(balances);

// Get transaction history
const transfers = await alchemy.core.getAssetTransfers({
  toAddress: '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045',
  category: ['external', 'erc20']
});

Webhooks (Real-time Notifications)

Receive HTTP POST requests when onchain events happen.

Webhook Types
Type	Use Case
Address Activity	Track transfers to/from specific addresses
NFT Activity	Track NFT sales, transfers, mints
Mined Transactions	Track when your txs are mined
Dropped Transactions	Get notified if tx is dropped
Gas Price	Alert on gas price thresholds
Create Webhook (Dashboard)
Go to dashboard.alchemy.com/webhooks
Click "Create Webhook"
Select type and configure
Add your endpoint URL
Webhook Payload Example
{
  "webhookId": "wh_abc123",
  "id": "evt_xyz789",
  "createdAt": "2024-01-15T12:00:00.000Z",
  "type": "ADDRESS_ACTIVITY",
  "event": {
    "network": "ETH_MAINNET",
    "activity": [{
      "fromAddress": "0x123...",
      "toAddress": "0x456...",
      "value": 1.5,
      "asset": "ETH"
    }]
  }
}

Common Patterns
Portfolio Tracker
# Get all assets for a wallet
./alchemy.sh balance 0x...      # ETH balance
./alchemy.sh tokens 0x...       # ERC-20 tokens
./alchemy.sh nfts 0x...         # NFTs

Transaction History
# Get full tx history for address
./alchemy.sh transfers 0x... --category external,erc20,erc721

NFT Collection Analysis
# Get all NFTs in a collection
./alchemy.sh collection 0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D

Multi-chain Query
# Check same address across chains
for chain in eth-mainnet polygon-mainnet arb-mainnet base-mainnet; do
  echo "=== $chain ==="
  ./alchemy.sh --chain $chain balance 0x...
done

Rate Limits
Plan	Compute Units/sec	Monthly CUs
Free	330	300M
Growth	660	Unlimited
Scale	Custom	Custom

Most endpoints cost 1-50 CUs. Check alchemy.com/docs/rate-limits for details.

Error Handling
// Rate limited
{"error": {"code": 429, "message": "Too Many Requests"}}

// Invalid API key
{"error": {"code": 401, "message": "Invalid API Key"}}

// Invalid params
{"error": {"code": -32602, "message": "Invalid params"}}

Resources
Get API Key: alchemy.com (free tier)
Dashboard: dashboard.alchemy.com
Docs: alchemy.com/docs
SDK: github.com/alchemyplatform/alchemy-sdk-js
Status: status.alchemy.com
About

Built by GizmoLab 🔧

GizmoLab is a Web3 development agency building dApps, smart contracts, and blockchain tools.

🌐 gizmolab.io — Agency services
🛠️ tools.gizmolab.io — Free blockchain dev tools
🎨 ui.gizmolab.io — Web3 UI components

Need custom blockchain development? Get in touch

AI Agent Workflows

The skill is designed for both human developers AND AI agents. See references/agent-workflows.md for complete examples:

Whale Tracker — Monitor large wallets for moves
Portfolio Monitor — Track balances across chains
NFT Floor Alert — Alert on price drops
Token Change Detector — Detect incoming/outgoing tokens
Gas Optimizer — Wait for low gas to transact
Mint Detector — Watch for new NFT mints
Dashboard Generator — Auto-generate wallet dashboards
Agent Pattern
QUERY → STORE → ANALYZE → DECIDE → ACT → REPEAT


Example cron job for an agent:

# Every hour, check whale activity and alert if >100 ETH moved
0 * * * * ~/.openclaw/workspace/skills/alchemy-web3/scripts/whale-tracker.sh

See Also
references/nft-api.md - Full NFT API reference
references/token-api.md - Full Token API reference
references/node-api.md - Full Node API reference
references/chains.md - All supported chains
references/agent-workflows.md - AI agent automation examples
Weekly Installs
26
Repository
0xgizmolab/alch…b3-skill
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn