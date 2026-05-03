---
rating: ⭐⭐
title: novel-research
url: https://skills.sh/smter/novel-skills/novel-research
---

# novel-research

skills/smter/novel-skills/novel-research
novel-research
Installation
$ npx skills add https://github.com/smter/novel-skills --skill novel-research
SKILL.md
小说调研
概述

创建单本小说项目，一次只向用户提出一个问题，并构建可供后续起草长期使用的 Markdown 知识库。

除非用户明确拒绝，否则默认进行联网调研。

何时使用
用户想从零开始一个新小说项目
用户只有一个故事前提，需要进一步结构化
项目需要设定、类型、风格或专业领域调研
在文件补齐前，起草阶段必须保持阻塞
必需产物

只有以下文件全部存在且内容充分时，才能将调研标记为完成：

00-project/project-brief.md
00-project/success-criteria.md
00-project/workflow-status.md
10-research/topic-research.md
10-research/setting-research.md
10-research/style-research.md
10-research/references.md
20-story/characters.md
20-story/plot-outline.md
20-story/foreshadowing.md
30-draft/chapter-plan.md
项目创建规则

调研开始时，使用书名或暂定名派生出的 slug 创建单书目录。

如果 agent 是从工作区根目录启动，而不是从书籍根目录启动，则创建并使用以下结构：

<workspace-root>/<book-slug>/00-project
<workspace-root>/<book-slug>/10-research
<workspace-root>/<book-slug>/20-story
<workspace-root>/<book-slug>/30-draft
<workspace-root>/<book-slug>/40-review
<workspace-root>/<book-slug>/50-delivery

当后续 skill 引用 00-project/... 这类路径时，应将其解析为相对于检测出的小说项目根目录。该根目录可能是：

the current working directory itself
exactly one child book directory under the current working directory

对应含义：

当前工作目录本身
当前工作目录下唯一的一个子级书籍目录

创建以下目录：

00-project
10-research
20-story
30-draft/chapters
40-review/chapter-reviews
50-delivery/output

在声明进度之前，必须先实例化所有模板文件。

需求访谈

围绕以下要素与用户访谈。在这些内容澄清之前，不得进入大纲阶段：

类型与体裁 - 这是什么样的故事？
目标读者 - 预期读者是谁？
篇幅目标 - 短篇、中篇、长篇？大致字数是多少？
语气与氛围 - 严肃、轻快、黑暗、希望感？
核心冲突 - 中心张力是什么？
主角欲望 - 主角最想得到什么？
结局倾向 - 圆满、悲剧、开放式、苦乐参半？
禁忌内容 - 有哪些题材、套路或元素必须避免？

一次只问一个问题。不要批量提问。

搜索策略

对于领域事实、时代细节、设定真实性、职业流程、地域背景和风格参照，除非用户明确禁止，否则默认进行联网调研。

如果禁止搜索：

Do not browse
Mark uncertain areas in references.md
State which details are inferred rather than verified

具体要求：

不要联网浏览
在 references.md 中标记不确定区域
明确指出哪些细节是推断而非验证所得
调研转化

不要停留在链接或摘录层面。

把每一个有用发现转化为以下一种或多种内容：

Setting constraints
Terminology notes
Realism pitfalls
Style rules
Taboo or continuity risks

对应含义：

设定约束
术语说明
真实性风险
风格规则
禁忌或连续性风险
完整性清单

在标记调研完成之前，确认：

 Protagonist, main conflict, and story goal are clearly defined
 Target length is determined with chapter count
 Chapter plan matches the target length
 Foreshadowing appears before its payoff point
 Style guidelines are sufficient to constrain later writing
 No critical background gaps remain

如果任一项失败，继续访谈或调研。不要过早标记为完成。

风险信号
在关键约束未澄清前就开始写大纲
用户没有禁止联网却跳过了调研
只堆原始链接，而不整理成结构化知识文件
核心文件仍然单薄或互相矛盾时就标记调研完成

出现以上任一情况，都意味着应保持在 research_in_progress，或转为 research_blocked。

常见自我说服
Excuse	Reality
"用户说得很模糊，所以给个宽松大纲就够了"	起草阶段需要明确约束和文件产物。
"这个类型我已经很熟，不用查了"	除非被拒绝，否则调研默认需要联网核验。
"章节计划短一点应该也没问题"	起草 skill 需要明确的章节推进设计。
状态流转
开始：将状态设为 research_in_progress
阻塞：将状态设为 research_blocked，并列出具体阻塞原因
完成：只有在所有文件通过完整性检查后，才能设为 research_complete
下一步

在 research_complete 之后，下一个允许使用的 skill 是 novel-drafting。

Weekly Installs
17
Repository
smter/novel-skills
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn