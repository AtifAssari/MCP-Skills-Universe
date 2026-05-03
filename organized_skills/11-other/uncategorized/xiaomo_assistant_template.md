---
rating: ⭐⭐⭐
title: xiaomo-assistant-template
url: https://skills.sh/aaaaqwq/claude-code-skills/xiaomo-assistant-template
---

# xiaomo-assistant-template

skills/aaaaqwq/claude-code-skills/xiaomo-assistant-template
xiaomo-assistant-template
Installation
$ npx skills add https://github.com/aaaaqwq/claude-code-skills --skill xiaomo-assistant-template
SKILL.md
小a助手配置模板

基于 xiaomo-starter-kit 改编的 OpenClaw 助手配置模板，帮助老板aa快速配置个性化的 AI 助手。

核心功能
1. 生成助手配置文件

根据用户需求生成完整的助手配置文件套件：

SOUL.md - 助手灵魂文件（性格、行为准则）
USER.md - 用户画像（让助手了解主人）
IDENTITY.md - 助手身份设定（名字、形象、语气）
HEARTBEAT.md - 心跳检查项
MEMORY.md - 长期记忆模板
2. 使用方法

快速开始：

# 复制模板到新目录
cp -r skills/xiaomo-assistant-template/templates/* /path/to/new-assistant/


或让小a助手帮你生成：

"帮我创建一个新助手配置"
"生成助手身份文件"
"配置一个专注于编程的助手"
3. 模板文件说明
文件	用途
SOUL.md	定义助手的核心性格和行为边界
USER.md	记录用户信息，让助手更了解你
IDENTITY.md	设定助手的名字、形象和说话风格
HEARTBEAT.md	配置助手定期自动执行的检查项
MEMORY.md	助手的长期记忆存储
命名规范
助手名称: 小a助手
用户称呼: 老板aa
推荐配套 Skills

以下 skills 可从 ClawdHub 安装，与本模板配合使用：

# 天气查询
clawdhub install weather

# 自然语言提醒
clawdhub install remind-me

# 任务管理
clawdhub install jdrhyne/todo-tracker

# Google 套件（需 OAuth）
clawdhub install gog

# YouTube 视频摘要
clawdhub install youtube-watcher

参考来源

原模板来自 xiaomo-starter-kit，由孟健创建。

Weekly Installs
25
Repository
aaaaqwq/claude-…e-skills
GitHub Stars
53
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass