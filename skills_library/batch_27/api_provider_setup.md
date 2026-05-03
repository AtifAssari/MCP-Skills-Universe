---
title: api-provider-setup
url: https://skills.sh/aaaaqwq/claude-code-skills/api-provider-setup
---

# api-provider-setup

skills/aaaaqwq/claude-code-skills/api-provider-setup
api-provider-setup
Installation
$ npx skills add https://github.com/aaaaqwq/claude-code-skills --skill api-provider-setup
SKILL.md
API Provider Setup

为 OpenClaw 添加和配置第三方 API 中转站供应商。

配置位置

配置文件：~/.openclaw/openclaw.json

在 models.providers 部分添加自定义供应商。

配置模板
Anthropic 兼容 API（如 anapi、智谱）
{
  "models": {
    "mode": "merge",
    "providers": {
      "供应商名称": {
        "baseUrl": "https://api.example.com",
        "apiKey": "sk-your-api-key",
        "auth": "api-key",
        "api": "anthropic-messages",
        "models": [
          {
            "id": "model-id",
            "name": "显示名称",
            "reasoning": false,
            "input": ["text"],
            "contextWindow": 200000,
            "maxTokens": 8192,
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            }
          }
        ]
      }
    }
  }
}

OpenAI 兼容 API（如 OpenRouter）
{
  "models": {
    "mode": "merge",
    "providers": {
      "供应商名称": {
        "baseUrl": "https://api.example.com/v1",
        "apiKey": "sk-your-api-key",
        "auth": "api-key",
        "api": "openai-completions",
        "models": [
          {
            "id": "gpt-4",
            "name": "GPT-4",
            "reasoning": false,
            "input": ["text"],
            "contextWindow": 128000,
            "maxTokens": 4096
          }
        ]
      }
    }
  }
}

关键字段说明
字段	必填	说明
baseUrl	✅	API 端点地址（不含 /v1/messages 等路径）
apiKey	✅	API 密钥
auth	✅	认证方式，通常为 api-key
api	✅	API 格式：anthropic-messages 或 openai-completions
models	✅	该供应商支持的模型列表
models[].id	✅	模型 ID（调用时使用）
models[].name	❌	显示名称
models[].contextWindow	❌	上下文窗口大小
models[].maxTokens	❌	最大输出 token 数
models[].reasoning	❌	是否支持推理模式
添加模型别名

在 agents.defaults.models 中添加别名：

{
  "agents": {
    "defaults": {
      "models": {
        "供应商/模型id": {
          "alias": "简短别名"
        }
      }
    }
  }
}


⚠️ 重要约束：alias 字段必须是字符串，不能是数组！

// ✅ 正确
"alias": "opus46"

// ❌ 错误 - 会导致 Config validation failed
"alias": ["opus46", "aixn/opus46"]


如果需要多个别名指向同一模型，需要在 models 中添加多条记录：

"供应商/模型id": { "alias": "别名1" }

设置为默认模型

在 agents.defaults.model 中设置：

{
  "agents": {
    "defaults": {
      "model": {
        "primary": "供应商/模型id",
        "fallbacks": [
          "备选供应商1/模型id",
          "备选供应商2/模型id"
        ]
      }
    }
  }
}

添加流程

获取供应商信息

Base URL
API Key
API 格式（Anthropic 或 OpenAI 兼容）
支持的模型列表

使用 gateway config.patch 添加

gateway config.patch 添加供应商配置


重启 Gateway 生效

gateway restart


测试新模型

session_status(model="新供应商/模型id")

常见中转站配置示例
Anapi (Anthropic 中转)
"anapi": {
  "baseUrl": "https://anapi.9w7.cn",
  "apiKey": "sk-xxx",
  "auth": "api-key",
  "api": "anthropic-messages",
  "models": [{"id": "opus-4.5", "name": "Opus 4.5", "contextWindow": 200000}]
}

智谱 ZAI
"zai": {
  "baseUrl": "https://open.bigmodel.cn/api/anthropic",
  "apiKey": "xxx.xxx",
  "auth": "api-key",
  "api": "anthropic-messages",
  "models": [{"id": "glm-4.7", "name": "GLM-4.7", "contextWindow": 200000}]
}

OpenRouter VIP
"openrouter-vip": {
  "baseUrl": "https://openrouter.vip/v1",
  "apiKey": "sk-xxx",
  "auth": "api-key",
  "api": "openai-completions",
  "models": [{"id": "gpt-5.2", "name": "GPT-5.2", "contextWindow": 200000}]
}

WOW (LinuxDo API 中转 - OpenAI 兼容)
"wow": {
  "baseUrl": "https://linuxdoapi-api-wow.223387.xyz/v1",
  "apiKey": "pass show api/wow",
  "auth": "api-key",
  "api": "openai-completions",
  "models": [
    {"id": "grok-4.1-thinking", "name": "grok-4.1-thinking", "reasoning": true, "contextWindow": 128000},
    {"id": "grok-imagine-1.0", "name": "grok-imagine-1.0", "input": ["text","image"], "contextWindow": 128000},
    {"id": "kimi-k2.5", "name": "kimi-k2.5", "contextWindow": 128000}
  ]
}


别名配置（agents.defaults.models）:

"wow/kimi-k2.5": { "alias": "wow-k2.5" },
"wow/grok-4.1-thinking": { "alias": "wow-grok-4.1-thinking" },
"wow/grok-imagine-1.0": { "alias": "wow-grok-imagine-1.0" }

⚡ 同步 Auth Profiles（改 Key 后必做）

背景：OpenClaw 运行时优先读 ~/.openclaw/agents/<agent>/agent/auth-profiles.json 中缓存的 key，而非 openclaw.json。改了 openclaw.json 的 apiKey 后必须同步。

脚本：~/clawd/skills/api-provider-setup/scripts/sync-agent-auth.sh

# 改了 openclaw.json 的 key 后，一键同步所有 agent
~/clawd/skills/api-provider-setup/scripts/sync-agent-auth.sh

# 只同步指定 provider（如改了 zai 的 key）
~/clawd/skills/api-provider-setup/scripts/sync-agent-auth.sh --provider zai

# 只同步指定 agent
~/clawd/skills/api-provider-setup/scripts/sync-agent-auth.sh --agent quant

# 预览（不实际修改）
~/clawd/skills/api-provider-setup/scripts/sync-agent-auth.sh --dry-run

# 同步后重启
openclaw gateway restart


配置优先级链：

auth-profiles.json (缓存key) > models.json (provider定义) > openclaw.json (全局配置)


完整改 Key 流程：

改 openclaw.json → models.providers.<provider>.apiKey
运行 sync-agent-auth.sh [--provider <name>]
openclaw gateway restart

完整改模型流程：

改 openclaw.json → agents.list[] 或 agents.defaults.model
运行 sync-agent-auth.sh（清除旧 auth 缓存+错误计数）
openclaw gateway restart
故障排查
401 Unauthorized - API Key 错误或过期
404 Not Found - baseUrl 路径错误或 API 格式不匹配
模型不存在 - 检查 models[].id 是否正确
格式错误 - 检查 api 字段是否匹配供应商的 API 格式
常见问题与解决方案
API 格式不匹配导致 404

症状：消息发送成功，但 AI 返回 404 status code (no body)

原因：供应商的 API 格式配置错误。

诊断：

# 测试 Anthropic Messages API 格式
curl -X POST "https://your-api-endpoint/v1/messages" \
  -H "Content-Type: application/json" \
  -H "x-api-key: YOUR_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{"model":"model-id","max_tokens":10,"messages":[{"role":"user","content":"hi"}]}'

# 测试 OpenAI Completions API 格式
curl -X POST "https://your-api-endpoint/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"model":"model-id","messages":[{"role":"user","content":"hi"}],"max_tokens":10}'


解决：

确认供应商使用的 API 格式：

Anthropic 格式：使用 /v1/messages，请求体包含 messages 数组
OpenAI 格式：使用 /v1/chat/completions，请求体包含 messages 数组

修改 models.json 中的 api 字段：

{
  "providers": {
    "your-provider": {
      "api": "anthropic-messages"  // 或 "openai-completions"
    }
  }
}


重启 Gateway：

openclaw gateway restart


案例：

Anapi 使用 Anthropic Messages API，必须设置 "api": "anthropic-messages"
OpenRouter VIP 使用 OpenAI Completions API，必须设置 "api": "openai-completions"
智谱 ZAI 使用 Anthropic Messages API，必须设置 "api": "anthropic-messages"
Weekly Installs
28
Repository
aaaaqwq/claude-…e-skills
GitHub Stars
53
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail