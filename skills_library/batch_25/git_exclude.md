---
title: git-exclude
url: https://skills.sh/snailuu/skill/git-exclude
---

# git-exclude

skills/snailuu/skill/git-exclude
git-exclude
Installation
$ npx skills add https://github.com/snailuu/skill --skill git-exclude
SKILL.md
Git 本地忽略技能
功能说明

将文件/文件夹添加到 .git/info/exclude，实现本地忽略而不影响 .gitignore。

.gitignore：提交到仓库，所有协作者共享
.git/info/exclude：仅本地生效，不会被提交
执行步骤
1. 检查 Git 仓库状态
git rev-parse --git-dir 2>/dev/null

成功 → 继续
失败 → 使用 AskUserQuestion 询问是否 git init
2. 解析忽略模式

支持的输入格式：单个文件、多个文件、文件夹（temp/）、通配符（*.log）、相对路径。

规范化处理：

去除路径开头的 ./
文件夹路径确保以 / 结尾
3. 检查并添加规则
# 检查文件是否存在
test -f .git/info/exclude && echo "exists" || echo "not exists"

# 幂等添加：检查重复后再追加
if ! grep -Fxq "pattern" .git/info/exclude 2>/dev/null; then
  echo "" >> .git/info/exclude
  echo "# Added by Claude Code on $(date '+%Y-%m-%d %H:%M:%S')" >> .git/info/exclude
  echo "pattern" >> .git/info/exclude
fi


已存在的规则提示用户，不重复添加。

4. 验证规则
git check-ignore -v file.txt

5. 处理已跟踪文件
git ls-files file.txt


如果文件已被跟踪，使用 AskUserQuestion 询问是否停止跟踪（git rm --cached）。停止跟踪后下次提交时该文件会从仓库中删除（本地文件保留）。

输出格式
成功添加：输出已添加的规则列表和验证结果
规则已存在：提示无需重复添加
已跟踪文件：警告并提供停止跟踪选项

详细输出示例、故障排查和命令参考见 references/guide.md。

Weekly Installs
9
Repository
snailuu/skill
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass