---
rating: ⭐⭐⭐
title: aave
url: https://skills.sh/fibrous-finance/fibx-skills/aave
---

# aave

skills/fibrous-finance/fibx-skills/aave
aave
Installation
$ npx skills add https://github.com/fibrous-finance/fibx-skills --skill aave
SKILL.md
Aave V3 Management

Interact with the Aave V3 lending protocol on Base only. View market data, supply assets to earn yield, borrow against collateral, repay debt, or withdraw.

Prerequisites
Active session required for status, supply, borrow, repay, withdraw.
markets does not require authentication — it is a public on-chain query.
Sufficient ETH on Base for gas fees (transactional actions only).
Rules
This skill ONLY works on Base. NEVER attempt Aave operations on Citrea, HyperEVM, or Monad. If requested, refuse and explain.
BEFORE any action, run npx fibx@latest balance to verify enough ETH for gas.
BEFORE borrow, you MUST run npx fibx@latest aave status to check the Health Factor:
Health Factor < 1.5 → WARN the user about liquidation risk.
Health Factor < 1.1 → DO NOT proceed without explicit double-confirmation from the user.
When the user wants to fully close a position, ALWAYS use max as the amount for repay and withdraw. This sends MAX_UINT256 to the contract.
Auto-Wrap/Unwrap: When supplying, repaying, or withdrawing ETH, the CLI automatically handles the ETH ↔ WETH conversion. You can safely use ETH as the token symbol for these actions.
Commands
npx fibx@latest aave <action> [amount] [token] [--simulate] [--json]

Actions
Action	Description	Example
status	Account health, LTV, net worth	npx fibx@latest aave status
markets	List all active reserves with APY & TVL	npx fibx@latest aave markets
supply	Deposit assets (auto-wraps ETH)	npx fibx@latest aave supply 1 ETH
borrow	Borrow against collateral	npx fibx@latest aave borrow 50 USDC
repay	Repay debt (auto-wraps ETH)	npx fibx@latest aave repay max ETH
withdraw	Withdraw assets (auto-unwraps WETH -> ETH)	npx fibx@latest aave withdraw max ETH
Parameters
Parameter	Type	Description	Required
action	string	status, markets, supply, borrow, repay, or withdraw	Yes
amount	string	Amount or max (for full repay/withdraw)	Yes (except status/markets)
token	string	Token symbol (USDC, ETH, DAI, etc.)	Yes (except status/markets)
simulate	flag	Estimate gas without executing the transaction	No
json	flag	Output as JSON	No
Dust Handling

When repaying or withdrawing, always prefer max if the user wants to fully close a position.

Passing max sends MAX_UINT256 to the Aave contract, which covers all accrued interest and prevents tiny residual balances (e.g. 0.000001 USDC) from remaining.

npx fibx@latest aave repay max USDC      # Repays all debt including accrued interest
npx fibx@latest aave withdraw max USDC   # Withdraws entire supplied position

Examples

User: "What markets are available on Aave?"

npx fibx@latest aave markets


User: "How is my Aave position doing?"

npx fibx@latest aave status


User: "Supply 1 ETH to Aave"

npx fibx@latest balance
npx fibx@latest aave supply 1 ETH


User: "How much gas would supplying 1 ETH cost?"

npx fibx@latest aave supply 1 ETH --simulate


User: "Borrow 100 USDC"

npx fibx@latest aave status
# If Health Factor > 1.5:
npx fibx@latest aave borrow 100 USDC


User: "Repay my ETH debt"

npx fibx@latest aave repay max ETH

Error Handling
Error	Action
Health Factor too low	Blocked to prevent liquidation. Suggest repaying or supplying.
Insufficient collateral	Cannot borrow without supplying first.
Insufficient balance	Check balance — user may need to swap for the token first.
Not authenticated	Run authenticate-wallet skill first.
Rate limit / 429	Use config skill to set a custom RPC.
Related Skills
Use trade to swap tokens before supplying (e.g. swap ETH → USDC, then supply USDC).
Use balance to verify available assets before any Aave operation.
Use portfolio to see Aave positions alongside all token holdings with USD values.
Use config to set a custom RPC if you encounter rate limit errors.
Weekly Installs
26
Repository
fibrous-finance…x-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn