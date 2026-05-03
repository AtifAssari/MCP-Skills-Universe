---
title: alicloud-ai-multimodal-qwen-omni
url: https://skills.sh/cinience/alicloud-skills/alicloud-ai-multimodal-qwen-omni
---

# alicloud-ai-multimodal-qwen-omni

skills/cinience/alicloud-skills/alicloud-ai-multimodal-qwen-omni
alicloud-ai-multimodal-qwen-omni
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-ai-multimodal-qwen-omni
SKILL.md

Category: provider

Model Studio Qwen Omni
Validation
mkdir -p output/alicloud-ai-multimodal-qwen-omni
python -m py_compile skills/ai/multimodal/alicloud-ai-multimodal-qwen-omni/scripts/prepare_omni_request.py && echo "py_compile_ok" > output/alicloud-ai-multimodal-qwen-omni/validate.txt


Pass criteria: command exits 0 and output/alicloud-ai-multimodal-qwen-omni/validate.txt is generated.

Critical model names

Use one of these exact model strings:

qwen3-omni-flash
qwen3-omni-flash-realtime
qwen-omni-turbo
qwen-omni-turbo-realtime
Typical use
Image + audio + text assistant
Realtime multimodal agents
Spoken responses grounded in visual input
Normalized interface (omni.chat)
Request
model (string, optional): default qwen3-omni-flash
text (string, optional)
image (string, optional)
audio (string, optional)
response_modalities (array, optional): e.g. ["text"], ["text","audio"]
Response
text (string, optional)
audio_url or audio_chunk (optional)
usage (object, optional)
Quick start
python skills/ai/multimodal/alicloud-ai-multimodal-qwen-omni/scripts/prepare_omni_request.py \
  --output output/alicloud-ai-multimodal-qwen-omni/request.json

References
references/sources.md
Weekly Installs
93
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass