---
title: sdd-slim-review
url: https://skills.sh/gracdjd/skills/sdd-slim-review
---

# sdd-slim-review

skills/gracdjd/skills/sdd-slim-review
sdd-slim-review
Installation
$ npx skills add https://github.com/gracdjd/skills --skill sdd-slim-review
SKILL.md
SDD Slim Review

先做 review，再生成测试，再直接 repair actionable findings。

路由
读取 review.md
读取 harness.md
review subagent 下发参考 prompts/subagent-review-prompt.md
test generation subagent 下发参考 prompts/subagent-test-generation-prompt.md
repair subagent 下发参考 prompts/subagent-repair-prompt.md
final harness subagent 下发参考 prompts/subagent-verification-harness-prompt.md
使用 templates/review-findings.md 记录审查结论、生成测试与验证报告
输出问题时参考 prompts/finding-output.md
示例见 examples/review-findings-example.md
独立性规则
本 skill 只能由用户手动调用
review、test generation、repair 与 final verification harness 都必须由 subagent 驱动；主 agent 只负责切分包边界、审核结果、回写 worklog.md、同步 spec.md 状态、决定完成状态
默认串行：review 包与 repair 包都必须逐个顺序处理
test generation 默认也串行；只有在多个测试包明确互不重叠时，才允许与其他 review 包同轮并行
如果用户消息中带有 --mutiAgent，或明确表达要并行开启多个 agent / 多个 subagent，主 agent 必须自行判断是否可安全并行；可并行就直接进入 multiAgent，不可并行就退回串行并记录原因
multiAgent 模式只允许并行处理彼此独立的 review 包、test generation 包或 repair 包；worklog.md 写回、最终 findings 裁定、Fix status 更新与 harness report 聚合仍必须由主 agent 串行收口
如果目标涉及 web / browser UI，必须先启用 Playwright MCP 浏览器工具链并至少完成一轮自动化验证；如果当前环境无法使用该工具链，且 spec / 项目基线也未显式允许仅靠项目命令兜底，必须记录 blocker 或验证缺口，不能宣称 web review 或 e2e harness 完整
review 阶段负责把 plan.md 里的 Test Design Handoff 落成最终测试文件；plan 只定义测试设计，不落最终测试代码
web 目标的 TG* e2e 产物默认优先落成仓库内的 Playwright 测试文件，供后续 CI / 项目级回归复用；Playwright MCP 自动化路径本身不是持久化测试文件
final harness 必须输出 unit coverage 与 e2e success rate；未执行的一侧必须标明 skipped / blocked 与原因
final harness 必须显式报告 .sdd-slim/_project/test.md 中项目级回归基线的执行结果
标准 review 阶段禁止用 askquestion 打断用户；范围不清、修复标准含糊或目标有多解时，必须自主做最保守判断并记录 assumption / deferred / blocker
不自动进入任何其他 skill
review 完成后必须同步完成本轮 actionable findings 的直接修复，并在收尾前执行 final verification harness；若 required harness 无法完成，必须明确记录 blocker / deferred 原因，然后停止
只要仍存在未处理完成、未被 blocker 阻断的 review 包、TG* 包、R* 包或 harness 回流问题，当前 review 调用就必须继续；不得用“下一波 review / repair 建议”替代继续执行
不得在仍有 runnable review 工作包时输出“下一波建议”“推荐后续顺序”“如果你不改方向我下一条继续”之类的半途交棒收尾；这类输出属于 workflow bug
Weekly Installs
12
Repository
gracdjd/skills
First Seen
Apr 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass