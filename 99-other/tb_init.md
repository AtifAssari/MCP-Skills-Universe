---
title: tb-init
url: https://skills.sh/kaelzhang321/teambition-agent-toolkit/tb-init
---

# tb-init

skills/kaelzhang321/teambition-agent-toolkit/tb-init
tb-init
Installation
$ npx skills add https://github.com/kaelzhang321/teambition-agent-toolkit --skill tb-init
SKILL.md
TeamBition 工作区初始化

重要：所有 tb-* skill 的凭证和配置都存储在当前工作目录下的 .teambition.md 文件中。不要去找 .mcp.json 或其他配置文件。

执行步骤
步骤 1：检查现有配置

检查当前工作目录下是否已有 .teambition.md：

已存在：读取并展示当前配置摘要（凭证、常用项目），用 AskUserQuestion 询问（3 个 option：重新配置 / 仅更新部分 / 取消）
不存在：告知用户"首次使用，需要配置 TeamBition 凭证"，从步骤 2 开始
步骤 2：配置凭证

在对话中告知用户：

请提供以下 4 个凭证（从 https://open.teambition.com → 应用管理 → 你的应用中获取）：

App ID
App Secret
Operator ID（你的用户 ID）
Organization ID（组织 ID）

请一次性粘贴，格式不限。

等用户回复后提取四个值。不要用 AskUserQuestion（这些是自由文本）。

步骤 3：配置参数

用 AskUserQuestion 收集（每个问题提供预设 option）：

最大常用项目数 — option: 3 / 5 / 8 / 10
最近任务记录数 — option: 5 / 10 / 15 / 20
步骤 4：写入临时配置

先将凭证写入 .teambition.md（至少包含凭证表格部分），这样后续脚本才能读取凭证获取 Token。

格式：

# TeamBition 工作区配置

> 由 /tb-init 生成，供所有 tb-* skill 读取
> 更新时间: {ISO时间}

## 凭证

| 参数 | 值 | 说明 |
|------|-----|------|
| App ID | {值} | 开放平台应用 ID |
| App Secret | {值} | 开放平台应用密钥 |
| Operator ID | {值} | 操作者用户 ID |
| Organization ID | {值} | 组织 ID |

> 凭证获取地址: https://open.teambition.com → 应用管理

步骤 5：选择常用项目

.teambition.md 已写入凭证，现在可以调用脚本：

node ${CLAUDE_SKILL_DIR}/scripts/tb-api.mjs get-projects


如果脚本报错（如 invalid appId），说明凭证填写有误，提示用户检查并重新输入。

成功后解析 JSON 中 data 数组，只展示 isArchived !== true 的项目。 用 AskUserQuestion（multiSelect，最多 4 个 option + Other）让用户选择常用项目。

步骤 6：生成完整 .teambition.md

用 Write 工具覆盖 .teambition.md，写入完整内容：凭证表格 + 配置表格 + 常用项目表格 + 空的最近任务表格。

## 配置

| 参数 | 值 |
|------|-----|
| 最大常用项目数 | {N} |
| 最近任务记录数 | {M} |

## 常用项目

| 序号 | 项目名称 | Project ID |
|------|---------|------------|
| 1 | {名称} | {ID} |
| ... | ... | ... |

## 最近任务

> 最近操作过的任务 ID（最新在前，最多保留 {M} 个）

| 序号 | Task ID | 标题 | 项目 | 操作时间 |
|------|---------|------|------|---------|

步骤 7：确认完成

展示配置摘要，告知用户后续可直接使用 /tb-create-task 等 skill。

Weekly Installs
10
Repository
kaelzhang321/te…-toolkit
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail