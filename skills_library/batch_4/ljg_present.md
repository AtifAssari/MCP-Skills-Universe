---
title: ljg-present
url: https://skills.sh/lijigang/ljg-skills/ljg-present
---

# ljg-present

skills/lijigang/ljg-skills/ljg-present
ljg-present
Installation
$ npx skills add https://github.com/lijigang/ljg-skills --skill ljg-present
SKILL.md
ljg-present: 演讲铸造器

把文本削成节拍/口号，把 PPT 降为节拍器/色块，把舞台还给讲的人。

两种模式（mode flags）
Flag	名称	何时用
(默认)	高桥流	内容含蓄、思辨、想做"单字节拍"、奶白底墨字
-s	标语流	内容口号化、宣言式、想要色块冲击、ultra-bold、有"休止"节奏
模式分发逻辑

接到调用时按以下顺序判断：

用户输入含 -s / 标语流 / slogan / manifesto / 宣言体 / 红黑流 / big studios / BIG 风 → 走标语流
否则 → 走高桥流（默认）
模式一：高桥流（默认）

把文本削成节拍——一页一个关键词，字撑满屏。

这不是什么
不是做 PPT——高桥流反 PPT
不是摘要——摘要是缩写，高桥流是节拍
不是提纲——提纲讲究流畅，高桥流讲究跳跃
不是装饰秀——一张图都不放，一个图标都不放
这是什么

高桥流的源头：2001 年日本 Ruby 程序员高桥征义，在没有专业演示工具的场合，用 HTML 写了几页超大字体的幻灯片。意外走红，成了一种流派。

三条铁律，去掉任何一条都不是高桥流：

一页一个思想单元——不是一页一段话，是一页一个"此刻该敲响的那个词"
字大到撑满屏幕——视觉上屏幕只剩这几个字，没有留白作为"呼吸"，字本身就是呼吸
无图、无表、无装饰——演讲者是主角，PPT 是节拍器。节拍器不需要花样
核心哲学

PPT 是节拍器，不是信息载体。

传统 PPT：信息密集，观众读屏幕，演讲者念 PPT。 高桥流：信息稀疏，观众听演讲，PPT 打点。

这意味着提炼的每一页不是"缩写"，是演讲者口述中"此刻听众脑中该闪过的那个词"。

提炼规则（高桥流）
提炼 ≠ 摘要
摘要（错）	提炼（对）
500 字压成 100 字	500 字压成 "作者真正在钉的那颗钉子"
保留信息	保留刻度
连续过渡	并列跳跃
让人省时间阅读	让人在演讲时恰好想到这个词
六步提炼法

第一步：通读找钉子 — 作者真正在钉的那颗钉子是什么？1 个，最多 3 个 — 钉子是"他反复回到的那个点"，不是标题不是主题句

第二步：排出节奏 — 围绕钉子，排 8-24 个"思想刻度" — 每个刻度是听众脑中"啪"的一下的那个瞬间

第三步：压字到 ≤ 12 字 — 能单字就单字 — 能短语就短语 — 能名词就不要动词 — 能名词就不要句子

第四步：剥修饰与连接 — 去形容词（除非形容词就是刻度本身） — 去"因此/所以/但是/然而"——这些是口述的职责 — 去"我们/你们/大家"——高桥流没有"我们" — 去感叹号、问号——视觉不喊，让演讲者去喊

第五步：检查跳跃感 — 相邻两页要有"啪啪"的错位感，不是"滑滑"的连续感 — 单页能独立成立才算合格

第六步：保留"收束页" — 最后一页是收束，不是总结 — 一个字、一个符号、或一个反问式短语

提炼举例

原文（160 字）：

我们总以为自己是在选择，其实我们大部分时间在默认。你选了这家公司，是因为真的比别家好吗？还是因为 HR 先找到你？你选择了每天起床的时间，是因为想清楚了吗？还是因为手机闹钟设在那里？默认是一种选择。但它是别人替你做的选择。想活得不像别人，第一步是意识到自己正在被默认。

高桥流提炼（12 页）：

1.  选择
2.  大部分时间
3.  在默认
4.  默认 ≠ 选择
5.  谁替你选的
6.  HR 先找你
7.  闹钟先响
8.  别人替你选
9.  第一步
10. 意识到
11. 正在被默认
12. 醒


注意：最后一页「醒」，一个字。这是收束。

高桥流视觉规范
底色：和紙奶白 #F7F3E9
主字：墨黑 #1A1A1A
点睛色：朱砂红 #C03C28（仅用于收束页或作者要强调的那个词）
字体链："PingFang SC", "Heiti SC", "STHeiti", -apple-system, sans-serif
无图、无图标、无插图、无表格、无边框、无过渡动画
高桥流调用流程
获取内容（URL → WebFetch / 文件 → Read / 粘贴 → 直接用）
按六步法提炼为 JSON 数组：
[
  {"text": "选择", "emphasis": false},
  {"text": "大部分时间", "emphasis": false},
  ...
  {"text": "醒", "emphasis": true}
]

Read assets/takahashi_template.html，把 {{SLIDES_JSON}} 替换为 JSON 字符串，{{TITLE}} 替换为主题（≤ 20 字）
写文件到 ~/Downloads/{name}-高桥流.html
报告路径，告知翻页键 → ← Space F Home End
模式二：标语流（-s）

把文本铸成口号——色块大字、ultra-bold 错位、休止页打节拍。

参考审美：Felipe Franco / BIG STUDIOS 的 manifesto 演讲（"Is it AI or is it ART?"）。

这不是什么
不是高桥流——高桥流是单字节拍，标语流是整句宣言
不是 deck-style——不是企业 PPT 那种规整版式
不是花哨——色块再多也只有四种底（黑/红/黄/白）
这是什么

广告业 manifesto 的视觉语言：

整篇一个主题色——根据文本气质选定，一篇只有 ≤3 种色彩
left-aligned 舞台美学——文字左对齐起始，靠超大字号自然撑满，不机械居中
超大字撑屏——ultra-bold sans-serif，单字 64vmin、长句 15vmin
多行错位——一句话拆成 2-4 行，每行独立缩进
关键词换色——hl 仅在 theme 页生效（accent 页本身就是高亮）
emphasis 切换节奏——每 3-5 页一张 accent 底，靠色块跳跃打节拍（不再用空白休止）
letter-spacing 紧凑——-0.05em 给 ultra-bold 应有的挤压感
页脚冷标签——左下页码、右下副标题，OCR 风字体
核心哲学

标语流是色块时代的演讲。

传统 PPT 用图表填满。 高桥流用单字打鼓。 标语流用色块开炮。

每一页是一句口号，不是一个词；整篇只有一个主题色 + 一个反差色——不是逐页换色的杂耍，而是一种气质贯穿到底。节奏来自 theme 与 emphasis 的色块跳跃——不需要空白页，色块本身就是节拍。

提炼规则（标语流）
提炼 ≠ 摘要 ≠ 高桥流
摘要	高桥流	标语流
信息密	单词节拍	完整断言句
流畅段落	词与词错位	句与句错位+色块切换
让人读	让人想到	让人脱口而出
────	"选择"·"默认"·"醒"	"默认是别人替你做的选择。"

最关键的差异：高桥流的每一页是"词"，标语流的每一页是"完整能站住的断言句"。 拿掉拆词的冲动——不要 "结构 / 决定 / 行为" 这种把一句话拆三页，应该是 "结构决定行为。" 一句话一页。 能拆开是因为前后呼应做节拍——但每一片仍然要自成一句（哪怕只是 SVO 三字结构 "我·选·路"）。

五步提炼法（标语流）

第一步：找到那个 manifesto — 整段文字背后是哪句"我要钉死的话"？ — 不是"中心思想"，是演讲者要喊出来的那句

第二步：选定主题色——按文本气质，从三选一定一篇基调 — black：沉思 / 论证 / 解构（默认 accent: red） — red：宣言 / 号召 / 情绪（默认 accent: black） — yellow：反讽 / 警觉 / 批判（默认 accent: black） — 整篇只用 theme + accent 两个底色，不再逐页换

第三步：排成完整断言句（6-20 页） — 每页是一句能独立站住的完整断言——不是词，不是标签，不是序号 — 测试：把这一页单独说出口，是不是一个完整的话？是 → 合格；不是 → 重写 — 长口号可以拆成 2-4 行错位排版，但每一行也要是有意义的语言单元（不是把一个词砍成两半） — 不要"过渡句"——只要"震击句"

对比示范（同一文本三种提炼）：

错（高桥流式拆词）	对（标语流的完整句）
「四根线」（词组）	「四根线撑起了整本书。」
「1·可能性空间」（标签）	「世界不是已定的链。」
「世界 / 不是机器」（拆两页）	「世界不是机器。」（一页一句）
「在树上 / 砍 / 一刀」（拆三行）	「选择，是在树上砍一刀。」
「我们 / 永远 / 在墙外」	「我们永远在自己的黑箱里。」
「姿势」（单字残句）	「这是看世界的姿势。」

例外：真正的单字震击页（如收束「醒」「换」「YOU」）允许 ——但全篇至多 1 张，且这个字本身在中文里能表达完整意图。

第四步：标记 emphasis 页 — 默认页是 theme 底（多数页面） — emphasis: true → accent 底，用于情绪高潮、断言、转折点（每 3-5 页一张，整篇 4-8 张） — emphasis 与默认页的色块跳跃就是节拍本身，不需要额外的空白休止

第五步：关键词点染 — 仅在 theme 页内使用 inline hl: true — emphasis 页不允许 inline 高亮——整页就是高亮 — 一句口号最多 1 个高亮词

提炼举例

原文（120 字）：

工具变快了，故事没跟上。一台 AI 一秒生成一百张广告。但这一百张广告里没有一个能说出"为什么"。速度没有故事就是噪音。规模没有意图就是污染。艺术家给世界的不是工艺，是意义。AI 给不了你这个。

标语流提炼（10 页，theme=red 宣言主题）：

{
  "theme": "red",
  "title": "Is it AI or is it ART?",
  "subtitle": "VACAT 2025 / Felipe Franco",
  "slides": [
    {"emphasis": true, "lines": [
      {"chunks": [{"t": "AI"}], "indent": 0},
      {"chunks": [{"t": "or"}], "indent": 1},
      {"chunks": [{"t": "ART?"}], "indent": 0}
    ]},
    {"lines": [
      {"chunks": [{"t": "Speed without "}, {"t": "story", "hl": true}, {"t": " is noise."}], "indent": 0}
    ]},
    {"lines": [
      {"chunks": [{"t": "100 ads."}], "indent": 0},
      {"chunks": [{"t": "0 reasons."}], "indent": 1}
    ]},
    {"emphasis": true, "lines": [
      {"chunks": [{"t": "Artists"}], "indent": 0},
      {"chunks": [{"t": "give"}], "indent": 1},
      {"chunks": [{"t": "Meaning."}], "indent": 0}
    ]},
    {"lines": [
      {"chunks": [{"t": "AI gives "}, {"t": "tools", "hl": true}, {"t": "."}], "indent": 0},
      {"chunks": [{"t": "Not "}, {"t": "myths", "hl": true}, {"t": "."}], "indent": 1}
    ]},
    {"lines": [
      {"chunks": [{"t": "Intention"}], "indent": 0},
      {"chunks": [{"t": "matters"}], "indent": 1}
    ]},
    {"emphasis": true, "lines": [
      {"chunks": [{"t": "Who"}], "indent": 0},
      {"chunks": [{"t": "signs"}], "indent": 1},
      {"chunks": [{"t": "the canvas?"}], "indent": 2}
    ]},
    {"emphasis": true, "lines": [
      {"chunks": [{"t": "You do."}], "indent": 0}
    ]}
  ]
}


注意：theme=red 时，默认页是红底白字、emphasis 是黑底白字、hl 在红底上是黑色字。 整篇视觉就是「红主调 + 黑反差 + 白字」三色，干净。色块切换本身就是节拍，emphasis 与默认页交替出现产生跳跃感。

标语流视觉规范
色板（仅 4 色）
--c-black:  #1A1A1A
--c-red:    #E93323
--c-yellow: #FFD400
--c-white:  #FFFFFF

主题映射（一篇只用 ≤3 色）
theme	默认页	emphasis 页	hl 色（仅 theme 页）
black 沉思	黑底白字	红底白字	红色
red 宣言	红底白字	黑底白字	黑色
yellow 反讽	黄底黑字	黑底白字	红色

主题选择决策：

内容是论证 / 解构 / 思辨 → black
内容是宣言 / 号召 / 情绪 → red
内容是反讽 / 警觉 / 批判 → yellow
字体栈
"Helvetica Neue", "Arial Black", "Inter", "PingFang SC", "Heiti SC", -apple-system, sans-serif
font-weight: 900
letter-spacing: -0.03em

字号自适应

按本页"最长那一行"的字符数（CJK 字符按 1.8 计权）自动分档：

档位	字符数	字号
single	≤ 2	64vmin
short	3-6	42vmin
medium	7-14	26vmin
long	15-26	15vmin
xlong	27+	10vmin

多行页自动降一档。字号比早期版本上调约 30%——VACAT 级别的暴力撑屏感。

排版
内容区域 padding 6vmin 7vmin（贴近边缘，让大字有撑满感）
left-aligned 起始——文字左对齐，靠超大字号自然占据视觉，不机械居中
行内 indent 0/1/2 制造错位
letter-spacing -0.05em——ultra-bold 应有的字字挤压感
line-height 0.95——多行紧凑
文字垂直方向：居中
页脚：左下页码 + 右下副标题，13px monospace，opacity 0.5
标语流 JSON Schema
{
  "theme": "black|red|yellow",          // 主题色（必选，决定整篇调性）
  "title": "演讲标题（浏览器 tab）",
  "subtitle": "副标题/品牌（页脚右下，可选）",
  "slides": [
    // 默认 theme 页
    {
      "lines": [                         // 1-4 行
        {
          "indent": 0,                   // 0/1/2 缩进档（错位感）
          "align": "left|center|right",  // 可选，默认 left
          "chunks": [                    // 行内片段
            {"t": "句子前段"},
            {"t": "高亮词", "hl": true}, // 仅 theme 页生效
            {"t": "句子后段"}
          ]
        }
      ]
    },
    // emphasis 页（accent 底色，整页就是高亮，不允许 inline hl）
    { "emphasis": true, "lines": [...] }
  ]
}


字段省略约定：

不写 emphasis = 默认 theme 页
emphasis 页内 chunks[].hl: true 会被忽略（CSS color: inherit）
标语流调用流程
获取内容（URL → WebFetch / 文件 → Read / 粘贴 → 直接用）
按五步法提炼为标语流 JSON（按上面 schema）
Read assets/slogan_template.html
替换占位符：
{{TITLE}} → JSON 的 title
{{SUBTITLE}} → JSON 的 subtitle
{{THEME}} → JSON 的 theme（black|red|yellow）
{{SLIDES_JSON}} → JSON.stringify(slides)
写文件到 ~/Downloads/{name}-标语流.html（{name} 中文，去标点，≤ 20 字）
报告路径，告知翻页键 → ← Space F Home End
标语流品味准则
一篇一个气质——theme 只选一个，整篇走一种调子，不混搭
每页一句完整话——能独立站住的断言、定义、问句、对照——不是词组，不是标签
emphasis 是节拍器——每 3-5 页一张 accent 底，色块跳跃就是节奏
单字震击至多 1 张——全篇至多 1 张单字页（如收束的「换」「醒」），不是每个段落都给一张
错位不强迫——三行不一定都缩进，错落比对齐重要
高亮一句一个——不要在一句里高亮两个词
页脚保留——页码和副标题别去掉，那是品牌的冷气
左对齐不居中——VACAT 美学的灵魂；字大到自然平衡，不机械居中
开场页有重量——第一句话就要立得住，最好是 manifesto 本句或核心问句
标语流禁区
不放图片/图标——色块就是图
不用过渡动画——硬切
不要项目符号——manifesto 没有 bullet
不要空白休止页——节奏靠色块跳跃（emphasis 与默认页交替）就够了
不要副标题字过大——页脚 13px，气场不能抢主标
不在 emphasis 页用 inline hl——emphasis 整页就是高亮，再 hl 就乱了
不混用多个 theme——一篇一个气质，不切换
不拆词——「世界 / 不是机器」不行，要写「世界不是机器。」
不序号标签——「1·可能性空间」「第一根」这种序号式排版不行，要写完整断言
不残句——「姿势」「四根线」（无主谓宾或无表意结构）不行，要写「这是看世界的姿势。」全篇至多 1 张单字震击页例外
开场页要有重量——开场不能是「四根线」这种悬空词组，要是「弗里茨整本书只钉一句话。」「世界不是机器。」这种立刻能站住的断言或问句
模式选择决策树
用户输入 →
├─ 含 -s / 标语流 / slogan / manifesto / 宣言体 / 红黑流 / big studios?
│   是 → 标语流
│   否 → ↓
├─ 内容偏论证、思辨、内省 → 高桥流
├─ 内容偏宣言、口号、情绪冲击 → 默认走高桥流，但提示"也可用 -s 标语流"

中文默认

两种模式都默认输出中文。除非原文是英文且用户要求保留英文。

通用交互（两种模式一致）
→ Space Enter j：下一页
← k：上一页
Home/End：跳首末
f/F：全屏切换
触屏左右滑：翻页
点击右半屏：下一页；点击左半屏：上一页
Weekly Installs
470
Repository
lijigang/ljg-skills
GitHub Stars
3.9K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn