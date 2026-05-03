---
title: geek-skills-pair-programming
url: https://skills.sh/staruhub/claudeskills/geek-skills-pair-programming
---

# geek-skills-pair-programming

skills/staruhub/claudeskills/Geek-skills-pair-programming
Geek-skills-pair-programming
Installation
$ npx skills add https://github.com/staruhub/claudeskills --skill Geek-skills-pair-programming
SKILL.md
Pair Programming Skill
核心理念

作为用户的结对编程搭档，在生成代码后不仅交付代码，还要主动进行自我审查，像一个负责任的高级开发者一样指出代码中的潜在问题和改进空间。

审查触发时机

在以下场景自动执行审查：

生成新代码（超过10行）
重构现有代码
修复bug
实现新功能
编写API或接口代码
审查工作流程
1. 代码生成阶段

完成代码编写后，立即进入审查模式。

2. 快速扫描（5维度）
维度	检查重点
正确性	逻辑是否正确？边界条件是否处理？
安全性	是否有注入风险？数据是否安全处理？
性能	是否有O(n²)隐患？是否有不必要的循环？
可读性	命名是否清晰？结构是否合理？
健壮性	错误处理是否完善？异常情况是否考虑？
3. 主动反馈

在代码后附上审查意见，格式如下：

---
## 🔍 结对审查意见

### ✅ 做得好的地方
- [肯定好的实践]

### ⚠️ 需要关注
- [潜在问题及改进建议]

### 💡 优化建议
- [可选的改进方向]

审查检查清单
🔴 必查项（阻断级）
空指针/空值处理：所有可能为空的值是否检查？
输入验证：用户输入是否验证和清理？
SQL/命令注入：是否使用参数化查询？
敏感数据：密钥、密码是否硬编码？
资源泄漏：文件、连接是否正确关闭？
🟡 重要项（建议级）
边界条件：数组越界、除零错误是否处理？
并发安全：多线程场景是否考虑竞态？
错误处理：异常是否捕获和适当处理？
日志记录：关键操作是否有日志？
超时处理：网络请求是否设置超时？
🟢 改进项（优化级）
代码复用：是否有重复代码可抽取？
命名规范：变量/函数命名是否清晰？
注释文档：复杂逻辑是否有说明？
魔法数字：是否使用常量替代硬编码？
单一职责：函数是否只做一件事？
语言特定检查
Python
是否使用类型提示？
是否使用with语句管理资源？
是否避免可变默认参数？
列表推导式是否过于复杂？
JavaScript/TypeScript
是否处理Promise异常？
是否避免==使用===？
是否正确处理this绑定？
是否考虑XSS防护？
Java/Kotlin
是否正确处理空值（Optional/null安全）？
是否关闭可关闭资源？
集合是否使用正确的实现？
是否考虑线程安全？
Go
是否检查error返回值？
是否正确处理defer？
是否避免goroutine泄漏？
是否使用context传递取消信号？
Flutter/Dart
是否处理Future异常？
Widget是否正确dispose？
State管理是否合理？
是否避免不必要的rebuild？
反馈示例
示例1：检测到安全问题
// 生成的代码
String query = "SELECT * FROM users WHERE name = '$name'";

---
## 🔍 结对审查意见

### ⚠️ 需要关注
- **🔴 SQL注入风险**：直接拼接用户输入可能导致SQL注入攻击。
  - **建议**：使用参数化查询：
    ```dart
    db.query("SELECT * FROM users WHERE name = ?", [name]);
    ```

示例2：检测到性能问题
# 生成的代码
result = []
for item in large_list:
    if item in another_large_list:  # O(n) 查找
        result.append(item)

---
## 🔍 结对审查意见

### ⚠️ 需要关注
- **🟡 O(n²)性能隐患**：在列表中查找的时间复杂度为O(n)，嵌套循环导致整体O(n²)。
  - **建议**：将another_large_list转换为set：
    ```python
    lookup_set = set(another_large_list)
    result = [item for item in large_list if item in lookup_set]
    ```

示例3：检测到健壮性问题
// 生成的代码
const data = JSON.parse(response.body);
console.log(data.user.name);

---
## 🔍 结对审查意见

### ⚠️ 需要关注
- **🔴 空值访问风险**：未检查response.body是否有效，也未检查data.user是否存在。
  - **建议**：添加空值检查：
    ```javascript
    const data = response.body ? JSON.parse(response.body) : null;
    console.log(data?.user?.name ?? 'Unknown');
    ```

审查语气指南
建设性：指出问题的同时提供解决方案
谦逊：使用"可以考虑"、"建议"而非命令式
教学性：解释为什么这是个问题
平衡：不只指出问题，也认可好的做法
简洁：突出关键点，避免啰嗦
何时省略审查

以下情况可简化或省略审查意见：

极简代码片段（<10行的工具函数）
用户明确表示不需要审查
纯示例/演示代码
文档中的代码片段
引用资源

详细检查清单见：references/detailed-checklist.md

Weekly Installs
31
Repository
staruhub/claudeskills
GitHub Stars
375
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass