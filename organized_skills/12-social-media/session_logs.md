---
rating: ⭐⭐
title: session-logs
url: https://skills.sh/steipete/clawdis/session-logs
---

# session-logs

skills/steipete/clawdis/session-logs
session-logs
Installation
$ npx skills add https://github.com/steipete/clawdis --skill session-logs
Summary

Search and analyze your complete conversation history using jq and rg.

Session logs stored as append-only JSONL files at ~/.openclaw/agents/<agentId>/sessions/, indexed by session ID with full message transcripts including role, timestamp, content type, and token cost
Extract user messages, assistant responses, tool calls, and metadata using jq filters; search across all sessions or within specific files using rg for keyword matching
Common patterns provided for listing sessions by date, finding specific days, calculating session costs, counting messages, and analyzing tool usage breakdown
Supports filtering by message role ("user", "assistant", "toolResult") and content type ("text", "toolCall", "thinking") for targeted analysis
SKILL.md
session-logs

Search your complete conversation history stored in session JSONL files. Use this when a user references older/parent conversations or asks what was said before.

Trigger

Use this skill when the user asks about prior chats, parent conversations, or historical context that isn't in memory files.

Location

Session logs live under the active state directory: $OPENCLAW_STATE_DIR/agents/<agentId>/sessions/ (default: ~/.openclaw/agents/<agentId>/sessions/). Use the agent=<id> value from the system prompt Runtime line.

sessions.json - Index mapping session keys to session IDs
<session-id>.jsonl - Full conversation transcript per session
Structure

Each .jsonl file contains messages with:

type: "session" (metadata) or "message"
timestamp: ISO timestamp
message.role: "user", "assistant", or "toolResult"
message.content[]: Text, thinking, or tool calls (filter type=="text" for human-readable content)
message.usage.cost.total: Cost per response
Common Queries
List all sessions by date and size
AGENT_ID="<agentId>"
SESSION_DIR="${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/agents/$AGENT_ID/sessions"
for f in "$SESSION_DIR"/*.jsonl; do
  date=$(head -1 "$f" | jq -r '.timestamp' | cut -dT -f1)
  size=$(ls -lh "$f" | awk '{print $5}')
  echo "$date $size $(basename $f)"
done | sort -r

Find sessions from a specific day
AGENT_ID="<agentId>"
SESSION_DIR="${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/agents/$AGENT_ID/sessions"
for f in "$SESSION_DIR"/*.jsonl; do
  head -1 "$f" | jq -r '.timestamp' | grep -q "2026-01-06" && echo "$f"
done

Extract user messages from a session
jq -r 'select(.message.role == "user") | .message.content[]? | select(.type == "text") | .text' <session>.jsonl

Search for keyword in assistant responses
jq -r 'select(.message.role == "assistant") | .message.content[]? | select(.type == "text") | .text' <session>.jsonl | rg -i "keyword"

Get total cost for a session
jq -s '[.[] | .message.usage.cost.total // 0] | add' <session>.jsonl

Daily cost summary
AGENT_ID="<agentId>"
SESSION_DIR="${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/agents/$AGENT_ID/sessions"
for f in "$SESSION_DIR"/*.jsonl; do
  date=$(head -1 "$f" | jq -r '.timestamp' | cut -dT -f1)
  cost=$(jq -s '[.[] | .message.usage.cost.total // 0] | add' "$f")
  echo "$date $cost"
done | awk '{a[$1]+=$2} END {for(d in a) print d, "$"a[d]}' | sort -r

Count messages and tokens in a session
jq -s '{
  messages: length,
  user: [.[] | select(.message.role == "user")] | length,
  assistant: [.[] | select(.message.role == "assistant")] | length,
  first: .[0].timestamp,
  last: .[-1].timestamp
}' <session>.jsonl

Tool usage breakdown
jq -r '.message.content[]? | select(.type == "toolCall") | .name' <session>.jsonl | sort | uniq -c | sort -rn

Search across ALL sessions for a phrase
AGENT_ID="<agentId>"
SESSION_DIR="${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/agents/$AGENT_ID/sessions"
rg -l "phrase" "$SESSION_DIR"/*.jsonl

Tips
Sessions are append-only JSONL (one JSON object per line)
Large sessions can be several MB - use head/tail for sampling
The sessions.json index maps chat providers (discord, whatsapp, etc.) to session IDs
Deleted sessions have .deleted.<timestamp> suffix
Fast text-only hint (low noise)
AGENT_ID="<agentId>"
SESSION_DIR="${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/agents/$AGENT_ID/sessions"
jq -r 'select(.type=="message") | .message.content[]? | select(.type=="text") | .text' "$SESSION_DIR"/<id>.jsonl | rg 'keyword'

Weekly Installs
1.3K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn