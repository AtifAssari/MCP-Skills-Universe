---
title: github-trending
url: https://skills.sh/wwwzhouhui/skills_collection/github-trending
---

# github-trending

skills/wwwzhouhui/skills_collection/github-trending
github-trending
Installation
$ npx skills add https://github.com/wwwzhouhui/skills_collection --skill github-trending
SKILL.md
GitHub Trending 摘要推送
功能
抓取 https://github.com/trending 今日热门前 5 项目
拉取每个项目 README
生成包含项目是什么、解决问题、技术栈、Star 数量的中文摘要
通过企业微信机器人发送摘要
脚本
1. 抓取与保存
python fetch_trending.py --output trending_top5.json

2. 生成摘要并发送
python send_wecom_summary.py --input trending_top5.json

配置
可选环境变量 GITHUB_TOKEN 用于提高 GitHub API 额度
可选环境变量 WEIXIN_WEBHOOK 覆盖默认企业微信机器人地址
Weekly Installs
83
Repository
wwwzhouhui/skil…llection
GitHub Stars
233
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn