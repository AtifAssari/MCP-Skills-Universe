---
rating: ⭐⭐⭐
title: wemp-operator
url: https://skills.sh/ianshaw027/wemp-operator/wemp-operator
---

# wemp-operator

skills/ianshaw027/wemp-operator/wemp-operator
wemp-operator
Installation
$ npx skills add https://github.com/ianshaw027/wemp-operator --skill wemp-operator
SKILL.md
wemp-operator

公众号自动化运营：内容采集、数据分析、互动管理。

环境检查
node scripts/setup.mjs        # 检查依赖
node scripts/setup.mjs --help # 配置指南

内容采集
node scripts/content/smart-collect.mjs \
  --query "需求" --keywords "关键词" --sources "数据源" [--deep]


数据源：hackernews, github, v2ex, 36kr, weibo, zhihu, producthunt, wallstreetcn 等

数据分析
node scripts/analytics/daily-report.mjs [--date YYYY-MM-DD]
node scripts/analytics/weekly-report.mjs

互动管理
node scripts/interact/check-comments.mjs [--list]
node scripts/interact/reply.mjs --comment-id <id> [--content "回复"]

Weekly Installs
8
Repository
ianshaw027/wemp-operator
GitHub Stars
81
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn