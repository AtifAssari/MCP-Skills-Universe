---
rating: ⭐⭐⭐
title: ai-video-generation
url: https://skills.sh/inference-sh/skills/ai-video-generation
---

# ai-video-generation

skills/inference-sh/skills/ai-video-generation
ai-video-generation
Originally frominfsh-skills/skills
Installation
$ npx skills add https://github.com/inference-sh/skills --skill ai-video-generation
Summary

Generate videos with 40+ AI models including Veo, Seedance, Wan, and Grok via inference.sh CLI.

Supports text-to-video, image-to-video, avatar animation, lipsync, video upscaling, and foley sound generation across multiple model families
Access to Google Veo (3.1, 3, 2), ByteDance Seedance, Falai Wan, xAI Grok, and economical alternatives like P-Video and WAN models
Includes utility tools for video upscaling, sound effect generation, and multi-clip merging with transitions
Requires inference.sh CLI (infsh) installation and authentication to run video generation commands
SKILL.md
AI Video Generation

Generate videos with 40+ AI models via inference.sh CLI.

Quick Start

Requires inference.sh CLI (belt). Install instructions

belt login

# Generate a video with Veo
belt app run google/veo-3-1-fast --input '{"prompt": "drone shot flying over a forest"}'

Available Models
Text-to-Video
Model	App ID	Best For
Veo 3.1 Fast	google/veo-3-1-fast	Fast, with optional audio
Veo 3.1	google/veo-3-1	Best quality, frame interpolation
Veo 3	google/veo-3	High quality with audio
Veo 3 Fast	google/veo-3-fast	Fast with audio
Veo 2	google/veo-2	Realistic videos
P-Video	pruna/p-video	Fast, economical, with audio support
WAN-T2V	pruna/wan-t2v	Economical 480p/720p
Grok Video	xai/grok-imagine-video	xAI, configurable duration
Seedance 2 T2V	falai/seedance-2-t2v	Text-to-video with sync audio
Seedance 2 R2V	falai/seedance-2-r2v	Reference images/videos/audio to video
HappyHorse T2V	alibaba/happyhorse-1-0-t2v	Physically realistic, up to 15s
Image-to-Video
Model	App ID	Best For
Wan 2.5	falai/wan-2-5	Animate any image
Wan 2.5 I2V	falai/wan-2-5-i2v	High quality i2v
WAN-I2V	pruna/wan-i2v	Economical 480p/720p
P-Video	pruna/p-video	Fast i2v with audio
Seedance 2 I2V	falai/seedance-2-i2v	Animate images with sync audio
HappyHorse I2V	alibaba/happyhorse-1-0-i2v	Animate images, up to 1080P/15s
HappyHorse R2V	alibaba/happyhorse-1-0-r2v	Character-preserving from references
Avatar / Lipsync
Model	App ID	Best For
OmniHuman 1.5	bytedance/omnihuman-1-5	Multi-character
OmniHuman 1.0	bytedance/omnihuman-1-0	Single character
Fabric 1.0	falai/fabric-1-0	Image talks with lipsync
PixVerse Lipsync	falai/pixverse-lipsync	Realistic lipsync
Video Editing
Model	App ID	Best For
HappyHorse Edit	alibaba/happyhorse-1-0-video-edit	Natural language video editing
Utilities
Tool	App ID	Description
HunyuanVideo Foley	infsh/hunyuanvideo-foley	Add sound effects to video
Topaz Upscaler	falai/topaz-video-upscaler	Upscale video quality
Media Merger	infsh/media-merger	Merge videos with transitions
Browse All Video Apps
belt app list --category video

Examples
Text-to-Video with Veo
belt app run google/veo-3-1-fast --input '{
  "prompt": "A timelapse of a flower blooming in a garden"
}'

Grok Video
belt app run xai/grok-imagine-video --input '{
  "prompt": "Waves crashing on a beach at sunset",
  "duration": 5
}'

Image-to-Video with Wan 2.5
belt app run falai/wan-2-5 --input '{
  "image_url": "https://your-image.jpg"
}'

AI Avatar / Talking Head
belt app run bytedance/omnihuman-1-5 --input '{
  "image_url": "https://portrait.jpg",
  "audio_url": "https://speech.mp3"
}'

Fabric Lipsync
belt app run falai/fabric-1-0 --input '{
  "image_url": "https://face.jpg",
  "audio_url": "https://audio.mp3"
}'

Seedance 2.0 Text-to-Video with Audio
belt app run falai/seedance-2-t2v --input '{
  "prompt": "a jazz band performing in a dimly lit club",
  "generate_audio": true,
  "duration": 10
}'

Seedance 2.0 Reference-to-Video
belt app run falai/seedance-2-r2v --input '{
  "prompt": "A person who looks like @Image1 walking through a garden",
  "images": ["https://portrait.jpg"],
  "generate_audio": true
}'

HappyHorse Text-to-Video
belt app run alibaba/happyhorse-1-0-t2v --input '{
  "prompt": "a golden retriever running through autumn leaves, slow motion",
  "duration": 10,
  "resolution": "1080P"
}'

HappyHorse Video Editing
belt app run alibaba/happyhorse-1-0-video-edit --input '{
  "video": "https://your-video.mp4",
  "prompt": "change the background to a snowy mountain landscape"
}'

PixVerse Lipsync
belt app run falai/pixverse-lipsync --input '{
  "image_url": "https://portrait.jpg",
  "audio_url": "https://speech.mp3"
}'

Video Upscaling
belt app run falai/topaz-video-upscaler --input '{"video_url": "https://..."}'

Add Sound Effects (Foley)
belt app run infsh/hunyuanvideo-foley --input '{
  "video_url": "https://silent-video.mp4",
  "prompt": "footsteps on gravel, birds chirping"
}'

Merge Videos
belt app run infsh/media-merger --input '{
  "videos": ["https://clip1.mp4", "https://clip2.mp4"],
  "transition": "fade"
}'

Related Skills
# Full platform skill (all 250+ apps)
npx skills add inference-sh/skills@infsh-cli

# Pruna P-Video (fast & economical)
npx skills add inference-sh/skills@p-video

# Google Veo specific
npx skills add inference-sh/skills@google-veo

# Seedance 2.0
npx skills add inference-sh/skills@seedance

# HappyHorse 1.0
npx skills add inference-sh/skills@happyhorse

# AI avatars & lipsync
npx skills add inference-sh/skills@ai-avatar-video

# Text-to-speech (for video narration)
npx skills add inference-sh/skills@text-to-speech

# Image generation (for image-to-video)
npx skills add inference-sh/skills@ai-image-generation

# Twitter (post videos)
npx skills add inference-sh/skills@twitter-automation


Browse all apps: belt app list

Documentation
Running Apps - How to run apps via CLI
Streaming Results - Real-time progress updates
Content Pipeline Example - Building media workflows
Weekly Installs
652
Repository
inference-sh/skills
GitHub Stars
395
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn