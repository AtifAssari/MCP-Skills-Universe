---
title: spot
url: https://skills.sh/htx-exchange/htx-skills-hub/spot
---

# spot

skills/htx-exchange/htx-skills-hub/spot
spot
Installation
$ npx skills add https://github.com/htx-exchange/htx-skills-hub --skill spot
SKILL.md
HTX Spot Skill

Spot trading on HTX using authenticated API endpoints. Requires API key and secret key for certain endpoints. Return the result in JSON format.

Quick Reference
Reference Data Endpoints
Endpoint	Description	Required	Optional	Authentication
GET /v2/market-status	Returns current market status with enum values including: 1=normal, 2=halted, 3=cancel-only	None	None	No
GET /v2/settings/common/symbols	Returns all supported trading symbols with detailed configuration including state, precision, and trading status	None	ts	No
GET /v2/settings/common/currencies	Returns all supported currencies with their configuration and display names	None	ts	No
GET /v1/settings/common/symbols	Returns symbol settings with pricing and trading precision information	None	None	No
GET /v1/settings/common/market-symbols	Returns market symbol configuration for spot trading	None	None	No
GET /v2/reference/currencies	Returns currency and blockchain chain reference data	None	None	No
GET /v1/common/timestamp	Returns current server timestamp in milliseconds	None	None	No
Market Data Endpoints
Endpoint	Description	Required	Optional	Authentication
GET /market/history/klines	Returns OHLC candlestick data for the specified symbol and time period	symbol, period	size, from	No
GET /market/detail	Returns the latest market ticker data for a symbol including price, volume, and 24h stats	symbol	None	No
GET /market/tickers	Returns latest ticker data for all trading pairs	None	None	No
GET /market/depth	Returns order book depth (bids and asks) for a symbol	symbol, type	None	No
GET /market/trade	Returns the latest trade data for a symbol	symbol	None	No
GET /market/history/trade	Returns recent trades for a symbol	symbol	size	No
GET /market/overview	Returns 24-hour market summary statistics for all symbols	None	None	No
GET /market/orderbook	Returns complete order book for a symbol with full depth	symbol	depth	No
Account Endpoints
Endpoint	Description	Required	Optional	Authentication
GET /v1/account/accounts	Returns all account details for the authenticated user	None	None	Yes
GET /v1/account/accounts/{account-id}/balance	Returns balance details for a specific account including assets and liabilities	account-id	None	Yes
GET /v2/account/valuation	Returns total asset valuation for all accounts in the user's portfolio	None	valuationCurrency	Yes
GET /v2/account/asset-valuation	Returns detailed asset valuation and portfolio composition	None	None	Yes
POST /v1/account/transfer	Transfers assets between accounts	from-account, to-account, currency, amount	None	Yes
GET /v1/account/history	Returns account history and transaction records	None	account-id, currency, type	Yes
POST /v1/futures/transfer	Transfers funds between spot trading account and futures contract account	currency, amount, type	None	Yes
GET /v1/point/account	Returns current HTX points balance and history	None	None	Yes
POST /v1/point/transfer	Transfers HTX points between accounts	from-user, to-user, amount	None	Yes
Trading Endpoints
Endpoint	Description	Required	Optional	Authentication
POST /v1/order/orders/place	Places a new spot trading order (limit or market)	account-id, amount, symbol, type	price, client-order-id, source, time-in-force	Yes
POST /v1/order/orders/{order-id}/cancel	Cancels a pending order	order-id	None	Yes
POST /v1/order/orders/batchcancel	Cancels multiple orders matching specified criteria	None	account-id, symbol	Yes
GET /v1/order/orders/{order-id}	Returns details of a specific order	order-id	None	Yes
GET /v1/order/orders	Returns orders matching specified criteria (open, closed, cancelled)	account-id	symbol, states, types, start-time, end-time, from, direct, size	Yes
GET /v1/order/orders/getClientOrder	Returns order details using client-order-id	client-order-id	None	Yes
GET /v1/order/matchresults	Returns trade history and fill details	None	symbol, types, start-time, end-time, from, direct, size	Yes
Margin Loan (Cross/Isolated) Endpoints
Endpoint	Description	Required	Optional	Authentication
POST /v1/margin/orders	Applies for a margin loan on cross or isolated margin account	currency, amount	account-id	Yes
POST /v1/margin/orders/{order-id}/repay	Repays a margin loan with interest	order-id, amount	None	Yes
GET /v1/margin/orders	Returns margin loan orders and their status	None	currency, state, from, size	Yes
GET /v1/margin/accounts/balance	Returns detailed balance information for margin accounts	None	account-id	Yes
Parameters
Common Parameters
symbol: Trading symbol (e.g., btcusdt, ethusdt)
symbols: Comma-separated list of symbols
account-id: Account ID (can be obtained from /v1/account/accounts)
type: Order type
amount: Order amount (for buy market orders, amount is in quote currency; for others, in base currency)
price: Order price (required for limit orders)
source: Order source (default: spot-api)
client-order-id: Client-defined order ID (max length: 64)
self-match-prevent: Self-match prevention (0=disabled, 1=enabled)
stop-price: Stop price for stop-limit orders
operator: Operator for stop orders (gte, lte)
order-id: Order ID
period: Kline period/interval
size: Number of records to return
depth: Depth level (e.g., step0, step1, step2, etc.)
side: Order side (buy, sell)
states: Order states (comma-separated)
types: Order types (comma-separated)
start-date: Start date (format: yyyy-mm-dd)
end-date: End date (format: yyyy-mm-dd)
start-time: Start time (unix timestamp in milliseconds)
end-time: End time (unix timestamp in milliseconds)
from: Start ID for pagination
direct: Direction for pagination (prev, next)
accountType: Account type for asset valuation
valuationCurrency: Currency for valuation (e.g., BTC, USDT, CNY)
transactTypes: Transaction types (comma-separated)
limit: Number of records to return
fromId: Starting ID for query
currency: Currency name (lowercase, e.g., btc, usdt)
show-desc: Show description (true, false)
ts: Timestamp for querying (optional)
authorizedUser: Authorized user flag (true, false)
Enums
period: 1min | 5min | 15min | 30min | 60min | 4hour | 1day | 1mon | 1week | 1year
type (order): buy-market | sell-market | buy-limit | sell-limit | buy-ioc | sell-ioc | buy-limit-maker | sell-limit-maker | buy-stop-limit | sell-stop-limit | buy-limit-fok | sell-limit-fok | buy-stop-limit-fok | sell-stop-limit-fok
side: buy | sell
states: submitted | partial-filled | partial-canceled | filled | canceled
operator: gte | lte
accountType: spot | margin | otc | point | super-margin | investment | borrow
transactTypes: trade | etf | transact-fee | deduction | transfer | credit | liquidation | interest | deposit-withdraw | withdraw-fee | exchange | other-types
depth (step): step0 | step1 | step2 | step3 | step4 | step5
Authentication

For endpoints that require authentication, you will need to provide HTX API credentials. Required credentials:

apiKey: Your HTX API key (for AccessKeyId parameter)
secretKey: Your HTX API secret (for signing)

Base URLs:

Mainnet: https://api.huobi.pro
Mainnet (AWS): https://api-aws.huobi.pro
Security
Share Credentials

Users can provide HTX API credentials by sending a file where the content is in the following format:

fe45419a...xyz
secretabc...key

Never Display Full Secrets

When showing credentials to users:

API Key: Show first 5 + last 4 characters: fe45419a...xyz
Secret Key: Always mask, show only last 5: ***...key1

Example response when asked for credentials:

Account: main
API Key: fe45419a...xyz
Secret: ***...key1
Environment: Mainnet

Listing Accounts

When listing accounts, show names and environment only — never keys:

HTX Accounts:
* main (Mainnet)
* trading (Mainnet - AWS)

Transactions in Mainnet

When performing transactions in mainnet, always confirm with the user before proceeding by asking them to write "CONFIRM" to proceed.

HTX Accounts
main
API Key: your_mainnet_api_key
Secret: your_mainnet_secret
Environment: https://api.huobi.pro
Description: Primary trading account
trading
API Key: your_aws_api_key
Secret: your_aws_secret
Environment: https://api-aws.huobi.pro
Description: AWS optimized trading
TOOLS.md Structure
## HTX Accounts

### main
- API Key: fe45419a...xyz
- Secret: secretabc...key
- Environment: https://api.huobi.pro
- Description: Primary trading account

### trading
- API Key: test456...abc
- Secret: testsecret...xyz
- Environment: https://api-aws.huobi.pro
- Description: AWS optimized trading

Agent Behavior
Credentials requested: Mask secrets (show last 5 chars only)
Listing accounts: Show names and environment, never keys
Account selection: Ask if ambiguous, default to main
When doing a transaction in mainnet, confirm with user before by asking to write "CONFIRM" to proceed
New credentials: Prompt for name, environment
Adding New Accounts

When user provides new credentials:

Ask for account name
Ask: Which environment (Mainnet or Mainnet-AWS)
Store in TOOLS.md with masked display confirmation
Signing Requests

All authenticated endpoints require HMAC SHA256 signature:

Create the pre-sign string in the following order:
HTTP method (GET/POST) + "\n"
API host (e.g., api.huobi.pro) + "\n"
API path (e.g., /v1/order/orders) + "\n"
Sorted query string parameters
Append required parameters to all authenticated requests:
AccessKeyId: Your API key
SignatureMethod: HmacSHA256
SignatureVersion: 2
Timestamp: UTC timestamp in format yyyy-MM-ddTHH:mm:ss
Sign the pre-sign string with secretKey using HMAC SHA256
Append signature to query string as Signature parameter
For POST requests, also include signature in the URL query string

Example pre-sign string:

POST\n
api.huobi.pro\n
/v1/order/orders/place\n
AccessKeyId=xxx&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2017-05-11T15:19:30

User Agent Header

Include User-Agent header with the following string: htx-spot/1.0.0 (Skill)

Important Notes
All timestamps are in Unix milliseconds
Symbol names should be lowercase (e.g., btcusdt, not BTCUSDT)
For market buy orders, the amount parameter represents the quote currency amount
For all other order types, amount represents the base currency amount
Account ID must be obtained from /v1/account/accounts endpoint before trading
Rate limits apply - see HTX API documentation for details
Signature must be calculated for every authenticated request
Timestamp in signature must be within 1 minute of server time
For order queries, the order created via API will no longer be queryable after being cancelled for more than 2 hours
The maximum query window for historical data is typically 48 hours, with data available for the last 180 days
When placing batch orders, maximum 10 orders per batch
Fee rates query supports maximum 10 trading pairs at a time
All request endpoints must match the endpoints specified in the documentation.
API Documentation

For more details, refer to the official HTX API documentation: https://www.htx.com/en-us/opend/newApiPages/

Weekly Installs
105
Repository
htx-exchange/ht…ills-hub
GitHub Stars
14
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail