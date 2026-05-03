---
title: xmtp-docs
url: https://skills.sh/xmtp/skills/xmtp-docs
---

# xmtp-docs

skills/xmtp/skills/xmtp-docs
xmtp-docs
Installation
$ npx skills add https://github.com/xmtp/skills --skill xmtp-docs
SKILL.md
XMTP Documentation Lookup

Query current XMTP documentation to find accurate SDK patterns before writing code.

Why This Skill Exists

CRITICAL: Never use training data for XMTP SDK methods. The SDK evolves frequently and method names change between versions. All method names, signatures, and patterns MUST be looked up from current documentation.

How to Query
Step 1: Find the right page

Use the docs index to find which page has what you need:

WebFetch({
  url: "https://docs.xmtp.org/llms.txt",
  prompt: "Find the page URL for [topic]"
})

Step 2: Fetch that page

Fetch the specific page for complete code examples:

WebFetch({
  url: "https://docs.xmtp.org[path-from-step-1]",
  prompt: "Extract [specific feature] with code examples"
})

Examples

Find how to create a client:

WebFetch({ url: "https://docs.xmtp.org/llms.txt", prompt: "Find the page URL for creating an XMTP client" })
// Returns: /chat-apps/core-messaging/create-a-client

WebFetch({ url: "https://docs.xmtp.org/chat-apps/core-messaging/create-a-client", prompt: "Extract how to create a client with code examples" })


Find how to stream messages:

WebFetch({ url: "https://docs.xmtp.org/llms.txt", prompt: "Find the page URL for streaming messages" })
// Returns: /chat-apps/list-stream-sync/stream

WebFetch({ url: "https://docs.xmtp.org/chat-apps/list-stream-sync/stream", prompt: "Extract streaming patterns with code examples" })

Tips
Always use the index first - Don't guess URLs; they change when docs reorganize
Ask for code examples - Docs include examples for Browser, Node, Kotlin, and Swift
One topic per query - Focused queries return better results
Don't use llms-full.txt - It's 500KB+ and WebFetch can't reliably search it
Weekly Installs
27
Repository
xmtp/skills
GitHub Stars
3
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn