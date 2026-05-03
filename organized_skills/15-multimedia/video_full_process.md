---
rating: ⭐⭐⭐
title: video-full-process
url: https://skills.sh/jykim/claude-obsidian-skills/video-full-process
---

# video-full-process

skills/jykim/claude-obsidian-skills/video-full-process
video-full-process
Installation
$ npx skills add https://github.com/jykim/claude-obsidian-skills --skill video-full-process
SKILL.md
Video Full Process Skill

Combines video-clean and video-add-chapters into a single workflow that:

Transcribes once (saving API costs)
Removes pauses and filler words
Detects and embeds chapters
Remaps chapter timestamps to the cleaned video
Generates YouTube chapter markers and documentation
When to Use This Skill
Processing raw video recordings end-to-end
Creating polished videos with embedded chapters
Generating YouTube-ready content with chapter markers
When you need both pause removal AND chapter organization
Quick Start
# Full processing with default settings
python process_video.py "video.mp4" --language ko

# Preview mode (see what will be changed)
python process_video.py "video.mp4" --preview

# Skip chapter embedding (only clean + generate docs)
python process_video.py "video.mp4" --no-embed-chapters

Workflow Overview
Input: raw_video.mp4
           │
           ▼
┌─────────────────────────────────────┐
│ 1. Transcribe (once)                │
│    - Uses chunked transcription     │
│    - Handles long videos (15min+)   │
│    - Output: transcript.json        │
└─────────────────────────────────────┘
           │
     ┌─────┴─────┐
     ▼           ▼
┌─────────┐  ┌─────────────┐
│ 2a.     │  │ 2b. Detect  │  ← Parallel
│ Clean   │  │ Chapters    │
└─────────┘  └─────────────┘
     │           │
     ▼           ▼
┌─────────┐  ┌─────────────┐
│ cleaned │  │ chapters.   │
│ .mp4    │  │ json        │
│ + pauses│  │             │
│ .json   │  │             │
└─────────┘  └─────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│ 3. Remap chapters to cleaned video  │
│    - Calculate removed time         │
│    - Adjust chapter timestamps      │
└─────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│ 4. Embed chapters + Generate docs   │
│    - ffmpeg metadata embed          │
│    - YouTube chapters txt           │
│    - Chapter markdown files         │
└─────────────────────────────────────┘
           │
           ▼
Output: cleaned-chapters.mp4 + docs

Output Files
File	Description
{video} - cleaned.mp4	Video with pauses/fillers removed
{video} - cleaned-chapters.mp4	Cleaned video with embedded chapters
{video} - pauses.json	Removed pause data (for remapping)
{video} - chapters.json	Detected chapter boundaries
{video} - chapters_remapped.json	Chapters adjusted for cleaned video
{video} - youtube_chapters.txt	Copy-paste for YouTube description
Chapter NN - Title.md	Per-chapter documentation
Requirements
System
Python 3.7+
FFmpeg (for video processing)
Python Packages
pip install openai

Environment Variables
OPENAI_API_KEY - Required for Whisper API
Detailed Usage
Full Processing
python process_video.py "presentation.mp4" --language ko


This runs:

Transcription (if not exists)
Chapter detection
Pause removal
Chapter remapping
Chapter embedding
Documentation generation
Partial Processing
# Skip transcription (reuse existing)
python process_video.py "video.mp4" --skip-transcribe

# Skip cleaning (only add chapters)
python process_video.py "video.mp4" --skip-clean

# Skip chapter embedding (only clean + generate docs)
python process_video.py "video.mp4" --no-embed-chapters

Customization
# Adjust pause threshold
python process_video.py "video.mp4" --pause-threshold 0.8

# Custom output directory
python process_video.py "video.mp4" --output-dir "./output"

Chapter Remapping Logic

When pauses are removed, chapter timestamps must be adjusted:

Original Video:
|--Ch1--|--pause--|--Ch2--|--pause--|--Ch3--|
0       30        40      60        70      90

Cleaned Video (pauses removed):
|--Ch1--|--Ch2--|--Ch3--|
0       30      50      70

Remapping:
- Ch1: 0 → 0 (no change)
- Ch2: 40 → 30 (10s pause removed before)
- Ch3: 70 → 50 (20s total pauses removed before)


The remap_chapters.py script handles this automatically using the pause data from video cleaning.

Integration with Existing Skills

This skill orchestrates two existing skills:

video-clean (.claude/skills/video-cleaning/)
Provides: transcribe_video.py, edit_video_remove_pauses.py
Modified: Added --output-pauses flag
video-add-chapters (Settings/Skills/video-add-chapters/)
Provides: transcribe_video.py, suggest_chapters.py, generate_docs.py
Modified: Added --skip-if-exists flag
Cost Estimate
Single transcription: ~$0.006/min (vs $0.012/min if running separately)
1-hour video: ~$0.36 (saves $0.36 by reusing transcript)
Troubleshooting
"Transcript not found" Error

Run transcription first or use --force-transcribe:

python process_video.py "video.mp4" --force-transcribe

"Chapter timestamps don't match"

Regenerate remapped chapters:

python remap_chapters.py "video - chapters.json" --pauses "video - pauses.json"

FFmpeg embed fails

Check that chapters.json format is correct:

{
  "chapters": [
    {"start": 0, "title": "Intro", "description": "..."},
    {"start": 120, "title": "Main", "description": "..."}
  ]
}

File Structure
video-full-process/
├── SKILL.md              # This documentation
├── process_video.py      # Main orchestrator script
└── remap_chapters.py     # Chapter timestamp remapping

Version History
v1.0 (2026-01): Initial release
Unified workflow for video-clean + video-add-chapters
Transcript reuse (single API call)
Automatic chapter remapping
FFmpeg chapter embedding
Weekly Installs
13
Repository
jykim/claude-ob…n-skills
GitHub Stars
43
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass