---
rating: ⭐⭐⭐
title: tigeropen
url: https://skills.sh/tigerfintech/tigeropen-skill/tigeropen
---

# tigeropen

skills/tigerfintech/tigeropen-skill/tigeropen
tigeropen
Installation
$ npx skills add https://github.com/tigerfintech/tigeropen-skill --skill tigeropen
SKILL.md
Tiger Open API Python SDK

老虎量化开放平台 Python SDK 完整技能集 / Complete AI skill set for Tiger Brokers OpenAPI

安全警告 / Safety Warning: 交易涉及真实资金。生成交易代码时默认使用模拟账户（Paper Trading），除非用户明确要求实盘。实盘下单前必须与用户确认订单详情。 Trading involves real money. Default to Paper Trading account when generating trading code unless the user explicitly requests live trading. Always confirm order details with the user before live orders.

Docs: https://docs.itigerup.com/docs/prepare
GitHub: https://github.com/tigerfintech/openapi-python-sdk
SDK: pip install tigeropen | Python 3.8 - 3.14
Language Rules / 语言规则

根据用户输入语言自动回复。用户使用英文提问则用英文回复，使用中文提问则用中文回复。技术术语（代码、API 名称、参数名）保持原文不翻译。 Reply in the user's language. Keep technical terms (code, API names, parameters) as-is.

Reference Guides

This skill is organized into focused reference files. Load the relevant guide based on your task:

Quickstart — SDK install, authentication, client setup, enums/objects, error codes, FAQ
Market Data — Real-time quotes, K-lines, depth, ticks, capital flow, fundamentals, scanner
Trading — Place orders (market/limit/stop/algo), order management, assets, positions, fund transfers
Options — Option chains, Greeks, single-leg/multi-leg combos, option calculator
Real-time Push — Subscribe to quote/depth/tick/K-line/order/position/asset changes via PushClient
CLI Tool — Command-line interface: config, quote, trade, account, push commands with table/json/csv output
MCP Server — Expose Tiger API as MCP tools for Cursor, Claude Code, Kiro, Trae
Quick Start
from tigeropen.common.consts import Language, Market
from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.common.util.signature_utils import read_private_key
from tigeropen.quote.quote_client import QuoteClient
from tigeropen.trade.trade_client import TradeClient

# 1. Configure / 配置
# 方式一：配置文件(推荐) / Method 1: Config file (recommended)
config = TigerOpenClientConfig(props_path='/path/to/your/config/')

# 方式二：代码赋值 / Method 2: Code assignment
# config = TigerOpenClientConfig()
# config.tiger_id = 'your_tiger_id'
# config.private_key = read_private_key('/path/to/your_private_key.pem')
# config.account = 'your_account'
# config.language = Language.en_US

# 2. Query quotes / 查询行情
quote_client = QuoteClient(config)
quote = quote_client.get_market_status(Market.US)

# 3. Place order / 下单
trade_client = TradeClient(config)
# See references/trade.md for order examples

When to Use Each Reference
Task	Reference
First time setup, SDK install, auth config	quickstart.md
Get stock/option/future quotes, K-lines, screener	quote.md
Place/modify/cancel orders, check positions/assets	trade.md
Option chains, Greeks, combo strategies	option.md
Real-time streaming data via WebSocket	push.md
CLI commands: query data, manage orders from terminal	cli.md
Set up MCP Server for AI editor integration	mcp.md
Common Symbols / 常见标的速查

当用户使用中文名称或英文简称时，按下表映射。不在表中的标的根据上下文判断。 Map user's natural language to symbols. For unlisted symbols, infer from context.

港股 HK
常见称呼	代码 Symbol
腾讯	00700
阿里巴巴、阿里	09988
美团	03690
小米	01810
京东	09618
比亚迪	01211
快手	01024
百度	09888
网易	09999
中芯国际	00981
MINIMAX	00100
智谱	02513
美股 US
常见称呼	代码 Symbol
苹果 / Apple	AAPL
特斯拉 / Tesla	TSLA
英伟达 / NVIDIA	NVDA
微软 / Microsoft	MSFT
谷歌 / Google	GOOGL
亚马逊 / Amazon	AMZN
Meta	META
台积电 / TSM	TSM
AMD	AMD
老虎证券 / Tiger / TIGR	TIGR
阿里巴巴（美股）/ BABA	BABA
京东（美股）/ JD	JD
拼多多 / PDD	PDD
标普500 ETF / SPY	SPY
纳指 ETF / QQQ	QQQ
Weekly Installs
105
Repository
tigerfintech/ti…en-skill
GitHub Stars
4
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn