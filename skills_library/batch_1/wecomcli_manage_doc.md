---
title: wecomcli-manage-doc
url: https://skills.sh/wecomteam/wecom-cli/wecomcli-manage-doc
---

# wecomcli-manage-doc

skills/wecomteam/wecom-cli/wecomcli-manage-doc
wecomcli-manage-doc
Installation
$ npx skills add https://github.com/wecomteam/wecom-cli --skill wecomcli-manage-doc
SKILL.md
企业微信文档管理

wecom-cli 是企业微信提供的命令行程序，所有操作通过执行 wecom-cli 命令完成。

管理企业微信文档的创建、读取和编辑。所有接口支持通过 docid 或 url 二选一定位文档。

调用方式

通过 wecom-cli 调用，品类为 doc：

wecom-cli doc <tool_name> '<json_params>'

返回格式说明

所有接口返回 JSON 对象，包含以下公共字段：

字段	类型	说明
errcode	integer	返回码，0 表示成功，非 0 表示失败
errmsg	string	错误信息，成功时为 "ok"

当 errcode 不为 0 时，说明接口调用失败，可重试 1 次；若仍失败，将 errcode 和 errmsg 展示给用户。

get_doc_content

获取文档完整内容数据，只能以 Markdown 格式返回。采用异步轮询机制：首次调用无需传 task_id，接口返回 task_id；若 task_done 为 false，需携带该 task_id 再次调用，直到 task_done 为 true 时返回完整内容。

首次调用（不传 task_id）：
wecom-cli doc get_doc_content '{"docid": "DOCID", "type": 2}'

轮询（携带上次返回的 task_id）：
wecom-cli doc get_doc_content '{"docid": "DOCID", "type": 2, "task_id": "xxx"}'

或通过 URL：
wecom-cli doc get_doc_content '{"url": "https://doc.weixin.qq.com/doc/xxx", "type": 2}'


参见 API 详情。

create_doc

新建文档（doc_type=3）或智能表格（doc_type=10）。创建成功返回 url 和 docid。

wecom-cli doc create_doc '{"doc_type": 3, "doc_name": "项目周报"}'

wecom-cli doc create_doc '{"doc_type": 10, "doc_name": "任务跟踪表"}'


注意：docid 仅在创建时返回，需妥善保存。创建智能表格时默认包含一个子表，可通过 smartsheet_get_sheet 查询其 sheet_id。

参见 API 详情。

edit_doc_content

用 Markdown 内容覆写文档正文。content_type 固定为 1（Markdown）。

wecom-cli doc edit_doc_content '{"docid": "DOCID", "content": "# 标题\n\n正文内容", "content_type": 1}'


参见 API 详情。

典型工作流
读取文档 →
wecom-cli doc get_doc_content '{"docid": "DOCID", "type": 2}'


，若 task_done 为 false 则携带 task_id 继续轮询 2. 创建新文档 →

wecom-cli doc create_doc '{"doc_type": 3, "doc_name": "文档名"}'


，保存返回的 docid 3. 编辑文档 → 先 get_doc_content 了解当前内容，再 edit_doc_content 覆写

Weekly Installs
2.4K
Repository
wecomteam/wecom-cli
GitHub Stars
1.9K
First Seen
Mar 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass