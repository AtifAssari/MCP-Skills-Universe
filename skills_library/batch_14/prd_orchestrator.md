---
title: prd-orchestrator
url: https://skills.sh/blueif16/amazing-claude-code-plugins/prd-orchestrator
---

# prd-orchestrator

skills/blueif16/amazing-claude-code-plugins/prd-orchestrator
prd-orchestrator
Installation
$ npx skills add https://github.com/blueif16/amazing-claude-code-plugins --skill prd-orchestrator
SKILL.md
PRD编排器

所有者: 仅主协调器

职责
接收 PRD 文件路径（如 docs/prds/reddit-bot.md）
创建项目文件夹结构
移动原始 PRD 到项目文件夹
分析 PRD 复杂度并决策拆分策略
生成 meta.yaml 和各部分的 mini-PRD
为每个部分生成验收标准和上下文边界
项目文件夹结构

当接收到 PRD 时，创建以下结构：

docs/prds/reddit-bot/
├── original.md          # 移动的原始 PRD（非复制）
├── meta.yaml           # 项目元数据和进度跟踪
└── sections/           # 各部分的详细信息
    ├── auth/
    │   ├── mini-prd.md
    │   └── checklist.md
    └── payments/
        ├── mini-prd.md
        └── checklist.md


重要： 原始 PRD 文件必须被移动（mv）而非复制，确保单一数据源。

拆分标准

默认行为：始终创建目录结构和 sections，即使 PRD 很小

拆分策略：

复杂 PRD：拆分为多个 sections
简单 PRD：创建单个 section
无论大小，都必须创建完整的项目文件夹结构
输出格式
meta.yaml
project: reddit-bot
created: 2025-01-15T10:00:00Z
original_prd: ./original.md
status: in_progress  # in_progress | completed | blocked

sections:
  auth:
    status: pending  # pending | in_progress | completed | blocked
    branch: reddit-bot/auth
    progress: "0/4"
    files_created: []

  payments:
    status: pending
    branch: reddit-bot/payments
    progress: "0/5"
    files_created: []

merge_status:
  completed: []
  pending: []
  conflicts: []

sections/{section-id}/mini-prd.md
# 认证模块

## 范围
实现用户注册、登录和令牌管理功能。

## 验收标准
- 用户可以使用邮箱/密码注册
- 登录时签发 JWT 令牌
- 受保护路由拒绝无效令牌
- 刷新令牌轮换正常工作

## 上下文边界
**拥有:** src/auth/*, src/middleware/auth.ts
**读取:** src/config/*, src/types/*
**禁止:** src/payments/*, src/ui/*

完成流程

编排完成后，立即将 meta.yaml 路径移交给 execution-manager。execution-manager 将：

为每个 section 创建 git worktree 和 tmux 会话
监控所有部分直到完成
自动调用 merge-resolver 合并结果

prd-orchestrator 只负责规划，不执行具体实现。

Weekly Installs
12
Repository
blueif16/amazin…-plugins
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass