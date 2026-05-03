---
rating: ⭐⭐
title: deepseek
url: https://skills.sh/vm0-ai/vm0-skills/deepseek
---

# deepseek

skills/vm0-ai/vm0-skills/deepseek
deepseek
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill deepseek
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name DEEPSEEK_TOKEN or zero doctor check-connector --url https://api.deepseek.com/chat/completions --method POST

How to Use

All examples below assume you have DEEPSEEK_TOKEN set.

The base URL for the DeepSeek API is:

https://api.deepseek.com (recommended)
https://api.deepseek.com/v1 (OpenAI-compatible)
1. Basic Chat Completion

Send a simple chat message:

Write to /tmp/deepseek_request.json:

{
  "model": "deepseek-chat",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "Hello, who are you?"
    }
  ]
}


Then run:

curl -s "https://api.deepseek.com/chat/completions" -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $DEEPSEEK_TOKEN" -d @/tmp/deepseek_request.json


Available models:

deepseek-chat: DeepSeek-V3.2 non-thinking mode (128K context, 8K max output)
deepseek-reasoner: DeepSeek-V3.2 thinking mode (128K context, 64K max output)
2. Chat with Temperature Control

Adjust creativity/randomness with temperature:

Write to /tmp/deepseek_request.json:

{
  "model": "deepseek-chat",
  "messages": [
    {
      "role": "user",
      "content": "Write a short poem about coding."
    }
  ],
  "temperature": 0.7,
  "max_tokens": 200
}


Then run:

curl -s "https://api.deepseek.com/chat/completions" -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $DEEPSEEK_TOKEN" -d @/tmp/deepseek_request.json | jq -r '.choices[0].message.content'


Parameters:

temperature (0-2, default 1): Higher = more creative, lower = more deterministic
top_p (0-1, default 1): Nucleus sampling threshold
max_tokens: Maximum tokens to generate
3. Streaming Response

Get real-time token-by-token output:

Write to /tmp/deepseek_request.json:

{
  "model": "deepseek-chat",
  "messages": [
    {
      "role": "user",
      "content": "Explain quantum computing in simple terms."
    }
  ],
  "stream": true
}


Then run:

curl -s "https://api.deepseek.com/chat/completions" -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $DEEPSEEK_TOKEN" -d @/tmp/deepseek_request.json


Streaming returns Server-Sent Events (SSE) with delta chunks, ending with data: [DONE].

4. Deep Reasoning (Thinking Mode)

Use the reasoner model for complex reasoning tasks:

Write to /tmp/deepseek_request.json:

{
  "model": "deepseek-reasoner",
  "messages": [
    {
      "role": "user",
      "content": "What is 15 * 17? Show your work."
    }
  ]
}


Then run:

curl -s "https://api.deepseek.com/chat/completions" -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $DEEPSEEK_TOKEN" -d @/tmp/deepseek_request.json | jq -r '.choices[0].message.content'


The reasoner model excels at math, logic, and multi-step problems.

5. JSON Output Mode

Force the model to return valid JSON:

Write to /tmp/deepseek_request.json:

{
  "model": "deepseek-chat",
  "messages": [
    {
      "role": "system",
      "content": "You are a JSON generator. Always respond with valid JSON."
    },
    {
      "role": "user",
      "content": "List 3 programming languages with their main use cases."
    }
  ],
  "response_format": {
    "type": "json_object"
  }
}


Then run:

curl -s "https://api.deepseek.com/chat/completions" -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $DEEPSEEK_TOKEN" -d @/tmp/deepseek_request.json | jq -r '.choices[0].message.content'

6. Multi-turn Conversation

Continue a conversation with message history:

Write to /tmp/deepseek_request.json:

{
  "model": "deepseek-chat",
  "messages": [
    {
      "role": "user",
      "content": "My name is Alice."
    },
    {
      "role": "assistant",
      "content": "Nice to meet you, Alice."
    },
    {
      "role": "user",
      "content": "What is my name?"
    }
  ]
}


Then run:

curl -s "https://api.deepseek.com/chat/completions" -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $DEEPSEEK_TOKEN" -d @/tmp/deepseek_request.json | jq -r '.choices[0].message.content'

7. Code Completion (FIM)

Use Fill-in-the-Middle for code completion (beta endpoint):

Write to /tmp/deepseek_request.json:

{
  "model": "deepseek-chat",
  "prompt": "def add(a, b):\n ",
  "max_tokens": 20
}


Then run:

curl -s "https://api.deepseek.com/beta/completions" -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $DEEPSEEK_TOKEN" -d @/tmp/deepseek_request.json | jq -r '.choices[0].text'


FIM is useful for:

Code completion in editors
Filling gaps in documents
Context-aware text generation
8. Function Calling (Tools)

Define functions the model can call:

Write to /tmp/deepseek_request.json:

{
  "model": "deepseek-chat",
  "messages": [
    {
      "role": "user",
      "content": "What is the weather in Tokyo?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get the current weather for a location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city name"
            }
          },
          "required": ["location"]
        }
      }
    }
  ]
}


Then run:

curl -s "https://api.deepseek.com/chat/completions" -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $DEEPSEEK_TOKEN" -d @/tmp/deepseek_request.json


The model will return a tool_calls array when it wants to use a function.

9. Check Token Usage

Extract usage information from response:

Write to /tmp/deepseek_request.json:

{
  "model": "deepseek-chat",
  "messages": [
    {
      "role": "user",
      "content": "Hello"
    }
  ]
}


Then run:

curl -s "https://api.deepseek.com/chat/completions" -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $DEEPSEEK_TOKEN" -d @/tmp/deepseek_request.json | jq '.usage'


Response includes:

prompt_tokens: Input token count
completion_tokens: Output token count
total_tokens: Sum of both
OpenAI SDK Compatibility

DeepSeek is fully compatible with OpenAI SDKs. Just change the base URL:

Python:

from openai import OpenAI
client = OpenAI(api_key="your-deepseek-key", base_url="https://api.deepseek.com")


Node.js:

import OpenAI from 'openai';
const client = new OpenAI({ apiKey: 'your-deepseek-key', baseURL: 'https://api.deepseek.com' });

Tips: Complex JSON Payloads

For complex requests with nested JSON (like function calling), use a temp file to avoid shell escaping issues:

Write to /tmp/deepseek_request.json:

{
  "model": "deepseek-chat",
  "messages": [{"role": "user", "content": "What is the weather in Tokyo?"}],
  "tools": [{
    "type": "function",
    "function": {
      "name": "get_weather",
      "description": "Get current weather",
      "parameters": {
        "type": "object",
        "properties": {"location": {"type": "string"}},
        "required": ["location"]
      }
    }
  }]
}


Then run:

curl -s "https://api.deepseek.com/chat/completions" -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $DEEPSEEK_TOKEN" -d @/tmp/deepseek_request.json

Guidelines
Choose the right model: Use deepseek-chat for general tasks, deepseek-reasoner for complex reasoning
Use caching: Repeated prompts with same prefix benefit from cache pricing ($0.028 vs $0.28)
Set max_tokens: Prevent runaway generation by setting appropriate limits
Use streaming for long responses: Better UX for real-time applications
JSON mode requires system prompt: When using response_format, include JSON instructions in system message
FIM uses beta endpoint: Code completion endpoint is at api.deepseek.com/beta
Complex JSON: Use temp files with -d @filename to avoid shell quoting issues
Weekly Installs
204
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass