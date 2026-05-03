---
title: video-engineer
url: https://skills.sh/404kidwiz/claude-supercode-skills/video-engineer
---

# video-engineer

skills/404kidwiz/claude-supercode-skills/video-engineer
video-engineer
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill video-engineer
SKILL.md
Video Engineer
Purpose

Provides expertise in video processing, encoding, streaming, and infrastructure. Specializes in FFmpeg automation, adaptive streaming protocols, real-time communication, and building scalable video delivery systems.

When to Use
Implementing video encoding and transcoding pipelines
Setting up HLS or DASH streaming infrastructure
Building WebRTC applications for real-time video
Automating video processing with FFmpeg
Optimizing video quality and compression
Creating video thumbnails and previews
Implementing video analytics and metadata extraction
Building video player integrations
Quick Start

Invoke this skill when:

Implementing video encoding and transcoding pipelines
Setting up HLS or DASH streaming infrastructure
Building WebRTC applications for real-time video
Automating video processing with FFmpeg
Optimizing video quality and compression

Do NOT invoke when:

Building general web applications → use fullstack-developer
Creating animated GIFs → use slack-gif-creator
Media file analysis only → use multimodal-analysis
Image processing without video → use appropriate skill
Decision Framework
Video Engineering Task?
├── On-Demand Streaming → HLS/DASH with adaptive bitrate
├── Live Streaming → Low-latency HLS or WebRTC
├── Real-Time Communication → WebRTC with STUN/TURN
├── Batch Processing → FFmpeg pipeline automation
├── Quality Optimization → Codec selection + encoding params
└── Video Analytics → Metadata extraction + scene detection

Core Workflows
1. Adaptive Streaming Setup
Analyze source video specifications
Define quality ladder (resolutions, bitrates)
Configure encoder settings per quality level
Generate HLS/DASH manifests
Set up CDN for segment delivery
Implement player with ABR support
Monitor playback quality metrics
2. FFmpeg Processing Pipeline
Define input sources and formats
Build filter graph for transformations
Configure encoding parameters
Handle audio/video synchronization
Implement error handling and retries
Parallelize for throughput
Validate output quality
3. WebRTC Implementation
Set up signaling server
Configure STUN/TURN servers
Implement peer connection handling
Manage media tracks and streams
Handle network adaptation (simulcast, SVC)
Implement recording if needed
Monitor connection quality metrics
Best Practices
Use hardware encoding (NVENC, QSV) when available for speed
Implement adaptive bitrate for variable network conditions
Pre-generate all quality levels for on-demand content
Use appropriate codecs for use case (H.264 compatibility, H.265/AV1 efficiency)
Set keyframe intervals appropriate for seeking and ABR switching
Monitor and alert on encoding queue depth and latency
Anti-Patterns
Single bitrate streaming → Always use adaptive bitrate
Ignoring audio sync → Verify A/V alignment after processing
Oversized segments → Keep HLS segments 2-10 seconds
No error handling → FFmpeg can fail; implement retries
Hardcoded paths → Parameterize for different environments
Weekly Installs
120
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass