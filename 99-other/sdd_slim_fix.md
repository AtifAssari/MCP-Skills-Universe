---
title: sdd-slim-fix
url: https://skills.sh/gracdjd/skills/sdd-slim-fix
---

# sdd-slim-fix

skills/gracdjd/skills/sdd-slim-fix
sdd-slim-fix
Installation
$ npx skills add https://github.com/gracdjd/skills --skill sdd-slim-fix
SKILL.md
SDD Slim Fix

只做 targeted fix。

路由
读取 fix.md
没有 review findings 时，使用 prompts/fix-target-question.md 询问用户本轮要修什么
使用 templates/fix-note.md 记录修复结果
如果信息不足，使用 templates/blocker-note.md 记录 blocker
示例见 examples/example-fix-note.md
独立性规则
本 skill 只能由用户手动调用
默认消化当前 review 暴露出的所有 actionable findings
如果 review 没有暴露任何 actionable findings，必须用 askquestion 让用户指定修复目标
如有必要，可以用 askquestion 澄清单个 finding 的成功标准或边界
不自动触发 sdd-slim-plan
不自动触发 sdd-slim-review
不自动进入任何其他 skill
完成后不主动推荐进入其他 skill
Weekly Installs
9
Repository
gracdjd/skills
First Seen
Apr 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass