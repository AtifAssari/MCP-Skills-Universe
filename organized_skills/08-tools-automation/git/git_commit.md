---
rating: ⭐⭐
title: git-commit
url: https://skills.sh/zrong/skills/git-commit
---

# git-commit

skills/zrong/skills/git-commit
git-commit
Installation
$ npx skills add https://github.com/zrong/skills --skill git-commit
SKILL.md
Git Commit with CalVer Tag

将当前仓库变更提交到 git，并按 CalVer 规则打 tag。

核心规则
先提交，再算版本，再打 tag。
版本号必须来自 calver.py，不得手动推断。
calver.py 是本 skill 自带脚本，不属于项目仓库。
**如果无法可靠定位 skill 的安装目录，就停止。**不要猜路径，也不要继续后续步骤。
只有用户明确要求时，才执行 git push 和 git push --tags。
脚本定位

calver.py 指的是 skill 自带脚本，而不是项目仓库里的同名文件。

执行时先定位 skill 的安装目录，再运行：

python3 <skill安装目录>/scripts/calver.py


如果环境不能提供安装目录，或目录无法可靠确定，立即停止并告知用户。

工作流程
查看仓库状态，确认当前变更范围。
只暂存并提交与当前任务相关的文件。
如用户提供额外的 commit message，则优先使用它。
运行 calver.py 获取下一个版本号。
用该版本号创建 tag。
如用户明确要求推送，再执行 git push 和 git push --tags。
CalVer 规则
格式：YY.WW.MICRO
YY：ISO 年份后两位
WW：ISO 周数
MICRO：全局递增序号，跨年不重置
常见错误
错误做法	正确做法
在项目仓库里找 scripts/calver.py	在 skill 安装目录里执行脚本
找不到路径就手动算版本号	直接停止
用户没明确要求就 push	先只提交和打 tag
把无关文件一起提交	只提交当前任务相关文件
Weekly Installs
19
Repository
zrong/skills
GitHub Stars
2
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass