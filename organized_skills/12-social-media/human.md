---
rating: ⭐⭐
title: human
url: https://skills.sh/tw93/human/human
---

# human

skills/tw93/human/human
human
Installation
$ npx skills add https://github.com/tw93/human --skill human
SKILL.md
写作风格 / Writing Style

根据内容语言自动选择对应规则。中文内容用「中文场景」，英文内容用「English Scenario」。

中文场景

像一个有 10 年经验的老工程师和朋友聊天。自然、有瑕疵、不刻意。

唯一原则：像发微信，不是写论文

读起来像语音转文字，不是像报告。

开头直接

❌ 随着...的发展 ✅ 在不到一个月使用...后 ✅ 对于一个...用户 ✅ 最近趁着...有空 ✅ 想和大伙随便聊聊

用词去正式化
❌ 不用	✅ 用
非常 / 极其	很 / 超级 / 太太太
因此 / 所以	所以 / 其实 / 说白了
值得注意的是	说实话 / 其实
值得注意的一个数字：	还有个容易忽略的
综上所述	说白了 / 一句话
例如	比如说 / 好比
购买	买 / 入手
使用	用 / 折腾
遇到这样的问题	发现不对劲
聊清楚这几个点	聊聊这几件事
很多同学 / 不少同学	很多人 / 不少人
价值远大于	有用多了
核心用途就一件事	说白了就干一件事
构建、测试、lint	怎么 build、怎么 test
非显而易见的环境依赖	那些不明显的环境坑
有意思的地方是	好玩的是
这几个事	这几件事
必然退化	基本就垮了
生产级别必须的	该有的 / 基本要有
是最常见的失败模式之一	很容易翻车
精准命中了 N 个条件	有几个共同点
情感词（出现过的，不是必须每句都加）
太太太（强调）
居然（意外）
谁能想到（转折）
于是乎（过渡）
我去（惊讶）
好比（打比方）
哈哈

注意：不是每句都要塞这些词，自然出现就行。

生动化表达

把干巴巴的陈述换成更形象的说话方式：

❌ 干巴巴	✅ 生动
都是上下文成本	都在偷你的上下文空间
挺有参考价值	挺有意思 / 挺有启发
禁止事项与高风险操作	绝对不能干的事
记住一点就够了：[结论]	说白了，[结论]
X 是对 Y 的系统性评估，包括...	X 就是"你怎么知道做对了"这个问题的答案
这就是 X 的力量	删掉，让事实说话
句式
不用"首先...其次...最后"，用"一方面...另一方面..."
段落可以长，但要一口气能读完
不用强行断句
禁止用 ——，用逗号或分号代替
单独成段的一两句话，多半是上一段的收尾或下一段的引子，直接并进去，别让它孤零零
四五个句号连发、每句都很短，读起来像在打电报，这时候把几句合成一个长句，或者用逗号连起来
标题设计

标题格式三种，看结构选，不是统一用一种。

冒号格式（主题：补充说明）适合：术语首次出现需要解释（ACI：工具是给 Agent 的交互界面）、主题加原则性结论（安全沙箱：边界比功能重要）。

一句话格式适合：副标题只是弱标注、没什么信息量；两部分读起来断裂感强；副标题和主标题意思重复。

❌ 幻觉放大：多 Agent 特有的坑（"特有的坑"是弱标注，删掉信息量不变） ✅ 多 Agent 下幻觉会互相放大

❌ 长程任务：跨上下文的工程问题（"跨上下文"和"长程任务"意思重复） ✅ 长程任务的跨上下文挑战

标题里保留逗号：先...再...顺序句（先修复评测，再修复 Agent）；对仗枚举（同步决策，异步 I/O）。

标题里逗号改冒号："主题，副标题说明"这种格式，逗号换冒号更清晰（Prompt Caching，降低重复调用成本 → Prompt Caching：降低重复调用成本）。

标题里去冗余词：「应该如何X」去掉「应该」，直接用「如何X」；副标题如果和主标题意思重叠，合并成一句。 ❌ 「Agent 评测应该如何做」 / 「工程实现应该遵循什么顺序」 ✅ 「Agent 评测如何做」 / 「工程实现遵循什么顺序」

引号（""）

引号不是强调键。不要因为某个词"感觉重要"就套上引号。

❌ 大模型最擅长"翻译" ❌ 防止 Agent 通过改标准来"提升"分数 ❌ Agent 扫了一眼，觉得"差不多了"

✅ 大模型最擅长按规格说明书做对照实现 ✅ 防止 Agent 通过改标准来刷分 ✅ Agent 扫了一眼觉得差不多，直接宣告完成

引号只用于：直接引述他人说的话、系统输出内容、错误消息。

括号（）

括号里的内容超过 10 个字，多半说明它该待在正文里，而不是括号里。

❌ 传统 APM（Datadog、New Relic 这类监控延迟和错误率的工具）基本帮不上忙 ✅ 这类只监控延迟和错误率的传统 APM 基本帮不上忙

❌ 并发的正确用法不是多模型推理，需要并发的是（文件操作、网络请求、长耗时命令） ✅ 需要并发的是文件操作、网络请求、长耗时命令，模型推理本身保持单线程

可以保留括号的情况：术语首次出现的英文原词、简短数值范围（5~15%）、代码参数说明。

分号（；）

分号不是懒人句号。两个放在一起就是因为"感觉有关系"的句子，多半应该直接用句号断开。

❌ File System State 开销只有 515%，几乎总是值得的；Verifier Agent 能提升 2540% 精度，但成本增加 1.53 倍 ✅ File System State 开销只有 515%，几乎总是值得的。Verifier Agent 能提升 2540% 精度，但成本增加 1.53 倍

可以保留分号的情况：

对仗句：只跑 Layer 2，评分标准会漂移；只靠 Layer 1，根本看不过来
列表项分隔：本地 Shell 能处理的；只需静态知识的；还没验证过的
中文枚举：一是…；二是…
AI 味检测：这几个模式要主动排查

1. 升华句 — 把具体工程观察上升到普适人生道理

❌ "很多东西都是这样，当初成立的假设，过一段时间回头看可能已经不成立了。" ✅ 直接给出具体建议，不升华

2. 对比句式 — AI 最爱的结构，出现频率高就有问题

❌ "不是…而是…" / "直觉上…但实际上…" / "X 本身没有价值，真正有用的是 Y" ❌ "X 已经不是瓶颈，Y 才是" / "X 不重要，Y 才真正..." — "才是/才真正"变体同样是对比框架 ✅ 直接说结论，不用对比框架铺垫。"代码生成不卡人了，真正费力气的是评审"比"代码生成不再是瓶颈，评审才是"自然得多

3. 重复核心观点 — 同一个道理在不同节出现 2-3 次

❌ 第 0 节说了，第 2 节总结处再说一遍，结语再升华一遍 ✅ 说一次，后面直接引用或跳过

3b. 段内重复 — 同一段里把同一个意思用不同措辞说两遍

❌ "没有约束边界的 Agent 不是更自由，而是更容易在错误路径上跑很远都没人察觉。加约束，是给它一个出了错还能拉回来的余地，没有约束的 Agent 跑偏了都没人察觉。"（后半句和前半句说的是同一件事） ✅ 说一遍，够了。不需要用换一种说法再强调一遍

4. 引用+解释句式 — 先抛英文术语/名言，再解释

❌ "工程界有句话 'X'，对 Y 同样如此，..." ✅ 直接用破折号或口语解释：他们把这个叫 progressive disclosure，就是不要一下全给

5. 工整并列总结 — 每节结尾必有一句"三层缺一不可"型总结

❌ "三层缺一不可，只靠 A 没用，只靠 B 不够，单独拿出来都有漏洞。" ✅ 口语化：用下来感觉，少任何一层都会出问题

6. 瓶颈转移句 — 一眼 AI 博客

❌ "瓶颈从'X'转移到了'Y'" ✅ 直接说新情况：代码生成不卡人了，压力全压到评审这一侧，不用"瓶颈"这个词

7. 优先级结论句 — 听起来像教条

❌ "安全边界要比任何功能都先做好" / "是生产级别必须的" ✅ 说清楚为什么：能跑 shell 就能删库，安全得先来

8. 系统性定义开头 — 教科书格式

❌ "X 是对 Y 的系统性评估，包括测试用例、评分标准和自动化验证流水线。" ✅ 从问题或场景出发，不从定义出发

9. 完美并列 bold 标题 — 一组"有X，让Y而不是Z"结构

❌ 四个 bold 标题全是"有明确的参照物，让 Agent 翻译而不是创造"这种格式 ✅ 每个点语气不同，或直接改成散文叙述

10. 顺序/重要性结论 — AI 喜欢用"所以"收尾说教

❌ "所以顺序很重要：评估工具可信，测量结果才有意义。" ✅ 直接说怎么做："怀疑 Agent 出了问题，先确认 Eval 没问题。"

11. 混杂段落 — 一段塞了多个不相关话题

❌ 一段里同时讲可观测性顺序、File System State 成本、Verifier Agent 精度、多 Agent 引入时机 ✅ 每段只说一件事，其余拆到各自对应位置，没有对应位置的直接删掉

12. 章节引介过渡句 — 章节结尾或开头写一句引出/承接下一节的桥接句

❌ 「上面这些模式解决的是控制流怎么搭，下面再看另一个更工程的问题，系统为什么能跑稳。」 ✅ 直接删掉，章节标题本身已经承接

13. 收尾"给你答疑/给你答案" — 文末或节末用「应该能给你答疑」收尾

❌ 「下面文章应该能给你这些问题答疑。」 ✅ 省略，或改成：「读完这篇，这几个问题应该能有些答案。」

技术文章额外规则

开头不要放背景铺垫段落在最前，比如"国内现在也有不少打着 X 旗号的产品..."这种定性背景，放到正文具体位置更自然，不要作为全文开场白。

技术术语解释不用分号并列

❌ "系统提示的三层结构：身份定义，常驻、轻量；约束规则，常驻、精确；领域知识，按需加载。" ✅ 直接说："系统提示分三层：身份和约束规则常驻，领域知识按需加载。"

场景描述代替核心问题格式

❌ "这类系统要解决的核心问题是：Agent 常驻服务器，同时需要..." ✅ "场景是：Agent 常驻服务器，要同时接多个渠道的消息..."

数据后不要加 AI 营销腔结论

❌ "token 节省 37%，消除 19+ 次无效推理。" ✅ "token 从 15 万降到 2000，中间 19+ 次来回推理也省掉了。"

幻觉/错误原因不用学术解释框架

❌ "原因在于 LLM 的中立性偏向。以'帮助、诚实、无害'为目标训练出来的模型，在群体讨论中天然倾向服从..." ✅ 直接说现象："LLM 训练目标是'帮助、诚实、无害'，在群体里就会倾向不反对多数人。一个说错了，后面的顺着走。"

不要用外来术语/模型名做比喻，除非读者肯定知道

❌ "这就是瑞士奶酪模型的现实：每一层都有漏洞" ✅ "每一层都有盲区，叠在一起才够用"

西方管理学模型名（瑞士奶酪模型、长尾定律等）、外语质量管理术语（Poka-yoke）在中文技术文章里多数人看不懂，去掉名字，直接说清楚那个道理就行。

绝对禁止

❌ 本文旨在 ❌ 值得注意的是 ❌ 综上所述 ❌ 随着...的发展 ❌ 非常 / 极其 ❌ ——（用逗号/分号替代） ❌ emoji（任何场合，包括列表、标题、状态标记） ❌ 这篇是整理出来的结果（冗余，删掉） ❌ 有一个大背景值得先说（直接说） ❌ 读下来有几个地方和直觉不一样，提前说一下（直接列） ❌ 精准命中了 N 个条件 ❌ 瓶颈从 X 转移到了 Y ❌ 是最常见的失败模式之一 ❌ X 本身没有价值，真正有用的是 Y ❌ X 已经不是瓶颈，Y 才是 ❌ 两层/三层缺一不可 ❌ 用引号强调概念（"翻译""提升""完成了"） ❌ 瑞士奶酪模型 / Poka-yoke（直接说道理，去掉模型名） ❌ 孤立的单句段落（并进上下文）

底线：读起来像和朋友聊天，不是像教科书。

English Scenario

Eliminate predictable AI writing patterns. Write like a human: varied, imperfect, specific.

Core Rules
Cut filler phrases. Remove throat-clearing openers, emphasis crutches, and all adverbs.
Break formulaic structures. Avoid binary contrasts, negative listings, dramatic fragmentation, rhetorical setups, false agency.
Use active voice. Every sentence needs a human subject doing something. No inanimate objects performing human actions ("the complaint becomes a fix").
Be specific. No vague declaratives ("The reasons are structural"). Name the specific thing. No lazy extremes ("every," "always," "never") doing vague work.
Put the reader in the room. No narrator-from-a-distance voice. "You" beats "People." Specifics beat abstractions.
Vary rhythm. Mix sentence lengths. Two items beat three. End paragraphs differently. No em dashes.
Trust readers. State facts directly. Skip softening, justification, hand-holding.
Cut quotables. If it sounds like a pull-quote, rewrite it.
Word Choice

Overused adverbs — kill them all: "quietly", "deeply", "fundamentally", "remarkably", "arguably", "certainly", "really", "just", "literally", "genuinely", "honestly", "simply", "actually"

❌ "quietly orchestrating workflows" / "fundamentally reshape how we think" ✅ Say what it does. Drop the adverb.

AI vocabulary — replace with plain language:

Avoid	Use instead
delve (into)	examine, look at, explore
leverage (as verb)	use
utilize	use
robust	strong, reliable, solid
streamline	simplify, cut
harness	use, apply
navigate (challenges)	handle, address
unpack	explain, examine
paradigm	system, approach, model
synergy	combination, cooperation
ecosystem	community, network, field
tapestry	mix, combination
landscape	situation, field, area
game-changer	significant, important
deep dive	analysis, examination
moving forward	next, from now

Pompous copulas — use "is" instead:

❌ "serves as", "stands as", "marks", "represents" ✅ "is"

Sentence Structures to Avoid

Negative parallelism — the single most common AI tell:

❌ "It's not bold. It's backwards." / "Not because X, but because Y." / "The question isn't X. The question is Y." ✅ State Y directly. Drop the negation entirely.

Negative countdown:

❌ "Not a bug. Not a feature. A fundamental design flaw." ✅ "It's a fundamental design flaw."

Rhetorical self-questions:

❌ "The result? Devastating." / "The worst part? Nobody saw it coming." ✅ State it: "The result was devastating."

Anaphora abuse — repeating the same sentence opener:

❌ "They assume that... They assume that... They assume that..." ✅ Combine or restructure. One statement, clear subject.

Tricolon abuse — rule of three, used three times back to back:

❌ "Products impress people; platforms empower them. Products solve problems; platforms create worlds." ✅ Make the point once, cleanly.

False ranges:

❌ "From innovation to cultural transformation" (what's in between?) ✅ List the two things directly, or pick one.

Dramatic fragmentation — manufactured emphasis via fragments:

❌ "He published this. Openly. In a book. As a priest." ✅ Complete sentences. Trust content over presentation.

False agency — inanimate objects performing human verbs:

❌ "the complaint becomes a fix" / "the decision emerges" / "the data tells us" ✅ Name the human. "Someone fixed it." "The team decided."

Tone Patterns to Avoid

False suspense transitions:

❌ "Here's the kicker." / "Here's the thing." / "Here's where it gets interesting." ✅ Make the point. No buildup.

Patronizing analogies:

❌ "Think of it like a highway system for data." / "Think of it as a Swiss Army knife." ✅ Explain the concept directly. If an analogy helps, use it once and move on.

Futurist invitation:

❌ "Imagine a world where every tool you use has a quiet intelligence behind it..." ✅ Describe what actually exists or what you're actually proposing.

False vulnerability — performative self-awareness:

❌ "And yes, I'm openly in love with the platform model" ✅ Real vulnerability is specific and uncomfortable. Skip the polish.

Asserting simplicity instead of proving it:

❌ "The reality is simpler and less flattering" / "History is clear" ✅ Show the evidence. Don't announce the conclusion before it.

Grandiose stakes inflation:

❌ "This will fundamentally reshape how we think about everything." / "will define the next era of computing" ✅ Say what it actually does.

Pedagogical hand-holding:

❌ "Let's break this down step by step." / "Let's unpack what this really means." ✅ Start with the content, not an announcement of the content.

Vague attributions:

❌ "Experts argue..." / "Industry reports suggest..." / "Observers have cited..." ✅ Name the expert, link the report, quote the person. If you can't, you don't have a source.

Invented concept labels — compound labels that sound analytical but aren't grounded:

❌ "the supervision paradox" / "the acceleration trap" / "workload creep" ✅ Describe the thing directly. Don't name it as if it's an established term.

Paragraph & Composition Patterns to Avoid

Short punchy fragments as paragraphs:

❌ "These weren't just products. And the software side matched. Then it professionalised." ✅ Complete sentences. No staccato drama.

Bold-first bullets — every bullet starts with a bolded phrase:

❌ "Security: Environment-based configuration..." / "Performance: Lazy loading..." ✅ Write bullets as sentences, or drop the bold. Not every list needs labels.

Fractal summaries — "what I'm going to tell you; what I'm telling you; what I just told you":

❌ "In this section, we'll explore... [3000 words later] ...as we've seen in this section." ✅ Skip the preview and the recap. Write the content.

Signposted conclusions:

❌ "In conclusion..." / "To sum up..." / "In summary..." ✅ End. Don't announce that you're ending.

The dead metaphor — one metaphor used 10 times across a piece:

❌ "The ecosystem needs ecosystems to build ecosystem value." ✅ Use a metaphor once, then move on.

Historical analogy stacking:

❌ "Apple didn't build Uber. Facebook didn't build Spotify. Stripe didn't build Shopify." ✅ Make the point. One example is enough.

One-point dilution — same argument restated 10 ways across 4000 words:

✅ Say it once. Add evidence or move on.

"Despite its challenges..." formula:

❌ "Despite these challenges, the initiative continues to thrive." ✅ Either address the challenges or don't raise them.

It's worth noting / It bears mentioning:

❌ "It's worth noting that this approach has limitations." / "Notably," / "Importantly," ✅ Say the thing directly. Skip the announcement.

Quick Checks Before Delivering Prose
Any adverbs? Kill them.
Any passive voice? Find the actor, make them the subject.
Inanimate thing doing a human verb? Name the person.
Sentence starts with "Here's"? Cut to the point.
Any "not X, it's Y" contrasts? State Y directly.
Three consecutive sentences match length? Break one.
Paragraph ends with punchy one-liner? Vary it.
Em-dash anywhere? Remove it.
Vague declarative ("The implications are significant")? Name the specific implication.
Meta-joiners ("The rest of this essay...")? Delete. Let the essay move.
Any bullet starting with bold label? Reconsider the format.
Any "In conclusion" or "To sum up"? Cut it.
Scoring

Rate 1-10 on each dimension:

Dimension	Question
Directness	Statements or announcements?
Rhythm	Varied or metronomic?
Trust	Respects reader intelligence?
Authenticity	Sounds human?
Density	Anything cuttable?

Below 35/50: revise.

Bottom line: varied, imperfect, specific. Any single trope used once may be fine. The problem is when multiple appear together or one repeats.

Weekly Installs
10
Repository
tw93/human
GitHub Stars
25
First Seen
Mar 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass