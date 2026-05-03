---
rating: ⭐⭐
title: core-first-simplicity
url: https://skills.sh/qiao-925/qiao-skills/core-first-simplicity
---

# core-first-simplicity

skills/qiao-925/qiao-skills/core-first-simplicity
core-first-simplicity
Installation
$ npx skills add https://github.com/qiao-925/qiao-skills --skill core-first-simplicity
SKILL.md
核心优先简化

这个 skill-unit 处理的是“复杂度是否值得引入”问题。它要求先保住主亮点，再谈扩展性、完备性与优雅性。

核心原则
1. 核心价值 —— 先保住主亮点
先回答：当前任务最值得被保住的核心价值是什么。
如果只能交付一个结果，默认优先保住最能体现任务价值的那一部分。
无法直接增强核心价值的工作，默认延后，而不是顺手一起做。
2. 复杂度预算 —— 有证据再加复杂度
新层级、新抽象、新配置、新扩展点都属于复杂度支出。
只有在收益明确、证据充分、且复杂度可局部封装时，才允许增加复杂度。
“以后可能会用到”不是复杂度准入证据。
3. 主路径优先 —— 先稳主链路，再扩能力
先让主链路跑通、讲清、可验证，再处理边角能力。
默认优先单一路径、默认实现、最短闭环。
如果一个设计让主路径更难理解，它通常不是当前阶段的好设计。
4. 延后与删除 —— 非核心不抢主线
锦上添花但不影响当前目标的内容，延后。
收益不明确却明显增加认知负担的内容，删除。
当两个方案都能达标时，默认选更简单、更容易验证的那个。
AI Agent 行为要求
默认适用场景
场景	最低要求	不该做什么
项目取舍	先定义本轮唯一主亮点，再决定做什么	同时推进多个非核心方向
架构设计	先保主链路，再评估扩展点是否必要	为未来规模预埋过多层级
模块重构	先缩减复杂度，再谈抽象优雅	一边重构一边继续加能力
实现裁剪	先做最小闭环版本，再补增强项	把“顺手优化”混进主任务
默认执行方式
先说清当前任务的核心目标、主亮点和最小验收闭环。
把候选动作分成三类：必须做、可延后、应删除。
优先选择能最快验证核心价值的实现路径。
若要引入复杂度，必须说明证据、收益与封装边界。
给出明确的延后项，避免把“暂不做”说成“以后再看”。
高风险复杂度信号

出现以下任一情况时，应主动提醒用户：

还没验证主路径，就开始插件化、配置化、平台化
还没稳定需求，就先抽象出通用框架
为了“更优雅”把简单路径拆成很多层
同时推进重构、扩展、治理三类目标，导致主线失焦
场景化展开
涉及项目级取舍与范围控制时，读取 references/project-level.md
涉及架构与模块层的复杂度预算时，读取 references/architecture-level.md
涉及代码、函数与实现路径裁剪时，读取 references/implementation-level.md
与其他 skill 的协同边界
与 architecture-governance：当问题已进入分层、契约、依赖方向时联动，顺序为“先判断值不值得复杂化，再决定结构怎么落”。
与 roi-value-density：当用户在问“现在做这个值不值得”时联动，用 ROI 判断是否值得投入，用本 skill 判断复杂度是否过量。
与 file-guardrails：当复杂度已经落到单文件膨胀、注释冗余、拆分失控时联动。
与 single-responsibility：当问题核心是职责混杂时联动，顺序为“先识别主职责，再删除多余复杂度”。
判断标准
是否能用一句话说明当前任务最重要的主亮点。
是否存在一个更短、更直接、更容易验证的闭环方案。
引入的复杂度是否有明确证据支撑，而不是预防式设计。
是否保住了清晰默认路径，而不是让读者先理解一堆机制才能进入主流程。
是否明确列出了延后项与删除项，而不是把所有东西都塞进当前轮次。
反模式
把“未来可能扩展”当成今天复杂化的理由。
用抽象层、配置层、通用层掩盖尚未稳定的需求。
主路径还没跑通，就提前做多场景适配。
为了“设计完整”保留大量当前用不到的能力。
看到局部不优雅就大动干戈，却不解释对核心目标的增益。
参考资料
references/project-level.md - 项目级的主亮点识别与范围控制
references/architecture-level.md - 架构级与模块级的复杂度预算
references/implementation-level.md - 实现级的代码与函数简化方法
Weekly Installs
19
Repository
qiao-925/qiao-skills
First Seen
Feb 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass