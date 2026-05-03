---
rating: ⭐⭐⭐
title: read-paper-pro
url: https://skills.sh/simingh124/skills/read-paper-pro
---

# read-paper-pro

skills/simingh124/skills/read-paper-pro
read-paper-pro
Installation
$ npx skills add https://github.com/simingh124/skills --skill read-paper-pro
SKILL.md
Read Paper Pro

把 arXiv 论文整理成一份面向 AI 研究者的读论文笔记。坚持 source-first：优先下载 src，读取 TeX 源码，不要默认只看 PDF。

Inputs

论文标题，例如 Scaling Transformer to 1M tokens and beyond with RMT

arXiv ID，例如 2304.11062 或 2304.11062v2

任意 arXiv URL：abs / pdf / html / src

如果标题解析出多个候选，立刻停下让用户确认；不要猜。

Paths

所有产物都放在当前工作目录：

./{paper_slug}/paper.tar.gz

./{paper_slug}/source

./{paper_slug}/reference_links.json

./{paper_slug}/summary_{paper_slug}.md

其中 {paper_slug} 由论文标题单词转成小写并用 _ 连接，例如 scaling_transformer_to_1m_tokens_and_beyond_with_rmt。

如果输入是 arXiv ID 或 URL，不要直接从原始输入猜 {paper_slug}。必须先解析出论文标题，再用标题生成 slug；例如 https://arxiv.org/pdf/2604.03444 应先解析到 Olmo Hybrid: From Theory to Practice and Back，再得到 olmo_hybrid_from_theory_to_practice_and_back，而不是 2604_03444。

开始下载前，先明确告诉用户这三个绝对路径：

下载路径

解压路径

总结路径

运行脚本时保持 shell 的当前目录仍然是用户当前目录，不要切到 skill 目录。

Reading boundary

默认不要参考当前工作目录、父目录、兄弟目录或历史产物目录中的其他内容。这类周围文件通常和当前论文无关，只会引入噪音并浪费时间 / token。

你应当只依赖以下两类信息源：

skill 内的说明与资源：SKILL.md、references/summary_prompt.md，以及本 skill 的脚本生成出的中间产物

当前论文下载得到的资源：source_dir 下的 TeX / bib / figure / table / appendix / supplement，以及由这些源码整理出来的 combined_source.tex、reference_links.json、figures/manifest.json 等论文派生产物

默认不要为了“找补充信息”去扫描其他论文目录、codex_assets/、用户当前目录里的无关文件，或任何与当前论文 source 无直接关系的路径。

只有当用户显式指定某个额外文件或目录必须参考时，才读取那个额外路径；否则就把注意力集中在 skill 自身说明和当前论文 source 上。

上述边界只是在限制本地目录漫游，不是在禁止外部搜索。若理解当前论文需要补充某篇引用论文、baseline、训练设置、评测协议、数据集或相关方法的具体细节，可以直接联网搜索，或打开 reference_links.json 中已有的链接继续查。目标是把这些被引用对象讲具体，而不是停留在“采用和 XXX 相同的方法 / 设置”这种过于抽象的说法。

Workflow
1. Resolve paper metadata and announce paths

运行：

python "<skill_dir>/scripts/prepare_arxiv_source.py" --resolve-only "<paper-title-or-url>"


如果系统没有 python，再改用 python3。

要求：

从脚本返回的 JSON 里读取 title、paper_slug、download_path、source_dir、summary_path

对 URL / arXiv ID 输入，也必须使用已解析标题生成 paper_slug；禁止把 2604.03444、2604_03444 之类的 ID 当作论文名或 slug

在真正下载前，先把这三个绝对路径明确告诉用户

如果标题解析出多个候选，立刻停下让用户确认；不要猜

2. Resolve paper and source tree

运行：

python "<skill_dir>/scripts/prepare_arxiv_source.py" "<paper-title-or-url>"


如果系统没有 python，再改用 python3。

要求：

统一解析到 arXiv src

下载失败、压缩包损坏、解压失败时直接报错

不要静默回退到 PDF

3. Build a readable TeX view

如果论文跨多个 \input{} / \include{} 文件，运行：

python "<skill_dir>/scripts/collect_tex.py" \
  --entrypoint "<entrypoint>" \
  --output "<paper_dir>/combined_source.tex"


优先阅读：Abstract / Introduction / 方法 / 训练设置 / 核心实验 / 局限性。

正文读完后，必须额外扫描 appendix / supplement 中与以下主题直接相关的 section：

Training Details / Implementation Details

Additional Experiments / More Comparison

Ablation / Analysis

Limitations

同时检查相关图注 / 表注，因为训练 recipe、实验设置和额外结论经常只写在 caption 里。

对 训练方法 这一节，额外要求：

主动留意正文、appendix / supplement、脚注、图注、表注里一笔带过的训练细节 / trick；只要它可能影响收敛、稳定性、最终指标或复现难度，就必须记到总结里，不要因为作者只写了一句就忽略

如果某条训练关键信息不自然落进模板已有标签，也仍然要总结出来；优先放进“其他训练关键信息”，必要时在该节下补充一条短 bullet

只有在正文、appendix / supplement、图注、表注都检查过之后，才允许写“论文未明确给出”。

4. Scan visual assets

先运行首轮图片扫描：

python "<skill_dir>/scripts/prepare_summary_figures.py" \
  --entrypoint "<entrypoint>" \
  --paper-dir "<paper_dir>"


这一步只生成 manifest.json，并默认物化一张 header.png。不要在这一步把所有 PDF 图片都转成 PNG。

规则：

不要假设 Markdown 能稳定内联 PDF 图片

只把最终总结实际会用到的 PDF figure 转成 PNG

图片显示宽度优先参考 figures/manifest.json 里的 suggested_width_pct

只用论文源码里真实存在的图

如果图片定义在被 \input{} / \include{} 的子文件里，或使用 \captionof{figure}，也要照常纳入候选

5. Build links for prior work

运行：

python "<skill_dir>/scripts/extract_reference_links.py" \
  --source-dir "<source_dir>" \
  --output "<paper_dir>/reference_links.json"


写 related methods / 核心挑战时：

直接点名具体方法，不要写“许多已有方法”“另一类方法”

优先给方法名加链接，例如 [Transformer-XL](...)

如果方法名已经是 Markdown 超链接，不要再把整个链接包进反引号
对：[Transformer-XL](...)
错：`[Transformer-XL](...)`

6. Build a coverage ledger

在动笔前，先做一个简短的 coverage ledger（可以是心智清单，也可以写成临时笔记；除非用户要求，否则不要单独交付）。至少覆盖：

问题定义：目标、约束、真正被优化的对象

核心挑战：至少 2-4 个具体 prior methods 及其不足

方法：先规划 ### 4.1 / 4.2 / ... 的子标题骨架；每个子节写什么由论文的方法结构决定，并在各 4.x 子节下继续用 bullet 分点讲清关键内容

训练方法：模型与初始化、优化器与训练调度、数据与样本构造、训练流程 / 阶段安排、关键细节与训练技巧、其他训练关键信息、batch / step / hardware / 成本、仍缺失的项；优先标出正文 / 附录 / 脚注 / 图注 / 表注里一笔带过但明显影响效果的 recipe / trick

实验与评估：主实验、关键 ablation / analysis、泛化 / 鲁棒性 / 效率 / 人类评测等适用维度

潜在问题与后续方向：作者明确 limitation、你可合理推出的失效边界

AI idea brainstorming：至少 3-5 个 idea，每个都有问题、继承 insight、改动方案、最小实验、风险

证据绑定：每个单独展开的实验后面要跟哪张图 / 哪张表；哪些点需要 2-3 张图联合说明，以及图注准备如何引导读图

如果某一节目前只能写出抽象概括，先回到源码补读证据，再写最终版，不要直接接受“较短但模糊”的草稿。

7. Draft the summary and choose evidence

读取 references/summary_prompt.md，按其中结构写一版完整草稿，并先决定：

最终要展示哪些 figure_id

哪些重要表格要转成 Markdown 表格

每个单独展开的实验后面紧跟哪张图或哪张表

要求：

主体用中文；只保留必要 English 术语

表述精确、简洁、少空话

只有在检查过正文、appendix / supplement、图注、表注之后，仍然缺失的信息，才能写“论文未明确给出”

## 5. 训练方法 的目标是最大化复现价值，而不是机械填空；凡是会显著影响收敛、稳定性、最终指标或复现难度的细节 / trick，都要主动提炼出来，即使它只在正文、appendix / supplement、脚注、图注或表注里出现一次

如果某条训练关键信息不自然落进模板已有标签，仍然要在 训练方法 中补充，不要因为模板没有现成栏位就遗漏

行与行之间留空行

关键概念、结论、限制用 Markdown 加粗

开头至少放一张代表性头图

所有图片都用居中的 HTML 包裹，例如 <p align="center"><img ... /></p>；不要直接裸放 <img>

数学公式必须使用 LaTeX math 定界符：行内公式写成 $...$，独立公式写成 $$...$$；不要把公式包进反引号 code span。对：$x_t = f(x_{t-1})$；错：`x_t = f(x_{t-1})`

当某个公式是一个独立的目标函数、更新式、复杂定义，或你接下来要逐项解释它时，优先写成块级公式并单独占行，例如：

$$\mathcal{L} = \mathcal{L}_{task} + \lambda \mathcal{L}_{aux}$$

这样比把长公式塞进一句话里更容易渲染，也更方便后续逐项解释各符号的意义

如果 2-3 张图共同说明同一个点，可以放进同一个 <p align="center">；图注要明确说明左图 / 右图 / 各子图分别看什么，以及合起来说明什么

重要实验图/表必须放在对应实验描述之后，不要统一堆到节末

方法 默认按 ### 4.1 / 4.2 / ... 展开；即使只有一个主方法块，也至少保留 ### 4.1；每个子节标题和其下讲什么内容，要由论文自己的方法结构决定，并在每个 4.x 下继续用 bullet 分点描述

只要保留实验与评估这一节，默认从该节对应的 ### x.1 开始组织；若训练方法被删去并顺延编号，就相应写成 ### 5.1、### 5.2 ...；每个子节都显式写 - **研究问题**：、- **设置**：、- **结果**：

洞见与创新 必须拆成当前节编号对应的 ### x.1 Insight 与 ### x.2 创新点；Insight 小节里至少写两条 - **Insight 1**：...，创新点 小节里先单独保留这一行：（格式：**【创新点解决的问题】 -> 【受哪个 insight 启发】 -> 【设计了什么创新点】**），且这行不要写成 list item；随后每条创新点都按 - **【...】 -> 【...】 -> 【...】** 展开

AI idea brainstorming 必须按 ### Idea X：标题 小节展开；每个 idea 都显式写 - **要解决的问题**：、- **继承的 insight / 机制 / 观察**：、- **方法设计**：、- **最小可行实验**：、- **主要风险**：

## 8.1 潜在问题 里的每一条都写成 {outline}: {detail} 结构，其中 {outline} 是短语型问题概括，{detail} 是具体问题、证据、影响范围或失效条件的展开；推荐写成 - **{outline}**：{detail}

如果一个 bullet 同时包含问题、设置、结果、多个数字和解释，优先拆成 2-4 条或改成小节，而不是继续拉长

完成初稿后，先做一轮结构归一化：把平铺方法改写成 ### 4.1 / 4.2 / ...，把平铺实验改写成与当前实验节编号一致的 ### x.1 / x.2 / ...，把 洞见与创新 改写成 ### x.1 Insight / x.2 创新点，把平铺 idea 改写成 ### Idea X，把所有裸 <img> 改成居中 HTML 包裹

8. Materialize only the selected figures

草稿定稿后，按实际用到的图片运行第二轮：

python "<skill_dir>/scripts/prepare_summary_figures.py" \
  --entrypoint "<entrypoint>" \
  --paper-dir "<paper_dir>" \
  --clean \
  --figure-ids <figure_id_1> <figure_id_2> ...


然后写最终版 Markdown；只引用这次二次物化后真实存在的资源。

9. Validate the final Markdown structure

写完最终版 Markdown 后，运行：

python "<skill_dir>/scripts/validate_summary_format.py" \
  --summary "<summary_path>"


如果系统没有 python，再改用 python3。

要求：

只要校验脚本报错，就回到 Markdown 继续改，直到通过

先修结构错误，再微调措辞；不要带着裸 <img>、缺失的实验子节标题或缺失的 ### Idea X 交付

10. Hand off with next-step questions

总结 Markdown 写完并校验通过后，在面向用户的最终回复里，除了给出总结路径，还要基于论文内容 + 你刚写出的总结内容，额外给出 2-3 个用户接下来大概率会感兴趣的问题，让用户直接选择下一步行为。

要求：

问题必须贴合这篇论文本身，不要给放之四海而皆准的空泛问题

优先覆盖这几类高价值后续动作中的 2-3 类：更深入解释方法机制、拆解训练 / 实验设计、与某个 baseline 或 prior work 对比、分析局限性 / failure case、把 paper idea 延伸成可做的研究方向

用编号列表给出，方便用户直接回复 1、2 或 3

每一项写成“用户可能会想继续追问的问题 / 你可以继续执行的动作”，而不是笼统写“继续分析论文”

如果论文最值得追问的是某个非常具体的点，例如某个关键实验、某个公式、某个训练接口、某个 surprising result，就优先把这个点放进候选问题

Final checks

交付前确认：

结构遵循 references/summary_prompt.md

如果论文训练了模型，包含“训练方法”；否则删去该节并顺延编号

训练方法 已覆盖模型与初始化、优化器与训练调度、数据与样本构造、训练流程、关键细节与训练技巧、其他训练关键信息、计算与实现、复现缺口等复现关键点

训练方法 已优先提取正文、appendix / supplement、脚注、图注、表注里可见的 recipe / trick；尤其没有漏掉那些只出现一次但明显影响结果的细节；只有剩余缺失项才写“论文未明确给出”

方法 已按 ### 4.1 / 4.2 / ... 子节展开，而不是压成一串大 bullet

实验与评估 已按当前节编号对应的 ### x.1 / x.2 / ... 子节展开；每个子节都显式写出“研究问题 / 设置 / 结果”

每个实验单元后面都有对应图或表

若多图共同说明同一个点，已在同一个居中的 HTML 图片块中组合，并在图注里写清楚各图分别怎么看、合起来说明什么

洞见与创新 已拆成当前节编号对应的 ### x.1 Insight 与 ### x.2 创新点；其中格式提示行 （格式：**【创新点解决的问题】 -> 【受哪个 insight 启发】 -> 【设计了什么创新点】**） 为单独说明行、不是 list item，且后续创新点都按 - **【...】 -> 【...】 -> 【...】** 展开

潜在问题与后续方向 已拆成当前节编号对应的 ### x.1 潜在问题 与 ### x.2 后续方向；其中 潜在问题 下包含 #### 作者明确承认的局限 与 #### 基于论文证据可推导的潜在问题，且两部分每条都按 {outline}: {detail} 展开

AI idea brainstorming 已按 ### Idea X：标题 拆开，且每个 idea 都显式包含“要解决的问题 / 继承的 insight / 机制 / 观察 / 方法设计 / 最小可行实验 / 主要风险”

重要表格若做节选，明确标注“表格节选”

所有图片都使用居中的 HTML 包裹，并且宽度设置合理

方法名超链接没有被反引号包裹

行内 / 块级公式分别使用 $...$ / $$...$$，没有把公式误写成反引号代码片段

Markdown 中引用的图片文件都真实存在

没有损坏的公式、明显乱码、破损的 LaTeX 控制序列或不必要的超长 bullet

已运行 scripts/validate_summary_format.py，且通过

给用户的最终回复里，除了总结路径，还包含 2-3 个基于该论文与总结内容定制的后续问题建议

Weekly Installs
11
Repository
simingh124/skills
GitHub Stars
1
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn