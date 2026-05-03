---
title: code-review
url: https://skills.sh/rtgs2017/nagaagent/code-review
---

# code-review

skills/rtgs2017/nagaagent/code-review
code-review
Installation
$ npx skills add https://github.com/rtgs2017/nagaagent --skill code-review
SKILL.md
代码审查技能

本技能提供专业的代码审查能力，帮助发现潜在问题并提供改进建议。

审查维度
1. 代码质量
可读性: 命名规范、注释完整性、代码结构
可维护性: 模块化程度、耦合度、复杂度
一致性: 代码风格、设计模式使用
2. 潜在问题
Bug 风险: 空指针、边界条件、异常处理
安全漏洞: 注入攻击、敏感数据泄露、权限问题
性能问题: 算法复杂度、资源泄漏、并发问题
3. 最佳实践
设计原则: SOLID、DRY、KISS
语言特性: 现代语法、标准库使用
测试覆盖: 单元测试、边界测试
审查流程
概览分析: 理解代码目的和结构
逐行审查: 检查每个函数和模块
问题分类: 按严重程度分为 Critical/Major/Minor
建议生成: 提供具体的改进方案
输出格式
## 代码审查报告

### 概述
[代码的整体评价]

### 发现的问题

#### Critical（严重）
- [ ] 问题描述 (文件:行号)
  - 原因分析
  - 建议修复

#### Major（重要）
- [ ] ...

#### Minor（次要）
- [ ] ...

### 改进建议
1. 建议一
2. 建议二

### 总体评分: X/10

使用示例

用户: "帮我审查这段 Python 代码" → 加载此技能，按照上述流程进行代码审查

Weekly Installs
51
Repository
rtgs2017/nagaagent
GitHub Stars
1.5K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass