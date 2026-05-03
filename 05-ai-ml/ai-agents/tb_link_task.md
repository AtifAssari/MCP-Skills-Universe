---
title: tb-link-task
url: https://skills.sh/kaelzhang321/teambition-agent-toolkit/tb-link-task
---

# tb-link-task

skills/kaelzhang321/teambition-agent-toolkit/tb-link-task
tb-link-task
Installation
$ npx skills add https://github.com/kaelzhang321/teambition-agent-toolkit --skill tb-link-task
SKILL.md
关联任务

重要：必须严格按照下面的步骤顺序执行，不得跳过任何步骤。

步骤 1（必须）：选择源任务所在项目

读取 .teambition.md 常用项目，用 AskUserQuestion（单选）让用户选择源任务所在的项目。

步骤 2（必须）：选择源任务

执行：

node ${CLAUDE_SKILL_DIR}/scripts/tb-api.mjs get-project-tasks --projectId <步骤1的项目ID>


用 AskUserQuestion（单选）让用户选择源任务。每个 option：

label: 任务标题
description: Task ID
步骤 3（必须）：选择目标任务所在项目

用 AskUserQuestion（单选）让用户选择目标任务所在的项目（从常用项目中选，可以和源项目相同）。

步骤 4（必须）：选择目标任务（多选）

执行：

node ${CLAUDE_SKILL_DIR}/scripts/tb-api.mjs get-project-tasks --projectId <步骤3的项目ID>


用 AskUserQuestion（multiSelect: true）让用户选择要关联的目标任务，支持选择多个。每个 option：

label: 任务标题
description: Task ID
步骤 5：逐个执行关联

对步骤 4 中选择的每个目标任务，分别执行：

node ${CLAUDE_SKILL_DIR}/scripts/tb-api.mjs link-task --taskId <源任务ID> --linkedTaskId <目标任务ID> --linkedProjectId <目标项目ID>

步骤 6：更新最近任务

用 Edit 工具将源任务和所有目标任务追加到 .teambition.md 最近任务记录。

步骤 7：展示结果

展示关联结果：源任务标题 → 每个目标任务标题，以及各自的 Task ID。

Weekly Installs
9
Repository
kaelzhang321/te…-toolkit
First Seen
Apr 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass