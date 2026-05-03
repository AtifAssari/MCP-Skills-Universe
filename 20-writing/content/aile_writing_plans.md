---
title: aile-writing-plans
url: https://skills.sh/zhucl1006/ailesuperpowers/aile-writing-plans
---

# aile-writing-plans

skills/zhucl1006/ailesuperpowers/aile-writing-plans
aile-writing-plans
Installation
$ npx skills add https://github.com/zhucl1006/ailesuperpowers --skill aile-writing-plans
SKILL.md
Aile：写计划（aile-writing-plans）
概述

这是团队自有的计划产出技能，用于把阶段 1（PM 需求 + UI 示意）的输入，转化为阶段 2 的标准化产物：

计划主入口：docs/plans/{Story-Key}/plan.md（若已存在则使用 plan-{序号}.md）
可选设计文件：docs/plans/{Story-Key}/design.pen
主上下文文件：docs/plans/{Story-Key}/analysis.md

假設工程師對我們的程式碼庫的背景為零且品味有問題，則編寫全面的實施計劃。記錄他們需要知道的一切：每個任務要接觸哪些文件、程式碼、測試、他們可能需要檢查的文檔、如何測試它。將整個計劃作為小任務交給他們。

假設他們是一位熟練的開發人員，但對我們的工具集或問題領域幾乎一無所知。

假設他們不太瞭解良好的測試設計。

边界约束：

本技能只负责读取 Story 描述与 analysis.md，并产出 plan.md
analysis.md 是主要上下文文件；Story 描述用于校验边界与补充缺失背景
本技能不负责创建 Jira Sub-task
本技能不默认执行 Jira 写操作；如需 Jira 变更，应由后续独立流程处理
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

何时使用

在以下情形使用：

你已经拿到 Jira Story 的需求描述
docs/plans/{Story-Key}/analysis.md 已存在，且已完成需求分析
需要产出可被执行的、任务颗粒度 2-5 分钟的实施计划
需要把分析结果转成可执行、可验证、可交接的 plan.md
核心产出契约（必须遵守）
计划文件必须落在：docs/plans/{Story-Key}/
首次计划文件名固定为：plan.md
若 plan.md 已存在，新计划必须使用：plan-{序号}.md（如 plan-1.md、plan-2.md）
序号 从 1 开始递增，始终取当前目录下下一个可用序号
禁止覆盖已有计划文件（包括 plan.md 与历史 plan-{序号}.md）
文件必须包含：
状态管理（整体进度、任务状态总览、执行记录）
从 analysis.md 继承的需求理解与风险
从 analysis.md 继承并细化的 UI / 交互约束（如适用）
任务拆解（每个任务 2-5 分钟）
测试用例与验收标准（可测试、无歧义）
AI 执行指引（明确执行顺序、约束、人工 Gate 节点）
每个任务必须以 TDD 方式描述：RED → 验证失败 → GREEN → 验证通过 → REFACTOR → 再次验证
状态管理必须可追踪：每个任务都要有 状态、负责人、开始时间、完成时间、阻塞原因，初始状态统一为 待开始
计划内容必须显式标注：
Story 描述中的原始约束
analysis.md 中的关键结论
计划阶段新增的实现决策
若 analysis.md 缺失、内容明显不完整、或与 Story 描述冲突：停止生成计划，先提示用户补齐或更新分析文件
一口大小的任務粒度

每一步都是一個動作（2-5 分鐘）：

“編寫失敗的測試”-步驟
「運行它以確保它失敗」-步驟
“實現最少的程式碼以使測試通過” - 步驟
“運行測試並確保它們通過”- 步驟
“提交”-步驟
上下文优先级（必须遵守）
第一优先级： docs/plans/{Story-Key}/analysis.md
作为任务拆解、风险边界、验收标准、测试思路的主依据
第二优先级： Jira Story 描述 / AC / 附件链接
用于校验 analysis.md 是否偏离原需求
用于补足 analysis.md 未覆盖的业务背景
第三优先级： 相关规格与模块文档
docs/specs/PRD.md
docs/specs/SAD.md
docs/modules/*.md
若 Story 描述与 analysis.md 冲突：
不得直接继续写计划
必须先在输出中标记冲突点
提示用户先更新 analysis.md 或确认以哪一份为准
执行流程

开始时声明：“我正在使用 aile-writing-plans 技能来生成团队计划。”

Step 0：读取上下文
读取 Jira Story 描述、AC、附件链接（若可获得）
优先读取 docs/plans/{Story-Key}/analysis.md
读取 docs/README.md 与相关模块文档（如影响范围涉及 docs/modules/*）
读取（如存在）docs/specs/PRD.md、docs/specs/SAD.md
读取（如存在）本 Story 之前的计划产物（docs/plans/{Story-Key}/）
Step 0.1：校验分析文件
若 docs/plans/{Story-Key}/analysis.md 不存在：立即停止，并要求先完成 aile-requirement-analysis
若 analysis.md 缺少以下关键内容之一：需求理解、风险、验收标准、AI 执行指引
立即停止
输出缺失项
提示用户先补齐分析文件
若 Story 描述与 analysis.md 明显冲突：
列出冲突点
请求用户确认
未确认前不得生成 plan.md
Step 1：确认 Story-Key 与范围边界
明确 Story-Key（例如 ABC-123），作为目录名
以 analysis.md 为主，明确“做什么 / 不做什么”
用 Story 描述校验边界，防止 analysis.md 漏项或偏差
Step 2：任务拆解与排序
任务粒度：单任务 2-5 分钟
输出：每个任务明确文件路径、测试、验证命令、预期输出
每项任务都需要能回溯到 analysis.md 中的某个需求、风险或验收条目
DRY：复用现有模式，不新增不必要抽象
Step 3：写入计划文件

先确定“当前计划文件”：

若 docs/plans/{Story-Key}/plan.md 不存在：写入 plan.md
若 plan.md 已存在：按 plan-1.md、plan-2.md…顺序查找并写入首个不存在的文件
不得覆盖任何已有计划文件

将内容写入“当前计划文件”，并确保其至少包含以下结构：

文档元数据（Story-Key、输入来源、生成日期）

上下文摘要

Story 描述摘要
analysis.md 关键结论摘要

任务拆解

测试与验收映射

执行顺序与人工 Gate

风险与待确认事项

初始化状态管理模块：

填写“整体进度”
建立“任务状态总览”（所有任务默认 待开始）
建立“执行记录”并写入首条记录
Step 4：提交 Git 变更（需用户明确要求）
仅当用户明确要求“提交代码/提交变更”时执行 git commit
仅提交当前 Story 相关文件（至少包含当前计划文件，必要时包含 design.pen）
提交前检查变更范围，避免混入无关文件：
git status
git add docs/plans/{Story-Key}/
git status
推荐提交信息模板：docs(plan): add {Story-Key} {plan-file}
plan-file 示例：plan.md、plan-1.md
提交命令示例：git commit -m "docs(plan): add {Story-Key} {plan-file}"
Step 5：交接到执行阶段
推荐后续执行技能：aile-executing-plans 或 aile-subagent-dev
Weekly Installs
23
Repository
zhucl1006/ailes…erpowers
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass