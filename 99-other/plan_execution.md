---
title: plan-execution
url: https://skills.sh/anian0/pick-skills/plan-execution
---

# plan-execution

skills/anian0/pick-skills/plan-execution
plan-execution
Installation
$ npx skills add https://github.com/anian0/pick-skills --skill plan-execution
SKILL.md
计划执行

按实施计划逐个执行模块，通过 subagent 连续实现模块内子步骤，模块边界审核确保质量。 默认范围只做模块级单元/集成测试，不做端到端测试。

版本号约定

1.X 为占位符。开始执行前先确认当前活跃版本号（查看 workplace/ 子目录），后续路径替换为该数字。

测试目录规范（强制）
workplace/1.X/test/
├── backend/
│   ├── unit/<module>/         # 后端单元测试（核心）
│   └── integration/<module>/  # 后端集成测试（仅关键路径）
├── frontend/
│   ├── unit/<page-or-store>/  # 前端单元测试
│   └── component/<component>/ # 前端组件测试
├── fixtures/                  # 共享测试数据
└── README.md                  # 运行命令矩阵 + 覆盖率目标


约束：

委派 implementer subagent 时，必须把"测试文件应落入的具体子目录"写进 prompt
模块审核 subagent 必须检查测试文件位置合规
如果 workplace/1.X/test/ 不存在，第一个被执行的模块负责创建该骨架（含 README.md）
本套 skill 不做端到端测试，因此测试目录中不应出现 e2e/
为什么用 Subagent

把模块委托给有隔离上下文的专用 agent。通过精确构建他们的指令和上下文，确保聚焦并成功完成模块。他们绝不继承你的会话上下文——你构建他们确切需要的内容。这也保护你的上下文用于协调。

核心原则：每个模块用新 subagent + 连续实现 + 边界审核。

模块状态管理

模块状态以计划文件中的状态列为准，不依赖内存（会话中断即丢失）。

时机	操作
开始执行某模块前	状态改为 执行中，保存文件
模块通过审核后	状态改为 完成，保存文件
用户决定不做某模块	改为 跳过，并在该模块章节末尾追加"跳过原因"与"受影响下游"；若下游依赖被跳过模块的输出，先与用户确认替代方案再继续
会话中断后恢复	读索引表，找第一个 待执行 或 执行中 模块继续；遇 跳过 直接越过，但需检查下游依赖是否仍可执行
按需加载原则
初始化：只读计划文件"执行索引"部分（紧凑表格），获取模块数量和顺序
执行每个模块前：通过标题跳转，只读该模块的"模块详情"章节，传给 subagent
执行流程（精简）
读取索引 → 选下一个待执行模块
       ↓
更新状态=执行中 → 委派实现 subagent (implementer-prompt.md)
       ↓
subagent 提问？→ 是：回答上下文 → 重新委派
              → 否：subagent 连续实现+自检+模块测试
       ↓
委派模块审核 subagent (module-reviewer-prompt.md)
       ↓
审核通过？→ 否：让实现 subagent 修复 → 重新审核
        → 是：更新状态=完成
       ↓
还有模块？→ 是：循环
        → 否：委派最终审核 subagent (final-reviewer-prompt.md) 做集成核对
              （仅做跨模块集成与验收标准核对，不做端到端测试）
       ↓
完成

模型选择

用足够完成模块的最弱模型以节省成本和时间。

模块类型	推荐模型
机械实现（重复性 CRUD）	最快最便宜
集成判断（多文件协调）	标准
模块审核	最强（需判断力）
最终集成核对	标准
禁止事项

绝不：

跳过模块审核（Spec 合规+代码质量+边界+测试目录合并为一次）
在审核有问题时继续下一个模块
让 subagent 自检替代实际审核
在执行过程中提交 git
并行委派多个实现 subagent（会冲突）
让 subagent 自己读取计划文件（由你提取当前模块详情后传入）
忽略 subagent 提问（回答后再继续）
在模块审核未通过时标记完成
接受"差不多符合"
把测试文件放在源码目录里
在没有为前端模块准备前端测试（单元/组件至少一类）的情况下声明前端模块完成
创建端到端测试（默认范围之外）
模块审核维度

模块审核器一次审核四件事：

1. Spec 合规（是否做了该做的）
子步骤完成度（是/否/部分）
缺失的要求（声称工作但未实现）
额外/不需要的工作（YAGNI）
2. 代码质量（是否做得好）
文件单一职责
关键接口命名清晰
遵循代码库现有模式
不逐行审查、不纠结格式（交给 linter）
3. 模块边界（接口是否正确）
输入：是否正确消费前置模块的接口/数据
输出：是否符合契约
数据格式、字段名、类型一致
4. 测试目录合规
所有新增测试文件位于 workplace/1.X/test/ 下
源码目录无残留 .test. / .spec. / test_*.py
后端单元在 backend/unit、集成在 backend/integration；前端单元在 frontend/unit、组件在 frontend/component
未出现 e2e/ 目录或端到端测试文件（出现即不通过，提醒移除）
前端模块至少包含单元/组件测试中的一类
测试命令可执行

审核传入：模块验收标准 + 引用的技术方案章节 + 相邻模块接口契约 + 本目录规范。

测试失败修复流程

模块测试失败时：

主控 agent 不修改代码，把失败摘要（命令、失败用例、错误日志）反馈给同一实现 subagent
委派该 subagent 仅修复测试失败相关的代码与测试
修复完成后再次运行模块测试命令
三次仍未通过 → 停止并向用户报告：当前情况、已尝试的修复、推测根因 → 由用户决定继续修、跳过还是回设计阶段
测试通过后无需重新做模块审核（除非修复涉及接口/架构变更，由主控判断）
最终审核（不做端到端测试）

所有模块完成后，委派最终审核 subagent（references/final-reviewer-prompt.md）做集成核对：

验收标准覆盖核查（需求文档每条验收 → 是否有模块覆盖）
模块间接口/数据格式一致性
横切关注点（错误处理、边界、用户反馈）是否完整
前端页面清单是否全部已实现
测试套件完整性（backend/unit、backend/integration、frontend/unit、frontend/component、fixtures、README）

不做：实际跑端到端用例、模拟完整用户路径——这些不在本套默认范围内。

提示词模板
references/implementer-prompt.md - 委派模块实现 subagent
references/module-reviewer-prompt.md - 委派模块审核 subagent（合并 Spec+质量+边界+测试目录）
references/final-reviewer-prompt.md - 委派最终审核 subagent（集成核对，不跑 E2E）
示例工作流
你：执行计划。

[读取计划.md "执行索引"，确认 6 个模块及顺序]

模块 M1：数据库迁移与模型
[读取 M1 详情，状态改"执行中"]
[委派 implementer，传入 M1 详情]

实现者："开始前 - 数据库连接配置在哪里？"
你："见技术方案 §1.2"
实现者：[实现] → 报告 DONE

[委派 module-reviewer]
审核：✅ 通过

[执行 M1 测试命令]
测试通过 → M1 状态改"完成"

模块 M2：业务服务层
... (同上)

[所有模块完成]
[委派 final-reviewer 做集成核对（不跑 E2E）]
最终审核：✅ 验收标准全部覆盖，集成无问题

完成！

优势
模块内上下文连续，减少切换开销
审核次数减少（每模块：实现者 + 1 审核者）
审核循环确保修复实际工作
测试聚焦单元+必要集成，省去 E2E 的高昂代价
早期发现问题比后期调试更便宜
与其他 Skill 的衔接
Skill	关系
implementation-planning	创建本 skill 执行的模块计划
tech-design	模块引用的技术方案来源
requirements-workshop	技术方案引用的需求来源
test-suite-maintainer（如有）	后续可基于 workplace/1.X/test/ 做测试整理与维护
Weekly Installs
9
Repository
anian0/pick-skills
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass