---
title: evm-swiss-knife
url: https://skills.sh/kukapay/crypto-skills/evm-swiss-knife
---

# evm-swiss-knife

skills/kukapay/crypto-skills/evm-swiss-knife
evm-swiss-knife
Installation
$ npx skills add https://github.com/kukapay/crypto-skills --skill evm-swiss-knife
SKILL.md
EVM Swiss Knife

This skill enables interaction with EVM-compatible blockchains through Foundry's cast command-line tool. It covers common blockchain operations like balance queries, contract calls, transaction sending, and network inspection.

Installation

To use this skill, you need Foundry installed, which provides the cast command.

Follow the official installation guide: https://getfoundry.sh/introduction/installation

Quick Install (Linux/Mac)

Install Foundryup:

curl -L https://foundry.paradigm.xyz | bash


Source your shell configuration or start a new terminal:

source ~/.bashrc  # or ~/.zshrc


Install Foundry:

foundryup


Verify installation:

cast --version


For other platforms or detailed instructions, see the full guide at https://getfoundry.sh/introduction/installation

Prerequisites
Foundry installed (cast command available)
RPC endpoint configured (via --rpc-url or environment variables)
Private key for transaction operations (if sending txs)
RPC URL Selection

To interact with different EVM networks, you need reliable RPC endpoints. Use ChainList's API at https://chainlist.org/rpcs.json to get a comprehensive JSON list of RPC URLs for all supported chains.

How to Select RPC URLs:

Fetch the RPC data:

curl -s https://chainlist.org/rpcs.json | jq '.[] | select(.chainId == 1)'  # For Ethereum (chain ID 1)


Look for RPC URLs that are:

Public and free: No API keys required
No or limited tracking: Avoid URLs with "tracking": "yes"
Fast and reliable: Prefer URLs with low latency or high score
Open source: Prefer community-maintained endpoints

Popular choices (extracted from ChainList):

Ethereum (ID 1): https://ethereum-rpc.publicnode.com
BNB Smart Chain (ID 56): https://bsc-dataseed.binance.org
Base (ID 8453): https://mainnet.base.org
Polygon (ID 137): https://polygon-rpc.com

For production use, consider paid RPC services like Alchemy, Infura, or QuickNode for higher reliability and rate limits.

Always verify the chain ID matches your intended network to avoid connecting to wrong chains.

Common Operations
Query Account Balance

Get ETH balance of an address:

cast balance <address> --rpc-url <rpc_url>


Get ERC20 token balance:

cast call <token_contract> "balanceOf(address)(uint256)" <address> --rpc-url <rpc_url>

Call Contract Functions (Read-Only)

Call a view/pure function:

cast call <contract_address> "<function_signature>" [args...] --rpc-url <rpc_url>


Example - get token total supply:

cast call 0xA0b86a33E6441e88C5F2712C3E9b74B6F3f5a8b8 "totalSupply()(uint256)" --rpc-url <rpc_url>

Send Transactions

Send ETH:

cast send --private-key <pk> --rpc-url <rpc_url> <to_address> --value <amount_in_wei>


Call contract function (write):

cast send --private-key <pk> --rpc-url <rpc_url> <contract_address> "<function_signature>" [args...]

Blockchain Inspection

Get latest block number:

cast block-number --rpc-url <rpc_url>


Get block details:

cast block <block_number> --rpc-url <rpc_url>


Get transaction details:

cast tx <tx_hash> --rpc-url <rpc_url>

Contract Deployment

Deploy a contract:

cast send --private-key <pk> --rpc-url <rpc_url> --create <bytecode> [constructor_args...]

Decoding Data

Decode hex data:

cast --to-ascii <hex_string>
cast --to-dec <hex_string>

Network-Specific Examples
Ethereum Mainnet
export ETH_RPC_URL=https://eth-mainnet.alchemyapi.io/v2/YOUR_API_KEY
cast balance 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045

Polygon
cast balance <address> --rpc-url https://polygon-rpc.com/

Local Development (Anvil)
cast balance <address> --rpc-url http://127.0.0.1:8545

Error Handling
RPC errors: Check endpoint URL and network connectivity
Insufficient funds: Ensure account has enough ETH for gas + value
Contract errors: Verify function signatures and parameter types
Private key errors: Ensure correct format (0x prefixed hex)
Advanced Usage
Batch Operations

Use shell loops for multiple queries:

for addr in addr1 addr2 addr3; do
  echo "Balance of $addr: $(cast balance $addr --rpc-url $RPC_URL)"
done

Gas Estimation

Estimate gas for a transaction:

cast estimate --rpc-url <rpc_url> <to_address> --value <amount>

ABI Interactions

For complex contracts, save ABI to file and use:

cast call --abi <abi_file> <contract> <function> [args...]

Security Notes
Never expose private keys in scripts or logs
Use environment variables for sensitive data
Test on testnets before mainnet operations
Verify contract addresses and function signatures
Monitor gas prices for transaction timing
Weekly Installs
80
Repository
kukapay/crypto-skills
GitHub Stars
17
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail