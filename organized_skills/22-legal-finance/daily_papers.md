---
rating: ⭐⭐
title: daily-papers
url: https://skills.sh/huangkiki/dailypaper-skills/daily-papers
---

# daily-papers

skills/huangkiki/dailypaper-skills/daily-papers
daily-papers
Installation
$ npx skills add https://github.com/huangkiki/dailypaper-skills --skill daily-papers
SKILL.md
每日论文推荐

这是面向用户的一句话入口。对用户来说，正常只需要说一次：

今日论文推荐
过去3天论文推荐
过去一周论文推荐
执行原则
先识别时间范围：
今日论文推荐、每日推荐、今日论文 -> 当天
过去3天论文推荐、最近3天论文 -> 3 天
过去一周论文推荐、看看这周有啥论文 -> 7 天
自动调用 /daily-papers-fetch。
第 1 步完成后，自动调用 /daily-papers-review。
第 2 步完成后，自动调用 /daily-papers-notes。
全部完成后，用一句话告诉用户：
推荐文件已生成
重点论文笔记已生成多少篇
目录页是否已自动刷新
重要约束
不要先要求用户手动跑 跑一下论文抓取 / 点评 / 笔记。
这 3 句是内部流水线和调试入口，不是首页主交互。
如果用户明确只想跑其中一步，再交给对应 skill。
自动化
本 skill 本身就是“一步跑完整流水线”的入口。
如果用户想做本地定时任务，默认也应该触发这一句，而不是写死三条内部命令。
Weekly Installs
30
Repository
huangkiki/daily…r-skills
GitHub Stars
633
First Seen
Mar 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn