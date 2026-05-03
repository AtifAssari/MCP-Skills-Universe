---
rating: ⭐⭐⭐
title: analyzing-data-html-report
url: https://skills.sh/dtyq/magic/analyzing-data-html-report
---

# analyzing-data-html-report

skills/dtyq/magic/analyzing-data-html-report
analyzing-data-html-report
Installation
$ npx skills add https://github.com/dtyq/magic --skill analyzing-data-html-report
SKILL.md
数据分析报告开发技能 / Data Analysis Report Development Skill

Provides data analysis report development capabilities, including creating analysis report projects, generating static HTML analysis reports, integrating visualization charts, and complete development workflows.

如何使用本文档 / How to Use This Document

This document provides quick guidance and core tool descriptions. For details, refer to the following reference documents:

Complete code examples → references/report-workflow.md
ECharts 5.6.0 specification → references/report-echarts-v5.md
代码执行方式 / Code Execution Method

Python analysis scripts are executed via Shell tool (e.g., python analyze.py).

快速开始 / Quick Start

Important: Before executing the following steps, it's recommended to read the corresponding reference documents to understand detailed specifications:

Before starting report development → Read reference/report-workflow.md for complete workflow and code examples
When configuring charts → Read reference/report-echarts-v5.md for ECharts 5.6.0 usage specification

Develop report project: Create report working directory and execute analysis:

# Step 1: 创建报告目录（目录名体现分析内容）/ Create report directory (name reflects analysis content)
import os
os.makedirs('销售数据分析', exist_ok=True)  # or 'Sales Data Analysis' for English

# Step 2: 编写分析脚本 / Write analysis script
# 脚本读取数据源，执行分析，输出 data.json


Develop HTML report:

<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/echarts/5.6.0/echarts.min.js"></script>
  </head>
  <body>
    <div id="chart" style="width:800px;height:400px;"></div>
    <script data-type="report">
      var reportData = {"total": 12345, "chart": [...]};
    </script>
    <script>
      var chart = echarts.init(document.getElementById('chart'));
      chart.setOption({...});
    </script>
  </body>
</html>

主要流程 / Main Workflow
Create report working directory: Must create dedicated directory at task start. Directory name must reflect analysis content (e.g., "Sales Data Analysis"). Place all report files (analyze.py, data.json, index.html, README.md) in this directory
Execute data analysis: Use Python script to get accurate analysis results and output data.json file
Develop HTML report: Create index.html file with ECharts visualization, data embedded via inline script tag
Documentation: Write README.md documentation
Complete delivery: Provide report summary
文件命名规范 / File Naming Rules

Directory Naming: Must reflect analysis content and business domain, intelligently determined by user preferred language, e.g.:

User preferred language is Chinese: "销售数据分析", "2024年财务报告", "用户行为分析"
User preferred language is English: "Sales Data Analysis", "2024 Financial Report", "User Behavior Analysis"

File Naming: Use standard names within directory, e.g.:

HTML report: index.html (main report file)
Data file: data.json (analysis result data)
Analysis script: analyze.py (data analysis script)
Documentation: README.md (project documentation)

Complete Examples:

Chinese project: 销售数据分析/index.html, 销售数据分析/data.json
English project: Sales Data Analysis/index.html, Sales Data Analysis/data.json
关键规则 / Key Rules
Staticization Principle
Single HTML file, all data inline, zero async loading
Data embedded via <script data-type="report"> tag: var reportData = {...};
Technical Constraints
Use ECharts 5.6.0 specification only
Python scripts for data analysis to get accurate results only, not for generating images
Charts must use ECharts, strictly prohibited to generate images via Python
决策树 / Decision Tree

Need analysis report? ├─ Yes → Report type? │ ├─ Static HTML single-page report → This skill │ └─ Interactive Dashboard → analyzing-data-dashboard skill └─ No → Only instant numeric answer → data-qa skill

Chart type? ├─ Line/Bar/Pie etc → ECharts 5.6.0 ├─ Table only → HTML table └─ Mixed → ECharts + table

技术栈 / Tech Stack

CDN Resources:

TailwindCSS: https://cdn.tailwindcss.com/3.4.17
ECharts: https://cdnjs.cloudflare.com/ajax/libs/echarts/5.6.0/echarts.min.js
FontAwesome: https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css
Tabler Icons: https://cdnjs.cloudflare.com/ajax/libs/tabler-icons/3.34.1/tabler-icons.min.css
Google Fonts: https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap
参考文档 / Reference

For detailed usage, refer to the reference directory:

report-workflow.md - Complete workflow and code examples
report-echarts-v5.md - ECharts 5.6.0 usage specification
Weekly Installs
16
Repository
dtyq/magic
GitHub Stars
4.8K
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn