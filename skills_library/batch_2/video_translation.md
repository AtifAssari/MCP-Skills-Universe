---
title: video-translation
url: https://skills.sh/noizai/skills/video-translation
---

# video-translation

skills/noizai/skills/video-translation
video-translation
Installation
$ npx skills add https://github.com/noizai/skills --skill video-translation
Summary

Translate video speech into another language with AI-generated dubbing that preserves original timing and emotion.

Downloads videos and subtitles, translates subtitle text, then generates dubbed audio using TTS with voice cloning matched to the original speaker's tone
Automatically aligns dubbed audio duration to original subtitle timestamps and preserves background audio outside speech segments
Requires youtube-downloader and tts skills as dependencies, plus ffmpeg and a Noiz API key for the TTS backend
Works with any video platform that provides subtitles; source language auto-detection supported but long videos may require significant processing time
SKILL.md
Video Translation

Translate a video's speech into another language, using TTS to generate the dubbed audio and replacing the original audio track.

Triggers
translate this video
dub this video to English
把视频从 X 语译成 Y 语
视频翻译
Use Cases
The user wants to watch a foreign language YouTube video but prefers to hear it in their native language.
The user provides a video link and explicitly requests changing the audio language.
Workflow

When the user asks to translate a video:

Download Video & Subtitles: Use the youtube-downloader skill to download the video and its subtitles as SRT. Make sure you specify the source language to fetch the correct subtitle.

python path/to/youtube-downloader/scripts/download_video.py "VIDEO_URL" --subtitles --sub-lang <source_lang_code> -o /tmp/video-translation


Translate Subtitles: Read the downloaded .srt file. Translate its contents sentence by sentence into the target language using the following fixed prompt. Keep the exact same SRT index and timestamp format!

Translation Prompt:

Translate the following subtitle text from to . Provide ONLY the translated text. Do not explain, do not add notes, do not add index numbers. The translation must be colloquial, natural-sounding, and suitable for video dubbing.

Save the translated text into a new file translated.srt.

Generate Dubbed Audio: Use the tts skill to render the timeline-accurate audio from the translated SRT. The Noiz backend automatically aligns the duration of each sentence to the original video's subtitle timestamps.

To ensure the cloned voice matches the original speaker's exact tone and emotion for each sentence, pass the original video file to --ref-audio-track. The TTS engine will automatically slice the original audio at each subtitle's exact timestamp and use it as the reference for that specific segment.

Create a basic voice_map.json:

{
  "default": {
    "target_lang": "<target_lang_code>"
  }
}


Render the timeline-accurate audio:

bash skills/tts/scripts/tts.sh render --srt translated.srt --voice-map voice_map.json --backend noiz --auto-emotion --ref-audio-track original_video.mp4 -o dubbed.wav


Replace Audio in Video: Use the replace_audio.sh script to merge the original video with the new dubbed audio. To keep the original video's non-speech audio background outside of translated segments, pass the --srt file.

bash skills/video-translation/scripts/replace_audio.sh --video original_video.mp4 --audio dubbed.wav --output final_video.mp4 --srt translated.srt


Present the Result: Return the final_video.mp4 file path to the user.

Inputs
Required inputs:
VIDEO_URL: The URL of the video to translate.
target_language: The language to translate the audio to.
Optional inputs:
source_language: The language of the original video (if not auto-detected or specified).
reference_audio: Specific audio file/URL to use for voice cloning instead of the dynamic original video track.
Outputs
Success: Path to the final video file with replaced audio.
Failure: Clear error message specifying whether download, TTS, or audio replacement failed.
Requirements
Dependencies (other skills)
youtube-downloader (crazynomad/skills) — SKILL.md
Install: clone or copy the skills/youtube-downloader directory from crazynomad/skills into your skills/ folder so that skills/youtube-downloader/scripts/download_video.py is available.
tts (NoizAI/skills) — SKILL.md
If not already in this repo: clone or copy the skills/tts directory from NoizAI/skills into your skills/ folder. Ensure skills/tts/scripts/tts.sh and related scripts are present.
NOIZ_API_KEY configured for the Noiz backend. If it is not set, first guide the user to get an API key from https://developers.noiz.ai/api-keys. After the user provides the key, ask whether they want to persist it; if they agree, either write/update NOIZ_API_KEY=... in the project's .env file or run bash skills/tts/scripts/tts.sh config --set-api-key YOUR_KEY to store it.
ffmpeg installed.
Limitations
The source video must have subtitles (or auto-generated subtitles) available on the platform for the source language.
Very long videos may take a significant amount of time to translate and dub.
Weekly Installs
1.7K
Repository
noizai/skills
GitHub Stars
487
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn