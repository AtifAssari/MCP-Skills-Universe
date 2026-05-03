---
rating: ⭐⭐
title: langgraph-docs
url: https://skills.sh/langchain-ai/deepagentsjs/langgraph-docs
---

# langgraph-docs

skills/langchain-ai/deepagentsjs/langgraph-docs
langgraph-docs
Installation
$ npx skills add https://github.com/langchain-ai/deepagentsjs --skill langgraph-docs
SKILL.md
langgraph-docs
Overview

This skill explains how to access LangGraph Python documentation to help answer questions and guide implementation.

Instructions
1. Fetch the Documentation Index

Use the fetch_url tool to read the following URL: https://docs.langchain.com/llms.txt

This provides a structured list of all available documentation with descriptions.

2. Select Relevant Documentation

Based on the question, identify 2-4 most relevant documentation URLs from the index. Prioritize:

Specific how-to guides for implementation questions
Core concept pages for understanding questions
Tutorials for end-to-end examples
Reference docs for API details
3. Fetch Selected Documentation

Use the fetch_url tool to read the selected documentation URLs.

4. Provide Accurate Guidance

After reading the documentation, complete the users request.

Weekly Installs
38
Repository
langchain-ai/de…agentsjs
GitHub Stars
1.2K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn