---
rating: ⭐⭐⭐
title: chat-ui
url: https://skills.sh/inference-sh/skills/chat-ui
---

# chat-ui

skills/inference-sh/skills/chat-ui
chat-ui
Installation
$ npx skills add https://github.com/inference-sh/skills --skill chat-ui
SKILL.md
Chat UI Components

Chat building blocks from ui.inference.sh.

Quick Start
# Install chat components
npx shadcn@latest add https://ui.inference.sh/r/chat.json

Components
Chat Container
import { ChatContainer } from "@/registry/blocks/chat/chat-container"

<ChatContainer>
  {/* messages go here */}
</ChatContainer>

Messages
import { ChatMessage } from "@/registry/blocks/chat/chat-message"

<ChatMessage
  role="user"
  content="Hello, how can you help me?"
/>

<ChatMessage
  role="assistant"
  content="I can help you with many things!"
/>

Chat Input
import { ChatInput } from "@/registry/blocks/chat/chat-input"

<ChatInput
  onSubmit={(message) => handleSend(message)}
  placeholder="Type a message..."
  disabled={isLoading}
/>

Typing Indicator
import { TypingIndicator } from "@/registry/blocks/chat/typing-indicator"

{isTyping && <TypingIndicator />}

Full Example
import {
  ChatContainer,
  ChatMessage,
  ChatInput,
  TypingIndicator,
} from "@/registry/blocks/chat"

export function Chat() {
  const [messages, setMessages] = useState([])
  const [isLoading, setIsLoading] = useState(false)

  const handleSend = async (content: string) => {
    setMessages(prev => [...prev, { role: 'user', content }])
    setIsLoading(true)
    // Send to API...
    setIsLoading(false)
  }

  return (
    <ChatContainer>
      {messages.map((msg, i) => (
        <ChatMessage key={i} role={msg.role} content={msg.content} />
      ))}
      {isLoading && <TypingIndicator />}
      <ChatInput onSubmit={handleSend} disabled={isLoading} />
    </ChatContainer>
  )
}

Message Variants
Role	Description
user	User messages (right-aligned)
assistant	AI responses (left-aligned)
system	System messages (centered)
Styling

Components use Tailwind CSS and shadcn/ui design tokens:

<ChatMessage
  role="assistant"
  content="Hello!"
  className="bg-muted"
/>

Related Skills
# Full agent component (recommended)
npx skills add inference-sh/skills@agent-ui

# Declarative widgets
npx skills add inference-sh/skills@widgets-ui

# Markdown rendering
npx skills add inference-sh/skills@markdown-ui

Documentation
Chatting with Agents - Building chat interfaces
Agent UX Patterns - Chat UX best practices
Real-Time Streaming - Streaming responses

Component docs: ui.inference.sh/blocks/chat

Weekly Installs
343
Repository
inference-sh/skills
GitHub Stars
395
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass