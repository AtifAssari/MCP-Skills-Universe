---
rating: ⭐⭐⭐
title: data-qa
url: https://skills.sh/dtyq/magic/data-qa
---

# data-qa

skills/dtyq/magic/data-qa
data-qa
Installation
$ npx skills add https://github.com/dtyq/magic --skill data-qa
SKILL.md
数据问答技能 / Data Q&A Skill

Precisely calculate data through Python scripts, provide immediate accurate numeric answers and business explanations. Directly reading data produces hallucinations; must use script complete calculation.

代码执行方式 / Code Execution Method

Data analysis code must be executed via run_python_snippet tool.

核心步骤 / Core Steps
Write script: Python processes full data, outputs JSON or structured result
Execute: run_python_snippet(python_code=..., script_path=..., cwd=...)
Parse: Extract answer, explanation from result.content
Answer: Natural language response with numeric result and business explanation
End task
完整工作流示例 / Complete Workflow Example
# Step 1: 使用 run_python_snippet 执行 Python 代码
run_python_snippet(
    python_code="""
import json
import pandas as pd

df = pd.read_csv('path/to/data.csv')
metric = df['column'].sum()  # 完整计算，勿仅读取片段
print(json.dumps({'answer': metric, 'explanation': '...'}))
""",
    script_path="temp_data_qa.py",
    cwd="工作区根目录"
)

# Step 2: 解析 result.content 获取计算结果
# Step 3: 基于计算结果用自然语言回答用户问题


Key: Script must process complete data and output structured result (e.g. JSON). Strictly prohibited to answer by directly reading file snippets.

核心原则 / Core Principle

Directly reading data produces hallucinations, misleading decisions. Only through script complete calculation can accurate results be obtained.

工具选择决策树 / Tool Selection Decision Tree

User asks numeric data question? ├─ Yes → Write run_python_snippet script to calculate └─ No → Do not use this skill

Data format? ├─ CSV/Excel → pandas read, full calculation, print(json.dumps(...)) ├─ JSON → json.load + processing logic └─ Other → See data processing instructions below

数据处理规范 / Data Processing Instructions

When scenarios involve data analysis, write Python scripts for analysis:

Python scripts are solely for data analysis processing, not data visualization. Use ECharts for visualization. Strictly prohibited to write chart rendering code in Python scripts.
For data files like Excel, CSV, use read_files to read first 10 lines to understand structure, then use Python scripts for data analysis.
For Excel files with multiple sheets or large size, always use Python scripts for analysis. First use script to view data structure and sheet structure, then perform analysis. Scripts should return only small amount of result data, avoid reading large volumes of useless data.
Python script processing results should be refined. Script's role is to calculate and distill core data, not return large amounts of process data. Typically hundreds to thousands of characters, max 5000 characters.
Follow latest mainstream Python programming practices. Ensure code robustness, aim for one-time successful execution.
Weekly Installs
10
Repository
dtyq/magic
GitHub Stars
4.8K
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass