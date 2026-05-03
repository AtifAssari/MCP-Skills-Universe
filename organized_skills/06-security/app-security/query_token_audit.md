---
rating: ⭐⭐
title: query-token-audit
url: https://skills.sh/binance/binance-skills-hub/query-token-audit
---

# query-token-audit

skills/binance/binance-skills-hub/query-token-audit
query-token-audit
Installation
$ npx skills add https://github.com/binance/binance-skills-hub --skill query-token-audit
Summary

Pre-trade token security scanning across Ethereum, BSC, Base, and Solana to detect honeypots, rug pulls, and malicious contracts.

Analyzes contract risks, trading risks, and scam indicators with three-tier risk classification (LOW, MEDIUM, HIGH)
Returns buy/sell tax percentages, contract verification status, and detailed risk item breakdowns with descriptions
Supports four blockchains: Ethereum, BSC, Base, and Solana via single unified API endpoint
Results valid only when both hasResult and isSupported flags are true; LOW risk does not guarantee safety and represents point-in-time snapshots
SKILL.md
Query Token Audit Skill
Overview
API	Function	Use Case
Token Security Audit	Token security scan	Detect honeypot, rug pull, scam, malicious functions
Use Cases
Pre-Trade Safety Check: Verify token security before buying or swapping
Scam Detection: Identify honeypots, fake tokens, and malicious contracts
Contract Analysis: Check for dangerous ownership functions and hidden risks
Tax Verification: Detect unusual buy/sell taxes before trading
Supported Chains
Chain Name	chainId
BSC	56
Base	8453
Solana	CT_501
Ethereum	1
API: Token Security Audit
Method: POST

URL:

https://web3.binance.com/bapi/defi/v1/public/wallet-direct/security/token/audit


Request Parameters:

Parameter	Type	Required	Description
binanceChainId	string	Yes	Chain ID: CT_501 (Solana), 56 (BSC), 8453 (Base), 1 (Ethereum)
contractAddress	string	Yes	Token contract address
requestId	string	Yes	Unique request ID (UUID v4 format)

Request Headers:

Content-Type: application/json
Accept-Encoding: identity
User-Agent: binance-web3/1.4 (Skill)


Example Request:

curl --location 'https://web3.binance.com/bapi/defi/v1/public/wallet-direct/security/token/audit' \
--header 'Content-Type: application/json' \
--header 'source: agent' \
--header 'Accept-Encoding: identity' \
--header 'User-Agent: binance-web3/1.4 (Skill)' \
--data '{
    "binanceChainId": "56",
    "contractAddress": "0x55d398326f99059ff775485246999027b3197955",
    "requestId": "'$(uuidgen)'"
}'


Response Example:

{
    "code": "000000",
    "data": {
        "requestId": "d6727c70-de6c-4fad-b1d7-c05422d5f26b",
        "hasResult": true,
        "isSupported": true,
        "riskLevelEnum": "LOW",
        "riskLevel": 1,
        "extraInfo": {
            "buyTax": "0",
            "sellTax": "0",
            "isVerified": true
        },
        "riskItems": [
            {
                "id": "CONTRACT_RISK",
                "name": "Contract Risk",
                "details": [
                    {
                        "title": "Honeypot Risk Not Found",
                        "description": "A honeypot is a token that can be bought but not sold",
                        "isHit": false,
                        "riskType": "RISK"
                    }
                ]
            }
        ]
    },
    "success": true
}


Response Fields:

Field	Type	Description
hasResult	boolean	Whether audit data is available
isSupported	boolean	Whether the token is supported for audit
riskLevelEnum	string	Risk level: LOW, MEDIUM, HIGH
riskLevel	number	Risk level number (1-5)
extraInfo.buyTax	string	Buy tax percentage (null if unknown)
extraInfo.sellTax	string	Sell tax percentage (null if unknown)
extraInfo.isVerified	boolean	Whether contract code is verified
riskItems[].id	string	Risk category: CONTRACT_RISK, TRADE_RISK, SCAM_RISK
riskItems[].details[].title	string	Risk check title
riskItems[].details[].description	string	Risk check description
riskItems[].details[].isHit	boolean	true = risk detected
riskItems[].details[].riskType	string	RISK (critical) or CAUTION (warning)

Risk Level Reference:

riskLevel	riskLevelEnum	Action	Description
0-1	LOW	Proceed with caution	Lower risk detected, but NOT guaranteed safe. DYOR.
2-3	MEDIUM	Exercise caution	Moderate risks detected, review risk items carefully
4	HIGH	Avoid trading	Critical risks detected, high probability of loss
5	HIGH	Block transaction	Severe risks confirmed, do NOT proceed

IMPORTANT: LOW risk does NOT mean "safe." Audit results are point-in-time snapshots. Project teams can modify contracts or restrict liquidity after purchase. These risks cannot be predicted in advance.

Response Handling:

If hasResult=false OR isSupported=false: → Reply: "Security audit data is not available for this token on this chain." → Do NOT show riskLevel, riskLevelEnum, or riskItems (data is unreliable when either field is false) → You may suggest the user verify the contract address and chain, or try again later
If hasResult=true AND isSupported=true: → Show the full audit result including risk level, tax info, and all risk items → Apply the Risk Level Reference table above for actionable guidance
User Agent Header

Include User-Agent header with the following string: binance-web3/1.4 (Skill)

Notes
All numeric fields are string format, convert when using
Audit results are ONLY valid when hasResult: true AND isSupported: true
riskLevel: 5 means transaction should be blocked; riskLevel: 4 is high risk
Tax thresholds: >10% is critical, 5-10% is warning, <5% is acceptable
Generate unique UUID v4 for each audit request
Only output security check risk flags, do NOT provide any investment advice
Always end with disclaimer: ⚠️ This audit result is for reference only and does not constitute investment advice. Always conduct your own research.
Weekly Installs
3.7K
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