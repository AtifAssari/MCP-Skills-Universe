---
title: kwc-vue-development
url: https://skills.sh/kingdee/kwc-skills/kwc-vue-development
---

# kwc-vue-development

skills/kingdee/kwc-skills/kwc-vue-development
kwc-vue-development
Installation
$ npx skills add https://github.com/kingdee/kwc-skills --skill kwc-vue-development
SKILL.md
KWC Vue 开发专家

当项目确认使用 Vue 框架后，本 Skill 负责该框架下的代码编写规范与组件使用指导。基于 Vue 3 (Composition API + <script setup>) 进行开发。

重要：使用前置条件

必须同时满足以下条件才能使用本 Skill：

当前目录已存在 .kd/config.json 文件
配置文件中 framework 字段值为 vue
工程已通过 kwc-project-scaffold 完成初始化

以下场景禁止使用本 Skill，必须交由 kwc-project-scaffold：

工程初始化（kd project init）
创建组件或页面（kd project create）
生成或修改 .js-meta.kwc 组件元数据
生成或修改 .page-meta.kwp 页面元数据
环境配置（kd env 相关命令）
部署操作（kd project deploy）
调试操作（kd debug）— 调试由 kwc-project-scaffold 负责，须以后台模式运行（is_background: true），详见其调试约定

若当前不满足上述前置条件，请立即停止并切换到 kwc-project-scaffold Skill。

核心职责

你负责指导用户进行 KWC Vue 组件的开发、修改和维护。 重要：你必须严格遵守本 Skill 目录下的 rule.md 文件中定义的硬性约束。在开始任何代码编写前，请务必阅读并理解这些规则。

1. 环境上下文确认
项目根目录：包含 .kd 文件夹和 app/kwc 目录。
配置环境：.kd/config.json 中 framework 为 vue。
重要：若当前环境不满足上述条件，必须立即停止使用本 Skill 的所有约束，转而按通用 Vue Web 项目标准协助用户。
2. Vue 3 开发基础

本项目基于 Vue 3，必须遵循以下基本原则：

Composition API：统一使用 <script setup> 语法，禁止使用 Options API（export default { data(), methods, computed, watch }）
响应式：使用 ref() / reactive() 声明响应式状态，禁止使用 this。向 Web Components 传递复杂数据（对象/数组）时，由于底层需检测引用变化，绝对禁止 push 或 splice 原地修改，必须通过重新赋值（如 data.value = [...data.value, new]）产生新引用来触发渲染。
生命周期：使用 onMounted() / onUnmounted() 等 Composition API 钩子
模板语法：
属性绑定：:prop="value"
事件绑定：@sl-change="handler"（Shoelace 组件使用 @sl-* 前缀）
向 Web Component 传递对象/数组属性：必须用 camelCase + .prop 修饰符：
【✅ 正确】 <sl-table :dataSource.prop="rows" :columns.prop="cols" :rowSelection.prop="sel"></sl-table>
【❌ 错误】 <sl-table :data-source="rows" :row-selection="sel"></sl-table>

数字类型属性使用 camelCase 不需 .prop（如 :pageSize="20"）；字符串/布尔属性必须用 camelCase（如 rowKey="id"、showHeader、simpleMode），禁止 kebab-case（如 row-key、show-header）
TypeScript：推荐使用 <script setup lang="ts">
3. 标准工作流 (Workflow)

新建组件：

必须使用 CLI 工具，严禁手工创建文件：
kd project create [组件名] --type kwc

组件命名遵循 PascalCase。

代码实现与修改：

学习：优先参考 app/kwc/exampleComponent。
严格合规：代码必须符合本 Skill 目录下的 rule.md 中的所有约束（导入规范、事件绑定等）。
Shoelace 集成：涉及 Shoelace 组件时，确保从 correct path 导入。

验证与交付：

按项目入口更新 app/kwc/main* 引用。
运行 npm run dev 进行验证。
4. 关键约束摘要 (详细请见本 Skill 目录下的 rule.md)
导入：import '@kdcloudjs/shoelace/dist/components/input/input.js';
业务组件导入：import '@kdcloudjs/shoelace-biz/dist/components/lookup/lookup.js';（注意包名为 shoelace-biz）
模板：使用 <sl-input> (kebab-case)。
事件：使用 @sl-change 绑定。
CSS：样式必须使用 Shoelace Design Token（var(--sl-color-*)、var(--sl-spacing-*)、var(--sl-font-size-*)、var(--sl-border-radius-*)），禁止硬编码 hex 色值和 px 数值。详见 ./reference/css-design-tokens.md。
5. 常用资源
扩展组件文档（位于本 Skill 的 reference/ 目录下）：
基础扩展组件（@kdcloudjs/shoelace）：
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
FloatButton: reference/sl-float-button.md
FloatButtonGroup: reference/sl-float-button.md
Sender: reference/sender/index.md
SenderHeader: reference/sender/index.md
SenderSwitch: reference/sender/index.md
Steps: reference/sl-steps.md
Grid: reference/sl-grid.md
Notification: reference/sl-notification.md
RadioGroup: reference/sl-radio-group.md
Space: reference/sl-space.md
Upload: reference/upload/index.md
Segmented: reference/sl-segmented.md
Transfer: reference/sl-transfer.md
Popconfirm: reference/sl-popconfirm.md
Bubble: reference/sl-bubble.md
业务组件（@kdcloudjs/shoelace-biz，导入路径为 @kdcloudjs/shoelace-biz/dist/components/...）：
Lookup (F7): reference/sl-lookup.md
使用前必须阅读相应文档。
标准组件文档：https://shoelace.style/
6. 输出检查清单

提交代码前，请自查：

 使用 Vue 3 Composition API (<script setup>)，未使用 Options API
 新建组件使用了 kd project create [组件名] --type kwc
 已阅读并遵守本 Skill 目录下的 rule.md 中的所有约束
 导入了所有使用的 Web Components
 模板标签为 kebab-case
 事件使用 @sl-*
 未运行任何 ESLint/Prettier 修复命令，并忽略了所有 ESLint 格式报错
Weekly Installs
89
Repository
kingdee/kwc-skills
GitHub Stars
2
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass