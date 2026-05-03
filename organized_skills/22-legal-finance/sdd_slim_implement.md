---
rating: ⭐⭐
title: sdd-slim-implement
url: https://skills.sh/gracdjd/skills/sdd-slim-implement
---

# sdd-slim-implement

skills/gracdjd/skills/sdd-slim-implement
sdd-slim-implement
Installation
$ npx skills add https://github.com/gracdjd/skills --skill sdd-slim-implement
SKILL.md
SDD Slim Implement

只做 implementation。

路由
读取 implement.md
实现前预处理参考 prompts/context-reset-preflight.md（内容为上下文压缩 preflight）
spec 选择提问参考 prompts/spec-selection-question.md
阻塞澄清提问参考 prompts/blocking-question.md
subagent 实现包下发参考 prompts/subagent-implementation-prompt.md
使用 templates/execution-note.md 记录执行结果
如果中途阻塞，使用 templates/blocker-note.md 回写 blocker
示例见 examples/example-execution-notes.md
独立性规则
本 skill 只能由用户手动调用
开始实现前，默认只执行一次 context compression preflight：优先且仅尝试 compact/compress
如果当前环境不支持 compact/compress，不得假设其存在，也不得主动改用 clear/reset 或 new session/fresh run
如果完成的是 compact/compress，必须明确说明这只是上下文压缩，不是 fresh context，也不等价于真正 clear
如果当前环境连 compact/compress 也不支持，必须明确说明“未进行上下文压缩”，然后重新读取 spec 与当前代码继续 implement
如有必要，可以用 askquestion 做阻塞澄清
实现必须把 spec 当作唯一执行边界：只实现已确认 T*，不得因为“顺手修一下”“先跑通主链路”而扩 scope
默认且强制采用 subagent-per-P：每个未完成 P* 实现包都必须先交给一个 subagent；主 agent 只负责选择当前 P* 包边界、下发约束、审核结果、决定是否接受
subagent 默认只应处理单个 P* 及其关联的多个 T*；不得同时承担多个未完成 P* 的跨点编排
主 agent 不得直接承担任何属于当前 P* 的产品代码实现；如果 subagent 结果不足，必须继续重派同一 P* 或记录 blocker，而不是主 agent 直接下场补实现
默认是单 agent 串行实现；如果用户消息中带有 --mutiAgent，或明确表达“开启多个 agent / 多个 subagent 并行实现”，则可直接切换到 multiAgent 模式，无需额外 askquestion 确认
multiAgent 模式只允许并行执行彼此独立的 P* 实现包；同一个 P* 内部仍由一个 subagent 负责，不得拆成多个 agent 并行改写同一实现包
若多个 P* 共享同一关键文件、迁移顺序、公共接口或验证环境，主 agent 必须判定其不独立并退回串行模式
主 agent 不得把 spec 状态管理、任务完成判定、deviation/blocker 认定完全外包给 subagent
每完成一个 P* 包中的任意 T*，都必须由主 agent 立即回写同一 spec 文件中的 Task Checklist 与 Execution Notes；不得拖到全部代码写完后再统一补记
只有当所有未完成 P* 都被重新计算为已完成、已部分完成但可接受，或因 blocker 停止时，implement 才允许结束；不得在仅完成部分 P* 后提前收尾
一旦发现实现已经偏离 spec、跳过回写、或在不确定的情况下继续编码，必须立即停止，先回写 deviation/blocker，再决定是否继续
如果某项工作尚未写回 spec，就不得宣称该 T* 已完成
如果验证尚未完成，就不得把该 T* 标为 [x]
不自动触发 sdd-slim-review
不自动触发 sdd-slim-fix
不自动进入任何其他 skill
完成后不主动推荐进入其他 skill
Weekly Installs
13
Repository
gracdjd/skills
First Seen
Apr 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass