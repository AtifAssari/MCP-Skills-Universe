---
rating: ⭐⭐
title: raycommondevelopskill
url: https://skills.sh/site/developer.tuya.com/raycommondevelopskill
---

# raycommondevelopskill

skills/developer.tuya.com/ray-common-develop-skill
ray-common-develop-skill
$ npx skills add https://developer.tuya.com/material/skills/RayCommonDevelopSkill-beta
SKILL.md
RayCommonDevelopSkill
Overview

本 Skill 帮助在 Ray 小程序（涂鸦面板/跨端小程序）场景下生成与修改页面与组件代码。Ray 与微信小程序、Taro、React Native 形态相似但 API 与标签体系不同，必须严格依据本 Skill 内的标签对应表、references 下的框架与 smart-ui 文档产出代码，避免上下文超载与 API 幻觉。

按需加载：本 Skill 下的 references/ 目录体量很大，【绝对禁止】在未明确需求前一次性读取该目录下所有内容。你必须先查阅 _meta.json 或使用 Read/Glob/Grep 等工具分步、按需读取具体文件。
索引优先：需要 UI 组件时，先读 references/smart-ui/_meta.json 定位组件与功能分类，再按需读取对应 references/smart-ui/<组件>.md。若 _meta.json 中无法定位，允许在 references/smart-ui/ 下用关键词（如 dialog、upload、progress）做检索后再读取候选文档，禁止在查不到时臆造组件或 Props。
基石标签表：以下标签对应表已内嵌，Skill 触发即生效。凡涉及 UI 结构、页面/组件代码生成或图片转代码时，必须优先按此表选用 Ray 标签，并在输出代码前做一次“语义–标签”校验。
版本对齐: 你必须注意 package.json 中的 @ray-js/smart-ui 版本, 是否与文档中要求的版本是否匹配，如果无法匹配，请提示用户进行升级 @ray-js/smart-ui 到最新版本。
Ray 标签对应表（基石）
Ray 标签	功能说明
View	视图容器
ScrollView	可滚动视图区域
Swiper	滑块视图容器
SwiperItem	仅可放置在 swiper 中，宽高 100%
MovableArea	movable-view 的可移动区域
MovableView	可拖拽滑动的视图容器
PageContainer	页面容器
CoverView	覆盖在原生组件之上的文本视图
Text	文本（类似 span）
Progress	进度条
RichText	富文本
Checkbox	多选项目
CheckboxGroup	多项选择器
Form	表单
Input	输入框
Label	改进表单可用性
Slider	滑动选择器
Switch	开关选择器
Textarea	多行输入框
Camera	相机
Image	图片
IpcPlayer	实时视频播放
Video	H5 视频
NativeVideo	原生视频
canvas	画布
Map	地图
Webview	承载网页的容器
禁止使用小写 HTML 标签（如 div、span），必须使用上表首字母大写的 Ray 标签（如 View、Text）。
Smart-UI 是 Ray 的基础 UI 库（类似 Vant），如果要用的组件在 Ray 标签对应表中和 Smart-UI 都可使用时，组优先使用 references/smart-ui/ 文档中的组件，Props 与事件以文档为准，禁止臆造未在文档中出现的属性。
Instructions
1. 文档加载强制流程
禁止一次性读取 references/ 或其子目录下的全部文件。
按任务类型执行：
UI/组件：先读 references/smart-ui/_meta.json → 按组件名或分类定位 doc → 仅读取需要的 references/smart-ui/<doc>。
索引未命中：在 references/smart-ui/ 下用关键词检索（如 Grep/Glob），再读取候选文档确认，禁止直接猜组件或 API。
页面/生命周期/路由：按需读取 references/ray/framework/page.md、references/ray/framework/api.md。
组件写法/属性风格：references/ray/framework/component.md + 对应 smart-ui 组件文档。
输出结论时，可简要说明本次依据了哪些文档或片段；若信息不足，显式声明“未在文档中找到，基于假设”而非静默猜测。
2. 任务执行 SOP（标准步骤）
需求澄清：确认是页面、组件、还是改现有代码；是否涉及多语言、样式、设备 API。
文档检索：
涉及 UI → 使用内嵌标签表 + references/smart-ui/_meta.json → 按需读具体 smart-ui 文档和package.json 中的 @ray-js/smart-ui 版本信息, 确认版本对齐。
涉及生命周期/路由 → 读 references/ray/framework/page.md 或 api.md。
方案/代码生成：按下面“代码原则”与“禁止项”产出。
生成前校验：
用标签对应表检查是否误用 div/span 或错误标签；
检查是否混用 wx.*/my.*；
检查 smart-ui 组件是否仅使用文档中的 Props/Events；
**【必须检查】**确认所有文案是否使用 Strings.getLang('key')，绝对禁止硬编码中文文案。
输出：代码 + 简短说明 + 必要时“依据文档”或“假设说明”。
3. 代码原则（与 ddd 对齐）
每个库在单个文件中只引入一次；优先使用 import { xx } from 'xxx'。
多语言（One Golden Rule - 最高优先级）：
**【绝对禁止】**在代码中直接使用中文或其他硬编码文案。
仅允许使用 import Strings from '@/i18n' 与 Strings.getLang('xxx')。
禁止在业务组件中直接引入 @ray-js/panel-sdk 的 I18N 类；多语言逻辑由项目 i18n 层统一处理。
所有页面/组件中的文案必须通过 Strings.getLang('key') 填充，key 命名使用语义化英文（如 confirmButtonText、welcomeMessage）。
若为页面，代码生成到 /pages；若为组件，生成到 /components。复杂模块先拆子组件再集成到主 tsx。
图片输入时：先分析图中页面元素，再结合标签表与 smart-ui 文档生成代码，优先使用 smart-ui 组件。
4. 禁止项（必须遵守）
禁止使用小写 HTML 标签（如 div、span），一律使用 Ray 标签（如 View、Text）。
禁止在 Ray 业务代码中混入微信/支付宝原生 API（如 wx.xxx、my.xxx）。
禁止虚构 Ray 生命周期或 API（如未在 references/ray 文档中出现的钩子或方法）。
禁止臆造 smart-ui 组件的 Props 或事件，必须以 references/smart-ui/<组件>.md 为准。
禁止在未通过 _meta.json 或检索确认前，一次性加载 references 下大量文档到上下文。
5. 输入/输出契约
输入：业务目标、页面/组件范围、数据结构与交互要求、约束（多语言、样式、目录等）。
输出：实现步骤摘要、关键代码、依赖说明、边界与校验要点；若引用文档，可注明来源。
资源与检索优先级
Ray 文档索引：references/ray/_meta.json（guide / framework / component / api / extended），按需进入对应目录读取具体 md。
Smart-UI 索引：references/smart-ui/_meta.json（components + categories），先查再读具体 references/smart-ui/<组件>.md。
优先级：官方 Ray/API 文档 > 本 SKILL 内嵌标签表 > smart-ui 文档 > 工程约定 > 通用推断。

文档抽样与归纳：Ray 按能力面抽样（如 framework/page、component、api）；smart-ui 按组件类型抽样（如 button、field、popup、switch 等代表组件）。所有组件的 Props、Events、样式变量均以当前读取到的文档为准，未在文档中出现的不得使用；同类组件可类比已读文档的用法模式，但新增属性必须再次查阅该组件文档确认。

示例问法与标准执行步骤

示例 1：写一个带进度条的弹窗

步骤 1：使用内嵌标签表确认“进度条”对应 Ray 的 Progress；弹窗在 smart-ui 中查找是否也存在Progress 组件，如果存在则优先使用 smart-ui 的 Progress。
步骤 2：读取 references/smart-ui/_meta.json 和 package.json 中的 @ray-js/smart-ui 版本信息, 确认版本对齐，定位弹窗类组件（如 popup、dialog）及进度条（progress）。
步骤 3：按需读取 references/smart-ui/popup.md、references/smart-ui/progress.md 查看 API。
步骤 4：按代码原则编写（less 分离、多语言用 Strings.getLang、无 div/span、无 wx/my）。
步骤 5：生成前校验标签与 Props 是否均来自文档。

示例 2：新建一个设置页，包含开关和输入项

步骤 1：标签表 + references/smart-ui/_meta.json 定位 Switch、Field 等。
步骤 2：读取 references/smart-ui/switch.md、references/smart-ui/field.md。
步骤 3：页面放到 /pages，样式用 index.module.less，多语言仅用 Strings。
步骤 4：校验禁止项后输出。

示例 3：图片转 Ray 页面

步骤 1：分析图片中的区块与控件（列表、按钮、表单等）。
步骤 2：用内嵌标签表映射到 View/ScrollView/Text/Button 等；若需组件则查 _meta.json 和 package.json 中的 @ray-js/smart-ui 版本信息, 确认版本对齐 再读对应 smart-ui 文档。
步骤 3：生成代码并做一次语义–标签与禁止项校验。
常见问题

Q：_meta.json 里没有想要的组件怎么办？
A：在 references/smart-ui/ 下用关键词（如 Grep）检索，再读取候选文档确认；仍无则说明“未在文档中找到”，不臆造 API, 可以使用基础标签表中的标签进行实现。

Q：多语言除了 Strings.getLang 还能用别的吗？
A：本 Skill 约定业务代码仅使用 import Strings from '@/i18n' 与 Strings.getLang('xxx')，不在业务组件中直接使用 panel-sdk 的 I18N 类。

Q：如何减少上下文占用？
A：只读与当前任务直接相关的 _meta.json 与 1～2 个具体文档；需要时再增量读取，绝不一次性加载 references 全量内容。

Weekly Installs
20
Source
developer.tuya.…ill-beta
First Seen
Mar 5, 2026
Security Audits
SocketPass