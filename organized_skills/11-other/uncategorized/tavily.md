---
rating: ⭐⭐
title: tavily
url: https://skills.sh/aaaaqwq/claude-code-skills/tavily
---

# tavily

skills/aaaaqwq/claude-code-skills/tavily
tavily
Installation
$ npx skills add https://github.com/aaaaqwq/claude-code-skills --skill tavily
SKILL.md
Tavily AI 搜索
功能说明

此技能使用 Tavily API 提供 AI 优化的网络搜索能力：

智能搜索（AI 优化结果）
实时信息获取
搜索并提取内容
支持搜索深度和范围控制
使用方式
1. 基础搜索
./scripts/tavily.sh search <query> [max_results]

2. 深度搜索（包含更多内容）
./scripts/tavily.sh search <query> --deep

3. 搜索并提取
./scripts/tavily.sh extract <query> [max_results]

API Key

存储在: pass show api/tavily

示例
搜索 Polymarket 信息
./scripts/tavily.sh search "Polymarket Fed interest rate decision 2026"

搜索 AI 新闻
./scripts/tavily.sh search "latest AI news today" 5

深度搜索
./scripts/tavily.sh search "Bitcoin price analysis" --deep

注意事项
Tavily 有使用限制（取决于套餐）
搜索结果经过 AI 优化，更适合 LLM 使用
支持实时数据获取
Weekly Installs
24
Repository
aaaaqwq/claude-…e-skills
GitHub Stars
53
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn