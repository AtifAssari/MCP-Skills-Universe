---
title: w04-review-gate
url: https://skills.sh/qiao-925/qiao-skills/w04-review-gate
---

# w04-review-gate

skills/qiao-925/qiao-skills/w04-review-gate
w04-review-gate
Installation
$ npx skills add https://github.com/qiao-925/qiao-skills --skill w04-review-gate
SKILL.md
多智能体审查提示

任务执行完成且产生代码变更时，主动提示用户新开 Agent 审查未提交代码；收尾由用户审查通过后主动发起。

⚠️ 核心强制要求
触发条件
任务主要交付已完成
产生了代码变更（存在 git 未提交修改）
必须执行的提示

主动提示（陈述，非问句）：

主要交付已完成。**运动员不当裁判**：请新开 Agent 审查当前 git 未提交的代码，审查通过后再进入收尾流程。

AI Agent 行为要求
提示时机

在交付总结、用户尚未发起收尾之前，若存在未提交的代码变更，则输出上述提示。

与 W00 协同（自动 + 手动）
审查前可自动调用 w00-workflow-checkpoint checkpoint 记录“待审查”状态。
审查结论确认后可自动或手动调用 /w00-workflow-checkpoint 记录结果与下一步。
禁止事项
❌ 将本提示纳入 w05-task-closure 收尾流程（二者独立：先审查，后收尾）
❌ 使用问句（如「是否进入收尾？」）—— 收尾由用户审查通过后主动发起
Weekly Installs
14
Repository
qiao-925/qiao-skills
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass