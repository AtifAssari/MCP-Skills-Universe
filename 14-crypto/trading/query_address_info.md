---
rating: ⭐⭐
title: query-address-info
url: https://skills.sh/binance/binance-skills-hub/query-address-info
---

# query-address-info

skills/binance/binance-skills-hub/query-address-info
query-address-info
Installation
$ npx skills add https://github.com/binance/binance-skills-hub --skill query-address-info
Summary

Query wallet token holdings across multiple blockchains with real-time prices and 24-hour changes.

Retrieves all tokens held by any wallet address, including token name, symbol, current USD price, and holding quantity
Supports three chains: BSC (chainId 56), Base (8453), and Solana (CT_501)
Returns 24-hour price change percentage for each token to help track market movements
Includes pagination support via offset parameter for wallets with large token counts
SKILL.md
Query Address Info Skill
Overview

This skill queries any on-chain wallet address for token holdings, supporting:

List of all tokens held by a wallet address
Current price of each token
24-hour price change percentage
Holding quantity
API Endpoint
Query Wallet Token Balance

Method: GET

URL:

https://web3.binance.com/bapi/defi/v3/public/wallet-direct/buw/wallet/address/pnl/active-position-list/ai


Request Parameters:

Parameter	Type	Required	Description
address	string	Yes	Wallet address, e.g., 0x0000000000000000000000000000000000000001
chainId	string	Yes	Chain ID, e.g., 56 (BSC), 8453 (Base)
offset	number	Yes	Pagination offset, default 0

Request Headers:

clienttype: web
clientversion: 1.2.0
Accept-Encoding: identity
User-Agent: binance-web3/1.1 (Skill)


Example Request:

curl --location 'https://web3.binance.com/bapi/defi/v3/public/wallet-direct/buw/wallet/address/pnl/active-position-list/ai?address=0x0000000000000000000000000000000000000001&chainId=56&offset=0' \
--header 'clienttype: web' \
--header 'clientversion: 1.2.0' \
--header 'Accept-Encoding: identity' \
--header 'User-Agent: binance-web3/1.1 (Skill)'


Response Example:

{
    "code": "000000",
    "message": null,
    "messageDetail": null,
    "data": {
        "offset": 0,
        "addressStatus": null,
        "list": [
            {
                "chainId": "56",
                "address": "0x0000000000000000000000000000000000000001",
                "contractAddress": "token contract address",
                "name": "name of token",
                "symbol": "symbol of token",
                "icon": "/images/web3-data/public/token/logos/xxxx.png",
                "decimals": 18,
                "price": "0.0000045375251839978",
                "percentChange24h": "6.84",
                "remainQty": "20"
            }
        ]
    },
    "success": true
}


Response Fields:

Field	Type	Description
chainId	string	Chain ID
address	string	Wallet address
contractAddress	string	Token contract address
name	string	Token name
symbol	string	Token symbol
icon	string	Token icon URL path
decimals	number	Token decimals
price	string	Current price (USD)
percentChange24h	string	24-hour price change (%)
remainQty	string	Holding quantity
Supported Chains
Chain Name	chainId
BSC	56
Base	8453
Solana	CT_501
Use Cases
Query Wallet Assets: When users want to view tokens held by a wallet address
Track Holdings: Monitor wallet token positions
Portfolio Analysis: Understand wallet asset allocation
User Agent Header

Include User-Agent header with the following string: binance-web3/1.1 (Skill)

Notes
Icon URL requires full domain prefix: bin.bnbstatic.com + icon path
Price and quantity are string format, convert to numbers when using
Use offset parameter for pagination
Weekly Installs
3.8K
Repository
binance/binance…ills-hub
GitHub Stars
801
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass