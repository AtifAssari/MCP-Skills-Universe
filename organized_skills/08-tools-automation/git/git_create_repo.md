---
rating: ⭐⭐
title: git-create-repo
url: https://skills.sh/zc277584121/mygitplugin/git-create-repo
---

# git-create-repo

skills/zc277584121/mygitplugin/git-create-repo
git-create-repo
Installation
$ npx skills add https://github.com/zc277584121/mygitplugin --skill git-create-repo
SKILL.md
Git Create Repo

在 GitHub 上创建新的仓库并 clone 到本地。

触发条件

当用户要求创建一个新的 GitHub 仓库时使用此 skill。

执行步骤

创建仓库：

gh repo create <repo-name> --public --add-readme

默认创建公开仓库（--public）。
如果用户明确要求私有仓库，使用 --private 替代。
默认添加 README 文件。

Clone 仓库：

gh repo clone zc277584121/<repo-name>


确认结果：进入项目目录，向用户报告仓库创建成功。

注意事项
GitHub 账号为 zc277584121。
如果用户没有指定公开或私有，默认使用公开（--public）。
如果用户提供了描述，使用 --description 参数。
Weekly Installs
53
Repository
zc277584121/mygitplugin
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass