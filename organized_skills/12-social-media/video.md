---
rating: ⭐⭐⭐
title: video
url: https://skills.sh/ibigqiang/feedgrab/video
---

# video

skills/ibigqiang/feedgrab/video
video
Installation
$ npx skills add https://github.com/ibigqiang/feedgrab --skill video
SKILL.md
Video & Podcast Digest Skill

Send a video/podcast link → get full transcript + structured summary

Supported Platforms
Platform	Type	Subtitles	Whisper Transcription
YouTube	Video	✅	✅
Bilibili	Video	✅	✅
X/Twitter	Video	❌	✅
Xiaoyuzhou (小宇宙)	Podcast	❌	✅
Apple Podcasts	Podcast	❌	✅
Direct links (mp3/mp4/m3u8)	Any	❌	✅
Trigger

Auto-triggered when a media URL is detected:

YouTube: youtube.com, youtu.be
Bilibili: bilibili.com, b23.tv
X/Twitter: x.com, twitter.com (tweets with video)
Xiaoyuzhou: xiaoyuzhoufm.com
Apple Podcasts: podcasts.apple.com
Direct: .mp3, .mp4, .m3u8, .m4a, .webm
Pipeline
Step 0: Detect Media Type
URL Pattern	Type	Pipeline
xiaoyuzhoufm.com/episode/	Podcast	→ Step 1b (Xiaoyuzhou)
podcasts.apple.com	Podcast	→ Step 1c (Apple)
bilibili.com, b23.tv	Video	→ Step 1d (Bilibili API)
.mp3, .m4a direct link	Audio	→ Step 2b (direct download)
Other	Video	→ Step 1a (subtitle extraction)
Step 1a: Video — Extract Subtitles
rm -f /tmp/media_sub*.vtt /tmp/media_audio.mp3 /tmp/media_transcript*.json /tmp/media_segment_*.mp3 2>/dev/null || true

# YouTube (prefer English, fallback Chinese)
yt-dlp --skip-download --write-auto-sub --sub-lang "en,zh-Hans" -o "/tmp/media_sub" "VIDEO_URL"

# Bilibili
yt-dlp --skip-download --write-auto-sub --sub-lang "zh-Hans,zh" -o "/tmp/media_sub" "VIDEO_URL"


Check for subtitles:

ls /tmp/media_sub*.vtt 2>/dev/null

Has subtitles → Read VTT content, skip to Step 3
No subtitles → Step 2a (download audio)
Step 1b: Xiaoyuzhou (小宇宙) — Extract Audio URL
AUDIO_URL=$(curl -sL -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" \
  "EPISODE_URL" \
  | grep -oE 'https://media\.xyzcdn\.net/[^"]+\.(m4a|mp3)' \
  | head -1)

echo "Audio URL: $AUDIO_URL"
curl -L -o /tmp/media_audio.mp3 "$AUDIO_URL"


→ Step 2b

Step 1c: Apple Podcasts — via yt-dlp
yt-dlp -f "ba[ext=m4a]/ba/b" --extract-audio --audio-format mp3 --audio-quality 5 \
  -o "/tmp/media_audio.%(ext)s" "APPLE_PODCAST_URL"


→ Step 2b

Step 1d: Bilibili — API Direct Audio Stream
BV="BV1xxxxx"

curl -s "https://api.bilibili.com/x/web-interface/view?bvid=$BV" \
  -H "User-Agent: Mozilla/5.0" -H "Referer: https://www.bilibili.com/" \
  | python3 -c "import json,sys; d=json.load(sys.stdin)['data']; print(f\"Title: {d['title']}\nDuration: {d['duration']}s\nCID: {d['cid']}\")"

CID=<CID from previous step>
AUDIO_URL=$(curl -s "https://api.bilibili.com/x/player/playurl?bvid=$BV&cid=$CID&fnval=16&qn=64" \
  -H "User-Agent: Mozilla/5.0" -H "Referer: https://www.bilibili.com/" \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['data']['dash']['audio'][0]['baseUrl'])")

curl -L -o /tmp/media_audio.m4s \
  -H "User-Agent: Mozilla/5.0" -H "Referer: https://www.bilibili.com/" "$AUDIO_URL"
ffmpeg -y -i /tmp/media_audio.m4s -acodec libmp3lame -q:a 5 /tmp/media_audio.mp3


→ Step 2b

Step 2a: Video — Download Audio (when no subtitles)
yt-dlp --cookies-from-browser chrome -f "ba[ext=m4a]/ba/b" --extract-audio --audio-format mp3 --audio-quality 5 \
  -o "/tmp/media_audio.%(ext)s" "VIDEO_URL"

Step 2b: Check Audio Size & Segment
FILE_SIZE=$(stat -f%z /tmp/media_audio.* 2>/dev/null || stat -c%s /tmp/media_audio.* 2>/dev/null)
echo "File size: $FILE_SIZE bytes"

≤ 25MB → Step 2c (transcribe directly)
> 25MB → Split into 10-minute segments:
DURATION=$(ffprobe -v error -show_entries format=duration -of csv=p=0 /tmp/media_audio.* | head -1)
SEGMENT_SEC=600
SEGMENTS=$(python3 -c "import math; print(math.ceil(float('$DURATION')/$SEGMENT_SEC))")

for i in $(seq 0 $((SEGMENTS-1))); do
  START=$((i * SEGMENT_SEC))
  ffmpeg -y -i /tmp/media_audio.* -ss $START -t $SEGMENT_SEC -acodec libmp3lame -q:a 5 \
    "/tmp/media_segment_${i}.mp3" 2>/dev/null
done


→ Call Step 2c for each segment sequentially (parallel triggers Groq 524 timeout)

Step 2c: Whisper Transcription

Prerequisite: GROQ_API_KEY environment variable

if [ -z "$GROQ_API_KEY" ]; then
  echo "❌ GROQ_API_KEY not set. Get one at: https://console.groq.com/keys"
  exit 1
fi

curl -s -X POST "https://api.groq.com/openai/v1/audio/transcriptions" \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@AUDIO_FILE" \
  -F "model=whisper-large-v3-turbo" \
  -F "response_format=verbose_json" \
  -F "language=zh" \
  > /tmp/media_transcript.json

python3 -c "import json; print(json.load(open('/tmp/media_transcript.json'))['text'])"

Step 3: Structured Summary

Video (≤20 min):

Overview (1-2 sentences)
Key Points (3-5 bullet points)
Notable Quotes (if any)
Action Items (if applicable)

Podcast (>20 min):

Overview (2-3 sentences)
Chapter Summary (segmented by topic)
Key Points (5-8 bullet points)
Notable Quotes
Action Items (if applicable)
Error Handling
Situation	Action
No subtitles + no GROQ_API_KEY	Prompt user to set API key
Audio >25MB	ffmpeg segment (10min/segment), transcribe sequentially
Podcast >2 hours	Warn user, confirm before proceeding
Groq 524 timeout	Do NOT parallelize — transcribe sequentially, sleep 5-8s between
Groq 429 rate limit	Wait for retry-after header, then retry
yt-dlp Bilibili 412	Use Bilibili API instead (Step 1d)
yt-dlp YouTube bot detection	Add --cookies-from-browser chrome
Spotify links	Not supported (DRM protected)
Dependencies
yt-dlp: video download + subtitle extraction
ffmpeg: audio conversion + segmentation
curl: audio download, API calls
GROQ_API_KEY: Whisper transcription (free at https://console.groq.com/keys)
Weekly Installs
40
Repository
ibigqiang/feedgrab
GitHub Stars
332
First Seen
Mar 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykWarn