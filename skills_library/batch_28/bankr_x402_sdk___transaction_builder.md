---
title: bankr x402 sdk - transaction builder
url: https://skills.sh/bankrbot/claude-plugins/bankr-x402-sdk---transaction-builder
---

# bankr x402 sdk - transaction builder

skills/bankrbot/claude-plugins/Bankr x402 SDK - Transaction Builder
Bankr x402 SDK - Transaction Builder
Installation
$ npx skills add https://github.com/bankrbot/claude-plugins --skill 'Bankr x402 SDK - Transaction Builder'
SKILL.md
SDK Transaction Builder

Build blockchain transactions for transfers, NFTs, bridges, and DeFi operations.

Transaction Types
Type	Description	Example Prompt
transfer_erc20	Send ERC20 tokens	"Send 100 USDC to 0x..."
transfer_eth	Send native ETH	"Send 0.1 ETH to 0x..."
convert_eth_to_weth	Wrap ETH	"Wrap 0.5 ETH"
convert_weth_to_eth	Unwrap WETH	"Unwrap 1 WETH"
transfer_nft	Send NFT	"Transfer my NFT #123 to 0x..."
buy_nft	Purchase NFT	"Buy the cheapest Pudgy Penguin"
mint_manifold_nft	Mint from Manifold	"Mint from Manifold at 0x..."
mint_seadrop_nft	Mint from SeaDrop	"Mint from SeaDrop at 0x..."
swapCrossChain	Bridge tokens	"Bridge 100 USDC from Ethereum to Base"
Prompt Patterns
# Transfers
"Send 100 USDC to 0x742d35..."
"Transfer 0.5 ETH to vitalik.eth"
"Send 50 USDC to 0x123... on Base"

# ETH/WETH
"Wrap 0.5 ETH to WETH"
"Unwrap 1 WETH to ETH"

# NFTs
"Transfer my Pudgy Penguin #1234 to 0x..."
"Buy the cheapest Pudgy Penguin on OpenSea"
"Mint NFT from Manifold contract 0x..."

# Cross-Chain
"Bridge 100 USDC from Ethereum to Base"
"Move 0.5 ETH from Base to Ethereum"

Usage
import { BankrClient } from "@bankr/sdk";

const client = new BankrClient({
  privateKey: process.env.BANKR_PRIVATE_KEY as `0x${string}`,
});

// Transfer tokens
const result = await client.promptAndWait({
  prompt: "Send 100 USDC to 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb0",
});

if (result.status === "completed" && result.transactions) {
  const tx = result.transactions[0].metadata.transaction;
  await wallet.sendTransaction(tx);
}

Transaction Metadata

All transactions include metadata for verification:

const tx = result.transactions[0];
const meta = tx.metadata.__ORIGINAL_TX_DATA__;

console.log(`Chain: ${meta.chain}`);
console.log(`Amount: ${meta.inputTokenAmount} ${meta.inputTokenTicker}`);
console.log(`To: ${meta.receiver}`);
console.log(`Message: ${meta.humanReadableMessage}`);

Timing Guidelines
Operation	Typical Time
ERC20/ETH transfer	2-5s
Wrap/Unwrap	2-5s
NFT transfer	3-5s
NFT purchase	5-10s
Cross-chain bridge	10-30s
Related Skills
sdk-token-swaps: Token swap patterns and approval handling
sdk-capabilities: Full list of supported operations
sdk-wallet-operations: Client setup and configuration
Weekly Installs
–
Repository
bankrbot/claude-plugins
GitHub Stars
72
First Seen
–