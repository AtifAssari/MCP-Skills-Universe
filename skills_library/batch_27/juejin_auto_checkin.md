---
title: juejin-auto-checkin
url: https://skills.sh/wcly/skills/juejin-auto-checkin
---

# juejin-auto-checkin

skills/wcly/skills/juejin-auto-checkin
juejin-auto-checkin
Installation
$ npx skills add https://github.com/wcly/skills --skill juejin-auto-checkin
SKILL.md
稀土掘金自动签到技能
🎯 功能介绍

此技能可以自动化完成稀土掘金的以下任务：

✅ 每日自动签到 - 获得签到奖励矿石
✅ 免费单抽 - 每天一次免费抽奖机会
⏰ 定时任务 - 支持设置每天定时执行
📋 使用方法

直接告诉我：

"稀土掘金自动签到"
"掘金免费单抽"
"juejin 签到"
"执行掘金签到"
⏰ 定时任务管理
设置定时任务

告诉我想设置几点执行，如 "每天 9:59 执行掘金签到"

查看定时任务

告诉 "查看掘金签到定时任务"

删除定时任务

告诉 "删除掘金签到定时任务"

手动执行

告诉 "执行掘金签到"

查看日志

告诉 "查看掘金签到日志"

📁 文件位置
脚本：~/.trae-cn/skills/juejin-auto-checkin/scripts/juejin_auto.py
日志：~/.juejin_auto.log
定时任务：~/Library/LaunchAgents/com.juejin.autosignin.plist
⚠️ 注意事项
首次使用会自动打开浏览器等待扫码登录（最多等待5分钟）
如果未登录，脚本会自动等待用户完成登录后再执行签到
登录状态会自动保存，下次无需重新登录
免费单抽每天只能使用一次
定时任务需要电脑在执行时间开机
Weekly Installs
31
Repository
wcly/skills
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykWarn