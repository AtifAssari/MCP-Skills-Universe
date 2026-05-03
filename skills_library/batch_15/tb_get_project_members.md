---
title: tb-get-project-members
url: https://skills.sh/kaelzhang321/teambition-agent-toolkit/tb-get-project-members
---

# tb-get-project-members

skills/kaelzhang321/teambition-agent-toolkit/tb-get-project-members
tb-get-project-members
Installation
$ npx skills add https://github.com/kaelzhang321/teambition-agent-toolkit --skill tb-get-project-members
SKILL.md
查询项目成员

缓存优先：从 .teambition.cache.md 读取。如果缓存不存在，提示先执行 /tb-sync。

步骤
读取 .teambition.md 常用项目，用 AskUserQuestion（单选）选择项目
读取 .teambition.cache.md 中该项目的"### 成员"表格
以表格展示：用户 ID、角色
Weekly Installs
10
Repository
kaelzhang321/te…-toolkit
First Seen
Apr 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass