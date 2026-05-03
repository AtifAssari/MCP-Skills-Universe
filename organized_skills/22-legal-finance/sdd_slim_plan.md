---
rating: ⭐⭐
title: sdd-slim-plan
url: https://skills.sh/gracdjd/skills/sdd-slim-plan
---

# sdd-slim-plan

skills/gracdjd/skills/sdd-slim-plan
sdd-slim-plan
Installation
$ npx skills add https://github.com/gracdjd/skills --skill sdd-slim-plan
SKILL.md
SDD Slim Plan

只做 planning / specify。

路由
读取 specify.md
主代理按 prompts/requirement-archive-prompt.md 直接完成需求获取 / 归档（如需抓取外部链接正文，直接调用对应 MCP / 工具；wiki 链接使用 mcp__hotel-tools__matrix-wiki-get）
使用 templates/spec.md、templates/plan.md、templates/worklog.md 作为 feature-level 模板
如果 .sdd-slim/_project/test.md 不存在，使用 templates/project-test.md 创建项目级测试基线文件
对单个 Q* 的澄清提问参考 prompts/clarification-question.md
对每个 P* 的用户确认提问参考 prompts/point-confirmation-question.md
multiAgent 开关确认提问参考 prompts/multi-agent-confirmation-question.md
对每个 P* 使用 prompts/subagent-task-prompt.md 驱动代码研究 subagent
输出待补充信息时参考 prompts/pending-input-output.md
输出任务研究摘要时参考 prompts/research-summary-output.md
示例见 examples/example.spec.md、examples/example.plan.md、examples/example.worklog.md
所有 P*/Q* 处理完成后的整体连贯性分析参考 prompts/coherence-check-prompt.md
独立性规则
本 skill 只负责生成 / 更新 planning artifacts：feature folder 下的 requirement.md、spec.md、plan.md、worklog.md，以及项目级 .sdd-slim/_project/test.md
不写任何产品代码
不得先输出“请提供需求来源 / 请选择需求类型 / 您希望规划哪个功能”之类的通用收集问题
需求获取必须先由主代理直接完成，并先落盘到 feature folder 下的 requirement.md
如果当前消息里已有链接，直接抓取；如果没有链接但有需求描述，直接归档并继续 planning
requirement 归档阶段必须先判定需求正文是否存在（available | partial | missing）；只有元信息不算完整需求
requirement 内容一旦整理完成，主代理必须立即写入 requirement archive；不得在落盘前插入无关等待、额外探索或长时间停顿
如果用户输入里有重复链接、重复粘贴段落或“链接 + 同内容补充”，必须先去重再归档
必须把 feature artifacts 放进 .sdd-slim/<YYYY.MM.DD>.<feature-name>/，避免所有需求产物平铺在 .sdd-slim/ 根目录
规划阶段必须确保项目级 .sdd-slim/_project/test.md 存在；若不存在，本轮创建 skeleton，供后续每个需求的 final verification harness 复用
plan 阶段必须把 feature-level Verification Strategy 与 Test Design Handoff 写清；这些内容供 review 阶段生成最终 unit / e2e 测试用例使用，但 plan 本身不生成测试代码
planning 阶段写入 worklog.md 的每个 T* 默认都要能在 implement 阶段被单独派发给一个 subagent；不得生成需要 implement 主 agent 二次拆包的 jumbo T*
每个 T* 至少要满足：单一主目标、最小必要文件范围、单一主验证焦点、明确 Dependencies
如果一个候选 T* 同时覆盖多个用户可感知行为、多个关键文件族或多条独立验证路径，必须在 plan 阶段继续拆分
如果存在阻塞 planning 的 follow-up，主代理必须在写完对应 planning 文档后立即通过 askquestion 发出第一个阻塞问题，然后停止等待用户回答
requirement 归档由主代理直接执行；如需抓取链接或本地文档正文，由主代理直接调用对应 MCP / 工具
每个 P* 在代码研究完成后都必须通过 askquestion 做一次用户确认，不得因需求简单或看似明确而跳过
额外的 Q* 也必须通过 askquestion 一次只问一个问题
每个 P* 的代码库研究必须由 subagent 完成；主代理不得自己直接用普通读文件/搜索结果替代这一步
plan 阶段所有与代码库有关的 explore / research / HOW 生成 / 入口定位 / 可复用模式识别 / 风险定位 / 验证路径识别 任务，都必须交给 subagent；不只限于 P*
主代理在 plan 阶段只负责 requirement 归档、文档写回、提问编排、以及对 subagent 返回结果做审查；不得亲自承担代码库探索工作
默认使用单 subagent 串行探索；若检测到用户传入 --mutiAgent 或明确表示要开启多个 subagent，主代理必须先通过 askquestion 做一次单点确认；只有收到明确同意后，才能进入 multiAgent 并行探索模式
如果用户没有明确确认 multiAgent，或回答否定 / 含糊，则继续保持串行 subagent 模式
multiAgent 模式只放开“代码库探索 / 问题研究”的并行度；文档写回、P* 用户确认、Q* 澄清、最终任务化与 ready 判定仍必须由主代理串行收口
如果某个 P* 还没有对应的 subagent 研究结果，就不得写入该 P* 的 Research Findings、不得生成该 P* 的 T*、不得声称 planning 完成
每个 P* 必须保留可审计的 subagent 产物痕迹：至少要能在 plan.md 中看到与该 P* 对应的代码依据、HOW、风险和验证建议
subagent 返回的 Candidate tasks 必须面向 implement-ready T* 包；主代理若发现粒度过大、依赖不清或仍需要 implement 再拆，必须重做拆分后再写入 worklog.md
如果主代理在 planning 中发现自己已经绕过了 subagent 或跳过了 P* 确认，必须立即停止后续 planning，补做缺失步骤，而不是继续推进到下一个 P*
完成后不主动询问是否进入 sdd-slim-implement
不触发 sdd-slim-review
其他 skill 只能由用户手动调用
Subagent 调度规则（CRITICAL）
默认模式是串行：每个 P* 必须逐个顺序处理
只有在满足以下全部条件时，才允许切换到 multiAgent 并行探索模式：
用户消息中显式包含 --mutiAgent，或明确要求开启多个 subagent / 多个 agent 并行探索
主代理已经通过 askquestion 单独询问“是否确认开启多个 agent 并行完成 plan 阶段探索”
用户给出明确肯定答复
如果缺少上述任一条件，就必须保持串行模式；不得因为用户“可能想快一点”而自行并发
multiAgent 模式下，只允许并行执行彼此独立的代码库探索或问题研究；不得并行执行文档写回、P* 用户确认、Q* 澄清、最终 coherence 判定
即使在 multiAgent 模式下，每个 subagent 也只负责一个 P* 或一个明确的问题研究包；主代理负责归并结果、去重冲突、判断 HOW 是否成立
处理顺序：
串行模式：subagent 探索 P* → 确认 HOW 正确性 → 写入 plan.md / spec.md / worklog.md → askquestion 确认当前 P* → 如仍有额外阻塞再 askquestion → 处理下一个 P*
multiAgent 模式：主代理划分独立探索包 → 多个 subagent 并行探索 → 主代理统一审核与去重 → 按 P* 顺序写入文档 → 按 P* 顺序 askquestion 确认 → 任务化
subagent 负责探索代码库并给出 grounded 的 HOW 建议；主代理在 subagent 返回后，先判断 HOW 是否正确，再决定是否写入文档
如果 HOW 不正确或不充分，主代理必须重新调用 subagent 对该 P* 再次探索，直到 HOW 足够正确
在所有 P* 和 Q* 都处理完成后，必须执行一次整体连贯性分析，检查所有任务是否能串起来、是否有漏洞
如果连贯性分析发现漏洞，必须通过 askquestion 向用户确认补充方案
如果任一 P* 缺少 subagent 研究、缺少用户确认、或 HOW 仍未经主代理审查确认，就禁止把 spec 状态标为 ready
如果 plan 过程中出现任何新的探索需求（例如为回答 Q*、修正 HOW、补做 coherence gap、核实依赖链），也必须重新调用 subagent，而不是由主代理直接下场搜索代码
Weekly Installs
14
Repository
gracdjd/skills
First Seen
Apr 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn