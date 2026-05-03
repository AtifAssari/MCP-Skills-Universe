---
title: harness-engineering-zh
url: https://skills.sh/10xchengtu/harness-engineering/harness-engineering-zh
---

# harness-engineering-zh

skills/10xchengtu/harness-engineering/harness-engineering-zh
harness-engineering-zh
Installation
$ npx skills add https://github.com/10xchengtu/harness-engineering --skill harness-engineering-zh
SKILL.md
Harness Engineering

Harness = 为项目中工作的 AI Agent 提供的操作系统。Model 是 CPU，Context 窗口是 RAM，Harness 则是操作系统。

核心原则

从简单开始，仅在必要时增加复杂度。 每一个 Harness 组件都代表了对模型无法独立完成任务的一种假设。要对这些假设进行压力测试 — 随着模型能力的提升，这些假设会失效。为"删除"而构建。

何时激活此 Skill
信号	行动
空项目/新项目	→ 进行完整的项目设置 (Section 1)
用户对 Agent 感到沮丧	→ 诊断并修复 Harness 缺失 (Section 7)
现有项目需要改进	→ 评估并逐步改进
明确的 Harness 问题	→ 参考相关章节
工作流
对于新项目
评估 (Assess) — 项目是什么？技术栈？团队规模？Agent 将如何被使用？
设置 (Setup) — 创建基础 Harness 文件 → 阅读 references/01-project-setup.md
Context — 设计信息架构 → 阅读 references/02-context-engineering.md
约束 (Constraints) — 添加护栏和 Linters → 阅读 references/03-constraints.md
评估 (Evaluate) — 设置反馈循环 → 阅读 references/05-eval-feedback.md
如果项目涉及多 Agent 或长任务 → 阅读 references/04-multi-agent.md, references/06-long-running.md
对于诊断 (Agent 表现不佳)
立即阅读 references/07-diagnosis.md
识别是哪一层 Harness 出现了问题
从相关参考文档中应用针对性修复
对于逐步改进

评估当前 Harness 的成熟度，识别最薄弱的层级，一次改进一个层级。

Harness 层级 (快速参考)
层级	内容	参考文档
项目设置 (Project Setup)	AGENTS.md, docs/, 目录规范	01-project-setup.md
Context 工程 (Context Engineering)	Agent 看到的信息、渐进式展示、工作状态	02-context-engineering.md
约束与护栏 (Constraints & Guardrails)	Linters、类型系统、架构强制执行、安全自主权	03-constraints.md
多 Agent 架构 (Multi-Agent Architecture)	Agent 分离、协作协议、委派模式	04-multi-agent.md
Eval 与反馈 (Eval & Feedback)	测试、评分、GC Agent、可观测性	05-eval-feedback.md
长运行任务 (Long-Running Tasks)	进度跟踪、Context 重置、交付产物	06-long-running.md
诊断 (Diagnosis)	当 Agent 失败时 — 在 Harness 中识别根因，而非模型	07-diagnosis.md
自我更新协议

当你在项目中发现新的可复用 Harness 模式时：

识别它属于哪个参考文件（或者是否需要一个新文件）
添加该模式，包括：它解决了什么问题，何时使用，以及如何实现它
保持简洁 — 拒绝废话，只保留模式
Weekly Installs
36
Repository
10xchengtu/harn…ineering
GitHub Stars
71
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass