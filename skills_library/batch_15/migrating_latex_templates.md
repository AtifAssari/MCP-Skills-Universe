---
title: migrating-latex-templates
url: https://skills.sh/huangwb8/chineseresearchlatex/migrating-latex-templates
---

# migrating-latex-templates

skills/huangwb8/chineseresearchlatex/migrating-latex-templates
migrating-latex-templates
Installation
$ npx skills add https://github.com/huangwb8/chineseresearchlatex --skill migrating-latex-templates
SKILL.md
LaTeX 标书智能迁移器

核心入口：python skills/transfer_old_latex_to_new/scripts/run.py --help

一键迁移：bash skills/transfer_old_latex_to_new/scripts/migrate.sh --old ... --new ...

配置中心：config.yaml

参考文档：references/

拆分文档： references/quickstart.md / references/config_guide.md / references/api_reference.md / references/troubleshooting.md / references/faq.md / references/case_study_2025_to_2026.md

快速开始
# 一键分析（生成结构差异报告）
python skills/transfer_old_latex_to_new/scripts/run.py analyze \
  --old /path/to/NSFC_2025 \
  --new /path/to/NSFC_2026

# 一键应用（执行迁移，apply前自动快照）
python skills/transfer_old_latex_to_new/scripts/run.py apply \
  --old /path/to/NSFC_2025 \
  --new /path/to/NSFC_2026 \
  --run-id <上一步输出的run_id>

# 一键编译（验证迁移结果）
python skills/transfer_old_latex_to_new/scripts/run.py compile \
  --run-id <run_id> \
  --new /path/to/NSFC_2026

# 一键恢复（回滚到apply前状态）
python skills/transfer_old_latex_to_new/scripts/run.py restore \
  --run-id <run_id> \
  --new /path/to/NSFC_2026

一键迁移（推荐）
bash skills/transfer_old_latex_to_new/scripts/migrate.sh \
  --old /path/to/NSFC_2025 \
  --new /path/to/NSFC_2026

runs 输出隔离（强烈建议：测试/批处理）
python skills/transfer_old_latex_to_new/scripts/run.py analyze \
  --old /path/to/NSFC_2025 \
  --new /path/to/NSFC_2026 \
  --runs-root /path/to/runs


输出目录：默认 skills/transfer_old_latex_to_new/runs/<run_id>/；指定 --runs-root 则输出到该目录。

runs/<run_id>/
├── input_snapshot/     # 旧新项目输入快照
├── analysis/           # 结构分析JSON（sections_map_*.json, structure_diff.json）
├── plan/               # 迁移计划（migration_plan.json）
├── backup/             # Apply前新项目快照（用于restore）
├── logs/               # 执行日志与编译输出
│   ├── apply_result.json        # 迁移执行结果
│   ├── compile_summary.json     # 编译摘要
│   ├── compile_*_*.out.txt      # 编译标准输出
│   ├── compile_*_*.err.txt      # 编译标准错误
│   └── latex_aux/               # LaTeX 中间文件隔离目录
│       ├── main.aux             # 辅助文件
│       ├── main.log             # 编译日志
│       ├── main.bbl             # BibTeX 输出
│       ├── main.blg             # BibTeX 日志
│       ├── main.out             # hyperref 输出
│       ├── main.toc             # 目录文件
│       └── *.aux                # 其他辅助文件
└── deliverables/       # 交付物（PDF、报告、指南）


中间文件隔离: 所有 LaTeX 编译中间文件(.aux/.log/.bbl等)自动保存在 logs/latex_aux/ 目录,避免在项目目录产生"垃圾"文件。最终 PDF 自动复制回项目根目录。

前置约束（铁律）
修改范围白名单

✅ 可修改:

extraTex/*.tex 内容文件（排除 @config.tex）
新项目 references/*.bib（如需更新引用格式）
本技能运行产物：runs/<run_id>/（日志、分析、备份、交付物）

❌ 禁止修改:

main.tex 模板结构文件
extraTex/@config.tex 配置文件
.cls、.sty 样式文件
任何影响编译环境的系统文件

更完整的流程说明、配置与排障文档已拆分到 references/：

references/quickstart.md
references/config_guide.md
references/api_reference.md
references/troubleshooting.md
📋 版本与变更

当前版本: v1.4.0（与 config.yaml 同步）

变更记录: 见根级 CHANGELOG.md

优化计划: 质量评估与优化计划见 plans/v202601081355.md（仓库根级）

最后更新: 2026-01-08 维护者: Bensz Conan 许可证: MIT

Weekly Installs
73
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