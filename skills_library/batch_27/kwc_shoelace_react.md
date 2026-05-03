---
title: kwc-shoelace-react
url: https://skills.sh/kingdee/kwc-skills/kwc-shoelace-react
---

# kwc-shoelace-react

skills/kingdee/kwc-skills/kwc-shoelace-react
kwc-shoelace-react
Installation
$ npx skills add https://github.com/kingdee/kwc-skills --skill kwc-shoelace-react
SKILL.md
React 组件开发专家

本 Skill 面向通用 React Web 项目，专门处理 @kdcloudjs/shoelace 标准组件和 KWC 扩展组件的接入、开发与修改。

1. 适用范围
当前项目是 React Web 项目
需要使用 @kdcloudjs/shoelace 组件
不依赖 KWC 工程目录、页面元数据或 KWC 脚手架
若检测到项目已经是 KWC React 工程，应切换到 kwc-react-development
2. 标准工作流
先确认当前需求是否只是“在现有 React 工程中使用组件”，而不是创建 KWC 工程。
开发前阅读本 Skill 目录下的 rule.md，严格遵守 React Wrapper、事件和样式约束。
遇到 Table、DatePicker、Pagination、Nav、XMarkdown、Think 等扩展组件时，先阅读对应 reference/ 文档。
代码交付时遵循当前 React 工程自己的入口、构建和测试方式，不引入任何 kd 脚手架命令。
3. 关键约束摘要
组件导入必须使用 @kdcloudjs/shoelace/dist/react/[component]/index.js
类型导入必须使用 @kdcloudjs/shoelace/dist/components/[component]/[component].js
Shoelace 事件必须映射为 onSl*
样式必须优先使用 Shoelace Design Token，避免硬编码颜色和间距
扩展组件 API 必须先看本地 reference/ 文档，不能凭空猜测
4. 常用资源
Table: reference/table/index.md
DatePicker: reference/datepicker/index.md
TimePicker: reference/sl-timepicker.md
Pagination: reference/sl-pagination.md
Daterangepicker: reference/sl-daterangepicker.md
ThoughtChain: reference/sl-thought-chain.md
Nav: reference/sl-nav.md
XMarkdown: reference/sl-xmarkdown.md
Think: reference/sl-think.md
TreeSelect: reference/sl-tree-select.md
Cascader: reference/sl-cascader.md
Steps: reference/sl-steps.md
Grid: reference/sl-grid.md
Notification: reference/sl-notification.md
RadioGroup: reference/sl-radio-group.md
Space: reference/sl-space.md
Upload: reference/upload/index.md
Image: reference/sl-image.md
Design Token: reference/css-design-tokens.md
Segmented: reference/sl-segmented.md
Transfer: reference/sl-transfer.md
PopConfirm: reference/sl-popconfirm.md
Bubble: reference/sl-bubble.md
5. 输出检查清单
 当前任务只处理组件接入，不依赖 KWC 工程目录或 KWC CLI 脚手架流程
 React 组件从 dist/react/.../index.js 导入
 事件命名使用 onSl*
 事件目标做了类型断言
 扩展组件先读过本地文档
 样式优先使用 Design Token
Weekly Installs
51
Repository
kingdee/kwc-skills
GitHub Stars
2
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass