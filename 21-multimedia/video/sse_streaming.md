---
rating: ⭐⭐⭐
title: sse-streaming
url: https://skills.sh/pv-udpv/pplx-sdk/sse-streaming
---

# sse-streaming

skills/pv-udpv/pplx-sdk/sse-streaming
sse-streaming
Installation
$ npx skills add https://github.com/pv-udpv/pplx-sdk --skill sse-streaming
SKILL.md
sse-streaming

Handle SSE streaming implementation, debugging, and reconnection for pplx-sdk.

When to use

Use this skill when implementing, debugging, or extending SSE streaming functionality for the Perplexity API.

Instructions
SSE Protocol Format

The Perplexity API uses standard SSE format:

event: query_progress
data: {"status": "searching", "progress": 0.5}

event: answer_chunk
data: {"text": "partial token", "backend_uuid": "uuid-here"}

event: final_response
data: {"text": "complete answer", "cursor": "cursor-value", "backend_uuid": "uuid-here"}

: [end]

Parsing Rules
Read line-by-line from streaming response
Skip lines starting with : (comments) — except check for [end] marker
Parse event: <type> lines → set current event type
Parse data: <json> lines → json.loads() into payload
Empty line → emit event (type + accumulated data), reset buffers
Stop on [end] marker
Event Types
Event	Purpose	Key Fields
query_progress	Search progress	status, progress
search_results	Source citations	sources[]
answer_chunk	Partial token	text
final_response	Complete answer	text, cursor, backend_uuid
related_questions	Follow-up suggestions	questions[]
error	Server error	message, code
Stream Lifecycle
for chunk in transport.stream(query="...", context_uuid="..."):
    if chunk.type == "answer_chunk":
        print(chunk.text, end="", flush=True)  # Incremental display
    elif chunk.type == "final_response":
        entry = Entry(...)  # Build complete entry
        break

Reconnection with Cursor

When a stream disconnects, resume using the cursor from the last final_response:

cursor = last_chunk.data.get("cursor")
backend_uuid = last_chunk.backend_uuid

payload["cursor"] = cursor
payload["resume_entry_uuids"] = [backend_uuid]

Retry with Exponential Backoff
from pplx_sdk.shared.retry import RetryConfig

config = RetryConfig(
    max_retries=3,
    initial_backoff_ms=1000,   # 1s, 2s, 4s
    max_backoff_ms=30000,
    backoff_multiplier=2.0,
    jitter=True,               # ±25% randomization
)

Common Pitfalls
Don't parse non-JSON data lines: Wrap json.loads() in try/except
Handle empty streams: Raise StreamingError if no events received
Buffer multi-line data: Some data: fields span multiple lines; accumulate until empty line
Respect [end] marker: Always check for [end] in comment lines to stop iteration
Weekly Installs
18
Repository
pv-udpv/pplx-sdk
First Seen
Feb 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn