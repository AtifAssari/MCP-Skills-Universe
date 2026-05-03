---
title: architecture-governance
url: https://skills.sh/qiao-925/qiao-skills/architecture-governance
---

# architecture-governance

skills/qiao-925/qiao-skills/architecture-governance
architecture-governance
Installation
$ npx skills add https://github.com/qiao-925/qiao-skills --skill architecture-governance
SKILL.md
架构治理

这个 skill-unit 处理的是“架构边界与演进质量”问题。它不替代具体职责拆分；当问题已经落到文件、类、函数职责边界时，应联动 single-responsibility。

核心原则
1. 分层与依赖方向 —— 单向流动
依赖方向必须单向流动：上层依赖下层，禁止反向依赖。
禁止跨层直连：上层通过明确的应用接口或服务访问下层能力。
基础设施实现不得承载业务决策。
每个模块都应能回答：自己属于哪一层、依赖谁、被谁依赖。
2. 架构变更影响面 —— 先看上下游
变更前先标注所在层级、主要职责、上游调用方、下游依赖与数据流。
任何接口变更都必须说明兼容策略：兼容、适配、版本化，至少占一种。
分层结构调整、依赖方向变化、数据流主路径重排，都属于高风险架构变更。
不能只看当前改动点本身，还要看它会把风险传播到哪里。
3. 接口契约与可替换性 —— 依赖抽象，不依赖实现
契约先于实现：优先定义稳定边界，再选择具体实现。
调用方默认依赖 Protocol / ABC 等抽象边界，而不是直接依赖具体实现。
依赖应通过构造函数、工厂或注册表组装，不通过静态单例硬绑定。
可替换能力应做到：新增实现时，不需要改主流程代码。
AI Agent 行为要求
默认适用场景
场景	最低要求	不该做什么
架构评审	明确层级边界、依赖方向、风险点	只谈抽象理念，不落到具体模块
重构设计	先看影响面，再决定是否调整结构	不做影响分析就直接改接口或分层
新模块设计	先定契约与层级归属，再选实现	先写实现，后补边界
项目初始化分析	先扫结构、依赖、核心流程，再给建议	一上来就给大而全改造方案
默认执行方式
先判断当前问题是不是“架构边界与演进质量”问题。
若是，优先检查三件事：依赖方向、影响面、契约与可替换性。
若改动已落到职责拆分层面，联动 single-responsibility。
若判断依赖外部框架、文档或版本能力，再联动 source-quality-control。
若用户在问“这次架构调整值不值得做”，再联动 roi-value-density。
高风险变更要求

出现以下任一情况时，应主动升级给用户决策：

分层结构调整或依赖方向改变
核心接口破坏性变更
数据流主路径重排
对性能、容量、一致性或扩展性有显著影响
项目初始化分析

当任务是“新接手项目的首轮架构体检”时，至少完成以下动作：

扫描技术栈、目录结构、模块边界与依赖关系。
明确业务目标、核心流程、关键组件与数据模型。
从架构、质量、性能、安全、可扩展性五个维度给出结论。
输出优先级明确的改进建议，避免一次性大改。
场景化展开
涉及分层与依赖规则时，读取 references/layering-and-dependencies.md
涉及架构变更风险评估时，读取 references/change-impact-analysis.md
涉及契约、依赖注入、可插拔设计时，读取 references/interface-di-and-pluggability.md
涉及新接手项目的首轮体检时，读取 references/project-initial-analysis.md
与其他 skill 的协同边界
与 single-responsibility：当核心问题是职责拆分时联动，顺序为“先定边界，再拆职责，再复核依赖”。
与 source-quality-control：当结论依赖外部框架、平台文档、版本差异或官方设计说明时联动。
与 roi-value-density：当用户在比较多种架构方向，或判断某次重构是否值得投入时联动。
判断标准
是否可以清楚回答“这次改动在哪一层、影响谁、依赖谁”。
是否仍满足单向依赖，且没有新增循环依赖。
是否通过契约、注入与配置保持实现可替换。
是否对高风险架构调整显式做了影响分析与升级判断。
若涉及职责拆分，是否已联动 single-responsibility 做边界收敛。
反模式
为了快速交付直接跨层调用底层实现。
在基础设施层写入业务规则。
直接改接口签名，却不给兼容策略。
业务代码长期硬绑定具体实现或静态单例。
明明在做架构调整，却不说明影响范围和数据流变化。
参考资料
references/layering-and-dependencies.md - 分层与依赖方向基线
references/change-impact-analysis.md - 架构变更影响面分析模板
references/interface-di-and-pluggability.md - 契约、依赖注入与可插拔设计
references/project-initial-analysis.md - 项目初始化分析清单与评估维度
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