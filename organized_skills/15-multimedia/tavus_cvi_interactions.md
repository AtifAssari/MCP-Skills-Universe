---
rating: ⭐⭐
title: tavus-cvi-interactions
url: https://skills.sh/tavus-engineering/tavus-skills/tavus-cvi-interactions
---

# tavus-cvi-interactions

skills/tavus-engineering/tavus-skills/tavus-cvi-interactions
tavus-cvi-interactions
Installation
$ npx skills add https://github.com/tavus-engineering/tavus-skills --skill tavus-cvi-interactions
SKILL.md
Tavus CVI Interactions Protocol

Control live conversations programmatically via WebRTC data channel.

Setup: Daily.js Client
<script src="https://unpkg.com/@daily-co/daily-js"></script>
<script>
const call = window.Daily.createFrame();

// Listen for events from CVI
call.on('app-message', (event) => {
  console.log('CVI event:', event.data);
});

// Join the conversation
call.join({ url: 'YOUR_CONVERSATION_URL' });

// Send interaction
function send(interaction) {
  call.sendAppMessage(interaction, '*');
}
</script>

Interactions You Can Send
Echo: Make Replica Speak Text

Bypass LLM, replica speaks exactly what you provide:

send({
  "message_type": "conversation",
  "event_type": "conversation.echo",
  "conversation_id": "YOUR_CONVERSATION_ID",
  "properties": {
    "modality": "text",
    "text": "Hello! Let me tell you about our product."
  }
});


For streaming audio (base64):

send({
  "message_type": "conversation",
  "event_type": "conversation.echo",
  "conversation_id": "YOUR_CONVERSATION_ID",
  "properties": {
    "modality": "audio",
    "audio": "BASE64_ENCODED_AUDIO",
    "sample_rate": 24000,
    "inference_id": "unique-id",
    "done": "true"
  }
});

Respond: Inject User Input

Treat text as if user spoke it (goes through LLM):

send({
  "message_type": "conversation",
  "event_type": "conversation.respond",
  "conversation_id": "YOUR_CONVERSATION_ID",
  "properties": {
    "text": "What are your pricing plans?"
  }
});

Interrupt: Stop Replica Speaking
send({
  "message_type": "conversation",
  "event_type": "conversation.interrupt",
  "conversation_id": "YOUR_CONVERSATION_ID"
});

Overwrite Context

Replace the entire conversational context:

send({
  "message_type": "conversation",
  "event_type": "conversation.overwrite_context",
  "conversation_id": "YOUR_CONVERSATION_ID",
  "properties": {
    "context": "User is now asking about enterprise features."
  }
});

Append Context

Add to existing context without replacing:

send({
  "message_type": "conversation",
  "event_type": "conversation.append_context",
  "conversation_id": "YOUR_CONVERSATION_ID",
  "properties": {
    "context": "User mentioned they have a team of 50 people."
  }
});

Adjust Sensitivity

Change turn-taking sensitivity mid-conversation:

send({
  "message_type": "conversation",
  "event_type": "conversation.sensitivity",
  "conversation_id": "YOUR_CONVERSATION_ID",
  "properties": {
    "participant_pause_sensitivity": "high",
    "participant_interrupt_sensitivity": "low"
  }
});


Values: low, medium, high

Events You Receive
Utterance (What Was Said)
{
  "event_type": "conversation.utterance",
  "properties": {
    "role": "user",
    "content": "Tell me about your product"
  }
}


Role: user or replica

Replica Started/Stopped Speaking
{
  "event_type": "conversation.replica.started_speaking",
  "properties": {
    "inference_id": "inf-123"
  }
}

{
  "event_type": "conversation.replica.stopped_speaking",
  "properties": {
    "inference_id": "inf-123",
    "duration": 4.5
  }
}

User Started/Stopped Speaking
{
  "event_type": "conversation.user.started_speaking"
}

Tool Call (Function Calling)

When LLM invokes a tool:

{
  "event_type": "conversation.tool_call",
  "properties": {
    "tool_name": "get_weather",
    "arguments": {
      "location": "San Francisco, CA"
    },
    "inference_id": "inf-123"
  }
}


Handle it, then respond with echo or respond interaction.

Perception Analysis

When Raven analyzes the user:

{
  "event_type": "conversation.perception_analysis",
  "properties": {
    "analysis": "User appears engaged, smiling, looking at camera"
  }
}

Replica Interrupted

Fired when replica was interrupted:

{
  "event_type": "conversation.replica.interrupted",
  "properties": {
    "inference_id": "inf-123"
  }
}

Python Client (Daily-Python)
from daily import Daily, CallClient

Daily.init()
client = CallClient()

def on_app_message(message, sender):
    print(f"Received: {message}")

client.set_user_name("bot")
client.join(meeting_url, completion=on_join)

# Send interaction
client.send_app_message({
    "message_type": "conversation",
    "event_type": "conversation.echo",
    "conversation_id": "xxx",
    "properties": {"text": "Hello!"}
})

Common Patterns
Echo Mode with Manual Control
Create persona with pipeline_mode: "echo"
Join conversation with Daily client
Send conversation.echo events to control speech
Send conversation.interrupt to stop
Listen for events to track state
Hybrid: LLM + Manual Injection
Use pipeline_mode: "full" for normal conversation
Inject context with conversation.append_context
Override with conversation.echo when needed
Use conversation.interrupt + conversation.echo for immediate takeover
Weekly Installs
28
Repository
tavus-engineeri…s-skills
GitHub Stars
5
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn