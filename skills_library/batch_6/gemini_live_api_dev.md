---
title: gemini-live-api-dev
url: https://skills.sh/google-gemini/gemini-skills/gemini-live-api-dev
---

# gemini-live-api-dev

skills/google-gemini/gemini-skills/gemini-live-api-dev
gemini-live-api-dev
Installation
$ npx skills add https://github.com/google-gemini/gemini-skills --skill gemini-live-api-dev
Summary

Real-time bidirectional streaming with Gemini over WebSockets for audio, video, and text conversations.

Supports audio input/output (16 kHz PCM), video frames, text, and automatic transcriptions with voice activity detection for interruption handling
Includes native audio features: affective dialog, proactive audio, and thinking mode; function calling for synchronous and asynchronous tool use; and Google Search grounding
Offers session management with context compression, resumption, and ephemeral tokens for secure client-side authentication
Available in Python (google-genai) and JavaScript/TypeScript (@google/genai) SDKs; integrates with LiveKit, Pipecat, Fishjam, and other platforms via WebRTC adapters
SKILL.md
Gemini Live API Development Skill
Overview

The Live API enables low-latency, real-time voice and video interactions with Gemini over WebSockets. It processes continuous streams of audio, video, or text to deliver immediate, human-like spoken responses.

Key capabilities:

Bidirectional audio streaming — real-time mic-to-speaker conversations
Video streaming — send camera/screen frames alongside audio
Text input/output — send and receive text within a live session
Audio transcriptions — get text transcripts of both input and output audio
Voice Activity Detection (VAD) — automatic interruption handling
Native audio — thinking (with configurable thinkingLevel)
Function calling — synchronous tool use
Google Search grounding — ground responses in real-time search results
Session management — context compression, session resumption, GoAway signals
Ephemeral tokens — secure client-side authentication

[!NOTE] The Live API currently only supports WebSockets. For WebRTC support or simplified integration, use a partner integration.

Models
gemini-3.1-flash-live-preview — Optimized for low-latency, real-time dialogue. Native audio output, thinking (via thinkingLevel). 128k context window. This is the recommended model for all Live API use cases.

[!WARNING] The following Live API models are deprecated and will be shut down. Migrate to gemini-3.1-flash-live-preview.

gemini-2.5-flash-native-audio-preview-12-2025 — Migrate to gemini-3.1-flash-live-preview.
gemini-live-2.5-flash-preview — Released June 17, 2025. Shutdown: December 9, 2025.
gemini-2.0-flash-live-001 — Released April 9, 2025. Shutdown: December 9, 2025.
SDKs
Python: google-genai — pip install google-genai
JavaScript/TypeScript: @google/genai — npm install @google/genai

[!WARNING] Legacy SDKs google-generativeai (Python) and @google/generative-ai (JS) are deprecated. Use the new SDKs above.

Partner Integrations

To streamline real-time audio/video app development, use a third-party integration supporting the Gemini Live API over WebRTC or WebSockets:

LiveKit — Use the Gemini Live API with LiveKit Agents.
Pipecat by Daily — Create a real-time AI chatbot using Gemini Live and Pipecat.
Fishjam by Software Mansion — Create live video and audio streaming applications with Fishjam.
Vision Agents by Stream — Build real-time voice and video AI applications with Vision Agents.
Voximplant — Connect inbound and outbound calls to Live API with Voximplant.
Firebase AI SDK — Get started with the Gemini Live API using Firebase AI Logic.
Audio Formats
Input: Raw PCM, little-endian, 16-bit, mono. 16kHz native (will resample others). MIME type: audio/pcm;rate=16000
Output: Raw PCM, little-endian, 16-bit, mono. 24kHz sample rate.

[!IMPORTANT] Use send_realtime_input / sendRealtimeInput for all real-time user input (audio, video, and text). send_client_content / sendClientContent is only supported for seeding initial context history (requires setting initial_history_in_client_content in history_config). Do not use it to send new user messages during the conversation.

[!WARNING] Do not use media in sendRealtimeInput. Use the specific keys: audio for audio data, video for images/video frames, and text for text input.

Quick Start
Authentication
Python
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

JavaScript
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({ apiKey: 'YOUR_API_KEY' });

Connecting to the Live API
Python
from google.genai import types

config = types.LiveConnectConfig(
    response_modalities=[types.Modality.AUDIO],
    system_instruction=types.Content(
        parts=[types.Part(text="You are a helpful assistant.")]
    )
)

async with client.aio.live.connect(model="gemini-3.1-flash-live-preview", config=config) as session:
    pass  # Session is active

JavaScript
const session = await ai.live.connect({
  model: 'gemini-3.1-flash-live-preview',
  config: {
    responseModalities: ['audio'],
    systemInstruction: { parts: [{ text: 'You are a helpful assistant.' }] }
  },
  callbacks: {
    onopen: () => console.log('Connected'),
    onmessage: (response) => console.log('Message:', response),
    onerror: (error) => console.error('Error:', error),
    onclose: () => console.log('Closed')
  }
});

Sending Text
Python
await session.send_realtime_input(text="Hello, how are you?")

JavaScript
session.sendRealtimeInput({ text: 'Hello, how are you?' });

Sending Audio
Python
await session.send_realtime_input(
    audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000")
)

JavaScript
session.sendRealtimeInput({
  audio: { data: chunk.toString('base64'), mimeType: 'audio/pcm;rate=16000' }
});

Sending Video
Python
# frame: raw JPEG-encoded bytes
await session.send_realtime_input(
    video=types.Blob(data=frame, mime_type="image/jpeg")
)

JavaScript
session.sendRealtimeInput({
  video: { data: frame.toString('base64'), mimeType: 'image/jpeg' }
});

Receiving Audio and Text

[!IMPORTANT] A single server event can contain multiple content parts simultaneously (e.g., audio chunks and transcript). Always process all parts in each event to avoid missing content.

Python
async for response in session.receive():
    content = response.server_content
    if content:
        # Audio — process ALL parts in each event
        if content.model_turn:
            for part in content.model_turn.parts:
                if part.inline_data:
                    audio_data = part.inline_data.data
        # Transcription
        if content.input_transcription:
            print(f"User: {content.input_transcription.text}")
        if content.output_transcription:
            print(f"Gemini: {content.output_transcription.text}")
        # Interruption
        if content.interrupted is True:
            pass  # Stop playback, clear audio queue

JavaScript
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data; // Base64 encoded
    }
  }
}
if (content?.inputTranscription) console.log('User:', content.inputTranscription.text);
if (content?.outputTranscription) console.log('Gemini:', content.outputTranscription.text);
if (content?.interrupted) { /* Stop playback, clear audio queue */ }

Limitations
Response modality — Only TEXT or AUDIO per session, not both
Audio-only session — 15 min without compression
Audio+video session — 2 min without compression
Connection lifetime — ~10 min (use session resumption)
Context window — 128k tokens (native audio) / 32k tokens (standard)
Async function calling — Not yet supported; function calling is synchronous only. The model will not start responding until you've sent the tool response.
Proactive audio — Not yet supported in Gemini 3.1 Flash Live. Remove any configuration for this feature.
Affective dialogue — Not yet supported in Gemini 3.1 Flash Live. Remove any configuration for this feature.
Code execution — Not supported
URL context — Not supported
Migrating from Gemini 2.5 Flash Live

When migrating from gemini-2.5-flash-native-audio-preview-12-2025 to gemini-3.1-flash-live-preview:

Model string — Update from gemini-2.5-flash-native-audio-preview-12-2025 to gemini-3.1-flash-live-preview.
Thinking configuration — Use thinkingLevel (minimal, low, medium, high) instead of thinkingBudget. Default is minimal for lowest latency.
Server events — A single event can contain multiple content parts simultaneously (audio + transcript). Process all parts in each event.
Client content — send_client_content is only for seeding initial context history (set initial_history_in_client_content in history_config). Use send_realtime_input for text during conversation.
Turn coverage — Defaults to TURN_INCLUDES_AUDIO_ACTIVITY_AND_ALL_VIDEO instead of TURN_INCLUDES_ONLY_ACTIVITY. If sending constant video frames, consider sending only during audio activity to reduce costs.
Async function calling — Not yet supported. Function calling is synchronous only.
Proactive audio & affective dialogue — Not yet supported. Remove any configuration for these features.
Best Practices
Use headphones when testing mic audio to prevent echo/self-interruption
Enable context window compression for sessions longer than 15 minutes
Implement session resumption to handle connection resets gracefully
Use ephemeral tokens for client-side deployments — never expose API keys in browsers
Use send_realtime_input for all real-time user input (audio, video, text). Reserve send_client_content only for seeding initial context history
Send audioStreamEnd when the mic is paused to flush cached audio
Clear audio playback queues on interruption signals
Process all parts in each server event — events can contain multiple content parts
Documentation Lookup
When MCP is Installed (Preferred)

If the search_docs tool (from the Google MCP server) is available, use it as your only documentation source:

Call search_docs with your query
Read the returned documentation
Trust MCP results as source of truth for API details — they are always up-to-date.

[!IMPORTANT] When MCP tools are present, never fetch URLs manually. MCP provides up-to-date, indexed documentation that is more accurate and token-efficient than URL fetching.

When MCP is NOT Installed (Fallback Only)

If no MCP documentation tools are available, fetch from the official docs index:

llms.txt URL: https://ai.google.dev/gemini-api/docs/llms.txt

This index contains links to all documentation pages in .md.txt format. Use web fetch tools to:

Fetch llms.txt to discover available documentation pages
Fetch specific pages (e.g., https://ai.google.dev/gemini-api/docs/live-session.md.txt)
Key Documentation Pages

[!IMPORTANT] Those are not all the documentation pages. Use the llms.txt index to discover available documentation pages

Live API Overview — getting started, raw WebSocket usage
Live API Capabilities Guide — voice config, transcription config, native audio (thinking), VAD configuration, media resolution
Live API Tool Use — function calling (sync and async), Google Search grounding
Session Management — context window compression, session resumption, GoAway signals
Ephemeral Tokens — secure client-side authentication for browser/mobile
WebSockets API Reference — raw WebSocket protocol details
Supported Languages

The Live API supports 70 languages including: English, Spanish, French, German, Italian, Portuguese, Chinese, Japanese, Korean, Hindi, Arabic, Russian, and many more. Native audio models automatically detect and switch languages.

Weekly Installs
2.6K
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