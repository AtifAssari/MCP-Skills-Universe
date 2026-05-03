---
title: whisper
url: https://skills.sh/davila7/claude-code-templates/whisper
---

# whisper

skills/davila7/claude-code-templates/whisper
whisper
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill whisper
Summary

Multilingual speech recognition with 99 languages, transcription, translation, and six model sizes from 39M to 1550M parameters.

Supports transcription, translation to English, language identification, and word-level timestamps across 99 languages trained on 680,000 hours of audio
Six model sizes (tiny through large) with configurable speed/quality tradeoffs; turbo model offers 8× speedup over large with comparable quality
GPU acceleration delivers 10–20× faster processing; CPU transcription available for resource-constrained environments
Command-line and Python API interfaces; outputs to plain text, SRT subtitles, WebVTT, or JSON with segment timing
Initial prompt support improves accuracy on technical terms and domain-specific vocabulary; temperature fallback for low-confidence segments
SKILL.md
Whisper - Robust Speech Recognition

OpenAI's multilingual speech recognition model.

When to use Whisper

Use when:

Speech-to-text transcription (99 languages)
Podcast/video transcription
Meeting notes automation
Translation to English
Noisy audio transcription
Multilingual audio processing

Metrics:

72,900+ GitHub stars
99 languages supported
Trained on 680,000 hours of audio
MIT License

Use alternatives instead:

AssemblyAI: Managed API, speaker diarization
Deepgram: Real-time streaming ASR
Google Speech-to-Text: Cloud-based
Quick start
Installation
# Requires Python 3.8-3.11
pip install -U openai-whisper

# Requires ffmpeg
# macOS: brew install ffmpeg
# Ubuntu: sudo apt install ffmpeg
# Windows: choco install ffmpeg

Basic transcription
import whisper

# Load model
model = whisper.load_model("base")

# Transcribe
result = model.transcribe("audio.mp3")

# Print text
print(result["text"])

# Access segments
for segment in result["segments"]:
    print(f"[{segment['start']:.2f}s - {segment['end']:.2f}s] {segment['text']}")

Model sizes
# Available models
models = ["tiny", "base", "small", "medium", "large", "turbo"]

# Load specific model
model = whisper.load_model("turbo")  # Fastest, good quality

Model	Parameters	English-only	Multilingual	Speed	VRAM
tiny	39M	✓	✓	~32x	~1 GB
base	74M	✓	✓	~16x	~1 GB
small	244M	✓	✓	~6x	~2 GB
medium	769M	✓	✓	~2x	~5 GB
large	1550M	✗	✓	1x	~10 GB
turbo	809M	✗	✓	~8x	~6 GB

Recommendation: Use turbo for best speed/quality, base for prototyping

Transcription options
Language specification
# Auto-detect language
result = model.transcribe("audio.mp3")

# Specify language (faster)
result = model.transcribe("audio.mp3", language="en")

# Supported: en, es, fr, de, it, pt, ru, ja, ko, zh, and 89 more

Task selection
# Transcription (default)
result = model.transcribe("audio.mp3", task="transcribe")

# Translation to English
result = model.transcribe("spanish.mp3", task="translate")
# Input: Spanish audio → Output: English text

Initial prompt
# Improve accuracy with context
result = model.transcribe(
    "audio.mp3",
    initial_prompt="This is a technical podcast about machine learning and AI."
)

# Helps with:
# - Technical terms
# - Proper nouns
# - Domain-specific vocabulary

Timestamps
# Word-level timestamps
result = model.transcribe("audio.mp3", word_timestamps=True)

for segment in result["segments"]:
    for word in segment["words"]:
        print(f"{word['word']} ({word['start']:.2f}s - {word['end']:.2f}s)")

Temperature fallback
# Retry with different temperatures if confidence low
result = model.transcribe(
    "audio.mp3",
    temperature=(0.0, 0.2, 0.4, 0.6, 0.8, 1.0)
)

Command line usage
# Basic transcription
whisper audio.mp3

# Specify model
whisper audio.mp3 --model turbo

# Output formats
whisper audio.mp3 --output_format txt     # Plain text
whisper audio.mp3 --output_format srt     # Subtitles
whisper audio.mp3 --output_format vtt     # WebVTT
whisper audio.mp3 --output_format json    # JSON with timestamps

# Language
whisper audio.mp3 --language Spanish

# Translation
whisper spanish.mp3 --task translate

Batch processing
import os

audio_files = ["file1.mp3", "file2.mp3", "file3.mp3"]

for audio_file in audio_files:
    print(f"Transcribing {audio_file}...")
    result = model.transcribe(audio_file)

    # Save to file
    output_file = audio_file.replace(".mp3", ".txt")
    with open(output_file, "w") as f:
        f.write(result["text"])

Real-time transcription
# For streaming audio, use faster-whisper
# pip install faster-whisper

from faster_whisper import WhisperModel

model = WhisperModel("base", device="cuda", compute_type="float16")

# Transcribe with streaming
segments, info = model.transcribe("audio.mp3", beam_size=5)

for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

GPU acceleration
import whisper

# Automatically uses GPU if available
model = whisper.load_model("turbo")

# Force CPU
model = whisper.load_model("turbo", device="cpu")

# Force GPU
model = whisper.load_model("turbo", device="cuda")

# 10-20× faster on GPU

Integration with other tools
Subtitle generation
# Generate SRT subtitles
whisper video.mp4 --output_format srt --language English

# Output: video.srt

With LangChain
from langchain.document_loaders import WhisperTranscriptionLoader

loader = WhisperTranscriptionLoader(file_path="audio.mp3")
docs = loader.load()

# Use transcription in RAG
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

vectorstore = Chroma.from_documents(docs, OpenAIEmbeddings())

Extract audio from video
# Use ffmpeg to extract audio
ffmpeg -i video.mp4 -vn -acodec pcm_s16le audio.wav

# Then transcribe
whisper audio.wav

Best practices
Use turbo model - Best speed/quality for English
Specify language - Faster than auto-detect
Add initial prompt - Improves technical terms
Use GPU - 10-20× faster
Batch process - More efficient
Convert to WAV - Better compatibility
Split long audio - <30 min chunks
Check language support - Quality varies by language
Use faster-whisper - 4× faster than openai-whisper
Monitor VRAM - Scale model size to hardware
Performance
Model	Real-time factor (CPU)	Real-time factor (GPU)
tiny	~0.32	~0.01
base	~0.16	~0.01
turbo	~0.08	~0.01
large	~1.0	~0.05

Real-time factor: 0.1 = 10× faster than real-time

Language support

Top-supported languages:

English (en)
Spanish (es)
French (fr)
German (de)
Italian (it)
Portuguese (pt)
Russian (ru)
Japanese (ja)
Korean (ko)
Chinese (zh)

Full list: 99 languages total

Limitations
Hallucinations - May repeat or invent text
Long-form accuracy - Degrades on >30 min audio
Speaker identification - No diarization
Accents - Quality varies
Background noise - Can affect accuracy
Real-time latency - Not suitable for live captioning
Resources
GitHub: https://github.com/openai/whisper ⭐ 72,900+
Paper: https://arxiv.org/abs/2212.04356
Model Card: https://github.com/openai/whisper/blob/main/model-card.md
Colab: Available in repo
License: MIT
Weekly Installs
913
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass