---
rating: ⭐⭐
title: tech-preferences
url: https://skills.sh/zrr1999/skills/tech-preferences
---

# tech-preferences

skills/zrr1999/skills/tech-preferences
tech-preferences
Installation
$ npx skills add https://github.com/zrr1999/skills --skill tech-preferences
SKILL.md
目的

技术偏好不能穷举——它是一个持续演进的过程。本 skill 提供一个偏好分析流程，帮助在具体任务中发现、讨论并固化偏好。

这是一个横切 skill：它帮助做选择，但不替代 project-workflows（开新/维护/学习的工作方式与输出契约）。

当前已知偏好（基线）
Python 生态
包管理：uv（替代 pip/poetry/pyenv）
代码质量：ruff（lint + format），ty（类型检查）
预提交/CI 钩子：prek（替代 pre-commit）
依赖自动升级：Renovate
数据模型：dataclasses（首选，原生零依赖）；仅在需要运行时校验或序列化时才引入 Pydantic v2
Web 后端
框架：FastAPI（async-first，自动 OpenAPI 文档）
输入校验/序列化（API 边界）：Pydantic v2
Web 前端
框架：Svelte（轻量，编译时优化，无运行时 vdom）
构建工具：Vite+（vp）（Vite/Vitest/Oxlint/Oxfmt 统一入口，curl -fsSL https://vite.plus | bash 安装）；或 Vite 单独使用。注：vp 当前仅支持 pnpm/npm/yarn，不支持 bun 作为包管理器。
系统 / 自动化
任务运行：just（替代 Makefile）
容器：Docker / OCI 镜像
macOS 守护进程：launchd（不用 cron）
数据格式
配置：TOML（首选），YAML（CI only），JSON（API 交换）
文本格式：Markdown（文档），结构化日志优先 JSON
偏好分析流程

在遇到技术选型时，按以下步骤分析：

识别决策点 — 明确需要选择的技术维度（语言/框架/工具/数据格式等）。
对比当前偏好 — 检查上方"已知偏好"列表，确认是否已有约定；若有，默认遵循。
分析偏差理由 — 如果需要偏离已知偏好，明确写出原因（性能、生态、约束等）。
讨论新偏好 — 如果发现新的、值得固化的偏好，在响应中明确提出：

建议将「X 替代 Y，原因：...」加入 tech-preferences skill。

自主提案 — 当偏好有明显新增或变化时，主动在 PR/Issue 中提交偏好变更提案（格式见下），无需等待人类提示。
沉淀更新 — 经人类确认后，将新偏好追加到"当前已知偏好"节。
示例分析

场景：需要为新 Python 项目选择测试框架。

决策点：测试框架选型
已知偏好：无（当前基线未列测试框架）
对比候选：pytest（生态最丰富，prek 默认集成）vs unittest（标准库，无额外依赖）
分析：已有仓库均使用 pytest；prek 钩子默认运行 pytest；选 pytest
新偏好提案：pytest（Python 测试框架首选）→ 提交提案加入基线
如何贡献新偏好

当发现偏好有明显新增或变化时，自主提交偏好变更提案，格式如下：

偏好提案：将 <新工具/框架> 加入 tech-preferences skill
- 类别：<Python生态 / Web后端 / 前端 / 系统 / 数据格式>
- 替代：<被替代的工具，若有>
- 原因：<具体理由，1-3句>
- 参考：<项目/PR/文档链接，若有>


可通过 PR 直接修改此 skill 的"当前已知偏好"节，或在相关 Issue/PR 中以评论形式提案。

Weekly Installs
23
Repository
zrr1999/skills
First Seen
Mar 8, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass