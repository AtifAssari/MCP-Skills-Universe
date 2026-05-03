---
title: comfyui-api
url: https://skills.sh/mckruz/comfyui-expert/comfyui-api
---

# comfyui-api

skills/mckruz/comfyui-expert/comfyui-api
comfyui-api
Installation
$ npx skills add https://github.com/mckruz/comfyui-expert --skill comfyui-api
SKILL.md
ComfyUI API Skill

Connect to ComfyUI's REST API to execute workflows, monitor progress, and retrieve outputs.

Configuration
Default URL: http://127.0.0.1:8188
Custom URL: Set in project manifest or pass as parameter
Timeout: 30s for API calls, no timeout for generation polling
Two Modes
Online Mode (ComfyUI Running)

Full API access. Preferred mode for interactive work.

Test connection: GET /system_stats
Discover capabilities: Use comfyui-inventory skill
Queue workflow: POST /prompt
Poll for results: GET /history/{prompt_id} every 5 seconds
Retrieve outputs: GET /view?filename=...
Offline Mode (No Server)

Export workflow JSON for manual loading in ComfyUI.

Generate workflow JSON following ComfyUI's format
Save to projects/{project}/workflows/{name}.json
Instruct user to drag-drop into ComfyUI
API Operations
Check Server Status
curl http://127.0.0.1:8188/system_stats


Response fields:

system.os: Operating system
system.comfyui_version: Version string
devices[0].name: GPU name
devices[0].vram_total: Total VRAM bytes
devices[0].vram_free: Free VRAM bytes
Queue a Workflow
curl -X POST http://127.0.0.1:8188/prompt \
  -H "Content-Type: application/json" \
  -d '{"prompt": WORKFLOW_JSON, "client_id": "video-agent"}'


WORKFLOW_JSON format:

{
  "1": {
    "class_type": "LoadCheckpoint",
    "inputs": {
      "ckpt_name": "flux1-dev.safetensors"
    }
  },
  "2": {
    "class_type": "CLIPTextEncode",
    "inputs": {
      "text": "photorealistic portrait...",
      "clip": ["1", 1]
    }
  }
}


Each node is keyed by a string ID. Inputs reference other nodes as ["{node_id}", {output_index}].

Response:

{"prompt_id": "abc-123-def", "number": 1}

Poll for Completion
curl http://127.0.0.1:8188/history/abc-123-def


Incomplete: Returns {} (empty object) Complete: Returns execution data with outputs:

{
  "abc-123-def": {
    "outputs": {
      "9": {
        "images": [{"filename": "ComfyUI_00001.png", "subfolder": "", "type": "output"}]
      }
    },
    "status": {"completed": true}
  }
}

Retrieve Output Image
curl "http://127.0.0.1:8188/view?filename=ComfyUI_00001.png&subfolder=&type=output" -o output.png

Upload Reference Image
curl -X POST http://127.0.0.1:8188/upload/image \
  -F "image=@reference.png" \
  -F "subfolder=input" \
  -F "type=input"

Cancel Current Generation
curl -X POST http://127.0.0.1:8188/interrupt

Free VRAM
curl -X POST http://127.0.0.1:8188/free \
  -H "Content-Type: application/json" \
  -d '{"unload_models": true}'

Polling Strategy

ComfyUI doesn't support WebSocket in CLI context. Use REST polling:

Queue workflow via POST /prompt → get prompt_id
Poll GET /history/{prompt_id} every 5 seconds
On empty response: generation in progress, continue polling
On populated response: check status.completed
If completed: true, extract outputs
If error in status, route to comfyui-troubleshooter

Timeout: Warn user after 10 minutes of polling. Video generation (Wan 14B) can take 15-30 minutes.

Workflow Validation

Before queuing any workflow:

Read state/inventory.json (via comfyui-inventory)
For each node in workflow: verify class_type exists in installed nodes
For each model reference: verify file exists in installed models
Flag missing items with:
Node: suggest ComfyUI-Manager install command
Model: provide download link from references/models.md
Version mismatch: suggest update
Error Handling
Error	Cause	Action
Connection refused	ComfyUI not running	Switch to offline mode, save JSON
400 Bad Request	Invalid workflow JSON	Validate node connections
500 Internal Error	ComfyUI crash	Suggest restart, check logs
Timeout (no response)	Server overloaded	Wait and retry once
Reference

Full API documentation: foundation/api-quick-ref.md

Weekly Installs
669
Repository
mckruz/comfyui-expert
GitHub Stars
50
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass