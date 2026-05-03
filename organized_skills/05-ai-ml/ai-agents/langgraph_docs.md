---
rating: ⭐⭐
title: langgraph-docs
url: https://skills.sh/langchain-ai/deepagents/langgraph-docs
---

# langgraph-docs

skills/langchain-ai/deepagents/langgraph-docs
langgraph-docs
Installation
$ npx skills add https://github.com/langchain-ai/deepagents --skill langgraph-docs
Summary

Access LangGraph documentation to build stateful agents and multi-agent workflows.

Fetches official LangGraph Python docs covering state machines, graph-based agent design, and human-in-the-loop patterns
Prioritizes relevant documentation by query type: implementation guides for how-to questions, concept pages for theory, tutorials for end-to-end examples, and API references for technical details
Automatically selects 2–4 most relevant documentation URLs and retrieves their content to answer questions about agent orchestration and LangGraph APIs
Falls back to direct documentation link if fetch operations fail, ensuring users can access source material independently
SKILL.md
langgraph-docs
Workflow
1. Fetch the Documentation Index

Use fetch_url to read: https://docs.langchain.com/llms.txt

This returns a structured list of all available documentation with descriptions.

2. Select Relevant Documentation

Identify 2-4 most relevant URLs from the index. Prioritize:

Implementation questions — specific how-to guides
Conceptual questions — core concept pages
End-to-end examples — tutorials
API details — reference docs
3. Fetch and Apply

Use fetch_url on the selected URLs, then complete the user's request using the documentation content.

If fetch_url fails or returns empty content, retry once. If it fails again, inform the user and suggest checking https://langchain-ai.github.io/langgraph/ directly.

Weekly Installs
2.9K
Repository
langchain-ai/deepagents
GitHub Stars
22.1K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn