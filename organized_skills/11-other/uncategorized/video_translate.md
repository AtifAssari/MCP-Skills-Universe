---
rating: ⭐⭐
title: video-translate
url: https://skills.sh/heygen-com/skills/video-translate
---

# video-translate

skills/heygen-com/skills/video-translate
video-translate
Installation
$ npx skills add https://github.com/heygen-com/skills --skill video-translate
Summary

Translate and dub videos into multiple languages with automatic lip-sync using HeyGen.

Supports 12+ languages including Spanish, French, German, Japanese, Chinese, and Arabic with automatic voice cloning to match original speaker characteristics
Offers two translation modes: full lip-sync dubbing or faster audio-only translation without video adjustments
Handles multi-speaker videos, custom vocabulary preservation, and optional background music removal or speech enhancement
Includes polling-based status tracking with up to 30-minute processing time; supports batch translation to multiple languages in parallel
SKILL.md
Video Translation (HeyGen)

Translate and dub existing videos into multiple languages, preserving lip-sync and natural speech patterns. Provide a video URL or HeyGen video ID — no need to create the video on HeyGen first.

Authentication

All requests require the X-Api-Key header. Set the HEYGEN_API_KEY environment variable.

curl -X POST "https://api.heygen.com/v2/video_translate" \
  -H "X-Api-Key: $HEYGEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video_url": "https://example.com/video.mp4", "output_language": "es-ES"}'

Default Workflow
Provide a video URL or HeyGen video ID
Call POST /v2/video_translate with the target language
Poll GET /v2/video_translate/{translate_id} until status is completed
Download the translated video from the returned URL
Creating a Translation Job
Request Fields
Field	Type	Req	Description
video_url	string	Y*	URL of video to translate (*or video_id)
video_id	string	Y*	HeyGen video ID (*or video_url)
output_language	string	Y	Target language code (e.g., "es-ES")
title	string		Name for the translated video
translate_audio_only	boolean		Audio only, no lip-sync (faster)
speaker_num	number		Number of speakers in video
callback_id	string		Custom ID for webhook tracking
callback_url	string		URL for completion notification

Either video_url or video_id must be provided.

curl
curl -X POST "https://api.heygen.com/v2/video_translate" \
  -H "X-Api-Key: $HEYGEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "video_url": "https://example.com/original-video.mp4",
    "output_language": "es-ES",
    "title": "Spanish Version"
  }'

TypeScript
interface VideoTranslateRequest {
  video_url?: string;
  video_id?: string;
  output_language: string;
  title?: string;
  translate_audio_only?: boolean;
  speaker_num?: number;
  callback_id?: string;
  callback_url?: string;
}

interface VideoTranslateResponse {
  error: null | string;
  data: {
    video_translate_id: string;
  };
}

async function translateVideo(config: VideoTranslateRequest): Promise<string> {
  const response = await fetch("https://api.heygen.com/v2/video_translate", {
    method: "POST",
    headers: {
      "X-Api-Key": process.env.HEYGEN_API_KEY!,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(config),
  });

  const json: VideoTranslateResponse = await response.json();

  if (json.error) {
    throw new Error(json.error);
  }

  return json.data.video_translate_id;
}

Python
import requests
import os

def translate_video(config: dict) -> str:
    response = requests.post(
        "https://api.heygen.com/v2/video_translate",
        headers={
            "X-Api-Key": os.environ["HEYGEN_API_KEY"],
            "Content-Type": "application/json"
        },
        json=config
    )

    data = response.json()
    if data.get("error"):
        raise Exception(data["error"])

    return data["data"]["video_translate_id"]

Supported Languages
Language	Code	Notes
English (US)	en-US	Default source
Spanish (Spain)	es-ES	European Spanish
Spanish (Mexico)	es-MX	Latin American
French	fr-FR	Standard French
German	de-DE	Standard German
Italian	it-IT	Standard Italian
Portuguese (Brazil)	pt-BR	Brazilian Portuguese
Japanese	ja-JP	Standard Japanese
Korean	ko-KR	Standard Korean
Chinese (Mandarin)	zh-CN	Simplified Chinese
Hindi	hi-IN	Standard Hindi
Arabic	ar-SA	Modern Standard Arabic
Translation Options
Basic Translation (with lip-sync)
const config = {
  video_url: "https://example.com/original.mp4",
  output_language: "es-ES",
  title: "Spanish Translation",
};

Audio-Only Translation (faster, no lip-sync)
const config = {
  video_url: "https://example.com/original.mp4",
  output_language: "es-ES",
  translate_audio_only: true,
};

Multi-Speaker Videos
const config = {
  video_url: "https://example.com/interview.mp4",
  output_language: "fr-FR",
  speaker_num: 2,
};

Advanced Options (v4 API)

For more control over translation:

interface VideoTranslateV4Request {
  input_video_id?: string;
  google_url?: string;
  output_languages: string[];        // Multiple languages in one call
  name: string;
  srt_key?: string;                  // Custom SRT subtitles
  instruction?: string;
  vocabulary?: string[];             // Terms to preserve as-is
  brand_voice_id?: string;
  speaker_num?: number;
  keep_the_same_format?: boolean;
  input_language?: string;
  enable_video_stretching?: boolean;
  disable_music_track?: boolean;
  enable_speech_enhancement?: boolean;
  srt_role?: "input" | "output";
  translate_audio_only?: boolean;
}

Multiple Output Languages
const config = {
  input_video_id: "original_video_id",
  output_languages: ["es-ES", "fr-FR", "de-DE"],
  name: "Multi-language translations",
};

Custom Vocabulary (preserve specific terms)
const config = {
  video_url: "https://example.com/product-demo.mp4",
  output_language: "ja-JP",
  vocabulary: ["SuperWidget", "Pro Max", "TechCorp"],
};

Custom SRT Subtitles
const config = {
  video_url: "https://example.com/video.mp4",
  output_language: "es-ES",
  srt_key: "path/to/custom-subtitles.srt",
  srt_role: "input",
};

Checking Translation Status
curl
curl -X GET "https://api.heygen.com/v2/video_translate/{translate_id}" \
  -H "X-Api-Key: $HEYGEN_API_KEY"

TypeScript
interface TranslateStatusResponse {
  error: null | string;
  data: {
    id: string;
    status: "pending" | "processing" | "completed" | "failed";
    video_url?: string;
    message?: string;
  };
}

async function getTranslateStatus(translateId: string): Promise<TranslateStatusResponse["data"]> {
  const response = await fetch(
    `https://api.heygen.com/v2/video_translate/${translateId}`,
    { headers: { "X-Api-Key": process.env.HEYGEN_API_KEY! } }
  );

  const json: TranslateStatusResponse = await response.json();

  if (json.error) {
    throw new Error(json.error);
  }

  return json.data;
}

Polling for Completion

Translations take longer than standard video generation — allow up to 30 minutes.

async function waitForTranslation(
  translateId: string,
  maxWaitMs = 1800000,
  pollIntervalMs = 30000
): Promise<string> {
  const startTime = Date.now();

  while (Date.now() - startTime < maxWaitMs) {
    const status = await getTranslateStatus(translateId);

    switch (status.status) {
      case "completed":
        return status.video_url!;
      case "failed":
        throw new Error(status.message || "Translation failed");
      default:
        console.log(`Status: ${status.status}...`);
        await new Promise((r) => setTimeout(r, pollIntervalMs));
    }
  }

  throw new Error("Translation timed out");
}

Complete Workflow
async function translateAndDownload(
  videoUrl: string,
  targetLanguage: string
): Promise<string> {
  console.log(`Starting translation to ${targetLanguage}...`);
  const translateId = await translateVideo({
    video_url: videoUrl,
    output_language: targetLanguage,
  });
  console.log(`Translation ID: ${translateId}`);

  console.log("Processing translation...");
  const translatedVideoUrl = await waitForTranslation(translateId);
  console.log(`Translation complete: ${translatedVideoUrl}`);

  return translatedVideoUrl;
}

const spanishVideo = await translateAndDownload(
  "https://example.com/my-video.mp4",
  "es-ES"
);

Batch Translation

Translate to multiple languages in parallel:

async function translateToMultipleLanguages(
  sourceVideoUrl: string,
  targetLanguages: string[]
): Promise<Record<string, string>> {
  const results: Record<string, string> = {};

  const translatePromises = targetLanguages.map(async (lang) => {
    const translateId = await translateVideo({
      video_url: sourceVideoUrl,
      output_language: lang,
    });
    return { lang, translateId };
  });

  const translationJobs = await Promise.all(translatePromises);

  for (const job of translationJobs) {
    try {
      const videoUrl = await waitForTranslation(job.translateId);
      results[job.lang] = videoUrl;
    } catch (error) {
      results[job.lang] = `error: ${error.message}`;
    }
  }

  return results;
}

const translations = await translateToMultipleLanguages(
  "https://example.com/original.mp4",
  ["es-ES", "fr-FR", "de-DE", "ja-JP"]
);

Features
Lip Sync — Automatically adjusts speaker's lip movements to match translated audio
Voice Cloning — Translated audio matches the original speaker's voice characteristics
Music Track Control — Optionally remove background music with disable_music_track: true
Speech Enhancement — Improve audio quality with enable_speech_enhancement: true
Best Practices
Source quality matters — Use high-quality source videos for better results
Clear audio — Videos with clear speech translate better
Single speaker — Best results with single-speaker content
Moderate pacing — Very fast speech may affect quality
Test first — Try with shorter clips before translating long videos
Allow extra time — Translation takes longer than video generation (up to 30 min)
Error Handling

Common errors and how to handle them:

async function safeTranslate(
  videoUrl: string,
  targetLanguage: string
): Promise<{ success: boolean; result?: string; error?: string }> {
  try {
    const url = await translateAndDownload(videoUrl, targetLanguage);
    return { success: true, result: url };
  } catch (error) {
    if (error.message.includes("quota")) {
      return { success: false, error: "Insufficient credits" };
    }
    if (error.message.includes("duration")) {
      return { success: false, error: "Video too long" };
    }
    if (error.message.includes("format")) {
      return { success: false, error: "Unsupported video format" };
    }
    return { success: false, error: error.message };
  }
}

Weekly Installs
1.2K
Repository
heygen-com/skills
GitHub Stars
202
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn