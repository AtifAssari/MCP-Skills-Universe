---
rating: ⭐⭐⭐
title: moralis-data-api
url: https://skills.sh/moralisweb3/onchain-skills/moralis-data-api
---

# moralis-data-api

skills/moralisweb3/onchain-skills/moralis-data-api
moralis-data-api
Installation
$ npx skills add https://github.com/moralisweb3/onchain-skills --skill moralis-data-api
SKILL.md
CRITICAL: Read Rule Files Before Implementing

The #1 cause of bugs is not reading the endpoint rule file before writing code.

For EVERY endpoint:

Read rules/{EndpointName}.md
Find "Example Response" section
Copy the EXACT JSON structure
Note field names (snake_case), data types, HTTP method, path, wrapper structure

Reading Order:

This SKILL.md (core patterns)
Endpoint rule file in rules/
Pattern references in references/ (for edge cases only)
Setup
API Key (optional)

Never ask the user to paste their API key into the chat. Instead:

Check if MORALIS_API_KEY is set in the environment (try running [ -n "$MORALIS_API_KEY" ] && echo "API key is set" || echo "API key is NOT set").
If not set, offer to create the .env file with an empty placeholder: MORALIS_API_KEY=
Tell the user to open the .env file and paste their key there themselves.
Let them know: without the key, you won't be able to test or call the Moralis API on their behalf.

If they don't have a key yet, point them to admin.moralis.com/register (free, no credit card).

Environment Variable Discovery

The .env file location depends on how skills are installed:

Create the .env file in the project root (same directory the user runs Claude Code from). Make sure .env is in .gitignore.

Verify Your Key
curl "https://deep-index.moralis.io/api/v2.2/YOUR_EVM_ADDRESS/balance?chain=0x1" \
  -H "X-API-Key: $MORALIS_API_KEY"

Base URLs
API	Base URL
EVM	https://deep-index.moralis.io/api/v2.2
Solana	https://solana-gateway.moralis.io
Authentication

All requests require: X-API-Key: $MORALIS_API_KEY

Quick Reference: Most Common Patterns
Data Type Rules
Field	Reality	NOT
block_number	Decimal 12386788	Hex 0xf2b5a4
timestamp	ISO "2021-05-07T11:08:35.000Z"	Unix 1620394115
balance	String "1000000000000000000"	Number
decimals	String or number	Always number
Block Numbers (always decimal)
block_number: 12386788; // number - use directly
block_number: "12386788"; // string - parseInt(block_number, 10)

Timestamps (usually ISO strings)
"2021-05-07T11:08:35.000Z"; // → new Date(timestamp).getTime()

Balances (always strings unless its a property named "formatted" eg. balanceFormatted, BigInt)
balance: "1000000000000000000";
// → (Number(BigInt(balance)) / 1e18).toFixed(6)

Response Patterns
Pattern	Example Endpoints
Direct array [...]	getWalletTokenBalancesPrice, getTokenMetadata
Wrapped { result: [] }	getWalletNFTs, getWalletTransactions
Paginated { page, cursor, result }	getWalletHistory, getNFTTransfers
// Safe extraction
const data = Array.isArray(response) ? response : response.result || [];

Common Field Mappings
token_address → tokenAddress
from_address_label → fromAddressLabel
block_number → blockNumber
receipt_status: "1" → success, "0" → failed
possible_spam: "true"/"false" → boolean check

Common Pitfalls (Top 5)
Block numbers are decimal, not hex - Use parseInt(x, 10), not parseInt(x, 16)
Timestamps are ISO strings - Use new Date(timestamp).getTime()
Balances are strings - Use BigInt(balance) for math
Response may be wrapped - Check for .result before .map()
Path inconsistencies - Some use /wallets/{address}/..., others /{address}/...

See references/CommonPitfalls.md for complete reference.

Pagination

Many endpoints use cursor-based pagination:

# First request
curl "...?limit=100" -H "X-API-Key: $KEY"

# Next page
curl "...?limit=100&cursor=<cursor_from_response>" -H "X-API-Key: $KEY"


See references/Pagination.md for details.

Testing Endpoints
ADDRESS="YOUR_EVM_ADDRESS"
CHAIN="0x1"

# Wallet Balance
curl "https://deep-index.moralis.io/api/v2.2/${ADDRESS}/balance?chain=${CHAIN}" \
  -H "X-API-Key: $MORALIS_API_KEY"

# Token Price
curl "https://deep-index.moralis.io/api/v2.2/erc20/YOUR_EVM_ADDRESS/price?chain=${CHAIN}" \
  -H "X-API-Key: $MORALIS_API_KEY"

# Wallet Transactions (note result wrapper)
curl "https://deep-index.moralis.io/api/v2.2/${ADDRESS}?chain=${CHAIN}&limit=5" \
  -H "X-API-Key: $MORALIS_API_KEY" | jq '.result'

Quick Troubleshooting
Issue	Cause	Solution
"Property does not exist"	Field name mismatch	Check snake_case in rule file
"Cannot read undefined"	Missing optional field	Use ?. optional chaining
"blockNumber is NaN"	Parsing decimal as hex	Use radix 10: parseInt(x, 10)
"Wrong timestamp"	Parsing ISO as number	Use new Date(timestamp).getTime()
"404 Not Found"	Wrong endpoint path	Verify path in rule file
Performance & Timeouts

Most endpoints respond quickly under normal conditions. Response times can vary based on wallet activity volume, chain, and query complexity.

Recommended client timeouts:

Simple queries (balance, price, metadata): 10s
Complex queries (wallet history, DeFi positions): 30s

Large wallets with extensive transaction histories may take longer — use pagination with reasonable limit values.

See references/PerformanceAndLatency.md for optimization tips.

Default Chain Behavior

EVM addresses (0x...): Default to Ethereum (chain=0x1) unless specified.

Solana addresses (base58): Auto-detected and routed to Solana API.

Supported Chains

EVM (40+ chains): Ethereum (0x1), Polygon (0x89), BSC (0x38), Arbitrum (0xa4b1), Optimism (0xa), Base (0x2105), Avalanche (0xa86a), and more.

Solana: Mainnet, Devnet

See references/SupportedApisAndChains.md for full list.

Endpoint Catalog

Complete list of all 136 endpoints (102 EVM + 34 Solana) organized by category.

Wallet

Balances, tokens, NFTs, transaction history, profitability, and net worth data.

Endpoint	Description
getNativeBalance	Get native balance by wallet
getNativeBalancesForAddresses	Get native balance for a set of wallets
getWalletActiveChains	Get active chains by wallet address
getWalletApprovals	Get ERC20 approvals by wallet
getWalletHistory	Get the complete decoded transaction history of a wallet
getWalletInsight	Get wallet insight metrics
getWalletNetWorth	Get wallet net worth
getWalletNFTCollections	Get NFT collections by wallet address
getWalletNFTs	Get NFTs by wallet address
getWalletNFTTransfers	Get NFT Transfers by wallet address
getWalletProfitability	Get detailed profit and loss by wallet address
getWalletProfitabilitySummary	Get profit and loss summary by wallet address
getWalletStats	Get summary stats by wallet address
getWalletTokenBalancesPrice	Get token balances with prices by wallet address
getWalletTokenTransfers	Get ERC20 token transfers by wallet address
getWalletTransactions	Get native transactions by wallet
getWalletTransactionsVerbose	Get decoded transactions by wallet
Token

Token prices, metadata, pairs, DEX swaps, analytics, security scores, and sniper detection.

Endpoint	Description
getAggregatedTokenPairStats	Get aggregated token pair statistics by address
getHistoricalTokenScore	Get historical token score by token address
getMultipleTokenAnalytics	Get token analytics for a list of token addresses
getPairAddress	Get DEX token pair address
getPairReserves	Get DEX token pair reserves
getPairStats	Get stats by pair address
getSnipersByPairAddress	Get snipers by pair address
getSwapsByPairAddress	Get swap transactions by pair address
getSwapsByTokenAddress	Get swap transactions by token address
getSwapsByWalletAddress	Get swap transactions by wallet address
getTimeSeriesTokenAnalytics	Retrieve timeseries trading stats by token addresses
getTokenAnalytics	Get token analytics by token address
getTokenBondingStatus	Get the token bonding status
getTokenCategories	Get ERC20 token categories
getTokenHolders	Get a holders summary by token address
getTokenMetadata	Get ERC20 token metadata by contract
getTokenMetadataBySymbol	Get ERC20 token metadata by symbols
getTokenOwners	Get ERC20 token owners by contract
getTokenPairs	Get token pairs by address
getTokenScore	Get token score by token address
getTokenStats	Get ERC20 token stats
getTokenTransfers	Get ERC20 token transfers by contract address
NFT

NFT metadata, transfers, traits, rarity, floor prices, and trades.

Endpoint	Description
getContractNFTs	Get NFTs by contract address
getMultipleNFTs	Get Metadata for NFTs
getNFTBulkContractMetadata	Get metadata for multiple NFT contracts
getNFTByContractTraits	Get NFTs by traits
getNFTCollectionStats	Get summary stats by NFT collection
getNFTContractMetadata	Get NFT collection metadata
getNFTContractSalePrices	Get NFT sale prices by collection
getNFTContractTransfers	Get NFT transfers by contract address
getNFTFloorPriceByContract	Get NFT floor price by contract
getNFTFloorPriceByToken	Get NFT floor price by token
getNFTHistoricalFloorPriceByContract	Get historical NFT floor price by contract
getNFTMetadata	Get NFT metadata
getNFTOwners	Get NFT owners by contract address
getNFTSalePrices	Get NFT sale prices by token
getNFTTokenIdOwners	Get NFT owners by token ID
getNFTTrades	Get NFT trades by collection
getNFTTradesByToken	Get NFT trades by token
getNFTTradesByWallet	Get NFT trades by wallet address
getNFTTraitsByCollection	Get NFT traits by collection
getNFTTraitsByCollectionPaginate	Get NFT traits by collection paginate
getNFTTransfers	Get NFT transfers by token ID
getTopNFTCollectionsByMarketCap	Get top NFT collections by market cap
DeFi

DeFi protocol positions, liquidity, and exposure data.

Endpoint	Description
getDefiPositionsByProtocol	Get detailed DeFi positions by protocol for a wallet
getDefiPositionsSummary	Get DeFi positions of a wallet
getDefiSummary	Get the DeFi summary of a wallet
Entity

Labeled addresses including exchanges, funds, protocols, and whales.

Endpoint	Description
getEntity	Get Entity Details By Id
getEntityCategories	Get Entity Categories
Price

Token and NFT prices, OHLCV candlestick data.

Endpoint	Description
getMultipleTokenPrices	Get Multiple ERC20 token prices
getPairCandlesticks	Get OHLCV by pair address
getPairPrice	Get DEX token pair price
getTokenPrice	Get ERC20 token price
Blockchain

Blocks, transactions, date-to-block conversion, and contract functions.

Endpoint	Description
getBlock	Get block by hash
getDateToBlock	Get block by date
getLatestBlockNumber	Get latest block number
getTransaction	Get transaction by hash
getTransactionVerbose	Get decoded transaction by hash
Discovery

Trending tokens, blue chips, market movers, and token discovery.

Endpoint	Description
getDiscoveryToken	Get token details
getTimeSeriesVolume	Retrieve timeseries trading stats by chain
getTimeSeriesVolumeByCategory	Retrieve timeseries trading stats by category
getTopCryptoCurrenciesByMarketCap	Get top crypto currencies by market cap
getTopCryptoCurrenciesByTradingVolume	Get top crypto currencies by trading volume
getTopERC20TokensByMarketCap	Get top ERC20 tokens by market cap
getTopERC20TokensByPriceMovers	Get top ERC20 tokens by price movements (winners and losers)
getTopGainersTokens	Get tokens with top gainers
getTopLosersTokens	Get tokens with top losers
getTopProfitableWalletPerToken	Get top traders for a given ERC20 token
getTrendingTokens	Get trending tokens
getVolumeStatsByCategory	Get trading stats by categories
getVolumeStatsByChain	Get trading stats by chain
Other

Utility endpoints including API version, endpoint weights, and address resolution.

Endpoint	Description
getBondingTokensByExchange	Get bonding tokens by exchange
getEntitiesByCategory	Get Entities By Category
getFilteredTokens	Returns a list of tokens that match the specified filters and criteria
getGraduatedTokensByExchange	Get graduated tokens by exchange
getHistoricalTokenHolders	Get timeseries holders data
getNewTokensByExchange	Get new tokens by exchange
getUniqueOwnersByCollection	Get unique wallet addresses owning NFTs from a contract.
resolveAddress	ENS lookup by address
resolveAddressToDomain	Resolve Address to Unstoppable domain
resolveDomain	Resolve Unstoppable domain
resolveENSDomain	ENS lookup by domain
reSyncMetadata	Resync NFT metadata
searchEntities	Search Entities, Organizations or Wallets
searchTokens	Search for tokens based on contract address, pair address, token name or token symbol.
Solana Endpoints

Solana-specific endpoints (24 native + 10 EVM variants that support Solana chain = 34 total).

Endpoint	Description
balance	Gets native balance owned by the given address
getAggregatedTokenPairStats	Get aggregated token pair statistics by address
getBondingTokensByExchange	Get bonding tokens by exchange
getCandleSticks	Get candlesticks for a pair address
getGraduatedTokensByExchange	Get graduated tokens by exchange
getHistoricalTokenHolders	Get token holders overtime for a given tokens
getMultipleTokenMetadata	Get multiple token metadata
getMultipleTokenPrices	Get token price
getNFTMetadata	Get the global metadata for a given contract
getNFTs	Gets NFTs owned by the given address
getNewTokensByExchange	Get new tokens by exchange
getPairStats	Get stats for a pair address
getPortfolio	Gets the portfolio of the given address
getSPL	Gets token balances owned by the given address
getSnipersByPairAddress	Get snipers by pair address.
getSwapsByPairAddress	Get all swap related transactions (buy, sell, add liquidity & remove liquidity)
getSwapsByTokenAddress	Get all swap related transactions (buy, sell)
getSwapsByWalletAddress	Get all swap related transactions (buy, sell) for a specific wallet address.
getTokenBondingStatus	Get Token Bonding Status
getTokenHolders	Get the summary of holders for a given token token.
getTokenMetadata	Get Token metadata
getTokenPairs	Get token pairs by address
getTokenPrice	Get token price
getTopHolders	Get paginated top holders for a given token.
getDiscoveryToken	Solana variant: Get token details
getHistoricalTokenScore	Solana variant: Get historical token score by token address
getTimeSeriesVolume	Solana variant: Retrieve timeseries trading stats by chain
getTimeSeriesVolumeByCategory	Solana variant: Retrieve timeseries trading stats by category
getTokenAnalytics	Solana variant: Get token analytics by token address
getTokenScore	Solana variant: Get token score by token address
getTopGainersTokens	Solana variant: Get tokens with top gainers
getTopLosersTokens	Solana variant: Get tokens with top losers
getTrendingTokens	Solana variant: Get trending tokens
getVolumeStatsByCategory	Solana variant: Get trading stats by categories
Reference Documentation
references/CommonPitfalls.md - Complete pitfalls reference
references/DataTransformations.md - Type conversion reference
references/FilteredTokens.md - Token discovery metrics, timeframes, filters, and examples
references/ApiResponseCodes.md - Common status codes and response field conventions
references/PerformanceAndLatency.md - Response time guidance, timeout recommendations, caching
references/ResponsePatterns.md - Pagination patterns
references/SpamDetection.md - Spam detection behavior and filtering guidance
references/SupportedApisAndChains.md - Chains and APIs
See Also
Endpoint rules: rules/*.md files
Streams API: @moralis-streams-api for real-time events
Weekly Installs
103
Repository
moralisweb3/onc…n-skills
GitHub Stars
8
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn