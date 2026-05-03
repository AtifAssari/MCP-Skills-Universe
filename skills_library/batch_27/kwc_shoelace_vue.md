---
title: kwc-shoelace-vue
url: https://skills.sh/kingdee/kwc-skills/kwc-shoelace-vue
---

# kwc-shoelace-vue

skills/kingdee/kwc-skills/kwc-shoelace-vue
kwc-shoelace-vue
Installation
$ npx skills add https://github.com/kingdee/kwc-skills --skill kwc-shoelace-vue
SKILL.md
Vue 组件开发专家

本 Skill 面向通用 Vue 3 项目，专门处理 @kdcloudjs/shoelace 标准组件和 KWC 扩展组件的接入、开发与修改。

1. 适用范围
当前项目是 Vue 3 Web 项目
需要使用 @kdcloudjs/shoelace 组件
不依赖 KWC 工程目录、页面元数据或 KWC 脚手架
若检测到项目已经是 KWC Vue 工程，应切换到 kwc-vue-development
2. 标准工作流
先确认当前需求是否只是“在现有 Vue 工程中使用组件”，而不是创建 KWC 工程。
开发前阅读本 Skill 目录下的 rule.md，严格遵守导入、事件和属性传递约束。
遇到 Table、DatePicker、Pagination、Nav、XMarkdown、Think 等扩展组件时，先阅读对应 reference/ 文档。
代码交付时遵循当前 Vue 工程自己的入口、构建和测试方式，不引入任何 kd 脚手架命令。
3. 关键约束摘要
组件导入必须使用 @kdcloudjs/shoelace/dist/components/[component]/[component].js
组件标签必须使用 kebab-case
Shoelace 事件必须使用 @sl-*
数组和对象属性必须使用 camelCase + .prop
样式必须优先使用 Shoelace Design Token
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
Upload: reference/upload/index.md
Segmented: reference/sl-segmented.md
Transfer: reference/sl-transfer.md
Popconfirm: reference/sl-popconfirm.md
Bubble: reference/sl-bubble.md
Design Token: reference/css-design-tokens.md
5. 输出检查清单
 当前任务只处理组件接入，不依赖 KWC 工程目录或 KWC CLI 脚手架流程
 组件已从 dist/components/... 导入
 模板标签使用 kebab-case
 事件使用 @sl-*
 数组和对象属性使用 camelCase + .prop
 扩展组件先读过本地文档
 样式优先使用 Design Token
Weekly Installs
44
Repository
kingdee/kwc-skills
GitHub Stars
2
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass