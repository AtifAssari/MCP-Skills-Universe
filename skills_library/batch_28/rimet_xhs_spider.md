---
title: rimet-xhs-spider
url: https://skills.sh/site/skills.volces.com/rimet-xhs-spider
---

# rimet-xhs-spider

skills/skills.volces.com/xhs-spider
xhs-spider
$ npx skills add https://skills.volces.com/skills/clawhub/rimetli
SKILL.md
小红书采集技能 (XHS-Spider)

本技能提供一系列与小红书数据采集相关的本地脚本执行能力。当用户需要抓取小红书相关数据时，可参考以下指令格式调用本地 Python 脚本。

执行指令规范

请使用内置的 exec 工具执行以下命令。执行前请确保已激活对应的 Python 虚拟环境，并已设置 XHS_COOKIE 环境变量。

获取博主基本信息：python cli.py --action profile --url "<用户主页链接>"
抓取博主主页笔记：python cli.py --action user --url "<用户主页链接>"
提取单篇笔记评论：python cli.py --action comment --url "<笔记链接>"
关键词搜索抓取：python cli.py --action search --keyword "<关键词>" --num 10

抓取完成后，请读取终端输出的 Excel 或媒体文件路径，并反馈给用户。

Weekly Installs
12
Source
skills.volces.c…/rimetli
First Seen
10 days ago