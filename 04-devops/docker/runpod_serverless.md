---
rating: ⭐⭐
title: runpod-serverless
url: https://skills.sh/jarmen423/skills/runpod-serverless
---

# runpod-serverless

skills/jarmen423/skills/runpod-serverless
runpod-serverless
Installation
$ npx skills add https://github.com/jarmen423/skills --skill runpod-serverless
SKILL.md
RunPod Serverless Creator

This skill helps you create and configure serverless endpoints on RunPod.io. It handles both the Template creation (software config) and the Endpoint creation (hardware config).

How to Use

The primary tool is the scripts/create_serverless.py script. It is idempotent: if a template or endpoint with the same name exists, it will reuse the template and update the endpoint.

Prerequisites
API Key: You need a RunPod API Key.
Ask the user to provide it or check if RUNPOD_API_KEY is in the environment.
Security: Do not hardcode the key in the script. Pass it via environment variable RUNPOD_API_KEY.
Command
python runpod-serverless/scripts/create_serverless.py \
  --name <NAME> \
  --runtime <python|node> \
  --gpu <GPU_TYPE> \
  [--disk <GB>] \
  [--min-workers <INT>] \
  [--max-workers <INT>]

Arguments
--name (Required): Unique name for the template and endpoint.
--runtime (Required): python or node. Maps to standard RunPod serverless base images.
--gpu (Required): GPU type alias (e.g., 3090, 4090, a100, a6000) or specific ID (e.g., AMPERE_24).
--disk: Container disk size in GB (default: 10).
--min-workers: Minimum active workers (default: 0 for cold-start serverless).
--max-workers: Maximum active workers (default: 1).
GPU Options (Aliases)
3090 -> AMPERE_24 (24GB VRAM)
4090 -> ADA_24 (24GB VRAM)
a4000 -> AMPERE_16 (16GB VRAM)
a6000 -> AMPERE_48 (48GB VRAM)
a100 -> AMPERE_80 (80GB VRAM)

See references/runpod_api.md for full API details and ID mappings.

Example Workflow

Ask User for:

Application Name
Runtime (Python/Node)
Preferred GPU
API Key (if not known)

Run Script:

$env:RUNPOD_API_KEY="<USER_KEY>"; python runpod-serverless/scripts/create_serverless.py --name my-ai-api --runtime python --gpu 3090


Verify: The script outputs the Template ID and Endpoint ID upon success.

Weekly Installs
13
Repository
jarmen423/skills
GitHub Stars
2
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass