---
title: li-upgrade
url: https://skills.sh/jiangjiax/li-skills/li-upgrade
---

# li-upgrade

skills/jiangjiax/li-skills/li-upgrade
li-upgrade
Installation
$ npx skills add https://github.com/jiangjiax/li-skills --skill li-upgrade
SKILL.md
升级 li-skills

将你的 li-skills 升级到最新版本。

步骤
第一步：确认当前版本
cat ~/.claude/skills/li-writer/SKILL.md | head -3

第二步：执行升级
npx skills update


或重新安装最新版：

npx skills add jiangjiax/li-skills

第三步：重启 Claude Code 会话加载新版本
注意事项
升级会覆盖同名 skill 文件，不会删除其他 skill
如有自定义修改，建议先备份对应 SKILL.md
升级后重启 Claude Code 会话以加载新版本
获取帮助
GitHub: https://github.com/jiangjiax/li-skills
Issues: https://github.com/jiangjiax/li-skills/issues
Weekly Installs
18
Repository
jiangjiax/li-skills
GitHub Stars
29
First Seen
Mar 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn