---
rating: ⭐⭐⭐
title: ai-tools
url: https://skills.sh/samhvw8/dotfiles/ai-tools
---

# ai-tools

skills/samhvw8/dotfiles/ai-tools
ai-tools
Installation
$ npx skills add https://github.com/samhvw8/dotfiles --skill ai-tools
SKILL.md
Google AI Tools

Unified integration for Google's AI ecosystem: Gemini API (multimodal), Gemini CLI, and NotebookLM.

Module Selection
Need	Module	When to Use
Media Processing	Gemini API	Audio/image/video/PDF analysis, generation
Second Opinion	Gemini CLI	Code review, cross-validation, alternative perspective
Web Research	Gemini CLI	Current info via Google Search grounding
Doc-Grounded Q&A	NotebookLM	Questions from uploaded documents
Gemini API (Multimodal)

Process audio, images, videos, documents, and generate images.

Prerequisites
export GEMINI_API_KEY="your-key"  # Get from https://aistudio.google.com/apikey
pip install google-genai python-dotenv pillow

Quick Commands

Transcribe Audio:

python scripts/gemini_batch_process.py --files audio.mp3 --task transcribe --model gemini-2.5-flash


Analyze Image:

python scripts/gemini_batch_process.py --files image.jpg --task analyze --prompt "Describe this" --output output.md


Process Video:

python scripts/gemini_batch_process.py --files video.mp4 --task analyze --prompt "Summarize with timestamps"


Extract from PDF:

python scripts/gemini_batch_process.py --files doc.pdf --task extract --prompt "Extract tables as JSON" --format json


Generate Image:

python scripts/gemini_batch_process.py --task generate --prompt "A futuristic city" --model gemini-2.5-flash-image

Model Selection
Model	Use Case	Context
gemini-2.5-flash	General (best price/perf)	1-2M tokens
gemini-2.5-pro	Highest quality	1-2M tokens
gemini-2.5-flash-image	Image generation	-
Supported Formats
Audio: WAV, MP3, AAC, FLAC, OGG (up to 9.5 hrs)
Images: PNG, JPEG, WEBP, HEIC (up to 3,600 images)
Video: MP4, MOV, AVI, WebM (up to 6 hrs)
Documents: PDF (up to 1,000 pages)

References: references/audio-processing.md, references/vision-understanding.md, references/video-analysis.md, references/document-extraction.md, references/image-generation.md

Gemini CLI

Orchestrate Gemini for code review, web search, and parallel tasks.

Verify Installation
command -v gemini || which gemini

Quick Commands

Code Generation:

gemini "Create [description]. Output complete file." --yolo -o text


Code Review:

gemini "Review [file] for bugs and security issues" -o text


Web Research:

gemini "What are the latest [topic]? Use Google Search." -o text


Architecture Analysis:

gemini "Use codebase_investigator to analyze this project" -o text


Faster Model:

gemini "[prompt]" -m gemini-2.5-flash -o text

Key Flags
--yolo / -y: Auto-approve tool calls
-o text: Human-readable output
-o json: Structured output
-m gemini-2.5-flash: Faster model
When to Use

✅ Second opinion on code ✅ Current web information ✅ Codebase architecture analysis ✅ Parallel code generation

❌ Simple quick tasks ❌ Interactive refinement

References: references/gemini-reference.md, references/gemini-patterns.md, references/gemini-templates.md, references/gemini-tools.md

NotebookLM

Query uploaded documents with source-grounded answers.

Prerequisites
python scripts/run.py auth_manager.py status  # Check auth
python scripts/run.py auth_manager.py setup   # One-time setup (browser visible)

Quick Commands

List Notebooks:

python scripts/run.py notebook_manager.py list


Add Notebook:

python scripts/run.py notebook_manager.py add \
  --url "https://notebooklm.google.com/notebook/..." \
  --name "Name" --description "What it contains" --topics "topic1,topic2"


Ask Question:

python scripts/run.py ask_question.py --question "Your question" --notebook-id ID


Search Notebooks:

python scripts/run.py notebook_manager.py search --query "keyword"

Critical Notes
Always use run.py wrapper - Handles venv automatically
Browser visible for auth - Required for Google login
Follow-up questions - Don't stop at first answer
Rate limit: 50 queries/day on free accounts

References: references/notebooklm-api.md, references/notebooklm-troubleshooting.md

Scripts Overview
Gemini API Scripts (in scripts/)
Script	Purpose
gemini_batch_process.py	Batch process media files
media_optimizer.py	Prepare media for API limits
document_converter.py	Convert docs to PDF
NotebookLM Scripts (via run.py)
Script	Purpose
auth_manager.py	Authentication management
notebook_manager.py	Library CRUD
ask_question.py	Query interface
cleanup_manager.py	Data cleanup
Cost Optimization
Gemini API Pricing
Model	Input	Output
2.5 Flash	$1.00/1M	$0.10/1M
2.5 Pro	$3.00/1M	$12.00/1M
Token Rates
Audio: 32 tokens/sec (1 min = 1,920 tokens)
Video: ~300 tokens/sec
PDF: 258 tokens/page
Image: 258-1,548 tokens
Best Practices
Use gemini-2.5-flash for most tasks
Use File API for files >20MB
Optimize media before upload
Process specific segments, not full videos
Error Handling
Error	Solution
401	Check API key
429	Rate limit - wait or use flash model
ModuleNotFoundError	Use run.py wrapper
Auth fails	Browser must be visible
References
Gemini API
references/audio-processing.md
references/vision-understanding.md
references/video-analysis.md
references/document-extraction.md
references/image-generation.md
Gemini CLI
references/gemini-reference.md
references/gemini-patterns.md
references/gemini-templates.md
references/gemini-tools.md
NotebookLM
references/notebooklm-api.md
references/notebooklm-troubleshooting.md
references/notebooklm-usage.md
Resources
Gemini API Key
Gemini API Docs
NotebookLM
Weekly Installs
28
Repository
samhvw8/dotfiles
GitHub Stars
12
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn