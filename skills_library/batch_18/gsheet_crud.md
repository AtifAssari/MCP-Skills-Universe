---
title: gsheet-crud
url: https://skills.sh/vkboo/gsheet-crud/gsheet-crud
---

# gsheet-crud

skills/vkboo/gsheet-crud/gsheet-crud
gsheet-crud
Installation
$ npx skills add https://github.com/vkboo/gsheet-crud --skill gsheet-crud
SKILL.md
GSheet-CRUD API 使用指南
前置条件
1. 分享 Google Sheets 权限

将以下服务账户邮箱添加为 Google Sheets 的编辑者：

gsheet-sql@axinan-dev.iam.gserviceaccount.com

2. 数据格式要求
第一行必须是列名（字段名）
数据从第二行开始
name	age	email
John	25	john@example.com
Jane	30	jane@example.com
API 端点
https://gsheet-sql.dev.iglooinsure.com/api/{doc_id}/{sheet_name}

doc_id: 从 Google Sheets URL 获取 https://docs.google.com/spreadsheets/d/{doc_id}/edit
sheet_name: 工作表名称（可选，默认 Sheet1）
GET - 查询数据

获取所有数据：

curl 'https://gsheet-sql.dev.iglooinsure.com/api/{doc_id}'


条件查询：

curl 'https://gsheet-sql.dev.iglooinsure.com/api/{doc_id}?name=John&age=25'


响应示例：

[
  {"name": "John", "age": 25, "email": "john@example.com"}
]

POST - 插入数据

插入单条记录：

curl -X POST 'https://gsheet-sql.dev.iglooinsure.com/api/{doc_id}' \
  -H 'Content-Type: application/json' \
  -d '{"name": "Mike", "age": 28, "email": "mike@example.com"}'


批量插入：

curl -X POST 'https://gsheet-sql.dev.iglooinsure.com/api/{doc_id}' \
  -H 'Content-Type: application/json' \
  -d '[
    {"name": "Mike", "age": 28, "email": "mike@example.com"},
    {"name": "Sarah", "age": 35, "email": "sarah@example.com"}
  ]'

PUT - 更新数据

通过查询参数匹配要更新的记录：

curl -X PUT 'https://gsheet-sql.dev.iglooinsure.com/api/{doc_id}?name=John' \
  -H 'Content-Type: application/json' \
  -d '{"age": 26, "email": "new_email@example.com"}'

DELETE - 删除数据

通过查询参数匹配要删除的记录：

curl -X DELETE 'https://gsheet-sql.dev.iglooinsure.com/api/{doc_id}?name=John'

JavaScript 调用示例
const API_BASE = 'https://gsheet-sql.dev.iglooinsure.com/api';
const DOC_ID = 'your_doc_id';

// 查询
const data = await fetch(`${API_BASE}/${DOC_ID}?name=John`).then(r => r.json());

// 插入
await fetch(`${API_BASE}/${DOC_ID}`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'Mike', age: 28, email: 'mike@example.com' })
});

// 更新
await fetch(`${API_BASE}/${DOC_ID}?name=John`, {
  method: 'PUT',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ age: 26 })
});

// 删除
await fetch(`${API_BASE}/${DOC_ID}?name=John`, { method: 'DELETE' });

Python 调用示例
import requests

API_BASE = 'https://gsheet-sql.dev.iglooinsure.com/api'
DOC_ID = 'your_doc_id'

# 查询
data = requests.get(f'{API_BASE}/{DOC_ID}', params={'name': 'John'}).json()

# 插入
requests.post(f'{API_BASE}/{DOC_ID}', json={'name': 'Mike', 'age': 28, 'email': 'mike@example.com'})

# 更新
requests.put(f'{API_BASE}/{DOC_ID}', params={'name': 'John'}, json={'age': 26})

# 删除
requests.delete(f'{API_BASE}/{DOC_ID}', params={'name': 'John'})

Weekly Installs
10
Repository
vkboo/gsheet-crud
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn