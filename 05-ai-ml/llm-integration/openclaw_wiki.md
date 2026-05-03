---
title: openclaw-wiki
url: https://skills.sh/chujianyun/skills/openclaw-wiki
---

# openclaw-wiki

skills/chujianyun/skills/openclaw-wiki
openclaw-wiki
Installation
$ npx skills add https://github.com/chujianyun/skills --skill openclaw-wiki
SKILL.md
OpenClaw Wiki

OpenClaw 官方文档知识库，提供多渠道 AI Agent 网关的使用指南和技术参考。

设计模式

本 skill 主要采用：

Tool Wrapper：把 OpenClaw 官方文档包装成可按需调用的知识上下文
Reviewer（轻度）：先判断问题属于安装、配置、渠道、模型、工具还是排障
Gotchas
不要跳过本地文档直接联网搜，先查仓库内 docs
不要把用户的问题泛化成“大而全的 OpenClaw 介绍”，先回答具体问题
不要编造不存在的命令或配置项；不确定时回到 docs 定位
如果问题明显是运维执行类，而不是文档问答类，应考虑分流到 openclaw-ops
文档不足时才联网补充，不要把联网搜索当默认第一步
使用方式
首先查阅 INDEX.md 获取文档索引和内容概览
根据用户问题定位相关文档
使用 Read 工具读取对应的 docs/ 目录下的文档
如文档信息不足，再考虑联网搜索补充
文档结构
docs/
├── index.md              # 项目首页和概述
├── start/                # 快速开始、入门向导、安装设置
├── concepts/             # 核心概念：Agent、Session、Memory、Models
├── gateway/              # Gateway 配置、安全、远程访问、故障排查
├── channels/             # 渠道配置：WhatsApp、Telegram、Discord、iMessage 等
├── tools/                # 工具：Browser、Skills、Subagents、Exec
├── install/              # 安装指南：Docker、Node、macOS、Linux
├── providers/            # 模型提供商：Anthropic、OpenAI、Ollama 等
├── nodes/                # 移动节点：iOS、Android
├── cli/                  # CLI 命令参考
├── web/                  # Web Control UI
├── help/                 # 帮助和故障排查
├── security/             # 安全配置
├── plugins/              # 插件开发
├── automation/           # 自动化配置
└── zh-CN/                # 中文文档

常见问题分类
问题类型	参考文档
什么是 OpenClaw	docs/index.md
快速开始/安装	docs/start/getting-started.md, docs/start/quickstart.md
入门向导	docs/start/wizard.md, docs/start/onboarding.md
Gateway 配置	docs/gateway/configuration.md, docs/gateway/configuration-reference.md
WhatsApp 连接	docs/channels/whatsapp.md
Telegram 连接	docs/channels/telegram.md
Discord 连接	docs/channels/discord.md
iMessage 连接	docs/channels/imessage.md
群组消息	docs/channels/groups.md, docs/channels/group-messages.md
Agent 概念	docs/concepts/agent.md, docs/concepts/agent-loop.md
Session 管理	docs/concepts/session.md, docs/concepts/session-tool.md
Memory 功能	docs/concepts/memory.md
模型配置	docs/concepts/models.md, docs/concepts/model-providers.md
多 Agent 路由	docs/concepts/multi-agent.md
Browser 工具	docs/tools/browser.md
Skills 配置	docs/tools/skills.md, docs/tools/creating-skills.md
Subagents	docs/tools/subagents.md
命令执行	docs/tools/exec.md, docs/tools/exec-approvals.md
Docker 安装	docs/install/docker.md
远程访问	docs/gateway/remote.md, docs/gateway/tailscale.md
安全配置	docs/gateway/sandboxing.md, docs/gateway/authentication.md
故障排查	docs/gateway/troubleshooting.md, docs/help/
CLI 命令	docs/cli/
Pi Agent	docs/pi.md
Weekly Installs
47
Repository
chujianyun/skills
GitHub Stars
539
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykWarn