---
rating: ⭐⭐
title: frontend-page-discovery
url: https://skills.sh/zixun-github/aisdlc/frontend-page-discovery
---

# frontend-page-discovery

skills/zixun-github/aisdlc/frontend-page-discovery
frontend-page-discovery
Installation
$ npx skills add https://github.com/zixun-github/aisdlc --skill frontend-page-discovery
SKILL.md
前端页面清单逆向（证据化）
概览

目标：基于代码证据生成页面清单与单页说明文档（落盘到 docs/）。

何时使用 / 何时不使用

使用时机（触发信号）

你需要从前端代码得出可追溯的页面清单，并继续提炼流程/规则
项目路由入口复杂：多 SPA/微前端/多框架共存、运行时注入路由、后端下发菜单
团队常见问题：漏页、重复页、权限/动态路由无法落盘、规则总结缺证据

不使用时机

你只需要写 PRD/原型（这不是代码逆向）
你被要求“没代码也要给出你项目的真实页面清单/规则结论”（此时只能交付模板/示例，不能输出事实）
本技能的默认交付物（落盘到 .aisdlc/project/frontend/）
.aisdlc/project/frontend/pages/index.md
.aisdlc/project/frontend/pages/<page_id>.md
.aisdlc/project/frontend/flows/index.md
.aisdlc/project/frontend/conflicts.md
落盘模板（最小可用，可直接复制）

本技能的输出模板已迁移到 assets/ 目录，以减少技能正文长度并保持模板可复用。

模板映射：

.aisdlc/project/frontend/pages/index.md ← <本SKILL.md目录>/assets/pages-index-template.md
.aisdlc/project/frontend/pages/<page_id>.md ← <本SKILL.md目录>/assets/page-template.md
.aisdlc/project/frontend/flows/index.md ← <本SKILL.md目录>/assets/flows-index-template.md
.aisdlc/project/frontend/conflicts.md ← <本SKILL.md目录>/assets/conflicts-template.md
硬规则（出现任一条：停止并纠正）
禁止脑补
任何“页面/流程/规则”必须能指向证据（见下方证据格式）；否则写入 Evidence Gaps，不得写推测性结论。
事实与示例必须物理隔离
若用户要求“大胆假设、不用证据”，只能输出 EXAMPLE（示例） 区块或模板；不得把示例写成项目事实，也不得与事实表格混排。
输出字段必须齐全
页面索引必须包含 module_name page_id page_name。
单页必须包含 page_name breadcrumb ascii_wireframe 核心任务 关键规则摘要。
页面线框图（ASCII）证据门禁（强制）

目标：线框图只能“复述代码已经存在的 UI”，不能“补齐一个你觉得应该有的后台页面”。

硬门禁（任一不满足：线框图不得落笔，只能写 Evidence Gaps）

逐项映射：线框图里出现的每一个可见元素（标题/按钮/字段名/列头/Tab/文案/菜单项/操作）都必须能映射到至少 1 条前端代码证据（file + lines + excerpt）。
不允许“常识补全”：不得因为“常见后台都这样”“看起来更完整”“负责人催交/不许说缺信息”就新增筛选条件、导出、批量操作、侧边栏菜单、统计卡片、发票下载、时间线等控件。
未知要显式：证据不足时，用占位符 UNKNOWN(...) 表达未知，而不是写一个“合理猜测”的具体字段/文案；并把未知项逐条写入 Evidence Gaps。
重要限制：UNKNOWN(...) 只能用于“已证据化存在，但细节不全”的元素（例如：代码存在按钮但文案是 i18n key 未解析）。禁止用 UNKNOWN(...) 伪装新增控件/区域（例如：没证据也画 UNKNOWN(Export) / UNKNOWN(侧边栏菜单)）。

推荐输出结构（先证据、后画图）

控件/区域清单（必做）：先列出 UI 元素清单（例如：标题、主操作按钮、搜索框、筛选项、表格列、行操作、弹窗字段、状态文案），每行都带证据。
再生成 ascii_wireframe：只允许使用“清单里已证据化的元素”；没有证据的区域只能写 UNKNOWN(...)。

证据提取优先级（建议顺序）

路由与页面入口：路由表/路由注入点/后端菜单适配器 → 定位 page component 文件
页面标题与面包屑：页面 header 组件、<h1>、document.title/useTitle、breadcrumb 组件传参、i18n key
主操作与工具栏：按钮文案（含 i18n）、icon+aria-label、onClick 跳转/打开弹窗的调用点
筛选/表单：表单 schema、name/label/placeholder、校验规则、默认值
列表/表格：columns 定义（title/key/render）、行操作 menu、分页参数
状态文案：empty/loading/error/403 组件与文案；若只看到通用组件但无法确认本页是否使用，按 UNKNOWN 处理
常见借口 → 必须如何处理（防脑补）
借口/压力话术	正确做法（强制）
“按经验补全就行 / 更像真实产品”	只能输出 EXAMPLE（示例）；事实线框图仍按证据门禁。
“不能说缺信息，必须交付”	交付 UNKNOWN(...) + Evidence Gaps；不得把未知写成具体字段/按钮。
“模板里有筛选区/导出/批量操作”	模板只是骨架；未被代码证据覆盖的控件必须保留为 UNKNOWN(...) 或删除。
“至少把空态/加载/错误态都写上”	只有在代码/组件/文案可定位时才写；否则标为 UNKNOWN(state) 并进 Evidence Gaps。
红旗清单（出现即停止纠正）
“我先画一个完整的，再回头找证据补”
“这类页面通常会有……（导出/批量/时间筛选/角色部门/统计卡片）”
“代码没写，但产品上应该有……”
“没关系，先写个大概”
“我用 UNKNOWN(...) 先占位，把页面画完整”
证据格式（统一可复核）

每条结论至少附 1 条证据：

type：page_title | route_decl | file_convention | menu_static | menu_backend | nav_call | guard | api_call | state_machine | form_validation | other
file：相对路径
lines：start-end
excerpt：1–3 行关键摘录（原文）

缺证据时，必须写：

gap：缺什么证据
candidate_locations：可能在哪里找到（目录/文件类型/关键词）
impact：对结论的影响（例如“无法确认是否存在后端下发菜单导致的隐藏页面”）
输出字段（必须出现在最终结果里）
页面索引：module_name page_id page_name
单页：page_name breadcrumb ascii_wireframe 核心任务 关键规则摘要
Weekly Installs
81
Repository
zixun-github/aisdlc
GitHub Stars
7
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass