---
title: aliyun-wan-r2v
url: https://skills.sh/cinience/alicloud-skills/aliyun-wan-r2v
---

# aliyun-wan-r2v

skills/cinience/alicloud-skills/aliyun-wan-r2v
aliyun-wan-r2v
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill aliyun-wan-r2v
SKILL.md

Category: provider

Model Studio Wan R2V
Validation
mkdir -p output/aliyun-wan-r2v
python -m py_compile skills/ai/video/aliyun-wan-r2v/scripts/prepare_r2v_request.py && echo "py_compile_ok" > output/aliyun-wan-r2v/validate.txt


Pass criteria: command exits 0 and output/aliyun-wan-r2v/validate.txt is generated.

Output And Evidence
Save reference input metadata, request payloads, and task outputs in output/aliyun-wan-r2v/.
Keep at least one polling result snapshot.

Use Wan R2V for reference-to-video generation. This is different from i2v (single image to video).

Critical model names

Use one of these exact model strings:

wan2.6-r2v-flash
wan2.6-r2v

Newer official releases may prefer the flash variant for lower latency and lower cost.

Prerequisites
Install SDK in a virtual environment:
python3 -m venv .venv
. .venv/bin/activate
python -m pip install dashscope

Set DASHSCOPE_API_KEY in your environment, or add dashscope_api_key to ~/.alibabacloud/credentials.
Normalized interface (video.generate_reference)
Request
prompt (string, required)
reference_video (string | bytes, required)
reference_image (string | bytes, optional)
duration (number, optional)
fps (number, optional)
size (string, optional)
seed (int, optional)
Response
video_url (string)
task_id (string, when async)
request_id (string)
Async handling
Prefer async submission for production traffic.
Poll task result with 15-20s intervals.
Stop polling when SUCCEEDED or terminal failure status is returned.
Local helper script

Prepare a normalized request JSON and validate response schema:

.venv/bin/python skills/ai/video/aliyun-wan-r2v/scripts/prepare_r2v_request.py \
  --prompt "Generate a short montage with consistent character style" \
  --reference-video "https://example.com/reference.mp4"

Output location
Default output: output/aliyun-wan-r2v/videos/
Override base dir with OUTPUT_DIR.
Workflow
Confirm user intent, region, identifiers, and whether the operation is read-only or mutating.
Run one minimal read-only query first to verify connectivity and permissions.
Execute the target operation with explicit parameters and bounded scope.
Verify results and save output/evidence files.
References
references/sources.md
Weekly Installs
35
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass