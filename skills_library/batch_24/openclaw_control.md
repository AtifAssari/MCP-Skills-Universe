---
title: openclaw-control
url: https://skills.sh/rtgs2017/nagaagent/openclaw-control
---

# openclaw-control

skills/rtgs2017/nagaagent/openclaw-control
openclaw-control
Installation
$ npx skills add https://github.com/rtgs2017/nagaagent --skill openclaw-control
SKILL.md
OpenClaw 控制技能

本技能让你能够控制和管理 OpenClaw AI 助手。

核心能力
1. 发送消息给 OpenClaw

通过 Naga 的 Agent Server API 向 OpenClaw 发送任务：

POST /openclaw/send
{
  "message": "你的消息内容",
  "wake_mode": "now"  // 立即执行
}

2. 检查 OpenClaw 状态
GET /openclaw/health - 健康检查
GET /openclaw/status - 运行状态
GET /openclaw/session - 会话信息
3. 管理 Gateway
POST /openclaw/gateway/start - 启动
POST /openclaw/gateway/stop - 停止
POST /openclaw/gateway/restart - 重启
GET /openclaw/gateway/status - 状态
4. 配置管理
GET /openclaw/config - 获取配置
POST /openclaw/config/model - 设置模型
POST /openclaw/config/hooks - 配置 Hooks
使用流程
检查连接: 先调用健康检查确认 OpenClaw 可用
发送任务: 使用 /openclaw/send 发送消息
监控结果: 通过 /openclaw/history 查看执行结果
注意事项
OpenClaw 默认运行在 http://127.0.0.1:18789
需要配置 Hooks Token 才能发送消息
建议使用免费的 GLM-4.7 模型进行测试
示例
让 OpenClaw 执行任务
{
  "message": "帮我整理桌面上的文件，按类型分类",
  "wake_mode": "now"
}

查询当前状态

调用 GET /openclaw/status 获取 OpenClaw 当前正在做什么。

Weekly Installs
57
Repository
rtgs2017/nagaagent
GitHub Stars
1.5K
First Seen
Feb 17, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass