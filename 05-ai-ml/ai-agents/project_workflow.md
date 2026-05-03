---
title: project-workflow
url: https://skills.sh/zhucl1006/skills/project-workflow
---

# project-workflow

skills/zhucl1006/skills/project-workflow
project-workflow
Installation
$ npx skills add https://github.com/zhucl1006/skills --skill project-workflow
SKILL.md
项目工作流

文档驱动的项目开发工作流，确保每次开发任务都有据可循、可追溯。

重要提示：本 skill 假设项目已有完整的文档结构（docs/README.md、PRD.md、SAD.md 等）。如果是新项目或缺少文档，强烈建议先使用 project-docs-setup skill 创建完整文档。如果需要制定新的开发计划，建议使用 project-planning skill。

工作流程概览
项目初始化：project-docs-setup（创建文档）
      ↓
计划制定：project-planning（需求澄清 + 设计 + 计划）
      ↓
执行开发：project-workflow（执行计划 + 更新文档）

前置要求
项目文档

本 skill 依赖完整的项目文档体系。如果项目缺少文档：

推荐做法：

使用 project-docs-setup skill：
  /project-docs-setup
  或告诉我："创建项目文档"

该 skill 会：
- 通过多轮对话了解项目需求
- 提供专业的产品和架构分析
- 生成完整的 PRD、SAD、开发指南等文档


快速模式： 不提供最小化目录结构创建。如需补全文档结构，请使用 /project-docs-setup。

代码审查 Agent

本 skill 使用 通用型 agent 进行代码质量检查和优化。

代码审查功能：

代码质量审查（代码规范、最佳实践）
Bug 和安全漏洞检测
性能优化建议
可读性和可维护性分析

使用方式：

使用 Task 工具调用：
  subagent_type="general-purpose"
  description="Code review for recent changes"
  prompt="详细的代码审查提示..."


审查流程：

调用通用型 agent 分析代码变更
agent 生成详细的审查报告
根据报告修复问题
重新运行审查直到没有重大问题
核心流程
0. 初始化文档结构 → 1. 读取文档 → 2. 判断任务类型
   ├─ 指定 plan → 3. 执行已有计划 → 代码审查 → 修复优化 → 4. 更新文档
   └─ 无 plan → 提示使用 project-planning 创建计划

Phase 0: 检查文档结构

在开始执行前自动检查。

0.1 检查必需的文档

检查项目是否存在标准文档结构：

# 检查必需的目录和文件
- docs/README.md           # 文档索引（必需）
- docs/plans/              # 计划文件目录
- docs/specs/              # 规格文档

0.2 文档缺失处理

如果检测到文档结构不完整：

1. 显示检测结果：
   "检测到项目缺少文档结构"

2. 提供建议：
   "建议使用 project-docs-setup skill 创建完整的项目文档：
   - 该 skill 会通过多轮对话了解项目需求
   - 自动生成 PRD、SAD、开发指南等完整文档
   - 提供最佳实践建议和架构分析

   运行方式：
   /project-docs-setup
   或
   告诉我：'创建项目文档'"

3. 默认行为：
   停止执行并引导使用 /project-docs-setup 生成完整文档结构。

0.3 文档已存在

如果文档结构完整，显示确认信息并跳过此阶段：

✓ 检测到完整的文档结构
✓ 直接进入 Phase 1

Phase 1: 读取项目文档

每次执行前必须完成。

1. 读取 docs/README.md 获取文档索引
2. 根据索引读取任务相关的文档：
   - 规格文档 (specs/)
   - 模块文档 (modules/)
   - 开发指南 (guides/)
3. 读取 AGENTS.md（如存在）了解项目约定


关键文档优先级：

架构设计 (SAD.md) > 需求文档 (PRD.md) > 模块文档 > 指南
Phase 2: 判断任务类型

根据用户输入判断是执行已有计划还是创建新计划。

2.1 识别任务类型

执行已有计划的标志：

用户明确指定 plan 编号："执行 plan 001"、"继续 001-user-authentication"
用户说"执行计划"、"继续上次的任务"且有进行中的计划

创建新计划的标志：

用户描述功能需求："实现用户认证"、"添加 OCR 模块"
用户说"开始开发 XXX 功能"
2.2 路由逻辑
if 用户指定了 plan 编号 or 有明确的进行中计划:
    → Phase 3: 执行已有计划
else:
    → 提示用户先使用 project-planning 创建计划

2.3 使用示例

场景 1：执行已有计划

用户："执行 plan 001"
或
用户："继续 001-user-authentication 的开发"

→ 路由到 Phase 3，读取并执行该计划


场景 2：没有计划

用户："实现用户认证功能"
或
用户："添加 API 速率限制"

→ 提示用户先使用 project-planning 创建计划：
   "请先使用 project-planning skill 创建实施计划。
    运行方式：/project-planning
    或告诉我：'帮我规划这个功能'"

Phase 3: 执行已有计划

当用户指定了具体的 plan 文件时，直接执行该计划。

3.1 读取计划
1. 根据用户指定的编号定位 plan 文件（如 docs/plans/001-user-authentication.md）
2. 读取计划文件完整内容
3. 检查计划状态（待执行/进行中/已完成）

3.2 创建任务列表
1. 使用 TodoWrite 将计划中的任务转为 todos
2. 将计划状态更新为"进行中"

3.3 逐步执行
对于每个任务：
  1. 标记 todo 为 in_progress
  2. 参考相关文档执行任务
  3. 运行测试/验证
  4. 标记 todo 为 completed
  5. 更新计划文件中的任务状态 [x]
  6. 在执行记录表格中添加记录


执行原则：

遵循项目 AGENTS.md 中的 CONVENTIONS 和 ANTI-PATTERNS
遵循 TDD：先写测试，再实现
每完成一个任务立即更新计划文件
3.3.1 子代理任务循环（仅在平台支持子代理时启用）
对每个任务：
  1. Implementer：实现与测试，自查结果
  2. Spec Review：验证是否完全匹配计划/规格
     - 不通过 → 返回 Implementer 修复 → 重新 Spec Review
  3. Quality Review：工程质量与可维护性检查
     - 不通过 → 返回 Implementer 修复 → 重新 Quality Review
  4. 通过两阶段审查后标记任务完成

3.4 完成验证
1. 确认所有任务完成
2. 运行完整测试套件
3. 执行代码审查
4. 修复优化循环
5. 将计划状态更新为"已完成"
6. 进入 Phase 4 更新文档

3.5 代码审查和修复循环

使用通用型 agent 进行代码质量检查：

循环执行直到没有重大问题：
  1. 调用通用型 agent
     使用 Task 工具：
       subagent_type="general-purpose"
       description="Code review for recent changes"
       prompt="
         请审查此功能/任务的代码变更。

         重点关注以下方面：
         1. 代码质量和最佳实践
            - 代码风格和一致性
            - 遵循项目约定（检查 AGENTS.md 如果存在）
            - SOLID 原则和设计模式

         2. Bug 和安全性
            - 潜在的 Bug 或边界情况
            - 安全漏洞（SQL 注入、XSS 等）
            - 错误处理完整性

         3. 性能
            - 性能瓶颈
            - 低效的算法或查询
            - 内存泄漏或资源管理问题

         4. 可维护性
            - 代码可读性和清晰度
            - 文档和注释（必要时）
            - 测试覆盖率

         请按严重程度分类问题：
         - 阻塞性：必须修复的关键问题（安全性、严重 Bug）
         - 重要：应该修复的重要问题（性能、代码质量）
         - 次要：改进建议（可读性、小优化）

         请为每个问题提供具体的文件路径和行号。
       "

  2. 分析审查报告
     - 代码规范问题
     - 潜在 Bug 和安全漏洞
     - 性能优化建议
     - 可维护性问题

  3. 根据严重程度分类
     - 阻塞性问题（必须修复）：安全漏洞、严重 Bug
     - 重要问题（应该修复）：性能问题、代码规范
     - 建议性优化（可选）：可读性改进、小优化

  4. 修复阻塞性和重要问题
     - 修改代码
     - 运行测试确保修复有效
     - 更新相关文档

  5. 重新运行代码审查
     - 验证问题已解决
     - 检查是否引入新问题

  6. 确认完成
     - 没有阻塞性问题
     - 重要问题已修复或有计划处理
     - 用户确认可以继续


代码审查原则：

阻塞性问题必须在此阶段解决
重要问题应该尽量解决
建议性优化可以记录到技术债务，后续处理
每次修复后重新运行代码审查
最多迭代 3-5 轮，避免过度优化
Phase 4: 更新文档

任务完成后，更新受影响的文档。

必须检查并更新的文档：

变更类型	需更新的文档
新增模块	docs/modules/{module}.md, docs/specs/SAD.md
API 变更	docs/api/*.md
数据库变更	docs/database/SCHEMA.md
新增功能	docs/specs/PRD.md
架构调整	docs/specs/SAD.md, AGENTS.md

更新 AGENTS.md：

如有新的约定或反模式，添加到对应章节
更新 CHANGELOG 记录变更
异常处理
场景	处理方式
无 docs/ 目录	停止执行并引导 project-docs-setup
无 docs/plans/ 目录	停止执行并引导 project-docs-setup
无计划文件	提示用户使用 project-planning 创建计划
代码审查 agent 执行失败	检查错误信息，尝试重新执行或跳过代码审查
代码审查发现阻塞性问题	必须修复后才能继续，记录到执行记录
代码审查迭代超过 5 轮	与用户讨论，决定是否继续优化或接受当前状态
计划执行中断	恢复时读取计划文件，从未完成任务继续
任务执行失败	记录失败原因到执行记录，询问用户处理方式
需求变更	更新计划文件，标记原任务状态，添加新任务
附录
计划文件命名规范
docs/plans/
├── 001-user-authentication.md
├── 002-llm-service-integration.md
├── 003-ocr-module.md
└── ...


命名规则：

格式：001-feature-name.md（3位数字编号 + 功能名称）
编号从 001 开始，递增
功能名称使用小写字母和连字符，简洁明确
使用 project-planning 制定计划

当没有计划文件时，使用 project-planning skill 创建计划：

调用 project-planning：

使用 Skill 工具调用：skill="project-planning"
或告诉用户："/project-planning" 或 "帮我规划这个功能"


project-planning 会自动：

判断需求清晰度
选择合适的模式（Brainstorming 或 Writing Plans）
产出计划文档（包含设计和实施，根据复杂度决定详细程度）
保存到 docs/plans/001-feature-name.md

完成后：

计划文件会保存到 docs/plans/001-feature-name.md（使用3位数字编号）
返回 project-workflow，使用 Phase 3 执行该计划

详细信息：

参考 project-planning skill 文档
支持需求澄清、设计讨论、详细计划编写
Weekly Installs
21
Repository
zhucl1006/skills
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass