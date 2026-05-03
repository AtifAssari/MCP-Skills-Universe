---
title: extended-thinking
url: https://skills.sh/lobbi-docs/claude/extended-thinking
---

# extended-thinking

skills/lobbi-docs/claude/extended-thinking
extended-thinking
Installation
$ npx skills add https://github.com/lobbi-docs/claude --skill extended-thinking
SKILL.md
Extended Thinking (Ultrathink) Skill

Enable Claude's extended thinking capabilities for complex reasoning tasks that benefit from internal deliberation before responding.

When to Use
Complex problem solving requiring multi-step reasoning
Code architecture decisions with multiple trade-offs
Debugging complex issues needing systematic analysis
Strategic planning with many variables
Mathematical or logical proofs
Security analysis requiring threat modeling
Performance optimization with multiple factors
Supported Models
Model	Extended Thinking	Summarized Thinking
Claude Opus 4.5	✓ Full	-
Claude Opus 4.1	✓ Full	-
Claude Opus 4	✓	✓ Summarized
Claude Sonnet 4.5	✓ Full	-
Claude Sonnet 4	✓	✓ Summarized
Claude Haiku 4.5	✓ Full	-
API Configuration
Basic Extended Thinking (Python)
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000  # Minimum 1,024
    },
    messages=[{
        "role": "user",
        "content": "Analyze this complex architecture decision..."
    }]
)

# Access thinking and response
for block in response.content:
    if block.type == "thinking":
        print(f"Thinking: {block.thinking}")
    elif block.type == "text":
        print(f"Response: {block.text}")

TypeScript Configuration
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const response = await client.messages.create({
  model: "claude-sonnet-4-20250514",
  max_tokens: 16000,
  thinking: {
    type: "enabled",
    budget_tokens: 10000,
  },
  messages: [
    {
      role: "user",
      content: "Analyze this complex architecture decision...",
    },
  ],
});

Streaming (Required for max_tokens > 21,333)
with client.messages.stream(
    model="claude-sonnet-4-20250514",
    max_tokens=32000,
    thinking={
        "type": "enabled",
        "budget_tokens": 20000
    },
    messages=[{"role": "user", "content": prompt}]
) as stream:
    for event in stream:
        if event.type == "content_block_delta":
            if hasattr(event.delta, "thinking"):
                print(event.delta.thinking, end="", flush=True)
            elif hasattr(event.delta, "text"):
                print(event.delta.text, end="", flush=True)

Budget Recommendations
Task Complexity	Budget Tokens	Use Case
Light	1,024 - 4,000	Simple clarifications, basic analysis
Medium	4,000 - 10,000	Code review, debugging, design decisions
Heavy	10,000 - 20,000	Architecture planning, security audits
Complex	20,000 - 32,000	Multi-system analysis, comprehensive reviews
Maximum	32,000+	Use batch API for budgets exceeding 32k
Tool Use with Extended Thinking

CRITICAL: When using tools with extended thinking, you MUST preserve thinking blocks in the conversation history.

# Initial request with thinking
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 8000},
    tools=[{
        "name": "analyze_code",
        "description": "Analyze code for issues",
        "input_schema": {
            "type": "object",
            "properties": {"code": {"type": "string"}},
            "required": ["code"]
        }
    }],
    messages=[{"role": "user", "content": "Analyze this code..."}]
)

# MUST include ALL content blocks including thinking
tool_use_block = next(b for b in response.content if b.type == "tool_use")
tool_result = execute_tool(tool_use_block)

# Continue with thinking blocks preserved
follow_up = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 8000},
    tools=[...],
    messages=[
        {"role": "user", "content": "Analyze this code..."},
        {"role": "assistant", "content": response.content},  # Includes thinking!
        {"role": "user", "content": [{
            "type": "tool_result",
            "tool_use_id": tool_use_block.id,
            "content": tool_result
        }]}
    ]
)

Interleaved Thinking (Claude 4 Models)

For Claude 4 models, use interleaved thinking for thinking between tool calls:

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    betas=["interleaved-thinking-2025-05-14"],  # Required for Claude 4
    messages=[...]
)

Constraints
Minimum budget: 1,024 tokens
Maximum output: 128k tokens (thinking + response)
Temperature: Must be 1 (default) - cannot modify
top_k: Cannot be used with extended thinking
Streaming required: When max_tokens > 21,333
System prompts: Fully compatible
Best Practices
Start conservative: Begin with lower budgets, increase as needed
Monitor actual usage: Track thinking_tokens in response usage
Use streaming: For better UX and larger outputs
Preserve thinking blocks: Critical for multi-turn tool use
Batch for heavy workloads: Use batch API for budgets > 32k tokens
Match budget to task: Don't over-allocate for simple tasks
Integration with Claude Code

When using Claude Code CLI with extended thinking models:

# The CLI automatically handles extended thinking for supported models
# Use opus or sonnet models for complex tasks

claude --model claude-opus-4-5-20250514 "Analyze this codebase architecture"

See Also
[[complex-reasoning]] - Multi-step reasoning patterns
[[deep-analysis]] - Analytical thinking templates
[[llm-integration]] - General LLM API patterns
Weekly Installs
45
Repository
lobbi-docs/claude
GitHub Stars
11
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass