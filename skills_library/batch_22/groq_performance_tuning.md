---
title: groq-performance-tuning
url: https://skills.sh/jeremylongshore/claude-code-plugins-plus-skills/groq-performance-tuning
---

# groq-performance-tuning

skills/jeremylongshore/claude-code-plugins-plus-skills/groq-performance-tuning
groq-performance-tuning
Installation
$ npx skills add https://github.com/jeremylongshore/claude-code-plugins-plus-skills --skill groq-performance-tuning
SKILL.md
Groq Performance Tuning
Overview

Maximize Groq's ultra-low-latency LPU inference. Groq delivers sub-100ms token generation; tuning focuses on streaming efficiency, prompt caching, model selection for speed vs quality, and parallel request orchestration.

Prerequisites
Groq API key with rate limit awareness
groq-sdk npm package installed
Understanding of LLM token economics
Monitoring for TTFT (time to first token)
Instructions
Step 1: Select Optimal Model for Speed
import Groq from 'groq-sdk';

const groq = new Groq({ apiKey: process.env.GROQ_API_KEY });

// Model speed tiers (approximate TTFT):
// llama-3.3-70b-versatile: ~200ms TTFT, best quality
// llama-3.1-8b-instant:    ~80ms TTFT, fastest
// mixtral-8x7b-32768:      ~150ms TTFT, long context  # 32768 = configured value

async function fastCompletion(prompt: string) {
  return groq.chat.completions.create({
    model: 'llama-3.1-8b-instant', // Fastest model
    messages: [{ role: 'user', content: prompt }],
    temperature: 0,       // Deterministic = cacheable
    max_tokens: 256,      // Limit output for speed  # 256 bytes
  });
}

Step 2: Streaming for Perceived Performance
async function streamCompletion(
  messages: any[],
  onToken: (token: string) => void
) {
  const stream = await groq.chat.completions.create({
    model: 'llama-3.3-70b-versatile',
    messages,
    stream: true,
    max_tokens: 1024,  # 1024: 1 KB
  });

  let fullResponse = '';
  for await (const chunk of stream) {
    const token = chunk.choices[0]?.delta?.content || '';
    fullResponse += token;
    onToken(token);
  }
  return fullResponse;
}

Step 3: Semantic Prompt Cache
import { LRUCache } from 'lru-cache';
import { createHash } from 'crypto';

const promptCache = new LRUCache<string, string>({
  max: 500,  # HTTP 500 Internal Server Error
  ttl: 1000 * 60 * 10, // 10 min for deterministic prompts  # 1000: 1 second in ms
});

function hashPrompt(messages: any[], model: string): string {
  return createHash('sha256')
    .update(JSON.stringify({ messages, model }))
    .digest('hex');
}

async function cachedCompletion(messages: any[], model: string) {
  const key = hashPrompt(messages, model);
  const cached = promptCache.get(key);
  if (cached) return cached;

  const response = await groq.chat.completions.create({
    model,
    messages,
    temperature: 0,
  });

  const result = response.choices[0].message.content!;
  promptCache.set(key, result);
  return result;
}

Step 4: Parallel Request Orchestration
async function parallelCompletions(
  prompts: string[],
  concurrency = 5
) {
  const results: string[] = [];

  for (let i = 0; i < prompts.length; i += concurrency) {
    const batch = prompts.slice(i, i + concurrency);
    const batchResults = await Promise.all(
      batch.map(prompt =>
        cachedCompletion(
          [{ role: 'user', content: prompt }],
          'llama-3.1-8b-instant'
        )
      )
    );
    results.push(...batchResults);
  }
  return results;
}

Error Handling
Issue	Cause	Solution
Rate limit 429	Over RPM/TPM quota	Use exponential backoff, batch requests
High TTFT	Using 70b model	Switch to 8b-instant for latency-sensitive tasks
Stream disconnect	Network timeout	Implement reconnection with partial response recovery
Token overflow	max_tokens too high	Set conservative limits, truncate prompts
Examples
Latency Benchmark
async function benchmarkModels(prompt: string) {
  const models = ['llama-3.1-8b-instant', 'llama-3.3-70b-versatile'];

  for (const model of models) {
    const start = performance.now();
    await groq.chat.completions.create({
      model,
      messages: [{ role: 'user', content: prompt }],
      max_tokens: 100,
    });
    console.log(`${model}: ${(performance.now() - start).toFixed(0)}ms`);
  }
}

Resources
Groq API Documentation
Groq Rate Limits
Groq Model Cards
Output
Configuration files or code changes applied to the project
Validation report confirming correct implementation
Summary of changes made and their rationale
Weekly Installs
25
Repository
jeremylongshore…s-skills
GitHub Stars
2.1K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass