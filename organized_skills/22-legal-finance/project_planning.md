---
rating: ⭐⭐
title: project-planning
url: https://skills.sh/zhucl1006/skills/project-planning
---

# project-planning

skills/zhucl1006/skills/project-planning
project-planning
Installation
$ npx skills add https://github.com/zhucl1006/skills --skill project-planning
SKILL.md
项目规划（分析 + 计划一体化）

本技能用于在开发前产出可执行的“分析计划文件”，既完成需求分析，也完成实施任务编排。

何时使用
你要规划一个新功能、模块改造或缺陷修复
你希望先澄清需求，再得到可落地的开发任务
你需要一份可追踪状态的计划文档，供后续 project-workflow 执行

不适用：仅需直接编码、不需要分析与计划沉淀的超小改动。

核心产出契约（必须遵守）
输出文件：docs/plans/001-feature-name.md（3 位编号 + kebab-case 名称）。
模板来源：./plan-templates/combined-plan-template.md。
文档必须同时包含：
需求分析（目标、边界、风险、隐含需求、验收标准）
实施计划（任务拆解、依赖关系、TDD 执行步骤）
状态管理（整体进度、任务状态总览、执行记录）
每个任务必须可追踪：任务ID、状态、负责人、开始时间、完成时间、阻塞原因。
初始状态统一为：待开始。
工作模式
模式 A：分析驱动（需求不清晰）

触发信号：需求边界模糊、方案分歧明显、验收标准不完整。

执行方式：

一次只问一个问题，优先多选题
每轮给出 2-3 个方案（含推荐与权衡）
分段确认后再进入任务拆解
模式 B：直写计划（需求清晰）

触发信号：目标、范围、验收标准、技术约束都已明确。

执行方式：

快速复述需求并确认边界
直接输出分析结论与实施计划
执行流程
Step 0：读取上下文
读取 docs/README.md
读取相关规范（如存在）：docs/specs/PRD.md、docs/specs/SAD.md
读取相关模块文档（如存在）：docs/modules/*.md
检查既有计划：docs/plans/
Step 1：需求澄清与边界确认

至少明确以下内容：

业务目标（为什么做）
范围内 / 范围外（做什么 / 不做什么）
成功标准（如何判定完成）
关键约束（技术、时间、依赖）
Step 2：产出需求分析

在计划文档中输出：

需求摘要
用户路径 / 核心交互
验收标准（AC）草案：改写为可测试条目
风险与假设
隐含需求清单（权限、空状态、错误状态、性能、兼容性、可观测性）
Step 3：产出实施计划

任务拆解要求：

单任务粒度 2-5 分钟
明确依赖与执行顺序
每个任务包含 TDD 最小闭环：
RED：先写失败测试并验证失败
GREEN：最小实现并验证通过
REFACTOR：重构并回归验证
每个任务写清：文件路径、命令、预期结果、完成证据
Step 4：初始化状态管理

计划落地时必须初始化：

整体进度（按阶段）
任务状态总览表（全部任务默认 待开始）
执行记录（写入第一条记录）
Step 5：质量校验（写入前自检）
KISS：任务描述不绕弯、可直接执行
YAGNI：删除“可能以后要做”的内容
DRY：避免重复任务；相同模式合并
SOLID：任务职责单一、依赖方向清晰
可验证：每条 AC 都能映射到测试或验证动作
Step 6：交付与下一步

完成后明确提示：

计划文件位置
推荐使用 project-workflow 执行
如有未决问题，列出“阻塞项 + 建议决策”
对话与澄清规范
每次只推进一个关键问题
优先多选题，减少沟通成本
回答后立即更新分析结论，避免信息漂移
当信息不足时，明确标注“假设”而不是臆测
任务编写规则（强约束）
每个任务必须有唯一 任务ID（如 T01、T02）。
每个任务必须标注 依赖任务（无依赖写 无）。
每个任务必须列出：
创建文件
修改文件
测试文件
每个任务必须具备可执行命令与预期输出。
未通过 RED/GREEN/REFACTOR 任一环节，不得标记为 已完成。
与其他技能关系
project-docs-setup：先补齐项目文档，再做计划。
project-workflow：按本技能产出的计划执行开发。

建议链路：project-docs-setup → project-planning → project-workflow。

Weekly Installs
13
Repository
zhucl1006/skills
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass