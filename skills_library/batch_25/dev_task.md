---
title: dev-task
url: https://skills.sh/bentz/dev-tasks-skills/dev-task
---

# dev-task

skills/bentz/dev-tasks-skills/dev-task
dev-task
Installation
$ npx skills add https://github.com/bentz/dev-tasks-skills --skill dev-task
SKILL.md
核心规则
永远使用中文进行对话。
用户明确提到 archive/归档 时，按 references/archiving.md 执行归档流程。
用户明确提到 经验/总结 时，按 references/experience.md 触发经验提取流程。
未指定任务 id 或任务文件路径时进入 Plan；指定后进入 Runner。
Plan 阶段未获用户确认前，不得落盘 tasks/。
破坏性命令必须先征询用户确认。
读取策略
仅按需读取 references，不全量加载。
Plan 阶段读取 references/plan-workflow.md。
Runner 阶段读取 references/task-workflow.md。
并发、归档、经验提取场景再读取对应文档。
默认读取 tasks/notes.md 获取经验。
模板仅从技能目录 references/templates/ 读取。
Weekly Installs
12
Repository
bentz/dev-tasks-skills
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass