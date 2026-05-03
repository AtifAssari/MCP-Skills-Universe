---
rating: ⭐⭐
title: sheets-report
url: https://skills.sh/cklxx/elephant.ai/sheets-report
---

# sheets-report

skills/cklxx/elephant.ai/sheets-report
sheets-report
Installation
$ npx skills add https://github.com/cklxx/elephant.ai --skill sheets-report
SKILL.md
sheets-report

飞书电子表格管理：创建电子表格、查询表格元信息、列出工作表。

调用

通过 channel tool 的 action 参数调用：

Action	说明
create_spreadsheet	创建新的飞书电子表格
get_spreadsheet	获取电子表格元信息
list_sheets	列出电子表格中的所有工作表
参数
create_spreadsheet
参数	类型	必填	说明
title	string	否	表格标题
folder_token	string	否	目标文件夹 token
get_spreadsheet / list_sheets
参数	类型	必填	说明
spreadsheet_token	string	是	电子表格 token
示例
创建数据报表
-> channel(action="create_spreadsheet", title="月度数据报表")

查看表格信息
-> channel(action="get_spreadsheet", spreadsheet_token="shtcnXXX")

列出所有工作表
-> channel(action="list_sheets", spreadsheet_token="shtcnXXX")

自动执行原则
folder_token 可选：创建表格时省略 folder_token 则创建在用户根目录，不要问用户放哪个文件夹。
title 智能推断：用户说"创建一个表格"时，根据上下文自动生成标题（如"数据报表 2026-02-21"），不要问用户取什么名。
零交互查询：用户提供 spreadsheet_token 后，直接查询，不要二次确认。
禁止交互式菜单：不要给出选项让用户选择，直接执行最合理的操作。
链式自动执行：获取表格信息后自动列出所有工作表，方便用户一次看到完整结构。
安全等级
get_spreadsheet / list_sheets: L1 只读，无需审批
create_spreadsheet: L3 高影响，需要审批
Weekly Installs
10
Repository
cklxx/elephant.ai
GitHub Stars
10
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail