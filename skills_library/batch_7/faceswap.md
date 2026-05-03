---
title: faceswap
url: https://skills.sh/heygen-com/skills/faceswap
---

# faceswap

skills/heygen-com/skills/faceswap
faceswap
Installation
$ npx skills add https://github.com/heygen-com/skills --skill faceswap
SKILL.md
Face Swap (HeyGen API)

Swap a face from a source image into a target video using GPU-accelerated AI processing. The source image provides the face to swap in, and the target video receives the new face.

Authentication

All requests require the X-Api-Key header. Set the HEYGEN_API_KEY environment variable.

curl -X POST "https://api.heygen.com/v1/workflows/executions" \
  -H "X-Api-Key: $HEYGEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"workflow_type": "FaceswapNode", "input": {"source_image_url": "https://example.com/face.jpg", "target_video_url": "https://example.com/video.mp4"}}'

Default Workflow
Call POST /v1/workflows/executions with workflow_type: "FaceswapNode", a source face image, and a target video
Receive a execution_id in the response
Poll GET /v1/workflows/executions/{id} every 10 seconds until status is completed
Use the returned video_url from the output
Execute Face Swap
Endpoint

POST https://api.heygen.com/v1/workflows/executions

Request Fields
Field	Type	Req	Description
workflow_type	string	Y	Must be "FaceswapNode"
input.source_image_url	string	Y	URL of the face image to swap in
input.target_video_url	string	Y	URL of the video to apply the face swap to
curl
curl -X POST "https://api.heygen.com/v1/workflows/executions" \
  -H "X-Api-Key: $HEYGEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "workflow_type": "FaceswapNode",
    "input": {
      "source_image_url": "https://example.com/face-photo.jpg",
      "target_video_url": "https://example.com/original-video.mp4"
    }
  }'

TypeScript
interface FaceswapInput {
  source_image_url: string;
  target_video_url: string;
}

interface ExecuteResponse {
  data: {
    execution_id: string;
    status: "submitted";
  };
}

async function faceswap(input: FaceswapInput): Promise<string> {
  const response = await fetch("https://api.heygen.com/v1/workflows/executions", {
    method: "POST",
    headers: {
      "X-Api-Key": process.env.HEYGEN_API_KEY!,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      workflow_type: "FaceswapNode",
      input,
    }),
  });

  const json: ExecuteResponse = await response.json();
  return json.data.execution_id;
}

Python
import requests
import os

def faceswap(source_image_url: str, target_video_url: str) -> str:
    payload = {
        "workflow_type": "FaceswapNode",
        "input": {
            "source_image_url": source_image_url,
            "target_video_url": target_video_url,
        },
    }

    response = requests.post(
        "https://api.heygen.com/v1/workflows/executions",
        headers={
            "X-Api-Key": os.environ["HEYGEN_API_KEY"],
            "Content-Type": "application/json",
        },
        json=payload,
    )

    data = response.json()
    return data["data"]["execution_id"]

Response Format
{
  "data": {
    "execution_id": "node-gw-f1s2w3p4",
    "status": "submitted"
  }
}

Check Status
Endpoint

GET https://api.heygen.com/v1/workflows/executions/{execution_id}

curl
curl -X GET "https://api.heygen.com/v1/workflows/executions/node-gw-f1s2w3p4" \
  -H "X-Api-Key: $HEYGEN_API_KEY"

Response Format (Completed)
{
  "data": {
    "execution_id": "node-gw-f1s2w3p4",
    "status": "completed",
    "output": {
      "video_url": "https://resource.heygen.ai/faceswap/output.mp4"
    }
  }
}

Polling for Completion
async function faceswapAndWait(
  input: FaceswapInput,
  maxWaitMs = 600000,
  pollIntervalMs = 10000
): Promise<string> {
  const executionId = await faceswap(input);
  console.log(`Submitted face swap: ${executionId}`);

  const startTime = Date.now();
  while (Date.now() - startTime < maxWaitMs) {
    const response = await fetch(
      `https://api.heygen.com/v1/workflows/executions/${executionId}`,
      { headers: { "X-Api-Key": process.env.HEYGEN_API_KEY! } }
    );
    const { data } = await response.json();

    switch (data.status) {
      case "completed":
        return data.output.video_url;
      case "failed":
        throw new Error(data.error?.message || "Face swap failed");
      case "not_found":
        throw new Error("Workflow not found");
      default:
        await new Promise((r) => setTimeout(r, pollIntervalMs));
    }
  }

  throw new Error("Face swap timed out");
}

Usage Examples
Basic Face Swap
curl -X POST "https://api.heygen.com/v1/workflows/executions" \
  -H "X-Api-Key: $HEYGEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "workflow_type": "FaceswapNode",
    "input": {
      "source_image_url": "https://example.com/headshot.jpg",
      "target_video_url": "https://example.com/presentation.mp4"
    }
  }'

Chain with Avatar Video

Generate an avatar video first, then swap in a custom face:

import time

# Step 1: Generate avatar video
avatar_execution_id = requests.post(
    "https://api.heygen.com/v1/workflows/executions",
    headers={"X-Api-Key": os.environ["HEYGEN_API_KEY"], "Content-Type": "application/json"},
    json={
        "workflow_type": "AvatarInferenceNode",
        "input": {
            "avatar": {"avatar_id": "Angela-inblackskirt-20220820"},
            "audio_list": [{"audio_url": "https://example.com/speech.mp3"}],
        },
    },
).json()["data"]["execution_id"]

# Step 2: Wait for avatar video to complete
while True:
    status = requests.get(
        f"https://api.heygen.com/v1/workflows/executions/{avatar_execution_id}",
        headers={"X-Api-Key": os.environ["HEYGEN_API_KEY"]},
    ).json()["data"]
    if status["status"] == "completed":
        avatar_video_url = status["output"]["video"]["video_url"]
        break
    time.sleep(10)

# Step 3: Swap in a custom face
faceswap_execution_id = faceswap(
    source_image_url="https://example.com/custom-face.jpg",
    target_video_url=avatar_video_url,
)

Best Practices
Use a clear, front-facing face photo — the source image should show a single face with good lighting
Face swap is GPU-intensive — expect 1-3 minutes processing time, poll every 10 seconds
Source image quality matters — higher resolution face photos produce better results
One face per source image — the source should contain exactly one face to swap in
Works with any video — the target video can be an avatar video, a recording, or any video with visible faces
Chain with other workflows — generate an avatar video first, then swap in a custom face for personalization
Weekly Installs
903
Repository
heygen-com/skills
GitHub Stars
202
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn