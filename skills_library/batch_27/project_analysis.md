---
title: project-analysis
url: https://skills.sh/escapewu/skills/project-analysis
---

# project-analysis

skills/escapewu/skills/project-analysis
project-analysis
Installation
$ npx skills add https://github.com/escapewu/skills --skill project-analysis
SKILL.md
项目分析技能

本技能是项目的深度分析层。

它不负责每次开发前后的通用 docs 编排；那由 project-docs-workflow 负责。它的职责是：在现有文档不足、链路复杂或用户明确需要时，做只读取证、调用链梳理、图表整理和性能观察，并把结果整理进项目文档。

默认行为：创建或更新 docs。 不再使用 analysis-only。当用户没有明确指定时，应优先判断是新建文档还是更新现有文档，并实际写入 docs/ 或调用方指定的长期文档落点。

强制要求：凡是输出 Mermaid 图表，必须在同一位置紧跟对应的 ASCII/TUI 预览图，方便用户在终端和代码评审中直接审查结构。不得省略，不得标记为可选。

分析主题

本技能可用于以下分析主题：

architecture：系统架构、模块边界、依赖关系、外部服务
dataflow：模块数据流、调用链、关键数据变换、外部 I/O
sequence：主流程时序、跨层交互、关键分支
performance-risk：性能热点、放大点、瓶颈候选、风险链路
执行模式

仅保留两种模式，且默认优先写文档：

模式 A：new-doc（默认）

当分析结果适合沉淀为一篇新的长期文档时使用。这也是未明确指定模式时的默认选择。

适用场景：

当前 docs/ 中没有合适文档可承接
需要形成独立、可长期维护的架构 / 数据流 / 时序 / 风险文档
用户明确要求“新建文档”“补一篇文档”“单独整理成文档”

输出：

新建文档（优先落到 docs/feature-* / docs/reference-*）
结构化结论
证据路径
Mermaid 图 + ASCII/TUI 预览图
可长期维护的 section 结构
模式 B：update-doc

当已有 feature-* / reference-* / OVERVIEW.md 能承接本次分析结果时使用。

适用场景：

已存在相关文档，只是内容过期、缺失或不准确
用户明确要求“更新 docs”“补充到现有文档”“回填文档”
由 project-docs-workflow 升级调用并提供候选文档路径

输出：

基于现有 feature-* / reference-* / OVERVIEW.md 的增量更新
保留仍然正确的内容
仅更新过期、缺失或不准确的部分

模式选择规则：

默认先判断 update-doc 是否可行：若存在合适承接文档，优先更新而不是平行新建
若没有合适文档，转为 new-doc
不再允许 analysis-only
不再使用 standalone-report 作为独立模式；用户若要求独立报告，按 new-doc 处理并创建合适的新文档
标准执行 SOP
1. 理解需求并检查项目 docs

先明确：

用户要的是 architecture / dataflow / sequence / performance-risk 哪类分析
分析范围：全项目 / 模块级
目标模块、入口点、关键功能点
当前执行模式：new-doc / update-doc

优先检查：

docs/OVERVIEW.md
相关 docs/feature-*.md
相关 docs/reference-*.md

如果调用方（如 project-docs-workflow）已经提供候选文档路径，优先读取这些文档；如果没有，再自行扫描 docs/。

这些文档只能作为半可信上下文：

可用于快速建立模块心智模型
但必须继续以当前代码核实
文档与代码冲突时，以代码为准

进入分析后，必须在写文档前完成模式判断：

如果已有合适文档可承接，使用 update-doc
如果没有合适文档，使用 new-doc
不再停留在只输出终端结论而不写文件的状态

如 docs/ 中存在旧式分析文档、frontmatter 元数据或需要做补充检索，可选使用 metadata 扫描脚本作为辅助：

python3 <skills-root>/skills/project-analysis/scripts/scan_docs_metadata.py <项目根目录>/docs


它不是主判断依据。主判断依据应是：

docs/OVERVIEW.md
docs/feature-*.md
docs/reference-*.md
当前代码
2. 拆解子任务

在正式读代码前，先把分析拆成 2-4 个边界清晰、只读、可并行的子任务。

拆分原则：

每个子任务只负责一类证据收集，不直接写最终文档
子任务之间尽量不要共享上下文，避免重复搜索
主 agent 负责最终判断、冲突消解、图表整理、文档落点选择与最终写入

推荐拆分方式：

系统架构分析：技术栈与入口点 / 目录与模块边界 / 依赖关系、外部服务与性能风险
模块数据流分析：入口点定位 / 调用链与关键节点 / 数据模型、外部 I/O 与放大点
时序或性能排查：主流程 / 分支与异常路径 / 热点候选与观察结论
3. 子任务下发 SubAgent 并行实施

使用 Agent 工具启动 SubAgent 并行执行子任务。

执行要求：

优先让 subagent 做只读工作：Glob、Grep、Read、依赖梳理、调用链追踪、模块职责归纳
一次并行 2-4 个子任务即可，只并行真正独立的分析
每个 subagent 的 prompt 必须写清：分析目标、目标目录/文件/关键词、要返回的结构化结果
subagent 不要直接写最终文档，只返回事实、路径、调用链、关键结论、可疑缺口、风险点
主 agent 不要和 subagent 重复执行同样的检索
4. 汇总子任务信息并整理结果

主 agent 汇总各 subagent 的结果后，再统一形成分析输出。

主 agent 负责：

合并并去重各子任务结论
解决冲突信息，必要时补充定向查证
产出结构化分析结论
生成 Mermaid 图表和对应 ASCII/TUI 预览图
将结果整理并写入目标文档（新建或更新）
维护必要的文档结构，如 frontmatter、section、Changelog 与入口索引
5. Review 与写入

写入前至少检查：

目标文档是否选对（feature-* / reference-* / OVERVIEW.md）
若为更新，是否保留了仍然正确的旧内容
若为新建，是否真的没有更合适的现有文档可承接
新增结论是否能回溯到文件路径、模块、入口点或调用链
Mermaid 与 ASCII/TUI 预览图语义一致
是否需要同步更新该文档的 Changelog
如果是新增模块，是否需要同步更新 docs/OVERVIEW.md
如果本次形成新的稳定踩坑经验，是否应提示调用方考虑补充“历史教训”或规则文档

如发现更适合沉淀到规则层的经验，只负责识别并提示调用方；不要默认直接修改 CLAUDE.md。

6. 向用户汇报分析结果

完成后，向用户汇报：

当前执行模式
输出类型：新建文档 / 更新文档
包含哪些图表（架构图、时序图、数据流图等）
2-4 条关键发现概览
如有未覆盖边界、风险点或建议追加分析，也一并说明
文档保存路径，以及本次属于 new 还是 update
文档落点优先级

默认优先维护这一套长期项目文档：

docs/feature-*.md
docs/reference-*.md
docs/OVERVIEW.md

优先规则：

功能行为、模块实现、接口、数据模型、测试方式、变更记录，优先回填 feature-*
外部系统、第三方 API、架构参考、限制条件，优先回填 reference-*
新增模块、模块边界、文档索引入口，更新 docs/OVERVIEW.md

仅在下列情况才生成独立分析文档：

当前项目中没有合适的长期文档可承接
用户明确要求单独成文
分析结果本身具备独立维护价值，且不适合硬塞进现有文档

注意：独立文档仍属于 new-doc，不是单独的第三种执行模式。

独立分析文档命名（仅例外使用）
分析类型	文件名格式
系统架构	architecture.md
数据流	dataflow-{功能}.md
时序图	sequence-{流程}.md

注意：这类文件不是默认长期落点。优先仍是 feature-* / reference-* / OVERVIEW.md。

来自 project-docs-workflow 的调用约定

如果本技能由 project-docs-workflow 升级调用，调用方应尽量提供：

当前分析目标
当前执行模式：new-doc / update-doc
候选文档路径（如 docs/feature-xxx.md、docs/reference-xxx.md）
是否已经有明确落点
是否要求输出可直接合并到现有文档的完整 section / patch

收到这些信息时，本技能应：

优先复用调用方给出的候选文档
避免重复做 docs 扫描
优先产出可回填 section，而不是重新发明完整文档结构
参考文件
架构分析详细步骤：references/mode-architecture.md
数据流 / 时序分析详细步骤：references/mode-dataflow.md
输出规范与落点优先级：references/output-spec.md
Mermaid 图表模板：references/mermaid-templates.md
Weekly Installs
19
Repository
escapewu/skills
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass