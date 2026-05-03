---
rating: ⭐⭐
title: aliyun-qvq
url: https://skills.sh/cinience/alicloud-skills/aliyun-qvq
---

# aliyun-qvq

skills/cinience/alicloud-skills/aliyun-qvq
aliyun-qvq
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill aliyun-qvq
SKILL.md

Category: provider

Model Studio QVQ Visual Reasoning
Validation
mkdir -p output/aliyun-qvq
python -m py_compile skills/ai/multimodal/aliyun-qvq/scripts/prepare_qvq_request.py && echo "py_compile_ok" > output/aliyun-qvq/validate.txt


Pass criteria: command exits 0 and output/aliyun-qvq/validate.txt is generated.

Critical model names

Use one of these exact model strings:

qvq-plus
qvq-max
Typical use
Mathematical reasoning from screenshots
Diagram and chart reasoning
Visually grounded multi-step problem solving
Quick start
python skills/ai/multimodal/aliyun-qvq/scripts/prepare_qvq_request.py \
  --output output/aliyun-qvq/request.json

Notes
Use skills/ai/multimodal/aliyun-qwen-vl/ for standard image understanding.
Use QVQ when the task explicitly needs stronger reasoning over visual evidence.
References
references/sources.md
Weekly Installs
34
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