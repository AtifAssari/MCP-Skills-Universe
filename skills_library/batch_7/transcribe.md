---
title: transcribe
url: https://skills.sh/openai/skills/transcribe
---

# transcribe

skills/openai/skills/transcribe
transcribe
Installation
$ npx skills add https://github.com/openai/skills --skill transcribe
Summary

Transcribe audio files to text with optional speaker diarization and known-speaker hints.

Supports fast text transcription via gpt-4o-mini-transcribe and speaker-labeled diarization via gpt-4o-transcribe-diarize
Accepts multiple audio formats and optional known-speaker references (up to 4 speakers) to improve diarization accuracy
Outputs as plain text, JSON, or diarized JSON with configurable output directories to prevent overwrites
Requires OPENAI_API_KEY environment variable; uses bundled Python CLI for deterministic, repeatable transcription runs
SKILL.md
Audio Transcribe

Transcribe audio using OpenAI, with optional speaker diarization when requested. Prefer the bundled CLI for deterministic, repeatable runs.

Workflow
Collect inputs: audio file path(s), desired response format (text/json/diarized_json), optional language hint, and any known speaker references.
Verify OPENAI_API_KEY is set. If missing, ask the user to set it locally (do not ask them to paste the key).
Run the bundled transcribe_diarize.py CLI with sensible defaults (fast text transcription).
Validate the output: transcription quality, speaker labels, and segment boundaries; iterate with a single targeted change if needed.
Save outputs under output/transcribe/ when working in this repo.
Decision rules
Default to gpt-4o-mini-transcribe with --response-format text for fast transcription.
If the user wants speaker labels or diarization, use --model gpt-4o-transcribe-diarize --response-format diarized_json.
If audio is longer than ~30 seconds, keep --chunking-strategy auto.
Prompting is not supported for gpt-4o-transcribe-diarize.
Output conventions
Use output/transcribe/<job-id>/ for evaluation runs.
Use --out-dir for multiple files to avoid overwriting.
Dependencies (install if missing)

Prefer uv for dependency management.

uv pip install openai


If uv is unavailable:

python3 -m pip install openai

Environment
OPENAI_API_KEY must be set for live API calls.
If the key is missing, instruct the user to create one in the OpenAI platform UI and export it in their shell.
Never ask the user to paste the full key in chat.
Skill path (set once)
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export TRANSCRIBE_CLI="$CODEX_HOME/skills/transcribe/scripts/transcribe_diarize.py"


User-scoped skills install under $CODEX_HOME/skills (default: ~/.codex/skills).

CLI quick start

Single file (fast text default):

python3 "$TRANSCRIBE_CLI" \
  path/to/audio.wav \
  --out transcript.txt


Diarization with known speakers (up to 4):

python3 "$TRANSCRIBE_CLI" \
  meeting.m4a \
  --model gpt-4o-transcribe-diarize \
  --known-speaker "Alice=refs/alice.wav" \
  --known-speaker "Bob=refs/bob.wav" \
  --response-format diarized_json \
  --out-dir output/transcribe/meeting


Plain text output (explicit):

python3 "$TRANSCRIBE_CLI" \
  interview.mp3 \
  --response-format text \
  --out interview.txt

Reference map
references/api.md: supported formats, limits, response formats, and known-speaker notes.
Weekly Installs
1.1K
Repository
openai/skills
GitHub Stars
18.0K
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass