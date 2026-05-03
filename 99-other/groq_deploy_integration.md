---
title: groq-deploy-integration
url: https://skills.sh/jeremylongshore/claude-code-plugins-plus-skills/groq-deploy-integration
---

# groq-deploy-integration

skills/jeremylongshore/claude-code-plugins-plus-skills/groq-deploy-integration
groq-deploy-integration
Installation
$ npx skills add https://github.com/jeremylongshore/claude-code-plugins-plus-skills --skill groq-deploy-integration
SKILL.md
Groq Deploy Integration
Overview

Deploy applications using Groq's inference API to Vercel Edge, Cloud Run, Docker, and other platforms. Groq's sub-200ms latency makes it ideal for edge deployments and real-time applications.

Prerequisites
Groq API key stored in GROQ_API_KEY
Application using groq-sdk package
Platform CLI installed (vercel, docker, or gcloud)
Instructions
Step 1: Vercel Edge Function
// app/api/chat/route.ts (Next.js App Router)
import Groq from "groq-sdk";

export const runtime = "edge";

export async function POST(req: Request) {
  const groq = new Groq({ apiKey: process.env.GROQ_API_KEY! });
  const { messages, stream: useStream } = await req.json();

  if (useStream) {
    const stream = await groq.chat.completions.create({
      model: "llama-3.3-70b-versatile",
      messages,
      stream: true,
      max_tokens: 2048,
    });

    const encoder = new TextEncoder();
    const readable = new ReadableStream({
      async start(controller) {
        for await (const chunk of stream) {
          const content = chunk.choices[0]?.delta?.content;
          if (content) {
            controller.enqueue(
              encoder.encode(`data: ${JSON.stringify({ content })}\n\n`)
            );
          }
        }
        controller.enqueue(encoder.encode("data: [DONE]\n\n"));
        controller.close();
      },
    });

    return new Response(readable, {
      headers: {
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        Connection: "keep-alive",
      },
    });
  }

  const completion = await groq.chat.completions.create({
    model: "llama-3.3-70b-versatile",
    messages,
    max_tokens: 2048,
  });

  return Response.json(completion);
}

Step 2: Vercel Deployment
set -euo pipefail
# Set secret
vercel env add GROQ_API_KEY production

# Deploy
vercel --prod

Step 3: Docker Container
FROM node:20-slim AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-slim
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json .
EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=5s CMD curl -sf http://localhost:3000/health || exit 1
CMD ["node", "dist/index.js"]

Step 4: Cloud Run Deployment
set -euo pipefail
# Store API key in Secret Manager
echo -n "$GROQ_API_KEY" | gcloud secrets create groq-api-key --data-file=-

# Deploy with streaming support
gcloud run deploy groq-api \
  --source . \
  --region us-central1 \
  --set-secrets=GROQ_API_KEY=groq-api-key:latest \
  --min-instances=1 \
  --max-instances=10 \
  --cpu=1 --memory=512Mi \
  --allow-unauthenticated \
  --timeout=60s

Step 5: Express Server with Health Check
import express from "express";
import Groq from "groq-sdk";

const app = express();
const groq = new Groq();

app.use(express.json());

// Health check -- uses cheapest model with minimal tokens
app.get("/health", async (_req, res) => {
  try {
    const start = performance.now();
    await groq.chat.completions.create({
      model: "llama-3.1-8b-instant",
      messages: [{ role: "user", content: "OK" }],
      max_tokens: 1,
    });
    res.json({
      status: "healthy",
      groq: { connected: true, latencyMs: Math.round(performance.now() - start) },
    });
  } catch (err: any) {
    res.status(503).json({
      status: "unhealthy",
      groq: { connected: false, error: err.message },
    });
  }
});

// Chat endpoint with streaming
app.post("/api/chat", async (req, res) => {
  const { messages, model = "llama-3.3-70b-versatile" } = req.body;

  if (req.headers.accept === "text/event-stream") {
    res.writeHead(200, {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache",
      Connection: "keep-alive",
    });

    const stream = await groq.chat.completions.create({
      model,
      messages,
      stream: true,
      max_tokens: 2048,
    });

    for await (const chunk of stream) {
      const content = chunk.choices[0]?.delta?.content;
      if (content) {
        res.write(`data: ${JSON.stringify({ content })}\n\n`);
      }
    }
    res.write("data: [DONE]\n\n");
    res.end();
  } else {
    const completion = await groq.chat.completions.create({
      model,
      messages,
      max_tokens: 2048,
    });
    res.json(completion);
  }
});

app.listen(3000, () => console.log("Groq API server on :3000"));

Step 6: Vercel AI SDK Integration
// Using @ai-sdk/groq for Vercel AI SDK
import { createGroq } from "@ai-sdk/groq";
import { streamText } from "ai";

const groq = createGroq({ apiKey: process.env.GROQ_API_KEY });

export async function POST(req: Request) {
  const { messages } = await req.json();

  const result = streamText({
    model: groq("llama-3.3-70b-versatile"),
    messages,
  });

  return result.toDataStreamResponse();
}

Environment Variable Config
Platform	Command
Vercel	vercel env add GROQ_API_KEY production
Cloud Run	gcloud secrets create groq-api-key --data-file=-
Fly.io	fly secrets set GROQ_API_KEY=gsk_...
Railway	railway variables set GROQ_API_KEY=gsk_...
Docker	-e GROQ_API_KEY=gsk_... or Docker secrets
Error Handling
Issue	Cause	Solution
Rate limited (429)	Too many requests	Implement request queuing with backoff
Edge timeout	Response > 25s	Use streaming for long completions
Model unavailable	Capacity or deprecation	Fall back to llama-3.1-8b-instant
Cold start latency	Serverless function init	Set min-instances=1 on Cloud Run
API key not found	Secret not configured	Check platform secret config
Resources
Groq API Documentation
Vercel AI SDK + Groq
Groq Client Libraries
Next Steps

For multi-environment setup, see groq-multi-env-setup.

Weekly Installs
26
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