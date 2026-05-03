---
title: dive-into-langgraph
url: https://skills.sh/luochang212/dive-into-langgraph/dive-into-langgraph
---

# dive-into-langgraph

skills/luochang212/dive-into-langgraph/dive-into-langgraph
dive-into-langgraph
Installation
$ npx skills add https://github.com/luochang212/dive-into-langgraph --skill dive-into-langgraph
SKILL.md
Dive Into LangGraph

LangGraph 是由 LangChain 团队开发的开源 Agent 框架。v1.0 是稳定版本，框架能力全面升级，支持中间件、状态图、多智能体等高级功能。本 skill 内容由《LangGraph 1.0 完全指南》提供。

LangGraph 1.0 完全指南：

在线文档：https://luochang212.github.io/dive-into-langgraph/
GitHub：https://github.com/luochang212/dive-into-langgraph
安装依赖

基础依赖：

pip install \
  langgraph \
  "langchain[openai]" \
  langchain-community \
  langchain-mcp-adapters \
  python-dotenv \
  pydantic

环境变量

使用模型供应商的大模型需要设置环境变量，推荐使用阿里云百炼（DashScope）的模型：

# 阿里云百炼 (DashScope)
# 获取地址: https://bailian.console.aliyun.com/
DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
DASHSCOPE_API_KEY=your_api_key_here

# 火山方舟 (ARK)
# 获取地址: https://console.volcengine.com/ark/
ARK_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
ARK_API_KEY=your_api_key_here

# 或者其他模型供应商...


请将环境变量添加到 .env 文件，并填入你的 API key。

章节概览
序号	章节	内容简介	在线阅读	离线阅读
1	快速入门	创建你的第一个 ReAct Agent	在线	本地
2	状态图	使用 StateGraph 创建工作流	在线	本地
3	中间件	预算控制、消息截断、敏感词过滤、PII 检测	在线	本地
4	人机交互	使用 HITL 中间件实现人机交互	在线	本地
5	记忆	短期记忆、长期记忆	在线	本地
6	上下文工程	使用 State、Store、Runtime 管理上下文	在线	本地
7	MCP Server	创建 MCP Server 并接入 LangGraph	在线	本地
8	监督者模式	两种方法：tool-calling、langgraph-supervisor	在线	本地
9	并行	节点并发、@task 装饰器、Map-reduce、Sub-graphs	在线	本地
10	RAG	向量检索、关键词检索、混合检索	在线	本地
11	网络搜索	DashScope、Tavily 和 DDGS	在线	本地
官方资源
LangChain 官方文档
LangGraph 官方文档
Deep Agents 官方文档
LangMem 官方文档
LangChain GitHub 仓库
LangGraph GitHub 仓库
langchain-academy GitHub 仓库
Weekly Installs
48
Repository
luochang212/div…anggraph
GitHub Stars
389
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn