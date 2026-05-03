---
title: sdd-slim-auto
url: https://skills.sh/gracdjd/skills/sdd-slim-auto
---

# sdd-slim-auto

skills/gracdjd/skills/sdd-slim-auto
sdd-slim-auto
Installation
$ npx skills add https://github.com/gracdjd/skills --skill sdd-slim-auto
SKILL.md
SDD Slim Auto

只做 orchestration，不改原 skill 定义。

路由
先读取 auto.md
把以下文档视为各阶段 canonical rules：
../sdd-slim-plan/specify.md
../sdd-slim-implement/implement.md
../sdd-slim-review/review.md
需要具体模板、提问格式或示例时，继续读取对应 skill 目录下的 prompts/、templates/、examples/
核心原则
sdd-slim-auto 是新的用户入口，不修改 sdd-slim-plan / sdd-slim-implement / sdd-slim-review
不直接“自动调用”其他三个主阶段 skill；而是在当前 skill 内按对应文档顺序执行同等阶段
用户显式触发 sdd-slim-auto，即表示已授权在当前需求闭环中继续执行 implement / review，无需再单独手动触发其他 skill
sdd-slim-plan 的 Q* 提问、P* 用户确认、默认串行 subagent 探索，以及在检测到 --mutiAgent 或用户明确要求后先经 askquestion 确认再切换为 multiAgent 并行探索的规则，必须原样保留
sdd-slim-implement 阶段中新增的 subagent-per-T 执行模型必须原样保留：每个未完成 T* 的实现与定向验证都先交给 subagent，P* 只作为来源点与聚合维度；默认串行；若用户要求并行，由主 agent 直接做独立性判断并自动决定是否开启 multiAgent
sdd-slim-review 阶段必须采用 subagent 驱动：先由 review subagent 产出 findings，再由 test-generation subagent 落地 unit / e2e tests，再由 repair subagent 直接修复 actionable findings；默认串行，若用户要求并行，由主 agent 直接做独立性判断并自动决定是否开启 multiAgent
sdd-slim-review 阶段中的 final verification harness 必须原样保留：web / browser UI 走 e2e，其他目标走 unit，并在 worklog.md 中回写统一测试报告，同时同步必要的 spec.md 高层状态
只有 plan 阶段的 askquestion 可以暂停 auto 流程；implement / review 阶段不得因提问而暂停
当前阶段合法完成且无用户阻塞后，才自动进入下一阶段
不为了自动化而弱化任何阶段的 hard gate、scope discipline 或 stop condition
在 implement / review 阶段，只要仍有 runnable 工作包，auto 就必须继续闭环；不得以“已完成当前一波，下一波建议如下”之类的半途交棒文案结束当前调用
如果用户在 auto 流程中途发来的是状态确认或事实查询，例如“现在是否完成”“是否已跑最终 e2e”“还差哪些任务”，主 agent 必须先给 grounded answer，再继续同一个 auto 闭环；除非用户明确要求“只回答 / 暂停 / 先别继续”
单次较大验证通过也只算阶段内 checkpoint，不算 auto 终态；只有完成最终 review、final verification harness 与统一报告后，auto 才能宣称整个需求完成
Weekly Installs
9
Repository
gracdjd/skills
First Seen
Apr 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass