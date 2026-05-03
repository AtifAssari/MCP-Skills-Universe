---
rating: ⭐⭐
title: heroagent
url: https://skills.sh/xiaozuoyou/heroagent/heroagent
---

# heroagent

skills/xiaozuoyou/heroagent/heroagent
heroagent
Installation
$ npx skills add https://github.com/xiaozuoyou/heroagent --skill heroagent
SKILL.md
HeroAgent
适用场景

当用户要处理以下问题时，使用 heroagent：

把模糊意图收敛为明确目标
把目标拆成阶段计划和执行任务
在多轮推进中维护当前状态、验收结论和下一步
复盘问题，并把稳定经验沉淀到知识库或流程标准
维护 .heroagent/wiki/ 项目知识库，并在后续动作中优先消费它

若用户只是做一次性代码修改、排错或实现功能，且不涉及目标推进或知识沉淀，不要强行使用 heroagent。

核心模型
初始化与知识入口：init、wiki
目标推进主流程：want -> plan -> todo -> achieve | abandon
状态观察动作：focus
问题复盘入口：reflect
内部沉淀方法：
realize：reflect 结论经用户确认后，把稳定经验写入 .heroagent/principles/
synthesize：在 wiki 内压缩长记录、提炼一句话结论、合并重复知识
forget：在 wiki 内淘汰旧知识、旧需求结论和失效约束
master：沉淀 HeroAgent 或项目级执行标准，不作为常规用户指令

优先保持单一主目标。若用户同时提出多个目标，先区分主目标、并行目标、暂存目标，再继续推进。

状态机骨架

HeroAgent 不是动作词典，而是一套轻量状态机。进入任何动作前，先重建以下最小状态：

CURRENT_OBJECT：goal | plan | task | issue | wiki
CURRENT_STAGE：clarify | planning | executing | reviewing | archiving
WORKFLOW_MODE：interactive | continuous
COMPLEXITY_LEVEL：light | standard | deep
NEXT_ACTION：下一步最合理动作
WIKI_SYNC_STATE：none | pending | draft | synced

若信息不足，至少重建：

当前主目标
当前阶段
下一步动作
已知阻塞

若用户没有提供历史状态，先根据对话和已有 .heroagent/ 材料重建，不要假装存在外部记忆。

复杂度分流

先判断复杂度，再决定流程强度。默认分为三档：

等级	适用情况	默认流程强度
light	目标已基本清楚，只需轻澄清、轻规划或快速看态势	不强制展开完整闭环，优先给最小可执行结果
standard	需要明确目标、拆阶段、列任务并推进执行	进入标准推进闭环：want -> plan -> todo -> achieve | abandon
deep	多目标冲突、长期推进、明显阻塞、需要复盘或知识治理	强制补状态、补风险、补验收口径，必要时转入 reflect 或 wiki

复杂度判断优先看四件事：

目标是否清楚
范围是否稳定
是否涉及长期状态维护
是否需要知识沉淀或复盘

不要因为信息很多就自动判成 deep；只有在推进成本和治理成本明显升高时，才升级流程强度。

动作入口

默认推荐用 ~动作 触发，对人和对 AI 都更稳定。

指令	目的	关键约束
~init	初始化 .heroagent/ 工作区	先建工作区，再进入后续动作
~wiki	维护并消费 .heroagent/wiki/	先消费现有 wiki，再决定是否补写
~want	定义目标	先评分，未达标时只做澄清
~plan	制定路径	输出阶段、风险、完成标志
~todo	形成执行单元	默认按优先级连续执行，不逐项确认
~focus	查看当前态势	这是观察动作，不是主流程阶段
~achieve	验证目标达成	不把任务完成等同于目标达成
~abandon	停止目标并收口	明确停损、保留资产与重启条件
~reflect	复盘问题	先取证，再判断根因

规则：

用户显式输入 ~动作 时，直接命中对应动作
显式指令优先级高于自然语言路由
未使用显式指令时，再按自然语言判断当前最阻塞的一步
若一次请求同时涉及推进、复盘和知识维护，先处理推进闭环中的阻塞动作，再处理 reflect 或 wiki
动作入口与出口
want
入口条件：用户在表达愿望、方向、想法，但还没有形成可验收目标
默认产物：目标卡或目标澄清结果
禁止行为：在评分未达标前直接展开完整计划
出口条件：
达标后进入 plan
用户选择继续补充需求时，留在 want
用户明确暂缓时，进入暂停状态
plan
入口条件：目标已明确，但阶段路径、关键里程碑或主要风险还不清楚
默认产物：阶段计划、里程碑、风险与完成标志
禁止行为：把阶段规划直接降格成零散任务清单
出口条件：
路径清楚后进入 todo
若目标边界重新变动，回到 want
若用户只要里程碑骨架，可停在 plan
todo
入口条件：已有清晰目标或计划，需要形成执行单元
默认产物：任务清单、依赖关系、优先级和完成定义
禁止行为：逐项机械确认所有低风险任务
出口条件：
默认连续执行全部任务
全部完成后自动进入“已完成，待验收”，下一步转入 achieve
若出现关键取舍或阻塞，暂停并等待确认
focus
入口条件：用户在问当前状态、优先级、阻塞或下一步
默认产物：current-focus.md 或一段当前态势总结
禁止行为：把观察动作扩展成新的规划动作
出口条件：
给出当前最值得关注的信息后结束
若用户顺势要求验收，转入 achieve
若用户顺势要求重新规划，转入 plan 或 todo
achieve
入口条件：任务已完成，或用户要求判断目标是否真正闭环
默认产物：验收结论、证据、缺口和是否归档建议
禁止行为：在没有证据时直接宣告达成
出口条件：
已达成且适合收口时进入归档
部分达成时回到 todo
目标已失去继续价值时转入 abandon
abandon
入口条件：用户明确停止推进、暂缓或放弃目标
默认产物：停损结论、沉没成本、可保留资产、重启条件
禁止行为：把明确放弃包装成继续规划
出口条件：
明确收口后结束
若用户改变决定，可回到 want、plan 或 todo
reflect
入口条件：用户要复盘原因、问题、失误、延期、偏差
默认产物：事实证据、判断、根因、漏判点、提前信号
禁止行为：在证据不足时把猜测当根因
出口条件：
结论经确认后，可内部触发 realize
若需要补充结构背景，可并行消费 wiki
若问题尚未解决，先回到推进闭环，不急于沉淀原则
wiki
入口条件：用户要维护知识库、消费项目知识、压缩长记录或清理旧知识
默认产物：更新后的 wiki、待补写草稿或维护建议
禁止行为：把草稿当正式事实直接输出
出口条件：
知识维护完成后结束
若同步后发现还需继续推进目标，再回到推进闭环
若沉淀结论升级为长期规则，可内部触发 master
核心执行规则
先收敛，再展开

若关键信息缺失，先用最少的问题补齐；若可以安全假设，则明确假设后继续。

区分事实与判断

输出时区分三类信息：

事实：用户已确认或已观察到的信息
判断：基于事实得出的分析
待确认：影响决策但尚未确认的信息
优先产出可执行结果

每个动作都要优先产出可直接使用的结果，例如：

清晰目标
可执行计划
可勾选任务
当前态势
验收结论
可复用原则或流程
todo 默认执行策略
进入 todo 后，默认按优先级一次性连续执行全部任务，不逐项向用户确认
只有遇到关键取舍、高风险变更、权限受限、外部依赖阻塞或需求边界变动时，才暂停并请求确认
若任务之间存在明确依赖，先按依赖顺序执行，再继续后续任务
若执行中出现新信息，只更新当前状态和剩余任务，不回退成逐项确认模式
当 todo 全部执行完成后，自动进入“已完成，待验收”的内部状态，下一步默认转入 achieve
want 评分门槛
先按 references/requirement-scoring.md 做 10 分制评分
阈值是 8
评分 < 8 时，只做 目标澄清，不要直接进入 plan
达到可进入下一步时，必须让用户在 继续 ~plan、继续补充需求、暂不处理 中选择
应同步把状态写入 progress/workflow-state.json
wiki 执行门槛
命中知识维护或知识消费意图时，优先执行 wiki
若 .heroagent/wiki/ 存在，在 want、plan、todo、focus、reflect 中优先消费其内容
先消费现有 wiki，再决定是否补写、生成草稿、合并草稿或切换策略
若用户要压缩长记录、提炼一句话经验或清理旧知识，也归到 wiki，在内部选择 synthesize、forget
若本轮只生成草稿，必须明确标注“未直接写入正式 wiki”
默认只在执行任务后出现代码、接口、数据或架构变化时，自动做 wiki 轻判断
want、plan、todo 默认不自动触发 wiki 轻判断；它们主要更新目标、计划、任务和当前状态
只有在需求边界、项目事实或技术约束被显式改写时，want、plan、todo 才需要额外触发 wiki 轻判断
achieve、显式 wiki 请求前，应优先检查是否存在待同步的 wiki 变化
wiki 轻判断属于 skill 内部机制，不要求用户手动调用脚本
打破静默规则

默认连续推进，只有在以下情况才停下来确认：

关键取舍会改变目标边界
需要做高风险落盘或覆盖性修改
当前目标与历史状态明显冲突
外部依赖阻塞导致无法继续推进
验收标准无法判断

若不满足上述条件，不要为了“显得谨慎”而频繁打断执行。

reflect 与沉淀联动
reflect 是唯一公开的问题复盘入口
当问题已解决且复盘结论经用户确认后，才内部触发 realize
realize 只负责把稳定经验沉淀到 .heroagent/principles/，不单独作为公开指令
若复盘结论进一步上升为长期执行约束，再视情况内部触发 master
输出约定

统一采用固定槽位输出，不依赖动作临场发挥。所有正式输出都应优先回答：

当前结论
当前依据
产物或状态更新
下一步

若需要用户决策，再补：

需要确认

使用 heroagent 时，回复首行应使用单行状态头，例如：

✅ HeroAgent · 计划制定
❓ HeroAgent · 需要确认
⚠️ HeroAgent · 当前态势
💡 HeroAgent · 咨询问答


统一要求：

先给结论，再给依据
缺失信息明确标注，不伪造内容
需要用户决策时，优先给 2 到 3 个低成本选项，并包含 暂不处理
最后给 下一步
若需要落盘，优先与 assets/templates/ 保持一致

详细字段与动作契约，按需读取 references/output-contracts.md。

按需加载

不要一次性全量加载资料。按场景读取：

路由与状态： references/command-routing.md references/state-management.md references/action-trigger-matrix.md references/complexity-routing.md
提问与输出： references/prompt-patterns.md references/output-contracts.md references/action-examples.md
落盘与归档： references/file-conventions.md references/init-conventions.md references/bootstrap-conventions.md references/focus-update-conventions.md references/archive-conventions.md
wiki： references/wiki-conventions.md references/wiki-context-consumption.md references/wiki-sync-rules.md
复盘： references/reflect-context-rules.md

如需直接落盘，优先复用：

assets/templates/goal-card.md
assets/templates/milestone-plan.md
assets/templates/todo-list.md
assets/templates/progress-snapshot.md
assets/templates/retrospective.md
assets/templates/principle-card.md
assets/templates/process-card.md
优先脚本

只在需要实际落盘、批处理或巡检时调用脚本。优先使用：

初始化与状态：scripts/init_heroagent.py、scripts/bootstrap_first_goal.py、scripts/update_current_focus.py、scripts/archive_goal.py、scripts/doctor_heroagent.py
want 状态：scripts/update_want_state.py
wiki 维护：scripts/update_wiki_context.py、scripts/suggest_wiki_updates.py、scripts/refresh_wiki_registry.py
wiki 草稿闭环：scripts/sync_wiki_from_changes.py、scripts/apply_wiki_draft.py、scripts/reconcile_wiki_state.py、scripts/promote_wiki_maintenance.py
wiki 增强：scripts/compact_wiki_memory.py、scripts/score_wiki_signals.py、scripts/assemble_wiki_context.py、scripts/extract_wiki_facts.py、scripts/run_wiki_strategy.py

内部状态机制：

wiki 轻判断由 skill 自动触发，可复用 scripts/update_wiki_signal_state.py，但不作为面向用户的公开命令
响应风格

保持语言简洁、明确、可执行。优先：

先给结论，再给依据
少讲术语，多讲动作
少给大而空的框架，多给当前可用结果
对未确认事项直接标注，不自行脑补

除非用户明确要求，不要引入复杂理论命名或冗长方法论。

Weekly Installs
19
Repository
xiaozuoyou/heroagent
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass