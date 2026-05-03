---
rating: ⭐⭐
title: langchain-components
url: https://skills.sh/krzysztofsurdy/code-virtuoso/langchain-components
---

# langchain-components

skills/krzysztofsurdy/code-virtuoso/langchain-components
langchain-components
Installation
$ npx skills add https://github.com/krzysztofsurdy/code-virtuoso --skill langchain-components
SKILL.md
LangChain Components

Complete reference for the LangChain ecosystem — models, agents, tools, retrieval, memory, middleware, streaming, multi-agent orchestration, LangGraph workflows, Deep Agents, and provider integrations for Python 3.10+.

Component Index
Models & Output
Models — Chat models, tool calling, multimodal inputs, caching, rate limiting, custom models reference
Messages — Message types (Human, AI, System, Tool), message operations, serialization, OpenAI format conversion reference
Agents
Agents — create_agent, tools, structured output, guardrails, human-in-the-loop, context engineering reference
Multi-Agent — Subagents, handoffs, skills, router, custom workflows, pattern selection reference
Tools & MCP
Tools — Tool creation (@tool decorator, ToolNode), InjectedState, MCP integration, error handling reference
Retrieval & RAG
Retrieval — Document loaders, text splitters, embeddings, vector stores, agentic RAG, semantic search reference
Memory
Memory — Short-term (checkpointers, message trimming, summarization), long-term (store abstraction, namespaces) reference
Middleware & Streaming
Middleware — 16 built-in middleware, custom middleware (decorator, class, wrap-style), execution order reference
Streaming — Stream modes (updates, messages, custom), token streaming, useStream React hook reference
Runtime & Architecture
Runtime — Dependency injection, context schemas, ToolRuntime, component architecture (5 layers) reference
Testing & Deployment
Testing — Unit testing (GenericFakeChatModel), integration testing (AgentEvals), LangSmith observability reference
LangGraph
LangGraph Core — Graph API, Functional API, workflows vs agents, state management, quickstart reference
LangGraph State — Memory, persistence, durable execution, interrupts, checkpointers reference
LangGraph Advanced — Subgraphs, time-travel, streaming, Graph API usage, Functional API usage reference
Deep Agents
Deep Agents — Harness framework, models, subagents, skills, sandboxes, human-in-the-loop, long-term memory reference
Integrations
Integrations — Chat models, document loaders, retrievers, embeddings, vector stores, tools, stores, splitters reference
Providers — OpenAI, Anthropic, Google, AWS, Ollama setup and configuration reference
Quick Patterns
Create an Agent with Tools
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_agent

model = init_chat_model("anthropic:claude-sonnet-4-20250514")

def get_weather(city: str) -> str:
    """Get weather for a city."""
    return f"Sunny, 72F in {city}"

agent = create_agent(model, [get_weather])
response = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in SF?"}]}
)

Structured Output
from pydantic import BaseModel

class SearchQuery(BaseModel):
    query: str
    year: int

structured_model = model.with_structured_output(SearchQuery)
result = structured_model.invoke("Who won the World Cup in 2022?")

RAG with Retrieval
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

docs = WebBaseLoader("https://example.com").load()
chunks = RecursiveCharacterTextSplitter(chunk_size=1000).split_documents(docs)
vector_store = InMemoryVectorStore.from_documents(chunks, OpenAIEmbeddings())
retriever_tool = vector_store.as_retriever()

Multi-Agent Handoffs
from langgraph.prebuilt import create_agent

billing_agent = create_agent(model, [lookup_billing], name="billing")
tech_agent = create_agent(model, [check_status], name="tech_support")
supervisor = create_agent(
    model,
    [billing_agent, tech_agent],
    prompt="Route to the appropriate specialist."
)

LangGraph Workflow
from langgraph.graph import StateGraph, START, END

graph = StateGraph(dict)
graph.add_node("process", process_fn)
graph.add_node("review", review_fn)
graph.add_edge(START, "process")
graph.add_edge("process", "review")
graph.add_edge("review", END)
app = graph.compile()

Streaming
for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "Hello"}]},
    stream_mode="messages"
):
    print(chunk)

Best Practices
Use init_chat_model() for provider-agnostic model initialization
Prefer create_agent over building custom agent loops
Use LangGraph for complex workflows requiring state, persistence, or human-in-the-loop
Apply middleware for cross-cutting concerns (guardrails, rate limiting, PII detection)
Use checkpointers for conversation persistence and short-term memory
Use the Store abstraction for long-term memory across conversations
Choose the right multi-agent pattern: handoffs for specialization, routers for classification, subagents for parallel work
Use with_structured_output() for type-safe LLM responses
Prefer agentic RAG (tool-based retrieval) over chain-based RAG for flexibility
Use stream_mode="messages" for token-level streaming to frontends
Weekly Installs
14
Repository
krzysztofsurdy/…virtuoso
GitHub Stars
17
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn