---
title: multi-search
url: https://skills.sh/nex-zmh/agent-websearch-skill/multi-search
---

# multi-search

skills/nex-zmh/agent-websearch-skill/multi-search
multi-search
Installation
$ npx skills add https://github.com/nex-zmh/agent-websearch-skill --skill multi-search
Summary

Intelligent multi-engine search with automatic network detection and fallback prioritization.

Supports four search engines with two priority modes: quality-first (Tavily > DuckDuckGo > Bing API > Bing scraper) or balanced/free-first (DuckDuckGo > Tavily > Bing API > Bing scraper)
Includes automatic quota management for API-based engines, 5-minute network detection caching, and forced re-detection after network changes
Provides web content fetching and batch enrichment of search results with full page content extraction
Integrates with the summarize skill for complete workflows: search > fetch > summarize > present
SKILL.md
Multi-Search Skill - 智能多引擎搜索

本技能整合多个搜索引擎，自动检测网络环境，智能选择最佳可用引擎。

引擎优先级
质量优先模式 (prefer_quality=True)
Tavily API (1000次/月) - 质量最高，需 API Key
DuckDuckGo (无限免费) - 无需 API Key
Bing Web Search API (1000次/月) - 需 API Key
Bing 爬虫 (无限免费) - 最终回退
平衡模式 (prefer_quality=False, 默认)
DuckDuckGo (无限免费) - 优先免费引擎
Tavily API (1000次/月) - 如果配置了 API Key
Bing Web Search API (1000次/月)
Bing 爬虫 (无限免费)
核心能力
智能网络检测与引擎切换
自动配额管理（Tavily/Bing API）
支持网页内容抓取
5分钟网络检测缓存
使用方式
基本搜索
from multi_search import search

# 平衡模式 - 优先免费引擎
results = search("Python tutorial", max_results=5)

# 质量优先模式 - 优先使用 Tavily
results = search("AI research", max_results=5, prefer_quality=True)

# 强制重新检测网络（切换 VPN 后使用）
results = search("OpenClaw skills", max_results=5, force_network_check=True)

搜索技能（自动质量优先）
from multi_search import search_skills

results = search_skills("OpenClaw AI agent automation", max_results=10)

查看系统状态
from multi_search import get_status

status = get_status()  # 使用缓存
status = get_status(force_network_check=True)  # 强制重新检测

抓取网页详细内容
from multi_search import search, fetch_web_content, fetch_search_results_content

# 搜索并抓取第一个结果的详细内容
results = search("OpenClaw new features", max_results=3)
if results:
    content = fetch_web_content(results[0]['href'], max_length=3000)
    # content['title'], content['content'], content['success']

# 批量抓取所有搜索结果的详细内容
enriched_results = fetch_search_results_content(results, max_length=2000)
for r in enriched_results:
    if r.get('full_content'):
        # 使用 summarize 技能总结内容
        pass

与 Summarize 技能结合使用
OpenClaw 工作流：
1. 使用 multi-search 搜索关键词
2. 选择感兴趣的搜索结果
3. 使用 fetch_web_content() 抓取网页内容
4. 使用 summarize 技能总结网页内容
5. 将摘要呈现给用户

返回结果格式
[
    {
        'title': '结果标题',
        'href': 'https://example.com',
        'body': '结果摘要...',
        'source': 'duckduckgo'  # 或 'tavily', 'bing_api', 'bing_scraper'
    }
]

参数说明
query: 搜索关键词
max_results: 最大结果数（默认5）
prefer_quality: 是否优先质量（默认False）
force_network_check: 是否强制重新检测网络（默认False）
注意事项
DuckDuckGo: 免费无限，但某些网络环境无法访问
Tavily: 质量高，需要 API key，1000次/月
Bing API: 官方稳定，需要 Azure 账号，1000次/月
Bing 爬虫: 免费无限，但可能受反爬影响
Weekly Installs
574
Repository
nex-zmh/agent-w…ch-skill
GitHub Stars
4
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn