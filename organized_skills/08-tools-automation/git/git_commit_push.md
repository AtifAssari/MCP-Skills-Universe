---
rating: ⭐⭐
title: git-commit-push
url: https://skills.sh/zc277584121/mygitplugin/git-commit-push
---

# git-commit-push

skills/zc277584121/mygitplugin/git-commit-push
git-commit-push
Installation
$ npx skills add https://github.com/zc277584121/mygitplugin --skill git-commit-push
SKILL.md
Git Commit & Push

提交改动并推送到 origin 远端，不创建 PR。

触发条件

当用户要求提交改动并 push（但不需要提 PR）时使用此 skill。

执行步骤

创建新分支：git checkout -b <branch-name>，分支名由用户指定或根据改动内容自动生成。如果用户希望直接在当前分支提交，则跳过此步。

Review 改动：先用 git status 和 git diff 自行检查所有改动，确保没有把临时文件、调试代码或不相关的文件混进来。

暂存文件：git add 相关改动文件。不要使用 git add -A 或 git add .，而是逐个添加相关文件。

提交改动：

git commit --signoff --author="Cheney Zhang <chen.zhang@zilliz.com>" -m "<commit message>"

commit message 用英文编写，简洁描述改动内容。
绝对不要在 commit message 中提及 AI、Claude、LLM 或任何自动生成相关的字样。

推送分支：git push origin <branch-name>。

注意事项
提交前检查是否有未暂存的改动需要处理。
所有 commit 都需要 --signoff，作者为 "Cheney Zhang chen.zhang@zilliz.com"。
commit message 中不能出现任何 AI 相关字样。
Weekly Installs
54
Repository
zc277584121/mygitplugin
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass