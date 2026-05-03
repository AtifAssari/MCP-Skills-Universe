---
rating: ⭐⭐⭐
title: web3-data
url: https://skills.sh/lxcong/web3-data-skill/web3-data
---

# web3-data

skills/lxcong/web3-data-skill/web3-data
web3-data
Installation
$ npx skills add https://github.com/lxcong/web3-data-skill --skill web3-data
SKILL.md
Web3 Data Explorer (Chainbase)

Query on-chain data via the Chainbase CLI.

Quick Reference

Install: npm install -g chainbase-cli (or use npx chainbase-cli)

Auth: Set API key via chainbase config set api-key YOUR_KEY, or env CHAINBASE_API_KEY. Falls back to demo key. If rate-limited, direct user to https://platform.chainbase.com to get a key.

x402 Payment: Supports pay-per-call micropayments via --x402 flag. Setup: chainbase config set private-key 0x...

# Top token holders
chainbase token top-holders 0xdAC17F958D2ee523a2206206994597C13D831ec7 --chain 1 --limit 10

# Token price
chainbase token price 0xdAC17F958D2ee523a2206206994597C13D831ec7

# ENS resolve
chainbase domain ens-resolve vitalik.eth

# SQL query
chainbase sql execute "SELECT * FROM ethereum.blocks ORDER BY number DESC LIMIT 5"


Use --json for machine-parseable output. Use --chain <id> to target a specific chain.

Chain IDs
Chain	ID	Chain	ID
Ethereum	1	Optimism	10
BSC	56	Base	8453
Polygon	137	zkSync	324
Avalanche	43114	Arbitrum	42161

Default to Ethereum (chain 1) unless user specifies otherwise.

Routing Logic

Match user intent to the right CLI command:

User wants	CLI command
Latest block number	chainbase block latest
Block details	chainbase block detail <number>
Transaction detail	chainbase tx detail <hash>
Wallet transaction history	chainbase tx list <address>
Token info (name, symbol, supply)	chainbase token metadata <contract>
Token price	chainbase token price <contract>
Historical token price	chainbase token price-history <contract> --from <ts> --to <ts>
List of holder addresses	chainbase token holders <contract>
Top token holders / who holds a token	chainbase token top-holders <contract>
Token transfer history	chainbase token transfers --contract <addr>
Native token balance (ETH/BNB)	chainbase balance native <address>
ERC20 token balances of wallet	chainbase balance tokens <address>
DeFi portfolio positions	chainbase balance portfolios <address>
ENS domains held by address	chainbase domain ens <address>
ENS name → address	chainbase domain ens-resolve <name>
Address → ENS name	chainbase domain ens-reverse <address>
Space ID resolve (BSC)	chainbase domain spaceid-resolve <domain>
Space ID reverse (BSC)	chainbase domain spaceid-reverse <address>
Call smart contract function	chainbase contract call --address <contract> --function "fn" --abi '[...]' --params '[...]'
Anything not covered above	SQL API: chainbase sql execute "SELECT ..."
Workflow
Identify intent — Determine what data the user needs
Resolve identifiers — If user gives token name (e.g. "USDT"), look up the contract address. Common tokens:
USDT: 0xdAC17F958D2ee523a2206206994597C13D831ec7 (ETH)
USDC: 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 (ETH)
WETH: 0xC02aaA39b223FE8D0A0e5c4F27eAD9083C756Cc2 (ETH)
DAI: 0x6B175474E89094C44Da98b954EedeAC495271d0F (ETH)
WBTC: 0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599 (ETH)
If unknown, use chainbase token metadata <contract> or ask the user for the contract address
Select command — Use the routing table above; fall back to SQL API for complex/custom queries
Execute — Run the CLI command. Add --json when you need to parse the output programmatically
Present results — Format data clearly with tables for lists, highlight key insights
Global Options

All commands support these options:

Option	Description	Default
--chain <id>	Target chain	1 (Ethereum)
--json	Machine-parseable JSON output	false
--page <n>	Page number for paginated results	1
--limit <n>	Results per page	20
--x402	Enable x402 micropayment mode	false
SQL API Fallback

When CLI commands don't cover the query, translate user intent to SQL:

chainbase sql execute "SELECT from_address, SUM(value) as total FROM ethereum.token_transfers WHERE contract_address = '0x...' GROUP BY from_address ORDER BY total DESC LIMIT 20"


Common table patterns (replace ethereum with chain name):

{chain}.blocks — Block data
{chain}.transactions — Transactions
{chain}.token_transfers — ERC20 transfers
{chain}.token_metas — Token metadata
{chain}.logs — Event logs

SQL constraints: max 100,000 results per query.

For full command help, run chainbase --help or chainbase <command> --help.

Crypto Social Intelligence (Tops)

Query crypto social signals via chainbase tops. No API key required — free to use.

Service: Tops — trending narratives, topic discovery, Twitter/X mentions. Base URL: https://api.chainbase.com/tops (called internally by the CLI) Rate limit: 10 req/s · 60 req/min · 600 req/hour (per client IP)

Quick Reference
# List trending crypto topics (default: English)
chainbase tops trending
chainbase tops trending --language zh   # Chinese
chainbase tops trending --language ko   # Korean

# Get structured details for a topic
chainbase tops topic <topic_id>

# Get posts/tweets under a topic
chainbase tops posts <topic_id>

# Search narrative candidates by keyword
chainbase tops search "RWA"
chainbase tops search "AI Agent"

# Search recent Twitter/X mentions
chainbase tops mentions "Ethereum ETF"


Use --json for machine-parseable output.

Routing Logic

Match user intent to the right subcommand:

User wants	CLI command
What's trending in crypto right now	chainbase tops trending [--language <lang>]
Details / summary of a specific topic	chainbase tops topic <topic_id>
Raw tweets / posts under a topic	chainbase tops posts <topic_id>
Find topics related to a narrative keyword	chainbase tops search <keyword>
Recent Twitter/X mentions of a project or keyword	chainbase tops mentions <keyword>
Workflow
Trend Tracking
chainbase tops trending → get current top topics (note id fields)
chainbase tops topic <id> → dive into summary, keywords, representative tweets
chainbase tops posts <id> → retrieve raw tweets for sentiment analysis
Narrative Discovery
chainbase tops search <keyword> → find candidate topics from a vague term
Cluster/summarize candidates, identify the target topic ID
chainbase tops topic <id> → confirm topic details
Real-time Monitoring
chainbase tops mentions <keyword> → monitor social mentions of a project/token
Extract stance, sentiment, key voices from results
Data Schemas

Story (topic): id, keyword, summary, score, current_rank, rank_status (new/up/down/same), is_new, authors[], tweet_urls[], first_tweet_time, snapshot_time

Tweet: id, text, media_json, user → {user_id, name, screen_name, blue_verified, profile_image}

Weekly Installs
34
Repository
lxcong/web3-data-skill
GitHub Stars
1
First Seen
8 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn