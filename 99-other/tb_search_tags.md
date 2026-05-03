---
title: tb-search-tags
url: https://skills.sh/kaelzhang321/teambition-agent-toolkit/tb-search-tags
---

# tb-search-tags

skills/kaelzhang321/teambition-agent-toolkit/tb-search-tags
tb-search-tags
Installation
$ npx skills add https://github.com/kaelzhang321/teambition-agent-toolkit --skill tb-search-tags
SKILL.md
搜索标签
执行步骤
用 AskUserQuestion（单选，2 个 option：查看全部 / 按关键词搜索）询问用户
如果选择"按关键词搜索"，在对话中问用户"请输入搜索关键词"，等用户回复
执行：
node ${CLAUDE_SKILL_DIR}/scripts/tb-api.mjs search-tags [--keyword <关键词>]

以表格展示：标签ID(id)、名称(name)、颜色(color)
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