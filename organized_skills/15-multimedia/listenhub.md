---
rating: ⭐⭐
title: listenhub
url: https://skills.sh/marswaveai/skills/listenhub
---

# listenhub

skills/marswaveai/skills/listenhub
listenhub
Installation
$ npx skills add https://github.com/marswaveai/skills --skill listenhub
Summary

Deprecated skill — migrate to individual focused skills for podcasts, videos, TTS, and image generation.

This skill has been replaced by separate, specialized skills: /podcast, /explainer, /tts, /image-gen, and /content-parser
Users should upgrade by running npx skills add marswaveai/skills and restarting their agent
Do not execute requests until the user has completed the migration to the new skill set
SKILL.md
Purpose

This is a router skill. When users trigger a general ListenHub action, this skill identifies the intent and delegates to the appropriate specialized skill.

Routing Table
User intent	Keywords	Route to
Podcast	"podcast", "播客", "debate", "dialogue"	/podcast
Explainer video	"explainer", "解说视频", "tutorial video"	/explainer
Slides / PPT	"slides", "幻灯片", "PPT", "presentation"	/slides
TTS / Read aloud	"TTS", "read aloud", "朗读", "配音", "语音合成"	/tts
Image generation	"generate image", "画一张", "生成图片", "AI图"	/image-gen
Music	"music", "音乐", "生成音乐", "翻唱", "cover"	/music
Content extraction	"parse URL", "extract content", "解析链接"	/content-parser
Audio transcription	"transcribe", "ASR", "语音转文字"	/asr
Creator workflow	"创作", "写公众号", "小红书", "口播"	/creator
How to Route
Read the user's message and identify which category it falls into
Tell the user which skill you're routing to
Follow that skill's SKILL.md completely

If the intent is ambiguous, ask the user to clarify:

Question: "What would you like to create?"
Options:
  - "Podcast" — Audio discussion on a topic
  - "Explainer Video" — Narrated video with AI visuals
  - "Slides" — Slide deck / presentation
  - "Music" — AI-generated music or cover

Prerequisites

Most skills require the ListenHub CLI. Check:

listenhub auth status --json


If not installed or not logged in, handle automatically — never ask the user to run install commands:

Auto-install: run npm install -g @marswave/listenhub-cli silently
Auto-login: run listenhub auth login (opens browser)

Exception: /asr runs locally and needs no CLI or API key.

Weekly Installs
967
Repository
marswaveai/skills
GitHub Stars
49
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass