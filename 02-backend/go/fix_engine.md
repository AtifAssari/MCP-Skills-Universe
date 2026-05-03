---
title: fix-engine
url: https://skills.sh/blueif16/amazing-claude-code-plugins/fix-engine
---

# fix-engine

skills/blueif16/amazing-claude-code-plugins/fix-engine
fix-engine
Installation
$ npx skills add https://github.com/blueif16/amazing-claude-code-plugins --skill fix-engine
SKILL.md
修复引擎

所有者: 仅子协调器

职责
读取 section_path 中的 mini-prd.md
将验收标准转换为 checklist.md（markdown 复选框格式）
编排：executor → validator → (失败则重试)
每次验证后更新 checklist.md 的复选框状态
更新 meta.yaml 中的进度摘要
跟踪尝试次数并累积失败上下文
超过最大重试次数时准备详细错误报告
检查清单创建

从 mini-prd.md 的验收标准生成 checklist.md（markdown 格式）：

## 认证模块检查清单

- [ ] 用户可以使用邮箱/密码注册
- [ ] 登录时签发 JWT 令牌
- [ ] 受保护路由拒绝无效令牌
- [ ] 刷新令牌轮换正常工作

**进度: 0/4**


每次 validator 返回结果后，更新对应的复选框：

通过的检查项：- [x]
失败的检查项：- [ ]

同时更新底部的进度摘要。

执行循环
attempt = 0
max_attempts = 3

while attempt < max_attempts:
    if attempt == 0:
        # 使用 executor agent 实现 .task/mini-prd.md
        call executor agent to implement .task/mini-prd.md
    else:
        call executor(task: "fix", failures: last_failures, previous_attempts: history)

    # 使用 validator agent 检查 .task/checklist.md
    result = call validator agent to check against .task/checklist.md

    # 更新 checklist.md
    update_checklist(result.checkbox_states)

    # 更新 meta.yaml 进度
    progress = f"{result.passed_count}/{result.total_count}"
    update_meta_yaml(section_id, progress: progress)

    if result.all_passed:
        # 完成协议：提交所有更改
        git add -A
        git commit -m "${section_name}: ${summary}

        - ${change_1}
        - ${change_2}

        🤖 Generated with InfiStack"

        # 更新状态文件（最后一步）
        update_meta_yaml(section_id, status: "completed")
        return SUCCESS

    history.append({
        attempt: attempt,
        failures: result.failures,
        executor_notes: executor.notes,
        code_snippets: result.relevant_code
    })

    attempt++

return ESCALATE(error_report: history)

完成协议

当所有检查清单项通过时：

暂存所有更改：git add -A
提交并附带结构化消息：
git commit -m "${section_name}: ${summary}

- ${change_1}
- ${change_2}

🤖 Generated with InfiStack"

写入 COMPLETE 到状态文件
只有在此之后才发出完成信号
错误报告格式
error_report:
  section_id: "auth-module"
  attempts: 3
  final_failures:
    - check_id: check-2
      expected: "400响应"
      actual: "500响应"
      code_snippet: |
        // src/auth/validate.ts:45-62
        function validateEmail(email) { ... }
      tested_methods:
        - validateEmail()
        - UserService.create()
        - AuthController.register()
  history:
    - attempt: 1
      approach: "初始实现"
      failures: [...]
    - attempt: 2
      approach: "添加try-catch"
      failures: [...]
    - attempt: 3
      approach: "重构验证"
      failures: [...]


将error_report交给escalation-router。

Weekly Installs
11
Repository
blueif16/amazin…-plugins
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass