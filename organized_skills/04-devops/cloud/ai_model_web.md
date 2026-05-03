---
rating: ⭐⭐
title: ai-model-web
url: https://skills.sh/tencentcloudbase/skills/ai-model-web
---

# ai-model-web

skills/tencentcloudbase/skills/ai-model-web
ai-model-web
Installation
$ npx skills add https://github.com/tencentcloudbase/skills --skill ai-model-web
Summary

AI text generation and streaming for browser applications via CloudBase SDK.

Supports two providers: Hunyuan (recommended: hunyuan-2.0-instruct-20251111) and DeepSeek (recommended: deepseek-v3.2)
Two core methods: generateText() for non-streaming responses and streamText() for incremental text chunks with async iteration
Requires @cloudbase/js-sdk initialization with anonymous authentication and publishable API key from CloudBase console
Not suitable for Node.js backends, WeChat Mini Programs, or image generation; use alternative skills for those contexts
SKILL.md
Standalone Install Note

If this environment only installed the current skill, start from the CloudBase main entry and use the published cloudbase/references/... paths for sibling skills.

CloudBase main entry: https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/SKILL.md
Current skill raw source: https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/ai-model-web/SKILL.md

Keep local references/... paths for files that ship with the current skill directory. When this file points to a sibling skill such as auth-tool or web-development, use the standalone fallback URL shown next to that reference.

When to use this skill

Use this skill for calling AI models in browser/Web applications using @cloudbase/js-sdk.

Use it when you need to:

Integrate AI text generation in a frontend Web app
Stream AI responses for better user experience
Call Hunyuan or DeepSeek models from browser

Do NOT use for:

Node.js backend or cloud functions → use ai-model-nodejs skill
WeChat Mini Program → use ai-model-wechat skill
Image generation → use ai-model-nodejs skill (Node SDK only)
HTTP API integration → use http-api skill
Available Providers and Models

CloudBase provides these built-in providers and models:

Provider	Models	Recommended
hunyuan-exp	hunyuan-turbos-latest, hunyuan-t1-latest, hunyuan-2.0-thinking-20251109, hunyuan-2.0-instruct-20251111	✅ hunyuan-2.0-instruct-20251111
deepseek	deepseek-r1-0528, deepseek-v3-0324, deepseek-v3.2	✅ deepseek-v3.2
Installation
npm install @cloudbase/js-sdk

Initialization
import cloudbase from "@cloudbase/js-sdk";

const app = cloudbase.init({
  env: "<YOUR_ENV_ID>",
  accessKey: "<YOUR_PUBLISHABLE_KEY>"  // Get from CloudBase console
});

const auth = app.auth();
await auth.signInAnonymously();

const ai = app.ai();


Important notes:

Always use synchronous initialization with top-level import
User must be authenticated before using AI features
Get accessKey from CloudBase console
generateText() - Non-streaming
const model = ai.createModel("hunyuan-exp");

const result = await model.generateText({
  model: "hunyuan-2.0-instruct-20251111",  // Recommended model
  messages: [{ role: "user", content: "你好，请你介绍一下李白" }],
});

console.log(result.text);           // Generated text string
console.log(result.usage);          // { prompt_tokens, completion_tokens, total_tokens }
console.log(result.messages);       // Full message history
console.log(result.rawResponses);   // Raw model responses

streamText() - Streaming
const model = ai.createModel("hunyuan-exp");

const res = await model.streamText({
  model: "hunyuan-2.0-instruct-20251111",  // Recommended model
  messages: [{ role: "user", content: "你好，请你介绍一下李白" }],
});

// Option 1: Iterate text stream (recommended)
for await (let text of res.textStream) {
  console.log(text);  // Incremental text chunks
}

// Option 2: Iterate data stream for full response data
for await (let data of res.dataStream) {
  console.log(data);  // Full response chunk with metadata
}

// Option 3: Get final results
const messages = await res.messages;  // Full message history
const usage = await res.usage;        // Token usage

Error Handling Pattern
const model = ai.createModel("deepseek");

try {
  const result = await model.generateText({
    model: "deepseek-v3.2",
    messages: [{ role: "user", content: "Generate a concise onboarding checklist" }],
  });

  console.log(result.text);
} catch (error) {
  console.error("Failed to call CloudBase AI from Web", error);
}

Type Definitions
interface BaseChatModelInput {
  model: string;                        // Required: model name
  messages: Array<ChatModelMessage>;    // Required: message array
  temperature?: number;                 // Optional: sampling temperature
  topP?: number;                        // Optional: nucleus sampling
}

type ChatModelMessage =
  | { role: "user"; content: string }
  | { role: "system"; content: string }
  | { role: "assistant"; content: string };

interface GenerateTextResult {
  text: string;                         // Generated text
  messages: Array<ChatModelMessage>;    // Full message history
  usage: Usage;                         // Token usage
  rawResponses: Array<unknown>;         // Raw model responses
  error?: unknown;                      // Error if any
}

interface StreamTextResult {
  textStream: AsyncIterable<string>;    // Incremental text stream
  dataStream: AsyncIterable<DataChunk>; // Full data stream
  messages: Promise<ChatModelMessage[]>;// Final message history
  usage: Promise<Usage>;                // Final token usage
  error?: unknown;                      // Error if any
}

interface Usage {
  prompt_tokens: number;
  completion_tokens: number;
  total_tokens: number;
}

Best Practices
Use streaming for long responses - Better user experience
Handle errors gracefully - Wrap AI calls in try/catch
Keep accessKey secure - Use publishable key, not secret key
Initialize early - Initialize SDK in app entry point
Ensure authentication - User must be signed in before AI calls
Weekly Installs
697
Repository
tencentcloudbase/skills
GitHub Stars
52
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass