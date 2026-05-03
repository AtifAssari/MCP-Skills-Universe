---
title: auto-claude-memory
url: https://skills.sh/adaptationio/skrillz/auto-claude-memory
---

# auto-claude-memory

skills/adaptationio/skrillz/auto-claude-memory
auto-claude-memory
Installation
$ npx skills add https://github.com/adaptationio/skrillz --skill auto-claude-memory
SKILL.md
Auto-Claude Memory System

Graphiti-based persistent memory for cross-session context retention.

Overview

Auto-Claude uses Graphiti with embedded LadybugDB for memory:

No Docker required - Embedded graph database
Multi-provider support - OpenAI, Anthropic, Ollama, Google AI, Azure
Semantic search - Find relevant context across sessions
Knowledge graph - Entity relationships and facts
Architecture
Agent Session
     │
     ▼
Memory Manager
     │
     ├──▶ Add Episode (new learnings)
     ├──▶ Search Nodes (find entities)
     ├──▶ Search Facts (find relationships)
     └──▶ Get Context (relevant memories)
     │
     ▼
Graphiti (Knowledge Graph)
     │
     ▼
LadybugDB (Embedded Storage)

Configuration
Enable Memory System

In apps/backend/.env:

# Enable Graphiti memory (default: true)
GRAPHITI_ENABLED=true

Provider Selection

Choose LLM and embedding providers:

# LLM provider: openai | anthropic | azure_openai | ollama | google | openrouter
GRAPHITI_LLM_PROVIDER=openai

# Embedder provider: openai | voyage | azure_openai | ollama | google | openrouter
GRAPHITI_EMBEDDER_PROVIDER=openai

Provider Configurations
OpenAI (Simplest)
GRAPHITI_ENABLED=true
GRAPHITI_LLM_PROVIDER=openai
GRAPHITI_EMBEDDER_PROVIDER=openai
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
OPENAI_MODEL=gpt-4o-mini
OPENAI_EMBEDDING_MODEL=text-embedding-3-small

Anthropic + Voyage (High Quality)
GRAPHITI_ENABLED=true
GRAPHITI_LLM_PROVIDER=anthropic
GRAPHITI_EMBEDDER_PROVIDER=voyage
ANTHROPIC_API_KEY=sk-ant-xxxxxxxx
GRAPHITI_ANTHROPIC_MODEL=claude-sonnet-4-5-latest
VOYAGE_API_KEY=pa-xxxxxxxx
VOYAGE_EMBEDDING_MODEL=voyage-3

Ollama (Fully Offline)
GRAPHITI_ENABLED=true
GRAPHITI_LLM_PROVIDER=ollama
GRAPHITI_EMBEDDER_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_LLM_MODEL=deepseek-r1:7b
OLLAMA_EMBEDDING_MODEL=nomic-embed-text
OLLAMA_EMBEDDING_DIM=768


Prerequisites:

# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull models
ollama pull deepseek-r1:7b
ollama pull nomic-embed-text

Google AI (Gemini)
GRAPHITI_ENABLED=true
GRAPHITI_LLM_PROVIDER=google
GRAPHITI_EMBEDDER_PROVIDER=google
GOOGLE_API_KEY=AIzaSyxxxxxxxx
GOOGLE_LLM_MODEL=gemini-2.0-flash
GOOGLE_EMBEDDING_MODEL=text-embedding-004

Azure OpenAI (Enterprise)
GRAPHITI_ENABLED=true
GRAPHITI_LLM_PROVIDER=azure_openai
GRAPHITI_EMBEDDER_PROVIDER=azure_openai
AZURE_OPENAI_API_KEY=xxxxxxxx
AZURE_OPENAI_BASE_URL=https://your-resource.openai.azure.com/...
AZURE_OPENAI_LLM_DEPLOYMENT=gpt-4
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small

OpenRouter (Multi-Provider)
GRAPHITI_ENABLED=true
GRAPHITI_LLM_PROVIDER=openrouter
GRAPHITI_EMBEDDER_PROVIDER=openrouter
OPENROUTER_API_KEY=sk-or-xxxxxxxx
OPENROUTER_LLM_MODEL=anthropic/claude-3.5-sonnet
OPENROUTER_EMBEDDING_MODEL=openai/text-embedding-3-small

Database Settings
# Database name (default: auto_claude_memory)
GRAPHITI_DATABASE=auto_claude_memory

# Storage path (default: ~/.auto-claude/memories)
GRAPHITI_DB_PATH=~/.auto-claude/memories

Memory Operations
How Memory Works

During Build

Agent discovers patterns, gotchas, solutions
Memory Manager extracts insights
Insights stored as episodes in knowledge graph

New Session

Agent queries for relevant context
Memory returns related insights
Agent builds on previous learnings
MCP Tools

When GRAPHITI_MCP_URL is set, agents can use:

Tool	Purpose
search_nodes	Search entity summaries
search_facts	Search relationships between entities
add_episode	Add data to knowledge graph
get_episodes	Retrieve recent episodes
get_entity_edge	Get specific entity/relationship
Python API
from integrations.graphiti.memory import get_graphiti_memory

# Get memory instance
memory = get_graphiti_memory(spec_dir, project_dir)

# Get context for session
context = memory.get_context_for_session("Implementing feature X")

# Add insight from session
memory.add_session_insight("Pattern: use React hooks for state")

# Search for relevant memories
results = memory.search("authentication patterns")

Memory Storage
Location
~/.auto-claude/memories/
├── auto_claude_memory/     # Main database
│   ├── nodes/              # Entity nodes
│   ├── edges/              # Relationships
│   └── episodes/           # Session insights
└── embeddings/             # Vector embeddings

Per-Spec Memory
.auto-claude/specs/001-feature/
└── graphiti/               # Spec-specific memory
    ├── insights.json       # Extracted insights
    └── context.json        # Session context

Querying Memory
Command Line
cd apps/backend

# Query memory
python query_memory.py --search "authentication"

# List recent episodes
python query_memory.py --recent 10

# Get entity details
python query_memory.py --entity "UserService"

Memory in Action

Example session:

Session 1:
  Agent: "Implemented OAuth login, discovered need to handle token refresh"
  Memory: Stores insight about token refresh pattern

Session 2:
  Agent: "Implementing user profile..."
  Memory: "Previously learned about token refresh in OAuth implementation"
  Agent: Uses learned pattern for profile API calls

Best Practices
Effective Memory Use

Let agents learn naturally

Don't force memory storage
Agents automatically extract insights

Use semantic search

Query with natural language
Memory finds related concepts

Clean up periodically

Remove outdated insights
Update incorrect information
Provider Selection
Use Case	Recommended
Production	OpenAI or Anthropic+Voyage
Development	Ollama (free, offline)
Enterprise	Azure OpenAI
Budget	OpenRouter or Google AI
Performance Tips

Embedding model selection

text-embedding-3-small: Fast, good quality
text-embedding-3-large: Better quality, slower

LLM model selection

gpt-4o-mini: Fast, cost-effective
claude-sonnet: High quality reasoning

Ollama optimization

# Use smaller models for speed
OLLAMA_LLM_MODEL=llama3.2:3b
OLLAMA_EMBEDDING_MODEL=all-minilm
OLLAMA_EMBEDDING_DIM=384

Troubleshooting
Memory Not Working
# Check if enabled
grep GRAPHITI apps/backend/.env

# Verify provider credentials
python -c "from integrations.graphiti.memory import get_graphiti_memory; print('OK')"

Provider Errors
# OpenAI
curl -H "Authorization: Bearer $OPENAI_API_KEY" https://api.openai.com/v1/models

# Ollama
curl http://localhost:11434/api/tags

# Check logs
DEBUG=true python query_memory.py --search "test"

Database Corruption
# Backup and reset
mv ~/.auto-claude/memories ~/.auto-claude/memories.backup
python query_memory.py --search "test"  # Creates fresh DB

Embedding Dimension Mismatch

If changing embedding models:

# Clear existing embeddings
rm -rf ~/.auto-claude/memories/embeddings

# Restart to re-embed
python run.py --spec 001

Advanced Usage
Custom Memory Integration
from integrations.graphiti.queries_pkg.graphiti import GraphitiMemory

# Create custom memory instance
memory = GraphitiMemory(
    database="custom_db",
    db_path="/path/to/storage",
    llm_provider="anthropic",
    embedder_provider="voyage"
)

# Custom operations
memory.add_entity("UserService", {"type": "service", "purpose": "auth"})
memory.add_relationship("UserService", "uses", "Database")

Memory MCP Server

Run standalone memory server:

# Start Graphiti MCP server
GRAPHITI_MCP_URL=http://localhost:8000/mcp/ python -m integrations.graphiti.server

Related Skills
auto-claude-setup: Initial configuration
auto-claude-optimization: Performance tuning
auto-claude-troubleshooting: Debugging
Weekly Installs
95
Repository
adaptationio/skrillz
GitHub Stars
9
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass