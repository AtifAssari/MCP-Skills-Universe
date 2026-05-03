---
rating: ⭐⭐⭐
title: init-plugin
url: https://skills.sh/blueif16/amazing-claude-code-plugins/init-plugin
---

# init-plugin

skills/blueif16/amazing-claude-code-plugins/init-plugin
init-plugin
Installation
$ npx skills add https://github.com/blueif16/amazing-claude-code-plugins --skill init-plugin
SKILL.md
插件结构知识库
目的

此skill是知识库，供其他skills引用。不应被用户直接调用。

插件目录结构
开发工作目录（.claude/）

开发时所有组件都创建在 .claude/ 目录下，可立即测试：

.claude/
├── skills/                  # 立即可用的skills
│   └── {skill-name}/
│       └── SKILL.md
├── agents/                  # 立即可用的agents
│   └── {agent-name}.md
├── commands/                # 需要本地安装才能使用
│   └── {command-name}.md
└── hooks/                   # 立即可用的hooks
    └── hooks.json

发布打包目录（{plugin-name}-dev/）

sync-to-marketplace 时创建，用于发布到 marketplace：

{plugin-name}-dev/
├── .claude-plugin/
│   └── plugin.json          # 插件元数据
├── skills/                  # 从 .claude/skills/ 复制
│   └── {skill-name}/
│       └── SKILL.md
├── agents/                  # 从 .claude/agents/ 复制
│   └── {agent-name}.md
├── commands/                # 从 .claude/commands/ 复制
│   └── {command-name}.md
├── hooks/                   # 从 .claude/hooks/ 复制
│   └── hooks.json
├── .skillforge-meta        # SkillForge元数据
├── .gitignore
└── README.md

plugin.json 结构
{
  "name": "插件名称（小写，连字符）",
  "description": "插件描述",
  "version": "0.1.0",
  "author": {
    "name": "作者名称"
  }
}

SKILL.md 模板
---
name: skill-name
description: skill描述
allowed-tools: Tool1, Tool2
---

# Skill标题

## 说明

[你的说明]

## 示例

[你的示例]

Agent .md 模板
---
name: agent-name
description: agent描述
tools: Tool1, Tool2
model: sonnet
---

# Agent标题

[你的agent说明]

Command .md 模板
---
description: 命令描述
---

# /command-name

[当用户输入 /command-name 时Claude的说明]

hooks.json 模板
{
  "hooks": {
    "PreToolUse": [],
    "PostToolUse": [],
    "PermissionRequest": [],
    "UserPromptSubmit": [],
    "Notification": [],
    "Stop": [],
    "SubagentStop": []
  }
}

.skillforge-meta 模板
{
  "pluginName": "plugin-name",
  "version": "0.1.0",
  "createdAt": "2025-01-15T00:00:00.000Z",
  "lastSync": null
}

.gitignore (项目根目录)
.claude/settings*.json
{plugin-name}-dev/
.DS_Store
*.log

.gitignore ({plugin-name}-dev/ 目录)
.DS_Store
*.log
.skillforge-meta

README.md 模板
# {plugin-name}

{description}

## 安装

\`\`\`
/plugin marketplace add <marketplace-url>
/plugin install {plugin-name}
\`\`\`

## 使用

[文档]

验证规则
关键验证
YAML frontmatter: 必须以 --- 开始和结束
Skill名称: 仅小写字母、数字、连字符
必需字段: name, description
版本格式: 遵循semver (x.y.z)
文件命名
仅小写字母
无特殊字符（连字符除外）
目录名与文件名一致
组件类型说明
立即可用（创建在 .claude/ 后立即生效）
Skills: 创建在 .claude/skills/ 后立即可在当前会话使用
Agents: 创建在 .claude/agents/ 后立即可在/agents菜单使用
Hooks: 创建在 .claude/hooks/ 后立即生效
需要本地安装（Commands）
Commands: 创建在 .claude/commands/ 后，需要通过本地marketplace安装才能使用
先创建 command 在 .claude/commands/
本地安装测试: /plugin marketplace add ./.claude
安装: /plugin install {plugin-name}@local
测试: /{command-name}
发布到 Marketplace

使用 sync-to-marketplace skill：

自动创建 {plugin-name}-dev/ 目录
从 .claude/* 复制所有组件到 {plugin-name}-dev/*
同步到远程 marketplace
完整开发工作流
1. 开发阶段（在 .claude/ 中工作）
创建 skill    → .claude/skills/{skill-name}/SKILL.md     (立即可用)
创建 agent    → .claude/agents/{agent-name}.md           (立即可用)
创建 hook     → .claude/hooks/hooks.json                 (立即可用)
创建 command  → .claude/commands/{command-name}.md       (需本地安装测试)

2. 本地测试 Commands
/plugin marketplace add ./.claude
/plugin install {plugin-name}@local
/{command-name}

3. 发布到 Marketplace
运行 sync-to-marketplace skill:
  - 创建 {plugin-name}-dev/ 目录
  - 复制 .claude/* → {plugin-name}-dev/*
  - 添加 .claude-plugin/plugin.json
  - 添加 .skillforge-meta
  - 同步到远程 marketplace

4. 目录关系
.claude/                    # 开发工作目录（真实工作位置）
  ├── skills/
  ├── agents/
  ├── commands/
  └── hooks/

{plugin-name}-dev/          # 打包发布目录（由 sync 创建）
  ├── .claude-plugin/
  ├── skills/               # 从 .claude/skills/ 复制
  ├── agents/               # 从 .claude/agents/ 复制
  ├── commands/             # 从 .claude/commands/ 复制
  └── hooks/                # 从 .claude/hooks/ 复制

Weekly Installs
11
Repository
blueif16/amazin…-plugins
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass