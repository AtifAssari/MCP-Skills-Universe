---
rating: ⭐⭐
title: aile-subagent-dev
url: https://skills.sh/zhucl1006/ailesuperpowers/aile-subagent-dev
---

# aile-subagent-dev

skills/zhucl1006/ailesuperpowers/aile-subagent-dev
aile-subagent-dev
Installation
$ npx skills add https://github.com/zhucl1006/ailesuperpowers --skill aile-subagent-dev
SKILL.md
Aile：子代理驱动开发（aile-subagent-dev）
来源原 Skill
来源：superpowers 子代理开发能力（已迁移为 aile-only）
团队改写：重构为面向 Codex subagent 的执行技能，明确输入为 analysis.md + 选定计划文件，并由主线程负责编排、审查与汇总
概述

本技能用于团队阶段 3 的计划执行，但它不是“默认执行模式”。

输入：docs/plans/{Story-Key}/analysis.md + 选定的计划文件
输出：按计划完成实现、验证、双阶段审查与最终汇总
角色分工：主线程做控制器；Codex subagent 负责实现、核对、审查等可拆分工作

核心原则：

必须同时读取 analysis.md 与计划文件，不能只看 plan.md
只有用户明确要求使用 subagent 模式时，才派发 Codex subagents
控制器负责读取上下文、拆任务、判定并行/串行、汇总结果
子代理只接收与自己任务相关的 Task Package，不自行通读整份计划
先做规格合规审查，再做代码质量审查
Codex Subagents 对齐

本技能对齐 Codex subagent 官方能力与使用原则：

子代理适用于复杂、可拆分、可并行的执行任务
是否真的派发 subagent，取决于主线程是否明确发起
内置角色优先使用 worker、explorer、default
主线程负责 orchestration，子代理负责 bounded task

因此，本技能的前提是：

用户明确要求使用 aile-subagent-dev
或用户明确要求“用 subagent / 子代理模式执行计划”
当前任务已经有阶段 2 产物：analysis.md 与计划文件
工作流程概览
项目初始化：aile-docs-init（创建文档）
      ↓
需求分析：aile-requirement-analysis（输出 analysis.md）
      ↓
计划制定：aile-writing-plans（输出 plan.md / plan-{n}.md）
      ↓
执行开发：aile-executing-plans 或 aile-subagent-dev
      ↓
交付总结：aile-delivery-report

何时使用

适用场景：

已经有可执行的 analysis.md 与计划文件
用户明确要求使用 Codex subagent 模式
计划可以按职责、模块或文件边界拆分
主线程更适合做控制器，而不是亲自串行完成全部编码细节

不适用场景：

用户没有明确要求 subagent 模式
任务强耦合、顺序依赖非常强，不适合拆分
analysis.md 或计划文件缺失
只是小改动，主线程直接完成更简单
与 aile-executing-plans 的边界

两者都属于阶段 3 的“执行计划”技能，但执行模式不同。

aile-executing-plans：

单主代理模式
主线程按批次推进任务
更适合强耦合、串行依赖明显、需要频繁人工检查点的计划

aile-subagent-dev：

Codex subagent 编排模式
主线程读取 analysis.md + 计划文件，构造 Task Package 后派发子代理
更适合复杂、可按职责拆分、存在并行空间的计划

选择原则：

主线程自己分批做完更直接：用 aile-executing-plans
需要“控制器 + 多子代理”协作执行：用 aile-subagent-dev
输入契约
必读文件
docs/plans/{Story-Key}/analysis.md
计划文件：
若用户明确指定：使用指定文件
若存在 plan-{序号}.md：使用最大序号文件
否则使用 plan.md
控制器读取要求
控制器在开始阶段一次性读取 analysis.md 与选定计划文件
从两份文件中提取需求边界、验收标准、任务拆解、依赖关系、验证命令
之后通过 Task Package 向子代理分发上下文，避免每个子代理重复读完整文档
Subagent 角色选择

默认优先考虑 Codex 内置角色：

worker
负责编码、修复、补测试、执行验证
默认承担 implementer
explorer
负责只读分析、规格核对、证据提取、差异核查
默认承担 spec reviewer
default
负责综合判断、跨任务质量评审、最终汇总
默认承担 code quality reviewer 或 final reviewer

如果当前系统还提供其他可用角色或自定义 subagent，控制器必须先分析其能力，再决定是否使用。不要机械地固定只用三种内置角色。

角色选择流程：

先识别当前系统可用的 subagent 角色
判断每个角色的主要能力边界：
是否擅长写代码
是否擅长只读分析
是否擅长综合评审
是否有特定领域能力，例如前端、测试、架构、数据、性能
将任务类型映射到最合适的角色
若没有更合适的系统角色，再回退到内置 worker / explorer / default
角色变了，职责边界不能变：
implementer 负责实现与验证
spec reviewer 负责规格核查
code quality reviewer 负责质量审查

选择原则：

写代码、改测试、修缺陷：优先 worker
读代码、对照 analysis.md / 计划文件核查实现：优先 explorer
做综合结论、全局质量判断、最终收口：优先 default
若系统存在更专业的角色，且其能力边界与任务更匹配，则优先选“更匹配的系统角色”

示例：

如果系统有专门的测试 reviewer 或 QA reviewer，可优先承担质量审查
如果系统有架构 reviewer，可优先处理跨模块设计一致性检查
如果系统有前端/后端/数据方向 implementer，可按任务域派发给对应角色

若仓库后续提供自定义 subagent，可替换默认角色，但职责边界不能变。

Task Package 规范

每次派发子代理前，控制器都要构造最小充分的 Task Package，至少包含：

任务编号与标题
任务目标与范围
来自 analysis.md 的需求边界、风险、验收标准
来自计划文件的任务步骤、依赖、约束
允许修改的文件范围
禁止修改或需谨慎处理的区域
验证命令与完成判定
前序任务产物或依赖说明

Task Package 原则：

给子代理“做事所需的完整上下文”，但不要塞整份计划
控制器负责裁剪上下文，避免任务漂移
并行任务必须具备清晰的文件边界或写入边界
执行流程
第 1 步：装载上下文
读取 analysis.md
选择并读取计划文件
校验两份文件是否一致：
需求边界是否冲突
任务是否覆盖验收标准
验证命令是否足够支撑完成判定
建立执行看板，标记依赖、可并行项、阻塞项
第 2 步：决定调度策略

按以下顺序判断：

是否存在前置依赖
是否会写同一文件集
是否适合并行
每个任务应该使用哪种 subagent，以及是否存在比内置角色更匹配的系统角色

若多个实现任务会修改同一文件集，则必须串行。

第 3 步：派发 implementer

对每个可执行任务：

构造 Task Package
派发 worker implementer
要求 implementer：
若存在阻塞疑问，先提问再动手
仅实现任务范围内内容
运行计划要求的验证
完成后先做自检，再回报结果
第 4 步：规格合规审查

implementer 回报后，控制器派发 spec reviewer：

默认使用 explorer
对照 analysis.md、计划文件、验收标准、测试要求进行核查
必须直接阅读代码与验证结果，不信任 implementer 的口头回报

若发现问题：

退回同一 implementer 修复
修复后重新做 spec review
直到规格合规通过
第 5 步：代码质量审查

规格合规通过后，再派发 code quality reviewer：

默认使用 default
若只是窄范围差异核查，也可使用 explorer
关注可维护性、一致性、测试有效性、实现复杂度、边界处理

若发现问题：

退回 implementer 修复
修复后重新做质量审查
直到质量通过
第 6 步：任务完成与收口

每个任务通过后：

更新执行看板状态
记录验证证据
决定是否释放后续依赖任务

所有任务完成后：

视复杂度决定是否派发一次 final reviewer
汇总实现结果、验证结果、残余风险
进入 aile-delivery-report
子代理提示模板

建议按以下模板派发：

implementer-prompt.md
spec-reviewer-prompt.md
code-quality-reviewer-prompt.md

这些模板面向 spawn_agent / send_input 的消息编排，而不是旧式“让子代理自己读文件”的做法。

相关技能
aile-writing-plans：生成 analysis.md 与计划文件
aile-executing-plans：非 subagent 的计划执行模式
aile-delivery-report：执行完成后的交付收尾
危险信号

绝不要这样做：

用户没有明确要求 subagent，却擅自派发 Codex subagents
只读取计划文件，不读取 analysis.md
让子代理自己通读 analysis.md 或整份计划文件
在规格合规通过前提前进入代码质量审查
并行派发多个会写同一文件集的 implementer
子代理未运行验证就宣称完成
用 implementer 自检替代正式审查
跳过返工后的复审

遇到以下情况应停止并重新判断：

analysis.md 与计划文件冲突
任务无法拆出清晰边界
并行拆分会造成明显冲突
验证命令无法证明任务完成
记住
aile-subagent-dev 是“Codex subagent 执行模式”，不是默认执行模式
主线程是控制器，负责读取 analysis.md 与计划文件、构造 Task Package、派发与汇总
子代理应拿到定制上下文，而不是自己去读完整文档
规格合规先于代码质量
与 aile-executing-plans 的差别，不在“是否执行计划”，而在“是否使用 Codex subagent 编排”
Weekly Installs
23
Repository
zhucl1006/ailes…erpowers
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass