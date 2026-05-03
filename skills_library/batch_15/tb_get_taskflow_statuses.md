---
title: tb-get-taskflow-statuses
url: https://skills.sh/kaelzhang321/teambition-agent-toolkit/tb-get-taskflow-statuses
---

# tb-get-taskflow-statuses

skills/kaelzhang321/teambition-agent-toolkit/tb-get-taskflow-statuses
tb-get-taskflow-statuses
Installation
$ npx skills add https://github.com/kaelzhang321/teambition-agent-toolkit --skill tb-get-taskflow-statuses
SKILL.md
查询工作流状态

缓存优先：从 .teambition.cache.md 读取。如果缓存不存在，提示先执行 /tb-sync。

步骤
读取 .teambition.md 常用项目，用 AskUserQuestion（单选）选择项目
读取 .teambition.cache.md 中该项目的"### 工作流状态"表格
以表格展示：状态名称、状态 ID、类型、工作流 ID
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