---
title: alicloud-ai-multimodal-qvq
url: https://skills.sh/cinience/alicloud-skills/alicloud-ai-multimodal-qvq
---

# alicloud-ai-multimodal-qvq

skills/cinience/alicloud-skills/alicloud-ai-multimodal-qvq
alicloud-ai-multimodal-qvq
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-ai-multimodal-qvq
SKILL.md

Category: provider

Model Studio QVQ Visual Reasoning
Validation
mkdir -p output/alicloud-ai-multimodal-qvq
python -m py_compile skills/ai/multimodal/alicloud-ai-multimodal-qvq/scripts/prepare_qvq_request.py && echo "py_compile_ok" > output/alicloud-ai-multimodal-qvq/validate.txt


Pass criteria: command exits 0 and output/alicloud-ai-multimodal-qwen-vqv/validate.txt is generated.

Critical model names

Use one of these exact model strings:

qvq-plus
qvq-max
Typical use
Mathematical reasoning from screenshots
Diagram and chart reasoning
Visually grounded multi-step problem solving
Quick start
python skills/ai/multimodal/alicloud-ai-multimodal-qvq/scripts/prepare_qvq_request.py \
  --output output/alicloud-ai-multimodal-qvq/request.json

Notes
Use skills/ai/multimodal/alicloud-ai-multimodal-qwen-vl/ for standard image understanding.
Use QVQ when the task explicitly needs stronger reasoning over visual evidence.
References
references/sources.md
Weekly Installs
92
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