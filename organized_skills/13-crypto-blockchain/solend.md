---
rating: ⭐⭐
title: solend
url: https://skills.sh/alsk1992/cloddsbot/solend
---

# solend

skills/alsk1992/cloddsbot/solend
solend
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill solend
SKILL.md
Solend

Solend is a decentralized lending and borrowing protocol on Solana. Supply assets to earn interest, borrow against collateral, and monitor health to avoid liquidation.

Commands
Lending
/solend deposit <amount> <token>       Deposit collateral
/solend withdraw <amount|all> <token>  Withdraw collateral
/solend borrow <amount> <token>        Borrow assets
/solend repay <amount|all> <token>     Repay borrowed assets

Account
/solend obligation                     View your positions (deposits & borrows)
/solend health                         Check health factor & liquidation risk

Markets
/solend reserves                       List reserves with APY & utilization
/solend rates                          View supply/borrow interest rates table
/solend markets                        List available lending markets

Examples
/solend deposit 100 USDC
/solend borrow 1 SOL
/solend health
/solend repay all SOL
/solend withdraw all USDC
/solend reserves
/solend rates

Configuration
export SOLANA_PRIVATE_KEY="your-base58-private-key"
export SOLANA_RPC_URL="https://api.mainnet-beta.solana.com"  # Optional

See Also
/kamino — Kamino Finance lending + liquidity vaults
/marginfi — MarginFi lending protocol
/jup — Jupiter DEX aggregator
/bags — Portfolio overview
Weekly Installs
9
Repository
alsk1992/cloddsbot
GitHub Stars
194
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn