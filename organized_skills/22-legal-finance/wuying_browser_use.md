---
rating: ⭐⭐
title: wuying-browser-use
url: https://skills.sh/agentbay-ai/agentbay-skills/wuying-browser-use
---

# wuying-browser-use

skills/agentbay-ai/agentbay-skills/wuying-browser-use
wuying-browser-use
Installation
$ npx skills add https://github.com/agentbay-ai/agentbay-skills --skill wuying-browser-use
SKILL.md
Wuying Browser Use

自动化浏览器操作，支持网页导航、表单填写、数据提取等任务。

依赖
python3 -m pip install wuying-agentbay-sdk

使用方法
python3 scripts/browser-use.py "<任务执行步骤>"

功能特性
✅ 网页导航和点击
✅ 表单填写和提交
✅ 数据提取和抓取
✅ 网页截图
✅ 搜索和浏览
✅ 支持中英文指令
常用场景
电商信息收集
python3 scripts/browser-use.py "访问京东搜索iPhone，提取前5个商品价格"

新闻监控
python3 scripts/browser-use.py "打开新浪新闻，获取今日头条"

社交媒体
python3 scripts/browser-use.py "访问微博热搜榜，提取前10个话题"

使用技巧
指令要具体明确 - 说清楚要访问哪个网站，做什么操作
一次一个任务 - 复杂流程拆分成多个命令
描述性语言 - 详细描述要提取的内容或点击的元素
注意事项
每次命令独立运行，不保持会话状态
某些网站可能限制自动化访问
指令不明确可能导致非预期结果
每次执行需要1~2分钟，会不断产生中间结果，不要提前杀死进程，也不要重试
skill调用后，控制台会打印出asp流化链接（可视化的url），可告知用户查看
Weekly Installs
67
Repository
agentbay-ai/age…y-skills
GitHub Stars
35
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn