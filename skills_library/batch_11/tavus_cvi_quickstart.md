---
title: tavus-cvi-quickstart
url: https://skills.sh/tavus-engineering/tavus-skills/tavus-cvi-quickstart
---

# tavus-cvi-quickstart

skills/tavus-engineering/tavus-skills/tavus-cvi-quickstart
tavus-cvi-quickstart
Installation
$ npx skills add https://github.com/tavus-engineering/tavus-skills --skill tavus-cvi-quickstart
SKILL.md
Tavus CVI Quick Start

Get a real-time AI video conversation running in minutes.

Fastest Path: Use Stock Resources
curl -X POST https://tavusapi.com/v2/conversations \
  -H "Content-Type: application/json" \
  -H "x-api-key: YOUR_API_KEY" \
  -d '{
    "replica_id": "rfe12d8b9597",
    "persona_id": "pdced222244b"
  }'


Response:

{
  "conversation_id": "c123456",
  "conversation_url": "https://tavus.daily.co/c123456",
  "status": "active"
}


Open conversation_url in browser to join the call.

Stock Resources

Replicas (the visual avatar):

rfe12d8b9597 - Default
re8e740a42 - Nathan

Personas (behavior/personality):

pdced222244b - Default
p24293d6 - Celebrity DJ
Create Custom Persona + Conversation
Step 1: Create Persona
curl -X POST https://tavusapi.com/v2/personas \
  -H "Content-Type: application/json" \
  -H "x-api-key: YOUR_API_KEY" \
  -d '{
    "persona_name": "Sales Coach",
    "pipeline_mode": "full",
    "system_prompt": "You are a friendly sales coach helping reps practice cold calls. Ask probing questions and give constructive feedback.",
    "context": "Focus on B2B SaaS sales scenarios.",
    "default_replica_id": "rfe12d8b9597"
  }'


Response:

{
  "persona_id": "p123456",
  "persona_name": "Sales Coach"
}

Step 2: Start Conversation
curl -X POST https://tavusapi.com/v2/conversations \
  -H "Content-Type: application/json" \
  -H "x-api-key: YOUR_API_KEY" \
  -d '{
    "persona_id": "p123456",
    "conversation_name": "Practice Session"
  }'

Conversation Options
{
  "persona_id": "p123456",
  "replica_id": "rfe12d8b9597",
  "conversation_name": "Demo Call",
  "conversational_context": "User is interested in enterprise pricing.",
  "custom_greeting": "Hi! I'm excited to help you today.",
  "callback_url": "https://your-webhook.com/tavus",
  "properties": {
    "enable_recording": true,
    "max_duration": 600
  }
}

End Conversation
curl -X POST https://tavusapi.com/v2/conversations/{conversation_id}/end \
  -H "x-api-key: YOUR_API_KEY"

Key Concepts
Concept	What it is
Replica	The visual avatar (face, appearance)
Persona	Behavior, voice, LLM config, system prompt
Conversation	A live WebRTC session combining replica + persona
Pipeline Modes
full - Complete CVI with perception, STT, LLM, TTS (recommended)
echo - Bypass LLM, replica speaks what you send directly
audio - Audio-only, no video
Latency

~600ms utterance-to-utterance response time with full pipeline.

Next Steps
tavus-cvi-persona - Deep dive on persona configuration
tavus-cvi-ui - React component integration
tavus-cvi-interactions - Control conversations programmatically
tavus-cvi-knowledge - Add knowledge base and memories
Weekly Installs
32
Repository
tavus-engineeri…s-skills
GitHub Stars
5
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail