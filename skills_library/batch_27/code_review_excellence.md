---
title: code-review-excellence
url: https://skills.sh/awesome-skills/code-review-skill/code-review-excellence
---

# code-review-excellence

skills/awesome-skills/code-review-skill/code-review-excellence
code-review-excellence
Installation
$ npx skills add https://github.com/awesome-skills/code-review-skill --skill code-review-excellence
SKILL.md
Code Review Excellence

Transform code reviews from gatekeeping to knowledge sharing through constructive feedback, systematic analysis, and collaborative improvement.

When to Use This Skill
Reviewing pull requests and code changes
Establishing code review standards for teams
Mentoring junior developers through reviews
Conducting architecture reviews
Creating review checklists and guidelines
Improving team collaboration
Reducing code review cycle time
Maintaining code quality standards
Core Principles
1. The Review Mindset

Goals of Code Review:

Catch bugs and edge cases
Ensure code maintainability
Share knowledge across team
Enforce coding standards
Improve design and architecture
Build team culture

Not the Goals:

Show off knowledge
Nitpick formatting (use linters)
Block progress unnecessarily
Rewrite to your preference
2. Effective Feedback

Good Feedback is:

Specific and actionable
Educational, not judgmental
Focused on the code, not the person
Balanced (praise good work too)
Prioritized (critical vs nice-to-have)
❌ Bad: "This is wrong."
✅ Good: "This could cause a race condition when multiple users
         access simultaneously. Consider using a mutex here."

❌ Bad: "Why didn't you use X pattern?"
✅ Good: "Have you considered the Repository pattern? It would
         make this easier to test. Here's an example: [link]"

❌ Bad: "Rename this variable."
✅ Good: "[nit] Consider `userCount` instead of `uc` for
         clarity. Not blocking if you prefer to keep it."

3. Review Scope

What to Review:

Logic correctness and edge cases
Security vulnerabilities
Performance implications
Test coverage and quality
Error handling
Documentation and comments
API design and naming
Architectural fit

What Not to Review Manually:

Code formatting (use Prettier, Black, etc.)
Import organization
Linting violations
Simple typos
Review Process
Phase 1: Context Gathering (2-3 minutes)

Before diving into code, understand:

Read PR description and linked issue
Check PR size (>400 lines? Ask to split)
Review CI/CD status (tests passing?)
Understand the business requirement
Note any relevant architectural decisions
Phase 2: High-Level Review (5-10 minutes)
Architecture & Design - Does the solution fit the problem?
For significant changes, consult Architecture Review Guide
Check: SOLID principles, coupling/cohesion, anti-patterns
Performance Assessment - Are there performance concerns?
For performance-critical code, consult Performance Review Guide
Check: Algorithm complexity, N+1 queries, memory usage
File Organization - Are new files in the right places?
Testing Strategy - Are there tests covering edge cases?
Phase 3: Line-by-Line Review (10-20 minutes)

For each file, check:

Logic & Correctness - Edge cases, off-by-one, null checks, race conditions
Security - Input validation, injection risks, XSS, sensitive data
Performance - N+1 queries, unnecessary loops, memory leaks
Maintainability - Clear names, single responsibility, comments
Phase 4: Summary & Decision (2-3 minutes)
Summarize key concerns
Highlight what you liked
Make clear decision:
✅ Approve
💬 Comment (minor suggestions)
🔄 Request Changes (must address)
Offer to pair if complex
Review Techniques
Technique 1: The Checklist Method

Use checklists for consistent reviews. See Security Review Guide for comprehensive security checklist.

Technique 2: The Question Approach

Instead of stating problems, ask questions:

❌ "This will fail if the list is empty."
✅ "What happens if `items` is an empty array?"

❌ "You need error handling here."
✅ "How should this behave if the API call fails?"

Technique 3: Suggest, Don't Command

Use collaborative language:

❌ "You must change this to use async/await"
✅ "Suggestion: async/await might make this more readable. What do you think?"

❌ "Extract this into a function"
✅ "This logic appears in 3 places. Would it make sense to extract it?"

Technique 4: Differentiate Severity

Use labels to indicate priority:

🔴 [blocking] - Must fix before merge
🟡 [important] - Should fix, discuss if disagree
🟢 [nit] - Nice to have, not blocking
💡 [suggestion] - Alternative approach to consider
📚 [learning] - Educational comment, no action needed
🎉 [praise] - Good work, keep it up!
Language-Specific Guides

根据审查的代码语言，查阅对应的详细指南：

Language/Framework	Reference File	Key Topics
React	React Guide	Hooks, useEffect, React 19 Actions, RSC, Suspense, TanStack Query v5
Vue 3	Vue Guide	Composition API, 响应性系统, Props/Emits, Watchers, Composables
Rust	Rust Guide	所有权/借用, Unsafe 审查, 异步代码, 错误处理
TypeScript	TypeScript Guide	类型安全, async/await, 不可变性
Python	Python Guide	可变默认参数, 异常处理, 类属性
Java	Java Guide	Java 17/21 新特性, Spring Boot 3, 虚拟线程, Stream/Optional
Go	Go Guide	错误处理, goroutine/channel, context, 接口设计
C	C Guide	指针/缓冲区, 内存安全, UB, 错误处理
C++	C++ Guide	RAII, 生命周期, Rule of 0/3/5, 异常安全
CSS/Less/Sass	CSS Guide	变量规范, !important, 性能优化, 响应式, 兼容性
Qt	Qt Guide	对象模型, 信号/槽, 内存管理, 线程安全, 性能
Additional Resources
Architecture Review Guide - 架构设计审查指南（SOLID、反模式、耦合度）
Performance Review Guide - 性能审查指南（Web Vitals、N+1、复杂度）
Common Bugs Checklist - 按语言分类的常见错误清单
Security Review Guide - 安全审查指南
Code Review Best Practices - 代码审查最佳实践
PR Review Template - PR 审查评论模板
Review Checklist - 快速参考清单
Weekly Installs
323
Repository
awesome-skills/…ew-skill
GitHub Stars
385
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass