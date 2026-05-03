---
title: trade
url: https://skills.sh/coinbase/agentic-wallet-skills/trade
---

# trade

skills/coinbase/agentic-wallet-skills/trade
trade
Installation
$ npx skills add https://github.com/coinbase/agentic-wallet-skills --skill trade
Summary

Execute token swaps on Base network using flexible amount formats and built-in token aliases.

Supports three common token aliases (USDC, ETH, WETH) plus arbitrary contract addresses; amounts can be specified as dollar values, decimals, whole numbers, or atomic units with automatic decimal detection
Includes configurable slippage tolerance (in basis points) and JSON output option for programmatic integration
Requires wallet authentication via the authenticate-wallet skill; validates all user input to prevent shell injection before executing trades
SKILL.md
Trading Tokens

Use the npx awal@2.8.2 trade command to swap tokens on Base or Polygon via the CDP Swap API. You must be authenticated to trade.

Confirm wallet is initialized and authed
npx awal@2.8.2 status


If the wallet is not authenticated, refer to the authenticate-wallet skill.

Command Syntax
npx awal@2.8.2 trade <amount> <from> <to> [options]

Arguments
Argument	Description
amount	Amount to swap (see Amount Formats below)
from	Source token: alias (usdc, eth, pol) or contract address (0x...)
to	Destination token: alias (usdc, eth, pol) or contract address (0x...)
Amount Formats

The amount can be specified in multiple formats:

Format	Example	Description
Dollar prefix	'$1.00', '$0.50'	USD notation (decimals based on token)
Decimal	1.0, 0.50, 0.001	Human-readable with decimal point
Whole number	5, 100	Interpreted as whole tokens
Atomic units	500000	Large integers treated as atomic units

Auto-detection: Large integers without a decimal point are treated as atomic units. For example, 500000 for USDC (6 decimals) = $0.50.

Decimals: For known tokens (usdc=6, eth=18, pol=18), decimals are automatic. For arbitrary contract addresses, decimals are read from the token contract.

Options
Option	Description
-c, --chain <name>	Blockchain network: base, polygon (default: base)
-s, --slippage <n>	Slippage tolerance in basis points (100 = 1%)
--json	Output result as JSON
Token Aliases
Alias	Token	Decimals	Chain
usdc	USDC	6	base
eth	ETH	18	base
pol	POL	18	polygon

IMPORTANT: Always single-quote amounts that use $ to prevent bash variable expansion (e.g. '$1.00' not $1.00).

Input Validation

Before constructing the command, validate all user-provided values to prevent shell injection:

amount: Must match ^\$?[\d.]+$ (digits, optional decimal point, optional $ prefix). Reject if it contains spaces, semicolons, pipes, backticks, or other shell metacharacters.
from / to: Must be a known alias (usdc, eth, pol) or a valid 0x hex address (^0x[0-9a-fA-F]{40}$). Reject any other value.
slippage: Must be a positive integer (^\d+$).

Do not pass unvalidated user input into the command.

Examples
# Swap $1 USDC for ETH (dollar prefix — note the single quotes)
npx awal@2.8.2 trade '$1' usdc eth

# Swap 0.50 USDC for ETH (decimal format)
npx awal@2.8.2 trade 0.50 usdc eth

# Swap 500000 atomic units of USDC for ETH
npx awal@2.8.2 trade 500000 usdc eth

# Swap 0.01 ETH for USDC
npx awal@2.8.2 trade 0.01 eth usdc

# Swap with custom slippage (2%)
npx awal@2.8.2 trade '$5' usdc eth --slippage 200

# Swap using contract addresses (decimals read from chain)
npx awal@2.8.2 trade 100 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913 0x4200000000000000000000000000000000000006

# Get JSON output
npx awal@2.8.2 trade '$1' usdc eth --json

# Swap USDC for POL on Polygon
npx awal@2.8.2 trade '$1' usdc pol --chain polygon

Prerequisites
Must be authenticated (awal status to check)
Wallet must have sufficient balance of the source token
Error Handling

Common errors:

"Not authenticated" - Run awal auth login <email> first
"Invalid token" - Use a valid alias (usdc, eth, pol) or 0x address
"POL only supported on polygon chain" - Use --chain polygon when trading POL
"Cannot swap a token to itself" - From and to must be different
"Swap failed: TRANSFER_FROM_FAILED" - Insufficient balance or approval issue
"No liquidity" - Try a smaller amount or different token pair
"Amount has X decimals but token only supports Y" - Too many decimal places
Weekly Installs
2.4K
Repository
coinbase/agenti…t-skills
GitHub Stars
102
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn