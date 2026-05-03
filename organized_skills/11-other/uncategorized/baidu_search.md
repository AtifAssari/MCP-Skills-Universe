---
rating: ⭐⭐⭐
title: baidu-search
url: https://skills.sh/countbot-ai/countbot/baidu-search
---

# baidu-search

skills/countbot-ai/countbot/baidu-search
baidu-search
Installation
$ npx skills add https://github.com/countbot-ai/countbot --skill baidu-search
Summary

Baidu AI search with four modes: web search, encyclopedia, video encyclopedia, and AI-generated answers.

Supports four search modes via the Baidu Qianfan platform: web search (default), Baidu Baike encyclopedia, Miaodong Baike video encyclopedia, and AI-generated responses
Command-line interface with filtering options: limit result count, filter by site, and filter by recency (week/month/semiyear/year)
Automatically includes current date context for time-sensitive queries
JSON output format available for agent integration; free tier includes 100 queries per day
SKILL.md
百度 AI 搜索

基于百度千帆平台的 AI 搜索服务，支持多种搜索模式。

配置

编辑 skills/baidu-search/scripts/config.json，填写 API Key：

{
  "api_key": "bce-v3/YOUR_API_KEY_HERE"
}


API Key 从 百度千帆平台 获取。

命令行调用
# 网页搜索（默认）
python3 skills/baidu-search/scripts/search.py "搜索关键词"

# JSON 输出（推荐 AI 使用）
python3 skills/baidu-search/scripts/search.py "人工智能最新进展" --json

# 限制结果数
python3 skills/baidu-search/scripts/search.py "Python教程" --limit 5

# 站点过滤
python3 skills/baidu-search/scripts/search.py "天气预报" --sites weather.com.cn

# 时间过滤（week/month/semiyear/year）
python3 skills/baidu-search/scripts/search.py "AI新闻" --recency week

# 百度百科
python3 skills/baidu-search/scripts/search.py "人工智能" --api-type baike

# 秒懂百科（视频）
python3 skills/baidu-search/scripts/search.py "深度学习" --api-type miaodong_baike

# AI 智能生成
python3 skills/baidu-search/scripts/search.py "什么是人工智能" --api-type ai_chat

API 类型
类型	说明
web_search	网页搜索（默认）
baike	百度百科
miaodong_baike	秒懂百科（视频）
ai_chat	AI 智能搜索生成
注意事项
免费额度：100 次/天
网页搜索查询最长 72 字符
自动包含当前日期上下文，方便处理时效性查询
Weekly Installs
1.4K
Repository
countbot-ai/countbot
GitHub Stars
546
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn