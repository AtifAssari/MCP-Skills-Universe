---
title: agent-reach
url: https://skills.sh/panniantong/agent-reach/agent-reach
---

# agent-reach

skills/panniantong/agent-reach/agent-reach
agent-reach
Installation
$ npx skills add https://github.com/panniantong/agent-reach --skill agent-reach
Summary

Multi-platform web search and content reading across 16+ social and web sources.

Supports 16 platforms including Twitter/X, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu, Douyin, Weibo, WeChat articles, LinkedIn, Instagram, V2EX, RSS, and general web search via Exa
Zero configuration required for 8 channels; others need cookies or API keys (Groq for podcast transcription, Exa for web search)
Provides command-line tools and Python APIs for searching, reading threads, extracting transcripts, and fetching user profiles across platforms
Built-in proxy and authentication support; run agent-reach doctor to check channel availability and troubleshoot setup issues
SKILL.md
Agent Reach — 路由器

17 平台工具集合。根据用户意图选择对应分类。

路由表
用户意图	分类	详细文档
网页搜索/代码搜索	search	references/search.md
小红书/抖音/微博/推特/B站/V2EX/Reddit	social	references/social.md
招聘/职位/LinkedIn	career	references/career.md
GitHub/代码	dev	references/dev.md
网页/文章/公众号/RSS	web	references/web.md
YouTube/B站/播客字幕	video	references/video.md
零配置快速命令
# Exa 网页搜索
mcporter call 'exa.web_search_exa(query: "query", numResults: 5)'

# 通用网页阅读
curl -s "https://r.jina.ai/URL"

# GitHub 搜索
gh search repos "query" --sort stars --limit 10

# Twitter 搜索
twitter search "query" --limit 10

# YouTube/B站字幕
yt-dlp --write-sub --skip-download -o "/tmp/%(id)s" "URL"

# Reddit 搜索
rdt search "query" --limit 10

# Reddit 读帖 + 评论
rdt read POST_ID

# V2EX 热门
curl -s "https://www.v2ex.com/api/topics/hot.json" -H "User-Agent: agent-reach/1.0"

环境检查
# 检查可用 channel
agent-reach doctor

# 查看所有 MCP 服务
mcporter_list_servers()

工作区规则

不要在 agent workspace 创建文件。 使用 /tmp/ 存放临时输出，~/.agent-reach/ 存放持久数据。

详细文档

根据用户需求，阅读对应的详细文档：

搜索工具 — Exa AI 搜索
社交媒体 — 小红书, 抖音, Twitter, B站, V2EX, Reddit
职场招聘 — LinkedIn
开发工具 — GitHub CLI
网页阅读 — Jina Reader, 微信公众号, RSS
视频播客 — YouTube, B站, 小宇宙
配置渠道

如果某个 channel 需要配置，获取安装指南： https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md

用户只需提供 cookies，其他配置由 agent 完成。

Weekly Installs
4.0K
Repository
panniantong/agent-reach
GitHub Stars
18.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail