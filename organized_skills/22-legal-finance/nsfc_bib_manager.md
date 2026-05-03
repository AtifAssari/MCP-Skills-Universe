---
rating: ⭐⭐
title: nsfc-bib-manager
url: https://skills.sh/huangwb8/chineseresearchlatex/nsfc-bib-manager
---

# nsfc-bib-manager

skills/huangwb8/chineseresearchlatex/nsfc-bib-manager
nsfc-bib-manager
Installation
$ npx skills add https://github.com/huangwb8/chineseresearchlatex --skill nsfc-bib-manager
SKILL.md
引用与 Bib 管理器

目标：只引“可核验”文献，且通过 \\cite{...} 使用，不手写参考文献列表。

0) 规则（硬约束）
不凭记忆编造 DOI/卷期页码/作者列表；核验不到就先不加，并标注“待核验”。
新增条目优先写入 references/ccs.bib（通用文献）；申请人已发论文写入 references/mypaper.bib。
参考文献样式不动：不要改 references/reference.tex 的 \\bibliographystyle{bibtex-style/gbt7714-nsfc.bst}。
1) 工作流（每次新增引用都走）
明确要支持的“主张”是什么（避免为了凑数加文献）。
联网检索并核验元数据：优先用 MCP 的论文检索/出版方元数据（题目、年份、期刊、DOI）。
生成 BibTeX 条目并落库（只做最小增量改动）。
在对应 .tex 中使用 \\cite{key} 引用（不手写条目）。
Weekly Installs
23
Repository
huangwb8/chines…rchlatex
GitHub Stars
1.5K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass