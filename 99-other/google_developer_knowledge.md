---
title: google-developer-knowledge
url: https://skills.sh/cnemri/google-genai-skills/google-developer-knowledge
---

# google-developer-knowledge

skills/cnemri/google-genai-skills/google-developer-knowledge
google-developer-knowledge
Installation
$ npx skills add https://github.com/cnemri/google-genai-skills --skill google-developer-knowledge
SKILL.md
Google Developer Knowledge

Use this skill to search and retrieve content from Google's public developer documentation corpus using the Developer Knowledge API.

This skill uses simple bash scripts with curl (no dependencies required).

Prerequisites

Enable the API: Enable the Developer Knowledge API in your Google Cloud project.

Create an API Key:

Go to the Credentials page
Click Create credentials → API key
Restrict the key to Developer Knowledge API only

Set Environment Variable:

DEVELOPERKNOWLEDGE_API_KEY: Your Developer Knowledge API key
Searchable Corpus

The API searches these domains:

ai.google.dev
developer.android.com
developer.chrome.com
developers.google.com
docs.cloud.google.com
firebase.google.com
web.dev
www.tensorflow.org
Usage
1. Search for Documents

Search for document chunks matching a query. Returns snippets and parent document references.

./skills/google-developer-knowledge/scripts/search_docs.sh "How to use Gemini API in Python"


With pagination:

./skills/google-developer-knowledge/scripts/search_docs.sh "BigQuery" --page-size 10

2. Get a Single Document

Retrieve the full content of a document using its name from search results.

./skills/google-developer-knowledge/scripts/get_document.sh "documents/ai.google.dev/gemini-api/docs/get-started/python"


Save to file:

./skills/google-developer-knowledge/scripts/get_document.sh "documents/ai.google.dev/..." --output doc.json

3. Batch Get Documents

Retrieve up to 20 documents in a single API call.

./skills/google-developer-knowledge/scripts/batch_get_documents.sh \
  "documents/ai.google.dev/gemini-api/docs/get-started/python" \
  "documents/ai.google.dev/gemini-api/docs/models"

Options

search_docs.sh

query: The search query (required)
--page-size: Number of results (1-20, default 5)
--page-token: Token for next page of results
--output: Save results to JSON file

get_document.sh

name: Document name from search results (required)
--output: Save content to file

batch_get_documents.sh

names: Space-separated document names (up to 20)
--output: Save all documents to directory
Weekly Installs
50
Repository
cnemri/google-g…i-skills
GitHub Stars
119
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass