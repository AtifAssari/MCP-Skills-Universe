---
rating: ⭐⭐
title: file-header-comments
url: https://skills.sh/qiao-925/qiao-skills/file-header-comments
---

# file-header-comments

skills/qiao-925/qiao-skills/file-header-comments
file-header-comments
Installation
$ npx skills add https://github.com/qiao-925/qiao-skills --skill file-header-comments
SKILL.md
代码文件顶部注释规范

所有代码文件必须在文件顶部包含功能描述注释。

⚠️ 核心强制要求
注释内容（按优先级）
核心功能概述（必需）：第一句话说明文件是干什么的
主要接口/功能（必需）：列出主要函数/类
快速开始示例（推荐）：最简单的使用示例
禁止事项
❌ 详细描述架构分层
❌ 重复代码中已明确的信息
❌ 冗长的执行流程描述
篇幅控制
单个文件注释 ≤ 30 行
AI Agent 行为要求
创建新文件时
必须自动添加符合规范的顶部注释
优先描述功能，少描述架构
修改现有文件时
缺少注释则添加
注释过于复杂则精简
确保注释与实际代码一致
参考资料
references/comment-templates.md - 各语言注释模板详细说明
references/best-practices.md - 注释最佳实践
Weekly Installs
17
Repository
qiao-925/qiao-skills
First Seen
Feb 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass