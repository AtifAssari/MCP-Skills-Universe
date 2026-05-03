---
rating: ⭐⭐
title: nanobanana
url: https://skills.sh/gargantuax/openskills/nanobanana
---

# nanobanana

skills/gargantuax/openskills/nanobanana
nanobanana
Installation
$ npx skills add https://github.com/gargantuax/openskills --skill nanobanana
SKILL.md
Nano Banana

A single Python entrypoint for Gemini-native Nano Banana image generation and editing, with model aliases, strict option validation, batch runs, and custom endpoint support.

Workflow
Open references/config.md to choose environment variables and override order.
Open references/models-and-api.md to pick the right Nano Banana tier and check model-specific constraints.
Prefer gemini-3.1-flash-image-preview (nanobanana-2) unless you need either the fastest low-cost default (nanobanana) or the highest-fidelity reasoning model (nanobanana-pro).
Run scripts/nanobanana.py generate for one request or scripts/nanobanana.py batch for repeated variants.
Add --dry-run first when the main risk is the payload shape, endpoint, or model-specific option support.
Pass --base-url or GEMINI_BASE_URL when you need a custom Gemini-compatible gateway.
Add --save-response <path> on generate when you need the raw JSON body for debugging.
Commands

Single text-to-image request:

python .\skills\nanobanana\scripts\nanobanana.py generate `
  --prompt "A retro-futurist product hero illustration for a developer tool" `
  --output .\out\hero.png `
  --model nanobanana-2 `
  --ratio 16:9 `
  --size 2K


Edit an existing image with two local references:

python .\skills\nanobanana\scripts\nanobanana.py generate `
  --prompt "Turn these references into a clean launch poster with legible title text" `
  --input-image .\refs\subject.png `
  --input-image .\refs\background.png `
  --output .\out\poster.png `
  --model nanobanana-pro `
  --ratio 4:5 `
  --size 2K


Use a custom Gemini-compatible gateway:

python .\skills\nanobanana\scripts\nanobanana.py generate `
  --prompt "A bold mascot sticker pack" `
  --output .\out\stickers.png `
  --base-url http://your-gateway.example.com/v1beta `
  --auth-mode bearer


Batch-generate five variants:

python .\skills\nanobanana\scripts\nanobanana.py batch `
  --prompt "Minimal app icon for a PDF workflow product" `
  --count 5 `
  --dir .\out\icons `
  --prefix icon `
  --model nanobanana `
  --ratio 1:1


Inspect the final request without sending it:

python .\skills\nanobanana\scripts\nanobanana.py generate `
  --prompt "An editorial illustration of AI agents at work" `
  --model nanobanana-2 `
  --output .\out\agents.png `
  --dry-run

Rules
--model accepts the aliases nanobanana, nanobanana-2, and nanobanana-pro, or an exact Gemini model ID.
nanobanana resolves to gemini-2.5-flash-image, nanobanana-2 resolves to gemini-3.1-flash-image-preview, and nanobanana-pro resolves to gemini-3-pro-image-preview.
image_size is only valid on Gemini 3 image models; nanobanana rejects --size.
512 resolution is only valid on nanobanana-2.
Process environment variables override .env; CLI flags override both.
Never print secrets.
generate accepts repeated --input-image paths for image editing or multi-reference generation.
--base-url should point to the Gemini API root such as https://generativelanguage.googleapis.com/v1beta, not directly to /models/....
--auth-mode auto uses x-goog-api-key for the official Google endpoint and sends both Authorization: Bearer and x-goog-api-key for custom endpoints to maximize gateway compatibility.
Resources
Script: scripts/nanobanana.py
Config reference: references/config.md
Models and API reference: references/models-and-api.md
Weekly Installs
303
Repository
gargantuax/openskills
GitHub Stars
1
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass