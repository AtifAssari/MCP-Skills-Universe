---
title: apifox
url: https://skills.sh/sunic4/skills/apifox
---

# apifox

skills/sunic4/skills/apifox
apifox
Installation
$ npx skills add https://github.com/sunic4/skills --skill apifox
SKILL.md
apifox

严格按以下流程执行，禁止读取 ~/.apifox/.env 文件内容：

用户要求同步时,不需要用户确认
查询结果会在终端打印
使用此技能时不需要查看其他文件
若同步或查询失败，先检查网络与 CLI 是否可用，再重试一次
若查询没有结果,由用户决定是否同步后再次查询
When to use

当用户需要查询apifox接口时使用该技能

Instructions
1. 同步项目（可选）
npx --yes --loglevel=error @sunic/skills-apifox-cli sync

2. 搜索接口
npx --yes --loglevel=error @sunic/skills-apifox-cli find <关键字>

3. Markdown 展示模板

查询到接口后，使用以下 Markdown 格式展示：

# {接口名称}

## 基本信息
- **项目ID**: {projectId}
- **接口名称**: {name}
- **请求方法**: {method}
- **接口路径**: {url}
- **更新时间**: {updatedAt}

## 请求参数

### Headers

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|------|
| {参数名} | {type} | {required} | {description} | {example} |

### Request Body

Content-Type: `application/json`

```json
{requestBody.example}

响应参数
成功响应 (200)

Content-Type: application/json

参数名	类型	必填	说明
{参数名}	{type}	{required}	{description}
data 数组项说明（如适用）
参数名	类型	说明
{参数名}	{type}	{description}
响应示例
{responses.200.content.application/json.example}

Weekly Installs
9
Repository
sunic4/skills
GitHub Stars
1
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn