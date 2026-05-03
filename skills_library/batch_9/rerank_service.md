---
title: rerank-service
url: https://skills.sh/lin-a1/skills-agent/rerank-service
---

# rerank-service

skills/lin-a1/skills-agent/rerank-service
rerank-service
Installation
$ npx skills add https://github.com/lin-a1/skills-agent --skill rerank-service
SKILL.md
功能

根据查询语句对候选文档进行相关性评分和排序，提升检索准确性。

调用方式
from services.rerank_service.client import RerankServiceClient

client = RerankServiceClient()

query = "什么是机器学习？"
documents = [
    "机器学习是人工智能的一个分支，通过数据训练模型。",
    "今天天气很好，适合出去散步。",
    "深度学习是机器学习的子领域，使用神经网络。"
]

# 完整重排序结果
result = client.rerank(query, documents, top_n=2)

# 简化结果：(索引, 分数, 文档) 元组列表
ranked = client.rerank_documents(query, documents, top_n=2)

# 只获取最相关的文档索引
indices = client.get_top_indices(query, documents, top_n=2)  # -> [0, 2]

返回格式
{
  "id": "rerank-xxx",
  "model": "BAAI/bge-reranker-v2-m3",
  "results": [
    {
      "index": 0,
      "document": {"text": "机器学习是人工智能的一个分支..."},
      "relevance_score": 0.999
    },
    {
      "index": 2,
      "document": {"text": "深度学习是机器学习的子领域..."},
      "relevance_score": 0.098
    }
  ]
}

Weekly Installs
9
Repository
lin-a1/skills-agent
GitHub Stars
7
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass