---
title: tb-get-projects
url: https://skills.sh/kaelzhang321/teambition-agent-toolkit/tb-get-projects
---

# tb-get-projects

skills/kaelzhang321/teambition-agent-toolkit/tb-get-projects
tb-get-projects
Installation
$ npx skills add https://github.com/kaelzhang321/teambition-agent-toolkit --skill tb-get-projects
SKILL.md
查询项目列表
执行步骤
读取 .teambition.md 中的常用项目列表（如果存在）
执行：
node ${CLAUDE_SKILL_DIR}/scripts/tb-api.mjs get-projects

解析 JSON，按 Active/Archived 分组展示
如果有常用项目配置，在表格中用标记区分常用项目（如在项目名前加 ★）
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