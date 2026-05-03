---
title: arxiv-researcher
url: https://skills.sh/teslavia/arxiv-researcher/arxiv-researcher
---

# arxiv-researcher

skills/teslavia/arxiv-researcher/arxiv-researcher
arxiv-researcher
Installation
$ npx skills add https://github.com/teslavia/arxiv-researcher --skill arxiv-researcher
SKILL.md
arXiv Researcher (Unified CLI)
Claude Code 最新使用方式

优先使用以下两种方式：

/arxiv-cli 统一入口（推荐）
例：/arxiv-cli 搜索最近 7 天 speculative decoding 且有代码的论文
自然语言目标驱动
例：“搜索最近 7 天 speculative decoding 且有代码的论文，并给出前三篇建议。”
显式命令驱动
例：“执行 arxiv daily "speculative decoding" --days 7 --code-only 并总结结果。”

说明：旧的 /arxiv-* 分散指令已迁移到统一入口 /arxiv-cli，底层执行命令为 arxiv <subcommand>。

安装
git clone https://github.com/teslavia/arxiv-researcher.git
cd arxiv-researcher
./install.sh


如果系统 Python 受限（PEP 668），使用虚拟环境：

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .

统一命令入口
arxiv --help


主要子命令：

arxiv search / arxiv fetch / arxiv daily
arxiv init / arxiv context
arxiv read / arxiv brain
arxiv repro / arxiv lab / arxiv deploy / arxiv dataset / arxiv fix
arxiv extend / arxiv contrib
推荐 SOP
search/daily -> init -> read -> repro -> lab/deploy/dataset -> contrib

项目结构（重构后）
arxiv-researcher/
├── arxiv_engine/
│   ├── cli.py
│   ├── core/
│   └── pipelines/
├── skills/arxiv-cli/SKILL.md
├── requirements.txt
├── setup.py
└── install.sh

故障排查
arxiv: command not found：执行 python3 -m pip install -e .
无当前上下文：先 arxiv init <id> 或 arxiv context <id>
查看参数帮助：arxiv <subcommand> --help
Weekly Installs
11
Repository
teslavia/arxiv-…searcher
GitHub Stars
9
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail