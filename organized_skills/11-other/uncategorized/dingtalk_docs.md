---
rating: ⭐⭐
title: dingtalk-docs
url: https://skills.sh/aliramw/dingtalk-docs/dingtalk-docs
---

# dingtalk-docs

skills/aliramw/dingtalk-docs/dingtalk-docs
dingtalk-docs
Installation
$ npx skills add https://github.com/aliramw/dingtalk-docs --skill dingtalk-docs
SKILL.md
钉钉云文档 Skill
⚠️ 版本兼容提醒

本 Skill v1.0 需要新版钉钉文档 MCP URL（mcpId=9629）。

如果你看到的工具名是 list_accessible_documents、write_content_to_document 等旧名称，说明配置的是旧版 MCP URL，需要重新获取：

访问 钉钉文档 MCP 广场 获取新版 StreamableHttp URL
重新配置：mcporter config add dingtalk-docs --url "<新版URL>"
严格禁止
禁止编造 nodeId / blockId — 必须从工具返回值中提取，编造 ID 会操作到错误文档或块
覆盖前必须确认 — update_document(mode="overwrite") 会清空全部内容，不确定时先问用户
禁止删除前不确认 blockId — delete_document_block 不可恢复，必须先用 list_document_blocks 确认
仅 ALIDOC 支持 Markdown 读写 — 表格/PPT/PDF 不支持 get_document_content 和 update_document
get_document_content 需要下载权限 — 仅有查看权限时无法获取内容，且不支持跨组织文档
heading.level 必须传整数 — insert_document_block 插入标题时，level 必须传 1 而非 "1"，传字符串会导致后端报错
工具列表
核心工具（8个）
工具	用途	必填参数
search_documents	搜索有权限的文档	无（keyword 选填）
create_document	创建在线文档（可含初始 Markdown 内容）	name
create_file	创建文件（在线文档/表格/演示/白板/脑图/多维表/文件夹）	name, type
get_document_content	获取文档 Markdown 内容	nodeId
update_document	更新文档内容（覆盖或追加）	nodeId, markdown
get_document_info	获取文档元信息	nodeId
create_folder	创建文件夹	name
list_nodes	遍历文件夹/知识库子节点	无（folderId 选填）
Block 精细编辑工具（4个，按需使用）
工具	用途	必填参数
list_document_blocks	查询块列表（获取 blockId）	nodeId
insert_document_block	在指定位置插入块元素	nodeId, element
update_document_block	更新块元素（仅支持 paragraph）	nodeId, blockId, element
delete_document_block	删除块元素（不可恢复）	nodeId, blockId
意图判断

创建在线文档（"新建文档/帮我建个文档/写个文档"）:

直接 create_document(name, markdown?) — 不传 folderId 默认到根目录
指定文件夹 → create_document(name, folderId=<文件夹nodeId>)

创建其他类型文件（"新建表格/脑图/白板/演示/多维表/文件夹"）:

create_file(name, type) — type 枚举：adoc/axls/appt/adraw/amind/able/folder
指定文件夹 → create_file(name, type, folderId=<文件夹nodeId>)
指定知识库 → create_file(name, type, workspaceId=<知识库ID>)（folderId 优先级高于 workspaceId）
create_document vs create_file：前者专为在线文档设计且支持写入初始 Markdown，后者支持 7 种文件类型但不支持初始内容

搜索文档（"找文档/查一下/有没有某个文档"）:

search_documents(keyword=关键词)

读取文档内容（"读文档/看看内容/这个文档写了什么"）:

get_document_content(nodeId) — nodeId 支持 URL 或 ID 自动识别
若返回 UNSUPPORTED_CONTENT_TYPE → 告知用户该文档类型不支持 Markdown 读取

更新文档内容（"写入/更新/编辑/往文档里加点东西"）:

替换全部 → update_document(nodeId, markdown, mode="overwrite")（⚠️ 会清空，先确认）
追加内容 → update_document(nodeId, markdown, mode="append")
不确定 → 先问用户是覆盖还是追加

创建文件夹（"建文件夹/新建目录"）:

create_folder(name, folderId?) — 不传 folderId 默认到根目录

遍历文件夹（"列出文件夹/看看里面有什么"）:

list_nodes(folderId?) — 支持分页（pageSize, nextPageToken）

精细编辑块元素（"修改第几段/在某段后面插入/删除某个块/在标题后加内容"）:

第一步：必须先 list_document_blocks(nodeId) 获取 blockId、index 和 blockType，禁止猜测或编造。

第二步，根据意图选择操作：

插入新块 → insert_document_block(nodeId, element, referenceBlockId?, where?)
不传位置参数 → 插入到文档末尾
where="after" / where="before" 配合 referenceBlockId 控制插入位置
修改已有块 → update_document_block(nodeId, blockId, element)（⚠️ 仅支持 paragraph 类型）
删除块 → delete_document_block(nodeId, blockId)（不可恢复，操作前务必向用户确认）
批量删除时从后向前按 index 倒序删除，避免 index 位移

⚠️ 高频易错点：

paragraph 属性对象不可省略，内容为空时须传 "paragraph": {}
heading.level 必须传整数（1 而非 "1"），传字符串会导致后端报错
列表块的 list 字段必填，不可省略
多级有序列表同组须保持相同 listId，否则展示错误

element 常用类型速查（完整结构见 dingtalk_document_struct.md）:

// 段落（paragraph）— paragraph 对象不可省略，空段落传 {}
{ "blockType": "paragraph", "paragraph": {}, "children": [{ "text": "普通文字" }] }

// 标题（heading）— level 传整数 1~6
{ "blockType": "heading", "heading": { "level": 1 }, "children": [{ "text": "一级标题" }] }

// 引用（blockquote）
{ "blockType": "blockquote", "blockquote": {}, "children": [{ "text": "引用内容" }] }

// 无序列表（unorderedList）— list 字段必填
{
  "blockType": "unorderedList",
  "unorderedList": {
    "list": { "level": 0, "listStyleType": "disc", "listStyle": { "format": "disc", "text": "%1", "align": "left" } }
  },
  "children": [{ "text": "列表项" }]
}

// 有序列表（orderedList）— list 字段必填，同组多级列表须保持相同 listId
{
  "blockType": "orderedList",
  "orderedList": {
    "list": { "listId": "list-001", "level": 0, "listStyleType": "decimal", "listStyle": { "format": "decimal", "text": "%1.", "align": "left" } }
  },
  "children": [{ "text": "列表项" }]
}

// 表格（table）— cells 为二维字符串数组
{ "blockType": "table", "table": { "rolSize": 2, "colSize": 3, "cells": [["A", "B", "C"], ["1", "2", "3"]] } }


children 行内元素（InlineElement）常用写法:

{ "text": "普通文字" }
{ "text": "加粗", "bold": true }
{ "text": "斜体", "italic": true }
{ "text": "代码", "fonts": "monospace" }
{ "elementType": "link", "properties": { "href": "https://..." }, "children": [{ "text": "链接文字" }] }
{ "elementType": "sticker", "properties": { "code": "灯泡" } }

核心工作流

创建文档并写入内容（一步完成）:

create_document(name="标题", markdown="# 标题\n\n内容") → 提取 nodeId


搜索并读取:

search_documents(keyword) → 提取 nodeId
get_document_content(nodeId) → 获取 markdown 内容


遍历文件夹并操作文档:

list_nodes(folderId?) → 提取 nodes[].nodeId
get_document_info(nodeId) → 确认 contentType=ALIDOC
get_document_content(nodeId) → 读取内容


Block 精细编辑:

list_document_blocks(nodeId) → 提取 blockId
insert_document_block(nodeId, referenceBlockId, where, element)

错误处理
PERMISSION_DENIED — 提示用户确认对该文档有操作权限
UNSUPPORTED_CONTENT_TYPE — 该文档类型（表格/PPT等）不支持 Markdown 读写
BLOCK_NOT_FOUND — blockId 不存在，先用 list_document_blocks 重新获取
UNSUPPORTED_BLOCK_TYPE — update_document_block 当前仅支持 paragraph 类型
CROSS_ORG_NOT_ALLOWED — 跨组织操作被禁止
Invalid credentials — 提示用户重新配置凭证，检查 MCP URL 是否为新版

遇到错误时展示 logId 给用户，便于向钉钉官方反馈排查。

详细参考（按需读取）
references/api-reference.md — 12 个工具完整参数 Schema + 返回值（含 Block 工具 9-12）
dingtalk_document_struct.md — Block 元素完整数据结构（BlockElement / InlineElement）
references/error-codes.md — 错误码说明 + 调试流程
Weekly Installs
131
Repository
aliramw/dingtalk-docs
GitHub Stars
43
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn