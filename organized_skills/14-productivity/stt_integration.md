---
rating: ⭐⭐⭐
title: stt-integration
url: https://skills.sh/vanman2024/ai-dev-marketplace/stt-integration
---

# stt-integration

skills/vanman2024/ai-dev-marketplace/stt-integration
stt-integration
Installation
$ npx skills add https://github.com/vanman2024/ai-dev-marketplace --skill stt-integration
SKILL.md
stt-integration

This skill provides comprehensive guidance for implementing ElevenLabs Speech-to-Text (STT) capabilities using the Scribe v1 model, which supports 99 languages with state-of-the-art accuracy, speaker diarization for up to 32 speakers, and seamless Vercel AI SDK integration.

Core Capabilities
Scribe v1 Model Features
Multi-language support: 99 languages with varying accuracy levels
Speaker diarization: Up to 32 speakers with identification
Word-level timestamps: Precise synchronization for video/audio alignment
Audio event detection: Identifies sounds like laughter and applause
High accuracy: Optimized for accuracy over real-time processing
Supported Formats
Audio: AAC, AIFF, OGG, MP3, Opus, WAV, WebM, FLAC, M4A
Video: MP4, AVI, Matroska, QuickTime, WMV, FLV, WebM, MPEG, 3GPP
Limits: Max 3 GB file size, 10 hours duration
Skill Structure
Scripts (scripts/)
transcribe-audio.sh - Direct API transcription with curl
setup-vercel-ai.sh - Install and configure @ai-sdk/elevenlabs
test-stt.sh - Test STT with sample audio files
validate-audio.sh - Validate audio file format and size
batch-transcribe.sh - Process multiple audio files
Templates (templates/)
stt-config.json.template - STT configuration template
vercel-ai-transcribe.ts.template - Vercel AI SDK TypeScript template
vercel-ai-transcribe.py.template - Vercel AI SDK Python template
api-transcribe.ts.template - Direct API TypeScript template
api-transcribe.py.template - Direct API Python template
diarization-config.json.template - Speaker diarization configuration
Examples (examples/)
basic-stt/ - Basic STT with direct API
vercel-ai-stt/ - Vercel AI SDK integration
diarization/ - Speaker diarization examples
multi-language/ - Multi-language transcription
webhook-integration/ - Async transcription with webhooks
Usage Instructions
1. Setup Vercel AI SDK Integration
# Install dependencies
bash scripts/setup-vercel-ai.sh

# Verify installation
npm list @ai-sdk/elevenlabs

2. Basic Transcription
# Transcribe a single audio file
bash scripts/transcribe-audio.sh path/to/audio.mp3 en

# Validate audio before transcription
bash scripts/validate-audio.sh path/to/audio.mp3

# Batch transcribe multiple files
bash scripts/batch-transcribe.sh path/to/audio/directory en

3. Test STT Implementation
# Run comprehensive tests
bash scripts/test-stt.sh

4. Use Templates
// Read Vercel AI SDK template
Read: templates/vercel-ai-transcribe.ts.template

// Customize for your use case
// - Set language code
// - Configure diarization
// - Enable audio event tagging
// - Set timestamp granularity

5. Explore Examples
# Basic STT example
Read: examples/basic-stt/README.md

# Vercel AI SDK example
Read: examples/vercel-ai-stt/README.md

# Speaker diarization example
Read: examples/diarization/README.md

Language Support
Excellent Accuracy (≤5% WER)

30 languages including: English, French, German, Spanish, Italian, Japanese, Portuguese, Dutch, Polish, Russian

High Accuracy (>5-10% WER)

19 languages including: Bengali, Mandarin Chinese, Tamil, Telugu, Vietnamese, Turkish

Good Accuracy (>10-25% WER)

30 languages including: Arabic, Korean, Thai, Indonesian, Hebrew, Czech

Moderate Accuracy (>25-50% WER)

19 languages including: Amharic, Khmer, Lao, Burmese, Nepali

Configuration Options
Provider Options (Vercel AI SDK)
languageCode: ISO-639-1/3 code (e.g., 'en', 'es', 'ja')
tagAudioEvents: Enable sound detection (default: true)
numSpeakers: Max speakers 1-32 (default: auto-detect)
diarize: Enable speaker identification (default: true)
timestampsGranularity: 'none' | 'word' | 'character' (default: 'word')
fileFormat: 'pcm_s16le_16' | 'other' (default: 'other')
Best Practices
Specify language code when known for better performance
Use pcm_s16le_16 format for lowest latency with uncompressed audio
Enable diarization for multi-speaker content
Set numSpeakers for better accuracy when speaker count is known
Use webhooks for files >8 minutes for async processing
Common Patterns
Pattern 1: Simple Transcription

Use direct API or Vercel AI SDK for single-language, single-speaker transcription.

Pattern 2: Multi-Speaker Transcription

Enable diarization and set numSpeakers for interviews, meetings, podcasts.

Pattern 3: Multi-Language Support

Detect language automatically or specify when known for content in 99 languages.

Pattern 4: Video Transcription

Extract audio from video formats and transcribe with timestamps for subtitles.

Pattern 5: Webhook Integration

Process long files asynchronously using webhook callbacks for results.

Integration with Other ElevenLabs Skills
tts-integration: Combine STT → processing → TTS for voice translation workflows
voice-cloning: Transcribe existing voice samples before cloning
dubbing: Use STT as first step in dubbing pipeline
Troubleshooting
Audio Format Issues
# Validate audio format
bash scripts/validate-audio.sh your-audio.mp3

Language Detection Problems
Specify languageCode explicitly instead of auto-detection
Ensure audio quality is sufficient for chosen language
Diarization Not Working
Verify numSpeakers is set correctly (1-32)
Check that diarize: true is configured
Ensure audio has clear speaker separation
File Size/Duration Limits
Max 3 GB file size
Max 10 hours duration
Files >8 minutes are chunked automatically
Script Reference

All scripts are located in skills/stt-integration/scripts/:

transcribe-audio.sh - Main transcription script with curl
setup-vercel-ai.sh - Install @ai-sdk/elevenlabs package
test-stt.sh - Comprehensive test suite
validate-audio.sh - Audio format and size validation
batch-transcribe.sh - Batch processing for multiple files
Template Reference

All templates are located in skills/stt-integration/templates/:

stt-config.json.template - JSON configuration
vercel-ai-transcribe.ts.template - TypeScript with Vercel AI SDK
vercel-ai-transcribe.py.template - Python with Vercel AI SDK
api-transcribe.ts.template - TypeScript with direct API
api-transcribe.py.template - Python with direct API
diarization-config.json.template - Diarization settings
Example Reference

All examples are located in skills/stt-integration/examples/:

basic-stt/ - Basic transcription workflow
vercel-ai-stt/ - Vercel AI SDK integration
diarization/ - Speaker identification
multi-language/ - Multi-language support
webhook-integration/ - Async processing

Skill Location: plugins/elevenlabs/skills/stt-integration/ Version: 1.0.0 Last Updated: 2025-10-29

Weekly Installs
14
Repository
vanman2024/ai-d…ketplace
GitHub Stars
10
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn