---
rating: ⭐⭐⭐
title: docx-perfect
url: https://skills.sh/aaaaqwq/claude-code-skills/docx-perfect
---

# docx-perfect

skills/aaaaqwq/claude-code-skills/docx-perfect
docx-perfect
Installation
$ npx skills add https://github.com/aaaaqwq/claude-code-skills --skill docx-perfect
SKILL.md
DOCX文档美化专家

将Word文档中的内容转换为专业表格格式，支持版本化迭代优化。

快速开始

文档美化采用递增式版本管理（v0.1, v0.2, ..., v1.0），每次优化一个章节后生成新版本。

工作流程
1. 分析源文档
python -c "import sys; sys.stdout.reconfigure(encoding='utf-8'); from docx import Document; doc = Document('source.docx'); [print(p.text.strip()) for p in doc.paragraphs if p.text.strip()]"

2. 确定本次优化的章节

识别需要美化的章节标题，如：

3.1 实体识别 → 创建实体属性表格
3.2 实体间联系 → 创建联系关系表格
5.2 索引优化设计 → 创建索引汇总表格
3. 创建表格

使用 scripts/create_table.py 创建表格，参考下方脚本模板。

4. 应用样式

使用统一样式：

表头: 深蓝色背景 (#4472C4) + 白色粗体文字
数据行: 白色/浅灰色隔行变色
边框: 黑色单线边框
5. 版本号管理

自动递增版本号，保存为新文件：文档名-v0.X.docx

脚本模板

详见 scripts/README.md

常见表格模式
实体属性表格
| 属性名 | 类型/约束 | 说明 |
|--------|-----------|------|
| field1 | INT, PK   | 主键   |

联系关系表格
| 联系 | 实体A | 实体B | 说明 |
|------|-------|-------|------|

索引汇总表格
| 表名 | 索引名 | 字段 | 类型 | 说明 |

样式规范
表头背景: #4472C4 (深蓝)
表头文字: 白色、粗体、11号
奇数行: 白色 #FFFFFF
偶数行: 浅灰 #E7E6E6
数据行文字: 宋体、10号
边框: 黑色单线，4磅
Weekly Installs
41
Repository
aaaaqwq/claude-…e-skills
GitHub Stars
53
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn