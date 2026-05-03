---
title: giggle-generation-aimv
url: https://skills.sh/giggle-official/skills/giggle-generation-aimv
---

# giggle-generation-aimv

skills/giggle-official/skills/giggle-generation-aimv
giggle-generation-aimv
Installation
$ npx skills add https://github.com/giggle-official/skills --skill giggle-generation-aimv
SKILL.md
MV Trustee Mode API Skill

Calls the MV trustee mode API to run the full MV generation workflow. Project creation and task submission are merged into one step in the script—call execute_workflow once only; never call create and submit separately.

⚠️ Review Before Installing

Please review before installing. This skill will:

Network – Calls Giggle.pro API for MV generation

Requirements: python3 (>=3.6), GIGGLE_API_KEY (system environment variable), pip packages: requests

No Retry on Error: If script execution encounters an error, do not retry. Report the error to the user directly and stop.

Required Setup Before First Use

Before performing any operation, confirm the user has configured the API Key.

API Key: Log in to giggle.pro. On the main site, use the left sidebar → API Key (API 密钥) section to create or copy your key.

Configuration: Set system environment variable GIGGLE_API_KEY

export GIGGLE_API_KEY=your_api_key

Verification steps:

Confirm the user has configured GIGGLE_API_KEY in system environment
If not configured, guide the user:

Open giggle.pro while logged in → left sidebar → API Key / API 密钥 → copy your key, then run export GIGGLE_API_KEY=your_api_key in the terminal.

Wait for the user to configure before continuing the workflow
Two Music Generation Modes
Mode	music_generate_type	Required params	Description
Prompt	prompt	prompt, vocal_gender	Describe music in text
Custom	custom	lyrics, style, title	Provide lyrics, style, and title
Shared Parameters (All Modes, Required)
reference_image or reference_image_url: Reference image—provide at least one (asset_id or download URL). Also supports base64 image, e.g. "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==". For base64: pass the raw Base64 string directly; do not add the data:image/xxx;base64 prefix.
aspect: Aspect ratio, 16:9 or 9:16
scene_description: Visual scene description, default empty—only set when the user explicitly mentions the scene (max 200 chars)
subtitle_enabled: Enable subtitles, default false
Mode-Specific Parameters

Prompt mode:

prompt: Music description (required)
vocal_gender: Vocal gender — male / female / auto (optional, default auto)
instrumental: Instrumental only (optional, default false)

Custom mode:

lyrics: Lyrics content (required)
style: Music style (required)
title: Song title (required)
Workflow Function

Use execute_workflow to run the full workflow—call once and wait. Internally: create project + submit task (merged) → poll progress (every 3 sec) → detect and pay pending items → wait for completion (max 1 hour).

Continuous progress updates (blocking MV workflow)

execute_workflow blocks for the full MV pipeline: create/submit (merged), poll (~every 3s), pay if needed, up to ~1 hour. You do not run shell --query yourself.

Before the call, tell the user the MV job is running, that it usually takes minutes and can approach ~1 hour, and you will report when the function returns.
Invoke execute_workflow without waiting for the user to ask for a status check first.
After return, forward the full signed download_url / video_asset on success or the error payload in plain language; include project_id when useful for support or manual pay/query.
create_and_submit only: if they only want ids up front, use that path and query later when they ask.

Important:

Never call create_project and submit_mv_task separately—always use execute_workflow or create_and_submit
After calling, just wait for the function to return; all intermediate steps are automatic
Function Signature
execute_workflow(
    music_generate_type: str,      # Mode: prompt / custom
    aspect: str,                    # Aspect ratio: 16:9 or 9:16
    project_name: str,              # Project name
    reference_image: str = "",      # Reference image asset_id (mutually exclusive with reference_image_url)
    reference_image_url: str = "",  # Reference image URL or base64 (mutually exclusive with reference_image)
    scene_description: str = "",    # Scene description, default empty
    subtitle_enabled: bool = False, # Subtitle toggle, default False
    # Prompt mode
    prompt: str = "",
    vocal_gender: str = "auto",
    instrumental: bool = False,
    # Custom mode
    lyrics: str = "",
    style: str = "",
    title: str = "",
)

Parameter Extraction Rules
reference_image and reference_image_url: At least one required. Use reference_image for asset_id; use reference_image_url for image URL or base64.
scene_description: Default empty—only fill when the user explicitly mentions "scene", "visual description", or "visual style".
subtitle_enabled: Default False—only set True when the user explicitly requests subtitles.
aspect: Use 9:16 when the user mentions portrait/vertical/9:16; otherwise default 16:9.
Mode selection: "Describe music / use prompt" → prompt; "Here are my lyrics / lyrics are" → custom;
Examples

Prompt mode:

api = MVTrusteeAPI()
result = api.execute_workflow(
    music_generate_type="prompt",
    aspect="16:9",
    project_name="My MV",
    reference_image_url="https://example.com/ref.jpg",
    prompt="Upbeat pop, sunny beach vibe",
    vocal_gender="female"
)


Custom mode (user provides lyrics):

result = api.execute_workflow(
    music_generate_type="custom",
    aspect="9:16",
    project_name="Lyrics MV",
    reference_image="asset_xxx",
    lyrics="Verse 1: Spring breeze on my face...",
    style="pop",
    title="Spring Song"
)


With scene description (when user explicitly describes the scene):

result = api.execute_workflow(
    music_generate_type="prompt",
    aspect="16:9",
    project_name="Scene MV",
    reference_image_url="https://...",
    prompt="Electronic dance music",
    scene_description="City nightscape, neon lights, flowing traffic"
)

Submit Task API Request Example (Prompt Mode)

Submit endpoint (/api/v1/trustee_mode/mv/submit) request body:

{
  "project_id": "<your-project-id>",
  "music_generate_type": "prompt",
  "prompt": "A cheerful pop song",
  "vocal_gender": "female",
  "instrumental": false,
  "reference_image_url": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUT...(base64 image data)",
  "scene_description": "A romantic beach walk at sunset, waves gently lapping the shore, pink sky gradient",
  "aspect": "16:9",
  "subtitle_enabled": false
}


Note: reference_image (asset_id) and reference_image_url (URL or base64) are mutually exclusive.

Custom mode:

{
  "project_id": "<your-project-id>",
  "music_generate_type": "custom",
  "lyrics": "Verse 1:\nStanding by the sea watching the sunset\nMemories rush in like waves\n\nChorus:\nLet the sea breeze blow away all worries\nIn this golden moment\nWe found each other\n",
  "style": "pop ballad",
  "title": "Seaside Memories",
  "reference_image": "<asset_id>",
  "scene_description": "A couple walking on the beach at dusk, long shadows, orange-red sky gradient",
  "aspect": "9:16",
  "subtitle_enabled": false
}

Query Progress API Response Example

Query endpoint (/api/v1/trustee_mode/mv/query) response (all steps completed):

{
  "code": 200,
  "msg": "success",
  "uuid": "<response-uuid>",
  "data": {
    "project_id": "<your-project-id>",
    "video_asset": {
      "asset_id": "<asset_id>",
      "download_url": "https://assets.giggle.pro/private/...",
      "thumbnail_url": "https://assets.giggle.pro/private/...",
      "signed_url": "https://assets.giggle.pro/private/...",
      "duration": 0
    },
    "shot_count": 0,
    "current_step": "editor",
    "completed_steps": "music-generate,storyboard,shot,editor",
    "pay_status": "paid",
    "status": "completed",
    "err_msg": "",
    "steps": [...]
  }
}


Note: When pay_status is pending, call the pay endpoint. When all steps are done, video_asset.download_url will have a value—return the full signed URL. Correct format:

https://assets.giggle.pro/private/ai_director/348e4956c7bd4f763b/qzjc7gwkpf.mp4?Policy=...&Key-Pair-Id=...&Signature=...&response-content-disposition=attachment


Do not strip response-content-disposition=attachment or other query params from the URL. Wrong (unsigned URL only):

https://assets.giggle.pro/private/ai_director/348e4956c7bd4f763b/qzjc7gwkpf.mp4

Pay API Request and Response

Pay endpoint (/api/v1/trustee_mode/mv/pay):

Request body:

{
  "project_id": "<your-project-id>"
}


Response:

{
  "code": 200,
  "msg": "success",
  "uuid": "<response-uuid>",
  "data": {
    "order_id": "<order-id>",
    "price": 580
  }
}

Retry API Request Example

When a step fails, guide the user to call the retry endpoint to resume from that step:

{
  "project_id": "<your-project-id>",
  "current_step": "shot"
}


Note: current_step is the step name to retry (e.g. music-generate, storyboard, shot, editor).

create_and_submit (Optional)

If you only need to create the project and submit the task without waiting for completion, use create_and_submit. Never call create_project and submit_mv_task separately:

api = MVTrusteeAPI()
r = api.create_and_submit(
    project_name="My MV",
    music_generate_type="prompt",
    aspect="16:9",
    reference_image_url="https://...",
    prompt="Upbeat pop"
)
# Returns project_id for manual query/pay later

Return Value

Success:

{
    "code": 200,
    "msg": "success",
    "data": {
        "project_id": "...",
        "download_url": "https://...",
        "video_asset": {...},
        "status": "completed"
    }
}


Returns error message on failure.

Troubleshooting
Scenario	Cause	Solution
401 Unauthorized or "invalid API key"	GIGGLE_API_KEY is missing, expired, or incorrect	Re-copy the key from giggle.pro → left sidebar → API Key / API 密钥, then re-export: export GIGGLE_API_KEY=your_api_key
429 Too Many Requests	API rate limit exceeded	Wait a few minutes and retry; avoid submitting multiple projects in rapid succession
Network timeout / connection error	Unstable network or API service temporarily unavailable	The script auto-retries up to 5 times with 5-second intervals; check your network if it still fails
pay_status: pending	The project requires payment before proceeding	The workflow function handles this automatically; if running manually, call the pay endpoint with the project_id
Task step failed (status: failed)	A generation step (e.g. music-generate, shot) encountered an error	Use the retry endpoint: {"project_id": "<your-project-id>", "current_step": "<failed-step>"} to resume from the failed step
Workflow timeout (> 1 hour)	MV generation took too long	Query progress manually with the project_id to check current status; contact support if the task is stuck
Weekly Installs
59
Repository
giggle-official/skills
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn