---
rating: ⭐⭐
title: asr
url: https://skills.sh/marswaveai/skills/asr
---

# asr

skills/marswaveai/skills/asr
asr
Installation
$ npx skills add https://github.com/marswaveai/skills --skill asr
Summary

Local offline audio transcription with multi-language support and optional AI polishing.

Transcribes audio files to text using coli asr with no API keys required; supports Chinese, English, Japanese, Korean, and Cantonese via sensevoice model, or English-only via whisper-tiny
Models download automatically on first use (~60MB) to ~/.coli/models/; requires coli CLI and ffmpeg (WAV files work without it)
Optional AI polishing step corrects punctuation, removes filler words, and improves readability while preserving original meaning
Exports transcripts as markdown files with metadata (source, date, model, duration, detected language)
SKILL.md
When to Use
User wants to transcribe an audio file to text
User provides an audio file path and asks for transcription
User says "转录", "识别", "transcribe", "语音转文字"
When NOT to Use
User wants to synthesize speech from text (use /tts)
User wants to create a podcast or explainer (use /podcast or /explainer)
Purpose

Transcribe audio files to text using coli asr, which runs fully offline via local speech recognition models. No API key required. Supports Chinese, English, Japanese, Korean, and Cantonese (sensevoice model) or English-only (whisper model).

Run coli asr --help for current CLI options and supported flags.

Hard Constraints
No shell scripts. Use direct commands only.
Always read config following shared/config-pattern.md before any interaction
Follow shared/cli-patterns.md for interaction patterns
Never ask more than one question at a time
Interaction Flow
Step 0: Prerequisites Check

Before config setup, silently check the environment:

COLI_OK=$(which coli 2>/dev/null && echo yes || echo no)
FFMPEG_OK=$(which ffmpeg 2>/dev/null && echo yes || echo no)
MODELS_DIR="$HOME/.coli/models"
MODELS_OK=$([ -d "$MODELS_DIR" ] && ls "$MODELS_DIR" | grep -q sherpa && echo yes || echo no)

Issue	Action
coli not found	Block. Tell user to run npm install -g @marswave/coli first
ffmpeg not found	Warn (WAV files still work). Suggest brew install ffmpeg / sudo apt install ffmpeg
Models not downloaded	Inform user: first transcription will auto-download models (~60MB) to ~/.coli/models/

If coli is missing, stop here and do not proceed.

Step 0: Config Setup

Follow shared/config-pattern.md Step 0 (Zero-Question Boot).

If file doesn't exist — silently create with defaults and proceed:

mkdir -p ".listenhub/asr"
echo '{"model":"sensevoice","polish":true}' > ".listenhub/asr/config.json"
CONFIG_PATH=".listenhub/asr/config.json"
CONFIG=$(cat "$CONFIG_PATH")


Do NOT ask any setup questions. Proceed directly to the Interaction Flow with sensible defaults (sensevoice model, polish enabled).

If file exists — read config silently and proceed:

CONFIG_PATH=".listenhub/asr/config.json"
[ ! -f "$CONFIG_PATH" ] && CONFIG_PATH="$HOME/.listenhub/asr/config.json"
CONFIG=$(cat "$CONFIG_PATH")

Setup Flow (user-initiated reconfigure only)

Only run when the user explicitly asks to reconfigure. Display current settings:

当前配置 (asr)：
  模型：sensevoice / whisper-tiny.en
  润色：开启 / 关闭


Ask in order:

model: "默认使用哪个语音识别模型？"

"sensevoice（推荐）" — 支持中英日韩粤，可检测语言、情绪、音频事件
"whisper-tiny.en" — 仅英文

polish: "转录后由 AI 润色文本？（修正标点、去语气词、提升可读性）"

"是（推荐）" → polish: true
"否，保留原始转录" → polish: false

Save all answers at once after collecting them.

Step 1: Get Audio File

If the user hasn't provided a file path, ask:

"请提供要转录的音频文件路径。"

Verify the file exists before proceeding.

Step 2: Confirm
准备转录：

  文件：{filename}
  模型：{model}
  润色：{是 / 否}

继续？

Step 3: Transcribe

Run coli asr with JSON output (to get metadata):

coli asr -j --model {model} "{file}"


On first run, coli will automatically download the required model. This may take a moment — inform the user if models haven't been downloaded yet.

Parse the JSON result to extract text, lang, emotion, event, duration.

Step 4: Polish (if enabled)

If polish is true, take the raw text from the transcription result and rewrite it to fix punctuation, remove filler words, and improve readability. Preserve the original meaning and speaker intent. Do not summarize or paraphrase.

Step 5: Present Result

Display the transcript directly in the conversation:

转录完成

{transcript text}

─────────────────
语言：{lang} · 情绪：{emotion} · 时长：{duration}s


If polished, show the polished version with a note that it was AI-refined. Offer to show the raw original on request.

Step 6: Export as Markdown (optional)

After presenting the result, ask:

Question: "保存为 Markdown 文件到当前目录？"
Options:
  - "是" — save to current directory
  - "否" — done


If yes, write {audio-filename}-transcript.md to the current working directory (where the user is running Claude Code). The file should contain the transcript text (polished version if polish was enabled), with a front-matter header:

---
source: {original audio filename}
date: {YYYY-MM-DD}
model: {model used}
duration: {duration}s
lang: {detected language}
---

{transcript text}

Composability
Invoked by: future skills that need to transcribe recorded audio
Invokes: nothing
Examples

"帮我转录这个文件 meeting.m4a"

Check prerequisites
Read config
Confirm: meeting.m4a, sensevoice, polish on
Run coli asr -j --model sensevoice "meeting.m4a"
Polish the raw text
Display inline

"transcribe interview.wav, no polish"

Check prerequisites
Read config
Override polish to false for this session
Run coli asr -j --model sensevoice "interview.wav"
Display raw transcript inline
Weekly Installs
789
Repository
marswaveai/skills
GitHub Stars
49
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass