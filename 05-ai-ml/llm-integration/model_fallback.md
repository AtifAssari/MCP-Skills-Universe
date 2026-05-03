---
title: model-fallback
url: https://skills.sh/aaaaqwq/claude-code-skills/model-fallback
---

# model-fallback

skills/aaaaqwq/claude-code-skills/model-fallback
model-fallback
Installation
$ npx skills add https://github.com/aaaaqwq/claude-code-skills --skill model-fallback
SKILL.md
模型降级与故障切换（实战版）

⚠️ 本文档基于 OpenClaw 2026.3.28 (f9b1079) 实战验证，非理论文档。

触发词
模型降级 / fallback / 故障切换
model switch / LiveSessionModelSwitchError
cron 模型 / session model
shibacc 欠费 / 余额不足
一、Model 优先级机制
三层模型解析（优先级从高到低）
1. cron payload.model  →  单个 cron 任务独立指定
2. agent model.primary  →  agent 级配置
3. agents.defaults.model.primary  →  全局默认

额外层级
agents.defaults.subagents.model  →  sessions_spawn 子任务默认模型


⚠️ 易遗漏！ 2026-03-31 事故中，agent primary 已改但 subagents.model 还是旧值，导致子任务全部走失败的 provider。

二、Cron Model 继承机制
三种情况
payload.kind	payload.model	实际使用的模型
agentTurn	显式指定（如 zai/glm-5.1）	用指定的 ✅
agentTurn	未指定	继承 agent 的 primary model
systemEvent	N/A	不走 LLM，纯文本注入
payload.fallbacks 也可以独立指定
"payload": {
  "kind": "agentTurn",
  "model": "zai/glm-5.1",
  "fallbacks": ["minimax/MiniMax-M2.7-highspeed", "xingsuancode/claude-opus-4-6"],
  "message": "..."
}


不指定则继承 agent 的 fallbacks 配置。

三、Session 缓存陷阱（核心坑）
问题描述

OpenClaw session 以 JSONL 文件持久化在磁盘：

~/.openclaw/agents/*/sessions/*.jsonl


session 文件内缓存了当前使用的 model 名称。即使 config 改了 primary，session 文件里的旧 model 不会自动更新。

表现
isolated session（cron 默认）理论上每次创建新 session，但仍可能复用缓存的 model 映射
session:xxx（绑定到特定 session）100% 会复用旧 model
Gateway SIGUSR1 热重启（config reload）不清除 session 缓存
Gateway 完整重启也不清除——session 文件从磁盘重新加载
解决方案
对活跃 session：在 Telegram 群里对该 agent 执行 /new 重置 session
对 cron isolated session：等旧 session 自然过期被清理，或删除 session 文件后重启
对 sessionTarget="session:xxx" 的 cron：必须手动 /new 对应 session 或更新 cron 的 sessionTarget
四、LiveSessionModelSwitchError Bug
Bug 揎标题

GitHub Issue: openclaw/openclaw#58406

触发条件

当 fallback 过程中，OpenClaw 检测到 session 的 model 被并发修改（live session model switch detected before attempt），会把所有 fallback 候选模型标记为 candidate_failed (reason=unknown)，不实际尝试 API 调用。

日志特征
[model-fallback/decision] candidate_failed requested=shibacc/claude-opus-4-6 candidate=zai/glm-5.1 reason=unknown
[agent/embedded] live session model switch detected before attempt: zai/glm-5.1 -> shibacc/claude-opus-4-6

根因

Fallback 流程中的 "live session model switch detection" 过于激进，不区分：

真正的用户主动切换（应该放弃）
fallback 过程中的正常模型变化（应该继续尝试）
临时 Workaround
不要在 fallback 过程中手动 /model 切换
将所有 agent primary 设为可用模型，减少对 fallback 链的依赖
确保没有并发操作修改 session model
五、运维 SOP
模型供应商故障时
# 1. 确认哪个 provider 挂了
journalctl _PID=$(pgrep openclaw-gateway) --since "10 min ago" | grep -i "error\|403\|429"

# 2. 查看当前所有 agent primary
cat ~/.openclaw/openclaw.json | python3 -c "
import json, sys
c = json.load(sys.stdin)
print('defaults.primary:', c['agents']['defaults']['model']['primary'])
print('subagents.model:', c['agents']['defaults']['subagents']['model'])
for a in c['agents']['list']:
    print(f'  {a[\"id\"]}: {a.get(\"model\",{}).get(\"primary\",\"(inherit)\")}')"

# 3. 批量切换所有 agent + subagents + cron payload.model
# 见下方"一键切换脚本"

一键切换所有模型
# config.patch 方式（推荐）—— 改 agent primary + fallbacks + subagents.model
# 通过 gateway tool 的 config.patch 操作

# cron payload.model 批量更新
# 需要逐个 cron update，设置 payload.model + payload.fallbacks

检查 Session 缓存污染
# 统计所有 session 文件引用的 model
grep -rh '"model"' ~/.openclaw/agents/*/sessions/*.jsonl 2>/dev/null \
  | grep -oP '"model":"[^"]*"' | sort | uniq -c | sort -rn | head -20

# 查看特定 agent 的活跃 session
ls -lt ~/.openclaw/agents/quant/sessions/*.jsonl | head -5

验证 Fallback 链路
# 查看最近 30 分钟的 fallback 日志
journalctl _PID=$(pgrep openclaw-gateway) --since "30 min ago" \
  | grep -i "fallback\|candidate_failed\|model.*switch" | tail -30

六、配置检查清单
新增 Provider 时
 models.providers.<name> 配置 baseUrl + apiKey + models
 auth.profiles.<name>:default 配置认证模式
 .env 添加对应环境变量
 pass show api/<name> 确保密钥可用
修改模型时
 agents.defaults.model.primary — 全局默认
 agents.defaults.subagents.model — ⚠️ 易遗漏
 agents.list[].model.primary — 各 agent 独立配置
 agents.list[].model.fallbacks — fallback 链
 各 cron 的 payload.model — 需逐个更新
 各 cron 的 payload.fallbacks — 需逐个更新
故障恢复时
 对活跃 session 执行 /new 清除缓存
 确认 subagents.model 已更新
 force-run 一个 cron 验证新配置生效
 检查 session 文件中旧 model 引用是否清除
七、已知问题跟踪
问题	状态	Issue
LiveSessionModelSwitchError 导致 fallback 全链失败	🟡 已报 bug	#58406
SIGUSR1 热重启不清除 session model 缓存	🟡 待确认	-
isolated cron session 复用旧 model 映射	🟡 待确认	-

Last updated: 2026-03-31 — 基于 shibacc 余额耗尽事故的完整复盘

Weekly Installs
44
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