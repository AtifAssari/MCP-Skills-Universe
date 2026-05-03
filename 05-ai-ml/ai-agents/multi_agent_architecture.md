---
title: multi-agent-architecture
url: https://skills.sh/aaaaqwq/claude-code-skills/multi-agent-architecture
---

# multi-agent-architecture

skills/aaaaqwq/claude-code-skills/multi-agent-architecture
multi-agent-architecture
Installation
$ npx skills add https://github.com/aaaaqwq/claude-code-skills --skill multi-agent-architecture
SKILL.md
Multi-Agent Architecture - 多 Agent 架构
概述

OpenClaw 支持多 Agent 架构，每个 Agent 可以有不同的：

专业领域和 System Prompt
模型配置和成本策略
Channel 绑定和权限
工具集和 MCP 配置
架构设计
推荐的 Agent 分工
┌─────────────────────────────────────────────────────────────┐
│                      Main Agent (小a)                        │
│  - 主会话处理                                                 │
│  - 任务分发和协调                                             │
│  - 复杂决策和规划                                             │
│  - 模型: opus-4.5 (高质量)                                    │
└─────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│   News Agent    │ │   Code Agent    │ │  Research Agent │
│  - 新闻抓取     │ │  - 代码生成     │ │  - 深度研究     │
│  - 内容摘要     │ │  - Bug 修复     │ │  - 文档分析     │
│  - 定时推送     │ │  - 代码审查     │ │  - 知识整合     │
│  模型: sonnet   │ │  模型: codex    │ │  模型: opus     │
└─────────────────┘ └─────────────────┘ └─────────────────┘
          │                   │                   │
          ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│  Quick Agent    │ │  Batch Agent    │ │  Monitor Agent  │
│  - 快速问答     │ │  - 批量处理     │ │  - 系统监控     │
│  - 简单任务     │ │  - 数据处理     │ │  - 健康检查     │
│  - 低延迟响应   │ │  - 文件操作     │ │  - 告警通知     │
│  模型: flash    │ │  模型: mini     │ │  模型: mini     │
└─────────────────┘ └─────────────────┘ └─────────────────┘

Agent 配置
1. 创建 Agent 目录结构
~/.openclaw/agents/
├── main/           # 主 Agent (已存在)
│   └── agent/
│       ├── AGENTS.md
│       ├── SOUL.md
│       └── ...
├── news/           # 新闻 Agent
│   └── agent/
│       ├── AGENTS.md
│       └── config.json
├── code/           # 代码 Agent
│   └── agent/
│       ├── AGENTS.md
│       └── config.json
├── research/       # 研究 Agent
│   └── agent/
│       ├── AGENTS.md
│       └── config.json
├── quick/          # 快速响应 Agent
│   └── agent/
│       └── config.json
└── batch/          # 批量处理 Agent
    └── agent/
        └── config.json

2. Agent 配置示例
News Agent (~/.openclaw/agents/news/agent/config.json)
{
  "model": {
    "primary": "anthropic/claude-sonnet-4-5"
  },
  "systemPrompt": "你是新闻抓取和摘要专家。专注于：\n1. 从权威来源抓取真实新闻\n2. 生成简洁准确的摘要\n3. 确保每条新闻有原文链接\n4. 按时推送到指定渠道",
  "tools": {
    "allow": ["web_fetch", "exec", "message"]
  }
}

Code Agent (~/.openclaw/agents/code/agent/config.json)
{
  "model": {
    "primary": "openrouter-vip/gpt-5.2-codex"
  },
  "systemPrompt": "你是代码专家。专注于：\n1. 高质量代码生成\n2. Bug 分析和修复\n3. 代码审查和优化\n4. 技术文档编写",
  "tools": {
    "allow": ["read", "write", "edit", "exec"]
  }
}

Quick Agent (~/.openclaw/agents/quick/agent/config.json)
{
  "model": {
    "primary": "google/gemini-flash-latest"
  },
  "systemPrompt": "你是快速响应助手。特点：\n1. 简洁直接的回答\n2. 低延迟响应\n3. 处理简单查询\n4. 不需要深度分析的任务"
}

3. 在 openclaw.json 中注册 Agent
{
  "agents": {
    "entries": {
      "news": {
        "enabled": true,
        "allowSpawnFrom": ["main"]
      },
      "code": {
        "enabled": true,
        "allowSpawnFrom": ["main"]
      },
      "research": {
        "enabled": true,
        "allowSpawnFrom": ["main"]
      },
      "quick": {
        "enabled": true,
        "allowSpawnFrom": ["main"]
      },
      "batch": {
        "enabled": true,
        "allowSpawnFrom": ["main"]
      }
    },
    "defaults": {
      "maxConcurrent": 4,
      "subagents": {
        "maxConcurrent": 8
      }
    }
  }
}

智能 Spawn 系统
任务分类规则

Main Agent 根据任务类型自动选择合适的 Agent：

任务类型	关键词	目标 Agent	模型
新闻抓取	news, 新闻, 早报, 推送	news	sonnet
代码任务	code, 代码, bug, 开发	code	codex
深度研究	research, 分析, 调研	research	opus
快速问答	简单, 快速, 查询	quick	flash
批量处理	batch, 批量, 文件	batch	mini
复杂任务	保留在 main	main	opus
智能 Spawn 实现
# 在 AGENTS.md 中添加智能 Spawn 逻辑

## 🧠 智能任务分发

当收到任务时，评估以下因素：

1. **任务复杂度**
   - 简单查询 → quick agent
   - 中等任务 → 专业 agent
   - 复杂任务 → main 处理或 research agent

2. **任务类型**
   - 新闻相关 → news agent
   - 代码相关 → code agent
   - 研究分析 → research agent
   - 批量操作 → batch agent

3. **时间敏感度**
   - 需要快速响应 → quick agent
   - 可以等待 → 专业 agent

4. **资源消耗**
   - 高 token 消耗 → 使用便宜模型的 agent
   - 需要高质量 → 使用 opus 的 agent

### Spawn 命令示例

```python
# 新闻任务
sessions_spawn(
    task="抓取今日科技新闻并推送到 DailyNews 群组",
    agentId="news",
    label="news-morning"
)

# 代码任务
sessions_spawn(
    task="修复 auth.py 中的登录 bug",
    agentId="code",
    label="fix-auth-bug"
)

# 研究任务
sessions_spawn(
    task="深度分析 GPT-5 的技术架构",
    agentId="research",
    label="gpt5-analysis"
)

# 快速查询
sessions_spawn(
    task="查询今天的天气",
    agentId="quick",
    label="weather-check"
)

并发处理
配置并发限制
{
  "agents": {
    "defaults": {
      "maxConcurrent": 4,      // 主 agent 最大并发
      "subagents": {
        "maxConcurrent": 8    // 子 agent 最大并发
      }
    }
  }
}

并发场景
用户消息 → Main Agent
              │
              ├─→ spawn(news) ──→ 抓取新闻
              │
              ├─→ spawn(code) ──→ 修复 bug
              │
              └─→ spawn(research) ──→ 深度分析
              
              ↓ (并行执行)
              
         所有任务完成后汇报

Channel 绑定
不同 Channel 使用不同 Agent
{
  "channels": {
    "telegram": {
      "defaultAgent": "main"
    },
    "whatsapp": {
      "defaultAgent": "main"
    }
  },
  "agents": {
    "entries": {
      "news": {
        "channels": ["telegram-newsbot"]
      }
    }
  }
}

监控和管理
查看活跃 Session
# 列出所有 session
openclaw sessions list

# 查看特定 agent 的 session
openclaw sessions list --agent news

查看 Spawn 状态
# 在代码中
sessions_list(kinds=["spawn"], limit=10)

最佳实践
1. 任务分发原则
简单任务不 spawn - 直接处理更快
耗时任务必 spawn - 不阻塞主会话
相关任务批量 spawn - 提高效率
2. 模型选择原则
质量优先 → opus
速度优先 → flash
代码任务 → codex
成本优先 → mini
3. 错误处理
# spawn 时设置超时
sessions_spawn(
    task="...",
    agentId="code",
    runTimeoutSeconds=300,  # 5分钟超时
    cleanup="keep"          # 保留 session 用于调试
)

相关资源
OpenClaw Agents 文档
Sessions Spawn 文档
模型配置指南

由小a设计 - 实现真正的多 Agent 协作

Weekly Installs
36
Repository
aaaaqwq/claude-…e-skills
GitHub Stars
53
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn