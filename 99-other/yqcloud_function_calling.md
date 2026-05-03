---
title: yqcloud-function-calling
url: https://skills.sh/binjie09/zknow-skills/yqcloud-function-calling
---

# yqcloud-function-calling

skills/binjie09/zknow-skills/yqcloud-function-calling
yqcloud-function-calling
Installation
$ npx skills add https://github.com/binjie09/zknow-skills --skill yqcloud-function-calling
SKILL.md
YQCloud 自定义 Function Calling 格式

yqcloud-ai-node 运行时接收符合此格式的函数定义，AI 决定调用某函数后，运行时自动发起 HTTP 请求（或交由前端处理），并将结果返回给 AI 继续对话。

1. JSON 结构

每个函数定义是一个 JSON 对象，包含外层（给 AI 看的标准 function calling 描述）和内层 function 字段（给运行时看的执行配置）。

{
  // ===== 外层：AI 可见 =====
  "name": "函数名",
  "description": "函数用途描述，AI 据此判断何时调用",
  "parameters": {
    "type": "object",
    "properties": { /* AI 需要填的参数 */ },
    "required": ["必填参数名"]
  },

  // ===== 内层：运行时执行配置 =====
  "function": {
    "type": "call_url",          // "call_url" = 发 HTTP 请求 | "manual" = 前端自行处理
    "method": "GET",             // HTTP 方法
    "url": "请求地址",            // 支持变量占位符和路径参数
    "headers": {},               // 请求头
    "queryParams": "a,b",        // 可选，逗号分隔。指定哪些参数放 query string，其余放 body
    "defaultPostData": {},       // 可选，POST 请求的默认 body 数据
    "requestParser": "JS代码",   // 可选，预处理 AI 传来的参数
    "responseParser": "JS代码",  // 可选，后处理 HTTP 响应
    "stopAfterFunctionCall": false,  // true = 调用后停止 AI 继续生成
    "stopAfterFunctionCallCondition": "JS代码",  // 可选，动态判断是否停止
    "typingMessage": "正在查询...",  // 可选，调用中显示给用户的提示
    "resultTips": "查询完成",        // 可选，结果返回时的提示
    "toolChoice": {},               // 可选，强制 AI 选择某工具
    "extraParamsBuilder": "JS代码"  // 可选，从结果中提取额外参数
  },

  // ===== 国际化（可选）=====
  "intl": {
    "zh_CN": { "description": "中文描述" },
    "en_US": { "description": "English description" }
  }
}

2. 变量占位符

在 url 和 headers 中可使用以下占位符，运行时自动替换：

占位符	含义
${STATIC#yqcloud_url}	YQCloud API 基础地址（如 https://api.yqcloud.com）
${tenantId}	当前租户 ID
${yqAccessToken}	当前用户 access_token
3. URL 路径参数

URL 中的 {paramName} 占位符会被 AI 传入的同名参数值替换。替换后该参数自动从 query/body 中移除，不会重复传参。

示例：URL 为 /api/v1/know/{knowId}，AI 传参 { "knowId": "abc123" }，实际请求 /api/v1/know/abc123。

4. 参数传递规则
HTTP 方法	默认行为	有 queryParams 时
GET	所有参数 → query string	queryParams 指定的 → query string
POST	所有参数 → request body	queryParams 指定的 → query string，其余 → body
5. JS 代码字段
字段	入参	用途
requestParser	data（JSON 字符串）、_（lodash）	预处理 AI 参数后返回新对象
responseParser	data（响应体对象）、_（lodash）	后处理响应后返回给 AI
stopAfterFunctionCallCondition	data（响应对象）、_（lodash）	返回 true 则停止 AI 继续
extraParamsBuilder	data（响应对象）、_（lodash）	提取额外参数传给前端
requestParser 示例

requestParser 的 data 是 AI 传参的 JSON 字符串，必须先 JSON.parse(data) 才能使用。返回值作为实际请求参数。

示例 1：重命名参数

// AI 传 { "keyword": "服务器故障" }，转换为 API 需要的 { "searchText": "服务器故障" }
"requestParser": "const params = JSON.parse(data); return { searchText: params.keyword };"


示例 2：添加固定参数

// AI 传 { "name": "张三" }，追加固定的分页和排序参数
"requestParser": "const params = JSON.parse(data); return { ...params, page: 0, size: 20, sort: 'createdDate,desc' };"


示例 3：用 lodash 处理参数

// 只保留指定字段，过滤掉 AI 可能多传的参数
"requestParser": "const params = JSON.parse(data); return _.pick(params, ['id', 'name', 'type']);"

responseParser 示例

responseParser 的 data 是 HTTP 响应体对象（已自动解析），无需 JSON.parse。返回值作为函数调用结果返回给 AI。

示例 1：精简返回数据（减少 token 消耗）

// 从分页响应中提取列表，只保留关键字段
"responseParser": "const list = (data?.content || []).filter(i => i.type === 'SERVICE').map(i => _.pick(i, ['id','name','description'])); return { list };"


示例 2：条件返回

"responseParser": "return data?.serviceItemList ? data : {result: 'no data'}"


示例 3：格式化错误信息

"responseParser": "if (data?.failed) { return { error: data.message }; } return { success: true, result: data.body };"

6. 特殊 URL
/transparent：不发 HTTP 请求，直接把 AI 传的参数作为"响应"返回。用于需要前端处理的交互场景。
7. 现有函数定义
7.1 ITSM 工单场景
getAllServiceItem — 获取全部服务项
{
  "name": "getAllServiceItem",
  "description": "获取全部服务项列表，用于匹配用户的工单需求",
  "parameters": { "type": "object", "properties": {} },
  "function": {
    "type": "call_url",
    "method": "GET",
    "url": "${STATIC#yqcloud_url}/itsm/v1/${tenantId}/service_items/catalog/page/all?serviceCatalogFlag=true&page=0&size=9999",
    "headers": { "Authorization": "bearer ${yqAccessToken}" },
    "stopAfterFunctionCall": false,
    "responseParser": "const list = (data?.content || []).filter(i => i.type === 'SERVICE' || i.type === 'RECORD').map(i => _.pick(i, ['id','name','shortDescription','description'])); return { allServiceItemList: list };"
  }
}

getCreateTicketParamJsonSchema — 获取工单表单 Schema
{
  "name": "getCreateTicketParamJsonSchema",
  "description": "根据服务项 ID 获取创建工单所需的表单字段 Schema",
  "parameters": {
    "type": "object",
    "properties": { "id": { "type": "string", "description": "服务项 ID" } },
    "required": ["id"]
  },
  "function": {
    "type": "call_url",
    "method": "GET",
    "url": "${STATIC#yqcloud_url}/ai/v1/${tenantId}/itsmScene/getServiceItemSchema",
    "headers": { "Authorization": "bearer ${yqAccessToken}" },
    "stopAfterFunctionCall": false
  }
}

requestUserSelectServiceItem — 请求用户选择服务项
{
  "name": "requestUserSelectServiceItem",
  "description": "当无法确定服务项时，展示候选列表让用户选择（最多传 1 个最可能匹配的）",
  "parameters": {
    "type": "object",
    "properties": { "serviceItemList": { "type": "array", "description": "候选服务项列表，最多 1 个" } },
    "required": ["serviceItemList"]
  },
  "function": {
    "type": "call_url",
    "method": "POST",
    "url": "/transparent",
    "stopAfterFunctionCall": true,
    "responseParser": "return data?.serviceItemList ? data : {result: 'no data'}"
  }
}

createTicket — 创建工单
{
  "name": "createTicket",
  "description": "收集完所有必填字段后创建工单",
  "parameters": { "type": "object", "properties": {}, "additionalProperties": true },
  "function": {
    "type": "manual",
    "stopAfterFunctionCall": true
  }
}


ITSM 调用流程：

用户提出工单需求
  → getAllServiceItem（获取服务项列表）
  → AI 匹配分析
    ├─ 能确定 → getCreateTicketParamJsonSchema → 逐个收集字段 → createTicket
    └─ 无法确定 → requestUserSelectServiceItem → 用户选择 → 重新进入流程

7.2 知识库场景
fetchKnowledgeElement — 查询知识内容详情

使用 URL 路径参数 {knowId}，AI 传入 knowId 后自动替换到 URL 路径中。

{
  "name": "fetchKnowledgeElement",
  "description": "根据知识内容 ID 查询知识库中的具体内容详情",
  "parameters": {
    "type": "object",
    "properties": {
      "knowId": { "type": "string", "description": "知识内容 ID" }
    },
    "required": ["knowId"]
  },
  "function": {
    "type": "call_url",
    "method": "GET",
    "url": "${STATIC#yqcloud_url}/knowledge/v1/${tenantId}/know/fetch/element/{knowId}",
    "headers": {
      "Accept": "application/json",
      "Authorization": "bearer ${yqAccessToken}",
      "x-tenant-id": "${tenantId}"
    },
    "stopAfterFunctionCall": false
  },
  "intl": {
    "zh_CN": { "description": "根据知识内容 ID 查询知识库中的具体内容详情" },
    "en_US": { "description": "Fetch knowledge element details by knowId." }
  }
}

8. 编写新函数的检查清单
name 唯一，使用 camelCase
description 清晰说明用途，AI 靠它决定何时调用
parameters 中列出 AI 需要收集的所有参数及 required
URL 路径中需要动态值的部分用 {paramName}，运行时自动替换
需要放 query string 的 POST 参数用 queryParams 声明
需要后处理响应的写 responseParser，精简返回数据减少 token 消耗
交互型函数（需要前端介入）设 stopAfterFunctionCall: true
纯数据查询函数设 stopAfterFunctionCall: false，让 AI 继续分析
Weekly Installs
12
Repository
binjie09/zknow-skills
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn