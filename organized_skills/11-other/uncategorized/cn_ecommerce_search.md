---
rating: ⭐⭐
title: cn-ecommerce-search
url: https://skills.sh/shopmeskills/mcp/cn-ecommerce-search
---

# cn-ecommerce-search

skills/shopmeskills/mcp/cn-ecommerce-search
cn-ecommerce-search
Installation
$ npx skills add https://github.com/shopmeskills/mcp --skill cn-ecommerce-search
SKILL.md
Chinese E-commerce Product Search

Search and retrieve product information across Chinese e-commerce platforms via the Shopme unified product database.

Zero-config — no API keys required.

When to Use
User asks to find a product on Taobao, Tmall, or 小红书
User shares a product link and wants details
User needs to search Chinese suppliers for a product
User asks about prices on Chinese platforms
User provides a product URL from Taobao, Tmall, or XHS
User wants to compare products across platforms
MCP Server Setup
{
  "mcpServers": {
    "cn-ecommerce-search": {
      "command": "npx",
      "args": ["-y", "@shopmeagent/cn-ecommerce-search-mcp"]
    }
  }
}


No environment variables required. Optional:

Variable	Default	Description
SHOPME_API_BASE	https://api.shopmeagent.com	Override API endpoint (e.g. http://localhost:8000 for local dev)
Available Tools
search_products

Search products by keyword across platforms.

Parameter	Type	Required	Default	Description
keyword	string	Yes	—	Search term (Chinese or English)
platform	string	No	all	Filter by platform: xhs, taobao, tmall
sort_by	string	No	relevance	relevance, price_asc, price_desc, sales_desc, created_at
page	number	No	1	Page number
limit	number	No	10	Items per page (max 50)
get_product_detail

Get detailed info about a specific product by ID or URL.

Parameter	Type	Required	Description
product_id	string	One of two	Product ID (recommended, faster)
url	string	One of two	Product URL
platform	string	No	Platform hint to speed up lookup
parse_product_link

Parse a product URL to identify the platform and product ID. Runs locally, no API call.

Parameter	Type	Required	Description
url	string	Yes	Product URL or text containing one
Supported Platforms
Platform	Code	Strengths	Price Range	Typical Buyer
淘宝 Taobao	taobao	Largest selection, consumer goods	¥ Low-Mid	End consumers
天猫 Tmall	tmall	Brand flagship stores, higher quality	¥ Mid-High	Quality-focused
小红书 XHS	xhs	Community picks, beauty/lifestyle	¥ Mid	Young women, lifestyle
Supported URL Formats
item.taobao.com/item.htm?id=123456
detail.tmall.com/item.htm?id=123456
mall.xiaohongshu.com/goods-detail/xxx
Short links: e.tb.cn/xxx, m.tb.cn/xxx
Price Understanding Guide
All prices are in CNY (¥). Rough conversion: 1 USD ≈ 7.2 CNY
Always consider shipping costs when comparing prices
Search Tips
Chinese keywords get more results
English keywords are auto-expanded with synonyms and word variants
Sort by sales_desc to find popular/trusted products (best on XHS)
Use platform filter to narrow results to a specific platform
Use get_product_detail with a URL directly — no need to parse first
Weekly Installs
594
Repository
shopmeskills/mcp
GitHub Stars
1
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn