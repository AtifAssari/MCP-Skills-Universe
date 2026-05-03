---
rating: ⭐⭐
title: runway
url: https://skills.sh/vm0-ai/vm0-skills/runway
---

# runway

skills/vm0-ai/vm0-skills/runway
runway
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill runway
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name RUNWAY_TOKEN or zero doctor check-connector --url https://api.dev.runwayml.com/v1/organization --method GET

How to Use

All examples below assume you have RUNWAY_TOKEN set.

Base URL: https://api.dev.runwayml.com/v1

Required headers for all requests:

Authorization: Bearer ${RUNWAY_TOKEN}
X-Runway-Version: 2024-11-06
Content-Type: application/json
1. Check Organization Credits

Check your credit balance:

curl -s -X GET "https://api.dev.runwayml.com/v1/organization" --header "Authorization: Bearer $RUNWAY_TOKEN" --header "X-Runway-Version: 2024-11-06"

2. Image to Video

Generate a video from an image:

Write to /tmp/runway_request.json:

{
  "model": "gen4_turbo",
  "promptImage": "https://example.com/your-image.jpg",
  "promptText": "A timelapse of clouds moving across the sky",
  "ratio": "1280:720",
  "duration": 5
}


Then run:

curl -s -X POST "https://api.dev.runwayml.com/v1/image_to_video" --header "Authorization: Bearer $RUNWAY_TOKEN" --header "X-Runway-Version: 2024-11-06" --header "Content-Type: application/json" -d @/tmp/runway_request.json


Response:

{
  "id": "task-id-here"
}

3. Text to Video

Generate a video from text only:

Note: Text-to-video only supports duration values of 4, 6, or 8 seconds (not arbitrary values like image-to-video).

Write to /tmp/runway_request.json:

{
  "model": "veo3.1",
  "promptText": "A serene forest with sunlight filtering through the trees",
  "ratio": "1280:720",
  "duration": 6
}


Then run:

curl -s -X POST "https://api.dev.runwayml.com/v1/text_to_video" --header "Authorization: Bearer $RUNWAY_TOKEN" --header "X-Runway-Version: 2024-11-06" --header "Content-Type: application/json" -d @/tmp/runway_request.json

4. Video to Video

Transform an existing video:

Write to /tmp/runway_request.json:

{
  "model": "gen4_aleph",
  "videoUri": "https://example.com/source-video.mp4",
  "promptText": "Add magical sparkles and fairy dust effects",
  "ratio": "1280:720"
}


Then run:

curl -s -X POST "https://api.dev.runwayml.com/v1/video_to_video" --header "Authorization: Bearer $RUNWAY_TOKEN" --header "X-Runway-Version: 2024-11-06" --header "Content-Type: application/json" -d @/tmp/runway_request.json

5. Text to Image

Generate images from text:

Write to /tmp/runway_request.json:

{
  "model": "gen4_image_turbo",
  "promptText": "A futuristic cityscape at sunset",
  "ratio": "1920:1080",
  "referenceImages": []
}


Then run:

curl -s -X POST "https://api.dev.runwayml.com/v1/text_to_image" --header "Authorization: Bearer $RUNWAY_TOKEN" --header "X-Runway-Version: 2024-11-06" --header "Content-Type: application/json" -d @/tmp/runway_request.json

6. Check Task Status

Poll for task completion. Replace <your-task-id> with the actual task ID:

curl -s -X GET "https://api.dev.runwayml.com/v1/tasks/<your-task-id>" --header "Authorization: Bearer $RUNWAY_TOKEN" --header "X-Runway-Version: 2024-11-06"


Response when complete:

{
  "id": "task-id",
  "status": "SUCCEEDED",
  "output": ["https://cdn.runwayml.com/generated-video.mp4"]
}


Possible statuses: PENDING, RUNNING, SUCCEEDED, FAILED

7. Cancel a Task

Cancel a running task. Replace <your-task-id> with the actual task ID:

curl -s -X DELETE "https://api.dev.runwayml.com/v1/tasks/<your-task-id>" --header "Authorization: Bearer $RUNWAY_TOKEN" --header "X-Runway-Version: 2024-11-06"

8. Video Upscale (4X)

Upscale video resolution:

Write to /tmp/runway_request.json:

{
  "model": "upscale_v1",
  "videoUri": "https://example.com/low-res-video.mp4"
}


Then run:

curl -s -X POST "https://api.dev.runwayml.com/v1/video_upscale" --header "Authorization: Bearer $RUNWAY_TOKEN" --header "X-Runway-Version: 2024-11-06" --header "Content-Type: application/json" -d @/tmp/runway_request.json

9. Generate Sound Effects

Generate audio from text:

Write to /tmp/runway_request.json:

{
  "model": "eleven_text_to_sound_v2",
  "promptText": "Thunder rumbling in the distance"
}


Then run:

curl -s -X POST "https://api.dev.runwayml.com/v1/sound_effect" --header "Authorization: Bearer $RUNWAY_TOKEN" --header "X-Runway-Version: 2024-11-06" --header "Content-Type: application/json" -d @/tmp/runway_request.json

Available Models
Endpoint	Models
Image to Video	gen4_turbo, gen3a_turbo, veo3.1, veo3
Text to Video	veo3.1, veo3.1_fast, veo3
Video to Video	gen4_aleph
Text to Image	gen4_image_turbo, gen4_image
Video Upscale	upscale_v1
Aspect Ratios

Common ratios for video generation:

1280:720 (16:9 landscape)
720:1280 (9:16 portrait)
1024:1024 (1:1 square)
Guidelines
Poll for completion: Video generation is async; poll /tasks/{id} until status is SUCCEEDED
Use appropriate models: gen4_turbo is faster, gen4_aleph for video-to-video
Download promptly: Output URLs may expire after some time
Monitor credits: Check /organization endpoint to track usage
Handle rate limits: API returns 429 when rate limited; add delays
Weekly Installs
89
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass