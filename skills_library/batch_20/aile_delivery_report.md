---
title: aile-delivery-report
url: https://skills.sh/zhucl1006/ailesuperpowers/aile-delivery-report
---

# aile-delivery-report

skills/zhucl1006/ailesuperpowers/aile-delivery-report
aile-delivery-report
Installation
$ npx skills add https://github.com/zhucl1006/ailesuperpowers --skill aile-delivery-report
SKILL.md
Aile：交付报告（aile-delivery-report）
来源原 Skill
来源：superpowers 交付收尾能力（已迁移为 aile-only）
策略：保留收尾决策与交付说明结构，并强化团队 PR/Jira 契约。
概述

本技能在提交 PR 时使用，目标是让 CR/QA/PM 在一个入口完成验收：

PR 必须引用计划与设计产物
PR 必须声明验证项（测试/构建等） -（可选）自动把 PR 链接回写 Jira，并流转状态
工作流程概览
项目初始化：project-docs-init（创建文档）
      ↓
需求分析：aile-requirement-analysis（结构化需求分析  + 更新文档）
      ↓
计划制定：aile-writing-plans（设计 + 计划）
      ↓
执行开发：aile-executing-plans 或 aile-subagent-dev（按计划执行 + 人工检查点）
      ↓
交付总结：aile-delivery-report（整理交付材料 + 回链 Story）

输出契约

PR Description 必须使用模板：docs-templates/stage3-pr-description-template.md。

至少包含：

Jira Story Key + 链接
Plan Reference：docs/plans/{Story-Key}/analysis.md（及可选 design.pencil）
Change Summary（2-3 句）
Verification（勾选项）
执行流程
从 analysis.md 提取 Story-Key 与计划引用
按模板生成 PR Description（可直接粘贴到 PR 平台） 3.（可选）若启用 Jira MCP：
在 Story Comment 贴 PR 链接并 @mention 开发负责人
Jira状态变更时调用 jira_update_issue 更新对应 Story 的状态字段为 developed
Weekly Installs
22
Repository
zhucl1006/ailes…erpowers
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass