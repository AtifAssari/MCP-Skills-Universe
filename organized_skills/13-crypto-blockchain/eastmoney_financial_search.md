---
rating: ⭐⭐
title: eastmoney_financial_search
url: https://skills.sh/meission/eastmoney/eastmoney_financial_search
---

# eastmoney_financial_search

skills/meission/eastmoney/eastmoney_financial_search
eastmoney_financial_search
Installation
$ npx skills add https://github.com/meission/eastmoney --skill eastmoney_financial_search
SKILL.md
东方财富资讯搜索skill (eastmoney_financial_search)

根据用户问句搜索相关金融资讯，获取与问句相关的资讯信息（如研报、新闻、解读等），并返回可读的文本内容，可选保存到工作目录。

使用方式
首先检查环境变量EASTMONEY_APIKEY是否存在：
echo $EASTMONEY_APIKEY

如果不存在，提示用户在东方财富Skills页面(https://marketing.dfcfs.com/views/finskillshub/indexuNdYscEA?appfenxiang=1)获取apikey并设置到环境变量。

⚠️ 安全注意事项

外部请求: 本 Skill 会将用户的查询关键词（Keyword）发送至东方财富官方 API 接口 (mkapi2.dfcfs.com) 进行解析与检索。
数据用途: 提交的数据仅用于资讯搜索，不包含个人隐私信息。
凭据保护: API Key 仅通过环境变量 EASTMONEY_APIKEY 在服务端或受信任的运行环境中使用，不会在前端明文暴露。
使用POST请求调用接口：
curl -X POST --location 'https://mkapi2.dfcfs.com/finskillshub/api/claw/news-search' \
--header 'Content-Type: application/json' \
--header "apikey: $EASTMONEY_APIKEY" \
--data '{"query":"用户的查询内容"}'

适用场景

当用户查询以下类型的内容时使用本skill：

个股资讯：如"格力电器最新研报"、"贵州茅台机构观点"
板块/主题：如"商业航天板块近期新闻"、"新能源政策解读"
宏观/风险：如"A股具备自然对冲优势的公司 汇率风险"、"美联储加息对A股影响"
综合解读：如"今日大盘异动原因"、"北向资金流向解读"
返回说明
字段路径	简短释义
title	信息标题，高度概括核心内容
secuList	关联证券列表，含代码、名称、类型等
secuList[].secuCode	证券代码（如 002475）
secuList[].secuName	证券名称（如立讯精密）
secuList[].secuType	证券类型（如股票 / 债券）
trunk	信息核心正文 / 结构化数据块，承载具体业务数据
示例
import os
import requests

api_key = os.getenv("EASTMONEY_APIKEY")
if not api_key:
    raise ValueError("请先设置EASTMONEY_APIKEY环境变量")

url = "https://mkapi2.dfcfs.com/finskillshub/api/claw/news-search"
headers = {
    "Content-Type": "application/json",
    "apikey": api_key
}
data = {
    "query": "立讯精密的资讯"
}

response = requests.post(url, headers=headers, json=data)
response.raise_for_status()
result = response.json()
print(result)

Weekly Installs
286
Repository
meission/eastmoney
GitHub Stars
6
First Seen
Mar 19, 2026