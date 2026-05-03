---
title: rag-service
url: https://skills.sh/lin-a1/skills-agent/rag-service
---

# rag-service

skills/lin-a1/skills-agent/rag-service
rag-service
Installation
$ npx skills add https://github.com/lin-a1/skills-agent --skill rag-service
SKILL.md
功能

RAG 多路检索服务，提供：

向量语义检索 - 基于 Milvus 的向量相似度搜索
Rerank 重排序 - 对检索结果进行精排
文档存储 - 保存文档到向量数据库
调用方式
from services.rag_service.client import RAGServiceClient

client = RAGServiceClient()

# 健康检查
status = client.health()

# 语义检索
result = client.retrieve(
    query="Python 异步编程最佳实践",
    top_k=5,
    min_score=0.85,
    rerank=True
)
print(result["results"])

# 便捷方法：只获取文本列表
texts = client.retrieve_texts(query="Python 异步编程", top_k=5)

# 保存文档
client.save(documents=[
    {"text": "文档内容...", "metadata": {"title": "标题", "url": "..."}}
])

返回格式
retrieve
{
  "query": "Python 异步编程",
  "results": [
    {
      "id": "abc123",
      "text": "Python异步编程基于asyncio库...",
      "score": 0.92,
      "metadata": {"title": "Python官方文档", "url": "..."}
    }
  ],
  "total": 3,
  "elapsed_ms": 45.2,
  "from_cache": false
}

save
{
  "saved_count": 5,
  "collection_name": "websearch_results"
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
Gen Agent Trust HubPass
SocketPass
SnykPass