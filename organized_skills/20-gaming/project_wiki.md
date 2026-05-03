---
rating: ⭐⭐⭐
title: project-wiki
url: https://skills.sh/morning-start/coze-skills/project-wiki
---

# project-wiki

skills/morning-start/coze-skills/project-wiki
project-wiki
Installation
$ npx skills add https://github.com/morning-start/coze-skills --skill project-wiki
SKILL.md
ProjectWiki - 智能项目知识助手

ProjectWiki 是一个智能项目知识助手，支持基础文档生成、文档流程管理和知识库查询。

核心能力
基础文档生成: README、ROADMAP、CHANGELOG、ARCHITECTURE
文档流程管理: 生成、更新、修改、完善文档，包含文档管理流程、评审、健康度检查
知识库查询: 技术框架、设计模式、最佳实践速查
文档一致性检查: 术语命名、内容逻辑、格式结构、数据参数、图表文字、角色权限、时间进度
项目类型文档指南: 前端、后端、全栈、移动端、桌面端、CLI/TUI、游戏项目差异化文档推荐
文档管理流程: 6 阶段生命周期管理、角色职责、评审 checklist、工具链推荐
三步工作流程
第一步：查阅信息
阅读项目结构和现有文档
查询知识库获取技术信息
识别项目类型（前端/后端/全栈/移动端/桌面端/CLI/TUI/游戏）
确定需要生成的文档类型
第二步：执行操作
根据项目类型选择合适的文档模板和指南
根据指南编写文档内容
使用 Mermaid 绘制图表
第三步：检查验收
验证文档完整性
运行一致性检查（7 大类检查项）
根据项目类型检查文档完整性
确认格式规范
生成检查报告
参考文档
文档指南
文档	用途	何时使用
guides/README.md	文档编写指南索引	编写任何文档前
guides/architecture-doc-guide.md	架构文档指南	编写 ARCHITECTURE.md
guides/design-doc-guide.md	设计文档指南	编写设计文档
guides/functional-doc-guide.md	功能文档指南	编写功能文档
guides/api-doc-guide.md	API 文档指南	编写 API 文档
guides/cicd-guide.md	CI/CD 文档指南	编写部署文档
guides/changelog-guide.md	变更日志指南	编写 CHANGELOG
guides/roadmap-guide.md	路线图指南	编写 ROADMAP
guides/consistency-check-guide.md	一致性检查指南	文档质量检查时
项目类型指南
文档	用途	何时使用
guides/frontend-project-guide.md	前端项目文档指南	Vue/Svelte/SolidJS 项目
guides/backend-project-guide.md	后端项目文档指南	FastAPI/Gin/Spring Boot 项目
guides/fullstack-project-guide.md	全栈项目文档指南	前后端分离项目
guides/mobile-project-guide.md	移动端项目文档指南	Flutter 项目
guides/desktop-project-guide.md	桌面端项目文档指南	Tauri/Wails/C#/Electron 项目
guides/cli-tui-project-guide.md	CLI/TUI 项目文档指南	命令行工具项目
guides/game-project-guide.md	游戏项目文档指南	Godot 游戏项目
文档管理
文档	用途	何时使用
guides/document-management-guide.md	文档管理流程	建立文档管理流程时
guides/document-health-check-guide.md	健康度检查	检查文档健康度时
guides/document-management-anti-patterns.md	反模式警示	识别文档管理问题时
文档模板
文档	用途	何时使用
templates/README.md	文档模板索引	选择模板时
templates/ARCHITECTURE.md	架构文档模板	生成 ARCHITECTURE.md
templates/CHANGELOG.md	变更日志模板	生成 CHANGELOG.md
templates/ROADMAP.md	路线图模板	生成 ROADMAP.md
templates/consistency-checklist-template.md	一致性检查清单	执行一致性检查
templates/rtm-template.md	需求追踪矩阵	需求 - 设计 - 测试对齐
templates/document-review-checklist.md	文档评审清单	文档评审时
templates/lightweight-doc-management-process.md	轻量级流程	中小团队快速落地时
知识库
文档	用途	何时使用
knowledge/README.md	知识库索引	查询知识库时
knowledge/frameworks.md	框架速查	技术选型时
knowledge/patterns.md	设计模式速查	架构设计时
knowledge/principles.md	设计原则	面向对象设计时
knowledge/consistency-rules.md	一致性规则	了解检查规则和自动化建议
knowledge/project-type-recognition.md	项目类型识别	识别项目类型时
knowledge/document-management-tools.md	工具链指南	选择文档管理工具时
文档类型速查
文档	文件名	用途
README	README.md	项目介绍和快速开始
ROADMAP	ROADMAP.md	项目规划和里程碑
CHANGELOG	CHANGELOG.md	版本变更记录
ARCHITECTURE	ARCHITECTURE.md	系统架构设计
API 文档	wiki/api.md	API 接口说明
设计文档	wiki/design.md	详细设计说明
使用示例
示例 1：生成项目文档

需求: 为新项目生成完整文档

第一步：查阅信息

1. 分析项目结构
   - 项目类型: Web应用
   - 技术栈: React + FastAPI
   - 复杂度: 中等

2. 查询知识库
   - 阅读 [knowledge/frameworks.md](references/knowledge/frameworks.md)
   - 了解 React 和 FastAPI 最佳实践


第二步：执行操作

1. 生成 README.md
   - 使用 [templates/README.md](references/templates/README.md)
   - 填写项目信息

2. 生成 ARCHITECTURE.md
   - 使用 [templates/architecture.md](references/templates/architecture.md)
   - 绘制系统架构图

3. 生成 ROADMAP.md
   - 使用 [templates/ROADMAP.md](references/templates/ROADMAP.md)
   - 规划开发里程碑


第三步：检查验收

□ 所有必需文档已生成
□ 文档格式符合规范
□ 图表清晰可读
□ 链接全部有效

检验结果: ✅ 通过

示例 2：版本发布前一致性检查

需求: 发布 v5.0.0 版本前进行文档一致性检查

第一步：查阅信息

1. 确定检查范围
   - 核心文档：SKILL.md, README.md, CHANGELOG.md, ROADMAP.md
   - 版本相关：版本号、发布日期、Git Tag

2. 准备检查工具
   - 一致性检查清单
   - 版本检查脚本


第二步：执行检查

1. 版本号一致性检查
   - SKILL.md: version: 5.0.0
   - CHANGELOG.md: ## [5.0.0] - 2024-02-20
   - Git Tag: v5.0.0
   ✅ 版本号一致

2. 日期格式检查
   - 所有日期使用 YYYY-MM-DD 格式
   ✅ 日期格式正确

3. 使用检查清单逐项检查
   - 术语与命名：✅
   - 内容逻辑：✅
   - 格式与结构：✅
   - 数据与参数：✅
   - 图表与文字：✅
   - 角色与权限：✅
   - 时间与进度：✅


第三步：生成报告

一致性检查报告：
- 检查日期：2024-02-20
- 检查项数：108
- 通过数：108
- 通过率：100%
- 结论：✅ 通过，可以发布

检验结果：✅ 通过

示例 3：需求变更后一致性检查

需求: 需求 REQ-003 发生变更，检查相关文档一致性

第一步：查阅信息

1. 识别变更影响
   - 需求文档：REQ-003 密码重置功能
   - 影响文档：设计文档、API 文档、测试用例

2. 准备追踪矩阵
   - 查看 RTM 中 REQ-003 的关联


第二步：执行检查

1. 更新需求文档
   - 修改 REQ-003 描述
   - 更新优先级和验收标准

2. 同步更新设计文档
   - 更新 3.2.3 章节
   - 修改流程图和接口定义

3. 更新 API 文档
   - 修改 /api/reset-password 接口
   - 更新请求/响应示例

4. 更新测试用例
   - 修改 TC-011~TC-015
   - 添加新的测试场景

5. 验证一致性
   - 使用 RTM 验证需求 - 设计 - 测试对齐
   - 运行一致性检查脚本


第三步：验证结果

RTM 更新后状态：
| 需求 ID | 设计章节 | 实现模块 | 测试用例 | 状态 |
|---------|---------|---------|---------|------|
| REQ-003 | 3.2.3 ✅ | UserController.resetPassword ✅ | TC-011~015 ✅ | 已验证 ✅ |

检验结果：✅ 通过

注意事项
标准化优先: 所有文档遵循项目规范
渐进式完善: 从核心文档开始，逐步完善
保持一致性: 确保术语、版本、配置在各文档间一致
及时更新: 代码变更时同步更新文档
定期验证: 版本发布前、需求变更后必须进行一致性检查
使用工具: 充分利用自动化检查工具提升效率
文档评审: 重要文档变更需经过同行评审和一致性检查
Weekly Installs
34
Repository
morning-start/c…e-skills
GitHub Stars
4
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass