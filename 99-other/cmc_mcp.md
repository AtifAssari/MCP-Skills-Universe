---
title: cmc-mcp
url: https://skills.sh/coinmarketcap-official/skills-for-ai-agents-by-coinmarketcap/cmc-mcp
---

# cmc-mcp

skills/coinmarketcap-official/skills-for-ai-agents-by-coinmarketcap/cmc-mcp
cmc-mcp
Installation
$ npx skills add https://github.com/coinmarketcap-official/skills-for-ai-agents-by-coinmarketcap --skill cmc-mcp
SKILL.md
CoinMarketCap MCP Skill

You have access to CoinMarketCap data through MCP tools. Use these tools to provide comprehensive, data-rich answers to crypto-related questions.

Prerequisites

Before using CMC tools, verify the MCP connection is working. If tools fail or return connection errors, ask the user to set up the MCP connection:

{
  "mcpServers": {
    "cmc-mcp": {
      "url": "https://mcp.coinmarketcap.com/mcp",
      "headers": {
        "X-CMC-MCP-API-KEY": "your-api-key"
      }
    }
  }
}


Get your API key from https://pro.coinmarketcap.com/login

Core Principle

Err on the side of fetching more data. A complete answer from multiple tools is better than a partial answer that leaves users asking for more. When in doubt, call additional tools to gather comprehensive data.

Workflow
1. Always Search First

When a user mentions a cryptocurrency by name or symbol, search for it first to get the ID:

User: "How is Solana doing?"
→ Call search_cryptos with query "solana"
→ Get ID (e.g., 5426)
→ Then call other tools using that ID


Most tools require the numeric CMC ID, not the name or symbol. The search tool returns: id, name, symbol, slug, and rank.

2. Batch Requests When Useful

When dealing with multiple coins, batch the requests:

User: "Compare BTC, ETH, and SOL"
→ Search for each to get IDs: 1, 1027, 5426
→ Call get_crypto_quotes_latest with id="1,1027,5426"


This is more efficient than separate calls and allows for direct comparison in the response.

3. Match Tools to Query Type

For price and market data:

get_crypto_quotes_latest returns price, market cap, volume, percent changes (1h, 24h, 7d, 30d, 90d, 1y), circulating supply, and dominance

For coin background and links:

get_crypto_info returns description, website, social links, explorer URLs, tags, and launch date

For technical analysis:

get_crypto_technical_analysis returns moving averages (SMA, EMA), MACD, RSI, Fibonacci levels, and pivot points

For recent news:

get_crypto_latest_news returns headlines, descriptions, content, URLs, and publish dates

For holder and distribution data:

get_crypto_metrics returns address counts by holding value, whale vs others distribution, and holder time breakdowns (traders, cruisers, holders)

For concept explanations:

search_crypto_info performs semantic search on crypto concepts, whitepapers, and FAQs

For overall market health:

get_global_metrics_latest returns total market cap, fear/greed index, altcoin season index, BTC/ETH dominance, volume, and ETF flows

For derivatives and leverage data:

get_global_crypto_derivatives_metrics returns open interest, funding rates, liquidations, and futures vs perpetuals breakdown

For total market cap technical analysis:

get_crypto_marketcap_technical_analysis returns TA indicators for the entire crypto market cap

For trending themes:

trending_crypto_narratives returns hot narratives with market cap, volume, performance, and top coins in each narrative

For upcoming catalysts:

get_upcoming_macro_events returns scheduled events like Fed meetings, regulatory deadlines, and major announcements
Error Handling

If search returns no results:

Report that the coin was not found
Ask the user to clarify or check the spelling
Suggest alternatives if the query might be ambiguous

If a tool fails or times out:

Retry once for transient errors
If still failing, note which data is unavailable and proceed with other tools
For price queries, get_crypto_quotes_latest is critical. If it fails after retry, inform the user data is temporarily unavailable.
For background queries, get_crypto_info failure means note "Project info unavailable" and provide what you can from other tools

If rate limited (429 error):

Inform the user the API is rate limited
Suggest waiting a moment before retrying
Consider if fewer tool calls could answer the question
Adapting to User Sophistication

Read context cues from the user's query:

Casual questions ("how's bitcoin doing?") warrant a clear summary with key numbers
Technical questions ("what's the RSI on BTC?") can include more detailed data
Broad questions ("what's happening in crypto?") benefit from market-wide tools like global metrics and trending narratives
Weekly Installs
66
Repository
coinmarketcap-o…arketcap
GitHub Stars
45
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn