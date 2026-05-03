---
rating: ⭐⭐⭐
title: huo15-openclaw-frontend-design
url: https://skills.sh/site/skills.volces.com/huo15-openclaw-frontend-design
---

# huo15-openclaw-frontend-design

skills/skills.volces.com/huo15-openclaw-frontend-design
huo15-openclaw-frontend-design
$ npx skills add https://skills.volces.com/c/arkclaw-personal/skills/clawhub/zhaobod1
SKILL.md
火一五前端设计技能 v1.0

高保真 Web UI 原型生成 — 青岛火一五信息科技有限公司 设计理念对标 Anthropic frontend-design skill 与 2026 社区共识，本土化改写、不拷贝官方内容

一、触发场景

当用户要构建以下任一，触发本技能：

网站 / 落地页 / 官网 / 仪表盘
React / Vue / HTML / Svelte 组件
营销海报 / 产品详情页 / 信息图
任何"美化页面 / 优化 UI"类请求

不触发（归其他技能）：

PPT 演示稿 → huo15-openclaw-ppt
Word / PDF 文档 → huo15-openclaw-office-doc
纯数据分析图表 → 常规 matplotlib / echarts 即可

产出：可直接运行的 HTML/CSS/JS（或 React/Vue）代码 + 3 行设计说明 + 可选截图验证命令。

二、设计思考（动手前必答四问）
维度	要回答
目的	这个界面解决什么问题？谁是使用者？
基调	选一个极端方向（见 §三）
约束	技术栈 / 性能 / 可访问性 / 目标设备
差异点	用户会记住哪一件事？

硬规则：承诺一个极端方向。极简和极繁同样有效，关键是意图明确，不要骑墙。

三、五大美学流派（必选其一）
流派	关键特征	适合场景	参考
BOLD-MINIMAL 勇敢极简	大字号、大留白、2 色系、无装饰	科技产品、B 端 SaaS、个人作品集	Stripe / Linear / Apple
EDITORIAL 编辑杂志	衬线字、纵向栅格、引号装饰、杂志版式	品牌故事、深度内容、报告	NYT Style / The Verge
BRUTALIST 野兽派	等宽字、粗黑线、打破网格、刻意粗糙	独立工作室、Web3、先锋作品	Bloomberg / early craigslist
RETRO-FUTURE 复古未来	像素字、CRT 光晕、80s 霓虹配色	游戏、音乐、娱乐	Vaporwave / Cyberpunk 2077
ORGANIC 有机自然	手绘感、暖色、不规则形状、柔边	食品、母婴、健康	Medium 早期 / Notion

如果用户没给方向：并行生成 3 个方向的 Junior pass（极简 / 编辑 / 一个反差方向）对比选择，调用 huo15-openclaw-design-director 协助打分。

四、反 AI Slop 硬红线（违反任一直接判废）
#	禁用项	为什么
1	默认 Inter / Roboto / Arial / system-ui 字体	字体即性格，系统字 = 没性格
2	紫色渐变（尤其紫色渐变打白底）	2023 以来 AI 最滥用的视觉陈词滥调
3	emoji 当图标	必须用 Lucide / Phosphor / Tabler / Heroicons 真图标
4	圆角卡片 + 左侧彩色竖条	Tailwind 默认范式，设计师都看腻了
5	CSS 画的伪产品图	真产品图用 Unsplash/Picsum 占位，明确标注"待替换"
6	默认暗黑 #121212 + 紫色主题	懒，且和 #2 联动犯错
7	Hero + Features + CTA + Footer 千篇一律骨架	按内容定制结构，不要模板化
8	全部用 #007AFF / #FF3B30 这类 iOS 系统色	没有记忆点
五、美学要素清单（每项都要想过）
5.1 字体 Typography
主字（display）选有性格的：Playfair Display / IBM Plex Serif / Space Mono / Noto Serif SC / DM Serif / Rubik Mono One
副字（body）选考究的：IBM Plex Sans / Source Serif / 思源宋体 / Noto Sans SC
主副反差要大，避免同字族
5.2 颜色 Color
主色 + 锐利强调色，CSS variables 统一管理
优先 oklch 色空间（感知均匀，避免灰调）
主色占 60-70%，强调色 5-10%，中性 20-30%
不要 evenly-distributed palette
5.3 动效 Motion
页面加载的 staggered reveal > 散落的微交互
animation-delay 做级联出场
CSS 优先，React 用 Motion（framer-motion）
一个高质量的动效 > 十个微交互
5.4 空间 Spatial Composition
不对称 / 重叠 / 对角线 / 打破网格
留白充足 或 密集信息，二选一
避免居中对齐一统到底
5.5 氛围 Backgrounds & Texture
渐变网格 / 噪点 / 几何图案 / 戏剧阴影
装饰性边框 / 自定义光标 / grain overlay
不要纯色底（除非极简流派明确需要）
六、工作流（Junior → Full 两趟渲染）
阶段 1 · 理解（Understand）
复述需求 / 目的 / 受众
确认基调和流派
列出硬约束（技术栈、浏览器兼容、a11y）
阶段 2 · Junior Pass（假设占位，快速出骨架）
用占位文案（Lorem Ipsum 或真实类似文案）+ 占位图片（Picsum/Unsplash 链接）
跑通结构、栅格、主要交互
诚实标注每一块占位（<!-- TODO: 真实文案 -->）
让用户看到方向再继续
阶段 3 · Full Pass（补内容、调细节）
补真实文案（问用户要 或 用 huo15-openclaw-brand-protocol 抓品牌资源）
替换真实图片（需要下载时返回 CLI 命令，不用 child_process）
微调字号、行高、字距、间距、阴影层级
加动效
阶段 4 · 自验证（Self-Verify）

返回一条 Playwright CLI 命令让用户执行（延续 enhance 插件"禁 child_process"铁律）：

npx playwright-core screenshot <URL 或 file:///绝对路径> ~/verify.png --viewport-size=1440,900


然后由用户或 huo15-openclaw-design-critique 对截图打分。

阶段 5 · 可选 · 评审（Review）

调用 huo15-openclaw-design-critique 做 5 维评分 + Keep/Fix/Quick Wins。

七、产出清单（每次交付必含）
代码文件（index.html / App.tsx / page.vue），可直接运行
3 行设计说明：
流派（从 §三 五选一）
关键设计选择（字体 / 主色 / 动效三选一突出）
差异点（用户会记住什么）
（可选）截图验证 CLI 命令
（可选）已知限制（占位图未替换 / 未测移动端等）
八、与其他 huo15 技能的分工
能力	归属技能
Web UI / HTML 原型 / 落地页	本技能
设计方向选择（多流派对比）	huo15-openclaw-design-director
品牌规范抓取 + brand-spec	huo15-openclaw-brand-protocol
设计评审 5 维打分	huo15-openclaw-design-critique
PPT 演示稿	huo15-openclaw-ppt
Word / PDF 文档	huo15-openclaw-office-doc
九、触发词
做网站 / 做落地页 / 做官网 / 做仪表盘
做组件 / 做 React 组件 / 做 Vue 组件
HTML 原型 / 页面原型 / 前端原型
美化页面 / 优化 UI / 前端设计 / Web 设计
做海报 / 做详情页 / 做信息图 / 产品页
十、版本历史
v1.0.0（当前 · 2026-04-23）：初始版本。对齐 Anthropic frontend-design 核心理念（BOLD 美学方向 + 反 AI slop），本土化中文改写，加入 5 流派选择、8 条硬红线、Junior/Full 两趟渲染工作流、Playwright 自验证 CLI、与火一五其他技能的分工边界。

技术支持： 青岛火一五信息科技有限公司

Weekly Installs
10
Source
skills.volces.c…zhaobod1
First Seen
3 days ago