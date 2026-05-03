---
rating: ⭐⭐
title: escalation-router
url: https://skills.sh/blueif16/amazing-claude-code-plugins/escalation-router
---

# escalation-router

skills/blueif16/amazing-claude-code-plugins/escalation-router
escalation-router
Installation
$ npx skills add https://github.com/blueif16/amazing-claude-code-plugins --skill escalation-router
SKILL.md
升级路由器

所有者: 仅子协调器

职责
分析error_report的复杂度
决策：研究员可以解决 或 需要人工
为选定路径格式化交接
向主协调器发送状态信号
决策标准

路由到研究员的情况：

错误是技术/知识缺口（缺少库使用、API混淆）
类似问题在线存在（可搜索）
不需要架构决策

路由到人工的情况：

需求模糊（PRD不清晰）
需要架构权衡
外部依赖阻塞（API密钥、服务）
研究员已经失败
研究员交接
research_request:
  problem_summary: "邮箱验证返回500而非400"
  error_report: {来自fix-engine的完整error_report}
  search_hints:
    - "express错误处理中间件"
    - "验证库自定义错误"
  constraints:
    - 不得更改API契约
    - 必须保留现有测试

人工交接

信号documenter子代理生成PRD，然后：

信号到主协调器: WAITING
原因: human_intervention_required
交接文档: ./handoff-prd-{section-id}.md

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