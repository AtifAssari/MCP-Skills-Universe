---
title: tavus-cvi-persona
url: https://skills.sh/tavus-engineering/tavus-skills/tavus-cvi-persona
---

# tavus-cvi-persona

skills/tavus-engineering/tavus-skills/tavus-cvi-persona
tavus-cvi-persona
Installation
$ npx skills add https://github.com/tavus-engineering/tavus-skills --skill tavus-cvi-persona
SKILL.md
Tavus CVI Persona Configuration

Deep configuration of persona behavior, LLM, TTS, perception, and turn-taking.

Full Persona Schema
curl -X POST https://tavusapi.com/v2/personas \
  -H "Content-Type: application/json" \
  -H "x-api-key: YOUR_API_KEY" \
  -d '{
    "persona_name": "Technical Interviewer",
    "pipeline_mode": "full",
    "system_prompt": "You are a senior technical interviewer...",
    "context": "Focus on system design and coding problems.",
    "default_replica_id": "rfe12d8b9597",
    "layers": {
      "llm": {...},
      "tts": {...},
      "perception": {...},
      "stt": {...}
    }
  }'

LLM Layer
Built-in Models (Optimized)
{
  "layers": {
    "llm": {
      "model": "tavus-gpt-4o"
    }
  }
}


Options: tavus-gpt-4o, tavus-gpt-4o-mini, tavus-llama

Bring Your Own LLM

Any OpenAI-compatible API:

{
  "layers": {
    "llm": {
      "model": "gpt-4-turbo",
      "base_url": "https://api.openai.com/v1",
      "api_key": "sk-...",
      "speculative_inference": true
    }
  }
}


Works with: OpenAI, Anthropic (via proxy), Groq, Together, local models with OpenAI-compatible endpoints.

Function Calling / Tools
{
  "layers": {
    "llm": {
      "model": "tavus-gpt-4o",
      "tools": [
        {
          "type": "function",
          "function": {
            "name": "get_weather",
            "description": "Get current weather for a location",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "City and state"
                }
              },
              "required": ["location"]
            }
          }
        }
      ]
    }
  }
}


Tool calls are sent via the Interactions Protocol.

TTS Layer
Cartesia (Default)
{
  "layers": {
    "tts": {
      "tts_engine": "cartesia",
      "voice_id": "your-cartesia-voice-id"
    }
  }
}

ElevenLabs
{
  "layers": {
    "tts": {
      "tts_engine": "elevenlabs",
      "voice_id": "your-elevenlabs-voice-id",
      "api_key": "your-elevenlabs-key"
    }
  }
}

PlayHT
{
  "layers": {
    "tts": {
      "tts_engine": "playht",
      "voice_id": "your-playht-voice-id",
      "api_key": "your-playht-key"
    }
  }
}

Perception Layer (Raven)

Enables the replica to "see" - analyzes expressions, gaze, background, screen content.

{
  "layers": {
    "perception": {
      "perception_model": "raven-0",
      "ambient_awareness": true
    }
  }
}


Use cases:

React to user expressions/emotions
See shared screens
Analyze user's environment
STT Layer (Speech Recognition)
Smart Turn Detection (Sparrow)
{
  "layers": {
    "stt": {
      "smart_turn_detection": true,
      "participant_pause_sensitivity": "medium",
      "participant_interrupt_sensitivity": "medium"
    }
  }
}


Sensitivity options: low, medium, high

pause_sensitivity: How long user pauses before replica responds
interrupt_sensitivity: How easily user can interrupt replica
Pipeline Modes
Full (Default)

Complete pipeline with all layers:

{ "pipeline_mode": "full" }

Echo

Bypass LLM - replica speaks exactly what you send:

{ "pipeline_mode": "echo" }


Use with Interactions Protocol to control speech directly.

Audio Only

Voice-only, no video:

{
  "pipeline_mode": "full",
  "audio_only": true
}

Update Existing Persona
curl -X PATCH https://tavusapi.com/v2/personas/{persona_id} \
  -H "Content-Type: application/json" \
  -H "x-api-key: YOUR_API_KEY" \
  -d '{
    "system_prompt": "Updated prompt...",
    "context": "New context..."
  }'

List & Delete Personas
# List
curl https://tavusapi.com/v2/personas -H "x-api-key: YOUR_API_KEY"

# Delete
curl -X DELETE https://tavusapi.com/v2/personas/{persona_id} \
  -H "x-api-key: YOUR_API_KEY"

Supported Languages

30+ languages via Cartesia + ElevenLabs fallback: English, French, German, Spanish, Portuguese, Chinese, Japanese, Hindi, Italian, Korean, Dutch, Polish, Russian, Swedish, Turkish, Indonesian, Filipino, Arabic, Czech, Greek, Finnish, Croatian, Danish, Tamil, Ukrainian, Hungarian, Norwegian, Vietnamese, and more.

Weekly Installs
27
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