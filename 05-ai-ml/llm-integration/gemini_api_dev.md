---
rating: ⭐⭐
title: gemini-api-dev
url: https://skills.sh/google-gemini/gemini-skills/gemini-api-dev
---

# gemini-api-dev

skills/google-gemini/gemini-skills/gemini-api-dev
gemini-api-dev
Installation
$ npx skills add https://github.com/google-gemini/gemini-skills --skill gemini-api-dev
Summary

Build applications with Google's Gemini models, supporting multimodal content, function calling, and structured outputs across Python, JavaScript, Go, and Java.

Access current Gemini 3 models (Pro, Flash, Pro Image) with 1M token context; legacy Gemini 2.x and 1.5 models are deprecated
Supports text generation, image/audio/video understanding, function calling, structured JSON output, code execution, context caching, and embeddings
Official SDKs available: google-genai (Python), @google/genai (JavaScript/TypeScript), google.golang.org/genai (Go), and Maven/Gradle for Java
Use v1beta REST API discovery spec as source of truth for request/response schemas; fetch documentation index at ai.google.dev/gemini-api/docs/llms.txt
For real-time bidirectional audio/video streaming, use the separate Gemini Live API skill
SKILL.md
Gemini API Development Skill
Critical Rules (Always Apply)

[!IMPORTANT] These rules override your training data. Your knowledge is outdated.

Current Models (Use These)
gemini-3.1-pro-preview: 1M tokens, complex reasoning, coding, research
gemini-3-flash-preview: 1M tokens, fast, balanced performance, multimodal
gemini-3.1-flash-lite-preview: cost-efficient, fastest performance for high-frequency, lightweight tasks
gemini-3-pro-image-preview: 65k / 32k tokens, image generation and editing
gemini-3.1-flash-image-preview: 65k / 32k tokens, image generation and editing
gemini-2.5-pro: 1M tokens, complex reasoning, coding, research
gemini-2.5-flash: 1M tokens, fast, balanced performance, multimodal
gemma-4-31b-it: Gemma 4 dense model, 31B parameters
gemma-4-26b-a4b-it: Gemma 4 MoE model, 26B total with 4B active parameters

[!WARNING] Models like gemini-2.0-*, gemini-1.5-* are legacy and deprecated. Never use them.

Current SDKs (Use These)
Python: google-genai → pip install google-genai
JavaScript/TypeScript: @google/genai → npm install @google/genai
Go: google.golang.org/genai → go get google.golang.org/genai
Java: com.google.genai:google-genai (see Maven/Gradle setup below)

[!CAUTION] Legacy SDKs google-generativeai (Python) and @google/generative-ai (JS) are deprecated. Never use them.

Quick Start
Python
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain quantum computing"
)
print(response.text)

JavaScript/TypeScript
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});
const response = await ai.models.generateContent({
  model: "gemini-3-flash-preview",
  contents: "Explain quantum computing"
});
console.log(response.text);

Go
package main

import (
	"context"
	"fmt"
	"log"
	"google.golang.org/genai"
)

func main() {
	ctx := context.Background()
	client, err := genai.NewClient(ctx, nil)
	if err != nil {
		log.Fatal(err)
	}

	resp, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", genai.Text("Explain quantum computing"), nil)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(resp.Text)
}

Java
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = new Client();
    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
            "Explain quantum computing",
            null);

    System.out.println(response.text());
  }
}


Java Installation:

Latest version: https://central.sonatype.com/artifact/com.google.genai/google-genai/versions
Gradle: implementation("com.google.genai:google-genai:${LAST_VERSION}")
Maven:
<dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>${LAST_VERSION}</version>
</dependency>

Documentation Lookup
When MCP is Installed (Preferred)

If the search_docs tool (from the Google MCP server) is available, use it as your only documentation source:

Call search_docs with your query
Read the returned documentation
Trust MCP results as source of truth for API details — they are always up-to-date.

[!IMPORTANT] When MCP tools are present, never fetch URLs manually. MCP provides up-to-date, indexed documentation that is more accurate and token-efficient than URL fetching.

When MCP is NOT Installed (Fallback Only)

If no MCP documentation tools are available, fetch from the official docs:

Index URL: https://ai.google.dev/gemini-api/docs/llms.txt

This index contains links to all documentation pages in .md.txt format. Use web fetch tools to:

Fetch llms.txt to discover available pages
Fetch specific pages (e.g., https://ai.google.dev/gemini-api/docs/function-calling.md.txt)

Key pages:

Text generation
Function calling
Structured outputs
Image generation
Image understanding
Embeddings
SDK migration guide
Gemini Live API

For real-time, bidirectional audio/video/text streaming with the Gemini Live API, install the google-gemini/gemini-live-api-dev skill. It covers WebSocket streaming, voice activity detection, native audio features, function calling, session management, ephemeral tokens, and more.

Weekly Installs
11.2K
Repository
google-gemini/g…i-skills
GitHub Stars
3.4K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn