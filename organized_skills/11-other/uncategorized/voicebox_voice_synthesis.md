---
rating: ⭐⭐⭐
title: voicebox-voice-synthesis
url: https://skills.sh/aradotso/trending-skills/voicebox-voice-synthesis
---

# voicebox-voice-synthesis

skills/aradotso/trending-skills/voicebox-voice-synthesis
voicebox-voice-synthesis
Installation
$ npx skills add https://github.com/aradotso/trending-skills --skill voicebox-voice-synthesis
SKILL.md
Voicebox Voice Synthesis Studio

Skill by ara.so — Daily 2026 Skills collection.

Voicebox is a local-first, open-source voice cloning and TTS studio — a self-hosted alternative to ElevenLabs. It runs entirely on your machine (macOS MLX/Metal, Windows/Linux CUDA, CPU fallback), exposes a REST API on localhost:17493, and ships with 5 TTS engines, 23 languages, post-processing effects, and a multi-track Stories editor.

Installation
Pre-built Binaries (Recommended)
Platform	Link
macOS Apple Silicon	https://voicebox.sh/download/mac-arm
macOS Intel	https://voicebox.sh/download/mac-intel
Windows	https://voicebox.sh/download/windows
Docker	docker compose up

Linux requires building from source: https://voicebox.sh/linux-install

Build from Source

Prerequisites: Bun, Rust, Python 3.11+, Tauri prerequisites

git clone https://github.com/jamiepine/voicebox.git
cd voicebox

# Install just task runner
brew install just        # macOS
cargo install just       # any platform

# Set up Python venv + all dependencies
just setup

# Start backend + desktop app in dev mode
just dev

# List all available commands
just --list

Architecture
Layer	Technology
Desktop App	Tauri (Rust)
Frontend	React + TypeScript + Tailwind CSS
State	Zustand + React Query
Backend	FastAPI (Python) on port 17493
TTS Engines	Qwen3-TTS, LuxTTS, Chatterbox, Chatterbox Turbo, TADA
Effects	Pedalboard (Spotify)
Transcription	Whisper / Whisper Turbo
Inference	MLX (Apple Silicon) / PyTorch (CUDA/ROCm/XPU/CPU)
Database	SQLite

The Python FastAPI backend handles all ML inference. The Tauri Rust shell wraps the frontend and manages the backend process lifecycle. The API is accessible directly at http://localhost:17493 even when using the desktop app.

REST API Reference

Base URL: http://localhost:17493
Interactive docs: http://localhost:17493/docs

Generate Speech
# Basic generation
curl -X POST http://localhost:17493/generate \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello world, this is a voice clone.",
    "profile_id": "abc123",
    "language": "en"
  }'

# With engine selection
curl -X POST http://localhost:17493/generate \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Speak slowly and with gravitas.",
    "profile_id": "abc123",
    "language": "en",
    "engine": "qwen3-tts"
  }'

# With paralinguistic tags (Chatterbox Turbo only)
curl -X POST http://localhost:17493/generate \
  -H "Content-Type: application/json" \
  -d '{
    "text": "That is absolutely hilarious! [laugh] I cannot believe it.",
    "profile_id": "abc123",
    "engine": "chatterbox-turbo",
    "language": "en"
  }'

Voice Profiles
# List all profiles
curl http://localhost:17493/profiles

# Create a new profile
curl -X POST http://localhost:17493/profiles \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Narrator",
    "language": "en",
    "description": "Deep narrative voice"
  }'

# Upload audio sample to a profile
curl -X POST http://localhost:17493/profiles/{profile_id}/samples \
  -F "file=@/path/to/voice-sample.wav"

# Export a profile
curl http://localhost:17493/profiles/{profile_id}/export \
  --output narrator-profile.zip

# Import a profile
curl -X POST http://localhost:17493/profiles/import \
  -F "file=@narrator-profile.zip"

Generation Queue & Status
# Get generation status (SSE stream)
curl -N http://localhost:17493/generate/{generation_id}/status

# List recent generations
curl http://localhost:17493/generations

# Retry a failed generation
curl -X POST http://localhost:17493/generations/{generation_id}/retry

# Download generated audio
curl http://localhost:17493/generations/{generation_id}/audio \
  --output output.wav

Models
# List available models and download status
curl http://localhost:17493/models

# Unload a model from GPU memory (without deleting)
curl -X POST http://localhost:17493/models/{model_id}/unload

TypeScript/JavaScript Integration
Basic TTS Client
const VOICEBOX_URL = process.env.VOICEBOX_API_URL ?? "http://localhost:17493";

interface GenerateRequest {
  text: string;
  profile_id: string;
  language?: string;
  engine?: "qwen3-tts" | "luxtts" | "chatterbox" | "chatterbox-turbo" | "tada";
}

interface GenerateResponse {
  generation_id: string;
  status: "queued" | "processing" | "complete" | "failed";
  audio_url?: string;
}

async function generateSpeech(req: GenerateRequest): Promise<GenerateResponse> {
  const response = await fetch(`${VOICEBOX_URL}/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(req),
  });

  if (!response.ok) {
    throw new Error(`Voicebox API error: ${response.status} ${await response.text()}`);
  }

  return response.json();
}

// Usage
const result = await generateSpeech({
  text: "Welcome to our application.",
  profile_id: "abc123",
  language: "en",
  engine: "qwen3-tts",
});

console.log("Generation ID:", result.generation_id);

Poll for Completion
async function waitForGeneration(
  generationId: string,
  timeoutMs = 60_000
): Promise<string> {
  const start = Date.now();

  while (Date.now() - start < timeoutMs) {
    const res = await fetch(`${VOICEBOX_URL}/generations/${generationId}`);
    const data = await res.json();

    if (data.status === "complete") {
      return `${VOICEBOX_URL}/generations/${generationId}/audio`;
    }
    if (data.status === "failed") {
      throw new Error(`Generation failed: ${data.error}`);
    }

    await new Promise((r) => setTimeout(r, 1000));
  }

  throw new Error("Generation timed out");
}

Stream Status with SSE
function streamGenerationStatus(
  generationId: string,
  onStatus: (status: string) => void
): () => void {
  const eventSource = new EventSource(
    `${VOICEBOX_URL}/generate/${generationId}/status`
  );

  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    onStatus(data.status);

    if (data.status === "complete" || data.status === "failed") {
      eventSource.close();
    }
  };

  eventSource.onerror = () => eventSource.close();

  // Return cleanup function
  return () => eventSource.close();
}

// Usage
const cleanup = streamGenerationStatus("gen_abc123", (status) => {
  console.log("Status update:", status);
});

Download Audio as Blob
async function downloadAudio(generationId: string): Promise<Blob> {
  const response = await fetch(
    `${VOICEBOX_URL}/generations/${generationId}/audio`
  );

  if (!response.ok) {
    throw new Error(`Failed to download audio: ${response.status}`);
  }

  return response.blob();
}

// Play in browser
async function playGeneratedAudio(generationId: string): Promise<void> {
  const blob = await downloadAudio(generationId);
  const url = URL.createObjectURL(blob);
  const audio = new Audio(url);
  audio.play();
  audio.onended = () => URL.revokeObjectURL(url);
}

Python Integration
import httpx
import asyncio

VOICEBOX_URL = "http://localhost:17493"

async def generate_speech(
    text: str,
    profile_id: str,
    language: str = "en",
    engine: str = "qwen3-tts"
) -> bytes:
    async with httpx.AsyncClient(timeout=120.0) as client:
        # Submit generation
        resp = await client.post(
            f"{VOICEBOX_URL}/generate",
            json={
                "text": text,
                "profile_id": profile_id,
                "language": language,
                "engine": engine,
            }
        )
        resp.raise_for_status()
        generation_id = resp.json()["generation_id"]

        # Poll until complete
        for _ in range(120):
            status_resp = await client.get(
                f"{VOICEBOX_URL}/generations/{generation_id}"
            )
            status_data = status_resp.json()

            if status_data["status"] == "complete":
                audio_resp = await client.get(
                    f"{VOICEBOX_URL}/generations/{generation_id}/audio"
                )
                return audio_resp.content

            if status_data["status"] == "failed":
                raise RuntimeError(f"Generation failed: {status_data.get('error')}")

            await asyncio.sleep(1.0)

        raise TimeoutError("Generation timed out after 120s")


# Usage
audio_bytes = asyncio.run(
    generate_speech(
        text="The quick brown fox jumps over the lazy dog.",
        profile_id="your-profile-id",
        language="en",
        engine="chatterbox",
    )
)

with open("output.wav", "wb") as f:
    f.write(audio_bytes)

TTS Engine Selection Guide
Engine	Best For	Languages	VRAM	Notes
qwen3-tts (0.6B/1.7B)	Quality + instructions	10	Medium	Supports delivery instructions in text
luxtts	Fast CPU generation	English only	~1GB	150x realtime on CPU, 48kHz
chatterbox	Multilingual coverage	23	Medium	Arabic, Hindi, Swahili, CJK + more
chatterbox-turbo	Expressive/emotion	English only	Low (350M)	Use [laugh], [sigh], [gasp] tags
tada (1B/3B)	Long-form coherence	10	High	700s+ audio, HumeAI model
Delivery Instructions (Qwen3-TTS)

Embed natural language instructions directly in the text:

await generateSpeech({
  text: "(whisper) I have a secret to tell you.",
  profile_id: "abc123",
  engine: "qwen3-tts",
});

await generateSpeech({
  text: "(speak slowly and clearly) Step one: open the application.",
  profile_id: "abc123",
  engine: "qwen3-tts",
});

Paralinguistic Tags (Chatterbox Turbo)
const tags = [
  "[laugh]", "[chuckle]", "[gasp]", "[cough]",
  "[sigh]", "[groan]", "[sniff]", "[shush]", "[clear throat]"
];

await generateSpeech({
  text: "Oh really? [gasp] I had no idea! [laugh] That's incredible.",
  profile_id: "abc123",
  engine: "chatterbox-turbo",
});

Environment & Configuration
# Custom models directory (set before launching)
export VOICEBOX_MODELS_DIR=/path/to/models

# For AMD ROCm GPU (auto-configured, but can override)
export HSA_OVERRIDE_GFX_VERSION=11.0.0


Docker configuration (docker-compose.yml override):

services:
  voicebox:
    environment:
      - VOICEBOX_MODELS_DIR=/models
    volumes:
      - /host/models:/models
    ports:
      - "17493:17493"
    # For NVIDIA GPU passthrough:
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]

Common Patterns
Voice Profile Creation Flow
// 1. Create profile
const profile = await fetch(`${VOICEBOX_URL}/profiles`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ name: "My Voice", language: "en" }),
}).then((r) => r.json());

// 2. Upload audio sample (WAV/MP3, ideally 5–30 seconds clean speech)
const formData = new FormData();
formData.append("file", audioBlob, "sample.wav");

await fetch(`${VOICEBOX_URL}/profiles/${profile.id}/samples`, {
  method: "POST",
  body: formData,
});

// 3. Generate with the new profile
const gen = await generateSpeech({
  text: "Testing my cloned voice.",
  profile_id: profile.id,
});

Batch Generation with Queue
async function batchGenerate(
  items: Array<{ text: string; profileId: string }>,
  engine = "qwen3-tts"
): Promise<string[]> {
  // Submit all — Voicebox queues them serially to avoid GPU contention
  const submissions = await Promise.all(
    items.map((item) =>
      generateSpeech({ text: item.text, profile_id: item.profileId, engine })
    )
  );

  // Wait for all completions
  const audioUrls = await Promise.all(
    submissions.map((s) => waitForGeneration(s.generation_id))
  );

  return audioUrls;
}

Long-Form Text (Auto-Chunking)

Voicebox auto-chunks at sentence boundaries — just send the full text:

const longScript = `
  Chapter one. The morning fog rolled across the valley floor...
  // Up to 50,000 characters supported
`;

await generateSpeech({
  text: longScript,
  profile_id: "narrator-profile-id",
  engine: "tada", // Best for long-form coherence
  language: "en",
});

Troubleshooting
API not responding
# Check if backend is running
curl http://localhost:17493/health

# Restart backend only (dev mode)
just backend

# Check logs
just logs

GPU not detected
# Check detected backend
curl http://localhost:17493/system/info

# Force CPU mode (set before launch)
export VOICEBOX_FORCE_CPU=1

Model download fails / slow
# Set custom models directory with more space
export VOICEBOX_MODELS_DIR=/path/with/space
just dev

# Cancel stuck download via API
curl -X DELETE http://localhost:17493/models/{model_id}/download

Out of VRAM — unload models
# List loaded models
curl http://localhost:17493/models | jq '.[] | select(.loaded == true)'

# Unload specific model
curl -X POST http://localhost:17493/models/{model_id}/unload

Audio quality issues
Use 5–30 seconds of clean, noise-free speech for voice samples
Multiple samples improve clone quality — upload 3–5 different sentences
For multilingual cloning, use chatterbox engine
Ensure sample audio is 16kHz+ mono WAV for best results
Use luxtts for highest output quality (48kHz) in English
Generation stuck in queue after crash

Voicebox auto-recovers stale generations on startup. If the issue persists:

curl -X POST http://localhost:17493/generations/{generation_id}/retry

Frontend Integration (React Example)
import { useState } from "react";

const VOICEBOX_URL = import.meta.env.VITE_VOICEBOX_URL ?? "http://localhost:17493";

export function VoiceGenerator({ profileId }: { profileId: string }) {
  const [text, setText] = useState("");
  const [audioUrl, setAudioUrl] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${VOICEBOX_URL}/generate`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text, profile_id: profileId, language: "en" }),
      });
      const { generation_id } = await res.json();

      // Poll for completion
      let done = false;
      while (!done) {
        await new Promise((r) => setTimeout(r, 1000));
        const statusRes = await fetch(`${VOICEBOX_URL}/generations/${generation_id}`);
        const { status } = await statusRes.json();
        if (status === "complete") {
          setAudioUrl(`${VOICEBOX_URL}/generations/${generation_id}/audio`);
          done = true;
        } else if (status === "failed") {
          throw new Error("Generation failed");
        }
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <textarea value={text} onChange={(e) => setText(e.target.value)} />
      <button onClick={handleGenerate} disabled={loading}>
        {loading ? "Generating..." : "Generate Speech"}
      </button>
      {audioUrl && <audio controls src={audioUrl} />}
    </div>
  );
}

Weekly Installs
1.1K
Repository
aradotso/trending-skills
GitHub Stars
42
First Seen
Mar 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass