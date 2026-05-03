---
title: minimax-multimodal-toolkit
url: https://skills.sh/minimax-ai/skills/minimax-multimodal-toolkit
---

# minimax-multimodal-toolkit

skills/minimax-ai/skills/minimax-multimodal-toolkit
minimax-multimodal-toolkit
Installation
$ npx skills add https://github.com/minimax-ai/skills --skill minimax-multimodal-toolkit
SKILL.md
MiniMax Multi-Modal Toolkit

Generate voice, music, video, and image content via MiniMax APIs — the unified entry for MiniMax multimodal use cases (audio + music + video + image). Includes voice cloning & voice design for custom voices, image generation with character reference, and FFmpeg-based media tools for audio/video format conversion, concatenation, trimming, and extraction.

Setup & Configuration
Prerequisites
brew install ffmpeg jq              # macOS
sudo apt install ffmpeg jq          # Linux (Debian/Ubuntu)
bash scripts/check_environment.sh   # verify environment


No Python or pip required — all scripts are pure bash using curl, ffmpeg, jq, and xxd.

Note: ffmpeg is required for TTS voice bubble conversion (.mp3 → .opus). Without it, TTS audio sends as a file attachment instead of a native voice bubble.

API Configuration

MiniMax provides two service endpoints for different regions:

Region	API Host
China Mainland（中国大陆）	https://api.minimaxi.com
Global（全球）	https://api.minimax.io

In OpenClaw — create a .env file in the skill directory (scripts load it automatically, no shell export needed):

~/.openclaw/workspace/skills/minimax-multimodal-toolkit/.env

MINIMAX_API_KEY=sk-cp-...
MINIMAX_API_HOST=https://api.minimaxi.com


Or configure via openclaw.json:

"skills": {
  "entries": {
    "minimax-multimodal-toolkit": {
      "env": {
        "MINIMAX_API_HOST": "https://api.minimaxi.com",
        "MINIMAX_API_KEY": "sk-cp-..."
      }
    }
  }
}


In other environments — set environment variables before running any script:

export MINIMAX_API_HOST="https://api.minimaxi.com"
export MINIMAX_API_KEY="your-key-here"


Keys start with sk-api- or sk-cp-, obtainable from https://platform.minimaxi.com (China) or https://platform.minimax.io (Global)

IMPORTANT — When credentials are missing: Before running any script, check that both MINIMAX_API_HOST and MINIMAX_API_KEY are set. If either is missing: ask the user for their region and API key, then help them configure using one of the methods above.

Output & Sending
Output Directory

All generated files MUST be saved to minimax-output/ under the AGENT'S current working directory (NOT the skill directory). Every script call MUST include an explicit --output / -o argument pointing to this location. Never omit the output argument or rely on script defaults.

Rules:

Before running any script, ensure minimax-output/ exists in the agent's working directory (create if needed: mkdir -p minimax-output)
Always use absolute or relative paths from the agent's working directory: --output minimax-output/video.mp4
Never cd into the skill directory to run scripts — run from the agent's working directory using the full script path
Intermediate/temp files (segment audio, video segments, extracted frames) are automatically placed in minimax-output/tmp/. They can be cleaned up when no longer needed: rm -rf minimax-output/tmp
Sending to Feishu (Native Bubbles)

After generating any media file, send it as a native Feishu bubble using the message tool:

message action=send media=<file-path>


Do NOT use [[reply_to_current]] for media — always use the message tool with the media parameter.

Media type	Format	Notes
Images	PNG/JPG/WebP	Send directly
Video	.mp4	Send directly
Music	.mp3	Send directly
TTS / Voice	Must convert to .opus first	MP3 sends as a file attachment, NOT a voice bubble

TTS audio — required conversion for native voice bubble:

ffmpeg -i output.mp3 -c:a libopus -b:a 128k -y output.opus
message action=send media=output.opus

Plan Limits & Quotas

IMPORTANT — Always respect the user's plan limits before generating content. If the user's quota is exhausted or insufficient, warn them before proceeding.

Standard Plans
Capability	Starter	Plus	Max
M2.7 (chat)	600 req/5h	1,500 req/5h	4,500 req/5h
Speech 2.8	—	4,000 chars/day	11,000 chars/day
image-01	—	50 images/day	120 images/day
Hailuo-2.3-Fast 768P 6s	—	—	2 videos/day
Hailuo-2.3 768P 6s	—	—	2 videos/day
Music-2.5	—	—	4 songs/day (≤5 min each)
High-Speed Plans
Capability	Plus-HS	Max-HS	Ultra-HS
M2.7-highspeed (chat)	1,500 req/5h	4,500 req/5h	30,000 req/5h
Speech 2.8	9,000 chars/day	19,000 chars/day	50,000 chars/day
image-01	100 images/day	200 images/day	800 images/day
Hailuo-2.3-Fast 768P 6s	—	3 videos/day	5 videos/day
Hailuo-2.3 768P 6s	—	3 videos/day	5 videos/day
Music-2.5	—	7 songs/day (≤5 min each)	15 songs/day (≤5 min each)

Key quota constraints:

Video resolution: 768P only — 1080P is not available on any plan
Video duration: 6s — all plan quotas are counted in 6-second units
Video quota is very limited (2–5/day depending on plan) — always confirm with the user before generating video
Key Capabilities
Capability	Description	Entry point
TTS	Text-to-speech synthesis with multiple voices and emotions	scripts/tts/generate_voice.sh
Voice Cloning	Clone a voice from an audio sample (10s–5min)	scripts/tts/generate_voice.sh clone
Voice Design	Create a custom voice from a text description	scripts/tts/generate_voice.sh design
Music Generation	Generate songs with lyrics or instrumental tracks	scripts/music/generate_music.sh
Image Generation	Text-to-image, image-to-image with character reference	scripts/image/generate_image.sh
Video Generation	Text-to-video, image-to-video, subject reference, templates	scripts/video/generate_video.sh
Long Video	Multi-scene chained video with crossfade transitions	scripts/video/generate_long_video.sh
Media Tools	Audio/video format conversion, concatenation, trimming, extraction	scripts/media_tools.sh
TTS (Text-to-Speech)

Entry point: scripts/tts/generate_voice.sh

🎙 Voice Selection (First Use)

On first TTS call, ask the user to pick a voice. Provide these options:

Recommended:

chunzhen_xuedi — 纯真学弟（乖巧、干净，适合日常）

Other options:

voice_id	Name	Feel
female-shaonv	少女	活泼年轻
female-yujie	御姐	成熟优雅
female-tianmei	甜美女性	温柔柔和
male-qn-qingse	青涩青年	校园青春
male-qn-badao	霸道青年	傲气强势
badao_shaoye	霸道少爷	霸总感
junlang_nanyou	俊朗男友	阳光温暖

Full list in references/tts-voice-catalog.md

How to set: After user picks, remember their choice and use -v <voice_id> in all subsequent TTS calls.

IMPORTANT: Single voice vs Multi-segment — Choose the right approach
User intent	Approach
Single voice / no multi-character need	tts command — generate the entire text in one call
Multiple characters / narrator + dialogue	generate command with segments.json

Default behavior: When the user simply asks to generate speech/voice and does NOT mention multiple voices or characters, use the tts command directly with a single appropriate voice. Do NOT split into segments or use the multi-segment pipeline — just pass the full text to tts in one call.

Only use multi-segment generate when:

The user explicitly needs multiple voices/characters
The text requires narrator + character dialogue separation
The text exceeds 10,000 characters (API limit per request) — in this case, split into segments with the same voice
Single-voice generation
# Generate TTS with chosen voice
bash scripts/tts/generate_voice.sh tts "你想说的话" -v chunzhen_xuedi -o minimax-output/output.mp3

# Convert to .opus (required for native Feishu voice bubble)
ffmpeg -i minimax-output/output.mp3 -c:a libopus -b:a 128k -y minimax-output/output.opus

# Send as native voice bubble
message action=send media=minimax-output/output.opus

Multi-segment generation (multi-voice / audiobook / podcast)

Complete workflow — follow ALL steps in order:

Write segments.json — split text into segments with voice assignments (see format and rules below)
Run generate command — this reads segments.json, generates audio for EACH segment via TTS API, then merges them into a single output file with crossfade
# Step 1: Write segments.json to minimax-output/
# (use the Write tool to create minimax-output/segments.json)

# Step 2: Generate audio from segments.json — this is the CRITICAL step
# It generates each segment individually and merges them into one file
bash scripts/tts/generate_voice.sh generate minimax-output/segments.json \
  -o minimax-output/output.mp3 --crossfade 200

# Step 3: Convert and send
ffmpeg -i minimax-output/output.mp3 -c:a libopus -b:a 128k -y minimax-output/output.opus
message action=send media=minimax-output/output.opus


Do NOT skip Step 2. Writing segments.json alone does nothing — you MUST run the generate command to actually produce audio.

Voice management
# List all available voices
bash scripts/tts/generate_voice.sh list-voices

# Voice cloning (from audio sample, 10s–5min)
bash scripts/tts/generate_voice.sh clone sample.mp3 --voice-id my-voice

# Voice design (from text description)
bash scripts/tts/generate_voice.sh design "A warm female narrator voice" --voice-id narrator

Audio processing
bash scripts/tts/generate_voice.sh merge part1.mp3 part2.mp3 -o minimax-output/combined.mp3
bash scripts/tts/generate_voice.sh convert input.wav -o minimax-output/output.mp3

TTS Models
Model	Notes
speech-2.8-hd	Recommended, auto emotion matching
speech-2.8-turbo	Faster variant
speech-2.6-hd	Previous gen, manual emotion
speech-2.6-turbo	Previous gen, faster
segments.json Format

Default crossfade between segments: 200ms (--crossfade 200).

[
  { "text": "Hello!", "voice_id": "female-shaonv", "emotion": "" },
  { "text": "Welcome.", "voice_id": "male-qn-qingse", "emotion": "happy" }
]


Leave emotion empty for speech-2.8 models (auto-matched from text).

IMPORTANT: Multi-Segment Script Generation Rules (Audiobooks, Podcasts, etc.)

When generating segments.json for audiobooks, podcasts, or any multi-character narration, you MUST split narration text from character dialogue into separate segments with distinct voices.

Rule: Narration and dialogue are ALWAYS separate segments.

A sentence like "Tom said: The weather is great today!" must be split into two segments:

Segment 1 (narrator voice): "Tom said:"
Segment 2 (character voice): "The weather is great today!"

Example — Audiobook with narrator + 2 characters:

[
  { "text": "Morning sunlight streamed into the classroom as students filed in one by one.", "voice_id": "narrator-voice", "emotion": "" },
  { "text": "Tom smiled and turned to Lisa:", "voice_id": "narrator-voice", "emotion": "" },
  { "text": "The weather is amazing today! Let's go to the park after school!", "voice_id": "tom-voice", "emotion": "happy" },
  { "text": "Lisa thought for a moment, then replied:", "voice_id": "narrator-voice", "emotion": "" },
  { "text": "Sure, but I need to drop off my backpack at home first.", "voice_id": "lisa-voice", "emotion": "" },
  { "text": "They exchanged a smile and went back to listening to the lecture.", "voice_id": "narrator-voice", "emotion": "" }
]


Key principles:

Narrator uses a consistent neutral narrator voice throughout
Each character has a dedicated voice_id, maintained consistently across all their dialogue
Split at dialogue boundaries — "He said:" is narrator, the quoted content is the character
Do NOT merge narrator text and character speech into a single segment
For characters without pre-existing voice_ids, use voice cloning or voice design to create them first, then reference the created voice_id in segments
Music Generation

Entry point: scripts/music/generate_music.sh

IMPORTANT: Instrumental vs Lyrics — When to use which
Scenario	Mode	Action
BGM for video / voice / podcast	Instrumental (default)	Use --instrumental directly, do NOT ask user
User explicitly asks to "create music" / "make a song"	Ask user first	Ask whether they want instrumental or with lyrics

When adding background music to video or voice content, always default to instrumental mode (--instrumental). Do not ask the user — BGM should never have vocals competing with the main content.

When the user explicitly asks to create/generate music as the primary task, ask them whether they want:

Instrumental (pure music, no vocals)
With lyrics (song with vocals — user provides or you help write lyrics)
# Instrumental (for BGM or when user chooses instrumental)
bash scripts/music/generate_music.sh \
  --instrumental \
  --prompt "ambient electronic, atmospheric" \
  --output minimax-output/ambient.mp3 --download
message action=send media=minimax-output/ambient.mp3

# Song with lyrics (when user chooses vocal music)
bash scripts/music/generate_music.sh \
  --lyrics "[verse]\nHello world\n[chorus]\nLa la la" \
  --prompt "indie folk, melancholic" \
  --output minimax-output/song.mp3 --download
message action=send media=minimax-output/song.mp3

Music Model

Default model: music-2.5

music-2.5 does not support --instrumental directly. When instrumental music is needed, the script automatically applies a workaround:

Sets lyrics to [intro] [outro] (empty structural tags, no actual vocals), appends pure music, no lyrics to the prompt

This produces instrumental-style output without requiring manual intervention. You can always use --instrumental and the script handles the rest.

Image Generation

Entry point: scripts/image/generate_image.sh

Model: image-01 — photorealistic image generation from text prompts, with optional character reference for image-to-image.

IMPORTANT: Mode Selection — t2i vs i2i
User intent	Mode
Generate image from text description (default)	t2i — text-to-image
Generate image with a character reference photo (keep same person)	i2i — image-to-image

Default behavior: When the user asks to generate/create an image without mentioning a reference photo, use t2i mode (default). Only use i2i mode when the user provides a character reference image or explicitly asks to base the image on an existing person's appearance.

IMPORTANT: Aspect Ratio — Infer from user context

Do NOT always default to 1:1. Analyze the user's request and choose the most appropriate aspect ratio:

User intent / context	Recommended ratio	Resolution
头像、图标、社交媒体头像、avatar、icon、profile pic	1:1	1024×1024
风景、横幅、桌面壁纸、landscape、banner、desktop wallpaper	16:9	1280×720
传统照片、经典比例、classic photo	4:3	1152×864
摄影作品、杂志封面、photography、magazine	3:2	1248×832
人像竖图、海报、portrait photo、poster	2:3	832×1248
竖版海报、书籍封面、tall poster、book cover	3:4	864×1152
手机壁纸、社交媒体故事、phone wallpaper、story、reel	9:16	720×1280
超宽全景、电影画幅、panoramic、cinematic ultrawide	21:9	1344×576
未指定特定需求 / ambiguous	1:1	1024×1024
IMPORTANT: Image Count — When to generate multiple images
User intent	Count (-n)
Default / single image request	1 (default)
用户说"几张"、"多张"、"一些" / "a few", "several"	3
用户说"多种方案"、"备选" / "variations", "options"	3–4
用户明确指定数量	Use the specified number (1–9)
Text-to-Image Examples
# Basic text-to-image
bash scripts/image/generate_image.sh \
  --prompt "A cat sitting on a rooftop at sunset, cinematic lighting, warm tones, photorealistic" \
  -o minimax-output/cat.png
message action=send media=minimax-output/cat.png

# Landscape with inferred aspect ratio
bash scripts/image/generate_image.sh \
  --prompt "Mountain landscape with misty valleys, photorealistic, golden hour" \
  --aspect-ratio 16:9 \
  -o minimax-output/landscape.png
message action=send media=minimax-output/landscape.png

# Phone wallpaper (portrait 9:16)
bash scripts/image/generate_image.sh \
  --prompt "Aurora borealis over a snowy forest, vivid colors, magical atmosphere" \
  --aspect-ratio 9:16 \
  -o minimax-output/wallpaper.png
message action=send media=minimax-output/wallpaper.png

# Multiple variations
bash scripts/image/generate_image.sh \
  --prompt "Abstract geometric art, vibrant colors" \
  -n 3 \
  -o minimax-output/art.png
message action=send media=minimax-output/art.png

# With prompt optimizer
bash scripts/image/generate_image.sh \
  --prompt "A man standing on Venice Beach, 90s documentary style" \
  --aspect-ratio 16:9 --prompt-optimizer \
  -o minimax-output/beach.png
message action=send media=minimax-output/beach.png

# Custom dimensions (must be multiple of 8)
bash scripts/image/generate_image.sh \
  --prompt "Product photo of a luxury watch on marble surface" \
  --width 1024 --height 768 \
  -o minimax-output/watch.png
message action=send media=minimax-output/watch.png

Image-to-Image (Character Reference)

Use a reference photo to generate images with the same character in new scenes. Best results with a single front-facing portrait. Supported formats: JPG, JPEG, PNG (max 10MB).

# Character reference — place same person in a new scene
bash scripts/image/generate_image.sh \
  --mode i2i \
  --prompt "A girl looking into the distance from a library window, warm afternoon light" \
  --ref-image face.jpg \
  --aspect-ratio 16:9 \
  -o minimax-output/girl_library.png
message action=send media=minimax-output/girl_library.png

# Multiple character variations
bash scripts/image/generate_image.sh \
  --mode i2i \
  --prompt "A woman in a red dress at a gala event, elegant, cinematic" \
  --ref-image face.jpg -n 3 \
  -o minimax-output/gala.png
message action=send media=minimax-output/gala.png

Aspect Ratio Reference
Ratio	Resolution	Best for
1:1	1024×1024	Default, avatars, icons, social media
16:9	1280×720	Landscape, banner, desktop wallpaper
4:3	1152×864	Classic photo, presentations
3:2	1248×832	Photography, magazine layout
2:3	832×1248	Portrait photo, poster
3:4	864×1152	Book cover, tall poster
9:16	720×1280	Phone wallpaper, social story/reel
21:9	1344×576	Ultra-wide panoramic, cinematic
Key Options
Option	Description
--prompt TEXT	Image description, max 1500 chars (required)
--aspect-ratio RATIO	Aspect ratio (see table above). Infer from user context
--width PX / --height PX	Custom size, 512–2048, must be multiple of 8, both required together. Overridden by --aspect-ratio if both set
-n N	Number of images to generate, 1–9 (default 1)
--seed N	Random seed for reproducibility. Same seed + same params → similar results
--prompt-optimizer	Enable automatic prompt optimization by the API
--ref-image FILE	Character reference image for i2i mode (local file or URL, JPG/JPEG/PNG, max 10MB)
--no-download	Print image URLs instead of downloading files
--aigc-watermark	Add AIGC watermark to generated images
Video Generation
IMPORTANT: Single vs Multi-Segment — Choose the right script
User intent	Script to use
Default / no special request	scripts/video/generate_video.sh (single segment, 6s, 768P)
User explicitly asks for "long video", "multi-scene", "story", or duration > 10s	scripts/video/generate_long_video.sh (multi-segment)

Default behavior: Always use single-segment generate_video.sh with duration 6s and resolution 768P unless the user explicitly asks for a long video or multi-scene video. Do NOT automatically split into multiple segments — a single 6s video is the standard output. Only use generate_long_video.sh when the user clearly needs multi-scene or longer content.

Entry point (single video): scripts/video/generate_video.sh Entry point (long/multi-scene): scripts/video/generate_long_video.sh

Video Model Constraints (MUST follow)

Supported resolutions and durations by model:

Model	Resolution	Duration
MiniMax-Hailuo-2.3	768P only	6s or 10s
MiniMax-Hailuo-2.3-Fast	768P only	6s or 10s
MiniMax-Hailuo-02	512P, 768P (default)	6s or 10s
T2V-01 / T2V-01-Director	720P	6s only
I2V-01 / I2V-01-Director / I2V-01-live	720P	6s only
S2V-01 (ref)	720P	6s only

Key rules:

Default: 6s + 768P — plan quotas are counted in 6-second units; use 6s unless user explicitly requests 10s
1080P is NOT supported on any plan — always use 768P for Hailuo-2.3/2.3-Fast
Older models (T2V-01, I2V-01, S2V-01) only support 6s at 720P

⚠️ Duration vs Account Plan: MiniMax-Hailuo-2.3 supports 6s or 10s, but some accounts only support 6s. If you encounter "token plan not support model, MiniMax-Hailuo-2.3-10s-768p" error, switch to --duration 6. Always check user's plan limits before attempting 10s video generation.

IMPORTANT: Prompt Optimization (MUST follow before generating any video)

Before calling any video generation script, you MUST optimize the user's prompt by reading and applying references/video-prompt-guide.md. Never pass the user's raw description directly as --prompt.

Optimization steps:

Apply the Professional Formula: Main subject + Scene + Movement + Camera motion + Aesthetic atmosphere

BAD: "A puppy in a park"
GOOD: "A golden retriever puppy runs toward the camera on a sun-dappled grass path in a park, [跟随] smooth tracking shot, warm golden hour lighting, shallow depth of field, joyful atmosphere"

Add camera instructions using [指令] syntax: [推进], [拉远], [跟随], [固定], [左摇], etc.

Include aesthetic details: lighting (golden hour, dramatic side lighting), color grading (warm tones, cinematic), texture (dust particles, rain droplets), atmosphere (intimate, epic, peaceful)

Keep to 1-2 key actions for 6-10 second videos — do not overcrowd with events

For i2v mode (image-to-video): Focus prompt on movement and change only, since the image already establishes the visual. Do NOT re-describe what's in the image.

BAD: "A lake with mountains" (just repeating the image)
GOOD: "Gentle ripples spread across the water surface, a breeze rustles the distant trees, [固定] fixed camera, soft morning light, peaceful and serene"

For multi-segment long videos: Each segment's prompt must be self-contained and optimized individually. The i2v segments (segment 2+) should describe motion/change relative to the previous segment's ending frame.

# Text-to-video (default: 6s, 768P)
bash scripts/video/generate_video.sh \
  --mode t2v \
  --prompt "A golden retriever puppy bounds toward the camera on a sunlit grass path, [跟随] tracking shot, warm golden hour, shallow depth of field, joyful" \
  --output minimax-output/puppy.mp4
message action=send media=minimax-output/puppy.mp4

# Image-to-video (prompt focuses on MOTION, not image content)
bash scripts/video/generate_video.sh \
  --mode i2v \
  --prompt "The petals begin to sway gently in the breeze, soft light shifts across the surface, [固定] fixed framing, dreamy pastel tones" \
  --first-frame photo.jpg \
  --output minimax-output/animated.mp4
message action=send media=minimax-output/animated.mp4

# Start-end frame interpolation (sef mode uses MiniMax-Hailuo-02)
bash scripts/video/generate_video.sh \
  --mode sef \
  --first-frame start.jpg --last-frame end.jpg \
  --output minimax-output/transition.mp4
message action=send media=minimax-output/transition.mp4

# Subject reference (face consistency, ref mode uses S2V-01, 6s only)
bash scripts/video/generate_video.sh \
  --mode ref \
  --prompt "A young woman in a white dress walks slowly through a sunlit garden, [跟随] smooth tracking, warm natural lighting, cinematic depth of field" \
  --subject-image face.jpg \
  --duration 6 \
  --output minimax-output/person.mp4
message action=send media=minimax-output/person.mp4

Long-form Video (Multi-scene)

Multi-scene long videos chain segments together: the first segment generates via text-to-video (t2v), then each subsequent segment uses the last frame of the previous segment as its first frame (i2v). Segments are joined with crossfade transitions for smooth continuity. Default is 6 seconds per segment.

Workflow:

Segment 1: t2v — generated purely from the optimized text prompt
Segment 2+: i2v — the previous segment's last frame becomes first_frame_image, prompt describes motion and change from that ending state
All segments are concatenated with 0.5s crossfade transitions to eliminate jump cuts
Optional: AI-generated background music is overlaid

Prompt rules for each segment:

Each segment prompt MUST be independently optimized using the Professional Formula
Segment 1 (t2v): Full scene description with subject, scene, camera, atmosphere
Segment 2+ (i2v): Focus on what changes and moves from the previous ending frame. Do NOT repeat the visual description — the first frame already provides it
Maintain visual consistency: keep lighting, color grading, and style keywords consistent across segments
Each segment covers only 6 seconds of action — keep it focused
# Example: 3-segment story with optimized per-segment prompts (default: 6s/segment, 768P)
bash scripts/video/generate_long_video.sh \
  --scenes \
    "A lone astronaut stands on a red desert planet surface, wind blowing dust particles, [推进] slow push in toward the visor, dramatic rim lighting, cinematic sci-fi atmosphere" \
    "The astronaut turns and begins walking toward a distant glowing structure on the horizon, dust swirling around boots, [跟随] tracking from behind, vast desolate landscape, golden light from the structure" \
    "The astronaut reaches the structure entrance, a massive doorway pulses with blue energy, [推进] slow push in toward the doorway, light reflects off the visor, awe-inspiring epic scale" \
  --music-prompt "cinematic orchestral ambient, slow build, sci-fi atmosphere" \
  --output minimax-output/long_video.mp4
message action=send media=minimax-output/long_video.mp4

# With custom settings
bash scripts/video/generate_long_video.sh \
  --scenes "Scene 1 prompt" "Scene 2 prompt" \
  --segment-duration 6 \
  --resolution 768P \
  --crossfade 0.5 \
  --music-prompt "calm ambient background music" \
  --output minimax-output/long_video.mp4
message action=send media=minimax-output/long_video.mp4

Add Background Music
bash scripts/video/add_bgm.sh \
  --video input.mp4 \
  --generate-bgm --instrumental \
  --music-prompt "soft piano background" \
  --bgm-volume 0.3 \
  --output minimax-output/output_with_bgm.mp4

Template Video
bash scripts/video/generate_template_video.sh \
  --template-id 392753057216684038 \
  --media photo.jpg \
  --output minimax-output/template_output.mp4

Video Models
Mode	Default Model	Default Duration	Default Resolution	Notes
t2v	MiniMax-Hailuo-2.3	6s	768P	Latest text-to-video
i2v	MiniMax-Hailuo-2.3	6s	768P	Latest image-to-video
sef	MiniMax-Hailuo-02	6s	768P	Start-end frame
ref	S2V-01	6s	720P	Subject reference, 6s only
Media Tools (Audio/Video Processing)

Entry point: scripts/media_tools.sh

Standalone FFmpeg-based utilities for format conversion, concatenation, extraction, trimming, and audio overlay. Use these when the user needs to process existing media files without generating new content via MiniMax API.

Video Format Conversion
# Convert between formats (mp4, mov, webm, mkv, avi, ts, flv)
bash scripts/media_tools.sh convert-video input.webm -o output.mp4
bash scripts/media_tools.sh convert-video input.mp4 -o output.mov

# With quality / resolution / fps options
bash scripts/media_tools.sh convert-video input.mp4 -o output.mp4 \
  --crf 18 --preset medium --resolution 1920x1080 --fps 30

Audio Format Conversion
# Convert between formats (mp3, wav, flac, ogg, aac, m4a, opus, wma)
bash scripts/media_tools.sh convert-audio input.wav -o output.mp3
bash scripts/media_tools.sh convert-audio input.mp3 -o output.flac \
  --bitrate 320k --sample-rate 48000 --channels 2

Video Concatenation
# Concatenate with crossfade transition (default 0.5s)
bash scripts/media_tools.sh concat-video seg1.mp4 seg2.mp4 seg3.mp4 -o merged.mp4

# Hard cut (no crossfade)
bash scripts/media_tools.sh concat-video seg1.mp4 seg2.mp4 -o merged.mp4 --crossfade 0

Audio Concatenation
# Simple concatenation
bash scripts/media_tools.sh concat-audio part1.mp3 part2.mp3 -o combined.mp3

# With crossfade
bash scripts/media_tools.sh concat-audio part1.mp3 part2.mp3 -o combined.mp3 --crossfade 1

Extract Audio from Video
# Extract as mp3
bash scripts/media_tools.sh extract-audio video.mp4 -o audio.mp3

# Extract as wav with higher bitrate
bash scripts/media_tools.sh extract-audio video.mp4 -o audio.wav --bitrate 320k

Video Trimming
# Trim by start/end time (seconds)
bash scripts/media_tools.sh trim-video input.mp4 -o clip.mp4 --start 5 --end 15

# Trim by start + duration
bash scripts/media_tools.sh trim-video input.mp4 -o clip.mp4 --start 10 --duration 8

Add Audio to Video (Overlay / Replace)
# Mix audio with existing video audio
bash scripts/media_tools.sh add-audio --video video.mp4 --audio bgm.mp3 -o output.mp4 \
  --volume 0.3 --fade-in 2 --fade-out 3

# Replace original audio entirely
bash scripts/media_tools.sh add-audio --video video.mp4 --audio narration.mp3 -o output.mp4 \
  --replace

Media File Info
bash scripts/media_tools.sh probe input.mp4

Script Architecture
scripts/
├── check_environment.sh         # Env verification (curl, ffmpeg, jq, xxd, API key)
├── media_tools.sh               # Audio/video conversion, concat, trim, extract
├── tts/
│   └── generate_voice.sh        # Unified TTS CLI (tts, clone, design, list-voices, generate, merge, convert)
├── music/
│   └── generate_music.sh        # Music generation CLI
├── image/
│   └── generate_image.sh        # Image generation CLI (2 modes: t2i, i2i)
└── video/
    ├── generate_video.sh        # Video generation CLI (4 modes: t2v, i2v, sef, ref)
    ├── generate_long_video.sh   # Multi-scene long video
    ├── generate_template_video.sh # Template-based video
    └── add_bgm.sh              # Background music overlay

References

Read these for detailed API parameters, voice catalogs, and prompt engineering:

tts-guide.md — TTS setup, voice management, audio processing, segment format, troubleshooting
tts-voice-catalog.md — Full voice catalog with IDs, descriptions, and parameter reference
music-api.md — Music generation API: endpoints, parameters, response format
image-api.md — Image generation API: text-to-image, image-to-image, parameters
video-api.md — Video API: endpoints, models, parameters, camera instructions, templates
video-prompt-guide.md — Video prompt engineering: formulas, styles, image-to-video tips
Weekly Installs
631
Repository
minimax-ai/skills
GitHub Stars
11.5K
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail