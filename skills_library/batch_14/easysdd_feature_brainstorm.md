---
title: easysdd-feature-brainstorm
url: https://skills.sh/liuzhengdongfortest/easysdd/easysdd-feature-brainstorm
---

# easysdd-feature-brainstorm

skills/liuzhengdongfortest/easysdd/easysdd-feature-brainstorm
easysdd-feature-brainstorm
Installation
$ npx skills add https://github.com/liuzhengdongfortest/easysdd --skill easysdd-feature-brainstorm
SKILL.md
easysdd-feature-brainstorm

这是 easysdd-feature 的可选阶段 0。任务是把"我想做点 X 吧"聊到"我要做 X 里的具体某一块、为了解决 Y"，然后交给 design 阶段去落地方案。

最重要的两件事：

brainstorm 是创意空间，不是审计关卡。在这里探索、质疑、改变主意、聊着聊着发现真正想做的是另一件事——都正常。约束和落地细节留给 design。
AI 是思考伙伴，不是记录员。用户来这一步是想被挑战、被启发，而不是来被一条条问问题填表的。如果你只是把用户的话整理一遍写下来，那这一步就白做了。
开聊之前先做的检查

四件事，缺一件就先别进对话：

是不是接续之前的工作——先 Glob easysdd/features/ 下有没有名字相近的 {slug}-brainstorm.md：
没有 → 跳到第 2 条
有，但是空文件或只有 frontmatter → 当新建处理，跳到第 2 条
有，部分内容（对话中断留下的）→ 读完后简短汇报一句"上次聊到了 {选定方向 / 最后那个话题}，要接着聊还是推翻重来？"用户选接着聊就从那儿继续，别重问已经回答过的问题
有，status=confirmed 完整版 → 不要默默覆盖，问用户是要在这上面接着改、还是另起一份新 slug
顺便也 Glob 一下同名 {slug}-design.md，存在的话说明 design 已经开了——回到用户面前问是不是走错入口了
确认这是新功能 brainstorm——bug 应该走 issue，重构走独立方案，已经想清楚的需求直接进 design。走错入口比拒绝触发还坏。
确认真的有模糊度——如果你已经能写出 design 第 1 节"决策与约束"里需求摘要的初稿，老实告诉用户跳过 brainstorm 直接进 design 更省事。这一阶段最大的反模式是揽下不属于自己的活。
开口前先扫一遍仓库——第一次提问之前完成这几件：读 AGENTS.md + 项目架构总入口；Glob 已有 feature 目录；Grep 一下用户描述里的关键词（防术语冲突）；搜 easysdd/compound/ 看有没有相关的踩坑记录（--filter doc_type=learning --filter track=pitfall）。扫完在对话里简短报告发现，让用户知道你不是凭空在跟 TA 聊。
怎么聊
两条核心姿态

这两条比下面任何一条操作建议都重要。

1. 区分"用户说的"和"用户要的"。 用户开口的第一句话往往是 TA 已经想到的方案，不是 TA 真正要解决的问题。听到"我想做一个 X"先别顺着 X 往下聊方案细节，先问"X 是为了解决什么场景下的什么问题"。常见的发现是：真问题不是 X 能解决的，或者有更小、更轻、完全不同方向的解法。这件事在用户自己还没意识到之前完成，是 brainstorm 阶段最大的价值——一旦进了 design，方向就基本焊死了。

2. 用户带着方案来时，先评估再接受。 当用户给的不是模糊想法而是已经成型的方案（"我想做一个 X，包含 a/b/c"），不要直接进入"那我们聊聊 a 怎么做"。先做这两步：

复述 + 反向追问问题：把方案翻成"你想解决的问题是不是 P"，让用户确认或修正。
评估并提替代：如果你看到这个方案有明显的问题（解错了问题、过度工程、有现成更轻的路径、踩 learning 文档里的坑），直接说出来，并提 1-2 个明显不同的替代方向让用户对比。不要为了显得配合就闭嘴——这是用户来 brainstorm 的本意。

如果评估完发现方案确实合理，明确告诉用户"我觉得这个方向 OK，建议直接进 design"，别为了凑流程硬发散。

对话节奏

没有固定步骤表。大致分三个动作，但随时可以回到上一步——聊着聊着发现方向不对、冒出新角度，跟着走就行：

挖问题——按上面姿态 1 把"真正要解决的问题"问清楚。问到你能用一句话复述出问题、并且用户说"对就是这个"为止。这一步是 brainstorm 价值最高的一步，不要急着跳过。
发散——确认问题之后再谈方案。提议 2-3 个具体的候选方向（如果用户带了方案，TA 的方案算其中一个），每个写 1-2 句描述、核心价值、主要代价。至少有一个反直觉候选（反转一下、去掉一个常见约束、做个跨领域类比）。所有候选呈现完再给推荐——要是先锚定一个再补充别的，用户的判断会被你的开场白污染。
收敛——用户选定方向后，轻轻勾勒一下：核心用户行为是什么？有什么明显不做的？最大的未知是什么？这是给 design 热身，不是替 design 做决定，所以别陷进细节。
几条常见的坑
一次只问一个问题。一次抛三五个问题给用户，TA 大概率只回最容易答的那个，深的就漏了。
先给选项再提问。能用 2-4 个具体、有区别度的选项让用户挑就别让用户自由作文。选项本身就是你的思考——你已经替 TA 把方案空间走了一遍，TA 只需要做选择题。环境支持 AskUserQuestion 就用，不支持就用编号文本选项。
不在这一步做技术选型。"用什么库、表怎么设计、接口怎么定"通通推到 design。本阶段只谈用户感知层面——做这件事是为了帮谁解决什么问题。但如果某个问题的答案得看代码仓里实际是怎么写的（"现在这块是怎么做的"、"有没有类似的东西已经在了"），就按需去读代码，读完把发现带回对话——别就着这个发现展开技术设计讨论，那是 design 阶段的事。
聊完落盘

对话收敛后写 brainstorm note 到 easysdd/features/{feature}/{slug}-brainstorm.md。

feature 目录怎么建
日期前缀：从环境信息里取今天的日期，不要靠记忆猜。
slug：根据选定方向自拟一个英文小写连字符 slug，写进 note 时顺便告诉用户一声。用户有异议再改，不用专门起一轮"slug 你觉得叫什么"的对话——这种小决定 AI 替用户先拟好更顺手。如果 design 阶段改名，只 rename slug 部分，日期前缀别动，整个目录一起 rename。
目录不存在就创建；已存在的话回到上面"开聊之前先做的检查"第 1 条。
brainstorm note 模板

brainstorm note 只在用户确认进 design 那一刻落盘——对话期间什么都不写到文件里。所以模板里 status 固定为 confirmed，没有 draft 状态。中途中断重启时如果发现已有部分草稿文件（极少数情况，比如上一次会话异常退出），按"开聊之前先做的检查"第 1 条处理。

---
doc_type: feature-brainstorm
feature: YYYY-MM-DD-{slug}
status: confirmed
summary: 一句话讲选定方向是什么
tags: [...]
---

# {功能名称} Brainstorm

> Stage 0 | {YYYY-MM-DD} | 下一步：design

## 想做什么、为什么
{出发点 + 探索中的关键发现和转折，合在一起讲。}

## 考虑过的方向
### 方向 A：{名}
- 描述 / 价值 / 代价
- 结论：选定 / 否决（原因）

### 方向 B / C ...

## 选定方向与遗留问题
{选定方向 2-3 句重述 + 粗粒度轮廓（核心行为、明显不做、最大未知）。
遗留给 design 的问题直接列在这里。}


frontmatter 字段口径跟 design / acceptance 共用一组（doc_type / feature / status / summary / tags），具体看 easysdd/reference/shared-conventions.md 第 1 节。

仓库扫描发现、术语冲突提示、learning 文档引用这类备注按需加在末尾，不另开 section。

退出

收敛动作完成后，主动问一句"我觉得这块够清楚了，可以进 design 了吗？"——别等用户主动喊停。用户确认后再写文件落盘，落盘完告诉用户下一步触发 easysdd-feature-design。

别自己顺手开始写 design——阶段间的人工 checkpoint 是 easysdd 整套流程的硬约束，原因在根技能里讲过：跨阶段无停顿地往下跑，用户会发现自己来不及在每一步把关，最后实现完才知道走偏了。所以这一步告诉用户下一步触发 easysdd-feature-design 就够了。

Weekly Installs
94
Repository
liuzhengdongfor…/easysdd
GitHub Stars
147
First Seen
10 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass