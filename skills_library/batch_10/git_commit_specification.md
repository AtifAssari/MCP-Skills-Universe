---
title: git-commit-specification
url: https://skills.sh/tencentblueking/bk-ci/git-commit-specification
---

# git-commit-specification

skills/tencentblueking/bk-ci/git-commit-specification
git-commit-specification
Installation
$ npx skills add https://github.com/tencentblueking/bk-ci --skill git-commit-specification
SKILL.md
Git 提交规范
Quick Reference
格式：标记: 提交描述 #issue编号
示例：feat: 添加流水线模板功能 #1234
分支：feature/xxx | bugfix/xxx | hotfix/xxx

标记类型
标记	说明	示例
feat	新功能	feat: 添加流水线模板支持 #1234
fix	Bug 修复	fix: 修复构建日志丢失 #5678
refactor	重构	refactor: 优化查询性能
perf	性能优化	perf: 减少数据库查询
test	测试	test: 添加单元测试
docs	文档	docs: 更新 API 文档
chore	构建/工具	chore: 更新 Gradle 配置
del	破坏性删除	del: 移除废弃 API（需特别批准）
When to Use
提交代码
创建分支
准备 PR
编写 commit message
提交格式
# 标准格式
feat: 添加流水线模板功能 #1234

# 带范围
feat(process): 添加流水线模板功能 #1234

分支命名
feature/pipeline-template-support   # 功能分支
bugfix/build-log-missing            # Bug 修复分支
hotfix/critical-security-issue      # 热修复分支

PR 提交前准备
# 使用 rebase 精简 commit
git rebase -i HEAD~5

# 同步上游代码
git fetch upstream
git rebase upstream/develop

Checklist

提交代码前确认：

 commit message 符合格式规范
 关联了 Issue 编号
 使用 rebase 精简了 commit
 没有包含敏感信息
 代码通过本地测试
Weekly Installs
63
Repository
tencentblueking/bk-ci
GitHub Stars
2.5K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass