---
rating: ⭐⭐⭐
title: remotion-video-toolkit
url: https://skills.sh/shreefentsar/remotion-video-toolkit/remotion-video-toolkit
---

# remotion-video-toolkit

skills/shreefentsar/remotion-video-toolkit/remotion-video-toolkit
remotion-video-toolkit
Installation
$ npx skills add https://github.com/shreefentsar/remotion-video-toolkit --skill remotion-video-toolkit
SKILL.md
Remotion Video Toolkit

Write React components, get real MP4 videos. This skill teaches your AI agent how to build with Remotion — from a first animation to a production rendering pipeline.

29 rules. Every major Remotion feature covered.

What you can build with this

Personalized video at scale Feed user data as JSON props, render a unique video per user. Think Spotify Wrapped, GitHub Unwrapped, onboarding walkthroughs — one template, thousands of outputs.

Automated social media clips Pull live data (stats, leaderboards, product metrics) and render daily or weekly video posts without anyone touching a timeline editor.

Dynamic ads and marketing videos Swap in customer name, product image, pricing. Same template, infinite variations. Render server-side via API or Lambda.

Animated data visualizations Turn dashboards and KPI reports into shareable video clips with animated charts and transitions.

TikTok and Reels captions Transcribe audio, display word-by-word highlighted subtitles, export ready for upload.

Product showcase videos Auto-generate from your database — images, specs, pricing — straight to MP4.

Educational and explainer content Animated course materials, certificate videos, step-by-step walkthroughs — all driven by code.

Video generation as a service Expose rendering as an HTTP endpoint. Your app sends JSON, gets back a video file.

Requirements
Node.js 18+
React 18+ (Remotion renders React components frame-by-frame)
Remotion — scaffold with npx create-video@latest
FFmpeg — ships with @remotion/renderer, no separate install needed
For serverless rendering: AWS account (Lambda) or GCP account (Cloud Run)
What's inside
Core
Rule	Description
Compositions	Define videos, stills, folders, default props, dynamic metadata
Rendering	CLI, Node.js API, AWS Lambda, Cloud Run, Express server patterns
Calculate metadata	Set duration, dimensions, and props dynamically at render time
Animation and timing
Rule	Description
Animations	Fade, scale, rotate, slide
Timing	Interpolation curves, easing, spring physics
Sequencing	Delay, chain, and orchestrate scenes
Transitions	Scene-to-scene transitions
Trimming	Cut the start or end of any animation
Text and typography
Rule	Description
Text animations	Typewriter, word highlight, reveal effects
Fonts	Google Fonts and local font loading
Measuring text	Fit text to containers, detect overflow
Media
Rule	Description
Videos	Embed, trim, speed, volume, loop, pitch shift
Audio	Import, trim, fade, volume and speed control
Images	The Img component
GIFs	Timeline-synced GIF playback
Assets	Importing any media into compositions
Decode check	Validate browser compatibility
Captions and subtitles
Rule	Description
Transcribe captions	Audio to captions via Whisper, Deepgram, or AssemblyAI
Display captions	TikTok-style word-by-word highlighting
Import SRT	Load existing .srt files
Data visualization
Rule	Description
Charts	Animated bar charts, line graphs, data-driven visuals
Advanced
Rule	Description
3D content	Three.js and React Three Fiber
Lottie	After Effects animations via Lottie
TailwindCSS	Style compositions with Tailwind
DOM measurement	Measure element dimensions at render time
Media utilities
Rule	Description
Video duration	Get length in seconds
Video dimensions	Get width and height
Audio duration	Get audio length
Extract frames	Pull frames at specific timestamps
Quick start
# Scaffold a project
npx create-video@latest my-video

# Preview in browser
cd my-video && npm start

# Render to MP4
npx remotion render src/index.ts MyComposition out/video.mp4

# Pass dynamic data
npx remotion render src/index.ts MyComposition out.mp4 --props '{"title": "Hello"}'

Contribute

Source: github.com/shreefentsar/remotion-video-toolkit

Missing something? Found a better approach? Open a PR — new rules, improved examples, bug fixes all welcome.

Built by Zone 99

Weekly Installs
492
Repository
shreefentsar/re…-toolkit
GitHub Stars
11
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn