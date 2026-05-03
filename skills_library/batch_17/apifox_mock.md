---
title: apifox-mock
url: https://skills.sh/giikin/skills/apifox-mock
---

# apifox-mock

skills/giikin/skills/apifox-mock
apifox-mock
Installation
$ npx skills add https://github.com/giikin/skills --skill apifox-mock
SKILL.md
Mock 数据生成规范

本技能提供四种 Mock 数据生成方式。默认生成 Apifox Mock JSON，只有用户明确指定时才切换到其他方式。

选择规则
用户指令特征	生成方式	输出形式	参考文档
默认（无特殊指定）	Apifox Mock JSON	直接在聊天中返回 JSON 代码块	apifox-mock-json.md
提到 js、脚本、script，或需要字段关联/条件逻辑	Apifox Mock 脚本	生成 .js 文件到项目根目录 mock/ 下，文件名与接口方法对应	apifox-mock-script.md
提到 local、本地，或指定了 .vue 文件	本地 Mock 文件	生成 .ts 文件到 Vue 文件同级目录	local-mock.md
提到 开启 mock 地址、初始化 mock 地址、接入 mock、代理到 Apifox	Mock 地址初始化	修改 .env.development 与 vite.config.ts	init-mock-address.md
通用流程

无论哪种方式，前两步相同：

1. 解析接口文件

读取 @/api/xxx/controller 下的接口文件，识别：

响应类型（如 RPageMcpServiceVo、RMcpServiceDetailVo）
请求类型（如 McpServicePageQuery）
2. 追溯类型定义

在 interface/apiTypes/ 目录下找到完整的类型定义，包括：

嵌套类型（如 PageMcpServiceVo → McpServiceVo[]）
关联类型（如 TagVo、McpServiceToolVo）
JSDoc 注释中的枚举值和业务含义
字段语义推断规则

根据字段名和类型智能生成合适的 mock 值，三种方式共用：

字段名模式	推断类型	示例值
id, *Id	自增/随机整数	1, 2, 3
name, *Name（中文语境）	中文标题/姓名	'商品名称', '张三'
name（英文标识符语境）	英文单词拼接	'mcp-service-alpha'
description, *Desc	中文段落	'这是一段描述...'
url, *Url, icon	图片/链接 URL	'https://picsum.photos/800/800'
*Time, *At, created*, updated*	日期时间	'2024-01-15 08:30:00'
status, is*（布尔语义）	0/1 或 true/false	1
*Color	十六进制颜色	'#3B82F6'
*Count, *Num, total	自然数	42
*Order, *Sort	自增排序	1, 2, 3
imgs, images, *List	对应类型数组	[{...}, {...}]
content（富文本）	HTML 内容	'<div><img src="..." /></div>'
枚举值识别

优先从 JSDoc 注释中提取枚举值：

interface Example {
  /** 创建类型：1-HTTP转MCP，2-MCP服务直接代理 */
  createType?: number;
  // → mock 值范围限定为 1 或 2
}

响应结构

项目统一的接口响应结构：

{
  "code": 200,
  "bizCode": 0,
  "data": {},
  "msg": "success"
}


分页响应包含 records、total、size、current、searchCount、pages 等字段。

Weekly Installs
64
Repository
giikin/skills
GitHub Stars
2
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass