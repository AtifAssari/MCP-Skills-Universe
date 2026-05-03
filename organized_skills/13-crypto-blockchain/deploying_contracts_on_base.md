---
rating: ⭐⭐
title: deploying-contracts-on-base
url: https://skills.sh/base/skills/deploying-contracts-on-base
---

# deploying-contracts-on-base

skills/base/skills/deploying-contracts-on-base
deploying-contracts-on-base
Installation
$ npx skills add https://github.com/base/skills --skill deploying-contracts-on-base
SKILL.md
Deploying Contracts on Base
Prerequisites
Configure RPC endpoint (testnet: sepolia.base.org, mainnet: mainnet.base.org)
Store private keys in Foundry's encrypted keystore — never commit keys
Obtain testnet ETH from CDP faucet (testnet only)
Get a BaseScan API key for contract verification
Security
Never commit private keys to version control — use Foundry's encrypted keystore (cast wallet import)
Never hardcode API keys in source files — use environment variables or foundry.toml with ${ENV_VAR} references
Never expose .env files — add .env to .gitignore
Use production RPC providers (not public endpoints) for mainnet deployments to avoid rate limits and data leaks
Verify contracts on BaseScan to enable public audit of deployed code
Input Validation

Before constructing shell commands, validate all user-provided values:

contract-path: Must match ^[a-zA-Z0-9_/.-]+\.sol:[a-zA-Z0-9_]+$. Reject paths with spaces, semicolons, pipes, or backticks.
rpc-url: Must be a valid HTTPS URL (^https://[^\s;|&]+$). Reject non-HTTPS or malformed URLs.
keystore-account: Must be alphanumeric with hyphens/underscores (^[a-zA-Z0-9_-]+$).
etherscan-api-key: Must be alphanumeric (^[a-zA-Z0-9]+$).

Do not pass unvalidated user input into shell commands.

Obtaining Testnet ETH via CDP Faucet

Testnet ETH is required to pay gas on Base Sepolia. Use the CDP Faucet to claim it. Supported tokens: ETH, USDC, EURC, cbBTC. ETH claims are capped at 0.0001 ETH per claim, 1000 claims per 24 hours.

Option A: CDP Portal UI (recommended for quick setup)

Agent behavior: If you have browser access, navigate to the portal and claim directly. Otherwise, ask the user to complete these steps and provide the funded wallet address.

Sign in to CDP Portal (create an account at portal.cdp.coinbase.com/create-account if needed)
Go to Faucets
Select Base Sepolia network
Select ETH token
Enter the wallet address and click Claim
Verify on sepolia.basescan.org that the funds arrived
Option B: Programmatic via CDP SDK

Requires a CDP API key and Wallet Secret.

npm install @coinbase/cdp-sdk dotenv

import { CdpClient } from "@coinbase/cdp-sdk";
import dotenv from "dotenv";
dotenv.config();

const cdp = new CdpClient();
const account = await cdp.evm.createAccount();

const faucetResponse = await cdp.evm.requestFaucet({
  address: account.address,
  network: "base-sepolia",
  token: "eth",
});

console.log(`Funded: https://sepolia.basescan.org/tx/${faucetResponse.transactionHash}`);


Environment variables needed in .env:

CDP_API_KEY_ID=your-api-key-id
CDP_API_KEY_SECRET=your-api-key-secret
CDP_WALLET_SECRET=your-wallet-secret


To fund an existing wallet instead of creating a new one, pass its address directly to requestFaucet.

Obtaining a BaseScan API Key

A BaseScan API key is required for the --verify flag to auto-verify contracts on BaseScan. BaseScan uses the same account system as Etherscan.

Agent behavior: If you have browser access, navigate to the BaseScan site and create the key. Otherwise, ask the user to complete these steps and provide the API key.

Go to basescan.org/myapikey (or etherscan.io/myapikey — same account works)
Sign in or create a free account
Click Add to create a new API key
Copy the key and set it in your environment:
export ETHERSCAN_API_KEY=your-basescan-api-key


Alternatively, pass it directly to forge:

forge create ... --etherscan-api-key <your-key>


Or add it to foundry.toml:

[etherscan]
base-sepolia = { key = "${ETHERSCAN_API_KEY}", url = "https://api-sepolia.basescan.org/api" }
base = { key = "${ETHERSCAN_API_KEY}", url = "https://api.basescan.org/api" }

Deployment Commands
Testnet
forge create src/MyContract.sol:MyContract \
  --rpc-url https://sepolia.base.org \
  --account <keystore-account> \
  --verify \
  --etherscan-api-key $ETHERSCAN_API_KEY

Mainnet
forge create src/MyContract.sol:MyContract \
  --rpc-url https://mainnet.base.org \
  --account <keystore-account> \
  --verify \
  --etherscan-api-key $ETHERSCAN_API_KEY

Key Notes
Contract format: <contract-path>:<contract-name>
--verify flag auto-verifies on BaseScan (requires API key)
Explorers: basescan.org (mainnet), sepolia.basescan.org (testnet)
CDP Faucet docs: docs.cdp.coinbase.com/faucets
Common Issues
Error	Cause
nonce has already been used	Node sync incomplete
Transaction fails	Insufficient ETH for gas — claim from faucet
Verification fails	Wrong RPC endpoint for target network
Verification 403/unauthorized	Missing or invalid BaseScan API key
Weekly Installs
213
Repository
base/skills
GitHub Stars
66
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn