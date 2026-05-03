---
title: im-contact-sorter
url: https://skills.sh/cafe3310/public-agent-skills/im-contact-sorter
---

# im-contact-sorter

skills/cafe3310/public-agent-skills/im-contact-sorter
im-contact-sorter
Installation
$ npx skills add https://github.com/cafe3310/public-agent-skills --skill im-contact-sorter
SKILL.md
IM Contact Sorter

此技能提供了一套标准化的流水线，帮助用户将缺少分类功能的 IM 软件中的联系人和群组进行整理。 整体思路是，通过界面截图 - OCR 识别 - 合并和分析，最终形成结构化的数据资产，并辅助进行清理和归档。

核心概念
Everything (全集): 包含所有联系人/群组的基础列表（通常来自原始截图的ocr）。
Primary Category (一级分类): 粗颗粒度的分类，如“所有联系人”、“所有群组”。
Secondary Category (二级分类): 细颗粒度的分类，如“重要群组”、“高价值讨论”。
Funnel Analysis (漏斗分析): 通过对比全集与各级分类，找出“未分类”和“分类不完全”的项目。
目录规范

使用此技能时，请在工作目录中遵循以下生命周期：

01-raw: 存放原始截图 (用户输入)。
02-cropped: 存放裁切和压缩后的图片 (脚本生成)。
03-ocr: 存放 OCR 识别后的 YAML 片段 (LLM生成)。
04-merged: 存放合并后的分类文件 (脚本生成)。
05-classified: 人工调整分类的工作区 (用户操作)。
06-report: 存放分析报告与操作建议 (脚本生成)。
工作流程
1. 准备与裁切 (Crop)

首先，用户将截图，按已有的分类文件夹放入 01-raw。例如 01-raw/everything，01-raw/working-groups 等。

然后，询问用户裁切参数 (左，上，宽，高)，以去除无关 UI 元素，只保留联系人列表区域。使用以下命令裁切图片：

# 用法: python crop.py <工作目录> <子目录名> <左> <上> <宽> <高>
# 示例: 裁切 'everything' 文件夹中的图片
python <path/to/skill>/scripts/crop.py . "everything" 0 200 1000 2000


你需要为每个子目录重复此步骤，直到所有截图均裁切完成，结果保存在 02-cropped/<子目录> 中。

2. 压缩 (Compress)

对图片进行原地压缩，减少传输体积。你需要为每个子目录执行以下命令：

# 用法: python compress.py <工作目录> <子目录名>
python <path/to/skill>/scripts/compress.py . "everything"

3. 识别 (OCR)

使用多模态模型识别 02-cropped 中的图片。这一步的 prompt 在 scripts/ocr.md 中定义，读取并执行它。

将结果保存到 03-ocr/<子目录>/<文件名>.yaml。

4. 合并 (Merge)

将碎片化的 YAML 合并为完整文件。

# 用法: python merge.py <工作目录>
python <path/to/skill>/scripts/merge.py .


此步将在 04-merged 中生成如 everything.yaml 的汇总文件。

5. 分类与分析 (Classify & Analyze)

人工分类: Agent 需要将 04-merged 的内容复制到 05-classified。提醒用户，可以根据需要调整分类结构。

Agent 分析:

# 用法: python analyze.py <工作目录>
python <path/to/skill>/scripts/analyze.py .


脚本将：

扫描 05-classified 中的 everything 文件，注入 groups 属性，识别每个项目所属的群组分类。
对比 everything 与各二级分类，识别未分类的项目。
生成 06-report/uncategorized_people.yaml (全局漏斗：未分类的人)。
生成 06-report/uncategorized_groups.yaml (全局漏斗：未分类的群)。
6. 闭环清理 (Action)

根据 06-report 中的报告：

清理: 对未分类且无价值的项目，在 IM 软件中删除。
归档: 对未分类但有价值的项目，手动加入正确的二级分类。
Weekly Installs
9
Repository
cafe3310/public…t-skills
GitHub Stars
197
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass