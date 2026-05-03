---
rating: ⭐⭐⭐
title: bankr x402 sdk - token swaps
url: https://skills.sh/bankrbot/claude-plugins/bankr-x402-sdk---token-swaps
---

# bankr x402 sdk - token swaps

skills/bankrbot/claude-plugins/Bankr x402 SDK - Token Swaps
Bankr x402 SDK - Token Swaps
Installation
$ npx skills add https://github.com/bankrbot/claude-plugins --skill 'Bankr x402 SDK - Token Swaps'
SKILL.md
SDK Token Swaps

Build and execute token swaps with AI-powered 0x routing.

Prompt Patterns
Pattern	Example
Amount-based	"Swap 0.1 ETH to USDC"
Value-based	"Buy $100 worth of DEGEN"
Percentage	"Swap 50% of my ETH to USDC"
Sell all	"Sell all my DEGEN"
Chain-specific	"Swap ETH to USDC on Polygon"
# Amount Swaps
"Swap 0.1 ETH to USDC"
"Exchange 100 USDC for WETH"
"Swap 1000 DEGEN to ETH"

# Value Swaps
"Buy $100 worth of DEGEN"
"Purchase $50 of ETH"

# Percentage Swaps
"Swap 50% of my ETH to USDC"
"Sell 25% of my DEGEN"

# Chain-Specific
"Swap 0.1 ETH to USDC on Base"
"Exchange 100 USDC for WETH on Ethereum"

ERC20 Approval Handling

For ERC20 swaps (selling tokens other than ETH), approval is required before the swap.

const result = await client.promptAndWait({
  prompt: "Swap 100 USDC to WETH",
});

const swapTx = result.transactions?.find(tx => tx.type === "swap");

// Check if approval is needed
if (swapTx?.metadata.approvalRequired) {
  // Execute pre-built approval transaction first
  await wallet.sendTransaction(swapTx.metadata.approvalTx);
}

// Then execute the swap
await wallet.sendTransaction(swapTx.metadata.transaction);

Approval Fields
Field	Description
approvalRequired	Whether approval needed before swap
approvalTx	Pre-built approval transaction (ready to send)
allowanceTarget	0x AllowanceHolder address (for manual approval)
Usage
import { BankrClient } from "@bankr/sdk";

const client = new BankrClient({
  privateKey: process.env.BANKR_PRIVATE_KEY as `0x${string}`,
});

const result = await client.promptAndWait({
  prompt: "Swap 0.1 ETH to USDC on Base",
});

if (result.status === "completed" && result.transactions?.length) {
  const tx = result.transactions[0].metadata.transaction;
  await wallet.sendTransaction(tx);
}

Supported Chains
Chain	Native Token	Default
Base	ETH	Yes
Ethereum	ETH	No
Polygon	MATIC	No
Solana	SOL	No
Related Skills
sdk-capabilities: Full list of supported operations
sdk-transaction-builder: Other transaction types (transfers, NFTs)
sdk-wallet-operations: Client setup and configuration
Weekly Installs
–
Repository
bankrbot/claude-plugins
GitHub Stars
72
First Seen
–