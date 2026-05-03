---
title: alicloud-ai-multimodal-qwen-vl
url: https://skills.sh/cinience/alicloud-skills/alicloud-ai-multimodal-qwen-vl
---

# alicloud-ai-multimodal-qwen-vl

skills/cinience/alicloud-skills/alicloud-ai-multimodal-qwen-vl
alicloud-ai-multimodal-qwen-vl
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-ai-multimodal-qwen-vl
SKILL.md

Category: provider

Model Studio Qwen VL (Image Understanding)
Validation
mkdir -p output/alicloud-ai-multimodal-qwen-vl
python -m py_compile skills/ai/multimodal/alicloud-ai-multimodal-qwen-vl/scripts/analyze_image.py && echo "py_compile_ok" > output/alicloud-ai-multimodal-qwen-vl/validate.txt


Pass criteria: command exits 0 and output/alicloud-ai-multimodal-qwen-vl/validate.txt is generated.

Output And Evidence
Save raw model responses and normalized extraction results to output/alicloud-ai-multimodal-qwen-vl/.
Include input image reference and prompt for traceability.

Use Qwen VL models for image input + text output understanding tasks via DashScope compatible-mode API.

Prerequisites
Install dependencies (recommended in a venv):
python3 -m venv .venv
. .venv/bin/activate
python -m pip install requests

Set DASHSCOPE_API_KEY in environment, or add dashscope_api_key to ~/.alibabacloud/credentials.
Critical model names

Prefer the Qwen3 VL family:

qwen3-vl-plus
qwen3-vl-flash

When you need explicit "latest" routing or reproducible snapshots, use supported aliases/snapshots from the official model list, such as:

qwen3-vl-plus-latest
qwen3-vl-plus-2025-12-19
qwen3-vl-flash-2026-01-22
qwen3-vl-flash-latest

Legacy names still seen in some workloads:

qwen-vl-max-latest
qwen-vl-plus-latest

For OCR-specialized extraction, prefer skills/ai/multimodal/alicloud-ai-multimodal-qwen-ocr/ instead of using the general VL skill.

Normalized interface (multimodal.chat)
Request
prompt (string, required): user question/instruction about image.
image (string, required): HTTPS URL, local path, or data: URL.
model (string, optional): default qwen3-vl-plus.
max_tokens (int, optional): default 512.
temperature (float, optional): default 0.2.
detail (string, optional): auto/low/high, default auto.
json_mode (bool, optional): return JSON-only response when possible.
schema (object, optional): JSON Schema for structured extraction.
max_retries (int, optional): retry count for 429/5xx, default 2.
retry_backoff_s (float, optional): exponential backoff base seconds, default 1.5.
Response
text (string): primary model answer.
model (string): model actually used.
usage (object): token usage if returned by backend.
Quickstart
python skills/ai/multimodal/alicloud-ai-multimodal-qwen-vl/scripts/analyze_image.py \
  --request '{"prompt":"Summarize the main content in this image","image":"https://example.com/demo.jpg"}' \
  --print-response


Using local image:

python skills/ai/multimodal/alicloud-ai-multimodal-qwen-vl/scripts/analyze_image.py \
  --request '{"prompt":"Extract key information from the image","image":"./samples/invoice.png","model":"qwen3-vl-plus"}' \
  --print-response


Structured extraction (JSON mode):

python skills/ai/multimodal/alicloud-ai-multimodal-qwen-vl/scripts/analyze_image.py \
  --request '{"prompt":"Extract fields: title, amount, date","image":"./samples/invoice.png"}' \
  --json-mode \
  --print-response


Structured extraction (JSON Schema):

python skills/ai/multimodal/alicloud-ai-multimodal-qwen-vl/scripts/analyze_image.py \
  --request '{"prompt":"Extract invoice fields","image":"./samples/invoice.png"}' \
  --schema skills/ai/multimodal/alicloud-ai-multimodal-qwen-vl/references/examples/invoice.schema.json \
  --print-response

cURL (compatible mode)
curl -sS https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model":"qwen3-vl-plus",
    "messages":[
      {
        "role":"user",
        "content":[
          {"type":"image_url","image_url":{"url":"https://example.com/demo.jpg"}},
          {"type":"text","text":"Describe this image and list executable actions"}
        ]
      }
    ],
    "max_tokens":512,
    "temperature":0.2
  }'

Output location
If --output is set, JSON response is saved to that file.
Default output dir convention: output/alicloud-ai-multimodal-qwen-vl/.
Smoke test
python tests/ai/multimodal/alicloud-ai-multimodal-qwen-vl-test/scripts/smoke_test_qwen_vl.py \
  --image ./tmp/vl_test_cat.png

Error handling
Error	Likely cause	Action
401/403	Missing or invalid key	Check DASHSCOPE_API_KEY and account permissions.
400	Invalid request schema or unsupported image source	Validate messages content and image URL/path format.
429	Rate limit	Retry with exponential backoff and lower concurrency.
5xx	Temporary backend issue	Retry with backoff and idempotent request design.
Operational guidance
For stable production behavior, pin snapshot model IDs instead of pure -latest.
Compress very large images before upload to reduce latency and cost.
Add explicit extraction constraints in prompt (fields, JSON shape, language).
For OCR-like output, ask for confidence notes and unresolved text markers.
Workflow
Confirm user intent, region, identifiers, and whether the operation is read-only or mutating.
Run one minimal read-only query first to verify connectivity and permissions.
Execute the target operation with explicit parameters and bounded scope.
Verify results and save output/evidence files.
References
Source list: references/sources.md
API notes: references/api_reference.md
Weekly Installs
337
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn