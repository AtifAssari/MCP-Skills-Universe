---
rating: ⭐⭐
title: wechat-message-sender
url: https://skills.sh/cloudsen/eliteforge-skills/wechat-message-sender
---

# wechat-message-sender

skills/cloudsen/eliteforge-skills/wechat-message-sender
wechat-message-sender
Installation
$ npx skills add https://github.com/cloudsen/eliteforge-skills --skill wechat-message-sender
SKILL.md
WeChat Message Sender
目标

调用 scripts/send_wechat_message.swift，在 macOS 微信桌面版里给指定联系人发送一段纯文本。

必填参数
contact：联系人显示名，必须与微信会话标题精确一致。
message：要发送的纯文本内容。
前置条件
已安装微信桌面版。
当前终端或 Codex 已授予 macOS 辅助功能权限。
只支持文本消息，不支持图片、文件、卡片。
工作流
校验 contact 和 message 非空。
运行脚本：
swift scripts/send_wechat_message.swift --contact "<contact>" --message "<message>"
脚本会自动：
打开或激活微信。
聚焦左侧搜索框并搜索联系人。
在结果列表里查找精确匹配项。
打开会话后再次校验标题完全等于 contact。
校验通过后发送消息。
调试
只验证定位，不真正发送：
swift scripts/send_wechat_message.swift --contact "<contact>" --message "<message>" --dry-run
安全规则
只接受精确标题匹配，不做模糊猜测。
找不到联系人、权限不足、窗口结构异常时，直接报错并停止。
如果脚本报结构错误，先确认微信已升级到最新版本，并重新授权辅助功能。
Weekly Installs
328
Repository
cloudsen/elitef…e-skills
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail