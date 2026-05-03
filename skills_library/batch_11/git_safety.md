---
title: git-safety
url: https://skills.sh/ab300819/skills/git-safety
---

# git-safety

skills/ab300819/skills/git-safety
git-safety
Installation
$ npx skills add https://github.com/ab300819/skills --skill git-safety
SKILL.md
Git Safety & Standards

该 Skill 旨在确保在 Git 仓库中进行文件操作时的安全性和历史完整性。

核心准则
1. 移动与重命名 (Move & Rename)
禁止直接使用 mv 命令操作受 Git 跟踪的文件。
强制使用 git mv <old_path> <new_path>。
理由：确保 Git 自动跟踪文件重构，保留文件的 Git History，避免识别为“删除 + 新增”。
2. 删除 (Delete)
禁止直接使用 rm 或 rm -rf 操作受 Git 跟踪的文件。
强制使用 git rm <path> 或 git rm -r <path>。
理由：直接从工作区和索引中同步移除，避免残留未跟踪的删除变更。
3. 操作前自检流程

当 Agent 准备操作文件时，应遵循以下逻辑：

检查状态：执行 git ls-files <path>。
判断：
如果有输出（说明文件受控）→ 使用 git mv / git rm。
如果无输出（说明是未跟踪文件）→ 使用普通 mv / rm。
适用场景
重构代码导致的文件目录结构调整。
删除过时的文档或代码文件。
项目清理。
约束
严禁在未确认文件状态的情况下盲目使用普通文件管理命令。
在执行大规模移动操作前，建议先执行 git status 确保工作区是干净的。
Weekly Installs
25
Repository
ab300819/skills
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass