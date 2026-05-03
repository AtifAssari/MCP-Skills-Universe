---
title: azure-ai
url: https://skills.sh/microsoft/azure-skills/azure-ai
---

# azure-ai

skills/microsoft/azure-skills/azure-ai
azure-ai
Installation
$ npx skills add https://github.com/microsoft/azure-skills --skill azure-ai
Summary

Access Azure AI Search, Speech, OpenAI, and Document Intelligence services through unified MCP tools.

AI Search supports full-text, vector, hybrid, and semantic search with built-in AI enrichment for entity extraction and OCR
Speech service handles real-time and batch speech-to-text transcription, text-to-speech synthesis with neural voices, and speaker diarization
MCP tools provide direct access: azure__search for index queries and azure__speech for transcription and synthesis
SDK references available for Python, TypeScript, .NET, and Java across all services; enable via /azure:setup or /mcp if MCP is not active
SKILL.md
Azure AI Services
Services
Service	Use When	MCP Tools	CLI
AI Search	Full-text, vector, hybrid search	azure__search	az search
Speech	Speech-to-text, text-to-speech	azure__speech	-
OpenAI	GPT models, embeddings, DALL-E	-	az cognitiveservices
Document Intelligence	Form extraction, OCR	-	-
MCP Server (Preferred)

When Azure MCP is enabled:

AI Search
azure__search with command search_index_list - List search indexes
azure__search with command search_index_get - Get index details
azure__search with command search_query - Query search index
Speech
azure__speech with command speech_transcribe - Speech to text
azure__speech with command speech_synthesize - Text to speech

If Azure MCP is not enabled: Run /azure:setup or enable via /mcp.

AI Search Capabilities
Feature	Description
Full-text search	Linguistic analysis, stemming
Vector search	Semantic similarity with embeddings
Hybrid search	Combined keyword + vector
AI enrichment	Entity extraction, OCR, sentiment
Speech Capabilities
Feature	Description
Speech-to-text	Real-time and batch transcription
Text-to-speech	Neural voices, SSML support
Speaker diarization	Identify who spoke when
Custom models	Domain-specific vocabulary
SDK Quick References

For programmatic access to these services, see the condensed SDK guides:

AI Search: Python | TypeScript | .NET
OpenAI: .NET
Vision: Python | Java
Transcription: Python
Translation: Python | TypeScript
Document Intelligence: .NET | TypeScript
Content Safety: Python | TypeScript | Java
Service Details

For deep documentation on specific services:

AI Search indexing and queries -> Azure AI Search documentation
Speech transcription patterns -> Azure AI Speech documentation
Weekly Installs
276.2K
Repository
microsoft/azure-skills
GitHub Stars
796
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass