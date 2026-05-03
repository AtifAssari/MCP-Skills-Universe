---
rating: ⭐⭐⭐
title: embedding-service
url: https://skills.sh/lin-a1/skills-agent/embedding-service
---

# embedding-service

skills/lin-a1/skills-agent/embedding-service
embedding-service
Installation
$ npx skills add https://github.com/lin-a1/skills-agent --skill embedding-service
SKILL.md
功能

将输入文本转换为高维向量表示，用于语义相似度计算、聚类分析等下游任务。

调用方式
from services.embedding_service.client import EmbeddingServiceClient

client = EmbeddingServiceClient()

# 单个文本向量化
vector = client.embed_query("人工智能")  # -> list[float]

# 多个文本向量化
texts = ["机器学习", "深度学习", "自然语言处理"]
vectors = client.embed_documents(texts)  # -> list[list[float]]

返回格式
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [-0.031, -0.016, -0.007, ...]
    }
  ],
  "model": "Qwen/Qwen3-Embedding-0.6B"
}

Weekly Installs
10
Repository
lin-a1/skills-agent
GitHub Stars
7
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn