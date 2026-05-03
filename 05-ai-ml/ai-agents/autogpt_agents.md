---
rating: ⭐⭐⭐
title: autogpt-agents
url: https://skills.sh/davila7/claude-code-templates/autogpt-agents
---

# autogpt-agents

skills/davila7/claude-code-templates/autogpt-agents
autogpt-agents
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill autogpt-agents
SKILL.md
AutoGPT - Autonomous AI Agent Platform

Comprehensive platform for building, deploying, and managing continuous AI agents through a visual interface or development toolkit.

When to use AutoGPT

Use AutoGPT when:

Building autonomous agents that run continuously
Creating visual workflow-based AI agents
Deploying agents with external triggers (webhooks, schedules)
Building complex multi-step automation pipelines
Need a no-code/low-code agent builder

Key features:

Visual Agent Builder: Drag-and-drop node-based workflow editor
Continuous Execution: Agents run persistently with triggers
Marketplace: Pre-built agents and blocks to share/reuse
Block System: Modular components for LLM, tools, integrations
Forge Toolkit: Developer tools for custom agent creation
Benchmark System: Standardized agent performance testing

Use alternatives instead:

LangChain/LlamaIndex: If you need more control over agent logic
CrewAI: For role-based multi-agent collaboration
OpenAI Assistants: For simple hosted agent deployments
Semantic Kernel: For Microsoft ecosystem integration
Quick start
Installation (Docker)
# Clone repository
git clone https://github.com/Significant-Gravitas/AutoGPT.git
cd AutoGPT/autogpt_platform

# Copy environment file
cp .env.example .env

# Start backend services
docker compose up -d --build

# Start frontend (in separate terminal)
cd frontend
cp .env.example .env
npm install
npm run dev

Access the platform
Frontend UI: http://localhost:3000
Backend API: http://localhost:8006/api
WebSocket: ws://localhost:8001/ws
Architecture overview

AutoGPT has two main systems:

AutoGPT Platform (Production)
Visual agent builder with React frontend
FastAPI backend with execution engine
PostgreSQL + Redis + RabbitMQ infrastructure
AutoGPT Classic (Development)
Forge: Agent development toolkit
Benchmark: Performance testing framework
CLI: Command-line interface for development
Core concepts
Graphs and nodes

Agents are represented as graphs containing nodes connected by links:

Graph (Agent)
  ├── Node (Input)
  │   └── Block (AgentInputBlock)
  ├── Node (Process)
  │   └── Block (LLMBlock)
  ├── Node (Decision)
  │   └── Block (SmartDecisionMaker)
  └── Node (Output)
      └── Block (AgentOutputBlock)

Blocks

Blocks are reusable functional components:

Block Type	Purpose
INPUT	Agent entry points
OUTPUT	Agent outputs
AI	LLM calls, text generation
WEBHOOK	External triggers
STANDARD	General operations
AGENT	Nested agent execution
Execution flow
User/Trigger → Graph Execution → Node Execution → Block.execute()
     ↓              ↓                 ↓
  Inputs      Queue System      Output Yields

Building agents
Using the visual builder
Open Agent Builder at http://localhost:3000
Add blocks from the BlocksControl panel
Connect nodes by dragging between handles
Configure inputs in each node
Run agent using PrimaryActionBar
Available blocks

AI Blocks:

AITextGeneratorBlock - Generate text with LLMs
AIConversationBlock - Multi-turn conversations
SmartDecisionMakerBlock - Conditional logic

Integration Blocks:

GitHub, Google, Discord, Notion connectors
Webhook triggers and handlers
HTTP request blocks

Control Blocks:

Input/Output blocks
Branching and decision nodes
Loop and iteration blocks
Agent execution
Trigger types

Manual execution:

POST /api/v1/graphs/{graph_id}/execute
Content-Type: application/json

{
  "inputs": {
    "input_name": "value"
  }
}


Webhook trigger:

POST /api/v1/webhooks/{webhook_id}
Content-Type: application/json

{
  "data": "webhook payload"
}


Scheduled execution:

{
  "schedule": "0 */2 * * *",
  "graph_id": "graph-uuid",
  "inputs": {}
}

Monitoring execution

WebSocket updates:

const ws = new WebSocket('ws://localhost:8001/ws');

ws.onmessage = (event) => {
  const update = JSON.parse(event.data);
  console.log(`Node ${update.node_id}: ${update.status}`);
};


REST API polling:

GET /api/v1/executions/{execution_id}

Using Forge (Development)
Create custom agent
# Setup forge environment
cd classic
./run setup

# Create new agent from template
./run forge create my-agent

# Start agent server
./run forge start my-agent

Agent structure
my-agent/
├── agent.py          # Main agent logic
├── abilities/        # Custom abilities
│   ├── __init__.py
│   └── custom.py
├── prompts/          # Prompt templates
└── config.yaml       # Agent configuration

Implement custom ability
from forge import Ability, ability

@ability(
    name="custom_search",
    description="Search for information",
    parameters={
        "query": {"type": "string", "description": "Search query"}
    }
)
def custom_search(query: str) -> str:
    """Custom search ability."""
    # Implement search logic
    result = perform_search(query)
    return result

Benchmarking agents
Run benchmarks
# Run all benchmarks
./run benchmark

# Run specific category
./run benchmark --category coding

# Run with specific agent
./run benchmark --agent my-agent

Benchmark categories
Coding: Code generation and debugging
Retrieval: Information finding
Web: Web browsing and interaction
Writing: Text generation tasks
VCR cassettes

Benchmarks use recorded HTTP responses for reproducibility:

# Record new cassettes
./run benchmark --record

# Run with existing cassettes
./run benchmark --playback

Integrations
Adding credentials
Navigate to Profile > Integrations
Select provider (OpenAI, GitHub, Google, etc.)
Enter API keys or authorize OAuth
Credentials are encrypted and stored securely
Using credentials in blocks

Blocks automatically access user credentials:

class MyLLMBlock(Block):
    def execute(self, inputs):
        # Credentials are injected by the system
        credentials = self.get_credentials("openai")
        client = OpenAI(api_key=credentials.api_key)
        # ...

Supported providers
Provider	Auth Type	Use Cases
OpenAI	API Key	LLM, embeddings
Anthropic	API Key	Claude models
GitHub	OAuth	Code, repos
Google	OAuth	Drive, Gmail, Calendar
Discord	Bot Token	Messaging
Notion	OAuth	Documents
Deployment
Docker production setup
# docker-compose.prod.yml
services:
  rest_server:
    image: autogpt/platform-backend
    environment:
      - DATABASE_URL=postgresql://...
      - REDIS_URL=redis://redis:6379
    ports:
      - "8006:8006"

  executor:
    image: autogpt/platform-backend
    command: poetry run executor

  frontend:
    image: autogpt/platform-frontend
    ports:
      - "3000:3000"

Environment variables
Variable	Purpose
DATABASE_URL	PostgreSQL connection
REDIS_URL	Redis connection
RABBITMQ_URL	RabbitMQ connection
ENCRYPTION_KEY	Credential encryption
SUPABASE_URL	Authentication
Generate encryption key
cd autogpt_platform/backend
poetry run cli gen-encrypt-key

Best practices
Start simple: Begin with 3-5 node agents
Test incrementally: Run and test after each change
Use webhooks: External triggers for event-driven agents
Monitor costs: Track LLM API usage via credits system
Version agents: Save working versions before changes
Benchmark: Use agbenchmark to validate agent quality
Common issues

Services not starting:

# Check container status
docker compose ps

# View logs
docker compose logs rest_server

# Restart services
docker compose restart


Database connection issues:

# Run migrations
cd backend
poetry run prisma migrate deploy


Agent execution stuck:

# Check RabbitMQ queue
# Visit http://localhost:15672 (guest/guest)

# Clear stuck executions
docker compose restart executor

References
Advanced Usage - Custom blocks, deployment, scaling
Troubleshooting - Common issues, debugging
Resources
Documentation: https://docs.agpt.co
Repository: https://github.com/Significant-Gravitas/AutoGPT
Discord: https://discord.gg/autogpt
License: MIT (Classic) / Polyform Shield (Platform)
Weekly Installs
393
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn