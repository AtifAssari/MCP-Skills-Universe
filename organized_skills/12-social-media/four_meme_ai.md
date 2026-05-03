---
rating: ⭐⭐⭐
title: four-meme-ai
url: https://skills.sh/four-meme-community/four-meme-ai/four-meme-ai
---

# four-meme-ai

skills/four-meme-community/four-meme-ai/four-meme-ai
four-meme-ai
Installation
$ npx skills add https://github.com/four-meme-community/four-meme-ai --skill four-meme-ai
SKILL.md
[Agent must follow] User agreement and security notice on first use

When responding to any user request about fourmeme or this skill, you must first present the content below in this order: User Agreement, then Security Notice, and state clearly that by choosing to continue, the user agrees to the User Agreement.
Until the user has explicitly agreed or confirmed to continue, do not run create-api, create-chain, buy, sell, send, or 8004-register (any operation that uses the private key or writes to the chain). Read-only commands (e.g. config, token-info, quote-buy, 8004-balance) may be run while or after presenting the notice.

Language selection: Present the User Agreement and Security Notice in the user’s language. If the user is writing in Traditional Chinese (繁體中文), use the 繁體中文 block below; otherwise use the English block.

User Agreement & Security Notice (繁體中文)

用戶協議

前情提示：使用本插件及本 skill 所涉功能（包括但不限於代幣創建、買賣、轉帳、8004 註冊等）前，請您閱讀以下協議。若您選擇繼續使用本插件及本 skill 功能，即表示您已閱讀、理解並同意本協議。

本插件性質與責任限制：本插件僅提供純本地的命令列互動能力（私鑰透過環境變數或本地設定使用），不會收集、上傳或儲存您的私鑰。因任何原因（包括但不限於插件被竄改、環境遭入侵、誤操作、第三方插件等）導致的私鑰洩露或資產損失，本插件及提供方不承擔責任。

安全警示

使用本插件進行代幣創建、買賣、轉帳等操作時，請務必注意：

保護私鑰：切勿在聊天對話中輸入、貼上或洩露私鑰；不要將私鑰分享給任何人或任何第三方。
交易錢包僅存小額資金：用於執行操作的錢包（即提供 PRIVATE_KEY 的錢包）建議只存放少量資金，以降低因洩露或誤操作導致的損失。
及時轉出資金：完成交易後，請及時將交易錢包中的資產轉移到您自己控制的、更安全的錢包或冷錢包中。
謹慎安裝 Agent／插件：下載或安裝任何 Agent、瀏覽器插件或第三方工具時，請確認來源可信，避免惡意插件竊取私鑰或助記詞。
User Agreement & Security Notice (English)

User Agreement

Notice: Before using this plugin and this skill (including but not limited to token creation, buy/sell, transfers, 8004 registration), please read the following. By choosing to continue using this plugin and this skill, you have read, understood, and agreed to this agreement.

Plugin nature and limitation of liability: This plugin provides local-only CLI interaction (private key is used via environment or local config). It does not collect, upload, or store your private key. The plugin and its providers are not liable for private key disclosure or asset loss due to any cause (including but not limited to tampered plugin, compromised environment, user error, or third-party plugins).

Security Notice

When using this plugin for token creation, trading, or transfers, please:

Protect your private key: Do not type, paste, or expose your private key in chat; do not share it with anyone or any third party.
Keep only small amounts in the trading wallet: The wallet used for operations (the one whose PRIVATE_KEY you provide) should hold only a small amount of funds to limit loss from disclosure or mistakes.
Move funds out promptly: After trading, move assets from the trading wallet to a wallet or cold storage you control.
Install agents/plugins carefully: When installing any agent, browser extension, or third-party tool, verify the source to avoid malware that could steal your private key or seed phrase.
fourmeme capability overview

After you agree to the above and confirm to continue, this skill can help you with the following (all via the fourmeme CLI on BSC):

Category	Capability	Description
Create	Create token	Upload image + name/symbol/description/label; optional tax-token params; API returns signature then on-chain create.
Query	Public config	Get raisedToken and other public config (no auth).
Query	Token info (on-chain)	By address: version, tokenManager, price, offers (Helper3).
Query	Token list / detail / rankings	REST: filtered paginated list, single-token detail and trading info, hot/24h volume/newest/graduated rankings.
Trading	Buy/sell quotes	Estimate cost or proceeds for buy or sell (no transaction sent).
Trading	Execute buy	Buy a given token by amount or by quote spent (requires PRIVATE_KEY).
Trading	Execute sell	Sell a given token amount; optional minimum quote received (requires PRIVATE_KEY).
Other	Event listening	Fetch TokenCreate, TokenPurchase, TokenSale, LiquidityAdded on-chain.
Other	Tax token fees	Query on-chain fee and burn/dividend/liquidity config for a token.
Other	Send	Send BNB or ERC20 to a given address (requires PRIVATE_KEY).
Other	EIP-8004	Register 8004 identity NFT; query balance by address.

See the CLI (fourmeme) table and sections below for commands and arguments.

fourmeme CLI

BSC only; all commands output JSON.

CLI (fourmeme)

Installation (required): npm install -g @four-meme/four-meme-ai@latest. After install, run fourmeme <command> [args]; with local install only, use npx fourmeme <command> [args] from the project root. Run fourmeme --help for usage.

This skill provides: token creation (API + chain), buy/sell quotes and execution, token info/list/rankings, event listening, Tax token fee queries, send, and EIP-8004 identity NFT register and balance. Contract addresses: references/contract-addresses.md. TokenManager V1 is not supported.

PRIVATE_KEY and BSC_RPC_URL

When using OpenClaw
This skill declares requires.env: ["PRIVATE_KEY"] and primaryEnv: "PRIVATE_KEY" in metadata; OpenClaw injects them only when an agent runs with this skill enabled (other skills cannot access them).

Required steps:

Configure private key: In the Skill management page, set the four-meme-ai skill’s apiKey (corresponds to primaryEnv: "PRIVATE_KEY"), or set PRIVATE_KEY under skills.entries["four-meme-ai"].env in ~/.openclaw/openclaw.json. Optionally set BSC_RPC_URL in global env if needed.
Enable this skill: In the agent or session, ensure the four-meme-ai skill is enabled. Only when the skill is enabled will OpenClaw inject PRIVATE_KEY into the process; otherwise create/buy/sell/send/8004-register will fail with missing key. BSC_RPC_URL is optional (metadata: optionalEnv); if not set, scripts use a default BSC RPC.

When not using OpenClaw (standalone)
Set PRIVATE_KEY and optionally BSC_RPC_URL via the process environment so they are available when running npx fourmeme or node bin/fourmeme.cjs:

.env file: Put a .env file in the directory where you run the fourmeme command (i.e. your project / working directory). Example: if you run fourmeme quote-buy ... from /path/to/my-project, place .env at /path/to/my-project/.env. The CLI automatically loads .env from that current working directory. Use lines like PRIVATE_KEY=... and BSC_RPC_URL=.... Do not commit .env; add it to .gitignore.
Shell export: export PRIVATE_KEY=your_hex_key and export BSC_RPC_URL=https://bsc-dataseed.binance.org (or another BSC RPC), then run npx fourmeme <command> ....
Declared and optional environment variables
Declared in registry metadata (injected by OpenClaw when skill is enabled): PRIVATE_KEY (required for write operations). Optional in metadata: BSC_RPC_URL (scripts fall back to default BSC RPC if unset).
Not in metadata; optional, may be set in env or project .env: BSC_RPC_URL, CREATION_FEE_WEI (extra BNB on create), WEB_URL, TWITTER_URL, TELEGRAM_URL, PRE_SALE, FEE_PLAN, 8004_NFT_ADDRESS / EIP8004_NFT_ADDRESS. Only PRIVATE_KEY is required for signing; others have defaults or are used only for specific commands (see Create token flow, EIP-8004, etc.). Tax token params use CLI only (--tax-options= or --tax-token --tax-fee-rate=...).
Execution and install
Invocation: The agent must run commands only via the fourmeme CLI: fourmeme <command> [args] or npx fourmeme <command> [args] (allowed-tools). Do not invoke scripts or npx tsx directly; the CLI entry (bin/fourmeme.cjs) dispatches to the correct script and loads .env from the current working directory.
Need	Command	When
Public config	fourmeme config	Get raisedToken / config (no auth)
Token info (on-chain)	fourmeme token-info <tokenAddress>	Version, tokenManager, price, offers (BSC Helper3)
Token list (REST)	fourmeme token-list — POST /public/token/search; legacy flags [--orderBy=] … plus legacy `--queryMode=Binance	USD1(inferslistType), or new [--type=] [--listType=] [--keyword=] [--tag=] [--status=] [--sort=] [--version=]`
Token detail (REST)	fourmeme token-get <tokenAddress>	Token detail and trading info (get/v2)
Token rankings (REST)	`fourmeme token-rankings <orderBy	type> [--barType=…]`
Buy quote	fourmeme quote-buy <token> <amountWei> [fundsWei]	Estimate only; no transaction
Sell quote	fourmeme quote-sell <token> <amountWei>	Estimate only; no transaction
Execute buy	fourmeme buy <token> amount <amountWei> <maxFundsWei>	Buy fixed amount (needs PRIVATE_KEY)
Execute buy	fourmeme buy <token> funds <fundsWei> <minAmountWei>	Spend fixed quote (e.g. BNB) (needs PRIVATE_KEY)
Execute sell	fourmeme sell <token> <amountWei> [minFundsWei]	Sell (needs PRIVATE_KEY)
Send	fourmeme send <toAddress> <amountWei> [tokenAddress]	Send BNB or ERC20 to address (needs PRIVATE_KEY)
EIP-8004 register	fourmeme 8004-register <name> [imageUrl] [description]	Register 8004 identity NFT (needs PRIVATE_KEY)
EIP-8004 query	fourmeme 8004-balance <ownerAddress>	Query 8004 NFT balance (read-only)
Events	fourmeme events <fromBlock> [toBlock]	TokenCreate / Purchase / Sale / LiquidityAdded
Tax token info	fourmeme tax-info <tokenAddress>	Fee/tax config for TaxToken
Read-only check	fourmeme verify	Run config + events (last 50 blocks)

Chain: BSC only (Arbitrum/Base not supported).

Create token (full flow)

1. Ask user for required information (must be done first)

Before calling create-instant, the Agent must ask the user for and confirm:

Info	Required	Description
Image path (imagePath)	Yes	Local logo path; jpeg/png/gif/bmp/webp
Token name (name)	Yes	Full token name
Token symbol (shortName)	Yes	e.g. MTK, DOGE
Description (desc)	Yes	Token description text
Label (label)	Yes	One of: Meme | AI | Defi | Games | Infra | De-Sci | Social | Depin | Charity | Others
Tax token?	No	If yes, ask for tokenTaxInfo (feeRate, four rates, recipientAddress, minSharing); see "tokenTaxInfo parameters" below

Optional: --web-url=, --twitter-url=, --telegram-url=, --pre-sale= (BNB), --fee-plan=; may be provided or left at defaults.

2. Technical flow (done by create-instant)

After collecting the above, execute in this order (handled by scripts or CLI):

Get nonce — POST /private/user/nonce/generate with body accountAddress, verifyType, networkCode (BSC).
Login — Sign You are sign in Meme {nonce} with wallet; POST /private/user/login/dex to get access_token.
Upload image — POST /private/token/upload with access_token in header and image as body; get imgUrl.
Create — fourmeme create-instant --image= --name= --short-name= --desc= --label= [options] runs API create and submits TokenManager2.createToken on BSC in one command.

Split flow (optional): Step 4 — GET /public/config for raisedToken; POST /private/token/create with name, shortName, desc, imgUrl, label, raisedToken, etc.; get createArg, signature. Step 5 — Call TokenManager2.createToken(createArg, sign) on BSC. Use fourmeme create-api then fourmeme create-chain for this split flow.

Commands: fourmeme create-instant --image= --name= --short-name= --desc= --label= [options] (recommended). Or split: fourmeme create-api ... then fourmeme create-chain <createArgHex> <signatureHex>. Full params: fourmeme --help. References: api-create-token.md, create-token-scripts.md, token-tax-info.md.

Tax token

Option 1: --tax-options=<path> — path to JSON file with { "tokenTaxInfo": { ... } }; fields see “tokenTaxInfo parameters” below.
Option 2: CLI: --tax-token --tax-fee-rate=5 --tax-burn-rate=0 --tax-divide-rate=0 --tax-liquidity-rate=100 --tax-recipient-rate=0 --tax-recipient-address= --tax-min-sharing=100000 (burn+divide+liquidity+recipient = 100). See references/token-tax-info.md.

tokenTaxInfo parameters (required for tax token, via JSON or CLI):

Field	Type	Description	Constraint
feeRate	number	Trading fee rate (%)	Only 1, 3, 5, 10
burnRate	number	Burn share (%)	Sum with next three = 100
divideRate	number	Dividend share (%)	Same
liquidityRate	number	Liquidity share (%)	Same
recipientRate	number	Recipient share (%)	0 if unused
recipientAddress	string	Recipient address	"" if unused
minSharing	number	Min balance for dividend (ether units)	d×10ⁿ, n≥5, 1≤d≤9; e.g. 100000, 1000000

Example (5% fee, 20% burn, 30% dividend, 40% liquidity, 10% recipient):

{
  "tokenTaxInfo": {
    "feeRate": 5,
    "burnRate": 20,
    "divideRate": 30,
    "liquidityRate": 40,
    "recipientRate": 10,
    "recipientAddress": "0x1234567890123456789012345678901234567890",
    "minSharing": 100000
  }
}

token-info
fourmeme token-info <tokenAddress>


On-chain query (Helper3); returns version, tokenManager, price, offers, etc.

token-list / token-get / token-rankings (REST)

Four.meme REST API; use Accept: application/json; no login or cookie.

Token list (filter / paginate) — POST /public/token/search

fourmeme token-list [--orderBy=Hot] [--pageIndex=1] [--pageSize=30] [--tokenName=] [--symbol=] [--labels=] [--listedPancake=false]
fourmeme token-list [--type=HOT] [--listType=NOR] [--keyword=] [--tag=Meme,AI] [--status=PUBLISH|TRADE|ALL] [--sort=DESC] [--version=]
fourmeme token-list [--queryMode=Binance|USD1] [--listedPancake=true|false]  (legacy shortcut; infers listType BIN/BIN_DEX or USD1/USD1_DEX)


Legacy listedPancake=false maps to status=PUBLISH; use --status=ALL when you need all statuses.

Token detail and trading info

fourmeme token-get <tokenAddress>


API: GET /private/token/get/v2?address=...

Rankings — POST /public/token/ranking

fourmeme token-rankings <orderBy|type> [--barType=HOUR24] [--pageSize=20] [--symbol=] [--version=] [--rankingKind=] [--minCap=] [--maxCap=] [--minVol=] [--maxVol=] [--minHold=] [--maxHold=] …


Legacy orderBy: Time → NEW | ProgressDesc | TradingDesc (volume window via --barType: HOUR24→VOL_DAY_1, HOUR4, HOUR1, MIN30, MIN5) | Hot | Graduated → DEX. Or pass API type directly (e.g. VOL_DAY_1, CAP, BURN). Output JSON.

quote-buy / quote-sell (estimate only; no transaction)
fourmeme quote-buy <tokenAddress> <amountWei> [fundsWei]
fourmeme quote-sell <tokenAddress> <amountWei>

amountWei: token amount (use 0 when buying by quote amount); fundsWei: quote to spend (omit or 0 when buying by token amount).
buy / sell (execute; requires PRIVATE_KEY)

Buy (one of):

By amount: fourmeme buy <token> amount <amountWei> <maxFundsWei> (spend at most maxFundsWei to buy amountWei tokens).
By funds: fourmeme buy <token> funds <fundsWei> <minAmountWei> (spend fundsWei quote, receive at least minAmountWei tokens).

Sell: Script performs approve then sell.

fourmeme sell <tokenAddress> <amountWei> [minFundsWei]

minFundsWei optional (slippage: minimum quote received). V2 tokens only.
send (send BNB or ERC20 to an address)

Send native BNB or ERC20 from the current wallet (PRIVATE_KEY) to a given address (BSC).

fourmeme send <toAddress> <amountWei> [tokenAddress]

Argument	Description
toAddress	Recipient address (0x...)
amountWei	Amount in wei (BNB or token smallest unit)
tokenAddress	Optional. Omit or use BNB / 0x0 for native BNB; otherwise ERC20 contract address
Env: PRIVATE_KEY. Optional: BSC_RPC_URL.
Output: JSON with txHash, to, amountWei, native (whether BNB).

Examples:

# Send 0.1 BNB (1e17 wei)
fourmeme send 0x1234...abcd 100000000000000000

# Send 1000 units of an ERC20 (18 decimals)
fourmeme send 0x1234...abcd 1000000000000000000000 0xTokenContractAddress

EIP-8004 identity NFT (register and query)

EIP-8004 identity NFT: register (mint) and query balance. Default contract: 0x8004A169FB4a3325136EB29fA0ceB6D2e539a432 (BSC). Override with env 8004_NFT_ADDRESS or EIP8004_NFT_ADDRESS.

Register: Requires PRIVATE_KEY. User provides name (required), image URL (optional), description (optional). CLI builds EIP-8004 payload (type, name, description, image, active, supportedTrust), encodes as data:application/json;base64,<base64> for agentURI, and calls register(string agentURI).

fourmeme 8004-register <name> [imageUrl] [description]

Argument	Description
name	Required. Identity name
imageUrl	Optional. Avatar/image URL (must be publicly reachable)
description	Optional. Description
Output JSON: txHash, agentId (from event), agentURI.

Query: Read-only; number of 8004 NFTs held by an address.

fourmeme 8004-balance <ownerAddress>

Output JSON: owner, balance.

Examples:

fourmeme 8004-register "myagent" "https://example.com/logo.png" "My agent description"
fourmeme 8004-balance 0x1234567890123456789012345678901234567890

events (TokenManager2 V2 only)

Fetch TokenCreate, TokenPurchase, TokenSale, LiquidityAdded on BSC.

fourmeme events <fromBlock> [toBlock]


Omit toBlock for latest. Real-time subscription: references/event-listening.md.

tax-info (TaxToken fee/tax)

Only for TaxToken (creatorType 5).

fourmeme tax-info <tokenAddress>


See references/tax-token-query.md.

Agent workflow: buy/sell from rankings or events

This skill supports a flow to discover tokens, get details, quote, and execute. The following is an example workflow, not a trading recommendation: discover → detail → quote → execute.

Discover (one or more of):
Rankings: fourmeme token-rankings <orderBy or type> (legacy: Hot, TradingDesc, Time, ProgressDesc, Graduated; or e.g. VOL_DAY_1); use token addresses from the response.
List: fourmeme token-list (/public/token/search) with --orderBy / --type, --labels / --tag, etc., to filter and get addresses.
On-chain events: fourmeme events <fromBlock> [toBlock]; parse token addresses from TokenCreate/TokenPurchase, etc., for "newly created" or "recent trades" strategies.
Get details: For each candidate, call fourmeme token-get <address> (REST detail and trading info) or fourmeme token-info <address> (on-chain version, tokenManager, price, offers) to filter or display.
Quote: fourmeme quote-buy <token> <amountWei> [fundsWei] / fourmeme quote-sell <token> <amountWei> for estimated cost or proceeds.
Execute: fourmeme buy ... / fourmeme sell ... (requires PRIVATE_KEY). Before executing, the Agent must confirm user intent (e.g. user said "buy 0.05 BNB each for top 5 by 24h volume" or "auto-buy 0.01 BNB for new tokens") and obtain explicit confirmation before first automated execution to avoid unauthorized use of funds.

When the user asks to "buy/sell based on rankings or activity", the Agent should clarify: which ranking (hot, 24h volume, newest, graduated, etc.), amount per token, and whether to quote only or also execute; then run the appropriate commands.

Trading (Buy / Sell)
Version – Use TokenManagerHelper3 getTokenInfo(token). If version === 1 use V1 TokenManager; if version === 2 use TokenManager2 (and check for X Mode / TaxToken / AntiSniperFeeMode if needed).
Quote (pre-calc) – TokenManagerHelper3:
Buy: tryBuy(token, amount, funds) – use amount > 0 for "buy X tokens", or funds > 0 for "spend X quote".
Sell: trySell(token, amount).
Execute – Use the tokenManager address from getTokenInfo and call the corresponding contract:
V1: purchaseToken / purchaseTokenAMAP, saleToken.
V2: buyToken / buyTokenAMAP, sellToken. For sell, user must ERC20.approve(tokenManager, amount) first.
X Mode tokens: use TokenManager2 buyToken(bytes args, uint256 time, bytes signature) with encoded BuyTokenParams.
API and config reference
Token detail (REST): GET /private/token/get?address=<token>, GET /private/token/getById?id=<requestId> (requestId from TokenCreate event). Response may include data.aiCreator (token created by Agent). List/rankings: references/token-query-api.md.
Agent Creator / Agent wallets: On-chain — token template bit 85 for “created by agent”; AgentIdentifier contract (isAgent(wallet)) on BSC to identify agent wallets. See references/agent-creator-and-wallets.md and references/contract-addresses.md.
raisedToken: GET https://four.meme/meme-api/v1/public/config for current raisedToken; use as-is in create body; do not modify its fields.
References
Document	Description
contract-addresses.md	TokenManager / TokenManager2 / Helper3 addresses (BSC)
api-create-token.md	Create token API (nonce / login / upload / create)
create-token-scripts.md	Create token script flow and examples
token-tax-info.md	Tax token tokenTaxInfo parameters and constraints
token-query-api.md	Token list / detail / rankings REST API
errors.md	buy/sell error codes; X Mode / TaxToken / AntiSniperFeeMode; Agent Creator
agent-creator-and-wallets.md	Token created by Agent Creator; AgentIdentifier contract and Agent wallets
execute-trade.md	Execute buy/sell CLI and contract usage
event-listening.md	TokenManager2 event listening (V2)
tax-token-query.md	TaxToken on-chain fee/tax query (tax-info)
Official four.meme API and contracts (online): Protocol Integration	API documents, ABIs: TokenManager, TokenManager2, Helper3, TaxToken, AgentIdentifier, etc.
Weekly Installs
287
Repository
four-meme-commu…-meme-ai
GitHub Stars
13
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn