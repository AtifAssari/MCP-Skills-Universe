---
rating: ⭐⭐
title: xhs-batch
url: https://skills.sh/chenxiachan/xhs-claude-skills/xhs-batch
---

# xhs-batch

skills/chenxiachan/xhs-claude-skills/xhs-batch
xhs-batch
Installation
$ npx skills add https://github.com/chenxiachan/xhs-claude-skills --skill xhs-batch
SKILL.md

用户希望批量提取多个小红书帖子。请按以下步骤处理：

常量定义
Cookies 文件: ~/cookies.json
Obsidian 保存目录: ~/Documents/Obsidian Vault/xhs
Whisper 模型: mlx-community/whisper-large-v3-turbo
输入

用户提供的链接列表: $ARGUMENTS

流程
步骤 1：解析链接

从输入中提取所有小红书链接（支持多行、空格分隔、逗号分隔）。 每个链接提取帖子 ID 和 xsec_token。

步骤 2：检查 Cookies

检查 ~/cookies.json 是否存在。如不存在，按 /xhs 的步骤 0 引导用户导出。

步骤 3：逐个提取

对每个链接，执行 /xhs 的完整提取流程（步骤 2-4）：

请求页面 → 解析 INITIAL_STATE
视频帖子做语音转录
按 Peter Thiel 风格整理
保存为 {YYYY-MM-DD} {短标题}.md

每个帖子之间间隔 3 秒，避免触发反爬。

步骤 4：汇总报告

全部完成后，输出简短汇总：

成功/失败数量
每个帖子的文件名和一句话摘要
Weekly Installs
18
Repository
chenxiachan/xhs…e-skills
GitHub Stars
229
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail