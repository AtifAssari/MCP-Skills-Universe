---
rating: ⭐⭐⭐
title: excel-reader
url: https://skills.sh/gmwenterprise/useful-skills/excel-reader
---

# excel-reader

skills/gmwenterprise/useful-skills/excel-reader
excel-reader
Installation
$ npx skills add https://github.com/gmwenterprise/useful-skills --skill excel-reader
SKILL.md
Excel Reader

读取 Excel 文件并输出 Markdown 和 JSON 两种格式，支持合并单元格、多 sheet、数据类型识别。

前置要求

重要：本技能依赖 uv 进行 Python 依赖管理。如果用户系统没有安装 uv，请停止任务执行并告知用户：

当前系统未安装 uv，无法执行此技能。请先安装 uv：

curl -LsSf https://astral.sh/uv/install.sh | sh

何时使用
需要读取 .xlsx 或 .xlsm 文件
需要提取 Excel 数据供 AI 分析
需要处理包含合并单元格的表格
需要读取特定 sheet 或全部 sheets
快速开始
# Bash/Linux/macOS
./scripts/excel-reader <excel_file> [sheet_name]

# PowerShell/Windows
./scripts/excel-reader.ps1 <excel_file> [sheet_name]

参数说明
参数	必填	说明
excel_file	是	Excel 文件路径（.xlsx 或 .xlsm）
sheet_name	否	指定读取的 sheet 名称，不指定则读取所有
输出格式

执行成功后，会在源文件所在目录生成两个文件：

Success: <文件名>
Markdown: <源文件目录>/<文件名>.excel_reader.md
JSON: <源文件目录>/<文件名>.excel_reader.json


输出文件命名规则：

源文件 demo.xlsx → 输出 demo.excel_reader.md 和 demo.excel_reader.json
源文件 /path/to/data.xlsx → 输出 /path/to/data.excel_reader.md 和 /path/to/data.excel_reader.json

Markdown 文件：包含格式化的表格，适合直接阅读。

JSON 文件：包含完整元数据（合并单元格信息、数据类型等），适合程序处理。

Markdown 示例：

# data.xlsx

## Sheet1

| 姓名 | 年龄 | 城市 |
| --- | --- | --- |
| 张三 | 25 | 北京 |
| 李四 | 30 | 上海 |


JSON 结构（包含完整元数据）：

{
  "file": "/path/to/file.xlsx",
  "sheets": [
    {
      "name": "Sheet1",
      "data": [[...]],
      "dimensions": {"rows": 10, "columns": 5},
      "merged_cells": [...]
    }
  ]
}

功能特性
合并单元格支持

自动识别合并单元格：

左上角单元格包含实际值
其他合并区域单元格标记为 type: "merged" 且 value: null
merged_cells 数组记录所有合并区域
数据类型识别

自动识别以下类型：

string - 文本
number - 数字（整数和浮点数）
boolean - 布尔值
date - 日期时间（转换为 ISO 8601 格式）
empty - 空单元格
merged - 合并区域的非主单元格
多 Sheet 支持
不指定 sheet_name 时读取所有 sheets
指定 sheet_name 时只读取指定 sheet
Sheet 不存在时会列出可用的 sheet 名称
常见问题
文件不存在
Error: Excel file not found: /path/to/file.xlsx


检查文件路径是否正确。

不支持的格式
Error: Unsupported file format: .xls


只支持 .xlsx 和 .xlsm 格式，不支持旧版 .xls。

Sheet 不存在
Error: Sheet 'Data' not found. Available sheets: Sheet1, Sheet2


使用列出的可用 sheet 名称。

依赖要求
Python 3.12+
openpyxl
uv（用于依赖管理）

首次运行会自动初始化虚拟环境并安装依赖。

示例
# 读取所有 sheets
./scripts/excel-reader data.xlsx
# 输出:
# Success: data.xlsx
# Markdown: /current/path/data.excel_reader.md
# JSON: /current/path/data.excel_reader.json

# 读取指定 sheet
./scripts/excel-reader data.xlsx "销售数据"

# 查看生成的 Markdown
cat data.excel_reader.md

Weekly Installs
9
Repository
gmwenterprise/u…l-skills
First Seen
Mar 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass