---
rating: ⭐⭐
title: ai sdk v6 ui
url: https://skills.sh/blockmatic/basilic/ai-sdk-v6-ui
---

# ai sdk v6 ui

skills/blockmatic/basilic/AI SDK v6 UI
AI SDK v6 UI
Installation
$ npx skills add https://github.com/blockmatic/basilic --skill 'AI SDK v6 UI'
SKILL.md
Skill: ai-sdk-ui
Scope
Applies to: React chat interfaces with Vercel AI SDK v5/v6, streaming UI patterns, tool approval workflows, agent integration
Does NOT cover: Backend AI implementation (see ai-sdk-core), Generative UI/RSC
Assumptions
AI SDK v5.0.99+ (stable) or v6.0.0-beta.108+ (beta)
React 18+ (React 19 supported)
Next.js 14+ (13.4+ works)
@ai-sdk/react package
Principles
Use useChat for chat interfaces with streaming
Use useCompletion for text completion (non-chat)
Use useObject for structured data generation
Use useAssistant for OpenAI-compatible assistant APIs
Use streaming for better UX (show tokens as they arrive)
Handle tool approval workflows with addToolApprovalResponse (v6)
Use controlled mode for dynamic body values (avoid stale values)
Use toDataStreamResponse() in App Router, pipeDataStreamToResponse() in Pages Router
Constraints
MUST
Use streaming responses (toDataStreamResponse() or pipeDataStreamToResponse())
Use controlled mode when body values change (sendMessage with data instead of body option)
Handle loading states (isLoading) and errors (error)
SHOULD
Use stop function to allow users to cancel generation
Auto-scroll to latest message during streaming
Show loading indicators during generation
Use InferAgentUIMessage (v6) for type-safe agent integration
AVOID
Using body option with dynamic values (causes stale values)
Non-streaming responses (poor UX)
Infinite loops in useEffect (only depend on messages, not callbacks)
Mixing v5 and v6 APIs without migration
Interactions
Uses ai-sdk-core for backend implementation
Works with nextjs App Router and Pages Router
Uses Zod for schema validation (see typescript)
Patterns
Basic Chat
import { useChat } from '@ai-sdk/react'

export default function Chat() {
  const { messages, input, handleInputChange, handleSubmit, isLoading } = useChat({
    api: '/api/chat',
  })

  return (
    <form onSubmit={handleSubmit}>
      <input value={input} onChange={handleInputChange} />
      <button disabled={isLoading}>Send</button>
    </form>
  )
}

Tool Approval (v6)
import { useChat } from '@ai-sdk/react'

const { messages, addToolApprovalResponse } = useChat({
  api: '/api/chat',
})

// Handle approval
addToolApprovalResponse({
  toolCallId: 'id',
  approved: true,
})


See Templates and Next.js Integration for detailed examples.

References
Next.js Integration - App Router and Pages Router patterns
Streaming Patterns - UI streaming best practices
Top UI Errors - Common error solutions
Resources
AI SDK UI Docs
useChat Hook
Troubleshooting
Weekly Installs
–
Repository
blockmatic/basilic
GitHub Stars
88
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass