---
rating: ⭐⭐
title: tavus-cvi-ui
url: https://skills.sh/tavus-engineering/tavus-skills/tavus-cvi-ui
---

# tavus-cvi-ui

skills/tavus-engineering/tavus-skills/tavus-cvi-ui
tavus-cvi-ui
Installation
$ npx skills add https://github.com/tavus-engineering/tavus-skills --skill tavus-cvi-ui
SKILL.md
Tavus CVI React UI Components

Pre-built React components for embedding CVI conversations.

Quick Setup (Vite)
npm create vite@latest my-app -- --template react-ts
cd my-app
npm install
npx @tavus/cvi-ui@latest init
npx @tavus/cvi-ui@latest add conversation


Creates:

src/components/cvi/components/
├── cvi-provider.tsx
└── conversation.tsx


Create cvi-components.json in project root:

{
  "tsx": true
}

Environment Variables

.env in project root:

VITE_TAVUS_API_KEY=your_api_key
VITE_REPLICA_ID=rfe12d8b9597
VITE_PERSONA_ID=pdced222244b

Basic Implementation
import { useState } from "react";
import { CVIProvider } from "./components/cvi/components/cvi-provider";
import { Conversation } from "./components/cvi/components/conversation";

export default function App() {
  const [url, setUrl] = useState<string | null>(null);

  const startConversation = async () => {
    const res = await fetch("https://tavusapi.com/v2/conversations", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": import.meta.env.VITE_TAVUS_API_KEY,
      },
      body: JSON.stringify({
        replica_id: import.meta.env.VITE_REPLICA_ID,
        persona_id: import.meta.env.VITE_PERSONA_ID,
      }),
    });
    const data = await res.json();
    setUrl(data.conversation_url);
  };

  return (
    <CVIProvider>
      {!url ? (
        <button onClick={startConversation}>Start</button>
      ) : (
        <Conversation 
          conversationUrl={url} 
          onLeave={() => setUrl(null)} 
        />
      )}
    </CVIProvider>
  );
}

Component: CVIProvider

Wraps your app, provides CVI context:

import { CVIProvider } from "./components/cvi/components/cvi-provider";

function App() {
  return (
    <CVIProvider>
      {/* Your app */}
    </CVIProvider>
  );
}

Component: Conversation

The main video conversation UI:

<Conversation
  conversationUrl={url}
  onLeave={() => setUrl(null)}
/>


Required: Parent container must have defined dimensions.

<div style={{ width: "100%", height: "600px" }}>
  <Conversation conversationUrl={url} onLeave={handleLeave} />
</div>

Hooks
useAppMessage

Listen for CVI events:

import { useAppMessage } from "./components/cvi/hooks/use-app-message";

function MyComponent() {
  useAppMessage((event) => {
    if (event.event_type === "conversation.utterance") {
      console.log("Said:", event.properties.content);
    }
  });
  
  return <div>...</div>;
}

useSendAppMessage

Send interactions to CVI:

import { useSendAppMessage } from "./components/cvi/hooks/use-send-app-message";

function Controls() {
  const send = useSendAppMessage();
  
  const interrupt = () => {
    send({
      message_type: "conversation",
      event_type: "conversation.interrupt",
      conversation_id: "xxx"
    });
  };
  
  return <button onClick={interrupt}>Stop</button>;
}

Alternative: iframe Embedding

For non-React or quick integration:

<iframe
  src="CONVERSATION_URL"
  allow="camera; microphone; display-capture"
  style="width: 100%; height: 600px; border: none;"
></iframe>

Server-Side API Calls (Recommended)

Keep API key on server:

// pages/api/conversation.ts (Next.js)
export default async function handler(req, res) {
  const response = await fetch("https://tavusapi.com/v2/conversations", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": process.env.TAVUS_API_KEY,
    },
    body: JSON.stringify({
      replica_id: process.env.REPLICA_ID,
      persona_id: process.env.PERSONA_ID,
    }),
  });
  
  const data = await response.json();
  res.json({ conversation_url: data.conversation_url });
}


Client calls your API:

const res = await fetch("/api/conversation", { method: "POST" });
const { conversation_url } = await res.json();

Styling the Conversation

Wrap in styled container:

<div style={{
  width: "100%",
  maxWidth: "900px",
  margin: "0 auto",
  borderRadius: "12px",
  overflow: "hidden",
  boxShadow: "0 4px 20px rgba(0,0,0,0.15)",
}}>
  <Conversation conversationUrl={url} onLeave={onLeave} />
</div>

HairCheck Component

Pre-call device check:

npx @tavus/cvi-ui@latest add haircheck

import { HairCheck } from "./components/cvi/components/haircheck";

<HairCheck onComplete={() => setShowConversation(true)} />

Example Projects
CVI UI Conversation
CVI UI Haircheck + Conversation
Santa Demo
Weekly Installs
27
Repository
tavus-engineeri…s-skills
GitHub Stars
5
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn