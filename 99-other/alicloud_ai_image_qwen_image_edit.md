---
rating: ⭐⭐
title: alicloud-ai-image-qwen-image-edit
url: https://skills.sh/cinience/alicloud-skills/alicloud-ai-image-qwen-image-edit
---

# alicloud-ai-image-qwen-image-edit

skills/cinience/alicloud-skills/alicloud-ai-image-qwen-image-edit
alicloud-ai-image-qwen-image-edit
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-ai-image-qwen-image-edit
SKILL.md

Category: provider

Model Studio Qwen Image Edit
Validation
mkdir -p output/alicloud-ai-image-qwen-image-edit
python -m py_compile skills/ai/image/alicloud-ai-image-qwen-image-edit/scripts/prepare_edit_request.py && echo "py_compile_ok" > output/alicloud-ai-image-qwen-image-edit/validate.txt


Pass criteria: command exits 0 and output/alicloud-ai-image-qwen-image-edit/validate.txt is generated.

Output And Evidence
Save edit request payloads, result URLs, and model parameters under output/alicloud-ai-image-qwen-image-edit/.
Keep one sample request/response pair for reproducibility.

Use Qwen Image Edit models for instruction-based image editing instead of text-to-image generation.

Critical model names

Use one of these exact model strings:

qwen-image-edit
qwen-image-edit-plus
qwen-image-edit-max
qwen-image-2.0
qwen-image-2.0-pro
qwen-image-2.0-2026-03-03
qwen-image-2.0-pro-2026-03-03
qwen-image-edit-plus-2025-12-15
qwen-image-edit-max-2026-01-16
Prerequisites
Install SDK in a virtual environment:
python3 -m venv .venv
. .venv/bin/activate
python -m pip install dashscope

Set DASHSCOPE_API_KEY in your environment, or add dashscope_api_key to ~/.alibabacloud/credentials.
Normalized interface (image.edit)
Request
prompt (string, required)
image (string | bytes, required) source image URL/path/bytes
mask (string | bytes, optional) inpaint region mask
size (string, optional) e.g. 1024*1024
seed (int, optional)
Response
image_url (string)
seed (int)
request_id (string)
Operational guidance
Keep prompts task-oriented: describe what to change and what to preserve.
Use masks for deterministic local edits.
Save output assets to object storage and persist only URLs.
For subject consistency, provide explicit constraints in prompt.
Local helper script

Prepare a normalized request JSON and validate response schema:

.venv/bin/python skills/ai/image/alicloud-ai-image-qwen-image-edit/scripts/prepare_edit_request.py \
  --prompt "Replace the sky with sunset, keep buildings unchanged" \
  --image "https://example.com/input.png"

Output location
Default output: output/alicloud-ai-image-qwen-image-edit/images/
Override base dir with OUTPUT_DIR.
Workflow
Confirm user intent, region, identifiers, and whether the operation is read-only or mutating.
Run one minimal read-only query first to verify connectivity and permissions.
Execute the target operation with explicit parameters and bounded scope.
Verify results and save output/evidence files.
References
references/sources.md
Weekly Installs
335
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass